#!/usr/bin/env python3
"""ambil_verdict.py — mengambil hasil audit/review dari GitHub TANPA pemilik menyalin apa pun.

MASALAH YANG DITUTUP
--------------------
Sebelum alat ini ada, alurnya: auditor menulis verdict → **pemilik** yang memberi tahu sesi yang
sedang berjalan → sesi membacanya. Pemilik jadi kurir. Permintaan pemilik (T30, 17 Sep 2026):

  *"aku mau itu dibuat otomatis terkirim ke github, sehingga ketika review/audit udh selesai,
  aku ga perlu laporin hasilnya ke agent sesi yang lagi jalan … aku cukup bilang bahwa
  review/audit udh selesai, dan dia otomatis tau semua hasilnya."*

Alat ini menutup sisi **pengambilannya**. Sisi pengirimannya ada di prompt yang dibangkitkan
`tools/audit_prompt.py` bagian 10 (kirim ke GitHub Issue dengan judul + label berpola tetap).

SATU ALAT, DUA KANAL — sengaja tidak dibuat dua alat:
  * audit ISI (non-PR) → **GitHub Issue**, judul `AUDIT <objek> @<sha7>`, label `audit-independen`
  * review PR          → **komentar PR** (kanal lama yang sudah terbukti; verdict ditempel sebagai
                         satu komentar, preseden log sesi 16 Sep 2026)

ATURAN PAKAI
------------
* **Read-only.** Alat ini hanya membaca. Ia tidak pernah menulis Issue, komentar, atau berkas repo.
* **Tidak menebak.** Kalau tidak ditemukan tepat satu kandidat "terbaru" yang tidak ambigu, alat ini
  **berhenti dan menyuruh memilih eksplisit** — pola fail-closed yang diwarisi dari `review_prompt.py`.
* Label `audit-independen` mungkin **belum ada** di repo. `gh issue create --label` gagal kalau
  labelnya belum dibuat. Sekali saja: `gh label create audit-independen --description "..."`.
  Alat ini tetap berfungsi tanpa label karena pencocokan memakai **label ATAU pola judul**.

Pemakaian:
  python3 tools/ambil_verdict.py --terbaru            # verdict audit-isi terbaru
  python3 tools/ambil_verdict.py --terbaru --objek _meta
  python3 tools/ambil_verdict.py --issue 42           # Issue tertentu
  python3 tools/ambil_verdict.py --pr 71              # kanal review PR
  python3 tools/ambil_verdict.py --daftar             # daftar kandidat tanpa mencetak isi
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LABEL_ISSUE = "audit-independen"
# Judul yang dibangkitkan tools/audit_prompt.py: "AUDIT <objek> @<sha7>"
JUDUL_RE = re.compile(r"^AUDIT\s+(?P<objek>\S+)\s+@(?P<sha>[0-9a-f]{7,40})\s*$", re.I)

VERDICT_RE = re.compile(
    r"\b(BERSIH|ADA\s+TEMUAN|TIDAK\s+BISA\s+DISIMPULKAN|APPROVE|REQUEST_CHANGES|COMMENT)\b", re.I
)


class ToolError(Exception):
    """Kegagalan yang harus terlihat sebagai exit non-zero + pesan spesifik."""


def _run(cmd: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def gh_tersedia() -> None:
    code, out, err = _run(["gh", "--version"])
    if code != 0:
        raise ToolError(
            f"`gh` tidak tersedia/tidak bisa dijalankan (keluar {code}): {(err or out).strip()[:160]}\n"
            "  Alat ini membaca GitHub lewat `gh`. Tanpa `gh`, hasil audit tidak bisa diambil otomatis —\n"
            "  buka Issue-nya di browser dan salin isinya manual."
        )
    code, out, err = _run(["gh", "api", "rate_limit"])
    if code != 0:
        raise ToolError(
            f"`gh` ada tetapi tidak terautentikasi / API tidak terjangkau (keluar {code}): "
            f"{(err or out).strip()[:200]}\n"
            "  Periksa autentikasi GitHub. Alat ini TIDAK menebak isi verdict dari sumber lain."
        )


def ambil_issue(nomor: int) -> dict:
    code, out, err = _run([
        "gh", "issue", "view", str(nomor), "--json",
        "number,title,state,body,labels,createdAt,author,comments",
    ])
    if code != 0:
        raise ToolError(f"gagal mengambil Issue #{nomor} (keluar {code}): {(err or out).strip()[:240]}")
    try:
        return json.loads(out or "{}")
    except json.JSONDecodeError as e:
        raise ToolError(f"jawaban `gh issue view` bukan JSON sah: {e}") from e


def daftar_kandidat(objek: str | None) -> list[dict]:
    """Issue yang cocok dengan kanal audit-isi: berlabel ATAU berpola judul AUDIT <objek> @<sha>."""
    code, out, err = _run([
        "gh", "issue", "list", "--state", "all", "--limit", "200",
        "--json", "number,title,state,createdAt,labels",
    ])
    if code != 0:
        raise ToolError(f"gagal mendaftar Issue (keluar {code}): {(err or out).strip()[:240]}")
    try:
        rows = json.loads(out or "[]")
    except json.JSONDecodeError as e:
        raise ToolError(f"jawaban `gh issue list` bukan JSON sah: {e}") from e

    cocok = []
    for r in rows:
        judul = (r.get("title") or "").strip()
        labels = {l.get("name", "") for l in (r.get("labels") or [])}
        via_label = LABEL_ISSUE in labels
        m = JUDUL_RE.match(judul)
        via_judul = bool(m)
        if not (via_label or via_judul):
            continue
        if objek:
            obj_target = objek.strip().strip("/").replace("\\", "/")
            obj_ditemukan = (m.group("objek").strip("/") if m else "")
            if obj_ditemukan != obj_target and obj_target not in judul:
                continue
        cocok.append({
            "number": r.get("number"),
            "title": judul,
            "state": r.get("state"),
            "createdAt": r.get("createdAt"),
            "objek": (m.group("objek") if m else "?"),
            "sha": (m.group("sha") if m else "?"),
            "via": ("label+judul" if via_label and via_judul else ("label" if via_label else "judul")),
        })
    cocok.sort(key=lambda x: (x.get("createdAt") or ""), reverse=True)
    return cocok


def ambil_pr(nomor: int) -> dict:
    code, out, err = _run([
        "gh", "pr", "view", str(nomor), "--json",
        "number,title,state,body,headRefOid,baseRefName,comments,reviews",
    ])
    if code != 0:
        raise ToolError(f"gagal mengambil PR #{nomor} (keluar {code}): {(err or out).strip()[:240]}")
    try:
        return json.loads(out or "{}")
    except json.JSONDecodeError as e:
        raise ToolError(f"jawaban `gh pr view` bukan JSON sah: {e}") from e


def simpulkan(teks: str) -> str:
    """Verdict satu baris kalau ada; kalau tidak ada, katakan TIDAK DITEMUKAN (jangan menebak)."""
    if not teks:
        return "TIDAK DITEMUKAN (badan/komentar kosong)"
    m = VERDICT_RE.search(teks)
    return m.group(1).upper() if m else "TIDAK DITEMUKAN (tidak ada kata verdict yang dikenali)"


def cetak_issue(nomor: int) -> int:
    d = ambil_issue(nomor)
    body = d.get("body") or ""
    comments = d.get("comments") or []
    labels = ", ".join(sorted(l.get("name", "") for l in (d.get("labels") or []))) or "(tanpa label)"
    print("=" * 78)
    print(f"ISSUE #{d.get('number')} — {d.get('title')}")
    print(f"state: {d.get('state')} · dibuat: {d.get('createdAt')} · label: {labels}")
    m = JUDUL_RE.match((d.get("title") or "").strip())
    if m:
        print(f"objek ter-pin: `{m.group('objek')}` · sha: `{m.group('sha')}`")
    else:
        print("objek ter-pin: TIDAK TERBACA dari judul (judul tidak mengikuti pola `AUDIT <objek> @<sha>`)")
    print("=" * 78)
    print(f"\nVERDICT (terbaca otomatis): {simpulkan(body)}")
    print("\n----- BADAN ISSUE -----")
    print(body.strip() or "(kosong)")
    if comments:
        # append-only: putaran berikutnya muncul sebagai komentar, jangan dibuang
        print(f"\n----- {len(comments)} KOMENTAR (putaran lanjutan; append-only) -----")
        for i, c in enumerate(comments, 1):
            cb = c.get("body") or ""
            print(f"\n### komentar {i} — {c.get('author', {}).get('login', '?')} @ {c.get('createdAt', '?')}")
            print(f"VERDICT (terbaca otomatis): {simpulkan(cb)}")
            print(cb.strip())
    print("\n" + "=" * 78)
    print("CATATAN UNTUK SESI YANG MEMBACA INI:")
    print("- Temuan di bagian 'DI LUAR CAKUPAN' **wajib ikut dilaporkan** ke pemilik, jangan disaring")
    print("  (ATURAN CAKUPAN di QUALITY_ASSURANCE_AND_EVOLUTION.md: cakupan membatasi pencarian dan klaim,")
    print("   tidak pernah membatasi laporan).")
    print("- Bagian 'kandidat yang DICABUT' adalah bagian dari kejujuran laporan, bukan sampah — jangan dibuang.")
    print("- **Membaca verdict ≠ menyetujuinya.** Bertindak atas temuan butuh mandat pemilik;")
    print("  menemukan ≠ memperbaiki (QA Prinsip 2).")
    return 0


def cetak_pr(nomor: int) -> int:
    d = ambil_pr(nomor)
    comments = d.get("comments") or []
    reviews = d.get("reviews") or []
    print("=" * 78)
    print(f"PR #{d.get('number')} — {d.get('title')}")
    print(f"state: {d.get('state')} · head: {(d.get('headRefOid') or '')[:12]} · base: {d.get('baseRefName')}")
    print("=" * 78)
    if reviews:
        print(f"\n----- {len(reviews)} REVIEW -----")
        for i, r in enumerate(reviews, 1):
            rb = r.get("body") or ""
            print(f"\n### review {i} — {r.get('author', {}).get('login', '?')} · state: {r.get('state')}")
            if rb.strip():
                print(f"VERDICT (terbaca otomatis): {simpulkan(rb)}")
                print(rb.strip())
    if comments:
        print(f"\n----- {len(comments)} KOMENTAR -----")
        for i, c in enumerate(comments, 1):
            cb = c.get("body") or ""
            print(f"\n### komentar {i} — {c.get('author', {}).get('login', '?')} @ {c.get('createdAt', '?')}")
            print(f"VERDICT (terbaca otomatis): {simpulkan(cb)}")
            print(cb.strip())
    if not reviews and not comments:
        print("\nTIDAK ADA review maupun komentar pada PR ini.")
        print("Artinya verdict **belum diserahkan**, bukan verdict-nya bersih. Jangan disimpulkan sendiri.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--terbaru", action="store_true", help="ambil hasil audit-isi terbaru dari kanal Issue")
    g.add_argument("--issue", type=int, metavar="N", help="ambil Issue nomor N")
    g.add_argument("--pr", type=int, metavar="N", help="ambil hasil review PR nomor N (kanal lama)")
    g.add_argument("--daftar", action="store_true", help="daftar kandidat audit-isi tanpa mencetak isi")
    ap.add_argument("--objek", help="saring berdasarkan objek, mis. `_meta` atau `sistem/sistem-klinik`")
    a = ap.parse_args()

    try:
        gh_tersedia()
        if a.pr:
            return cetak_pr(a.pr)
        if a.issue:
            return cetak_issue(a.issue)

        kandidat = daftar_kandidat(a.objek)
        if a.daftar:
            if not kandidat:
                print("Tidak ada Issue yang cocok dengan kanal audit-isi"
                      + (f" untuk objek `{a.objek}`" if a.objek else "") + ".")
                print(f"Kanal yang dikenali: label `{LABEL_ISSUE}` ATAU judul berpola `AUDIT <objek> @<sha>`.")
                return 0
            print(f"{len(kandidat)} kandidat audit-isi (terbaru di atas):")
            for k in kandidat:
                print(f"  #{k['number']:<4} {k['createdAt'][:19]}  {k['state']:<6} "
                      f"objek={k['objek']} sha={k['sha']} via={k['via']}")
                print(f"         {k['title']}")
            return 0

        # --terbaru
        if not kandidat:
            raise ToolError(
                "tidak ditemukan hasil audit di kanal Issue"
                + (f" untuk objek `{a.objek}`" if a.objek else "") + ".\n"
                f"  Kanal yang dikenali: label `{LABEL_ISSUE}` ATAU judul berpola `AUDIT <objek> @<sha>`.\n"
                "  Kemungkinan: (a) audit memang belum diserahkan; (b) auditor menulisnya di tempat lain;\n"
                f"  (c) labelnya belum dibuat — sekali saja: gh label create {LABEL_ISSUE}.\n"
                "  Alat ini TIDAK menebak dan TIDAK menyimpulkan 'bersih' dari ketiadaan hasil.\n"
                "  Periksa manual: gh issue list --state all --limit 30"
            )
        if len(kandidat) > 1 and kandidat[0]["createdAt"] == kandidat[1]["createdAt"]:
            nums = ", ".join(f"#{k['number']}" for k in kandidat[:5])
            raise ToolError(
                f"ambigu: ada beberapa hasil audit dengan waktu pembuatan identik ({nums}).\n"
                "  'Terbaru' TIDAK ditebak. Pilih eksplisit: python3 tools/ambil_verdict.py --issue <N>\n"
                "  Lihat daftarnya: python3 tools/ambil_verdict.py --daftar"
            )
        pilih = kandidat[0]
        if len(kandidat) > 1:
            print(f"[diambil yang terbaru: #{pilih['number']} · {pilih['createdAt']} · "
                  f"{len(kandidat) - 1} kandidat lain lebih lama — lihat --daftar]\n")
        return cetak_issue(pilih["number"])
    except ToolError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
