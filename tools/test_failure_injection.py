#!/usr/bin/env python3
"""Executable fail-closed checks for the generic checkpoint contract."""
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]


def state_is_safe(unit: Path) -> bool:
    status = unit / "STATUS.md"
    if not status.is_file():
        return False
    text = status.read_text(encoding="utf-8")
    if "- **Status:** `released`" in text or "- **Status:** `approved`" in text:
        output = unit / "OUTPUT.md"
        if not output.is_file():
            return False
    return "Pekerjaan belum tersimpan: Tidak ada" in text


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
            "- **Status:** `released`\n- Pekerjaan belum tersimpan: Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("FI-02 missing output", not state_is_safe(unit)))

        # FI-07: a blocked state must never be treated as released.
        unit = base / "fi07"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `blocked`\n- Pekerjaan belum tersimpan: Tidak ada\n",
            encoding="utf-8",
        )
        checks.append(("FI-07 blocked state", state_is_safe(unit)))

        # Healthy state is accepted only with output and no unsaved work.
        unit = base / "healthy"
        unit.mkdir()
        (unit / "STATUS.md").write_text(
            "- **Status:** `released`\n- Pekerjaan belum tersimpan: Tidak ada\n",
            encoding="utf-8",
        )
        (unit / "OUTPUT.md").write_text("checked output", encoding="utf-8")
        checks.append(("healthy released state", state_is_safe(unit)))

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("FAILURE-INJECTION TESTS FAILED")
        for name in failed:
            print(f"- {name}")
        raise SystemExit(1)
    print(f"FAILURE-INJECTION TESTS PASSED: {len(checks)} fail-closed scenarios")


if __name__ == "__main__":
    run()
