# Template Release — Meta-Sistem

**Tujuan:** Menentukan apa yang termasuk template bersih dan bagaimana memverifikasinya (AT-10)

## Definisi Template Bersih

Template bersih adalah salinan siap pakai untuk membuat repo baru, yang **tidak** membawa:

- data pribadi
- output produksi (contoh: arsip naskah, unit-aktif, OUTPUT.md produksi)
- audit internal (`_meta/_internal/`)
- keputusan domain contoh (misal isi `sistem-konten-kreator/` yang spesifik ke konten kreator)

Template **wajib** membawa:

- entry point pengguna (`PANDUAN_PENGGUNA.md`)
- entry point agent (`_meta/00_CARA_KERJA_META.md`)
- discovery level-0 (`_meta/01_DISCOVERY_LEVEL_0.md`)
- prinsip universal (`_meta/02_PRINSIP_UNIVERSAL.md`)
- indeks sistem kosong (`_meta/INDEKS_SISTEM.md` dengan header saja)
- manifest template (`_meta/SYSTEM_MANIFEST_TEMPLATE.md`)
- definition of done, checkpoint recovery, QA & evolution, acceptance tests, session report, failure injection, next session prompt
- manifest meta (`_meta/SYSTEM_MANIFEST.md`) sebagai referensi versi
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

Jika ada, build gagal.

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
