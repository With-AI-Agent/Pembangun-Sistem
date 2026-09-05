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
├── PELAJARAN_DECK_01.md        ← catatan kegagalan+pelajaran deck #1 (**BUKAN sample**)
├── _sistem/
│   ├── 01_ATURAN_DESIGN_ISI_GAMBAR.md  ← aturan AKTIF (isi, desain, gambar, portabilitas)
│   ├── 02_KNOWLEDGE_DESIGN_VISUAL.md   ← basis pengetahuan desain + akumulasi riset + bahasa + layout
│   ├── 03_MEMAHAMI_KBUTUHAN_DAN_TUJUAN.md ← wajib: tangkap verbatim kebutuhan/tujuan + purpose-fit
│   ├── 04_QA_PRODUKSI.md               ← QA SETIAP produksi (otomatis + gerbang manusia)
│   ├── 05_SUMBER_DAN_ANTI_NGARANG.md   ← jejak sumber, 3 tingkat, fail-closed
│   ├── 06_PRINSIP_DESIGN_BERBASIS_BUKTI.md ← lantai desain + override sah
│   ├── 07_MODE_GAMBAR_DAN_LISENSI.md   ← M0–M4, G-1, G-2, gerbang lisensi M4
│   ├── 08_PERANCANGAN_BERBASIS_REKOMENDASI.md ← paket 5 bagian, dasar sah
│   ├── 09_PEMAHAMAN_BAHAN_MENDALAM.md  ← 5 langkah, Arab=visi, fail-closed
│   ├── 10_RENDER_DAN_VERIFIKASI.md     ← build + 3 jalur verifikasi
│   ├── qa_deck.py                      ← cek otomatis per-produksi
│   └── validate_system.py              ← cek kelengkapan struktur sistem+deck
├── _generator/  G1_BRIEF · G2_VISUAL · G3_KETENTUAN   ← prompt Discovery (berbasis rekomendasi)
├── _template/   T1–T9                                  ← blanko living-docs
└── ACCEPTANCE_TESTS.md                                 ← skenario uji + prosedur SIMULASI
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
**Struktur lengkap sesuai rencana kerangka** (diverifikasi `validate_system.py` exit 0, 5 Sep 2026): `_sistem/01–10`, `_generator/G1–G3`, `_template/T1–T9`, acceptance tests, validator, QA per-produksi. **Deck nyata #1 HANYA unit kerja & sumber pelajaran anti-pola — BUKAN sample/contoh** (prosesnya cacat: sesi perancangan isi & visual dilewati; lihat `PELAJARAN_DECK_01.md`). Yang inherently butuh manusia: tinjauan bahasa asli & approval gerbang (by design).
