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

# Files to include in clean template.
# M-01 (audit 5 Sep 2026): the list used to be static and silently drifted —
# files added to _meta/ after v1.0.0 (PANDUAN_PENGGUNA_TEMPLATE, TEMPLATE_LOG_SESI)
# were missing from the template. INCLUDE is now the STATIC CORE inventory
# (obligation, checkpoint_core) UNION the derived repository glob: a new file
# ships automatically, and a deleted core file makes the build FAIL instead
# of silently disappearing (review finding F1).
import checkpoint_core as core

ROOT_META_EXCLUDE = ()  # no _meta file is excluded; empty = fail-loud default

def include_list():
    items = sorted(
        set(core.CORE_META_FILES)
        | {f"_meta/{p.name}" for p in (ROOT / "_meta").glob("*.md")}
    )
    items += [
        "PANDUAN_PENGGUNA.md",
        "PROMPT_ENTRI_UNIVERSAL.md",
        ".gitignore",
        ".gitattributes",
    ]
    items += sorted(
        set(core.CORE_TOOL_FILES)
        | {f"tools/{p.name}" for p in (ROOT / "tools").glob("*.py")}
    )
    return items

# Additional empty dirs to create
EMPTY_DIRS = [
    "_pegangan-kamu",
    "_cadangan-claude",
]

MANIFEST_BANNER = (
    "<!-- BANNER DITAMBAHKAN OLEH build_template.py (M-16, audit 5 Sep 2026):\n"
    "     Salinan dari master blueprint. Di repo HASIL-EKSTRAKSI ini, isi di bawah\n"
    "     adalah SEJARAH master, BUKAN manifest repo ini — manifest sistem-domain\n"
    "     repo baru dibuat dari _meta/SYSTEM_MANIFEST_TEMPLATE.md mulai versi 0.1.0.\n"
    "     Untuk meta-sistem repo ini sendiri, catat versi release di INDEKS. -->\n"
)


def build():
    if TEMPLATE_DIR.exists():
        shutil.rmtree(TEMPLATE_DIR)
    TEMPLATE_DIR.mkdir(parents=True)

    missing = [rel for rel in include_list() if not (ROOT / rel).is_file()]
    if missing:
        print(f"TEMPLATE BUILD FAILED: required source missing: {missing}")
        return False

    for rel in include_list():
        src = ROOT / rel
        dst = TEMPLATE_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    # M-16: the shipped master manifest is history/reference, not the new
    # repo's identity — mark it so a fresh agent cannot mistake it for one.
    manifest_copy = TEMPLATE_DIR / "_meta/SYSTEM_MANIFEST.md"
    if manifest_copy.is_file():
        body = manifest_copy.read_text(encoding="utf-8")
        manifest_copy.write_text(MANIFEST_BANNER + body, encoding="utf-8")

    # F5 (review PR #11, 5 Sep 2026): template self-containment transforms.
    # Two active instructions in the shipped master docs point at files the
    # template deliberately does not ship (the handoff doc, and the
    # konten-kreator user guide). Rewrite them in the TEMPLATE COPIES only —
    # the master keeps its operational references. An anchor that no longer
    # matches means the source doc changed: fail the build, do not ship a
    # template with a silently stale bootstrap.
    def transform(rel, pairs):
        path = TEMPLATE_DIR / rel
        t = path.read_text(encoding="utf-8")
        for old, new in pairs:
            # Idempotent: re-running on an already-templated repo is a no-op;
            # a doc that has NEITHER the anchor NOR the target text has
            # drifted — fail the build.
            if old in t:
                t = t.replace(old, new)
            elif new not in t:
                return (f"transform anchor not found in {rel}: {old[:70]!r} "
                        "(dan teks target tidak ada — dokumen berubah?)")
        path.write_text(t, encoding="utf-8")
        return None

    for err in (
        transform("_meta/NEXT_SESSION_PROMPT.md", [
            ("6. Baca `_meta/_internal/HANDOFF_NEXT_SESSION.md`.",
             "6. Kalau `_meta/_internal/HANDOFF_NEXT_SESSION.md` ada, bacanya. "
             "Di repo baru dari template file ini TIDAK ada — lewati tanpa konflik "
             "(handoff dibuat sesi terakhir di repo asal; ketiadaannya bukan cacat)."),
            ("9. Verifikasi bahwa path dan artefak yang disebut handoff benar-benar ada.",
             "9. Verifikasi bahwa path dan artefak yang disebut handoff (kalau ada) "
             "benar-benar ada."),
        ]),
        transform("PANDUAN_PENGGUNA.md", [
            ("Untuk istilah teknis lain (branch, PR, merge, commit) — lihat "
             "`sistem-konten-kreator/panduan/PANDUAN_PENGGUNA.md`, penjelasannya sama "
             "berlaku di sini.",
             "Istilah teknis singkat: **branch** = salinan kerja; **commit** = snapshot "
             "tersimpan; **PR** = usulan penggabungan kerja; **merge** = penggabungan "
             "usulan yang sudah disetujui. Tiap sistem di repo ini juga punya "
             "PANDUAN_PENGGUNA.md miliknya sendiri (kontrak W-01) dengan istilah yang "
             "disesuaikan."),
        ]),
    ):
        if err:
            print(f"TEMPLATE BUILD FAILED: {err}")
            return False

    # M-01 guard: every core _meta file (obligation) that is referenced
    # (bare filename or _meta/path) from any active _meta document must ship
    # in the template — this is what silently broke for
    # PANDUAN_PENGGUNA_TEMPLATE.md and TEMPLATE_LOG_SESI.md. The core list is
    # checked even for files that no longer exist on disk (F1).
    import re

    ref_re = re.compile(r"`([^`\n]+\.md)`")
    meta_files = {
        Path(f).name: ROOT / f
        for f in (set(core.CORE_META_FILES)
                  | {f"_meta/{p.name}" for p in (ROOT / "_meta").glob("*.md")})
    }
    drifted = []
    for doc in meta_files.values():
        for line in doc.read_text(encoding="utf-8").splitlines():
            for m in ref_re.finditer(line):
                ref = m.group(1).split("/")[-1]
                if ref in meta_files and not (TEMPLATE_DIR / "_meta" / ref).is_file():
                    drifted.append(f"{doc.name} -> {ref}")
    if drifted:
        print("TEMPLATE BUILD FAILED: referenced _meta file not in template: "
              + ", ".join(sorted(set(drifted))))
        return False

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
