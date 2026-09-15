# 04 — QA Per-Produksi (berlaku SETIAP pembuatan, bukan per-kasus)

> Menjawab: "kualitas harus benar di **setiap** pembuatan". QA ini dijalankan tiap kali `.pptx` dibangun, sebelum diajukan ke G3. Gabungan cek otomatis (skrip) + cek manusia (gerbang).

## A. Cek otomatis — jalankan `qa_deck.py`
```
PYTHONPATH=/tmp/pptxlib python3 _sistem/qa_deck.py <path-ke-pptx>
```
Yang dicek (exit≠0 bila gagal):
1. Berkas terbuka; jumlah slide ≥ rencana.
2. Tiap slide punya paragraf `rtl=1` (untuk deck Arab) & run ber-font complex-script (`a:ea`).
3. **Tidak ada** tashkeel tersisa dan **tidak ada** karakter bidi-riskan `( ) — +` dalam teks Arab.
4. Tiap slide punya **Notes** terisi (naskah pembicara tidak di slide).
5. Gambar: laporkan nilai crop (crop>0 = aspect-safe); gambar tanpa crop pada kotak non-proporsional = peringatan gepeng.
6. Tabel (bila direncanakan) ada & terisi.

## B. Cek manusia / gerbang (tidak bisa diotomasi)
1. **Bahasa:** untuk bahasa non-default, tinjauan penutur/kompeten asli WAJIB (02.G). Agent tidak mensertifikasi sendiri.
2. **Purpose-fit:** jalankan 03.C (cocok tujuan, traceability butir↔slide).
3. **Kedalaman isi:** tidak over-summarize; temuan di depan (01.A).
4. **Desain:** prinsip 02.A (alignment/contrast/whitespace/hierarki), aspect-ratio 02.B, layout kaya bila perlu 02.H.
5. **Buka visual** (preview/PowerPoint) — struktur lulus ≠ tampilan bagus.

## C. Pencatatan
Hasil QA (otomatis + manusia) dicatat di `STATUS.md` deck + tiap temuan/koreksi masuk Log & (bila pelajaran umum) ke `PELAJARAN_DECK_*.md` / `02`. Dengan ini tiap produksi menaikkan mutu sistem, dan kesalahan tidak terulang.

## Log
| Tanggal | Keputusan | Oleh |
|---|---|---|
| 2026-09-05 | QA per-produksi ditetapkan; qa_deck.py dibuat | agent |
