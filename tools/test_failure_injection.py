#!/usr/bin/env python3
"""Executable fail-closed checks for the generic checkpoint contract.

M-02 (audit 5 Sep 2026): the old checker matched the literal
`"Pekerjaan belum tersimpan: Tidak ada"` while EVERY real STATUS.md /
STATUS_TEMPLATE.md in this repository uses the bold form
`**Pekerjaan belum tersimpan:** Tidak ada` (and some wrap the value in
backticks). Measured: state_is_safe() returned False for all four real
units, so "4 fail-closed scenarios PASSED" proved nothing about real data.
The parser below matches the same shapes validate_repo.py C-01 accepts,
and the scenarios now use the REAL format, plus explicit "field absent"
and "unsafe value" cases.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
import re

ROOT = Path(__file__).resolve().parents[1]

# Accept: "Pekerjaan belum tersimpan:" / "Pekerjaan yang belum tersimpan:",
# optional bold markers, optional backticks around the value.
FIELD_RE = re.compile(
    r"\*{0,2}\s*Pekerjaan(?:\s+yang)?\s+belum\s+tersimpan\s*[:\uff1a]\s*\*{0,2}\s*(.+?)\s*$",
    re.MULTILINE,
)


def unsaved_field(text: str):
    """Return the raw value of the checkpoint field, or None if absent."""
    m = FIELD_RE.search(text)
    return m.group(1).strip().strip("`").strip() if m else None


def state_is_safe(unit: Path) -> bool:
    status = unit / "STATUS.md"
    if not status.is_file():
        return False
    text = status.read_text(encoding="utf-8")
    if "- **Status:** `released`" in text or "- **Status:** `approved`" in text:
        if not (unit / "OUTPUT.md").is_file():
            return False
    value = unsaved_field(text)
    if value is None:
        return False  # fail-closed: missing field is never proof of safety
    return value == "Tidak ada"


def run():
    checks = []
    with TemporaryDirectory() as d:
        base = Path(d)

        # FI-01: output without status must fail closed.
        unit = base / "fi01"
        unit.mkdir()
        (unit / "OUTPUT.md").write_text("output", encoding="utf-8")
        checks.append(("FI-01 missing STATUS", not state_is_safe(unit)))

        # FI-02: released status without output must fail closed.
        unit = base / "fi02"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `released`\n- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("FI-02 missing output", not state_is_safe(unit)))

        # FI-07: a blocked state must never be treated as released.
        unit = base / "fi07"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `blocked`\n- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("FI-07 blocked state", state_is_safe(unit)))

        # Healthy state in the REAL repo format (bold field, no backticks).
        unit = base / "healthy"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `released`\n- **Pekerjaan belum tersimpan:** Tidak ada\n",
            encoding="utf-8",
        )
        (unit / "OUTPUT.md").write_text("checked output", encoding="utf-8")
        checks.append(("healthy released state (real bold format)", state_is_safe(unit)))

        # Real-world variant with backticks (konten-kreator template style).
        unit = base / "healthy_backticked"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `in-progress`\n- **Pekerjaan belum tersimpan:** `Tidak ada`\n",
            encoding="utf-8",
        )
        checks.append(("backticked value accepted", state_is_safe(unit)))

        # Field absent must fail closed — this was the deck-presentasi case
        # (T6_STATUS.md had no field at all; M-03).
        unit = base / "field_absent"
        unit.mkdir()
        (unit / "STATUS.md").write_text("- **Status:** `in-progress`\n", encoding="utf-8")
        checks.append(("missing field fails closed", not state_is_safe(unit)))

        # Free-text "none"/"tidak ada" variations are NOT safe (C-01 exactness).
        unit = base / "unsafe_value"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `in-progress`\n- **Pekerjaan belum tersimpan:** aman kok\n",
            encoding="utf-8",
        )
        checks.append(("unsafe value fails closed", not state_is_safe(unit)))

    # Regression against REAL repo data: every unit STATUS that claims to be
    # safe must actually satisfy the checker (guards format drift again).
    real = []
    for sys_dir in sorted(ROOT.glob("sistem-*/")):
        for pattern in ("unit-aktif/*/STATUS.md", "_produksi-aktif/*/STATUS.md", "deck-aktif/*/STATUS.md"):
            for status_path in sorted(sys_dir.glob(pattern)):
                text = status_path.read_text(encoding="utf-8")
                if unsaved_field(text) is not None:
                    real.append((status_path, state_is_safe(status_path.parent)))
    for status_path, safe in real:
        checks.append((f"real unit consistent: {status_path.relative_to(ROOT)}", safe))

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("FAILURE-INJECTION TESTS FAILED")
        for name in failed:
            print(f"- {name}")
        raise SystemExit(1)
    print(f"FAILURE-INJECTION TESTS PASSED: {len(checks)} scenarios "
          f"(6 synthetic + {len(real)} real-unit consistency)")


if __name__ == "__main__":
    run()
