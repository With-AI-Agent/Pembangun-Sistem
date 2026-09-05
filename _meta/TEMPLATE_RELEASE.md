# Template Release — Meta-Sistem

**Tujuan:** Menentukan apa yang termasuk template bersih dan bagaimana memverifikasinya (AT-10)

## Definisi Template Bersih

Template bersih adalah salinan siap pakai untuk membuat repo baru, yang **tidak** membawa:

- data pribadi
- output produksi (contoh: arsip naskah, unit-aktif, OUTPUT.md produksi)
- audit internal (`_meta/_internal/`)
- keputusan domain contoh (misal isi `sistem-konten-kreator/` yang spesifik ke konten kreator)

Template **wajib** membawa (diselaraskan dengan temuan M-01/M-16 audit 5 Sep 2026):

- SEMUA `_meta/*.md` top-level — daftar ini **tidak lagi manual**: `tools/build_template.py` men-glob folder, jadi file meta baru otomatis ikut; guard kelengkapan membuat BUILD GAGAL kalau ada `_meta/*.md` yang dirujuk dokumen aktif tapi tidak ikut terbawa
- SEMUA `tools/*.py` — tanpa validator/FI/backup/template, repo hasil ekstrak kehilangan regresi struktural dan penegakan kontrak warisan (dulu tidak ikut: cacat M-01 kelas distribusi)
- entry point pengguna (`PANDUAN_PENGGUNA.md`) + prompt entri (`PROMPT_ENTRI_UNIVERSAL.md`)
- indeks sistem dikosongkan (`_meta/INDEKS_SISTEM.md` dengan header + baris kosong)
- manifest meta (`_meta/SYSTEM_MANIFEST.md`) sebagai referensi versi — **diberi banner otomatis** oleh builder bahwa isinya sejarah master, bukan identitas repo baru (M-16)
- `.gitignore`, `.gitattributes`
- folder kosong `_pegangan-kamu/` dan `_cadangan-claude/` dengan `.gitkeep`

## Cara Build

```bash
python3 tools/build_template.py
```

Output:
- `_meta/_internal/template_clean/` — folder template bersih
- `_meta/_internal/template_clean.zip` — zip siap distribusi

## Verifikasi

`tools/build_template.py` melakukan verifikasi AT-10:

- tidak ada `_internal` di dalam template
- tidak ada `sistem-konten-kreator/`
- tidak ada `sistem-pilot-`
- tidak ada `arsip-naskah`
- tidak ada `unit-aktif`
- **kelengkapan (M-01):** setiap `_meta/*.md` yang dirujuk dari dokumen aktif `_meta/` HARUS ikut terbawa; sumber INCLUDE yang hilang = build gagal

Jika ada pelanggaran, build gagal.

**Smoke test pasca-build (wajib setiap kali template/validator berubah):** ekstrak zip ke direktori kosong, `git init`, lalu jalankan di sana `python3 tools/validate_repo.py` dan `python3 tools/test_failure_injection.py` — keduanya harus PASS (exit 0) tanpa ada sistem terdaftar. Ini membuktikan template berdiri sendiri (diverifikasi 5 Sep 2026; lihat `AUDIT_META_SISTEM_2026-09-05.md` rencana regressi #3). **Yang normal di repo hasil ekstrak:** warning (bukan error) yang menunjuk artefak khusus master — file `sistem-konten-kreator/…`, `_meta/_internal/…`, path pilot — karena template memang TIDAK membawanya; exit code tetap 0 dan itu bukan cacat template. Target "0 warning" hanya berlaku di master blueprint.

## Backup

Backup esensial dilakukan via:

```bash
python3 tools/backup_verify.py
```

Output:
- `_meta/_internal/backups/backup_essential.zip`
- Verifikasi restore ke temp dir dan bandingkan manifest

## Status Rilis

- Template bersih: built dan verified 2026-09-04 via `tools/build_template.py`
- Backup: created dan verified 2026-09-04 via `tools/backup_verify.py`

Kedua artefak disimpan di `_meta/_internal/` (bukan bagian dari template bersih itu sendiri).
