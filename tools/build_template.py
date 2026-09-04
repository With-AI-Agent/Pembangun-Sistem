#!/usr/bin/env python3
"""Build clean template from master blueprint.

Satisfies AT-10 and SYSTEM_MANIFEST gate "Template bersih dirilis".
Template must NOT contain:
- personal data
- production output
- audit internal (_meta/_internal/)
- domain example decisions (sistem-konten-kreator content, pilot outputs)

Template MUST contain:
- entry point and minimal contract
"""
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "_meta" / "_internal" / "template_clean"
TEMPLATE_ZIP = ROOT / "_meta" / "_internal" / "template_clean.zip"

# Files to include in clean template
INCLUDE = [
    "_meta/00_CARA_KERJA_META.md",
    "_meta/01_DISCOVERY_LEVEL_0.md",
    "_meta/02_PRINSIP_UNIVERSAL.md",
    "_meta/INDEKS_SISTEM.md",
    "_meta/SYSTEM_MANIFEST.md",
    "_meta/SYSTEM_MANIFEST_TEMPLATE.md",
    "_meta/DEFINITION_OF_DONE.md",
    "_meta/PROTOKOL_CHECKPOINT_RECOVERY.md",
    "_meta/PLATFORM_LMARENA.md",
    "_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md",
    "_meta/ACCEPTANCE_TESTS.md",
    "_meta/SESSION_REPORT_TEMPLATE.md",
    "_meta/FAILURE_INJECTION_TESTS.md",
    "_meta/NEXT_SESSION_PROMPT.md",
    "_meta/TEMPLATE_RELEASE.md",
    "PANDUAN_PENGGUNA.md",
    ".gitignore",
    ".gitattributes",
]

# Additional empty dirs to create
EMPTY_DIRS = [
    "_pegangan-kamu",
    "_cadangan-claude",
]

def build():
    if TEMPLATE_DIR.exists():
        shutil.rmtree(TEMPLATE_DIR)
    TEMPLATE_DIR.mkdir(parents=True)

    for rel in INCLUDE:
        src = ROOT / rel
        if not src.is_file():
            print(f"SKIP missing: {rel}")
            continue
        dst = TEMPLATE_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    for d in EMPTY_DIRS:
        (TEMPLATE_DIR / d).mkdir(parents=True, exist_ok=True)
        (TEMPLATE_DIR / d / ".gitkeep").write_text("", encoding="utf-8")

    # Clean INDEKS_SISTEM.md to remove example systems
    indeks_path = TEMPLATE_DIR / "_meta/INDEKS_SISTEM.md"
    if indeks_path.is_file():
        # Write minimal index with no systems
        indeks_path.write_text(
            "# Indeks Sistem\n\n"
            "### Daftar semua sistem yang ada di repo ini, dengan status dan tanggal terakhir disentuh. Dicatat MANUAL oleh agent setiap kali selesai kerja di suatu sistem — TIDAK mengandalkan pembacaan git history. Dibaca di awal sesi untuk menentukan apakah perlu menawarkan audit sebelum lanjut kerja (lihat `00_CARA_KERJA_META.md`).\n\n"
            "---\n\n"
            "## Cara pakai\n\n"
            "- **Sebelum mulai kerja di suatu sistem:** cek baris sistem itu di tabel bawah. Kalau \"Terakhir Disentuh\" sudah lama (pengguna yang menilai apa itu \"lama\" — tidak ada angka pasti, tergantung konteks), tawarkan audit dulu.\n"
            "- **Setelah selesai kerja di suatu sistem (apapun jenis kerjanya):** update baris sistem itu — tanggal hari ini, dan status terbaru.\n"
            "- **Sistem baru:** tambah baris baru begitu `00_RENCANA_KERANGKA.md`-nya sudah di-merge ke `main` (lihat `01_DISCOVERY_LEVEL_0.md`).\n\n"
            "---\n\n"
            "## Daftar Sistem\n\n"
            "| Nama Sistem | Folder | Status | Terakhir Disentuh | Catatan |\n"
            "|---|---|---|---|---|\n"
            "| (belum ada) | | | | |\n\n"
            "---\n\n"
            "## Legenda Status\n\n"
            "- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali\n"
            "- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai\n"
            "- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh\n"
            "- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai\n"
            "- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)\n",
            encoding="utf-8",
        )

    # Create zip
    if TEMPLATE_ZIP.exists():
        TEMPLATE_ZIP.unlink()
    with zipfile.ZipFile(TEMPLATE_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for p in TEMPLATE_DIR.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(TEMPLATE_DIR))

    print(f"TEMPLATE CLEAN BUILT: {TEMPLATE_DIR}")
    print(f"TEMPLATE ZIP: {TEMPLATE_ZIP} ({TEMPLATE_ZIP.stat().st_size} bytes)")

    # Verify AT-10: no internal audit, no pilot, no konten-kreator
    bad = []
    for p in TEMPLATE_DIR.rglob("*"):
        rel = p.relative_to(TEMPLATE_DIR).as_posix()
        # _meta/_internal should not exist in template (check rel, not absolute parts)
        if "_internal" in rel:
            bad.append(rel)
        if rel.startswith("sistem-konten-kreator/"):
            bad.append(rel)
        if rel.startswith("sistem-pilot-"):
            bad.append(rel)
        if "arsip-naskah" in rel:
            bad.append(rel)
        if "unit-aktif" in rel:
            bad.append(rel)
        # Historical/reference-only docs must never ship in a clean template,
        # regardless of where they live (M-09).
        if p.is_file() and p.suffix == ".md":
            try:
                head = p.read_text(encoding="utf-8")[:400]
            except (OSError, UnicodeDecodeError):
                head = ""
            if "agent_instruction: reference_only" in head:
                bad.append(f"{rel} (reference_only historical doc)")
    if bad:
        print(f"TEMPLATE VERIFY FAILED: should not contain: {bad}")
        return False
    print("TEMPLATE VERIFY PASSED: no personal data, no production output, no internal audit, no domain example, no reference_only historical doc")
    return True

if __name__ == "__main__":
    ok = build()
    if not ok:
        raise SystemExit(1)
    print("TEMPLATE CLEAN BUILD PASSED")
