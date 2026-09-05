# START DI SINI — Sistem Presentasi (mandiri)

> Entry point sistem ini. Dokumen ini **self-contained**: semua yang dibutuhkan ada di folder ini, jadi folder `sistem-presentasi/` dapat diunduh dan dijadikan **repo tersendiri** tanpa `_meta/`.

## Apa ini
Sistem untuk mengubah **bahan** (dokumen pengguna / topik riset) menjadi **berkas presentasi** (default `.pptx`) yang setia pada sumber, berjejak halaman, RTL-bila-Arab, dan prosesnya bisa dilanjutkan sesi lain.

## Peta folder
```
sistem-presentasi/
├── START_DI_SINI.md            ← file ini
├── SYSTEM_MANIFEST.md          ← identitas & kontrak
├── 00_RENCANA_KERANGKA.md      ← rencana dokumen (sejarah/perancangan)
├── PELAJARAN_DECK_01.md        ← pelajaran dari deck nyata #1
├── _sistem/
│   ├── 01_ATURAN_DESIGN_ISI_GAMBAR.md  ← aturan AKTIF (isi, desain, gambar, portabilitas)
│   ├── 02_KNOWLEDGE_DESIGN_VISUAL.md   ← basis pengetahuan desain + akumulasi riset + bahasa + layout
│   ├── 03_MEMAHAMI_KBUTUHAN_DAN_TUJUAN.md ← wajib: tangkap verbatim kebutuhan/tujuan + purpose-fit
│   ├── 04_QA_PRODUKSI.md               ← QA SETIAP produksi (otomatis + gerbang manusia)
│   └── qa_deck.py                      ← cek otomatis per-produksi (exit≠0 bila gagal)
└── deck-aktif/<nama-deck>/
    ├── bahan/                  ← sumber (PDF/dok)
    ├── BRIEF.md, PEMAHAMAN_BAHAN.md, CHECKLIST_CAKUPAN.md, OUTLINE.md,
    │   RENCANA_VISUAL.md, DAFTAR_GAMBAR.md, STATUS.md
    ├── gambar/                 ← aset gambar (M1/M3/M4)
    ├── build_deck_v*.py        ← skrip build (reproducible)
    ├── export_html.py          ← preview dari baca-balik .pptx
    └── keluaran/               ← .pptx + preview.html + index.html
```

## Alur produksi (5 tahap + 3 gerbang approval)
1. **Brief** → `BRIEF.md` (sumber, mode gambar, preferensi bullet/paragraf, slug).
2. **Pahami bahan** → `PEMAHAMAN_BAHAN.md` + `CHECKLIST_CAKUPAN.md`. **Arab = jalur VISI** (render→baca), ekstraksi hanya peta. → **G1** (bila bahan besar).
3. **Outline + Rencana Visual** → `OUTLINE.md` + `RENCANA_VISUAL.md`. → **G2**.
4. **Produksi** → jalankan `build_deck_v*.py` → `.pptx`; `export_html.py` → preview.
5. **Verifikasi** → baca-balik `.pptx` + buka visual + (bahasa non-default: tinjauan penutur asli WAJIB). → **G3**.

## Aturan yang mengikat (baca sebelum produksi)
- `_sistem/01` — kedalaman isi, desain, gambar multi-mode (M0–M4) + 2 batasan (teks tidak dibakar ke gambar; gambar boleh parsial), portabilitas.
- `_sistem/02` — prinsip desain (hasil riset, terakumulasi), aspect-ratio, bidi, **kompetensi bahasa**, library layout kaya, **mandat riset visual yang didokumentasikan**.

## Menjalankan build (reproducible)
```
python3 -m pip install --target /tmp/pptxlib python-pptx
PYTHONPATH=/tmp/pptxlib python3 build_deck_v*.py
PYTHONPATH=/tmp/pptxlib python3 export_html.py
```
(Hasil ke `keluaran/`. `/tmp` tidak persisten → install tiap sesi.)

## Unduh / distribusi
Di lingkungan lmarena, viewer/preview TIDAK bisa unduh biner dan link web dipagari token; jalur unduh yang didukung = **GitHub** (halaman file → Download raw). Setelah dijadikan repo sendiri, gunakan mekanisme repo itu.

## Status
Belum 100%: `_sistem/03+`, `_template/`, `_generator/`, dan perluasan validator masih direncanakan. Alur inti (G1–G3 + build) sudah berfungsi & terbukti pada deck nyata #1.
