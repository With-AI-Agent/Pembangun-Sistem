# Prompt Pembuka Universal — Sistem Konten Kreator

File ini berisi satu blok prompt siap pakai untuk memulai sesi apa pun di sistem ini. Cukup salin isi bagian "Prompt" di bawah ke chat pertama — prompt ini mengarahkan agent membangun konteks yang diperlukan lewat entry point (membaca konteks wajib sesuai jenis sesi) lalu menanyakan kamu mau melakukan apa. Ini arahan kerja, bukan jaminan bahwa agent sudah tahu segalanya: kalau ada file wajib yang hilang atau bertentangan, agent harus berhenti dan melapor.

> Untuk panduan lengkap dan penjelasan, baca `panduan/PANDUAN_PENGGUNA.md`.

---

## Prompt

```
Kamu adalah lmarena Agent yang terhubung ke repo sistem konten kreator ini.
Sebelum melakukan apa pun:

1. Baca `_sistem/START_DI_SINI.md` dan `_sistem/00_CARA_PAKAI_SISTEM.md`
2. Deteksi kondisi branch saat ini (baru/kosong vs lama/ada progres?)
3. Cek dan laporkan status semua PR yang masih terbuka
4. Cari file `LOG_SESI_*.md` terbaru (root repo / folder sistem / folder unit kerja). Kalau keadaannya `OPEN`, BACA dan laporkan keadaan sesi sebelumnya SEBELUM bertanya tujuan sesi — jangan tanya ulang konteks yang sudah tercatat di sana
5. Tanyakan: "Apa tujuan sesi ini?" (misal: mulai dari nol, buat channel baru, produksi konten, revisi, diskusi, cek konsistensi, atau lainnya)
6. Berdasarkan jawaban, baca sendiri file konteks wajib untuk jenis sesi itu — pakai tabel "Konteks Wajib per Jenis Sesi" di `_sistem/00_CARA_PAKAI_SISTEM.md`, bukan tafsiran bebas soal apa yang relevan. Sebutkan file kondisional yang kamu lewati beserta alasannya. TANPA perlu aku tempel manual isinya
7. Jangan mulai eksekusi/menulis file apa pun sebelum aku konfirmasi tujuan sesi ini sudah jelas

Setelah itu, bawa aku langsung ke langkah yang tepat sesuai tujuan.
```

---

## Catatan Penggunaan

- Prompt ini bisa dipakai dalam **keadaan apa pun**: sesi baru, sesi lanjutan, diskusi, produksi, revisi, atau hanya sekadar cek konsistensi.
- Di chat pertama, agent membaca konteks wajib untuk jenis sesi yang kamu sebut (tabel "Konteks Wajib per Jenis Sesi" di `_sistem/00_CARA_PAKAI_SISTEM.md`) dan melaporkan kondisi repo, termasuk file kondisional yang dilewati beserta alasannya. Di chat kedua (atau dalam sesi yang sama), kamu tinggal jelaskan apa yang kamu mau.
- Agent tidak akan memproses file di `panduan/` sebagai instruksi eksekusi kecuali kamu meminta secara eksplisit.
