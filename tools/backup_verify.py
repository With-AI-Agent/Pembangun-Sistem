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

ESSENTIAL = [
    "_meta/SYSTEM_MANIFEST.md",
    "_meta/00_CARA_KERJA_META.md",
    "_meta/01_DISCOVERY_LEVEL_0.md",
    "_meta/02_PRINSIP_UNIVERSAL.md",
    "_meta/INDEKS_SISTEM.md",
    "_meta/SYSTEM_MANIFEST_TEMPLATE.md",
    "_meta/DEFINITION_OF_DONE.md",
    "_meta/PROTOKOL_CHECKPOINT_RECOVERY.md",
    "_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md",
    "_meta/ACCEPTANCE_TESTS.md",
    "_meta/SESSION_REPORT_TEMPLATE.md",
    "_meta/FAILURE_INJECTION_TESTS.md",
    "_meta/NEXT_SESSION_PROMPT.md",
    "PANDUAN_PENGGUNA.md",
    "sistem-konten-kreator/SYSTEM_MANIFEST.md",
    "tools/validate_repo.py",
    "tools/test_failure_injection.py",
]

def create_backup():
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
        # Verify content matches (at least for manifest)
        orig_manifest = (ROOT / "_meta/SYSTEM_MANIFEST.md").read_text(encoding="utf-8")
        restored_manifest = (tmp_path / "_meta/SYSTEM_MANIFEST.md").read_text(encoding="utf-8")
        if orig_manifest != restored_manifest:
            print("BACKUP VERIFY FAILED: manifest content mismatch")
            return False
        print(f"BACKUP VERIFIED: {backup_path} contains {len(ESSENTIAL)} files, restore OK")
        return True

if __name__ == "__main__":
    bp = create_backup()
    print(f"BACKUP CREATED: {bp}")
    ok = verify_restore(bp)
    if not ok:
        raise SystemExit(1)
    print("BACKUP AND RESTORE TEST PASSED")
