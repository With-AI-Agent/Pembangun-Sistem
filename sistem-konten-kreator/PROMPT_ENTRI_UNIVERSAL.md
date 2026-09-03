# Prompt Pembuka Universal — Sistem Konten Kreator

File ini berisi satu blok prompt siap pakai untuk memulai sesi apa pun di sistem ini. Cukup salin isi bagian "Prompt" di bawah ke chat pertama — kemudian agent akan otomatis memahami semua konteks dan tanya kamu mau melakukan apa.

> Untuk panduan lengkap dan penjelasan, baca `panduan/PANDUAN_PENGGUNA.md`.

---

## Prompt

```
Kamu adalah lmarena Agent yang terhubung ke repo sistem konten kreator ini.
Sebelum melakukan apa pun:

1. Baca `_sistem/START_DI_SINI.md` dan `_sistem/00_CARA_PAKAI_SISTEM.md`
2. Deteksi kondisi branch saat ini (baru/kosong vs lama/ada progres?)
3. Cek dan laporkan status semua PR yang masih terbuka
4. Tanyakan: "Apa tujuan sesi ini?" (misal: mulai dari nol, buat channel baru, produksi konten, revisi, diskusi, cek konsistensi, atau lainnya)
5. Berdasarkan jawaban, baca sendiri file sistem yang relevan — TANPA perlu aku tempel manual isinya
6. Jangan mulai eksekusi/menulis file apa pun sebelum aku konfirmasi tujuan sesi ini sudah jelas

Setelah itu, bawa aku langsung ke langkah yang tepat sesuai tujuan.
```

---

## Catatan Penggunaan

- Prompt ini bisa dipakai dalam **keadaan apa pun**: sesi baru, sesi lanjutan, diskusi, produksi, revisi, atau hanya sekadar cek konsistensi.
- Di chat pertama, agent akan membaca semua file sistem yang relevan dan melaporkan kondisi repo. Di chat kedua (atau dalam sesi yang sama), kamu tinggal jelaskan apa yang kamu mau.
- Agent tidak akan memproses file di `panduan/` sebagai instruksi eksekusi kecuali kamu meminta secara eksplisit.
