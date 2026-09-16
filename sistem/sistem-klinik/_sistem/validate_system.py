#!/usr/bin/env python3
"""Validator struktur Sistem Klinik — self-contained (stdlib only).

Dijalankan dari root sistem manapun:
    python3 _sistem/validate_system.py          (cwd = folder sistem)
    python3 sistem/sistem-klinik/_sistem/validate_system.py   (cwd = root repo meta)

Mengexit 0 bila struktur sistem ini konsisten; 1 + daftar temuan bila tidak.
Aturan yang ditegakkan DI SINI adalah aturan sistem ini sendiri (bukan salinan
validator meta) — supaya folder ini tetap bisa diverifikasi saat berdiri sendiri
(prinsip folder-mandiri; provenance aturan: sistem regresi meta di repo induk).
"""
import hashlib
import re
import sys
from pathlib import Path

SYS_DIR = Path(__file__).resolve().parent.parent

REQUIRED = [
    "START_DI_SINI.md",
    "SYSTEM_MANIFEST.md",
    "00_RENCANA_KERANGKA.md",
    "PANDUAN_PENGGUNA.md",
    "PROMPT_ENTRI_UNIVERSAL.md",
    "STATUS.md",
    "10_LOG_SESI.md",
]

def check_file_exists(errs):
    for rel in REQUIRED:
        if not (SYS_DIR / rel).is_file():
            errs.append(f"berkas wajib hilang: {rel}")

def check_status_fields(errs):
    """Field deterministik checkpoint (pola kontrak warisan W-03): tepat satu
    kemuncilan nilai exact, plus Waktu pembaruan bertanggal."""
    for status in sorted(SYS_DIR.rglob("STATUS.md")):
        if "_template" in status.parts:
            continue
        text = status.read_text(encoding="utf-8")
        n = len(re.findall(r"\*\*Pekerjaan belum tersimpan:\*\*\s*Tidak ada\s*$",
                           text, re.MULTILINE))
        if n != 1:
            errs.append(f"{status.relative_to(SYS_DIR)}: field "
                        "'Pekerjaan belum tersimpan: Tidak ada' harus muncul "
                        f"tepat 1x (exact, akhir baris); ditemukan {n}")
        if not re.search(r"\*\*Waktu pembaruan:\*\*\s*\d{4}-\d{2}-\d{2}\s+—\s+\S", text):
            errs.append(f"{status.relative_to(SYS_DIR)}: field 'Waktu pembaruan' "
                        "harus ada, format 'YYYY-MM-DD — <peristiwa>'")

def check_manifest(errs):
    m = SYS_DIR / "SYSTEM_MANIFEST.md"
    if not m.is_file():
        return
    text = m.read_text(encoding="utf-8")
    if "Dipakai via lmarena" not in text:
        errs.append("SYSTEM_MANIFEST.md tanpa bagian 'Dipakai via lmarena?' (fakta platform)")
    for w in range(1, 10):
        if f"W-0{w}" not in text:
            errs.append(f"SYSTEM_MANIFEST.md tidak menyebut butir Warisan W-0{w}")
    if not re.search(r"^- \*\*Tahap:\*\* `?(kerangka|siap-pakai)`?", text, re.MULTILINE):
        errs.append("SYSTEM_MANIFEST.md: field 'Tahap' wajib terbaca (kerangka|siap-pakai)")

def check_no_meta_operational_refs(errs):
    """Dokumen AKTIF sistem (bukan 00_RENCANA_KERANGKA = riwayat) tidak boleh
    merujuk _meta/ atau tools/ dengan backtick tanpa salinan berlabel di
    dalam folder — rujukan operasional wajib hidup di sini."""
    forbidden = ("_meta/", "tools/")
    for doc in sorted(SYS_DIR.rglob("*.md")):
        if doc.name == "00_RENCANA_KERANGKA.md":
            continue  # rencana kerangka = dokumen riwayat/provenance
        rel = doc.relative_to(SYS_DIR)
        text = doc.read_text(encoding="utf-8")
        for ref in re.findall(r"`((?:_meta|tools)/[^`\s]+)`", text):
            salinan = list((SYS_DIR / "_salinan-meta").glob(Path(ref).name)) if (SYS_DIR / "_salinan-meta").is_dir() else []
            if not salinan:
                errs.append(f"{rel}: rujukan ber-backtick `{ref}` butuh salinan berlabel di _salinan-meta/ (atau tulis tanpa backtick sebagai provenance)")

def check_kit(errs):
    """Bila folder kit/ sudah dirakit: isi minimal + label asal-usul per
    dokumen turunan wajib ada (ditegakkan dari sistem ini sendiri, bukan
    dari alat meta)."""
    kit = SYS_DIR / "kit"
    if not kit.is_dir():
        return  # kit dibangun bertahap; sebelum ada, tidak ada yang ditegakkan
    for needed in ("PROMPT-ENTRI-KIT.md", "PROMPT-PENUTUP-KIT.md", "VERSI.txt"):
        if not (kit / needed).is_file():
            errs.append(f"kit/ belum mandiri: {needed} hilang")
    aturan = kit / "aturan"
    if aturan.is_dir():
        for f in sorted(aturan.glob("*.md")):
            lines = f.read_text(encoding="utf-8").splitlines()
            if not lines or not lines[0].startswith("> Sumber:"):
                errs.append(f"kit/aturan/{f.name}: baris pertama wajib label "
                            "'> Sumber: <berkas master> sha <40> tanggal <YYYY-MM-DD> versi-kit <x.y.z>'")

# Aturan master yang wajib punya turunan di kit/aturan/ (06_RITME_KIT §1).
ATURAN_KIT = ("01_ALUR_RUN.md", "02_KATALOG_CACAT.md", "03_KEBIJAKAN_LEBUR.md",
              "04_KONTRAK_TANAMAN.md", "05_TAWARAN_KAPABILITAS.md", "06_RITME_KIT.md")
STAMP = re.compile(r"^> Sumber: (\S+) sha ([0-9a-f]{40}) tanggal (\d{4}-\d{2}-\d{2}) versi-kit (\S+)$")


def _blob_sha(path):
    """Blob SHA git dihitung TANPA memanggil git: sha1("blob <len>\0" + isi) — stdlib saja,
    supaya validator ini tetap portabel (panggung rawat inap/suntik bisa tanpa git)."""
    b = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def check_kit_segarkan(errs):
    """Kit TIDAK BOLEH BASI terhadap master — 06_RITME_KIT §2: "Jika aturan master `_sistem/`
    berubah, pemilik atau agent wajib mensinkronisasi ke `kit/` sebelum melakukan PR rilis";
    "Cek Kit Basi: ... Jika basi, build harus *fail-closed*".

    Sampai 2026-09-16 aturan itu hanya ditegakkan AT-KL-02 sebagai **prosedur manual**, sehingga
    panen C-07 (run ke-2 Building Aplikasi, PR #63) menyunting master katalog tanpa sync dan
    TIDAK ADA gerbang yang menyala — persis pola yang dikatalogkan C-07 (aturan tanpa gerbang)
    dan F-8 (hijau karena tidak memeriksa apa pun). Yang ditegakkan cek ini: kelengkapan 6
    turunan, sha blob master vs sha di stamp, isi turunan identik master, versi-kit stamp vs
    kit/VERSI.txt, dan kit/VERSI.txt vs field Versi manifest.
    """
    kit = SYS_DIR / "kit"
    if not kit.is_dir():
        return  # panggung rawat inap / target suntik: kit tidak ada di pohon (K-11)
    versi_file = kit / "VERSI.txt"
    versi = versi_file.read_text(encoding="utf-8").strip() if versi_file.is_file() else None
    if versi is None:
        errs.append("kit/VERSI.txt tidak ada — versi kit tidak terbaca (06_RITME_KIT §2)")
    man = SYS_DIR / "SYSTEM_MANIFEST.md"
    if man.is_file() and versi:
        m = re.search(r"^- \*\*Versi:\*\* `?([0-9]+(?:\.[0-9]+)*)`?", man.read_text(encoding="utf-8"), re.MULTILINE)
        if not m:
            errs.append("SYSTEM_MANIFEST.md: field Versi tidak terbaca — kesegaran kit tidak bisa dibandingkan")
        elif m.group(1) != versi:
            errs.append(f"kit BASI terhadap manifest: kit/VERSI.txt = {versi} tetapi SYSTEM_MANIFEST.md Versi = {m.group(1)} "
                        "(06_RITME_KIT §2: kit tidak boleh tertinggal manifest — sinkronkan kit lalu samakan versinya)")
    for nama in ATURAN_KIT:
        turunan = kit / "aturan" / nama
        master = SYS_DIR / "_sistem" / nama
        if not master.is_file():
            errs.append(f"_sistem/{nama}: berkas master tidak ada — kit/aturan/{nama} tidak punya sumber")
            continue
        if not turunan.is_file():
            errs.append(f"kit/aturan/{nama} hilang — setiap aturan master wajib punya turunan berstempel (06_RITME_KIT §1)")
            continue
        teks = turunan.read_text(encoding="utf-8")
        baris = teks.splitlines()
        m = STAMP.match(baris[0]) if baris else None
        if not m:
            continue  # bentuk stamp sudah ditegakkan check_kit()
        sumber, sha, tanggal, vk = m.groups()
        if sumber != f"_sistem/{nama}":
            errs.append(f"kit/aturan/{nama}: stamp menunjuk sumber {sumber} — seharusnya _sistem/{nama}")
        nyata = _blob_sha(master)
        if sha != nyata:
            errs.append(f"kit/aturan/{nama} BASI: sha di stamp {sha[:12]} != blob sha master saat ini {nyata[:12]} "
                        f"(stamp tanggal {tanggal}, master sudah berubah; 06_RITME_KIT §2 wajib sync sebelum PR rilis)")
        if versi and vk != versi:
            errs.append(f"kit/aturan/{nama}: stamp versi-kit {vk} != kit/VERSI.txt {versi} — satu rilis kit = satu versi")
        if teks != f"{baris[0]}\n\n" + master.read_text(encoding="utf-8"):
            errs.append(f"kit/aturan/{nama}: isi turunan tidak identik dengan master (bentuk wajib: stamp + baris kosong + isi master verbatim)")


def main():
    errs = []
    check_file_exists(errs)
    check_status_fields(errs)
    check_manifest(errs)
    check_no_meta_operational_refs(errs)
    check_kit(errs)
    check_kit_segarkan(errs)
    if errs:
        print("SYSTEM-KLINIK VALIDATOR: GAGAL")
        for e in errs:
            print(f"- {e}")
        return 1
    print("SYSTEM-KLINIK VALIDATOR: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
