# Aturan Log Sesi — Sistem Klinik (self-contained, W-02)

> Aturan ini disalin/diturunkan supaya sistem klinik tetap berfungsi penuh saat foldernya dibawa keluar dari repo master (prinsip folder-mandiri). Provenance: protokol checkpoint/recovery + template log sesi di folder _meta repo induk — dokumen itu TIDAK dibutuhkan saat runtime.

## Aturan inti

1. **Setiap sesi kerja di sistem ini** (bangun dokumen, rakit kit, jalankan run bengkel) memelihara SATU file `LOG_SESI_YYYY-MM-DD.md` di folder _log-sesi/ root repo (level repo/meta) — atau `LOG_SESI_YYYY-MM-DD_<n>.md` bila sudah ada sesi lain hari itu.
2. **Header "Keadaan Sesi" selalu segar** — dibaca pertama oleh agent baru: Keadaan `OPEN`/`CLOSED`, scope, di mana kita, sudah disepakati, masih terbuka, langkah berikutnya.
3. **Append + commit + push segera** setelah tiap pertukaran yang menghasilkan informasi baru (keputusan/koreksi/preferensi pemilik near-verbatim; proposal penting + dasar; kesepakatan/penolakan + alasan; fakta terverifikasi; state kerja; pertanyaan terbuka). BUKAN dump chat, BUKAN basa-basi, BUKAN mengulang isi STATUS (tunjuk path).
4. **Akhir sesi:** header → `CLOSED` (atau `OPEN` bila kerja memang dilanjutkan — tulis "dilanjutkan di mana"). PR dibuka tanpa auto-merge.
5. **Awal sesi baru (entry point):** cari LOG_SESI terbaru di _log-sesi/ dan folder sistem; bila `OPEN` → baca, laporkan, konfirmasi sebelum lanjut; bila `OPEN` tapi PR-nya ternyata sudah merged → tutup retrospektif dulu (edit hanya header + entri penutupan baru; kronologi lama append-only, tidak diedit).

## Kenapa (alasan kausal — fakta platform, bukan birokrasi)

Sesi agent bisa crash kapan saja dan sesi baru TIDAK punya akses ke chat lama — hanya file di repo yang bertahan. Setelah PR di-merge/di-close, sesi TIDAK BISA push lagi (akses dicabut platform — bukan "sebaiknya jangan"). Tanpa log + commit segera: konteks hilang permanen dan kerja pasca-merge terjebak. Mekanisme yang sama PERSIS inilah yang menjadi barang tanam utama klinik ke sistem-sistem target (Kontrak Tanaman) — sistem ini menerapkannya pada dirinya sendiri lebih dulu.

## Format file

Template: ikuti struktur header + "Kronologi (append, terbaru di bawah)" — contoh hidup: berkas-berkas di _log-sesi/ repo ini (mis. pola laporan awal + entri per putaran diskusi yang dipakai saat Discovery Level-0 11 Sep 2026).
