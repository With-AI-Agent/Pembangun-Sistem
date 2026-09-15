# Prompt Pembuka Universal — Sistem Presentasi

File ini berisi satu blok prompt siap pakai untuk memulai sesi apa pun di sistem ini. Cukup salin isi bagian "Prompt" di bawah ke chat pertama — prompt ini mengarahkan agent membangun konteks yang diperlukan lewat entry point, lalu menanyakan kamu mau melakukan apa. Ini arahan kerja, bukan jaminan bahwa agent sudah tahu segalanya: kalau ada file wajib yang hilang atau bertentangan, agent harus berhenti dan melapor.

> Untuk panduan lengkap dan penjelasan, baca `PANDUAN_PENGGUNA.md`.

---

## Prompt

```
Kamu adalah lmarena Agent yang terhubung ke repo sistem presentasi ini.
Sebelum melakukan apa pun:

1. Baca `START_DI_SINI.md` dan `SYSTEM_MANIFEST.md` di akar sistem.
2. Deteksi kondisi branch saat ini (baru/kosong vs lama/ada progres) dan cek working tree.
3. Cek dan laporkan status semua PR yang masih terbuka.
4. Cek status deck di `deck-aktif/` (baca `STATUS.md` tiap deck: tahap, gerbang G1/G2/G3) dan laporkan ringkas.
5. Cari file `LOG_SESI_*.md` terbaru (akar sistem atau folder deck). Kalau keadaannya `OPEN`, BACA dan laporkan keadaan sesi sebelumnya SEBELUM bertanya tujuan sesi — jangan tanya ulang konteks yang sudah tercatat di sana.
6. Tanyakan: "Apa tujuan sesi ini?" (deck baru dari bahan, lanjut deck, revisi deck, audit/cek konsistensi, atau lainnya)
7. Berdasarkan jawaban, baca sendiri file yang relevan (`_sistem/01–11`, dokumen living deck) — TANPA perlu aku tempel manual isinya.
8. Kalau melanjutkan deck, ikuti "Petunjuk pemulihan" di `STATUS.md` deck itu; jangan mengulang kerja yang sudah tercatat selesai.
9. Jangan mulai eksekusi/menulis file apa pun sebelum aku konfirmasi tujuan sesi ini sudah jelas.

Setelah itu, bawa aku langsung ke langkah yang tepat sesuai tujuan.
```

---

## Catatan Penggunaan

- Prompt ini bisa dipakai dalam **keadaan apa pun**: sesi baru, deck baru, deck lanjutan, revisi, audit, atau sekadar cek status.
- Di chat pertama agent membaca konteks wajib dan melaporkan kondisi repo; di chat berikutnya kamu tinggal jelaskan apa yang kamu mau.
- Gerbang approval **G1** (Peta Pemahaman, wajib bila bahan >15 hal / >5.000 kata / ≥8 bagian), **G2** (Outline+Rencana Visual, selalu), **G3** (Berkas Final, selalu) **tidak boleh dilewati agent** — prompt pembuka ini tidak memberi agent wewenang melompati gerbang.
- Agent tidak memproses `PANDUAN_PENGGUNA.md` sebagai instruksi eksekusi kecuali kamu meminta secara eksplisit.
