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
| Sistem Presentasi | `sistem-presentasi/` | `0.4.2` Built & terverifikasi; **teraudit 1x** — audit independen Sedang 5 Sep 2026 (laporan `_meta/_internal/AUDIT_SISTEM_PRESENTASI_2026-09-05.md`): 11 temuan (2×P1 skrip, 3×P2 state deck, 6×P3) **semua diperbaiki 5 Sep 2026** di v0.3.0; **pegangan pengguna tersedia** (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md`, prompt pembuka+penutup); **v0.4.0 (5 Sep): mekanisme log sesi (`LOG_SESI`) diturunkan self-contained** (`_sistem/11_LOG_SESI.md`) + prompt pembuka/penutup diperbarui | 8 September 2026 | Unit aktif `deck-aktif/presentasi-tesis-fikih-hiasan-wanita/` (14 slide, isi diperpanjang sesuai tesis) — **deck#1 & prosesnya BUKAN sample** (lihat `PELAJARAN_DECK_01.md`). Bahan Arab via **visi**. Heading Q2 belum verbatim (rekonstruksi berlabel); pembimbing kosong; pemilik akan menambah butir. **v0.4.1 (5 Sep):** field checkpoint di `T6_STATUS.md`+STATUS deck, wording provenance + tabel Warisan — audit meta v1.3.0. **6 Sep:** rujukan protokol review independen (meta v1.4.0) + level trigger 3 baris di `ACCEPTANCE_TESTS.md`. **7 Sep (v0.4.2): + paket repo mandiri LULUS (7 September 2026, versi `0.4.2`)** — `validate_system.py` diadaptasi seperlunya; hasil pack lolos validator repo (0 warning) + validator sistem di dalam pack; protokol `_meta/PAKET_REPO_MANDIRI.md`; bukti `ACCEPTANCE_TEST_LOG.md` bagian "Paket repo mandiri". **8 Sep:** entri bukti paket digantikan entri baru (angka lama 86 berkas / 21 subset tidak reproduktif di HEAD karena dokumen bukti ikut mengubah subset — perbaikan meta v1.6.0: benih = dokumen aktif). Menunggu review independen L1. |
| Sistem Konten Kreator | `sistem-konten-kreator/` | `0.3.6` candidate — audit P0+P1 ditutup, belum divalidasi pemakaian nyata | 8 September 2026 | **F7 DITUTUP 6 Sep 2026** — AT-KK-05 / Run 7 **LULUS** + AT-KK-05b / Run 8 **LULUS**, keduanya `0.3.4`. Riwayat: Run 4 **GAGAL** (`0.3.2`); Run 5 **GAGAL-metode** (`0.3.3`); Run 6 lama **void**. Status/bukti: `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md` (Run 7 + Run 8). Status sistem: `sistem-konten-kreator/SYSTEM_MANIFEST.md`; PR #13 + #14 + #15 + #16 + #17 merged. **v0.3.5 (6 Sep):** protokol review independen diwariskan dari meta v1.4.0 — dokumen `PROTOKOL_REVIEW_INDEPENDEN.md` baru di root sistem + rujukan di 4 titik; aturan `00`/`05`/`06` tidak berubah (regresi AT-KK tidak terpicu). **7 Sep (v0.3.6): + paket repo mandiri LULUS (7 September 2026, versi `0.3.6`)** — validator sistem sendiri BARU di `_sistem/validate_system.py` (self-contained); hasil pack lolos validator repo (0 warning) + validator sistem di dalam pack; protokol `_meta/PAKET_REPO_MANDIRI.md`; bukti `ACCEPTANCE_TEST_LOG.md` bagian "Paket repo mandiri"; aturan `00`/`05`/`06` tetap tidak diubah. **8 Sep:** entri bukti paket digantikan entri baru (run ulang di HEAD; angkanya identik — bukti KK stabil — tapi sha sumber dan alat berubah, jadi entri baru menggantikan yang lama). Menunggu review independen L1. |

*(Tambah baris baru di bawah ini untuk tiap sistem baru yang dibangun)*

> **Catatan tanggal:** kolom "Terakhir Disentuh" mengikuti tanggal UTC sesi; peristiwa bertanggal WIB ditandai di log terkait. Riwayat penanggalan uji: `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md`.

---

## Yang sengaja TIDAK didaftarkan di tabel ini

- **`sistem-pilot-catatan-belajar/`** — bukan sistem domain, melainkan **fixture uji** untuk memvalidasi meta-sistem itu sendiri (behavioral test, recovery test FI-01 s/d FI-07). Statusnya `pilot-only — not released` di manifestnya sendiri. Pengecualian ini **keputusan sadar**, bukan kelalaian pencatatan — jangan "diperbaiki" dengan menambahkannya ke tabel di atas. Kalau suatu saat pilot ini dipromosikan jadi sistem nyata, itu keputusan tersendiri yang dicatat dulu.
- **Meta-sistem (`_meta/`)** — ini kerangka yang menaungi semua sistem, bukan salah satu isinya. Statusnya dilacak di `_meta/SYSTEM_MANIFEST.md` (saat ini `Released — v1.6.0`: pegangan pengguna wajib + log sesi berkelanjutan + kontrak warisan W-01…W-09 + tools regresi berbasis INDEKS + protokol review independen + paket repo mandiri + satu definisi dokumen aktif).
  - **File baru v1.6.0 (8 Sep 2026):** perbaikan akar masalah bukti basi — cakupan pemindaian jadi SATU definisi `dokumen_aktif()` di `tools/checkpoint_core.py` (dipakai validator + packager); benih subset `_meta/` = dokumen aktif saja; rujukan dokumen non-aktif dicatat di `PAKET_REPO.md`; AT-15 dapat L6; skenario P3 anti pembusukan daftar putih di `tools/test_failure_injection.py`. Tidak ada berkas baru — berkas yang diubah: `tools/checkpoint_core.py`, `tools/validate_repo.py`, `tools/pack_repo.py`, `tools/test_failure_injection.py`, `_meta/PAKET_REPO_MANDIRI.md`, `_meta/ACCEPTANCE_TESTS.md`, `_meta/FAILURE_INJECTION_TESTS.md`.
  - **File baru v1.5.0 (7 Sep 2026):** `_meta/PAKET_REPO_MANDIRI.md` — protokol mengeluarkan satu sistem jadi repo mandiri yang tervalidasi (alat: `tools/pack_repo.py`); rujukan 1 baris di `QUALITY_ASSURANCE_AND_EVOLUTION.md`, butir di `DEFINITION_OF_DONE.md`, skenario AT-15 di `ACCEPTANCE_TESTS.md`.
  - **File baru v1.4.0 (6 Sep 2026):** `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` — review independen oleh SESI LAIN sebagai lapisan verifikasi eksternal (permintaan pengguna pasca-F7); rujukan 1 baris di `QUALITY_ASSURANCE_AND_EVOLUTION.md`.

---

## Legenda Status

- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali
- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai
- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh
- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai
- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)


## Catatan pemindahan repo mandiri — 2026-09-08 (bukan penutupan gate)

- Sistem Presentasi: repo mandiri **BELUM tersedia di luar sandbox**, percobaan 2026-09-08 dari sha 1609cfba83798d168d171c67aaa1d9715988c14a, privat; createRepository ditolak integration, upload ZIP gagal EOF; [draft release tanpa aset](https://github.com/With-AI-Agent/Pembangun-Sistem/releases/tag/untagged-9cc6b35931837ea69df2) (ID release stabil 384501472), bukan klaim "dibuat" atau "tersedia sebagai aset release".
- Sistem Konten Kreator: repo mandiri **BELUM tersedia di luar sandbox**, percobaan 2026-09-08 dari sha 1609cfba83798d168d171c67aaa1d9715988c14a, privat; createRepository ditolak integration, upload ZIP gagal EOF; [draft release tanpa aset](https://github.com/With-AI-Agent/Pembangun-Sistem/releases/tag/untagged-2004269a4cf25d30081b) (ID release stabil 384500886), bukan klaim "dibuat" atau "tersedia sebagai aset release".
