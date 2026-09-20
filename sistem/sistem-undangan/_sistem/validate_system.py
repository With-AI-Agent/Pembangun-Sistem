#!/usr/bin/env python3
"""Validator mandiri folder `sistem-undangan` (W-06/W-07: self-contained).

Cakupan — diperluas 2026-09-20 sesuai **T-69** (commit pengisian dokumen pertama; alasan diperluas
ditulis alat ini sendiri pada tahap kerangka: "Cakupan ini wajib diperluas saat Tahap naik"):
  1. keberadaan berkas wajib folder,
  2. field identitas manifest (Versi / Tahap / Status),
  3. keberadaan 10 baris deklarasi Warisan W-01..W-10 di manifest,
  4. setiap dokumen KERANGKA menyatakan statusnya dengan tegas (anti-"kerangka yang menyamar jadi jadi"),
  5. (T-69) setiap dokumen yang SUDAH TERISI: **banner kerangka TIDAK BOLEH ada** (anti-"dokumen yang
     membantah dirinya sendiri" — jebakan T-69: pengisian pertama tanpa perluasan ini membuat alat MERAH),
     bagian **Log Keputusan** ada + minimal satu baris keputusan bertanggal, dan bagian-bagian **isi wajib** ada,
  6. (T-69) konsistensi manifest: Tahap `kerangka` tidak boleh berlaku lagi kalau sudah ada dokumen terisi.

Jalankan:  python3 sistem/sistem-undangan/_sistem/validate_system.py
Exit 0 = lulus, 1 = ada error.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

FOLDER = Path(__file__).resolve().parents[1]
# W-01 (pegangan pengguna 2 file) DITEGAKKAN DI SINI, bukan hanya di validator level repo.
# Alasannya: folder sistem ini harus tetap berdiri sendiri waktu diunduh jadi repo tersendiri,
# dan di keadaan itu tidak ada validator level repo yang menegur kalau pegangannya hilang.
WAJIB = ["00_RENCANA_KERANGKA.md", "SYSTEM_MANIFEST.md",
         "PANDUAN_PENGGUNA.md", "PROMPT_ENTRI_UNIVERSAL.md"]

BANNER_KERANGKA = "STATUS: KERANGKA — BELUM ADA ISI"

# (T-69) daftar menyusut: 01_IDENTITAS_PEMILIK.md pindah ke DOC_ISI (diisi 2026-09-20, Discovery 01).
# (mekanika prompt 02) 2026-09-20: 02_PROFIL_JENIS_ACARA.md pindah ke DOC_ISI (diisi, Discovery 02 —
# jenis acara pertama: pernikahan). Daftar ini WAJIB menyusut lagi setiap pengisian dokumen berikutnya.
DOC_KERANGKA = [
    "03_TEMPLATE_DATA_ACARA.md", "04_TEMPLATE_BRIEF_UNDANGAN.md",
    "05_DISCOVERY_DESAIN_PROMPT.md", "06_SPESIFIKASI_ASET_DAN_RESOLUSI.md",
    "07_SPESIFIKASI_CETAK_PREPRESS.md", "08_PIPELINE_VIDEO.md", "09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md",
    "10_ARSITEKTUR_WEBSITE_INDUK.md", "11_AMPLOP_DIGITAL.md",
]

# (T-69) dokumen yang sudah terisi + bagian isi wajibnya (anti-"isi yang kosong/kurang tanpa tercatat").
DOC_ISI = ["01_IDENTITAS_PEMILIK.md", "02_PROFIL_JENIS_ACARA.md"]
ISI_WAJIB: dict[str, list[str]] = {
    "01_IDENTITAS_PEMILIK.md": [
        "Merek / Nama", "Font Default", "Palet Default", "Gaya Ornament", "Nada Bahasa",
        "Harga & Masa Aktif", "Amplop Digital", "Serah Terima", "Skill / Plugin",
        "Batasan Mutlak", "Konsekuensi Perubahan L1", "Log Keputusan",
    ],
    "02_PROFIL_JENIS_ACARA.md": [
        "Pernikahan", "Cakupan dan Prinsip Umum", "Bentuk Pengesahan dan Kata Baku",
        "Etika Penulisan dan Titik Sensitif", "Matriks Variasi", "Daftar Field Default",
        "Konvensi Desain dan Pantangan", "Katalog model", "Hal yang Selalu Konsisten",
        "Waktu dan Siklus", "Bawaan L2 vs Per-Undangan", "Catatan untuk L3", "Log Keputusan",
    ],
}

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

    # (T-69) pemeriksaan dokumen yang SUDAH TERISI
    terisi: list[str] = []
    for rel in DOC_ISI:
        p = FOLDER / rel
        if not p.is_file():
            err.append(f"dokumen terisi tidak ada: {rel}")
            continue
        txt = p.read_text(encoding="utf-8")
        terisi.append(rel)
        if BANNER_KERANGKA in txt:
            err.append(f"{rel}: banner kerangka masih ada — dokumen yang membantah dirinya sendiri (T-69: banner wajib dicabut saat isi)")
        if "Log Keputusan" not in txt:
            err.append(f"{rel}: tidak punya bagian Log Keputusan (W-05)")
        elif not re.search(r"^\|\s*20\d\d-", txt, re.M):
            err.append(f"{rel}: Log Keputusan masih kosong (hanya baris placeholder) — isi tanpa keputusan tercatat")
        for kw in ISI_WAJIB.get(rel, []):
            if kw not in txt:
                err.append(f"{rel}: bagian isi wajib tidak ada: {kw}")

    # (T-69) konsistensi Tahap manifest dengan keadaan isi
    if terisi and m and m.group(1) == "kerangka":
        err.append(
            f"manifest: Tahap masih `kerangka` padahal {len(terisi)} dokumen terisi "
            f"({', '.join(terisi)}) — inkonsisten (T-69: Tahap/Versi manifest wajib diperbarui di commit yang sama)"
        )

    if not (FOLDER / "Input-Pengguna").is_dir():
        err.append("folder Input-Pengguna/ tidak ada (mekanisme input milik pemilik)")

    if err:
        print(f"VALIDATOR SISTEM-UNDANGAN: {len(err)} ERROR")
        for e in err:
            print(f"  - {e}")
        return 1
    print(f"VALIDATOR SISTEM-UNDANGAN: PASS  (Tahap: {m.group(1) if m else '?'}, "
          f"{len(WAJIB)} berkas wajib, {len(DOC_KERANGKA)} kerangka, {len(terisi)} terisi, {len(WARISAN)} butir warisan terdeklarasi)")
    print("  catatan T-69: cakupan mencakup dokumen terisi — banner kerangka, Log Keputusan bertanggal, bagian isi wajib, konsistensi Tahap manifest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
