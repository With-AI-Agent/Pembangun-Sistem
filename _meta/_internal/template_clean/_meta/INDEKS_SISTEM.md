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
| (belum ada) | | | | |

---

## Legenda Status

- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali
- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai
- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh
- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai
- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)
