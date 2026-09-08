# Indeks Sistem

### Daftar semua sistem yang ada di repo ini, dengan status dan tanggal terakhir disentuh. Dicatat MANUAL oleh agent setiap kali selesai kerja di suatu sistem — TIDAK mengandalkan pembacaan git history. Dibaca di awal sesi untuk menentukan apakah perlu menawarkan audit sebelum lanjut kerja (lihat `00_CARA_KERJA_META.md`).

---

## Cara pakai

- **Sebelum mulai kerja di suatu sistem:** cek baris sistem itu di tabel bawah. Kalau "Terakhir Disentuh" sudah lama (pengguna yang menilai apa itu "lama" — tidak ada angka pasti, tergantung konteks), tawarkan audit dulu.
- **Setelah selesai kerja di suatu sistem (apapun jenis kerjanya):** update baris sistem itu — tanggal hari ini, dan status terbaru.
- **Sistem baru:** tambah baris baru begitu `00_RENCANA_KERANGKA.md`-nya sudah di-merge ke `main` (lihat `01_DISCOVERY_LEVEL_0.md`).

---

## Daftar Sistem

| Nama Sistem | Folder | Status | Terakhir Disentuh | Catatan |
|---|---|---|---|---|
| Sistem Presentasi | `sistem-presentasi/` | belum mandiri — jalankan python3 tools/check_selfcontained.py --sistem sistem-presentasi | 8 September 2026 | Rujukan keluar folder dan rujukan ke diri sendiri menjadi pekerjaan PR C; PR A tidak menyunting isi folder sistem ini. |
| Sistem Konten Kreator | `sistem-konten-kreator/` | belum mandiri — jalankan python3 tools/check_selfcontained.py --sistem sistem-konten-kreator | 8 September 2026 | Rujukan keluar folder dan rujukan ke diri sendiri menjadi pekerjaan PR B; PR A tidak menyunting isi folder sistem ini. |

*(Tambah baris baru di bawah ini untuk tiap sistem baru yang dibangun)*

> **Catatan tanggal:** kolom "Terakhir Disentuh" mengikuti tanggal UTC sesi; peristiwa bertanggal WIB ditandai di log terkait. Riwayat penanggalan uji: `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md`.

---

## Yang sengaja TIDAK didaftarkan di tabel ini

- **`sistem-pilot-catatan-belajar/`** — bukan sistem domain, melainkan **fixture uji** untuk memvalidasi meta-sistem itu sendiri (behavioral test, recovery test FI-01 s/d FI-07). Statusnya `pilot-only — not released` di manifestnya sendiri. Pengecualian ini **keputusan sadar**, bukan kelalaian pencatatan — jangan "diperbaiki" dengan menambahkannya ke tabel di atas. Kalau suatu saat pilot ini dipromosikan jadi sistem nyata, itu keputusan tersendiri yang dicatat dulu.
- **Meta-sistem (`_meta/`)** — ini kerangka yang menaungi semua sistem, bukan salah satu isinya. Statusnya dilacak di `_meta/SYSTEM_MANIFEST.md` (saat ini `Released — v1.10.0`, terakhir disentuh 8 September 2026: pegangan pengguna wajib + log sesi berkelanjutan + kontrak warisan W-01…W-09 + tools regresi berbasis INDEKS + protokol review independen + folder sistem sebagai deliverable).
  - **Bagian baru v1.10.0 (8 Sep 2026):** protokol folder mandiri menggantikan packager lama; alat baru `tools/check_selfcontained.py` menjadi gerbang selesai; tools/pack_repo.py pensiun dengan jejak di `_meta/PAKET_REPO_MANDIRI.md`; template bersih membawa sistem-benih dengan validator dan satu salinan berlabel nyata. Disetujui pemilik PR A; menunggu review independen L1.
  - **Bagian baru v1.9.0 (8 Sep 2026):** prompt review independen dibangkitkan alat, bukan dikarang — pembangkit baru di `tools/` (nomor PR, base/head sha, daftar berkas pelindung diambil dari data PR di GitHub), bagian "Sumber prompt" di `_meta/PROTOKOL_REVIEW_INDEPENDEN.md`, satu baris checklist penutupan sesi di `_meta/00_CARA_KERJA_META.md` + `_meta/DEFINITION_OF_DONE.md`, bagian "Minta Review, Tanpa Perantara" di `PANDUAN_PENGGUNA.md` + langkah penutup di `PROMPT_ENTRI_UNIVERSAL.md`. Disetujui pemilik 8 Sep 2026 ("mekanisme harus bisa dipakai tanpa perantara sesi"). Menunggu review independen L1; penggabungan = keputusan pemilik langsung.
  - **File baru v1.6.0 (8 Sep 2026):** perbaikan akar masalah bukti basi — cakupan pemindaian jadi SATU definisi `dokumen_aktif()` di `tools/checkpoint_core.py`. Pada masa packager lama, definisi ini juga dipakai untuk benih subset meta; mekanisme itu kini pensiun. Berkas yang saat itu diubah termasuk checkpoint_core, validator, packager lama, injeksi kegagalan, protokol paket, acceptance tests, dan failure injection tests.
  - **File baru v1.5.0 (7 Sep 2026):** `_meta/PAKET_REPO_MANDIRI.md` lahir sebagai protokol paket repo mandiri lama; alat pelaksananya tools/pack_repo.py kini pensiun per keputusan pemilik 8 Sep 2026.
  - **File baru v1.4.0 (6 Sep 2026):** `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` — review independen oleh SESI LAIN sebagai lapisan verifikasi eksternal (permintaan pengguna pasca-F7); rujukan 1 baris di `QUALITY_ASSURANCE_AND_EVOLUTION.md`.

---

## Legenda Status

- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali
- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai
- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh
- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai
- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)


## Catatan historis pemindahan repo mandiri lama — 2026-09-08

- Sistem Presentasi: percobaan pemindahan lama tidak menjadi bukti kemandirian folder. Status berlaku sekarang: belum mandiri — jalankan python3 tools/check_selfcontained.py --sistem sistem-presentasi.
- Sistem Konten Kreator: percobaan pemindahan lama tidak menjadi bukti kemandirian folder. Status berlaku sekarang: belum mandiri — jalankan python3 tools/check_selfcontained.py --sistem sistem-konten-kreator.
