#!/usr/bin/env python3
"""Validator struktur Sistem Building Aplikasi — self-contained (stdlib only).

Dijalankan dari root sistem manapun:
    python3 _sistem/validate_system.py          (cwd = folder sistem)
    python3 sistem/sistem-building-aplikasi/_sistem/validate_system.py   (cwd = root repo meta)

Mengexit 0 bila struktur sistem ini konsisten; 1 + daftar temuan bila tidak.
Aturan yang ditegakkan DI SINI adalah aturan sistem ini sendiri — supaya folder ini tetap bisa diverifikasi saat berdiri sendiri (prinsip folder-mandiri; provenance aturan: sistem regresi meta di repo induk).
"""
import re
import sys
from pathlib import Path

SYS_DIR = Path(__file__).resolve().parent.parent

REQUIRED = [
    "START_DI_SINI.md",
    "SYSTEM_MANIFEST.md",
    "STATUS.md",
    "PANDUAN_PENGGUNA.md",
    "PROMPT_ENTRI_UNIVERSAL.md",
    "10_LOG_SESI.md",
    "AGENT_SYSTEM.md",
    "ACCEPTANCE_TESTS.md",
    "PROFIL_PENGGUNA.md",
]

def check_file_exists(errs):
    for rel in REQUIRED:
        if not (SYS_DIR / rel).is_file():
            errs.append(f"berkas wajib hilang: {rel}")

def check_status_fields(errs):
    """Field deterministik checkpoint (pola kontrak warisan W-03): tepat satu kemuncilan nilai exact, plus Waktu pembaruan bertanggal."""
    for status in sorted(SYS_DIR.rglob("STATUS.md")):
        text = status.read_text(encoding="utf-8")
        n = len(re.findall(r"\*\*Pekerjaan belum tersimpan:\*\*\s*Tidak ada\s*$", text, re.MULTILINE))
        if n != 1:
            errs.append(f"{status.relative_to(SYS_DIR)}: field 'Pekerjaan belum tersimpan: Tidak ada' harus muncul tepat 1x (exact, akhir baris); ditemukan {n}")
        if not re.search(r"\*\*Waktu pembaruan:\*\*\s*\d{4}-\d{2}-\d{2}\s+—\s+\S", text):
            errs.append(f"{status.relative_to(SYS_DIR)}: field 'Waktu pembaruan' harus ada, format 'YYYY-MM-DD — <peristiwa>'")

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
    if not re.search(r"^- \*\*Versi:\*\* `?0\.", text, re.MULTILINE):
        errs.append("SYSTEM_MANIFEST.md: baris Versi tidak ada atau tidak bisa di-parse")

def check_no_meta_operational_refs(errs):
    """Dokumen AKTIF sistem (bukan 00_RENCANA_KERANGKA = riwayat) tidak boleh merujuk _meta/ atau tools/ dengan backtick tanpa salinan berlabel."""
    for doc in sorted(SYS_DIR.rglob("*.md")):
        # AGENT_SYSTEM.md is legacy instruction; its refs to /docs and PROJECT_STATE are internal, not _meta — exempt
        # but check anyway
        if doc.name.startswith("00_RENCANA"):
            continue
        rel = doc.relative_to(SYS_DIR)
        text = doc.read_text(encoding="utf-8")
        for ref in re.findall(r"`((?:_meta|tools)/[^`\s]+)`", text):
            salinan = list((SYS_DIR / "_salinan-meta").glob(Path(ref).name)) if (SYS_DIR / "_salinan-meta").is_dir() else []
            if not salinan:
                errs.append(f"{rel}: rujukan ber-backtick `{ref}` butuh salinan berlabel di _salinan-meta/ (atau tulis tanpa backtick sebagai provenance)")

def check_pegangan(errs):
    pu = SYS_DIR / "PANDUAN_PENGGUNA.md"
    pe = SYS_DIR / "PROMPT_ENTRI_UNIVERSAL.md"
    if pu.is_file() and pe.is_file():
        pu_text = pu.read_text(encoding="utf-8")
        pe_text = pe.read_text(encoding="utf-8")
        # extract first code fence block from each
        def first_block(t):
            m = re.search(r"```\n(.*?)\n```", t, re.DOTALL)
            return m.group(1).strip() if m else ""
        b1 = first_block(pu_text)
        b2 = first_block(pe_text)
        if b1 and b2 and b1 != b2:
            errs.append("PANDUAN_PENGGUNA.md dan PROMPT_ENTRI_UNIVERSAL.md: blok prompt harus identik (cek 2-file)")
        if "PROMPT_ENTRI_UNIVERSAL" not in pu_text:
            errs.append("PANDUAN_PENGGUNA.md: tidak menyebut PROMPT_ENTRI_UNIVERSAL")
        if "Prompt Penutup" not in pu_text:
            errs.append("PANDUAN_PENGGUNA.md: tidak ada Prompt Penutup")

def main():
    errs = []
    check_file_exists(errs)
    check_status_fields(errs)
    check_manifest(errs)
    check_no_meta_operational_refs(errs)
    check_pegangan(errs)
    if errs:
        print("SYSTEM-BUILDING-APLIKASI VALIDATOR: GAGAL")
        for e in errs:
            print(f"- {e}")
        return 1
    print("SYSTEM-BUILDING-APLIKASI VALIDATOR: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
