#!/usr/bin/env python3
"""check_manuals.py — penjaring KANDIDAT cacat pegangan pengguna (W-01) + Standar Kelulusan Manual.

STATUS ALAT INI (baca dulu, jangan dilewati)
--------------------------------------------
Alat ini **PENJARING KANDIDAT, BUKAN PEMBERI PUTUSAN**.

Rasio positif palsunya TERUKUR ~65% pada korpus audit 17 Sep 2026 (28 dari 43 kandidat
dicabut setelah diverifikasi manusia). Sumber angka: 
_meta/_internal/AUDIT_MANUAL_DAN_MEKANISME_REVIEW_2026-09-17.md bagian 1 dan 5.

Konsekuensi yang disengaja:
  * exit code **selalu 0** kecuali `--strict` dipakai. Alat ini TIDAK boleh dipasang sebagai
    gerbang yang memblokir, sampai presisinya diukur naik. Memasang penjaring 65%-salah
    sebagai gerbang = cry-wolf, dan itu penyebab utama alat review ditinggalkan.
  * setiap kandidat WAJIB dibaca di sumbernya sebelum dipercaya atau ditindak.
  * yang TIDAK BISA diperiksa alat ini: apakah kalimatnya benar-benar bisa dipahami orang awam.
    Itu lensa #5 QUALITY_ASSURANCE_AND_EVOLUTION.md, dan hanya bisa dinilai manusia
    (Standar Kelulusan Manual Syarat 4).

PERINGATAN OVERFITTING (jangan dilewati saat membaca angka presisi alat ini)
---------------------------------------------------------------------------
Pada korpus 12 pegangan (17 Sep 2026) alat ini menghasilkan **8 kandidat, dan kedelapannya
cocok dengan temuan yang sudah diverifikasi manusia (F-01…F-06) — 0 positif palsu**.

**Angka itu TIDAK BOLEH dikutip sebagai presisi umum.** Alasannya: pola-pola di bawah
(sempitnya MANUSIA_DI_PROMPT, dihapusnya batas panjang K5, pengecualian baris Log Keputusan
dan baris contoh) **disempitkan justru berdasarkan temuan yang sudah diverifikasi di korpus
yang sama**. Mengukur alat pada data yang dipakai untuk menyetelnya = overfitting, dan
menghasilkan angka yang terlihat bagus tetapi tidak berlaku di tempat lain.

**Pengukuran yang sah** = menjalankan alat ini pada korpus yang BELUM dipakai menyetel,
misalnya pegangan `sistem-undangan` saat sistem itu dibangun nanti. Sampai itu dilakukan,
anggap presisi alat ini **tidak diketahui**, dan perlakukan tiap keluarannya sebagai kandidat.

**KORPUS BARU PERTAMA ITU KINI ADA (18 Sep 2026) dan hasilnya dicatat, bukan dilewatkan:**
pegangan `sistem-undangan` (PANDUAN_PENGGUNA.md 331 baris + PROMPT_ENTRI_UNIVERSAL.md 54 baris)
dijalankan lewat --berkas dan menjaring **0 kandidat**. Kontrol positif dijalankan bersamaan:
pegangan sistem-building-aplikasi tetap menjaring **2** kandidat dan pegangan sistem-klinik **4**,
jadi angka 0 itu **bukan** tanda alatnya tidak memeriksa apa-apa.
**Tetapi angka 0 ini TIDAK mengukur presisi maupun recall.** Pada korpus baru, 0 kandidat bisa berarti
"bersih" dan bisa berarti "cacatnya jenis yang tidak dijaring" — alat ini tidak bisa membedakan keduanya
tanpa manusia. Yang tetap berlaku: **presisi alat tidak diketahui**, kelulusan pegangan itu **belum
dinyatakan** (Syarat 4 Standar Kelulusan Manual melarang penulis menilai sendiri), dan penilaian
sesungguhnya menunggu audit lensa kemudahan pakai oleh sesi independen + uji pemakaian nyata oleh pemilik.

Yang diperiksa (semuanya turunan aturan yang sudah ada, bukan aturan baru karangan alat):
  K1  W-01   kedua berkas pegangan ada (PANDUAN_PENGGUNA.md + PROMPT_ENTRI_UNIVERSAL.md)
  K2  W-01   penanda `agent_instruction` ada dalam bentuk yang bisa dibaca mesin (frontmatter)
  K3  W-01   blok prompt pembuka IDENTIK antara 2 berkas (template: "wajib identik", preseden M-15)
  K4  Syarat5 tabel kembar di dalam satu dokumen yang SUDAH MENYIMPANG (bukti: temuan F-01)
  K5  Syarat3 kalimat yang ditujukan ke MANUSIA di dalam blok prompt yang harusnya ke AGENT
  K6  Syarat3 prosa dokumen bersuara orang-pertama AGENT = residu chat (bukti: temuan F-05)
  K7  Syarat2 tabel perintah tanpa kolom penjelas (fungsi / kapan / keluaran / kalau gagal)
  K8  catatan-kualitas prompt menggandeng `_meta/` sehingga tidak portabel (bukti: temuan F-02)
  K9  Syarat1 seksi mekanisme yang isinya hanya rujukan silang, tanpa langkah (bukti: F-03/F-04)

Pemakaian:
  python3 tools/check_manuals.py            # semua pegangan, keluaran ringkas
  python3 tools/check_manuals.py --report   # + bukti per baris
  python3 tools/check_manuals.py --berkas <path.md>   # satu berkas
  python3 tools/check_manuals.py --uji      # uji-diri: fixture harus-merah & harus-hijau
  python3 tools/check_manuals.py --strict   # exit 1 kalau ada kandidat (JANGAN dipakai di gerbang)
"""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- inventaris
# Ditulis EKSPLISIT (inventaris = kewajiban), bukan diturunkan dari glob:
# pegangan yang hilang harus gagal berisik, bukan lenyap dari cakupan.
# (prinsip sama dengan CORE_REQUIRED di checkpoint_core.py)
PEGANGAN = [
    # (label, PANDUAN, PROMPT_ENTRI, folder_sistem_atau_None_untuk_root)
    ("root meta", "PANDUAN_PENGGUNA.md", "PROMPT_ENTRI_UNIVERSAL.md", None),
    ("sistem-building-aplikasi", "sistem/sistem-building-aplikasi/PANDUAN_PENGGUNA.md",
     "sistem/sistem-building-aplikasi/PROMPT_ENTRI_UNIVERSAL.md", "sistem/sistem-building-aplikasi"),
    ("sistem-klinik", "sistem/sistem-klinik/PANDUAN_PENGGUNA.md",
     "sistem/sistem-klinik/PROMPT_ENTRI_UNIVERSAL.md", "sistem/sistem-klinik"),
    ("sistem-konten-kreator", "sistem/sistem-konten-kreator/panduan/PANDUAN_PENGGUNA.md",
     "sistem/sistem-konten-kreator/PROMPT_ENTRI_UNIVERSAL.md", "sistem/sistem-konten-kreator"),
    ("sistem-presentasi", "sistem/sistem-presentasi/PANDUAN_PENGGUNA.md",
     "sistem/sistem-presentasi/PROMPT_ENTRI_UNIVERSAL.md", "sistem/sistem-presentasi"),
    # Ditambahkan 18 Sep 2026 sesudah review independen putaran 2 PR #74 (ketiga hakim, saling
    # bebas): sistem ke-6 SUDAH terdaftar di INDEKS_SISTEM.md dan validator warisan, tetapi TIDAK
    # di inventaris ini - jadi 23 dokumennya belum pernah disisir satu pun pola. Prinsip inventaris
    # ini sendiri ("kewajiban tidak diturunkan dari keberadaan, glob hanya pelengkap") yang
    # dilanggar, persis seperti A-01/A-02 di checkpoint_core pada 17 Sep 2026.
    ("sistem-undangan", "sistem/sistem-undangan/PANDUAN_PENGGUNA.md",
     "sistem/sistem-undangan/PROMPT_ENTRI_UNIVERSAL.md", "sistem/sistem-undangan"),
]

# ---------------------------------------------------------------- pola
# K5: ditujukan ke MANUSIA di dalam blok prompt.
# Sengaja SEMPIT: hanya penanda yang hampir pasti salah arah. Pola luas menghasilkan
# positif palsu massal (terukur: 11 dari 14 kandidat "residu chat" versi awal adalah salah).
MANUSIA_DI_PROMPT = [
    (r"\bsilakan\b|\bsilahkan\b", "kata sopan ke manusia"),
    (r"\bAnda\b", "sapaan formal ke manusia"),
    (r"\bpengguna\b(?! akhir)", "menyebut manusia pihak ketiga"),
]
# K6: suara orang-pertama AGENT di prosa (bukan di dalam blok prompt, bukan di Log Keputusan).
AGENT_ORANG_PERTAMA = [
    r"\baku jujur\b", r"\baku (sudah|putuskan|sarankan|usulkan|kira|rasa)\b",
    r"\bmenurutku\b", r"\busulanku\b", r"\bsaran(ku)\b", r"\bkuputuskan\b",
    r"\bide kamu\b", r"\bkamu benar\b", r"\bkeberatan(mu|kamu)\b",
    r"\bkoreksi (diri|ku)\b", r"\bsebagaimana kamu\b",
]
# kalimat perintah ke AGENT — dipakai untuk menilai apakah sebuah blok memang instruksi
IMPERATIF_AGENT = (r"\b(baca|verifikasi|laporkan|jangan|jalankan|periksa|catat|cek|tulis|cari|"
                   r"tanyakan|tanya|update|perbarui|commit|push|buka|ikuti|lakukan|kerjakan|"
                   r"ambil|buat|pastikan|hentikan|tolong|ulang|bandingkan|hitung|simpan)\b")
# K7: kolom penjelas tabel perintah
KOLOM_PENJELAS = {
    "fungsi/untuk apa": r"(fungsi|untuk\s+apa|guna|kegunaan|apa\s+ini)",
    "kapan dipakai": r"(kapan|saat|waktu|situasi)",
    "keluaran diharapkan": r"(keluaran|hasil|output|expect|muncul)",
    "kalau gagal": r"(gagal|error|masalah|troubleshoot|kalau\s+tidak)",
}
# K9: seksi yang isinya hanya menyuruh pindah dokumen
RUJUK_SILANG = r"^(sama seperti|lihat |rujuk |ikuti |sesuai |detail (ada|di)|aturannya (ada|di)|cara nya (ada|di))"
# baris yang dikecualikan dari K6 (memang tempatnya historis/contoh)
KECUALI_BARIS = re.compile(r"^\s*\|\s*20\d\d-")          # baris tabel Log Keputusan
KECUALI_CONTOH = re.compile(r'^\s*[-*]\s*(Mau|Kalau|Contoh|"|\')')  # contoh kalimat untuk pengguna


def fenced_spans(text: str):
    """Rentang baris (awal, akhir) dari setiap blok ``` ... ``` — 1-based, inklusif."""
    spans, start = [], None
    lines = text.split("\n")
    for i, ln in enumerate(lines, 1):
        if ln.strip().startswith("```"):
            if start is None:
                start = i
            else:
                spans.append((start, i))
                start = None
    if start is not None:
        spans.append((start, len(lines)))
    return spans


def fenced_blocks(text: str):
    out, cur, start = [], [], None
    for i, ln in enumerate(text.split("\n"), 1):
        if ln.strip().startswith("```"):
            if start is None:
                start, cur = i, []
            else:
                out.append((start, "\n".join(cur)))
                start, cur = None, []
        elif start is not None:
            cur.append(ln)
    if start is not None:
        out.append((start, "\n".join(cur)))
    return out


def in_span(n: int, spans) -> bool:
    return any(a <= n <= b for a, b in spans)


def tables(text: str):
    """(baris_header_1based, header, tuple_baris_isi) per tabel markdown."""
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and i + 1 < len(lines) \
                and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            body, j = [], i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                body.append(lines[j].strip())
                j += 1
            out.append((i + 1, lines[i].strip(), tuple(body)))
            i = j
        else:
            i += 1
    return out


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def sections(text: str):
    """(baris_1based, judul, badan) untuk setiap heading ## / ### / ####."""
    out = []
    heads = [(m.start(), text[:m.start()].count("\n") + 1, m.group(0).strip())
             for m in re.finditer(r"^#{2,4}\s+.+$", text, re.M)]
    for k, (pos, ln, head) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(text)
        out.append((ln, head, text[pos:end]))
    return out


# ---------------------------------------------------------------- pemeriksaan
def periksa(label: str, rel_panduan: str, rel_entri: str, folder_sistem):
    """Kembalikan daftar (kode, prioritas, pesan). Prioritas = dugaan; putusan tetap manusia."""
    out = []
    pg, pe = ROOT / rel_panduan, ROOT / rel_entri
    if not pg.exists():
        return [("K1", "P1", f"`{rel_panduan}` TIDAK ADA — W-01 mewajibkan pegangan ada")]
    tp = pg.read_text(encoding="utf-8")
    te = pe.read_text(encoding="utf-8") if pe.exists() else ""
    if not pe.exists():
        out.append(("K1", "P1", f"`{rel_entri}` TIDAK ADA — W-01 mewajibkan 2 berkas"))
    spans = fenced_spans(tp)

    # K2 penanda machine-readable
    if not re.match(r"^---\n(.*\n)*?agent_instruction:", tp):
        if "agent_instruction" in tp:
            out.append(("K2", "P3", "`agent_instruction` ada tapi BUKAN di frontmatter — tidak bisa digrep andal"))
        else:
            out.append(("K2", "P2", "penanda `agent_instruction: IGNORE for execution — USER GUIDE ONLY` TIDAK ADA "
                                    "(template §1) — dokumen bisa diperlakukan agent sebagai instruksi eksekusi"))

    # K3 identitas blok prompt antar 2 berkas
    if te:
        be = [norm(b) for _, b in fenced_blocks(te) if len(b.strip()) > 100]
        bp = [norm(b) for _, b in fenced_blocks(tp) if len(b.strip()) > 100]
        if be and bp and not (set(be) & set(bp)):
            out.append(("K3", "P1", "blok prompt di PROMPT_ENTRI_UNIVERSAL **TIDAK IDENTIK** dengan yang di "
                                    "PANDUAN_PENGGUNA — template: 'wajib identik'; selisih diam-diam = temuan audit (M-15)"))

    # K4 tabel kembar yang menyimpang
    tb = tables(tp)
    for a in range(len(tb)):
        for b in range(a + 1, len(tb)):
            la, ha, ba = tb[a]
            lb, hb, bb = tb[b]
            if ha != hb or not ba or not bb or ba == bb:
                continue
            sa, sb = set(ba), set(bb)
            ov = len(sa & sb)
            if ov >= 2 and ov >= min(len(sa), len(sb)) - 2:
                out.append(("K4", "P1", f"**tabel kembar SUDAH MENYIMPANG**: baris {la} dan {lb} berheader sama "
                                        f"`{ha[:46]}` — {ov} baris sama, {len(sa - sb)} hanya di pertama, "
                                        f"{len(sb - sa)} hanya di kedua (Syarat 5; preseden F-01)"))

    # K5 manusia di dalam blok prompt.
    # TANPA batas panjang: pola di MANUSIA_DI_PROMPT sengaja sempit (hanya penanda yang
    # hampir pasti salah arah), jadi blok pendek pun sah diperiksa. Batas panjang 60 karakter
    # pada versi pertama alat ini membuat prompt pendek yang salah arah LOLOS — tertangkap
    # oleh uji-dirinya sendiri pada hari yang sama (fixture MERAH tidak memicu K5).
    for st, isi in fenced_blocks(tp) + fenced_blocks(te):
        if len(isi.strip()) < 20:
            continue
        for pat, lbl in MANUSIA_DI_PROMPT:
            for m in re.finditer(pat, isi):
                frag = norm(isi[max(0, m.start() - 40):m.end() + 40])
                out.append(("K5", "P2", f"blok mulai baris {st}: **{lbl}** di dalam prompt — `…{frag}…` "
                                        f"(Syarat 3.1: prompt wajib berkalimat perintah ke agent)"))

    # K6 prosa bersuara agent
    for i, ln in enumerate(tp.split("\n"), 1):
        if in_span(i, spans) or KECUALI_BARIS.match(ln) or KECUALI_CONTOH.match(ln):
            continue
        for pat in AGENT_ORANG_PERTAMA:
            m = re.search(pat, ln, re.I)
            if m:
                out.append(("K6", "P2", f"baris {i}: prosa bersuara **agent orang-pertama** `{m.group(0)}` — "
                                        f"residu chat (Syarat 3.2; preseden F-05): `{ln.strip()[:110]}`"))
                break

    # K7 tabel perintah tanpa kolom penjelas
    for ln, hdr, _ in tb:
        h = hdr.lower()
        if not re.search(r"(perintah|command|alat|tool|skrip|script)", h):
            continue
        kurang = [k for k, p2 in KOLOM_PENJELAS.items() if not re.search(p2, h)]
        if len(kurang) >= 3:
            out.append(("K7", "P2", f"tabel baris {ln} `{hdr[:70]}` — kolom penjelas HILANG: {', '.join(kurang)} "
                                    f"(Syarat 2: tabel perintah yang hanya berisi perintah tidak bisa dipakai)"))

    # K8 portabilitas prompt (hanya untuk folder sistem)
    if folder_sistem:
        for st, isi in fenced_blocks(tp) + fenced_blocks(te):
            for m in re.finditer(r"_meta/[\w\-./]+", isi):
                out.append(("K8", "P2", f"prompt mulai baris {st} menggandeng `{m.group(0)}` — TIDAK PORTABEL; "
                                        f"template: prompt wajib path relatif folder sistem supaya benar saat "
                                        f"sistem berdiri sebagai repo mandiri (preseden F-02)"))

    # K9 seksi yang isinya hanya rujukan silang
    for ln, head, body in sections(tp):
        b = body.split("\n", 1)[-1].strip() if "\n" in body else ""
        if len(b) > 420 or "|" in b or "```" in b:
            continue
        if re.match(RUJUK_SILANG, b, re.I) and not re.search(r"(\n\s*\d+\.|langkah|kalau gagal|jika gagal)", b, re.I):
            out.append(("K9", "P2", f"seksi baris {ln} `{head[:58]}` — isinya **hanya rujukan silang** "
                                    f"(`{b[:88]}…`): pembaca awam harus loncat dokumen, tidak ada langkah "
                                    f"(Syarat 1 bidang 3; preseden F-03/F-04)"))
    return out


# ---------------------------------------------------------------- uji-diri
FIX_MERAH = """---
agent_instruction: IGNORE for execution
---
# Uji

## 1. Pembuka
> **Aku jujur:** ide kamu ini benar.

## 2. Situasi
| Situasi | Yang terjadi |
|---|---|
| A | a1 |
| B | b1 |
| C | c1 |

## 3. Situasi lagi
| Situasi | Yang terjadi |
|---|---|
| A | a1 |
| B | b1 |

## 4. Cara review
Sama seperti repo induk: buka PR lalu merge.

## 5. Perintah
| Perintah | Contoh |
|---|---|
| x | y |

```
Silakan tempel prompt ini, Anda akan melihat hasilnya.
```
"""
FIX_HIJAU = """---
agent_instruction: IGNORE for execution — USER GUIDE ONLY
---
# Uji

## 1. Pembuka
Pegangan ini menjelaskan cara memakai sistem.

## 2. Cara review & merge
1. Agent membuka PR.
2. Pengguna meninjau berkas yang berubah.
3. Kalau sudah yakin, tekan tombol merge.
4. Kalau gagal: periksa apakah semua sudah ter-push.

```
Baca START_DI_SINI.md, verifikasi branch, laporkan keadaan, jangan eksekusi apa pun dulu.
```
"""


def uji_diri() -> int:
    gagal = []
    merah = periksa("fixture-merah", "<memori>", "<tidak ada>", None)
    # jalankan langsung pada teks fixture
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        dp = Path(d)
        for nama, isi, kode_wajib in (("m.md", FIX_MERAH, {"K4", "K5", "K6", "K7", "K9"}),
                                      ("h.md", FIX_HIJAU, set())):
            f = dp / nama
            f.write_text(isi, encoding="utf-8")
            global ROOT
            lama = ROOT
            ROOT = dp
            try:
                if nama == "m.md":
                    got = {k for k, _, _ in periksa("m", "m.md", "tidak-ada.md", "sistem/uji")}
                else:
                    got = {k for k, _, _ in periksa("h", "h.md", "tidak-ada.md", None)}
            finally:
                ROOT = lama
            if nama == "m.md":
                for k in sorted(kode_wajib - got):
                    gagal.append(f"FIXTURE MERAH: kode {k} HARUS terdeteksi tapi tidak")
            else:
                for k in sorted(got - {"K1", "K3"}):
                    gagal.append(f"FIXTURE HIJAU: kode {k} muncul padahal tidak boleh (positif palsu)")
    print("UJI-DIRI check_manuals.py")
    if gagal:
        for g in gagal:
            print("  ❌", g)
        print("HASIL: GAGAL")
        return 1
    print("  ✅ fixture MERAH memicu K4 K5 K6 K7 K9")
    print("  ✅ fixture HIJAU tidak memicu K4..K9 (K1/K3 dikecualikan: fixture memang 1 berkas)")
    print("HASIL: LULUS")
    return 0


# ---------------------------------------------------------------- utama
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", action="store_true", help="cetak bukti per baris (default: ringkas)")
    ap.add_argument("--berkas", metavar="PATH", help="periksa satu berkas saja")
    ap.add_argument("--uji", action="store_true", help="uji-diri dengan fixture harus-merah & harus-hijau")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 kalau ada kandidat — JANGAN dipakai sebagai gerbang (rasio positif palsu ~65%%)")
    a = ap.parse_args()

    if a.uji:
        return uji_diri()

    print("CHECK MANUALS — penjaring KANDIDAT cacat pegangan pengguna (W-01 + Standar Kelulusan Manual)")
    print("⚠ ALAT INI BUKAN PEMBERI PUTUSAN. Rasio positif palsu terukur ~65% (28 dari 43 kandidat audit 17 Sep")
    print("  dicabut setelah diverifikasi). SETIAP kandidat wajib dibaca di sumbernya sebelum dipercaya/ditindak.")
    print("  Yang tidak bisa diperiksa di sini: apakah kalimatnya benar-benar paham-awam (lensa #5, hanya manusia).\n")

    total = 0
    hitung = {}
    for label, rp, re_, fs in PEGANGAN:
        if a.berkas and a.berkas not in rp and a.berkas not in re_:
            continue
        temuan = periksa(label, rp, re_, fs)
        total += len(temuan)
        if not temuan:
            print(f"== {label}: 0 kandidat")
            continue
        print(f"== {label}: {len(temuan)} kandidat")
        for kode, pri, pesan in temuan:
            hitung[kode] = hitung.get(kode, 0) + 1
            if a.report:
                print(f"   [{kode}/{pri}] {pesan}")
            else:
                print(f"   [{kode}/{pri}] {pesan[:118]}{'…' if len(pesan) > 118 else ''}")
    print(f"\nTOTAL KANDIDAT: {total}   per kode: {hitung if hitung else '{}'}")
    print("LANGKAH WAJIB BERIKUTNYA: baca tiap kandidat di sumbernya, putuskan nyata / positif palsu,")
    print("baru tindak. Laporan audit 17 Sep adalah contoh cara melakukannya (bagian 5 = yang dicabut).")
    if a.strict and total:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
