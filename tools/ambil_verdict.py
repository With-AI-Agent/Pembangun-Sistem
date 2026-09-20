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
`tools/audit_prompt.py` bagian 10.

SATU ALAT, DUA KANAL — sengaja tidak dibuat dua alat, dan urutannya SATU keputusan, bukan dua
pilihan yang bersaing (T-61, temuan P2 putaran 8 PR #74: petunjuk penyerahan di empat tempat
saling bertentangan, sebagian masih menyebut Issue sebagai tujuan tanpa label apa pun):
  * audit ISI (non-PR) → **KANAL A = berkas ter-commit** di `_meta/_internal/audit/`, baris pertama
                         `# AUDIT <objek> @<sha7>` — UTAMA dan terbukti berfungsi. **Kanal B = GitHub
                         Issue** berlabel `audit-independen` adalah ALTERNATIF yang terukur TERBLOKIR
                         HTTP 403 `Resource not accessible by integration` (17 Sep 2026), jadi jangan
                         pernah disebut sebagai tujuan penyerahan tanpa label alternatif-terblokir itu
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
# Sengaja KETAT dan TIDAK memuat kata "verdict" atau "temuan" polos. Alasannya diukur dua kali:
#   (a) komentar penulis PR #74 berjudul "...status tiap temuan" ikut terhitung sebagai slot;
#   (b) SESUDAH perbaikan itu, komentar penulis berikutnya berjudul "...kuorum verdict TIDAK
#       terpenuhi (1 dari 3)" MASIH ikut terhitung, karena memuat kata "verdict" polos — jadi
#       PR #74 terbaca punya 2 slot hakim padahal hanya 1. Regresi ini tertangkap karena alat
#       dijalankan ULANG sesudah komentar ditempel, bukan sebelumnya.
# Katanya dibatasi pada token putusan sungguhan (kosakata VERDICT_RE minus COMMENT, yang terlalu
# mudah kena kata "komentar") + penanda diri laporan review.
# CATATAN BATAS: penyaringan berdasarkan PENULIS komentar TIDAK MUNGKIN di platform ini — semua
# sesi memakai satu identitas bot yang sama, jadi penulis dan hakim tak bisa dibedakan dari author.
LAPORAN_RE = re.compile(
    r"(\bMERAH\b|\bHIJAU\b|\bBERSIH\b|\bBLOCKER\b|ADA\s+TEMUAN"
    r"|TIDAK\s+BISA\s+DISIMPULKAN|APPROVE|REQUEST_CHANGES"
    r"|review\s+independen|putaran\s*\d|jangan\s+merge)",
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


PUTARAN_RE = re.compile(r"putaran\s+(\d+)", re.IGNORECASE)


def putaran_dari(teks: str) -> int | None:
    """Nomor putaran yang DINAMAI sebuah laporan; None kalau tidak menamai putaran.

    Dibaca sesudah pagar kode dikosongkan (`strip_code_fences`), jadi contoh judul di dalam prompt yang
    dipagari tidak ikut terhitung — pola yang sama dengan `slot_hakim()`.
    """
    m = PUTARAN_RE.search(strip_code_fences(teks or ""))
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------------------
# Validasi pin SHA laporan (T-59 — temuan P1 putaran 8 PR #74, direproduksi dua hakim)
# ---------------------------------------------------------------------------
# Cacat yang ditutup: `cetak_pr()` hanya menyimpan hasil `simpulkan()` + nomor putaran, dan
# `headRefOid` cuma DICETAK di baris head, tidak pernah dipakai memvalidasi apa pun. Akibatnya
# tiga laporan yang tidak menyebut SHA — atau menyebut SHA head lain — bisa menjadi bukti HIJAU
# sekaligus kuorum LENGKAP untuk head yang sedang diadili. Reproduksi hakim: memanggil fungsi
# kanal nyata `cetak_pr(999, 3, 8)` dengan fixture tiga komentar hijau berformat sah tetapi tanpa
# SHA menghasilkan "HIJAU — semua 3 verdict hijau" dan "kuorum 3/3 LENGKAP (0 bukan hijau)".
# Prinsip penggantinya fail-closed dan SENGAJA asimetris:
#   * HIJAU butuh bukti bahwa ia bicara tentang head yang diadili -> pin SHA wajib cocok;
#   * MERAH tidak butuh bukti apa pun                             -> selalu menahan, pin atau tidak.
# Merah yang salah pin paling jauh membuat kita berhenti terlalu awal dan bertanya; hijau yang
# salah pin membuat kita merge benda yang tidak pernah diperiksa siapa pun.
SHA_HEX_RE = re.compile(r"\b[0-9a-f]{7,40}\b")
KONTEKS_PIN_RE = re.compile(
    r"(?:\b(?:head|pin|pinned|terpin|ter-pin|dinilai|diadili|objek|commit|sha|revisi)\b|@)",
    re.I,
)


def pin_verdict(teks: str, head: str | None) -> str:
    """Status pin SHA sebuah laporan terhadap head yang diadili.

    Keluaran: ``"cocok"`` | ``"tanpa-pin"`` | ``"beda:<sha7>[|<sha7>...]"`` | ``"head-tak-terbaca"``.

    Hanya SHA di baris BERKONTEKS pin (menyebut head/pin/objek/commit/sha, atau pola judul
    ``@<sha7>``) yang dihitung, dan isi pagar kode dikosongkan lebih dulu — jadi SHA yang cuma
    nongol di dalam contoh perintah `git diff` tidak diklaim sebagai pin. Ketatnya sengaja:
    salah menolak laporan hijau yang sah hanya membuat kita berhenti dan bertanya, sedangkan
    salah menerima laporan hijau untuk head lain membuat kita merge benda yang tak pernah diperiksa.
    """
    if not head or not head.strip():
        return "head-tak-terbaca"
    head = head.strip().lower()
    disebut: list[str] = []
    for baris in strip_code_fences(teks or "").splitlines():
        if not KONTEKS_PIN_RE.search(baris):
            continue
        disebut += [t.lower() for t in SHA_HEX_RE.findall(baris)]
    if not disebut:
        return "tanpa-pin"
    for t in disebut:
        if t == head or head.startswith(t) or t.startswith(head):
            return "cocok"
    unik = sorted({t[:7] for t in disebut})
    return "beda:" + "|".join(unik[:3]) + ("|..." if len(unik) > 3 else "")


def sah_untuk_head(status_pin: str) -> bool:
    """Hanya pin yang COCOK yang boleh menjadi bukti hijau. Fail-closed, tanpa pengecualian."""
    return status_pin == "cocok"


# ---------------------------------------------------------------------------
# Agregasi kanal berkas append-only (T-60 — temuan P1 putaran 8 PR #74, dua hakim)
# ---------------------------------------------------------------------------
# Cacat yang ditutup: `_meta/PROTOKOL_AUDIT_ISI.md` (bagian "Apa yang terjadi sesudahnya")
# mengizinkan putaran lanjutan ditambahkan di bawah laporan berkas yang sama, tetapi
# `cetak_berkas()` meringkas dengan `simpulkan(teks)` yang mengambil kecocokan PERTAMA — jadi
# berkas berisi "Putaran 1: BERSIH" lalu "Putaran 2: ADA TEMUAN" diringkas BERSIH. Isi putaran
# kedua memang ikut tercetak; yang salah adalah ringkasan keputusan otomatisnya, dan ringkasan
# itulah yang dibaca pemilik. Fail-closed: satu putaran bukan hijau -> gabungan menahan.
PUTARAN_HEADING_RE = re.compile(r"^[ \t]{0,3}#{2,6}[ \t]*putaran[ \t]+(\d+)[ \t]*$", re.I | re.M)


def pecah_putaran(teks: str) -> list[tuple[int | None, str]]:
    """Pecah laporan append-only per bagian `## Putaran N`.

    Teks sebelum putaran pertama (judul, metadata) dikembalikan sebagai ``(None, ...)``, supaya
    verdict yang ditulis di luar bagian putaran tetap ikut dihitung dan tidak hilang diam-diam.
    """
    bersih = strip_code_fences(teks or "")
    potong = [(m.group(1), m.start()) for m in PUTARAN_HEADING_RE.finditer(bersih)]
    if not potong:
        return [(None, bersih)]
    hasil: list[tuple[int | None, str]] = []
    if potong[0][1] > 0:
        hasil.append((None, bersih[:potong[0][1]]))
    for i, (nomor, awal) in enumerate(potong):
        akhir = potong[i + 1][1] if i + 1 < len(potong) else len(bersih)
        hasil.append((int(nomor), bersih[awal:akhir]))
    return hasil


def verdict_per_putaran(teks: str) -> list[tuple[int | None, str]]:
    """[(nomor putaran, verdict)] hanya untuk bagian yang verdict-nya TERBACA."""
    hasil: list[tuple[int | None, str]] = []
    for nomor, bagian in pecah_putaran(teks):
        v = simpulkan(bagian)
        if v.startswith("TIDAK DITEMUKAN"):
            continue
        hasil.append((nomor, v))
    return hasil


def ringkas_berkas(teks: str) -> str:
    """Ringkasan fail-closed kanal berkas: agregasi SEMUA putaran, bukan verdict pertama."""
    bagian = verdict_per_putaran(teks)
    if len(bagian) <= 1:
        return simpulkan(teks)
    label = ", ".join(f"putaran {n if n is not None else '?'}: {v}" for n, v in bagian)
    bukan_hijau = [(n, v) for n, v in bagian if v not in HIJAU_SET]
    if bukan_hijau:
        rinci = ", ".join(f"putaran {n if n is not None else '?'}: {v}" for n, v in bukan_hijau)
        token = "/".join(sorted({v for _, v in bukan_hijau}))
        return (f"{token} — MENAHAN: {len(bukan_hijau)} dari {len(bagian)} putaran bukan hijau ({rinci}). "
                f"Verdict putaran pertama TIDAK menutup putaran sesudahnya. Semua putaran: {label}")
    return f"HIJAU — semua {len(bagian)} putaran hijau ({label})"


def kuorum_putaran(pasangan: list[tuple[str, int | None]], diharapkan: int | None = None,
                   putaran: int | None = None) -> str:
    """Laporan kuorum PER PUTARAN (temuan #3 hakim putaran 3 PR #74, P1).

    **Sebab fungsi ini ada.** `gabungkan(..., diharapkan)` membandingkan kuorum terhadap SELURUH slot,
    sedangkan slot lintas putaran menumpuk: di PR #74 putaran 3, `--harapkan 3` mencetak "5 dari 5 slot"
    (lalu "7 dari 7") dan **tidak pernah** bisa memberi tahu pemilik bahwa 2 dari 3 hakim putaran 3 belum
    menyerahkan laporan. Itu persis mode kegagalan D-3 yang `--harapkan` dibuat untuk menutupnya — jadi
    penjaganya fail-open di tingkat putaran walaupun fail-closed di tingkat agregat.

    **Yang TIDAK berubah:** agregat lintas putaran tetap fail-closed (satu MERAH di putaran mana pun
    menahan merge, verdict tak terbaca menahan merge). Fungsi ini hanya MENAMBAH laporan per putaran,
    karena dari laporan itulah pemilik memutuskan boleh tidaknya bertindak dengan verdict belum lengkap.

    `putaran` = putaran yang hendak diputus (default: putaran terbaru yang ada di kanal).
    """
    b: list[str] = []
    a = b.append
    per: dict[int, list[tuple[str, bool]]] = {}
    tanpa_nomor: list[str] = []
    for item in pasangan or []:
        # Tripel (verdict, putaran, sah-pin) sejak T-59; pasangan lama (2 unsur) tetap diterima
        # dan dianggap sah supaya pemanggil lama tidak berubah perilakunya diam-diam.
        v, r = item[0], item[1]
        sah = True if len(item) < 3 else bool(item[2])
        if r is None:
            tanpa_nomor.append(v or "TIDAK TERBACA")
        else:
            per.setdefault(r, []).append((v or "TIDAK TERBACA", sah))
    a("  KUORUM PER PUTARAN (agregat fail-closed di atas tetap berlaku lintas putaran):")
    if not per and not tanpa_nomor:
        a("    belum ada slot hakim yang terbaca — belum ada putaran yang bisa dilaporkan")
    for r in sorted(per):
        vs = [v for v, _ in per[r]]
        tak_sah = sum(1 for _, sh in per[r] if not sh)
        ringkas = ", ".join(sorted(set(vs)))
        ekor = f" · {tak_sah} slot pin SHA-nya tidak cocok dengan head yang diadili" if tak_sah else ""
        a(f"    putaran {r}: {len(vs)} slot — {ringkas}{ekor}")
    if tanpa_nomor:
        a(f"    (tanpa nomor putaran: {len(tanpa_nomor)} slot — {', '.join(sorted(set(tanpa_nomor)))}; "
          "tidak bisa dipetakan ke putaran mana pun, jadi TIDAK dihitung sebagai kuorum putaran)")
    if not per:
        return "\n".join(b)
    target = putaran if putaran is not None else max(per)
    asal = "dipilih eksplisit lewat --putaran" if putaran is not None else "putaran terbaru di kanal"
    if target not in per:
        a(f"  >> PUTARAN YANG DIPUTUS: {target} ({asal}) — **TIDAK ADA slot hakim untuk putaran ini**.")
        a("     Artinya verdict belum diserahkan, BUKAN bersih. Jangan merge, jangan simpulkan hijau.")
        return "\n".join(b)
    n = len(per[target])
    n_sah = sum(1 for _, sh in per[target] if sh)
    merah = [v for v, _ in per[target] if v not in HIJAU_SET]
    if diharapkan is None:
        a(f"  >> PUTARAN YANG DIPUTUS: {target} ({asal}) — {n} slot terbaca ({n_sah} ter-pin pada head "
          f"yang diadili), {len(merah)} di antaranya bukan hijau.")
        a("     Kuorum TIDAK DINYATAKAN: jalankan dengan `--harapkan N` (N = jumlah hakim yang sungguh")
        a("     kamu kerahkan) supaya verdict yang tidak sampai terbaca sebagai KUORUM BELUM LENGKAP.")
    elif n_sah < diharapkan:
        a(f"  >> PUTARAN YANG DIPUTUS: {target} ({asal}) — kuorum SAH {n_sah}/{diharapkan} "
          f"**BELUM LENGKAP**.")
        if n_sah < n:
            a(f"     {n - n_sah} dari {n} slot yang terbaca TIDAK SAH untuk head ini: pin SHA-nya absent")
            a("     atau menunjuk head lain. Laporan yang tidak bisa dipetakan ke head yang diadili BUKAN")
            a("     bukti hijau — hijau hanya boleh dinyatakan dari pemeriksaan atas benda yang akan di-merge.")
        else:
            a(f"     {diharapkan - n_sah} hakim belum menyerahkan laporan atau laporannya tidak terbaca.")
        a("     Hakim yang hening bukan hakim yang puas: jangan bertindak atas putaran ini seolah-olah")
        a("     lengkap, dan jangan menyimpulkan apa pun dari putaran yang belum penuh.")
    else:
        a(f"  >> PUTARAN YANG DIPUTUS: {target} ({asal}) — kuorum {n_sah}/{diharapkan} LENGKAP "
          f"({len(merah)} bukan hijau) · semua slot ter-pin pada head yang diadili.")
    return "\n".join(b)


class ToolError(Exception):
    """Kegagalan yang harus terlihat sebagai exit non-zero + pesan spesifik."""


def _run(cmd: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def head_repo() -> str:
    """SHA HEAD repo saat ini; kosong bila git tidak bisa ditanya (jangan menebak)."""
    code, out, _ = _run(["git", "rev-parse", "HEAD"])
    return out.strip() if code == 0 else ""


def catatan_pin_audit(sha_laporan: str | None) -> str:
    """Catatan kesegaran pin untuk kanal audit-isi (peringatan, BUKAN penurunan verdict).

    Audit isi tidak memutuskan merge, jadi laporan lama tetap sah sebagai riwayat; yang wajib
    terlihat adalah apakah laporan itu masih bicara tentang isi yang sama dengan HEAD sekarang.
    Ini saudara dari T-59 di kanal PR: di sana pin yang salah membuat hijau ditolak, di sini pin
    yang salah membuat umur laporan dinyatakan terang-terangan.
    """
    head = head_repo()
    if not sha_laporan:
        return ("  \u26a0 judul tidak memuat pin `@<sha7>` — tidak bisa dipastikan laporan ini memeriksa"
                " keadaan yang mana; jangan dibaca sebagai laporan atas HEAD sekarang.")
    if not head:
        return "  \u26a0 HEAD repo tidak terbaca — kesegaran pin tidak bisa diperiksa."
    a, b = sha_laporan.strip().lower(), head.lower()
    if a == b or b.startswith(a) or a.startswith(b):
        return f"  pin laporan: `{sha_laporan}` == HEAD repo sekarang (laporan bicara tentang isi terkini)."
    return (f"  \u26a0 pin laporan `{sha_laporan}` != HEAD repo sekarang `{head[:12]}` — laporan ini"
            " memeriksa keadaan LAMA. Sah sebagai riwayat, tetapi jangan dipakai menyimpulkan isi hari ini.")


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
    print(catatan_pin_audit(m.group("sha") if m else None))
    print("=" * 78)
    print(teks)
    print("=" * 78)
    bagian = verdict_per_putaran(teks)
    if len(bagian) > 1:
        print("VERDICT PER PUTARAN (berkas append-only — putaran lanjutan TIDAK menutup yang pertama):")
        for nomor, v in bagian:
            print(f"  putaran {nomor if nomor is not None else '(di luar bagian putaran)'}: {v}")
    print(f"VERDICT TERBACA OTOMATIS: {ringkas_berkas(teks)}")
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
    print(catatan_pin_audit(m.group("sha") if m else None))
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


def cetak_pr(nomor: int, diharapkan: int | None = None, putaran: int | None = None) -> int:
    d = ambil_pr(nomor)
    comments = d.get("comments") or []
    reviews = d.get("reviews") or []
    print("=" * 78)
    print(f"PR #{d.get('number')} — {d.get('title')}")
    print(f"state: {d.get('state')} · head: {(d.get('headRefOid') or '')[:12]} · base: {d.get('baseRefName')}")
    print("=" * 78)
    head = (d.get("headRefOid") or "").strip()
    slot: list[dict] = []                              # {"v", "r", "pin", "sah", "dipakai"}
    kumpul: list[str] = []                             # diisi di blok putusan pin (T-59)
    pasangan: list[tuple[str, int | None, bool]] = []  # (verdict, putaran, sah-pin) — T-59
    bukan_slot = 0
    if reviews:
        print(f"\n----- {len(reviews)} REVIEW -----")
        for i, r in enumerate(reviews, 1):
            rb = r.get("body") or ""
            print(f"\n### review {i} — {r.get('author', {}).get('login', '?')} · state: {r.get('state')}")
            if rb.strip():
                v = simpulkan(rb)
                pin = pin_verdict(rb, head)
                slot.append({"v": v, "r": putaran_dari(rb), "pin": pin})
                print(f"VERDICT (terbaca otomatis): {v} · pin SHA laporan: {pin}")
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
            pin = pin_verdict(cb, head)
            slot.append({"v": v, "r": putaran_dari(cb), "pin": pin})
            print(f"VERDICT (terbaca otomatis): {v} · pin SHA laporan: {pin}")
            print(cb.strip())
    if not reviews and not comments:
        print("\nTIDAK ADA review maupun komentar pada PR ini.")
        print("Artinya verdict **belum diserahkan**, bukan verdict-nya bersih. Jangan disimpulkan sendiri.")
        return 0
    print("\n" + "=" * 78)
    print("AGREGASI FAIL-CLOSED (aturan pemilik 17 Sep 2026: \"Selagi ada yang merah, maka harus diperbaiki\")")
    print("=" * 78)
    # T-59: putusan pin SHA. Hanya putaran yang DIPUTUS yang boleh menurunkan verdict hijau;
    # putaran lama dibiarkan apa adanya (hijau mereka sah untuk head mereka sendiri), tetapi status
    # pinnya tetap dilaporkan supaya riwayat tidak terbaca sebagai bukti atas head hari ini.
    if slot:
        ada_putaran = [x["r"] for x in slot if x["r"] is not None]
        target = putaran if putaran is not None else (max(ada_putaran) if ada_putaran else None)
        if not head:
            print("\n  \u26a0 head PR TIDAK TERBACA dari API — validasi pin SHA tidak bisa dijalankan;")
            print("    fail-closed, hijau tidak dinyatakan untuk putaran yang diputus.")
        for x in slot:
            x["sah"] = sah_untuk_head(x["pin"])
            dipakai = x["v"]
            if x["r"] == target and x["v"] in HIJAU_SET and not x["sah"]:
                dipakai = (f"TIDAK SAH UNTUK HEAD INI (laporan menyebut {x['v']} tetapi pin SHA-nya "
                           f"{x['pin']}; head yang diadili {(head or '?')[:12]})")
            x["dipakai"] = dipakai
            kumpul.append(dipakai)
            pasangan.append((dipakai, x["r"], x["sah"]))
        cocok = sum(1 for x in slot if x["sah"])
        print(f"  pin SHA: {cocok} dari {len(slot)} slot menunjuk head yang diadili ({(head or '?')[:12]}).")
        print("  Slot putaran lama yang pin-nya berbeda itu WAJAR — yang menentukan putaran yang diputus.")
    for i, v in enumerate(kumpul, 1):
        print(f"  hakim {i}: {v}")
    print(f"\n  slot hakim terbaca: {len(kumpul)} · komentar bukan slot (penulis/non-laporan): {bukan_slot}")
    if diharapkan is None:
        print("  (bila pemilik mengerahkan N hakim, jalankan dengan `--harapkan N`: verdict yang")
        print("   TIDAK SAMPAI akan terbaca sebagai KUORUM BELUM TERPENUHI, bukan sebagai hening)")
    print(f"\n  >> HASIL GABUNGAN (SEMUA putaran, fail-closed): {gabungkan(kumpul, diharapkan)}")
    print()
    print(kuorum_putaran(pasangan, diharapkan, putaran))
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
    # Regresi D-3b NYATA: komentar penulis ini membuat PR #74 terbaca punya 2 slot hakim.
    ("D-3b NYATA: judul penulis ber-kata 'verdict' polos BUKAN slot",
     "## Head yang hendak diputuskan sekarang: `4ba2c47` — dan **kuorum verdict TIDAK terpenuhi (1 dari 3)**\n",
     False),
    ("D-3b: judul penulis ber-kata 'temuan' polos BUKAN slot",
     "## Head yang hendak diputuskan sekarang: `ac25de0` — dan status tiap temuan\n", False),
    ("D-3: laporan verdict berpemarkah VERDICT: + MERAH = slot",
     "# VERDICT: MERAH — Review Independen Putaran 1/2 (PR #74)\n", True),
]

# D-3: kuorum. Hakim yang tidak menyerahkan laporan BUKAN hakim yang puas.
KASUS_GABUNG2 = [
    ("D-3: kuorum kurang + ada MERAH -> KUORUM", ["MERAH"], 3, "KUORUM"),
    ("D-3: kuorum kurang walau SEMUA hijau -> tetap bukan HIJAU", ["HIJAU", "HIJAU"], 3, "KUORUM"),
    ("D-3: kuorum kurang + belum ada verdict sama sekali -> KUORUM", [], 3, "KUORUM"),
    ("D-3: kuorum terpenuhi -> tidak menyebut KUORUM", ["MERAH", "HIJAU", "HIJAU"], 3, "MERAH"),
    ("D-3: tanpa --harapkan perilaku lama tetap", ["HIJAU", "HIJAU"], None, "HIJAU"),
]

# Temuan #3 hakim putaran 3 PR #74: kuorum PER PUTARAN. Slot lintas putaran menumpuk, jadi kuorum
# yang dihitung dari seluruh slot tidak pernah bisa mengatakan "2 dari 3 hakim putaran 3 belum masuk".
_P1, _P2, _P3 = ("MERAH", 1), ("MERAH", 2), ("MERAH", 3)
KASUS_PUTARAN = [
    ("kuorum putaran: 1 dari 3 verdict putaran 3 -> BELUM LENGKAP walau slot total 5",
     [_P1, _P2, _P2, _P2, _P3], 3, None, "BELUM LENGKAP"),
    ("kuorum putaran: 3 dari 3 putaran 3 -> LENGKAP",
     [_P1, _P2, _P2, _P2, _P3, ("HIJAU", 3), ("MERAH", 3)], 3, None, "LENGKAP"),
    ("kuorum putaran: --putaran memilih putaran lama, bukan yang terbaru",
     [_P1, _P2, _P2, _P2, _P3, ("HIJAU", 4), ("HIJAU", 4), ("HIJAU", 4)], 3, 3, "BELUM LENGKAP"),
    ("kuorum putaran: tanpa --harapkan tidak mengarang kuorum",
     [_P1, _P2, _P3], None, None, "Kuorum TIDAK DINYATAKAN"),
    ("kuorum putaran: verdict tanpa nomor putaran tidak hilang dan tidak dihitung sebagai kuorum",
     [_P1, ("MERAH", None)], 3, None, "tanpa nomor putaran: 1 slot"),
    ("kuorum putaran: putaran yang diminta tidak ada di kanal -> dinyatakan belum diserahkan",
     [_P1, _P2], 3, 9, "TIDAK ADA slot hakim untuk putaran ini"),
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


# ---------------------------------------------------------------------------
# KUNCI REGRESI T-59 (pin SHA) + T-60 (agregasi kanal berkas) — dua temuan P1 putaran 8
# PR #74 yang direproduksi independen oleh dua hakim. Norma repo: mekanisme baru wajib diuji
# dengan fixture/mutasi, bukan hanya dijalankan sekali lalu terlihat hijau.
KASUS_PIN = [
    # (nama, teks laporan, head yang diadili, harapan status pin)
    ("pin cocok: head disebut di baris berpemarkah",
     "## Review independen PR #74 — putaran 8 — VERDICT: HIJAU\n\n- **Head yang dinilai:** `e698272`\n",
     "e69827297cb0fefbc955958ee8c82872e8309629", "cocok"),
    ("pin cocok: sha penuh 40 karakter di laporan, head API pendek",
     "## Review — putaran 8 — HIJAU\n- head ter-pin: e69827297cb0fefbc955958ee8c82872e8309629\n",
     "e69827297cb0", "cocok"),
    ("pin cocok: pola judul kanal berkas `@<sha7>`",
     "# AUDIT _meta @e698272\n\n## Putaran 1\n- **VERDICT:** BERSIH\n",
     "e69827297cb0", "cocok"),
    ("REGRESI T-59: laporan hijau TANPA sha tidak boleh jadi bukti",
     "## Review independen PR #74 — putaran 8 — VERDICT: HIJAU\n\nSemua cek hijau, tanpa BLOCKER.\n",
     "e69827297cb0", "tanpa-pin"),
    ("REGRESI T-59: laporan hijau untuk head LAIN tidak boleh jadi bukti",
     "## Review independen PR #74 — putaran 8 — VERDICT: HIJAU\n\n- **Head yang dinilai:** `c1b618b`\n",
     "e69827297cb0", "beda:c1b618b"),
    ("sha yang cuma muncul di dalam pagar kode bukan pin",
     "## Review — putaran 8 — HIJAU\n\n```bash\ngit diff 6798bb2 e698272\n```\n",
     "e69827297cb0", "tanpa-pin"),
    ("head tidak terbaca dari API -> tidak pernah sah (fail-closed)",
     "## Review — putaran 8 — HIJAU\n- head dinilai: `e698272`\n", "", "head-tak-terbaca"),
    ("token bukan heks atau terlalu pendek tidak dihitung sebagai pin",
     "## Review — putaran 8 — HIJAU\n- head: `zz12` lalu `12345`\n", "e69827297cb0", "tanpa-pin"),
]

KASUS_BERKAS = [
    # (nama, teks laporan, substring WAJIB ada, substring DILARANG ada)
    ("REGRESI T-60: putaran 2 ADA TEMUAN tidak boleh diringkas BERSIH",
     "# AUDIT _meta @e698272\n\n## Putaran 1\n- **VERDICT:** BERSIH\n\n## Putaran 2\n"
     "- **VERDICT:** ADA TEMUAN\n\nTemuan baru belum ditutup.\n",
     "ADA TEMUAN — MENAHAN", None),
    ("REGRESI T-60: tiga putaran, yang terakhir MERAH, tetap menahan",
     "# AUDIT _meta @e698272\n\n## Putaran 1\n- **VERDICT:** BERSIH\n\n## Putaran 2\n"
     "- **VERDICT:** BERSIH\n\n## Putaran 3\n- **VERDICT:** MERAH\n",
     "MERAH — MENAHAN: 1 dari 3", None),
    ("temuan putaran 1 yang disebut sudah ditutup putaran 2 TETAP menahan (fail-closed)",
     "# AUDIT _meta @e698272\n\n## Putaran 1\n- **VERDICT:** ADA TEMUAN\n\n## Putaran 2\n"
     "- **VERDICT:** BERSIH\n", "ADA TEMUAN/MENAHAN".replace("/", " — MENAHAN: 1 dari 2 putaran bukan hijau (putaran 1: ADA TEMUAN").split(" — ")[0], None),
    ("semua putaran hijau -> hijau, jumlahnya disebut",
     "# AUDIT _meta @e698272\n\n## Putaran 1\n- **VERDICT:** BERSIH\n\n## Putaran 2\n"
     "- **VERDICT:** BERSIH\n", "semua 2 putaran hijau", "MENAHAN"),
    ("berkas satu verdict tanpa bagian putaran: perilaku lama tidak berubah",
     "# AUDIT _meta @e698272\n\n- **VERDICT:** ADA TEMUAN\n\nRincian.\n",
     "ADA TEMUAN", "MENAHAN"),
]

KASUS_PIN_KUORUM = [
    # (nama, pasangan slot, diharapkan, putaran diputus, WAJIB ada, DILARANG ada)
    ("REGRESI T-59: tiga hijau tanpa pin BUKAN kuorum lengkap",
     [("HIJAU", 8, False), ("HIJAU", 8, False), ("HIJAU", 8, False)], 3, 8,
     "kuorum SAH 0/3", "LENGKAP (0 bukan hijau)"),
    ("REGRESI T-59: campuran dua sah + satu tanpa pin belum lengkap",
     [("HIJAU", 8, True), ("HIJAU", 8, True), ("HIJAU", 8, False)], 3, 8,
     "kuorum SAH 2/3", "3/3 LENGKAP"),
    ("tiga hijau ter-pin pada head yang diadili = kuorum lengkap",
     [("HIJAU", 8, True), ("HIJAU", 8, True), ("HIJAU", 8, True)], 3, 8,
     "kuorum 3/3 LENGKAP (0 bukan hijau)", "BELUM LENGKAP"),
    ("merah tanpa pin TETAP menahan, tidak dibuang",
     [("MERAH", 8, False), ("HIJAU", 8, True), ("HIJAU", 8, True)], 3, 8,
     "BELUM LENGKAP", "LENGKAP (0 bukan hijau)"),
    ("pemanggil lama dengan pasangan dua unsur tidak berubah perilakunya",
     [("HIJAU", 2), ("HIJAU", 2), ("HIJAU", 2)], 3, 2,
     "kuorum 3/3 LENGKAP (0 bukan hijau)", "BELUM LENGKAP"),
]


def uji() -> int:
    global VERDICT_RE, PENULIS_RE, LAPORAN_RE
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
    for nama, pasangan, n, put, harap in KASUS_PUTARAN:
        got = kuorum_putaran(pasangan, n, put)
        ok = harap in got
        print(f"  [{'OK ' if ok else 'GAGAL'}] {nama}")
        if not ok:
            print(f"        harapan memuat: {harap} · dapat: {got[:200]}")
            gagal += 1
    # MUTASI kuorum putaran: kalau perhitungan per putaran dilewatkan (semua slot dianggap satu
    # putaran), kasus "1 dari 3 putaran 3" harus berubah jadi LENGKAP — bukti ujinya bukan tautologi.
    _asli = kuorum_putaran([_P1, _P2, _P2, _P2, _P3], 3, None)
    _palsu = kuorum_putaran([(v, 3) for v, _r in [_P1, _P2, _P2, _P2, _P3]], 3, None)
    _mutasi_ok = ("BELUM LENGKAP" in _asli) and ("BELUM LENGKAP" not in _palsu)
    print(f"  [{'OK ' if _mutasi_ok else 'GAGAL'}] MUTASI kuorum putaran: nomor putaran diabaikan -> "
          f"laporan kuorum berubah (bukti uji tidak tautologis)")
    if not _mutasi_ok:
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

    # MUTASI 5 (D-3b) — longgarkan LAPORAN_RE jadi memuat kata "verdict" polos: komentar penulis
    # berjudul "...kuorum verdict TIDAK terpenuhi" harus BOCOR jadi slot hakim. Ini yang menguji
    # bahwa pembatasan kosakata LAPORAN_RE load-bearing, bukan hiasan.
    asli_l = LAPORAN_RE
    LAPORAN_RE = re.compile(r"(review\s+independen|verdict|putaran\s*\d|\bMERAH\b|\bHIJAU\b)", re.I)
    bocor5 = sum(1 for _, teks, harap in KASUS_SLOT if slot_hakim(teks) != harap)
    LAPORAN_RE = asli_l
    # Ambang >=1, bukan >=2: penulis sempat menulis >=2 dan uji ini langsung MENANGKAPnya —
    # hanya 1 kasus yang benar-benar bergantung pada kata "verdict" polos (kasus "temuan" polos
    # tidak terpengaruh oleh mutasi ini). Ambang yang terlalu tinggi = uji yang berteriak salah.
    print(f"  [{'OK ' if bocor5 >= 1 else 'GAGAL'}] MUTASI kosakata LAPORAN_RE dilonggarkan terdeteksi "
          f"({bocor5} kasus klasifikasi jadi salah; harus >=1)")
    if bocor5 < 1:
        gagal += 1

    print("UJI pin SHA laporan (T-59 — hijau butuh bukti ia bicara tentang head yang diadili)")
    for nama, teks, head, harap in KASUS_PIN:
        got = pin_verdict(teks, head)
        ok = got == harap
        print(f"  [{'OK ' if ok else 'GAGAL'}] {nama}")
        if not ok:
            print(f"        harapan: {harap} · dapat: {got}")
            gagal += 1
    print("UJI agregasi kanal berkas append-only (T-60 — putaran pertama tidak menutup yang kemudian)")
    for nama, teks, wajib, dilarang in KASUS_BERKAS:
        got = ringkas_berkas(teks)
        ok = (wajib is None or wajib in got) and (dilarang is None or dilarang not in got)
        print(f"  [{'OK ' if ok else 'GAGAL'}] {nama}")
        if not ok:
            print(f"        wajib: {wajib!r} · dilarang: {dilarang!r} · dapat: {got}")
            gagal += 1
    print("UJI kuorum dengan pin SHA (T-59 — laporan tak ter-pin bukan pemenuh kuorum)")
    for nama, pasangan, diharapkan, put, wajib, dilarang in KASUS_PIN_KUORUM:
        got = kuorum_putaran(pasangan, diharapkan, put)
        ok = (wajib is None or wajib in got) and (dilarang is None or dilarang not in got)
        print(f"  [{'OK ' if ok else 'GAGAL'}] {nama}")
        if not ok:
            print(f"        wajib: {wajib!r} · dilarang: {dilarang!r}")
            print("        dapat: " + got.replace("\n", " / "))
            gagal += 1

    total = (len(KASUS) + len(KASUS_GABUNG) + len(KASUS_SLOT) + len(KASUS_GABUNG2)
             + len(KASUS_PUTARAN) + len(KASUS_PIN) + len(KASUS_BERKAS) + len(KASUS_PIN_KUORUM) + 7)
    if gagal:
        print(f"\nHASIL: {gagal} GAGAL dari {total} pemeriksaan")
        return 1
    print(f"\nHASIL: PASS {total}/{total} pemeriksaan "
          f"({len(KASUS)} pembacaan + {len(KASUS_GABUNG) + len(KASUS_GABUNG2)} agregasi "
          f"+ {len(KASUS_SLOT)} klasifikasi slot + {len(KASUS_PUTARAN)} kuorum per putaran "
          f"+ {len(KASUS_PIN)} pin SHA + {len(KASUS_BERKAS)} agregasi berkas "
          f"+ {len(KASUS_PIN_KUORUM)} kuorum berpin + 6 mutasi + 1 smoke kanal)")
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
    ap.add_argument("--putaran", type=int, metavar="R",
                    help="putaran yang hendak diputus untuk laporan kuorum (default: putaran terbaru "
                         "yang ada di kanal)")
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
            return cetak_pr(a.pr, a.harapkan, a.putaran)
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
