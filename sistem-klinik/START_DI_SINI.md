# START DI SINI — Sistem Klinik

> Entry point sistem ini. Sesi agent yang bekerja pada folder sistem ini mulai dari sini — SETELAH entry point tingkat repo selesai (laporan awal sesuai template laporan sesi, cek PR menggantung, cek INDEKS_SISTEM, cek LOG_SESI terbaru; aturannya di dokumen cara-kerja repo induk — provenance tanpa backtick: _meta/00_CARA_KERJA_META.md).
> Sistem ini "klinik" untuk sistem-sistem milik pemilik: 1 run = 1 kunjungan perawatan ke 1 sistem target. Dua panggung: SUNTIK (rawat jalan, default — agent bekerja di repo target) dan BENGKEL (rawat inap, pengecualian — salinan target menginap di repo meta).

## Peta baca minimum (semua jenis sesi)

1. `STATUS.md` — keadaan kerja terakhir (field deterministik; jangan tanya ulang yang sudah tercatat)
2. `SYSTEM_MANIFEST.md` — identitas, tahap, bentuk, titik gerbang
3. LOG_SESI terbaru yang masih `OPEN` di `_log-sesi/` (level repo) — bila ada, lanjutkan konteksnya, jangan mulai dari nol

Sisanya baca SESUAI jenis sesi di bawah — jangan baca seluruh folder sekaligus.

## Jenis sesi 1 — Melanjutkan pembangunan / kerangka

1. Baca `00_RENCANA_KERANGKA.md` bagian "Langkah setelah rencana merge" — urutan wajibnya ada di situ; `STATUS.md` menyebut tahap terakhir yang selesai.
2. Kerjakan SATU dokumen penuh sampai disetujui, baru lanjut dokumen berikutnya (bukan banyak sekaligus).
3. Gerbang: approval pemilik per dokumen; tanya diborong (model K-10 di rencana, bagian Titik Penguncian).

## Jenis sesi 2 — Menyiapkan & menjalankan run SUNTIK (rawat jalan)

Run suntik terjadi di REPO TARGET, bukan di folder ini. Yang dikerjakan di meta sebelum run:

1. **Cek kit tidak basi** (fail-closed): stamp `sha` di setiap `kit/aturan/*.md` harus sama dengan blob sha master `_sistem/` aktual, dan `kit/VERSI.txt` = field Versi `SYSTEM_MANIFEST.md` (aturan: `06_RITME_KIT.md` §2). Beda → sinkron dulu, jangan bawa kit basi.
2. Baca `_sistem/01_ALUR_RUN.md` secara penuh — inilah aturan run (Tahap A–F, dua gerbang, adaptasi panggung, fail-closed).
3. Di repo target: salin folder `kit/` ke workspace target (TIDAK pernah ikut commit git target — Kebijakan Lebur aturan 4), lalu kirim isi `kit/PROMPT-ENTRI-KIT.md` sebagai prompt pembuka sesi target.
4. Gerbang yang menghentikan: G-Rencana (sebelum menyentuh target), G-Final (sebelum peleburan/PR), overwrite & install kapabilitas selalu per-item diborong (K-10). Merge = pemilik.
5. Setelah run: **Tahap F Panen wajib** — temuan cacat/celah aturan dilaporkan balik ke folder ini (usulan entri `02_KATALOG_CACAT.md` atau perbaikan aturan; boleh nihil, diam tidak sah).

## Jenis sesi 3 — Menjalankan run BENGKEL (rawat inap)

1. Baca `_bengkel/README.md` dulu — aturan menginap: salinan hidup HANYA di branch kerja, TIDAK pernah merge ke main repo meta, hygiene ukuran K-9 (yang dibedah saja, aset di-exclude), pemulangan via patch/download, PR berisi laporan lalu di-close, branch dihapus (keputusan sadar pemilik).
2. Sisanya sama dengan suntik — ikuti `_sistem/01_ALUR_RUN.md` §12 (adaptasi dua panggung).

## Jenis sesi 4 — Audit / evolusi kit

1. Cek trigger audit di `SYSTEM_MANIFEST.md` bagian Quality & Evolution (tiap 3 run selesai; cacat berulang di 2+ target; perubahan aturan inti; perintah pemilik).
2. Jalankan skenario di `ACCEPTANCE_TESTS.md` (AT-KL) — bukti eksekusi dicatat di `ACCEPTANCE_TEST_LOG.md` (bukti pakai struktur/exit code, bukan angka yang berubah-ubah — lihat C-04 di katalog).
3. Perubahan aturan master `_sistem/` wajib, sebelum PR: lolos acceptance test + sinkron `kit/` (stamping ulang berkas yang berubah) + versi kit naik + satu baris Log Keputusan.
4. Verifikasi mekanis minimal: `python3 _sistem/validate_system.py` harus PASS; gerbang folder-mandiri dijalankan dari root repo induk (alat meta check_selfcontained — provenance, tanpa backtick: tools/check_selfcontained.py).

## Jenis sesi 5 — Review PR klinik

Baca deskripsi PR + berkas yang disentuh. Tidak ada auto-merge — merge selalu keputusan pemilik. Prompt review independen dibangkitkan dari alat repo induk (provenance, tanpa backtick: tools/review_prompt.py) dan ditempel sebagai satu blok berpagar di pesan terakhir sesi.

## Penutup sesi (semua jenis)

Ikuti bagian "Prompt Penutup" di `PROMPT_ENTRI_UNIVERSAL.md`: STATUS.md disegarkan, header LOG_SESI ditutup, INDEKS_SISTEM diperbarui, semua ter-push sebelum PR (setelah merge/close sesi tidak bisa push lagi — fakta platform), PR tanpa auto-merge.

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-14 | Berkas dibuat (Langkah 7 rencana kerangka) | Rencana menetapkan entry point per jenis sesi (bangun / run suntik / run bengkel / audit); sebelumnya navigasi sementara lewat 00_RENCANA_KERANGKA + PROMPT_ENTRI_UNIVERSAL |
