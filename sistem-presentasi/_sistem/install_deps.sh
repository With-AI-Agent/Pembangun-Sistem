#!/bin/bash
# install_deps.sh — pasang & verifikasi dependency Sistem Presentasi.
# /tmp TIDAK persisten antar sesi -> jalankan skrip ini tiap sesi sebelum build.
# Pemakaian: bash install_deps.sh [target_dir]   (default: /tmp/pptxlib)
set -e
TARGET="${1:-/tmp/pptxlib}"
echo ">> install ke $TARGET ..."
python3 -m pip install -q --target "$TARGET" python-pptx Pillow pypdf python-docx matplotlib
echo ">> verifikasi import ..."
PYTHONPATH="$TARGET" python3 -c "
import importlib
mods = {'pptx':'python-pptx','PIL':'Pillow','pypdf':'pypdf','docx':'python-docx','matplotlib':'matplotlib'}
for m,name in mods.items():
    importlib.import_module(m); print('OK', name)
print('SEMUA DEPENDENCY VALID')
"
