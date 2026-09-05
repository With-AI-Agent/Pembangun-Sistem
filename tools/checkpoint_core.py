#!/usr/bin/env python3
"""Shared core for the structural regression tools (single source of truth).

Created 5 Sep 2026 after the independent review of PR #11: validate_repo,
test_failure_injection, build_template and backup_verify used to each carry
their own (drifting) copy of the same judgments. This module holds:

  * CORE_REQUIRED — the STATIC core inventory. It is an OBLIGATION list,
    independent of file presence: a deleted core file must FAIL the tools
    (review finding F1 — before, deleting a required source silently
    shrank the derived requirement set and everything passed).
  * parse_index — STRICT 'Daftar Sistem' parsing (F2): a row is valid only
    with an exact backticked `sistem-<nama>/` folder cell; the old
    substring checks (folder-name `in row`, `"pilot" in name`) matched
    false positives such as an unregistered `sistem-autopilot-data/`.
  * unit_status_files — enumeration of EXPECTED units, not only discovered
    ones (F3): any `STATUS.md` under a system folder (unit-aktif/,
    deck-aktif/, _produksi-aktif/, runs/, ...), templates excluded.
  * the shared fail-closed checkpoint parser (F4): line-anchored (quoted
    blockquote examples do not count), code-fence contents ignored,
    duplicate/ambiguous field = NOT safe (a dirty second field after a safe
    one used to be invisible), protocol formats (`- Status: approved`)
    recognized, not only the literal bold form.
  * Warisan / Tahap parsing for the inheritance-contract enforcement (F9):
    all 9 items W-01..W-09 must be present in a system manifest; an
    'override' row only exempts the mechanical check of that item when the
    full approval trail (alasan:, dampak:, tanggal:, approval:) is present.
"""
import re
from pathlib import Path

SAFE_VALUE = "Tidak ada"
EXACT_PILOT = "sistem-pilot-catatan-belajar"

# --- Static core inventory (F1) -------------------------------------------
# These files MUST exist even if somebody deleted them. The derived glob
# lists in the tools still auto-require every file that EXISTS (so a NEW
# active file can never be forgotten — the original M-01 property); this
# static list is what makes a DELETED core file fail loudly instead of
# silently disappearing from the requirement set.
CORE_META_FILES = [
    "_meta/00_CARA_KERJA_META.md",
    "_meta/01_DISCOVERY_LEVEL_0.md",
    "_meta/02_PRINSIP_UNIVERSAL.md",
    "_meta/03_KONTRAK_WARISAN.md",
    "_meta/ACCEPTANCE_TESTS.md",
    "_meta/DEFINITION_OF_DONE.md",
    "_meta/FAILURE_INJECTION_TESTS.md",
    "_meta/INDEKS_SISTEM.md",
    "_meta/NEXT_SESSION_PROMPT.md",
    "_meta/PANDUAN_PENGGUNA_TEMPLATE.md",
    "_meta/PLATFORM_LMARENA.md",
    "_meta/PROTOKOL_CHECKPOINT_RECOVERY.md",
    "_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md",
    "_meta/SESSION_REPORT_TEMPLATE.md",
    "_meta/SYSTEM_MANIFEST.md",
    "_meta/SYSTEM_MANIFEST_TEMPLATE.md",
    "_meta/TEMPLATE_LOG_SESI.md",
    "_meta/TEMPLATE_RELEASE.md",
]
CORE_ROOT_FILES = ["PANDUAN_PENGGUNA.md", "PROMPT_ENTRI_UNIVERSAL.md"]
CORE_TOOL_FILES = [
    "tools/checkpoint_core.py",
    "tools/validate_repo.py",
    "tools/test_failure_injection.py",
    "tools/backup_verify.py",
    "tools/build_template.py",
]
CORE_REQUIRED = CORE_META_FILES + CORE_ROOT_FILES + CORE_TOOL_FILES

# --- Fence / field / status parsing (F4) -----------------------------------
def strip_code_fences(text: str) -> str:
    """Blank out fenced code block contents (state may never be taken from
    an example pasted inside a fence)."""
    out, in_fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
        elif in_fence:
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


FIELD_RE = re.compile(
    r"^[ \t]*(?:[-*][ \t]+)?\*{0,2}\s*Pekerjaan(?:\s+yang)?\s+belum\s+tersimpan"
    r"\s*[:：]\s*\*{0,2}\s*(.+?)\s*$",
    re.MULTILINE,
)


def unsaved_field_values(text: str):
    """All checkpoint-field values outside code fences, in document order.
    The field must sit at line start (optional list bullet): quoted examples
    (blockquotes `>`, prose mentions) are not state."""
    return [
        m.group(1).strip().strip("`").strip()
        for m in FIELD_RE.finditer(strip_code_fences(text))
    ]


def parse_unsaved_field(text: str):
    """Return (kind, value) with kind in 'absent' | 'ambiguous' | 'value'.
    'ambiguous' = the field appears more than once — a dirty value after a
    safe one is NOT proof of safety (review F4)."""
    vals = unsaved_field_values(text)
    if not vals:
        return ("absent", None)
    if len(vals) > 1:
        return ("ambiguous", vals)
    return ("value", vals[0])


STATUS_RE = re.compile(
    r"^[ \t]*(?:[-*][ \t]+)?\*{0,2}\s*Status\*{0,2}\s*[:：]\s*\*{0,2}\s*`?([A-Za-z][A-Za-z-]*)`?[ \t]*$",
    re.MULTILINE | re.IGNORECASE,
)


def status_values(text: str):
    """Unit status tokens, format-tolerant: bold `**Status:**` released,
    plain protocol `- Status: approved`, backticked or not (F4 — the old
    checker only matched one literal bold spelling, so the official protocol
    format was invisible)."""
    return [m.group(1).lower() for m in STATUS_RE.finditer(strip_code_fences(text))]


RELEASED_STATES = {"released", "approved"}


def state_is_safe(unit: Path) -> bool:
    """Fail-closed gate for a unit folder (contains STATUS.md / OUTPUT.md).
    Safe = field present exactly once AND value exactly 'Tidak ada', and if
    any status line claims released/approved then OUTPUT.md exists."""
    status = unit / "STATUS.md"
    if not status.is_file():
        return False
    text = status.read_text(encoding="utf-8")
    if any(v in RELEASED_STATES for v in status_values(text)):
        if not (unit / "OUTPUT.md").is_file():
            return False
    kind, value = parse_unsaved_field(text)
    return kind == "value" and value == SAFE_VALUE


# --- INDEKS parsing (F2) -----------------------------------------------------
FOLDER_CELL_RE = re.compile(r"^`(sistem-[A-Za-z0-9._-]+)/?`$")


def parse_index(text: str):
    """Strict parse of the 'Daftar Sistem' table.
    Returns (folders, errors). Rules:
      * first table row must be the header (Nama Sistem / Folder);
      * a data row is valid only if its Folder cell is exactly
        `sistem-<nama>/` (backticked) or a placeholder (empty / '(belum ada)');
      * anything else is a parse ERROR — the old code silently ignored
        rows without backticks, so a registered-looking line produced no
        coverage at all (review F2).
    """
    rows, in_table = [], False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_table = s[3:].strip().lower().startswith("daftar sistem")
            continue
        if in_table and s.startswith("|"):
            rows.append(s)

    errors, folders = [], []
    if not rows:
        if text.strip():
            errors.append("'Daftar Sistem' tabel kosong")
        return folders, errors

    first = [c.strip() for c in rows[0].strip("|").split("|")]
    if not any("folder" in c.lower() for c in first):
        errors.append("baris pertama 'Daftar Sistem' bukan header (Nama Sistem/Folder/...)")
        return folders, errors

    for row in rows[1:]:
        cells = [c.strip() for c in row.strip("|").split("|")]
        if all(re.fullmatch(r"[-: ]*", c) for c in cells):
            continue  # separator
        folder_cell = cells[1] if len(cells) > 1 else ""
        if folder_cell == "" or folder_cell.startswith("(belum ada)"):
            continue  # placeholder row (template extract)
        m = FOLDER_CELL_RE.match(folder_cell)
        if not m:
            errors.append(
                "baris 'Daftar Sistem' tidak valid — kolom Folder harus persis "
                f"backticked `sistem-<nama>/` (ditemui: {folder_cell!r})"
            )
            continue
        folders.append(m.group(1))
    return folders, errors


# --- Unit enumeration (F3) ---------------------------------------------------
def unit_status_files(sys_dir: Path):
    """All unit STATUS.md of a system, ANY layout (unit-aktif/, deck-aktif/,
    _produksi-aktif/, runs/, ...). Templates are excluded. Review F3: a
    registered system is EXPECTED to have at least one — discovering zero
    files used to silently shrink coverage instead of failing."""
    return sorted(
        p for p in sys_dir.rglob("STATUS.md")
        if "_template" not in p.parts
    )


# --- Warisan / Tahap (F9) ------------------------------------------------------
WARISAN_ITEMS = [f"W-{i:02d}" for i in range(1, 10)]
OVERRIDE_LABELS = ("alasan:", "dampak:", "tanggal:", "approval:")


def manifest_tahap(text: str) -> str:
    """Build stage declared in the manifest: 'kerangka' (registered skeleton
    — W-01/W-02/W-03 presence checks downgrade to warnings) or
    'siap-pakai' (default; everything required)."""
    m = re.search(r"^\s*-\s*\*\*Tahap:\*\*\s*`?([A-Za-z-]+)`?", text, re.MULTILINE)
    return m.group(1).lower() if m else "siap-pakai"


def warisan_rows(text: str):
    """Yield (item, row) for each manifest table row starting '| W-0n'."""
    out = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|"):
            m = re.match(r"\|\s*(W-0\d)\b", s)
            if m:
                out.append((m.group(1), s))
    return out


def warisan_errors(name: str, text: str):
    """F9: all nine items must be present; an 'override' row without the
    full approval trail is NOT a valid override (contract rule 3) and is an
    error. Format-agnostic presence (table rows or prose enumeration); the
    mechanical exemption (overridden_items) only applies to table rows."""
    errors = []
    for w in WARISAN_ITEMS:
        if not re.search(rf"\b{w}\b", text):
            errors.append(f"{name}: Warisan tidak menyebut butir {w}")
    for w, row in warisan_rows(text):
        if "override" in row.lower() and not all(l in row.lower() for l in OVERRIDE_LABELS):
            errors.append(
                f"{name}: baris Warisan {w} menandakan override tapi tidak lengkap — "
                "wajib menyebut alasan:, dampak:, tanggal:, approval: (kontrak W, aturan 3)"
            )
    return errors


def overridden_items(text: str):
    """Items whose table row carries a COMPLETE override → exempt from the
    mechanical check of that item (the deactivation was approved and
    recorded; the checker must not then demand the deactivated artifact)."""
    out = set()
    for w, row in warisan_rows(text):
        low = row.lower()
        if "override" in low and all(l in low for l in OVERRIDE_LABELS):
            out.add(w)
    return out
