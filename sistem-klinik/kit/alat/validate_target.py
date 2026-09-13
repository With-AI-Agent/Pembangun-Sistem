#!/usr/bin/env python3
"""Validator portabel untuk sistem target yang dirawat Sistem Klinik."""

import re
import sys
from pathlib import Path

def main():
    errors = []
    root = Path.cwd()
    
    # Cek STATUS
    status_file = root / "STATUS.md"
    readme_file = root / "README.md"
    
    status_content = ""
    if status_file.exists():
        status_content = status_file.read_text()
    elif readme_file.exists():
        status_content = readme_file.read_text()
        
    if not re.search(r'STATUS.*\b(aktif|dalam-pembangunan|rusak)\b', status_content, re.IGNORECASE):
        errors.append("W-03: Field STATUS (aktif/dalam-pembangunan/rusak) tidak ditemukan di STATUS.md atau README.md")

    if errors:
        print("VALIDATION FAILED (TARGET):")
        for e in errors:
            print(f"- {e}")
        sys.exit(1)
    else:
        print("VALIDATION PASSED (TARGET)")
        sys.exit(0)

if __name__ == '__main__':
    main()
