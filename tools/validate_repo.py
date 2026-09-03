#!/usr/bin/env python3
"""Small dependency-free structural regression check for the master blueprint."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "_meta/00_CARA_KERJA_META.md",
    "_meta/01_DISCOVERY_LEVEL_0.md",
    "_meta/02_PRINSIP_UNIVERSAL.md",
    "_meta/INDEKS_SISTEM.md",
    "_meta/SYSTEM_MANIFEST_TEMPLATE.md",
    "_meta/DEFINITION_OF_DONE.md",
    "_meta/PROTOKOL_CHECKPOINT_RECOVERY.md",
    "_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md",
    "PANDUAN_PENGGUNA.md",
    "_cadangan-claude/RINGKASAN_sistem-konten-kreator.md",
    "sistem-konten-kreator/SYSTEM_MANIFEST.md",
    "sistem-konten-kreator/QUALITY_ASSURANCE_AND_EVOLUTION.md",
    "sistem-konten-kreator/_sistem/START_DI_SINI.md",
    "sistem-konten-kreator/_sistem/STATUS_TEMPLATE.md",
    "sistem-pilot-catatan-belajar/SYSTEM_MANIFEST.md",
    "sistem-pilot-catatan-belajar/START_DI_SINI.md",
    "sistem-pilot-catatan-belajar/WORKFLOW.md",
    "sistem-pilot-catatan-belajar/OUTPUT_TEMPLATE.md",
    "sistem-pilot-catatan-belajar/QUALITY.md",
    "sistem-pilot-catatan-belajar/STATUS_TEMPLATE.md",
    "sistem-pilot-catatan-belajar/unit-aktif/pilot-001/STATUS.md",
    "sistem-pilot-catatan-belajar/unit-aktif/pilot-001/OUTPUT.md",
]
errors = []
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

for p in ROOT.rglob("*.md"):
    if ".git" in p.parts:
        continue
    text = p.read_text(encoding="utf-8")
    if any(marker in text for marker in ("<<<<<<<", ">>>>>>>")):
        errors.append(f"merge conflict marker: {p.relative_to(ROOT)}")
    if text.count("```") % 2:
        errors.append(f"unpaired code fence: {p.relative_to(ROOT)}")

index = (ROOT / "_meta/INDEKS_SISTEM.md").read_text(encoding="utf-8")
if "sistem-konten-kreator/" not in index:
    errors.append("index does not contain the content creator system")
if "sistem-pilot-catatan-belajar/" in index:
    errors.append("pilot must not be listed as an active system")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"VALIDATION PASSED: {len(required)} required files and Markdown invariants checked")
