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
import contextlib
import io
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
# D-3: penanda bahwa sebuah komentar adalah LAPORAN REVIEW, bukan komentar penulis PR.
# Sengaja KETAT: kata "temuan"/"review" saja tidak cukup, karena komentar penulis di PR #74
# memuat kata-kata itu di judulnya dan akan ikut terhitung sebagai slot hakim.
LAPORAN_RE = re.compile(
    r"(review\s+independen|verdict|putaran\s*\d|jangan\s+merge|\bMERAH\b|\bHIJAU\b|\bBLOCKER\b)",
    re.I,
)


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


def slot_hakim(teks: str) -> bool:
    """Apakah komentar/review ini SLOT HAKIM, bukan komentar penulis PR (perbaikan D-3).

    Keputusan hanya dari BARIS BERPARKAH PERTAMA (judul):
      1. judul menyebut dirinya dari penulis -> BUKAN slot (diperiksa LEBIH DULU);
      2. judul memuat token laporan review   -> slot;
      3. selain itu                          -> BUKAN slot.

    Fail-closed dijaga: laporan review yang verdictnya tidak terbaca TETAP jadi slot, karena
    TIDAK DITEMUKAN menahan merge. Risiko sisa — laporan hakim yang judulnya tidak memuat
    token apa pun ikut terlewat — dikompensasi oleh `--harapkan N`: slot yang kurang muncul
    sebagai KUORUM BELUM TERPENUHI, bukan sebagai keheningan.
    """
    for baris in strip_code_fences(teks or "").splitlines():
        if not (PENANDA_RE.match(baris) or HEADING_RE.match(baris)):
            continue
        if PENULIS_RE.search(baris):
            return False
        return bool(LAPORAN_RE.search(baris))
    return False


def gabungkan(verdicts: list[str], diharapkan: int | None = None) -> str:
    """Agregasi FAIL-CLOSED atas banyak hakim (keputusan pemilik 17 Sep 2026).

    Satu saja verdict yang bukan hijau -> gabungan MENAHAN merge. Tidak ada mayoritas,
    tidak ada rata-rata: yang dicari reviewer independen adalah alasan untuk menolak,
    bukan suara terbanyak. Verdict TIDAK DITEMUKAN juga menahan, karena "tidak terbaca"
    bukan berarti "bersih".

    `diharapkan` = KUORUM (D-3): jumlah hakim yang sungguh dikerahkan pemilik. Bila slot yang
    terbaca kurang dari itu, hasilnya TIDAK PERNAH hijau — hakim yang tidak menyerahkan laporan
    bukan hakim yang puas. Lahir dari kejadian nyata 18 Sep 2026: 3 hakim dikerahkan untuk
    PR #74, hanya 1 verdict yang sampai ke GitHub, dan alat lama melaporkan "1 dari 4 verdict
    bukan hijau" tanpa sedikit pun menandakan bahwa 2 verdict HILANG — malah menghitung 3
    komentar penulis PR sebagai slot hakim.
    """
    sah = [v for v in verdicts if v and not v.startswith("TIDAK DITEMUKAN")]
    kurang = diharapkan - len(verdicts) if diharapkan is not None and diharapkan > len(verdicts) else None
    if not verdicts:
        dasar = "BELUM ADA VERDICT — jangan merge, jangan simpulkan bersih"
    else:
        merah = [v for v in sah if v not in HIJAU_SET]
        tak_terbaca = [v for v in verdicts if v.startswith("TIDAK DITEMUKAN")]
        if merah:
            dasar = (f"MERAH — JANGAN MERGE ({len(merah)} dari {len(verdicts)} slot bukan hijau: "
                     f"{', '.join(sorted(set(merah)))})")
        elif tak_terbaca:
            dasar = (f"MENAHAN — {len(tak_terbaca)} verdict TIDAK TERBACA dari {len(verdicts)}; "
                     "tidak terbaca BUKAN bersih")
        else:
            dasar = f"HIJAU — semua {len(sah)} verdict hijau ({', '.join(sorted(set(sah)))})"
    if kurang:
        return (f"KUORUM BELUM TERPENUHI ({len(verdicts)}/{diharapkan} slot terbaca, {kurang} hakim "
                f"belum menyerahkan atau tidak terbaca) — MENAHAN merge. Dasar: {dasar}")
    return dasar


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


def cetak_issue(nomor: int, diharapkan: int | None = None) -> int:
    d = ambil_issue(nomor)
    body = d.get("body") or ""
    comments = d.get("comments") or []
    # D-4: `kumpul` dulu TIDAK PERNAH didefinisikan di fungsi ini padahal dipakai di bawah ->
    # NameError setiap kali isu punya komentar. Kanal --terbaru ikut lewat sini, jadi kanal UTAMA
    # alat ini crash dan --uji tidak menangkapnya karena tidak pernah memanggil fungsi kanal.
    kumpul: list[str] = []
    bukan_slot = 0
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
            if not slot_hakim(cb):
                bukan_slot += 1
                print("BUKAN SLOT HAKIM (komentar penulis/non-laporan) — tidak dihitung sebagai verdict.")
                print(cb.strip())
                continue
            v = simpulkan(cb)
            kumpul.append(v)
            print(f"VERDICT (terbaca otomatis): {v}")
            print(cb.strip())
    kumpul.insert(0, simpulkan(body))  # verdict badan isu = slot pertama
    print("\n" + "=" * 78)
    print("AGREGASI FAIL-CLOSED (aturan pemilik 17 Sep 2026)")
    print("=" * 78)
    for i, v in enumerate(kumpul, 1):
        print(f"  hakim {i}: {v}")
    print(f"\n  slot terbaca: {len(kumpul)} · komentar bukan slot (penulis/non-laporan): {bukan_slot}")
    print(f"\n  >> HASIL GABUNGAN: {gabungkan(kumpul, diharapkan)}")
    print("\n" + "=" * 78)
    print("CATATAN UNTUK SESI YANG MEMBACA INI:")
    print("- Temuan di bagian 'DI LUAR CAKUPAN' **wajib ikut dilaporkan** ke pemilik, jangan disaring")
    print("  (ATURAN CAKUPAN di QUALITY_ASSURANCE_AND_EVOLUTION.md: cakupan membatasi pencarian dan klaim,")
    print("   tidak pernah membatasi laporan).")
    print("- Bagian 'kandidat yang DICABUT' adalah bagian dari kejujuran laporan, bukan sampah — jangan dibuang.")
    print("- **Membaca verdict ≠ menyetujuinya.** Bertindak atas temuan butuh mandat pemilik;")
    print("  menemukan ≠ memperbaiki (QA Prinsip 2).")
    return 0


def cetak_pr(nomor: int, diharapkan: int | None = None) -> int:
    d = ambil_pr(nomor)
    comments = d.get("comments") or []
    reviews = d.get("reviews") or []
    print("=" * 78)
    print(f"PR #{d.get('number')} — {d.get('title')}")
    print(f"state: {d.get('state')} · head: {(d.get('headRefOid') or '')[:12]} · base: {d.get('baseRefName')}")
    print("=" * 78)
    kumpul: list[str] = []
    bukan_slot = 0
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
            if not slot_hakim(cb):
                bukan_slot += 1
                print("BUKAN SLOT HAKIM (komentar penulis/non-laporan) — tidak dihitung sebagai verdict.")
                print(cb.strip())
                continue
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
    print(f"\n  slot hakim terbaca: {len(kumpul)} · komentar bukan slot (penulis/non-laporan): {bukan_slot}")
    if diharapkan is None:
        print("  (bila pemilik mengerahkan N hakim, jalankan dengan `--harapkan N`: verdict yang")
        print("   TIDAK SAMPAI akan terbaca sebagai KUORUM BELUM TERPENUHI, bukan sebagai hening)")
    print(f"\n  >> HASIL GABUNGAN: {gabungkan(kumpul, diharapkan)}")
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

# D-3: komentar penulis PR BUKAN slot hakim. Semua kasus di bawah diambil dari komentar NYATA
# di PR #74, yaitu kasus yang membuat alat lama melaporkan "1 dari 4 verdict".
KASUS_SLOT = [
    ("D-3 NYATA: 'Koreksi terbuka dari penulis PR' bukan slot",
     "## ⚠️ Koreksi terbuka dari penulis PR — harap dibaca sebelum mereview\n\nIsi.\n", False),
    ("D-3 NYATA: 'Tanggapan penulis atas verdict putaran 1 (MERAH)' bukan slot "
     "(penulis diperiksa SEBELUM token laporan)",
     "## Tanggapan penulis atas verdict putaran 1 (MERAH) + 2 cacat tambahan\n", False),
    ("D-3 NYATA: deklarasi head penulis bukan slot walau judul memuat kata 'temuan'",
     "## Head yang hendak diputuskan sekarang: `ac25de0` — dan status tiap temuan\n", False),
    ("D-3 NYATA: laporan hakim ke-1 PR #74 = slot",
     "## Review independen — putaran 1 — MERAH (parsial, bukan persetujuan)\n", True),
    ("D-3: laporan verdict berpemarkah = slot",
     "# VERDICT: HIJAU — Review Independen Putaran 1/2 (PR #75)\n", True),
    ("D-3 fail-closed: laporan yang verdictnya tak terbaca TETAP slot",
     "## Review independen — putaran 1\n\nLaporan tanpa kata verdict.\n", True),
]

# D-3: kuorum. Hakim yang tidak menyerahkan laporan BUKAN hakim yang puas.
KASUS_GABUNG2 = [
    ("D-3: kuorum kurang + ada MERAH -> KUORUM", ["MERAH"], 3, "KUORUM"),
    ("D-3: kuorum kurang walau SEMUA hijau -> tetap bukan HIJAU", ["HIJAU", "HIJAU"], 3, "KUORUM"),
    ("D-3: kuorum kurang + belum ada verdict sama sekali -> KUORUM", [], 3, "KUORUM"),
    ("D-3: kuorum terpenuhi -> tidak menyebut KUORUM", ["MERAH", "HIJAU", "HIJAU"], 3, "MERAH"),
    ("D-3: tanpa --harapkan perilaku lama tetap", ["HIJAU", "HIJAU"], None, "HIJAU"),
]

# D-4: fixture untuk smoke test KANAL. --uji dulu hanya menguji fungsi murni, jadi NameError di
# cetak_issue (kanal --issue DAN --terbaru) lolos dari uji sendiri.
FIX_ISU = {
    "number": 901, "title": "AUDIT _meta @abc1234567", "state": "OPEN", "createdAt": "2026-09-18T00:00:00Z",
    "labels": [{"name": "audit-independen"}],
    "body": "# AUDIT _meta @abc1234567\n\n**VERDICT:** ADA TEMUAN\n",
    "comments": [
        {"author": {"login": "bot"}, "createdAt": "2026-09-18T00:01:00Z",
         "body": "## Tanggapan penulis atas verdict (MERAH)\n"},
        {"author": {"login": "bot"}, "createdAt": "2026-09-18T00:02:00Z",
         "body": "## Review independen — putaran 1 — MERAH\n"},
    ],
}
FIX_PR = {
    "number": 902, "title": "PR uji", "state": "OPEN", "headRefOid": "ac25de0" * 5,
    "baseRefName": "main", "reviews": [],
    "body": "",
    "comments": [
        {"author": {"login": "bot"}, "createdAt": "1", "body": "## ⚠️ Koreksi terbuka dari penulis PR\n"},
        {"author": {"login": "bot"}, "createdAt": "2", "body": "## Review independen — putaran 1 — MERAH\n"},
        {"author": {"login": "bot"}, "createdAt": "3", "body": "## Head yang hendak diputuskan: `ac25de0`\n"},
    ],
}


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
    for nama, teks, harap in KASUS_SLOT:
        got = slot_hakim(teks)
        print(f"  [{'OK ' if got == harap else 'GAGAL'}] {nama}")
        if got != harap:
            print(f"        harapan slot={harap} · dapat slot={got}")
            gagal += 1
    for nama, vs, n, harap in KASUS_GABUNG2:
        got = gabungkan(vs, n)
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

    # MUTASI 4 (D-3) — matikan PENULIS_RE di slot_hakim: komentar penulis harus BOCOR jadi slot.
    # Ini yang menguji bahwa URUTAN pemeriksaan (penulis lebih dulu dari token laporan) load-bearing.
    asli_p2 = PENULIS_RE
    PENULIS_RE = re.compile(r"(?!x)x")
    bocor4 = sum(1 for _, teks, harap in KASUS_SLOT if slot_hakim(teks) != harap)
    PENULIS_RE = asli_p2
    print(f"  [{'OK ' if bocor4 >= 1 else 'GAGAL'}] MUTASI pagar penulis di slot_hakim terdeteksi "
          f"({bocor4} kasus klasifikasi jadi salah; harus >=1)")
    if bocor4 < 1:
        gagal += 1

    # REGRESI D-4 — smoke KANAL NYATA: panggil cetak_issue dan cetak_pr dengan fixture.
    # Dulu keduanya TIDAK PERNAH dipanggil --uji, jadi NameError `kumpul` di cetak_issue
    # (kanal --issue DAN kanal utama --terbaru) lolos dari uji sendiri.
    asli_ii, asli_ap = globals()["ambil_issue"], globals()["ambil_pr"]
    globals()["ambil_issue"] = lambda n: FIX_ISU
    globals()["ambil_pr"] = lambda n: FIX_PR
    cacat = []
    for nama, fn in (("cetak_issue", lambda: cetak_issue(901, 3)), ("cetak_pr", lambda: cetak_pr(902, 3))):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                rc = fn()
            out = buf.getvalue()
            if rc != 0:
                cacat.append(f"{nama}: rc={rc}")
            if "KUORUM BELUM TERPENUHI" not in out:
                cacat.append(f"{nama}: kuorum tidak dilaporkan")
            if "BUKAN SLOT HAKIM" not in out:
                cacat.append(f"{nama}: komentar penulis tidak disaring")
        except Exception as e:  # NameError D-4 mendarat di sini
            cacat.append(f"{nama}: {type(e).__name__}: {e}")
    globals()["ambil_issue"], globals()["ambil_pr"] = asli_ii, asli_ap
    print(f"  [{'OK ' if not cacat else 'GAGAL'}] REGRESI D-4 smoke kanal (cetak_issue + cetak_pr "
          f"dipanggil sungguhan, kuorum + saringan penulis terlihat)")
    for c in cacat:
        print(f"        {c}")
        gagal += 1

    total = len(KASUS) + len(KASUS_GABUNG) + len(KASUS_SLOT) + len(KASUS_GABUNG2) + 5
    if gagal:
        print(f"\nHASIL: {gagal} GAGAL dari {total} pemeriksaan")
        return 1
    print(f"\nHASIL: PASS {total}/{total} pemeriksaan "
          f"({len(KASUS)} pembacaan + {len(KASUS_GABUNG) + len(KASUS_GABUNG2)} agregasi "
          f"+ {len(KASUS_SLOT)} klasifikasi slot + 4 mutasi + 1 smoke kanal)")
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
    ap.add_argument("--harapkan", type=int, metavar="N",
                    help="KUORUM (D-3): jumlah hakim yang sungguh dikerahkan pemilik. Slot terbaca "
                         "< N = KUORUM BELUM TERPENUHI dan hasil tidak pernah hijau")
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
            return cetak_pr(a.pr, a.harapkan)
        if a.issue:
            return cetak_issue(a.issue, a.harapkan)

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
        return cetak_berkas(ROOT / pilih["path"]) if pilih["via"] == "berkas" else cetak_issue(pilih["number"], a.harapkan)
    except ToolError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
