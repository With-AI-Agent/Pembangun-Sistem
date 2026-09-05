#!/usr/bin/env python3
"""Small dependency-free structural regression check for the master blueprint.

Reworked during the 5 Sep 2026 full meta audit:
- M-01: the required-file list was static and drifted from _meta/. Top-level
  `_meta/*.md`, root pegangan files, and `tools/*.py` are now REQUIRED BY
  GLOB — a new active meta file can never be forgotten by the checker again.
- M-03: the deterministic checkpoint-field check (C-01) only covered the pilot
  units, so the presentation system shipped a STATUS template without the
  field and nobody noticed. It now covers EVERY `sistem-*/` unit directory and
  every STATUS template, and the check is fail-closed: a unit STATUS.md
  without the field is an ERROR.
- Inheritance contract (03_KONTRAK_WARISAN.md): pegangan + LOG_SESI descent is
  now checked generically for every system listed in INDEKS_SISTEM.md, so new
  systems inherit it automatically.
- The validator is designed to run in THREE repos with the same source file:
  master blueprint, clean-template extract (no systems registered -> system
  loops must pass trivially), and a usage repo. Keep it path-relative.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

# --- Required files -------------------------------------------------------
# Meta-level requirements are derived, not hardcoded (M-01).
required = [f"_meta/{p.name}" for p in sorted((ROOT / "_meta").glob("*.md"))]
required += ["PANDUAN_PENGGUNA.md", "PROMPT_ENTRI_UNIVERSAL.md"]
required += [f"tools/{p.name}" for p in sorted((ROOT / "tools").glob("*.py"))]

# --- Index-driven system coverage (inheritance contract) ------------------
INDEX_PATH = ROOT / "_meta/INDEKS_SISTEM.md"


def index_system_rows(text):
    """Return (rows, folders) of the 'Daftar Sistem' table in INDEKS_SISTEM."""
    rows, in_table = [], False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            in_table = stripped.lower().startswith("## daftar sistem")
            continue
        if in_table and stripped.startswith("|"):
            rows.append(stripped)
    folders = []
    for row in rows:
        m = re.search(r"`(sistem-[^`]+?)/?`", row)
        if m:
            folders.append(m.group(1).rstrip("/"))
    return rows, folders


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

index_text = INDEX_PATH.read_text(encoding="utf-8") if INDEX_PATH.is_file() else ""
if not INDEX_PATH.is_file():
    errors.append("missing _meta/INDEKS_SISTEM.md")

index_rows, index_folders = index_system_rows(index_text)

if not index_rows:
    errors.append("INDEKS_SISTEM has no 'Daftar Sistem' table")

# The pilot must not be an ACTIVE SYSTEM ROW in the "Daftar Sistem" table.
# Prose that explains why it is deliberately excluded is allowed and wanted:
# a blanket substring ban would forbid documenting the exclusion at all, which
# is how the same "finding" gets re-raised every session.
for row in index_rows:
    if "sistem-pilot-catatan-belajar" in row:
        errors.append("pilot must not be listed as an active system")
        break

# Every sistem-* folder on disk (except pilot fixtures) must be registered.
for sys_dir in sorted(ROOT.glob("sistem-*/")):
    name = sys_dir.name
    if "pilot" in name:
        continue
    if not any(name in row for row in index_rows):
        errors.append(f"system folder {name}/ not registered in INDEKS_SISTEM 'Daftar Sistem'")

# Inheritance contract checks for each registered system (03_KONTRAK_WARISAN.md):
# pegangan users manual (two files) + manifest + a descent of the LOG_SESI rule.
for name in index_folders:
    sys_dir = ROOT / name
    if not sys_dir.is_dir():
        errors.append(f"INDEKS lists {name}/ but the folder does not exist")
        continue
    if not (sys_dir / "SYSTEM_MANIFEST.md").is_file():
        errors.append(f"{name}: missing SYSTEM_MANIFEST.md")
    if not (sys_dir / "PROMPT_ENTRI_UNIVERSAL.md").is_file():
        errors.append(f"{name}: missing PROMPT_ENTRI_UNIVERSAL.md (pegangan, required by 00_CARA_KERJA)")
    if not ((sys_dir / "PANDUAN_PENGGUNA.md").is_file() or (sys_dir / "panduan/PANDUAN_PENGGUNA.md").is_file()):
        errors.append(f"{name}: missing PANDUAN_PENGGUNA.md (root or panduan/) — pegangan wajib")
    manifest = (sys_dir / "SYSTEM_MANIFEST.md")
    if manifest.is_file() and "Dipakai via lmarena" not in manifest.read_text(encoding="utf-8"):
        errors.append(f"{name}: SYSTEM_MANIFEST.md lacks 'Batasan Platform' (Dipakai via lmarena?)")
    # LOG_SESI descent: at least one active document inside the system folder
    # must contain the mechanism (self-contained). Living documents of units
    # (deck-aktif etc.) do not count — look in root/_sistem/panduan only.
    descent = any(
        "LOG_SESI" in f.read_text(encoding="utf-8")
        for pat in (f"{name}/*.md", f"{name}/_sistem/*.md", f"{name}/panduan/*.md")
        for f in ROOT.glob(pat)
    )
    if not descent:
        errors.append(f"{name}: LOG_SESI mechanism not descended into the system folder (self-contained requirement)")

# --- Deterministic checkpoint field check (C-01, generalized per M-03) ----
# Every unit STATUS.md under a sistem-*/ dir must carry the field; every
# STATUS template (STATUS_TEMPLATE.md or _template/T*_STATUS.md) must define
# it with the exact safe value. Field must be exact `Tidak ada` when safe.
STATUS_VALUE_OK = "Tidak ada"
UNIT_PATTERNS = ("unit-aktif/*/STATUS.md", "_produksi-aktif/*/STATUS.md", "deck-aktif/*/STATUS.md")


def unsaved_value(text):
    m = re.search(
        r"\*{0,2}\s*Pekerjaan(?:\s+yang)?\s+belum\s+tersimpan\s*[:\uff1a]\s*\*{0,2}\s*(.+?)\s*$",
        text, re.MULTILINE,
    )
    if not m:
        return None
    return m.group(1).strip().strip("`").strip()


for sys_dir in sorted(ROOT.glob("sistem-*/")):
    for pattern in UNIT_PATTERNS:
        for status_path in sorted(sys_dir.glob(pattern)):
            text = status_path.read_text(encoding="utf-8")
            val = unsaved_value(text)
            rel = status_path.relative_to(ROOT)
            if val is None:
                errors.append(f"STATUS missing field Pekerjaan belum tersimpan: {rel}")
                continue
            if not val:
                errors.append(f"STATUS empty Pekerjaan belum tersimpan value: {rel}")
            elif val != STATUS_VALUE_OK:
                # "unsafe" values are allowed to be lists/descriptions; but any
                # case-variant of "tidak ada" that is not exact is an error.
                if "tidak ada" in val.lower():
                    errors.append(f"STATUS must use exact 'Tidak ada' (case-sensitive): {rel}: {val}")
    for tmpl in sorted(list(sys_dir.glob("STATUS_TEMPLATE.md")) + list(sys_dir.glob("_sistem/STATUS_TEMPLATE.md")) + list(sys_dir.glob("_template/T*_STATUS.md"))):
        t = tmpl.read_text(encoding="utf-8")
        if "belum tersimpan" not in t:
            errors.append(f"STATUS template missing field: {tmpl.relative_to(ROOT)}")
        elif STATUS_VALUE_OK not in t:
            errors.append(f"STATUS template should mention exact 'Tidak ada': {tmpl.relative_to(ROOT)}")

ref_docs, ref_checked, ref_warnings = [], 0, []


# --- Warning-tier path reference check (A-B3a, extended by M-01/M-03) -----
# Scope: _meta/*.md + root pegangan + each REGISTERED system's active docs
# (root, _sistem, panduan, _generator, _template). Deliberate exclusions:
#   * `_internal/` — historical audit references, not active instructions;
#   * unit living dirs (deck-aktif, unit-aktif, _produksi-aktif) — per-unit
#     work state, checked by the C-01 rules above and the systems' own tools;
#   * `00_RENCANA_KERANGKA.md` — plan document kept as history; the final
#     numbering is documented in-file ("Catatan renumbering 5 Sep"), so its
#     old names are labeled, not defects;
#   * `ACCEPTANCE_TEST_LOG.md` — test-run records citing /tmp paths.
# Build artifacts intentionally gitignored (_meta/_internal/backups/*,
# template_clean*) are whitelisted so that "0 warnings" is a healthy baseline.
ARTIFACT_PREFIXES = ("_meta/_internal/backups/", "_meta/_internal/template_clean")
SCAN_DOC_GLOBS = [
    "_meta/*.md",
    "PANDUAN_PENGGUNA.md",
    "PROMPT_ENTRI_UNIVERSAL.md",
]
for _name in index_folders:
    SCAN_DOC_GLOBS += [
        f"{_name}/*.md",
        f"{_name}/_sistem/*.md",
        f"{_name}/panduan/*.md",
        f"{_name}/_generator/*.md",
        f"{_name}/_template/*.md",
    ]
SCAN_DOC_EXCLUDE_NAMES = ("00_RENCANA_KERANGKA.md", "ACCEPTANCE_TEST_LOG.md", "DISKUSI_MENTAH")
REF_RE = re.compile(r"`([^`\n]+)`")
PATH_EXTENSIONS = (".md", ".py", ".zip", ".json")


def resolve_roots():
    roots = ["", "_meta", "_meta/_internal"]
    for name in index_folders:
        roots += [
            name, f"{name}/_sistem", f"{name}/panduan",
            f"{name}/_generator", f"{name}/_template", f"{name}/_produksi-aktif",
        ]
        for unit in sorted((ROOT / name / "deck-aktif").glob("*")):
            if unit.is_dir():
                roots.append(f"{name}/{unit.parent.name}/{unit.name}")
        # Sistem konten kreator menyimpan arsip per channel; dokumen aktifnya
        # menulis `arsip-naskah/indeks.md` RELATIF terhadap folder channel.
        # Fixture channel menyediakan basis resolusi yang deterministik.
        if (ROOT / name / "channel-fixture-narasi-sejarah").is_dir():
            roots.append(f"{name}/channel-fixture-narasi-sejarah")
    roots.append("sistem-pilot-catatan-belajar")
    return roots


RESOLVE_ROOTS = resolve_roots()


def active_documents():
    """Active documents in scope, sorted for deterministic output."""
    docs = []
    for pattern in SCAN_DOC_GLOBS:
        docs.extend(p for p in ROOT.glob(pattern) if p.is_file())
    kept = []
    for p in docs:
        rel = p.relative_to(ROOT).as_posix()
        if any(part in ("_internal", "deck-aktif", "unit-aktif", "_produksi-aktif") for part in p.relative_to(ROOT).parts):
            continue
        if any(x in p.name for x in SCAN_DOC_EXCLUDE_NAMES):
            continue
        kept.append(p)
    return sorted(set(kept))


def is_path_like(ref):
    # "[", "<", "*" are placeholders/glob patterns; spaces mean a command line
    # (e.g. `python3 tools/validate_repo.py`); absolute paths ("/tmp/...") are
    # external evidence. None of these are repository paths — never judged.
    # Bare filenames in prose are not judged: resolving them needs a writing
    # convention this repository has not adopted.
    return (
        "/" in ref
        and not any(c in ref for c in ("[", "<", "*", " "))
        and not ref.startswith("/")
        and ref.lower().endswith(PATH_EXTENSIONS)
    )


def resolves(ref):
    if any(ref.startswith(p) for p in ARTIFACT_PREFIXES):
        return True  # gitignored build artifacts — known-unresolved by design
    return any((ROOT / base / ref).is_file() for base in RESOLVE_ROOTS)


def scan_references():
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
print(f"SYSTEMS CHECKED (inheritance contract): {len(index_folders)} registered + pilot excluded by design")
for w in ref_warnings:
    print(w)
print(f"WARNINGS: {len(ref_warnings)} (warning tier, exit code unaffected)")
