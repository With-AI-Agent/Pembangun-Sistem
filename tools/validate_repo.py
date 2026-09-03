#!/usr/bin/env python3
"""Small dependency-free structural regression check for the master blueprint."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
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
    "PANDUAN_PENGGUNA.md",
    "_cadangan-claude/RINGKASAN_sistem-konten-kreator.md",
    "sistem-konten-kreator/SYSTEM_MANIFEST.md",
    "sistem-konten-kreator/QUALITY_ASSURANCE_AND_EVOLUTION.md",
    "sistem-konten-kreator/_sistem/START_DI_SINI.md",
    "sistem-konten-kreator/_sistem/STATUS_TEMPLATE.md",
    "sistem-pilot-catatan-belajar/SESSION_REPORT.md",
    "sistem-pilot-catatan-belajar/SYSTEM_MANIFEST.md",
    "sistem-pilot-catatan-belajar/START_DI_SINI.md",
    "sistem-pilot-catatan-belajar/WORKFLOW.md",
    "sistem-pilot-catatan-belajar/OUTPUT_TEMPLATE.md",
    "sistem-pilot-catatan-belajar/QUALITY.md",
    "sistem-pilot-catatan-belajar/STATUS_TEMPLATE.md",
    "sistem-pilot-catatan-belajar/unit-aktif/pilot-001/STATUS.md",
    "sistem-pilot-catatan-belajar/unit-aktif/pilot-001/OUTPUT.md",
]

# --- Warning-tier path reference check (A-B3a) ---------------------------
#
# Purpose: DEFINITION_OF_DONE requires "Dependency dirujuk dengan path yang
# valid", but nothing enforced it, so a broken reference survived in the main
# agent entry point (finding A-B1). This tier reports such references.
#
# The scope is deliberately narrow and deterministic:
#
#   * Only ACTIVE documents are scanned: `_meta/*.md` plus
#     `PANDUAN_PENGGUNA.md`.
#   * `_meta/_internal/` is EXCLUDED on purpose. Those files are historical
#     audit references, not active instructions (see `00_CARA_KERJA_META.md`,
#     section "Lapisan Kendali dan Definition of Done"). They legitimately
#     cite paths belonging to the pre-migration system that never existed in
#     this repository -- verified: `arsip-naskah/indeks.md` and
#     `arsip-naskah/indeks-karakter.md` in
#     `AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md` (finding A-B11). Scanning
#     them would add warnings unrelated to any active defect.
#   * Only "path-like" references are judged: a backticked span that contains
#     "/", ends with a known extension, and holds no "[" placeholder. Bare
#     filenames in prose (e.g. `START_DI_SINI.md`) are intentionally NOT
#     judged: resolving them needs a writing convention this repository has
#     not adopted, and no such rule is added to any active document here.
#     Measured effect of this rule on the 14 active documents: 8 references
#     checked, 0 false positives.
#
# Warnings NEVER change the exit code. This tier reports; it does not gate.
ACTIVE_DOC_GLOBS = ["_meta/*.md"]
ACTIVE_DOC_EXTRA = ["PANDUAN_PENGGUNA.md"]
ACTIVE_DOC_EXCLUDE_PARTS = ("_internal",)
REF_RE = re.compile(r"`([^`\n]+)`")
PATH_EXTENSIONS = (".md", ".py", ".zip", ".json")
RESOLVE_ROOTS = [
    "",
    "_meta",
    "_meta/_internal",
    "sistem-konten-kreator",
    "sistem-konten-kreator/_sistem",
    "sistem-pilot-catatan-belajar",
]


def active_documents():
    """Active documents in scope, sorted for deterministic output."""
    docs = []
    for pattern in ACTIVE_DOC_GLOBS:
        docs.extend(p for p in ROOT.glob(pattern) if p.is_file())
    for rel in ACTIVE_DOC_EXTRA:
        candidate = ROOT / rel
        if candidate.is_file():
            docs.append(candidate)
    kept = [
        p
        for p in docs
        if not any(part in ACTIVE_DOC_EXCLUDE_PARTS for part in p.relative_to(ROOT).parts)
    ]
    return sorted(set(kept))


def is_path_like(ref):
    return (
        "/" in ref
        and "[" not in ref
        and ref.lower().endswith(PATH_EXTENSIONS)
    )


def resolves(ref):
    return any((ROOT / base / ref).is_file() for base in RESOLVE_ROOTS)


def scan_references():
    """Return (docs, checked_count, warnings). Warnings are non-gating."""
    docs = active_documents()
    checked = 0
    warnings = []
    for path in docs:
        rel = path.relative_to(ROOT).as_posix()
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for match in REF_RE.finditer(line):
                ref = match.group(1)
                if not is_path_like(ref):
                    continue
                checked += 1
                if not resolves(ref):
                    warnings.append(
                        f"WARNING reference: {rel}:{lineno}: "
                        f"unresolved path reference `{ref}`"
                    )
    return docs, checked, warnings


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

ref_docs, ref_checked, ref_warnings = scan_references()

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    for w in ref_warnings:
        print(w)
    sys.exit(1)

# The line below is quoted verbatim by _meta/_internal/HANDOFF_NEXT_SESSION.md
# and by audit records on other branches. Keep it byte-identical; report the
# new coverage on additional lines instead of rewriting this one.
print(f"VALIDATION PASSED: {len(required)} required files and Markdown invariants checked")
print(
    f"COVERAGE: {len(ref_docs)} active documents scanned, "
    f"{ref_checked} path references checked, {len(ref_warnings)} unresolved"
)
for w in ref_warnings:
    print(w)
print(f"WARNINGS: {len(ref_warnings)} (warning tier, exit code unaffected)")
