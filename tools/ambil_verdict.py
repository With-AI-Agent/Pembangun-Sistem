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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checkpoint_core import strip_code_fences  # noqa: E402  (status tidak boleh diambil dari contoh di dalam pagar kode)

ROOT = Path(__file__).resolve().parents[1]

LABEL_ISSUE = "audit-independen"

# KANAL BERKAS (git-based) — ditambahkan 17 Sep 2026 sesudah UJI NYATA membuktikan kanal Issue
# DITOLAK di lingkungan produksi ini: `gh issue create` -> HTTP 403 "Resource not accessible by
# integration (createIssue)", sementara `gh label create` BERHASIL dan `git push` BERHASIL.
# Mekanisme tidak boleh bergantung pada kanal yang diblokir, jadi hasil audit juga sah diserahkan
# sebagai berkas yang di-commit. Folder ini SENGAJA di bawah _meta/_internal/ karena folder itu
# TIDAK ikut ke ekstrak template (diperiksa: build_template.py), sehingga artefak per-run tidak
# bocor ke sistem anak.
DIR_AUDIT = ROOT / "_meta" / "_internal" / "audit"
JUDUL_BERKAS_RE = re.compile(r"^#\s*AUDIT\s+(?P<objek>\S+)\s+@(?P<sha>[0-9a-f]{7,40})\s*$",
                             re.I | re.M)
# Judul yang dibangkitkan tools/audit_prompt.py: "AUDIT <objek> @<sha7>"
JUDUL_RE = re.compile(r"^AUDIT\s+(?P<objek>\S+)\s+@(?P<sha>[0-9a-f]{7,40})\s*$", re.I)

# ---------------------------------------------------------------------------
# Kosakata verdict. CACAT D-1 (ditemukan penulis atas PR #74, 17 Sep 2026):
# sebelumnya HANYA kosakata audit-isi yang ada (BERSIH / ADA TEMUAN / ...),
# padahal protokol review memakai HIJAU / MERAH — sehingga verdict review
# "MERAH" TIDAK PERNAH bisa terbaca, dan `.search()` yang mengambil kecocokan
# pertama DI MANA SAJA membuat kata "bersih" di dalam kalimat larangan
# ("...agar diff menjadi bersih") terbaca sebagai verdict atas laporan MERAH.
# Itu fail-open pada instrumen keselamatan: "Jangan merge" dilaporkan "BERSIH".
#   review PR    : HIJAU / MERAH        (PROTOKOL_REVIEW_INDEPENDEN.md, Mekanika putusan)
#   audit isi    : BERSIH / ADA TEMUAN / TIDAK BISA DISIMPULKAN
#   state GitHub : APPROVE / REQUEST_CHANGES / COMMENT
VERDICT_RE = re.compile(
    r"\b(MERAH|HIJAU|BERSIH|ADA\s+TEMUAN|TIDAK\s+BISA\s+DISIMPULKAN|APPROVE|REQUEST_CHANGES|COMMENT)\b",
    re.I,
)
# Fail-closed — keputusan pemilik 17 Sep 2026: "Selagi ada yang merah, maka harus diperbaiki."
# Yang dihitung hijau HANYA kata yang memang hijau; apa pun selain itu MENAHAN merge.
HIJAU_SET = {"HIJAU", "BERSIH", "APPROVE"}
# Baris yang layak jadi verdict: (a) deklarasi berpemarkah di AWAL baris, atau (b) judul Markdown.
# Kata verdict di dalam PROSA tidak dihitung — itu penyebab D-1.
PENANDA_RE = re.compile(r"^\s*(?:[-*>]\s*)?\*{0,2}(?:VERDICT|PUTUSAN|HASIL\s+REVIEW)\*{0,2}\s*[:=]", re.I)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
# Verdict dikeluarkan oleh pihak yang BUKAN penulis (prinsip protokol: pencatat != subjek).
# Baris yang menyebut dirinya dari penulis bukan verdict.
PENULIS_RE = re.compile(r"\b(penulis|koreksi terbuka|tanggapan penulis)\b", re.I)


def simpulkan(teks: str) -> str:
    """Verdict satu baris kalau ada; kalau tidak ada, katakan TIDAK DITEMUKAN (jangan menebak).

    Tiga pagar yang ditambahkan setelah cacat D-1:
      1. isi pagar kode dikosongkan dulu (memakai `strip_code_fences` dari checkpoint_core) —
         status tidak boleh diambil dari contoh yang ditempel di dalam fence;
      2. hanya baris berpemarkah di awal baris atau baris judul yang diperiksa —
         kata verdict di prosa diabaikan;
      3. baris yang menyebut dirinya dari penulis diabaikan — verdict bukan dari penulis.
    """
    if not teks:
        return "TIDAK DITEMUKAN (badan/komentar kosong)"
    for baris in strip_code_fences(teks).splitlines():
        if PENULIS_RE.search(baris):
            continue
        if not (PENANDA_RE.match(baris) or HEADING_RE.match(baris)):
            continue
        m = VERDICT_RE.search(baris)
        if m:
            return re.sub(r"\s+", " ", m.group(1).upper())
    return "TIDAK DITEMUKAN (tidak ada baris verdict; kata verdict di dalam prosa TIDAK dihitung)"


def gabungkan(verdicts: list[str]) -> str:
    """Agregasi FAIL-CLOSED atas banyak hakim (keputusan pemilik 17 Sep 2026).

    Satu saja verdict yang bukan hijau -> gabungan MENAHAN merge. Tidak ada mayoritas,
    tidak ada rata-rata: yang dicari reviewer independen adalah alasan untuk menolak,
    bukan suara terbanyak. Verdict TIDAK DITEMUKAN juga menahan, karena "tidak terbaca"
    bukan berarti "bersih".
    """
    sah = [v for v in verdicts if v and not v.startswith("TIDAK DITEMUKAN")]
    if not verdicts:
        return "BELUM ADA VERDICT — jangan merge, jangan simpulkan bersih"
    merah = [v for v in sah if v not in HIJAU_SET]
    tak_terbaca = [v for v in verdicts if v.startswith("TIDAK DITEMUKAN")]
    if merah:
        return f"MERAH — JANGAN MERGE ({len(merah)} dari {len(verdicts)} verdict bukan hijau: {', '.join(sorted(set(merah)))})"
    if tak_terbaca:
        return (f"MENAHAN — {len(tak_terbaca)} verdict TIDAK TERBACA dari {len(verdicts)}; "
                "tidak terbaca BUKAN bersih")
    return f"HIJAU — semua {len(sah)} verdict hijau ({', '.join(sorted(set(sah)))})"


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
        # BUKAN kegagalan fatal: kanal Issue boleh tidak tersedia (token tanpa izin issues:write,
        # gh tidak terpasang, jaringan diblokir). Kanal berkas tetap bisa menjawab. Yang dilarang
        # adalah menyimpulkan "tidak ada hasil" dari ketidaktersediaan kanal.
        return [], f"kanal Issue tidak tersedia (keluar {code}): {(err or out).strip()[:180]}"
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
    return cocok, None


def daftar_berkas(objek: str | None) -> tuple[list[dict], str | None]:
    """Hasil audit yang diserahkan sebagai berkas ter-commit di DIR_AUDIT.

    Metadata diambil dari baris judul `# AUDIT <objek> @<sha>` DI DALAM berkas — bukan dari nama
    berkas — supaya satu sumber kebenaran dan pola judulnya sama dengan kanal Issue.
    """
    if not DIR_AUDIT.is_dir():
        return [], None
    cocok = []
    for f in sorted(DIR_AUDIT.glob("*.md")):
        try:
            teks = f.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            return [], f"gagal membaca {f.name}: {e}"
        m = JUDUL_BERKAS_RE.search(teks)
        if not m:
            continue  # bukan hasil audit kanal ini; jangan ditebak dari nama berkas
        if objek:
            obj_target = objek.strip().strip("/").replace("\\", "/")
            if m.group("objek").strip("/") != obj_target and obj_target not in teks[:400]:
                continue
        cocok.append({
            "number": None,
            "title": m.group(0).lstrip("# ").strip(),
            "state": "berkas",
            "createdAt": __import__("datetime").datetime.fromtimestamp(
                f.stat().st_mtime).astimezone().isoformat(timespec="seconds"),
            "objek": m.group("objek"),
            "sha": m.group("sha"),
            "via": "berkas",
            "path": str(f.relative_to(ROOT)),
        })
    cocok.sort(key=lambda x: x["createdAt"], reverse=True)
    return cocok, None


def cetak_berkas(path: Path) -> int:
    if not path.is_file():
        raise ToolError(f"berkas hasil audit tidak ada: {path}")
    teks = path.read_text(encoding="utf-8", errors="replace")
    m = JUDUL_BERKAS_RE.search(teks)
    print("=" * 78)
    print(f"HASIL AUDIT ISI (kanal BERKAS ter-commit) — {path.relative_to(ROOT)}")
    print(f"Judul : {m.group(0).lstrip('# ').strip() if m else '(tidak berpola AUDIT <objek> @<sha>)'}")
    print(f"Panjang: {len(teks.splitlines())} baris")
    print("=" * 78)
    print(teks)
    print("=" * 78)
    print(f"VERDICT TERBACA OTOMATIS: {simpulkan(teks)}")
    print("Membaca verdict BUKAN menyetujuinya: bertindak atas temuan tetap butuh keputusan pemilik.")
    return 0


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
            v = simpulkan(cb)
            kumpul.append(v)
            print(f"VERDICT (terbaca otomatis): {v}")
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
    kumpul: list[str] = []
    if reviews:
        print(f"\n----- {len(reviews)} REVIEW -----")
        for i, r in enumerate(reviews, 1):
            rb = r.get("body") or ""
            print(f"\n### review {i} — {r.get('author', {}).get('login', '?')} · state: {r.get('state')}")
            if rb.strip():
                v = simpulkan(rb)
                kumpul.append(v)
                print(f"VERDICT (terbaca otomatis): {v}")
                print(rb.strip())
    if comments:
        print(f"\n----- {len(comments)} KOMENTAR -----")
        for i, c in enumerate(comments, 1):
            cb = c.get("body") or ""
            print(f"\n### komentar {i} — {c.get('author', {}).get('login', '?')} @ {c.get('createdAt', '?')}")
            v = simpulkan(cb)
            kumpul.append(v)
            print(f"VERDICT (terbaca otomatis): {v}")
            print(cb.strip())
    if not reviews and not comments:
        print("\nTIDAK ADA review maupun komentar pada PR ini.")
        print("Artinya verdict **belum diserahkan**, bukan verdict-nya bersih. Jangan disimpulkan sendiri.")
        return 0
    print("\n" + "=" * 78)
    print("AGREGASI FAIL-CLOSED (aturan pemilik 17 Sep 2026: \"Selagi ada yang merah, maka harus diperbaiki\")")
    print("=" * 78)
    for i, v in enumerate(kumpul, 1):
        print(f"  hakim {i}: {v}")
    print(f"\n  >> HASIL GABUNGAN: {gabungkan(kumpul)}")
    print("\n  Membaca verdict BUKAN menyetujuinya. Bertindak atas temuan tetap butuh keputusan pemilik,")
    print("  dan PR yang mengubah alat pengadil tidak boleh di-merge oleh reviewer (konflik kepentingan).")
    return 0


# ---------------------------------------------------------------------------
# Uji-mutasi untuk perbaikan D-1 + agregasi fail-closed. Norma repo: mekanisme
# baru wajib diuji dengan MUTASI, bukan hanya dijalankan sekali lalu terlihat hijau.
# D-1 sendiri lahir dari alat yang TIDAK punya uji semacam ini.
KASUS = [
    # (nama, teks, harapan)
    ("verdict review MERAH di judul",
     "## Review independen — putaran 1 — MERAH (parsial, bukan persetujuan)\n\n**Jangan merge.**\n",
     "MERAH"),
    ("verdict review HIJAU di judul",
     "## Review independen — putaran 2 — HIJAU\n\nBoleh merge atas izin pemilik.\n",
     "HIJAU"),
    ("deklarasi eksplisit VERDICT:",
     "Laporan.\n\n**VERDICT:** MERAH\n\nRincian.\n",
     "MERAH"),
    ("D-1 REGRESI: kata 'bersih' di prosa tidak boleh mengalahkan MERAH di judul",
     "## Review — MERAH\n\nJangan menghapus bukti historis agar diff menjadi bersih.\n",
     "MERAH"),
    ("D-1 REGRESI: prosa 'bersih' tanpa baris verdict = TIDAK DITEMUKAN",
     "Laporan temuan.\n\nJangan menyunting bukti agar diff menjadi bersih.\n",
     "TIDAK DITEMUKAN"),
    ("baris penulis yang menyebut MERAH bukan verdict",
     "## Tanggapan penulis atas verdict putaran 1 (MERAH)\n\nIsi.\n",
     "TIDAK DITEMUKAN"),
    ("isi pagar kode tidak dihitung walau berbentuk baris verdict",
     "Laporan.\n\n```text\n## Review — HIJAU\n```\n\nSelesai.\n",
     "TIDAK DITEMUKAN"),
    ("audit isi: ADA TEMUAN tetap terbaca (kanal kedua tidak rusak)",
     "# AUDIT objek @abc1234\n\n**VERDICT:** ADA TEMUAN\n",
     "ADA TEMUAN"),
]

KASUS_GABUNG = [
    ("fail-closed: 1 MERAH + 2 HIJAU = MERAH (bukan mayoritas)",
     ["MERAH", "HIJAU", "HIJAU"], "MERAH"),
    ("semua hijau = HIJAU", ["HIJAU", "HIJAU"], "HIJAU"),
    ("belum ada verdict = menahan", [], "BELUM ADA"),
    ("tidak terbaca BUKAN bersih", ["HIJAU", "TIDAK DITEMUKAN (x)"], "MENAHAN"),
    ("audit: ADA TEMUAN menahan merge", ["BERSIH", "ADA TEMUAN"], "MERAH"),
]


def uji() -> int:
    global VERDICT_RE, PENULIS_RE
    gagal = 0
    print("UJI-MUTASI pembaca verdict (D-1) + agregasi fail-closed")
    for nama, teks, harap in KASUS:
        got = simpulkan(teks)
        ok = got.startswith(harap) if harap == "TIDAK DITEMUKAN" else got == harap
        print(f"  [{'OK ' if ok else 'GAGAL'}] {nama}")
        if not ok:
            print(f"        harapan: {harap} · dapat: {got}")
            gagal += 1
    for nama, vs, harap in KASUS_GABUNG:
        got = gabungkan(vs)
        ok = got.startswith(harap)
        print(f"  [{'OK ' if ok else 'GAGAL'}] {nama}")
        if not ok:
            print(f"        harapan awalan: {harap} · dapat: {got}")
            gagal += 1

    # MUTASI 1 — kembalikan kosakata lama (tanpa MERAH/HIJAU). Uji verdict review harus
    # GAGAL; kalau tidak, uji ini tautologi (persis cacat RP5b yang pernah ditemukan di
    # review PR #55: memeriksa teks ada, bukan perilakunya).
    asli = VERDICT_RE
    VERDICT_RE = re.compile(
        r"\b(BERSIH|ADA\s+TEMUAN|TIDAK\s+BISA\s+DISIMPULKAN|APPROVE|REQUEST_CHANGES|COMMENT)\b", re.I)
    mutasi = sum(1 for _, teks, harap in KASUS
                 if harap in ("MERAH", "HIJAU") and simpulkan(teks) != harap)
    VERDICT_RE = asli
    print(f"  [{'OK ' if mutasi >= 4 else 'GAGAL'}] MUTASI kosakata lama terdeteksi "
          f"({mutasi} uji verdict review jadi gagal; harus >=4)")
    if mutasi < 4:
        gagal += 1

    # MUTASI 2 — matikan pagar PENULIS_RE: komentar penulis harus bocor jadi verdict.
    asli_p = PENULIS_RE
    PENULIS_RE = re.compile(r"(?!x)x")
    bocor = simpulkan("## Tanggapan penulis atas verdict putaran 1 (MERAH)\n")
    PENULIS_RE = asli_p
    print(f"  [{'OK ' if bocor == 'MERAH' else 'GAGAL'}] MUTASI pagar penulis terdeteksi "
          f"(tanpa pagar, komentar penulis terbaca: {bocor})")
    if bocor != "MERAH":
        gagal += 1

    # MUTASI 3 — matikan strip_code_fences: isi fence harus bocor jadi verdict.
    asli_f = globals()["strip_code_fences"]
    globals()["strip_code_fences"] = lambda s: s
    bocor2 = simpulkan("Laporan.\n\n```text\n## Review — HIJAU\n```\n")
    globals()["strip_code_fences"] = asli_f
    print(f"  [{'OK ' if bocor2 == 'HIJAU' else 'GAGAL'}] MUTASI pagar fence terdeteksi "
          f"(tanpa pagar, isi fence terbaca: {bocor2})")
    if bocor2 != "HIJAU":
        gagal += 1

    total = len(KASUS) + len(KASUS_GABUNG) + 3
    if gagal:
        print(f"\nHASIL: {gagal} GAGAL dari {total} pemeriksaan")
        return 1
    print(f"\nHASIL: PASS {total}/{total} pemeriksaan "
          f"({len(KASUS)} pembacaan + {len(KASUS_GABUNG)} agregasi + 3 mutasi)")
    return 0

def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--terbaru", action="store_true", help="ambil hasil audit-isi terbaru dari kanal Issue")
    g.add_argument("--issue", type=int, metavar="N", help="ambil Issue nomor N")
    g.add_argument("--pr", type=int, metavar="N", help="ambil hasil review PR nomor N (kanal lama)")
    g.add_argument("--uji", action="store_true",
                   help="uji-mutasi pembaca verdict (D-1) + agregasi fail-closed; tidak memanggil GitHub")
    g.add_argument("--daftar", action="store_true", help="daftar kandidat audit-isi tanpa mencetak isi")
    g.add_argument("--berkas", metavar="PATH", help="ambil hasil audit dari berkas ter-commit (kanal git)")
    ap.add_argument("--objek", help="saring berdasarkan objek, mis. `_meta` atau `sistem/sistem-klinik`")
    a = ap.parse_args()

    try:
        # Kanal berkas TIDAK butuh gh sama sekali — itulah gunanya ada.
        if a.berkas:
            return cetak_berkas((ROOT / a.berkas).resolve()
                                if not Path(a.berkas).is_absolute() else Path(a.berkas))
        if a.pr or a.issue:
            gh_tersedia()
        if a.uji:
            return uji()
        if a.pr:
            return cetak_pr(a.pr)
        if a.issue:
            return cetak_issue(a.issue)

        berkas, err_berkas = daftar_berkas(a.objek)
        if a.pr is None and a.issue is None:
            try:
                gh_tersedia()
                kandidat, err_gh = daftar_kandidat(a.objek)
            except ToolError as e:
                kandidat, err_gh = [], str(e)
        else:
            kandidat, err_gh = [], None
        for e in (err_gh, err_berkas):
            if e:
                print(f"[catatan kanal] {e}", file=sys.stderr)
        semua = kandidat + berkas
        if a.daftar:
            if not semua:
                print("Tidak ada Issue yang cocok dengan kanal audit-isi"
                      + (f" untuk objek `{a.objek}`" if a.objek else "") + ".")
                print(f"Kanal yang dikenali: label `{LABEL_ISSUE}` ATAU judul berpola `AUDIT <objek> @<sha>`.")
                return 0
            print(f"{len(semua)} kandidat audit-isi (terbaru di atas; kanal Issue + kanal berkas):")
            for k in sorted(semua, key=lambda x: x["createdAt"], reverse=True):
                idn = f"#{k['number']:<4}" if k.get("number") else "berkas"
                print(f"  {idn:<6} {k['createdAt'][:19]}  {k['state']:<6} "
                      f"objek={k['objek']} sha={k['sha']} via={k['via']}")
                print(f"         {k.get('path') or k['title']}")
            return 0

        # --terbaru: dua kanal digabung, yang terbaru menang, tanpa menebak
        if not semua:
            raise ToolError(
                "tidak ditemukan hasil audit di KEDUA kanal"
                + (f" untuk objek `{a.objek}`" if a.objek else "") + ".\n"
                f"  Kanal Issue : label `{LABEL_ISSUE}` ATAU judul `AUDIT <objek> @<sha>`"
                + (f" — TIDAK TERSEDIA: {err_gh}" if err_gh else " — tersedia, kosong") + ".\n"
                f"  Kanal berkas: `_meta/_internal/audit/*.md` berbaris judul `# AUDIT <objek> @<sha>`"
                + (f" — {err_berkas}" if err_berkas else " — tersedia, kosong") + ".\n"
                "  Kemungkinan: (a) audit memang belum diserahkan; (b) auditor menulisnya di tempat lain.\n"
                "  PENTING (terverifikasi 17 Sep 2026): di lingkungan produksi ini `gh issue create`\n"
                "  DITOLAK HTTP 403 'Resource not accessible by integration', jadi kanal Issue bisa jadi\n"
                "  memang tidak pernah bisa dipakai di sini — pakai kanal berkas.\n"
                "  Alat ini TIDAK menebak dan TIDAK menyimpulkan 'bersih' dari ketiadaan hasil.\n"
                "  Periksa manual: gh issue list --state all --limit 30 ; ls _meta/_internal/audit/"
            )
        terurut = sorted(semua, key=lambda x: x["createdAt"], reverse=True)
        if len(terurut) > 1 and terurut[0]["createdAt"] == terurut[1]["createdAt"]:
            ids = ", ".join((f"#{k['number']}" if k.get("number") else k["path"]) for k in terurut[:5])
            raise ToolError(
                f"ambigu: ada beberapa hasil audit dengan waktu identik ({ids}).\n"
                "  'Terbaru' TIDAK ditebak. Pilih eksplisit: --issue <N> atau --berkas <PATH>\n"
                "  Lihat daftarnya: python3 tools/ambil_verdict.py --daftar"
            )
        pilih = terurut[0]
        if len(terurut) > 1:
            print(f"[diambil yang terbaru: {pilih.get('path') or '#' + str(pilih['number'])} · "
                  f"{pilih['createdAt']} · {len(terurut) - 1} kandidat lain lebih lama — lihat --daftar]\n")
        return cetak_berkas(ROOT / pilih["path"]) if pilih["via"] == "berkas" else cetak_issue(pilih["number"])
    except ToolError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
