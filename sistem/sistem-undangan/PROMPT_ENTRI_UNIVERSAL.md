# Prompt Pembuka Universal — Sistem Undangan

File ini berisi **satu blok prompt siap pakai** untuk memulai sesi apa pun di sistem ini. Cukup salin isi
bagian "Prompt" di bawah ke chat pertama — prompt ini menyuruh agent membangun sendiri konteks yang
diperlukan (baca dokumen sistem, cek branch, cek PR terbuka, cek status, cek bahan milikmu, cari log sesi
yang belum ditutup, jalankan validator), lalu menanyakan apa tujuanmu. Ini **arahan kerja**, bukan jaminan
agent sudah tahu segalanya: kalau ada berkas wajib yang hilang atau saling bertentangan, agent harus
berhenti dan melapor.

> Untuk panduan lengkap dan penjelasan tiap bagiannya, baca `PANDUAN_PENGGUNA.md`.

---

## Prompt

```
Kamu adalah lmarena Agent yang terhubung ke repo sistem undangan ini.
Sebelum melakukan apa pun:

1. Baca `SYSTEM_MANIFEST.md`, `STATUS.md`, dan `00_RENCANA_KERANGKA.md` di akar sistem ini.
2. Deteksi kondisi branch saat ini (baru/kosong vs lama/sudah ada progres) dan cek working tree; JANGAN berasumsi sedang berada di branch utama.
3. Cek dan laporkan SEMUA PR yang masih terbuka di repo ini — dari sistem mana pun, bukan hanya sistem undangan.
4. Laporkan keadaan sistem ini dari `STATUS.md`: tahap (kerangka/berkembang/siap-pakai), versi, tahap terakhir yang selesai, tahap berikutnya, dan apakah ada pekerjaan yang belum tersimpan.
5. Baca `Input-Pengguna/README.md` dan laporkan apakah ada bahan milik pemilik yang sudah masuk tetapi belum diproses.
6. Cari file `LOG_SESI_*.md` terbaru (akar sistem ini, folder unit kerja, atau folder log sesi repo). Kalau keadaannya `OPEN`, BACA dan laporkan keadaan sesi sebelumnya SEBELUM bertanya tujuan sesi — jangan tanya ulang konteks yang sudah tercatat di sana.
7. Jalankan `python3 _sistem/validate_system.py` dan laporkan hasilnya APA ADANYA, termasuk peringatan atau kegagalan yang belum dibereskan. Jangan menghaluskannya.
8. Kalau tahap sistem masih `kerangka`, katakan terus terang bahwa sistem ini BELUM bisa memproduksi undangan, dan sebutkan apa yang sudah ada dan apa yang belum. Jangan berpura-pura siap.
9. Tanyakan: "Apa tujuan sesi ini?" (mulai undangan baru untuk client, lanjut undangan yang sudah ada, revisi desain atau aset, isi identitas pemilik L1, tambah profil jenis acara L2, siapkan terbit/cetak/serah terima, audit atau cek konsistensi, atau lainnya)
10. Berdasarkan jawaban, baca sendiri dokumen yang relevan (`01_IDENTITAS_PEMILIK.md` sampai `11_AMPLOP_DIGITAL.md`) — TANPA perlu aku tempel manual isinya.
11. Kalau melanjutkan unit kerja yang sudah ada, ikuti petunjuk pemulihan di `STATUS.md` unit itu; jangan mengulang kerja yang sudah tercatat selesai.
12. Jangan lewati gerbang G0 sampai G5. Gerbang berisiko BESAR (G0, G2, G5, dan perubahan apa pun pada data L1) wajib keputusan pemilik langsung dan TIDAK BOLEH diwakilkan ke agent.
13. Kalau ada data acara yang kurang, NYATAKAN bahwa data itu kurang. Jangan mengisi diam-diam dengan nilai karangan.
14. Jangan mulai eksekusi atau menulis file apa pun sebelum aku konfirmasi tujuan sesi ini sudah jelas.

Setelah itu, bawa aku langsung ke langkah yang tepat sesuai tujuan.
```

---

## Catatan Penggunaan

- Prompt ini bisa dipakai dalam **keadaan apa pun**: sesi baru, undangan baru, undangan lanjutan, revisi,
  audit, atau sekadar cek status. Tidak ada keadaan yang butuh prompt pembuka berbeda.
- Di chat pertama agent membaca konteks wajib dan melaporkan kondisi repo; di chat berikutnya kamu tinggal
  jelaskan apa yang kamu mau.
- Sistem ini punya **6 gerbang penguncian (G0 sampai G5)**. Yang berisiko **BESAR** — G0 (brief + jenis
  acara), G2 (desain & format dikunci), G5 (terbit/serah terima), dan **perubahan apa pun pada data L1**
  (identitas & preferensi pemilik) — **tidak boleh dilewati atau diwakilkan agent**. Prompt pembuka ini
  sengaja **tidak** memberi agent wewenang melompati gerbang.
- Agent **tidak** memproses `PANDUAN_PENGGUNA.md` sebagai instruksi eksekusi kecuali kamu memintanya
  secara eksplisit.
- **Isi blok prompt di file ini dan di §"Prompt Pembuka Universal" `PANDUAN_PENGGUNA.md` wajib IDENTIK**
  (dua file, satu sumber). Kalau salah satunya diubah, ubah keduanya lalu bandingkan — selisih diam-diam
  antar dua file ini pernah terjadi di repo induk dan jadi temuan audit.
