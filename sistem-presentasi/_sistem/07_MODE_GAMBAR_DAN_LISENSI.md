# 07 — Mode Gambar & Lisensi (M0–M4) + Aturan Keras Penempatan

| Mode | Isi | Risiko | Kapan |
|---|---|---|---|
| M0 | teks+struktur | none | deck padat argumen; BUKAN mode gagal |
| M1 | visual milik pengguna (figur skripsi/file sendiri) | paling aman | default sidang |
| M2 | diagram/grafik dari data nyata (generate kode) | none | slide berangka; angka wajib dari sumber |
| M3 | gambar AI | kejujuran | ilustrasi konsep SAJA; label "ilustrasi AI" terlihat; DILARANG untuk data/bukti |
| M4 | gambar internet | paling berisiko | hanya bila M1–M3 tak sanggup; lewat gerbang lisensi |

Mode dipilih per deck di `BRIEF.md`; per-slide boleh override dengan alasan tercatat.

## Aturan G-1: teks TIDAK boleh jadi bagian gambar
- Semua teks yang mungkin diubah wajib di text frame nyata.
- Prompt generate WAJIB: *no text, no letters, no words, no numbers, no watermark*.
- Verifikasi 3 lapis: (a) prompt melarang teks; (b) agent **melihat sendiri** hasilnya tiap sesi (jangan warisi klaim sesi lain); (c) pengguna lihat preview di G2.
- Pengecualian: M1 (dokumen asli pengguna) boleh mengandung teks.

## Aturan G-2: gambar di AREA tertentu, bukan otomatis penuh
- Geometri eksplisit (area, w, h) di `RENCANA_VISUAL.md`; teks tetap punya ruang.
- Slide penuh hanya bila diminta eksplisit (pembuka/penutup/kutipan).
- **Rasio gambar wajib = rasio area** (jangan gepeng); bila tak cocok, sesuaikan area, bukan paksa gambar. (Implementasi: crop aspect-safe — lihat build_deck & 02.B.)

## Gerbang lisensi M4
1. Daftar putih = **kriteria**: sumber yang blok lisensinya bisa dibaca & diverifikasi (Wikimedia terbukti). Bukan daftar situs tetap.
2. Wajib baca blok lisensi; catat lisensi, pemegang hak, atribusi, flag `NC`/`SA`.
3. Lisensi tak terbaca → `TIDAK DIKETAHUI` → **tolak**; tawarkan mode lain.
4. Pengguna setujui tiap gambar M4 **satu per satu** di G2.
5. Atribusi di slide (catatan kaki) **dan** `DAFTAR_GAMBAR.md`.

## Log
| Tanggal | Keputusan | Oleh |
|---|---|---|
| 2026-09-05 | Ditulis dari kerangka + permintaan pengguna 4 Sep | agent |
