#!/usr/bin/env python3
"""Backup & restore verification for meta-system.

Creates a backup of essential meta files and verifies restore.
This satisfies DEFINITION_OF_DONE.md "Prosedur backup dan restore berhasil diuji"
and SYSTEM_MANIFEST.md gate "Backup lokal terverifikasi".
"""
from pathlib import Path
import zipfile
import tempfile
import shutil

ROOT = Path(__file__).resolve().parents[1]
BACKUP_DIR = ROOT / "_meta" / "_internal" / "backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# M-01 (audit 5 Sep 2026): ESSENTIAL was a static list frozen at v1.0.0 and
# silently missed every _meta file added later (PANDUAN_PENGGUNA_TEMPLATE.md,
# TEMPLATE_LOG_SESI.md). It is now the STATIC CORE inventory (obligation,
# checkpoint_core) UNION the derived repository glob: a new active file ships
# automatically, and a deleted core file makes the backup FAIL instead of
# silently shrinking the list (review finding F1). Restore verification
# (existence + byte match of every file, not just the manifest) closes the
# drift risk.
import checkpoint_core as core


def essential_list():
    items = sorted(
        set(core.CORE_META_FILES)
        | {f"_meta/{p.name}" for p in (ROOT / "_meta").glob("*.md")}
    )
    items += [
        "PANDUAN_PENGGUNA.md",
        "PROMPT_ENTRI_UNIVERSAL.md",
        "_meta/INDEKS_SISTEM.md",
        ".gitignore",
        ".gitattributes",
    ]
    items += sorted(
        set(core.CORE_TOOL_FILES)
        | {f"tools/{p.name}" for p in (ROOT / "tools").glob("*.py")}
    )
    items += sorted(
        f"{p.parent.name}/SYSTEM_MANIFEST.md"
        for p in ROOT.glob("sistem-*/SYSTEM_MANIFEST.md")
    )
    return sorted(set(items))


ESSENTIAL = essential_list()


def create_backup():
    missing_src = [rel for rel in ESSENTIAL if not (ROOT / rel).is_file()]
    if missing_src:
        print(f"BACKUP FAILED: essential source missing: {missing_src}")
        raise SystemExit(1)
    backup_path = BACKUP_DIR / "backup_essential.zip"
    with zipfile.ZipFile(backup_path, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in ESSENTIAL:
            p = ROOT / rel
            if p.is_file():
                z.write(p, rel)
    return backup_path

def verify_restore(backup_path):
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        with zipfile.ZipFile(backup_path, "r") as z:
            z.extractall(tmp_path)
        # Verify all essential files exist after restore
        missing = []
        for rel in ESSENTIAL:
            if not (tmp_path / rel).is_file():
                # Only check if original existed
                if (ROOT / rel).is_file():
                    missing.append(rel)
        if missing:
            print(f"BACKUP VERIFY FAILED: missing after restore: {missing}")
            return False
        # M-01: content-verify EVERY essential file byte-for-byte (was: manifest only),
        # so a restored backup that silently truncated a file cannot pass.
        mismatch = []
        for rel in ESSENTIAL:
            orig = ROOT / rel
            if orig.is_file() and (tmp_path / rel).read_bytes() != orig.read_bytes():
                mismatch.append(rel)
        if mismatch:
            print(f"BACKUP VERIFY FAILED: content mismatch after restore: {mismatch}")
            return False
        print(f"BACKUP VERIFIED: {backup_path} contains {len(ESSENTIAL)} files, restore OK (all bytes verified)")
        return True

if __name__ == "__main__":
    bp = create_backup()
    print(f"BACKUP CREATED: {bp}")
    ok = verify_restore(bp)
    if not ok:
        raise SystemExit(1)
    print("BACKUP AND RESTORE TEST PASSED")
