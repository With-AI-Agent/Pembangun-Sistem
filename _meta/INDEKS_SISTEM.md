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
| Sistem Presentasi | `sistem-presentasi/` | `0.2.0` Built & terverifikasi — struktur lengkap, audit otomatis exit 0, **di-merge ke main 5 Sep 2026 atas permintaan pengguna**; belum audit independen | 5 September 2026 | Unit aktif `deck-aktif/presentasi-tesis-fikih-hiasan-wanita/` (14 slide, isi diperpanjang sesuai tesis) — **deck#1 & prosesnya BUKAN sample** (lihat `PELAJARAN_DECK_01.md`). Bahan Arab via **visi**. Heading Q2 belum verbatim (rekonstruksi berlabel); pembimbing kosong; pemilik akan menambah butir. |
| Sistem Konten Kreator | `sistem-konten-kreator/` | Sedang dibangun — audit P0+P1 ditutup, gate checkpoint/recovery sudah teruji, belum divalidasi pemakaian nyata | 4 September 2026 | Manifest `0.3.1-audit-remediation`. Kandidat sistem contoh; belum ditetapkan sebagai acuan final. **AT-KK-05 LULUS** (2026-09-04, Run 2) dan **AT-KK-05b LULUS** (2026-09-05, Run 3) — keduanya clean run di sesi agent baru pada versi sistem yang sama; bukti di `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md`, tabel Rekaman Hasil di `sistem-konten-kreator/ACCEPTANCE_TESTS.md`. Karena itu gate "Prosedur checkpoint dan recovery diuji" **DITUTUP 5 Sep 2026** di `sistem-konten-kreator/SYSTEM_MANIFEST.md`. Fixture produksi pertama: `channel-fixture-narasi-sejarah/` + `_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/` (bahan uji, **bukan** penutup L-04). Gate tersisa: Brand Core approved/merged (belum ada channel nyata), pilot end-to-end 1 channel terisi penuh (L-04), acceptance test sistem LULUS — sisa AT-KK-01/02/03/03b/04/06/07/08 (L-05) |

*(Tambah baris baru di bawah ini untuk tiap sistem baru yang dibangun)*

> **Catatan tanggal (ditambahkan 4 Sep 2026, sesi `arena/01a06d7b`):** kolom "Terakhir Disentuh" memakai tanggal UTC sesi, sedangkan log uji Sistem Konten Kreator mencatat sebagian peristiwa dengan tanggal WIB — contoh: AT-KK-05b tercatat 2026-09-05 WIB padahal PR-nya (#7) di-merge 2026-09-04 17:07 UTC. Keduanya peristiwa yang sama, bukan dua kejadian berbeda. Baris di atas diselaraskan ke `SYSTEM_MANIFEST.md` + Rekaman Hasil karena sebelumnya masih menulis kedua test itu sebagai "dry run / belum LULUS" dan masih mencantumkan "recovery teruji bersih" sebagai gate tersisa — sudah tidak benar sejak PR #6 dan #7.

---

## Yang sengaja TIDAK didaftarkan di tabel ini

- **`sistem-pilot-catatan-belajar/`** — bukan sistem domain, melainkan **fixture uji** untuk memvalidasi meta-sistem itu sendiri (behavioral test, recovery test FI-01 s/d FI-07). Statusnya `pilot-only — not released` di manifestnya sendiri. Pengecualian ini **keputusan sadar**, bukan kelalaian pencatatan — jangan "diperbaiki" dengan menambahkannya ke tabel di atas. Kalau suatu saat pilot ini dipromosikan jadi sistem nyata, itu keputusan tersendiri yang dicatat dulu.
- **Meta-sistem (`_meta/`)** — ini kerangka yang menaungi semua sistem, bukan salah satu isinya. Statusnya dilacak di `_meta/SYSTEM_MANIFEST.md` (saat ini `Released — v1.0.0`).

---

## Legenda Status

- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali
- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai
- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh
- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai
- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)
