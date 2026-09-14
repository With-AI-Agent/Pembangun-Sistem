# START DI SINI — Sistem Klinik

> Entry point sistem ini. Sesi agent yang bekerja pada folder sistem ini mulai dari sini — SETELAH entry point tingkat repo selesai (laporan awal sesuai template laporan sesi, cek PR menggantung, cek INDEKS_SISTEM, cek LOG_SESI terbaru; aturannya di dokumen cara-kerja repo induk — provenance tanpa backtick: _meta/00_CARA_KERJA_META.md).
> Sistem ini "klinik" untuk sistem-sistem milik pemilik: 1 run = 1 kunjungan perawatan ke 1 sistem target. Dua panggung (K-11): SUNTIK (rawat jalan — target di repo eksternal, kit disalin ke sana) dan RAWAT INAP (target = folder sistem di repo meta ini — alur standar meta + aturan klinik; sistemnya tinggal di repo sebagai warga kelas satu).

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

## Jenis sesi 3 — Menjalankan run RAWAT INAP (target = folder sistem di repo ini, K-11)

1. **Prasyarat:** pemilik telah meletakkan folder sistem target di repo ini — lokasinya mengikuti konvensi folder sistem repo ini, **dibaca dari `_meta/INDEKS_SISTEM.md` (single source of truth path) — jangan menebak/hardcode**. Bila foldernya belum ada, BERHENTI dan tanya pemilik.
2. Orientasi: baca manifest / STATUS / LOG_SESI terbaru folder target dulu. Lalu baca `_sistem/01_ALUR_RUN.md` PENUH — inilah aturan run. Panggung rawat inap membaca **MASTER di tempatnya** — tidak ada salinan kit, tidak ada stamp, tidak ada peleburan kit (kit eksklusif suntik; §1.2 + §12).
3. **Tanya pemilik apa yang mau dilakukan** — audit menyeluruh / perbaiki X / upgrade Y — SEBELUM menyentuh apa pun. G-Rencana berlaku utuh: diagnosis + rencana disetujui pemilik sebelum satu byte pun ditulis (Tahap B read-only).
4. Tahap A–F, dua gerbang, borongan K-10, REKAM-KLINIK + cap versi kit — identik dengan suntik (adaptasi dua panggung §12; format laporan diagnosis §4.5, bagian 7 = catatan folder tamu).
5. **PR = PR meta normal** (perubahan tertanam + rekam + STATUS target + sinkron INDEKS) — TANPA auto-merge; merge = keputusan pemilik. Pasca-run: sistem TETAP di repo sebagai warga kelas satu (terdaftar INDEKS_SISTEM); penghapusan folder = keputusan sadar pemilik, dicatat di log — tidak pernah diam-diam.

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
| 2026-09-14 UTC / 15 Sep WIB | Jenis sesi 3 ditulis ulang: BENGKEL (staging `_bengkel/`) → RAWAT INAP (folder sistem target di repo ini; alur standar meta + aturan klinik; master dibaca di tempatnya; PR normal → merge pemilik; sistem tetap warga kelas satu) + header dua panggung disinkron | K-11 — ratifikasi eksplisit pemilik; interaksi yang dikehendaki: pemilik meletakkan folder + tempel prompt universal → agent orientasi lalu MENANYA apa yang mau dilakukan sebelum menyentuh apa pun |
