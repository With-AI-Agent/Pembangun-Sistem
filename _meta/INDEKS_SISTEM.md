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
| Sistem Presentasi | `sistem-presentasi/` | `0.4.1` Built & terverifikasi; **teraudit 1x** — audit independen Sedang 5 Sep 2026 (laporan `_meta/_internal/AUDIT_SISTEM_PRESENTASI_2026-09-05.md`): 11 temuan (2×P1 skrip, 3×P2 state deck, 6×P3) **semua diperbaiki 5 Sep 2026** di v0.3.0; **pegangan pengguna tersedia** (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md`, prompt pembuka+penutup); **v0.4.0 (5 Sep): mekanisme log sesi (`LOG_SESI`) diturunkan self-contained** (`_sistem/11_LOG_SESI.md`) + prompt pembuka/penutup diperbarui | 5 September 2026 | Unit aktif `deck-aktif/presentasi-tesis-fikih-hiasan-wanita/` (14 slide, isi diperpanjang sesuai tesis) — **deck#1 & prosesnya BUKAN sample** (lihat `PELAJARAN_DECK_01.md`). Bahan Arab via **visi**. Heading Q2 belum verbatim (rekonstruksi berlabel); pembimbing kosong; pemilik akan menambah butir. **v0.4.1 (5 Sep):** field checkpoint di `T6_STATUS.md`+STATUS deck, wording provenance + tabel Warisan — audit meta v1.3.0. |
| Sistem Konten Kreator | `sistem-konten-kreator/` | `0.3.3` candidate — audit P0+P1 ditutup, belum divalidasi pemakaian nyata | 6 September 2026 | **F7 TERBUKA — Run 5 berjalan.** AT-KK-05 / Run 4 **GAGAL**, `0.3.2-warisan-sync`; AT-KK-05 / Run 5 **berjalan** (dicatat di log; PR #14 review, belum merged); AT-KK-05b / Run 6 **dijadwalkan**, `0.3.3`. Riwayat: AT-KK-05 / Run 2 dan AT-KK-05b / Run 3 **LULUS**, `0.3.1-audit-remediation`. Status/bukti: `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md` (Run 5). Status sistem: `sistem-konten-kreator/SYSTEM_MANIFEST.md`; PR #13 merged, PR #14 review. |

*(Tambah baris baru di bawah ini untuk tiap sistem baru yang dibangun)*

> **Catatan tanggal:** kolom "Terakhir Disentuh" mengikuti tanggal UTC sesi; peristiwa bertanggal WIB ditandai di log terkait. Riwayat penanggalan uji: `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md`.

---

## Yang sengaja TIDAK didaftarkan di tabel ini

- **`sistem-pilot-catatan-belajar/`** — bukan sistem domain, melainkan **fixture uji** untuk memvalidasi meta-sistem itu sendiri (behavioral test, recovery test FI-01 s/d FI-07). Statusnya `pilot-only — not released` di manifestnya sendiri. Pengecualian ini **keputusan sadar**, bukan kelalaian pencatatan — jangan "diperbaiki" dengan menambahkannya ke tabel di atas. Kalau suatu saat pilot ini dipromosikan jadi sistem nyata, itu keputusan tersendiri yang dicatat dulu.
- **Meta-sistem (`_meta/`)** — ini kerangka yang menaungi semua sistem, bukan salah satu isinya. Statusnya dilacak di `_meta/SYSTEM_MANIFEST.md` (saat ini `Released — v1.3.0`: pegangan pengguna wajib + log sesi berkelanjutan + kontrak warisan W-01…W-09 + tools regresi berbasis INDEKS).

---

## Legenda Status

- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali
- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai
- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh
- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai
- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)
