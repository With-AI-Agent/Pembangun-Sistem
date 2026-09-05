# ACCEPTANCE TEST LOG — Sistem Presentasi

> Bukti per run. Lihat skenario di `ACCEPTANCE_TESTS.md`.

## Run 2026-09-05 — AT-SP-15 SIMULASI end-to-end (perkataan pemilik kiriman 2)
Input: `deck-aktif/presentasi-tesis-fikih-hiasan-wanita/PERKATAAN_PEMILIK_VERBATIM.md` (Arab, verbatim).

| Tahap | Hasil | Catatan |
|---|---|---|
| Brief (G1-gen) | verbatim disimpan; traceability 13 butir→slide; tujuan=alat sidang tesis | satu bagian=satu slide (permintaan eksplisit) |
| G1 Peta | kartu 13/13; pertanyaan diperbarui: Q1(ص٩٠)+Q3(ص١٤٦) verbatim, Q2 rekonstruksi berlabel | jalur VISI |
| G2 Outline+Visual | outline mengikuti urutan pemilik; palet A; aspect-safe; purpose-fit: temuan & pertanyaan menonjol, metode 1 slide/sesuai butir | disetujui pola v2-v6 |
| Produksi | `build_deck_v6.py` → 14 slide (judul + 13 butir) | satu bagian/slide; Q1–Q3 digabung tanpa jawaban |
| QA otomatis | `qa_deck.py` exit 0 (14 slide, 0 fail, 0 warn) | jalur (a) |
| QA manusia | preview `preview.html` (jalur b); putusan final = pemilik (jalur c) | Q2 & nama pembimbing menunggu tinjauan pemilik |
| G3 | diajukan; menunggu approval pemilik | |

**Temuan utk Log pelajaran:** heading "السؤال" tak terdeteksi ekstraksi → wajib VISI; jawaban Q1 sangat panjang sehingga Q2/Q3 di akhir Bab 4; pemilik akan menambah butir kemudian → struktur harus mudah ditambah slide.
