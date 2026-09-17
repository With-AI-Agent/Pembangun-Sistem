#!/usr/bin/env python3
"""Validator mandiri folder `sistem-undangan` (W-06/W-07: self-contained).

Tahap sistem ini `kerangka`, jadi yang BISA divalidasi secara jujur baru:
  1. keberadaan berkas wajib folder,
  2. field identitas manifest (Versi / Tahap / Status),
  3. keberadaan 10 baris deklarasi Warisan W-01..W-10 di manifest,
  4. setiap dokumen kerangka menyatakan statusnya dengan tegas (anti-"kerangka yang menyamar jadi jadi").

Alat ini SENGAJA tidak memeriksa isi sistem — isinya belum ada, dan memeriksa sesuatu yang belum ada
akan menghasilkan hijau palsu. Cakupan ini wajib diperluas saat Tahap naik ke `siap-pakai`.

Jalankan:  python3 sistem/sistem-undangan/_sistem/validate_system.py
Exit 0 = lulus, 1 = ada error.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

FOLDER = Path(__file__).resolve().parents[1]
WAJIB = ["00_RENCANA_KERANGKA.md", "SYSTEM_MANIFEST.md"]
DOC_KERANGKA = [
    "01_IDENTITAS_PEMILIK.md", "02_PROFIL_JENIS_ACARA.md", "03_TEMPLATE_DATA_ACARA.md",
    "04_TEMPLATE_BRIEF_UNDANGAN.md", "05_DISCOVERY_DESAIN_PROMPT.md",
    "06_SPESIFIKASI_ASET_DAN_RESOLUSI.md", "07_SPESIFIKASI_CETAK_PREPRESS.md",
    "08_PIPELINE_VIDEO.md", "09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md",
    "10_ARSITEKTUR_WEBSITE_INDUK.md", "11_AMPLOP_DIGITAL.md",
]
WARISAN = [f"W-{i:02d}" for i in range(1, 11)]


def main() -> int:
    err: list[str] = []

    for rel in WAJIB:
        if not (FOLDER / rel).is_file():
            err.append(f"berkas wajib tidak ada: {rel}")
    if err:
        print("\n".join(f"ERROR: {e}" for e in err))
        return 1

    man = (FOLDER / "SYSTEM_MANIFEST.md").read_text(encoding="utf-8")

    if not re.search(r"^\s*-\s*\*\*Versi:\*\*\s*`[^`]+`", man, re.M):
        err.append("manifest: field Versi tidak ada atau tidak ber-backtick")
    m = re.search(r"^\s*-\s*\*\*Tahap:\*\*\s*`?([A-Za-z-]+)`?", man, re.M)
    if not m:
        err.append("manifest: field Tahap tidak ada")
    if not re.search(r"^\s*-\s*\*\*Status:\*\*\s*`[^`]+`", man, re.M):
        err.append("manifest: field Status tidak ada atau tidak ber-backtick")
    if "Dipakai via lmarena" not in man:
        err.append("manifest: bagian Batasan Platform (W-07) tidak ada")

    for w in WARISAN:
        if not re.search(rf"^\|\s*{w}\b", man, re.M):
            err.append(f"manifest: butir warisan {w} tidak punya BARIS deklarasi")

    for rel in DOC_KERANGKA:
        p = FOLDER / rel
        if not p.is_file():
            err.append(f"dokumen kerangka tidak ada: {rel}")
            continue
        txt = p.read_text(encoding="utf-8")
        if "KERANGKA" not in txt:
            err.append(f"{rel}: tidak menyatakan status KERANGKA — dokumen kerangka yang menyamar jadi dokumen jadi")
        if "Log Keputusan" not in txt:
            err.append(f"{rel}: tidak punya bagian Log Keputusan (W-05)")

    if not (FOLDER / "Input-Pengguna").is_dir():
        err.append("folder Input-Pengguna/ tidak ada (mekanisme input milik pemilik)")

    if err:
        print(f"VALIDATOR SISTEM-UNDANGAN: {len(err)} ERROR")
        for e in err:
            print(f"  - {e}")
        return 1
    print(f"VALIDATOR SISTEM-UNDANGAN: PASS  (Tahap: {m.group(1) if m else '?'}, "
          f"{len(WAJIB) + len(DOC_KERANGKA)} berkas diperiksa, {len(WARISAN)} butir warisan terdeklarasi)")
    print("  catatan: cakupan sengaja terbatas — ISI sistem belum ada, jadi belum bisa divalidasi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
