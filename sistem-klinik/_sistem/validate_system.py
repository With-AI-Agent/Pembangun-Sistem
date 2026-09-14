#!/usr/bin/env python3
"""Validator struktur Sistem Klinik — self-contained (stdlib only).

Dijalankan dari root sistem manapun:
    python3 _sistem/validate_system.py          (cwd = folder sistem)
    python3 sistem-klinik/_sistem/validate_system.py   (cwd = root repo meta)

Mengexit 0 bila struktur sistem ini konsisten; 1 + daftar temuan bila tidak.
Aturan yang ditegakkan DI SINI adalah aturan sistem ini sendiri (bukan salinan
validator meta) — supaya folder ini tetap bisa diverifikasi saat berdiri sendiri
(prinsip folder-mandiri; provenance aturan: sistem regresi meta di repo induk).
"""
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

def main():
    errs = []
    check_file_exists(errs)
    check_status_fields(errs)
    check_manifest(errs)
    check_no_meta_operational_refs(errs)
    check_kit(errs)
    if errs:
        print("SYSTEM-KLINIK VALIDATOR: GAGAL")
        for e in errs:
            print(f"- {e}")
        return 1
    print("SYSTEM-KLINIK VALIDATOR: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
