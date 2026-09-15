# Prompt Pembuka Universal — Sistem Klinik

File ini berisi satu blok prompt siap pakai untuk memulai sesi apa pun di sistem ini. Cukup salin isi bagian "Prompt" di bawah ke chat pertama. Ini arahan kerja, bukan jaminan bahwa agent sudah tahu segalanya: kalau ada file wajib yang hilang atau bertentangan, agent harus berhenti dan melapor.

> Untuk panduan lengkap dan penjelasan, baca `PANDUAN_PENGGUNA.md` di folder ini.

---

## Prompt

```
Kamu adalah agent yang terhubung ke repo meta ini, dan sesi ini bekerja pada Sistem Klinik (folder sistem-klinik/).
Sebelum melakukan apa pun:

1. Jalankan Entry Point tingkat repo yang WAJIB (aturannya tertulis di file 00_CARA_KERJA_META.md di folder _meta — baca itu): laporan awal mengikuti SESSION_REPORT_TEMPLATE, cek PR menggantung lewat gh pr list --state all, cek INDEKS_SISTEM, dan cari LOG_SESI terbaru di _log-sesi/ — kalau ada yang OPEN, BACA dulu dan laporkan; jangan tanya ulang konteks yang sudah tercatat
2. Baca `START_DI_SINI.md` (entry point sistem — urutan baca per jenis sesi: pembangunan / run suntik / run rawat inap / audit kit / review PR) + `STATUS.md` dan `SYSTEM_MANIFEST.md` sebagai peta sistem ini; `00_RENCANA_KERANGKA.md` dibaca bila kerja menyentuh rencana kerangka
3. Tanyakan: "Apa tujuan sesi ini?" — kandidat: menjalankan run klinik (suntik = target di repo eksternal, kit disalin ke sana; rawat inap = target adalah folder sistem di repo ini — alur standar meta + aturan klinik, K-11); melanjutkan pembangunan dokumen yang dijadwalkan rencana kerangka; memperbaiki/menambah katalog cacat hasil temuan run; atau lain-lain
4. Baca sendiri konteks wajib sesuai tujuan — jangan baca seluruh isi repo. JANGAN menyentuh isi sistem lain (folder _produksi-aktif/, folder sistem lain, repo target manapun) kecuali tujuan sesi ini eksplisit memintanya
5. Jangan mulai eksekusi/menulis file apa pun sebelum aku konfirmasi tujuan sesi ini jelas

Sepanjang sesi: pelihara LOG_SESI di _log-sesi/ (aturannya ada di `10_LOG_SESI.md`), commit+push tiap pertukaran yang menghasilkan informasi baru, tanya di tiap gerbang approval, akhiri dengan PR tanpa auto-merge.
```

---

## Prompt Penutup

```
Tutup sesi ini:
1. Perbarui `STATUS.md` di sistem-klinik/ — field deterministik wajib benar: Pekerjaan belum tersimpan = "Tidak ada" hanya bila working tree memang bersih dan seluruh commit ter-push
2. Perbarui header LOG_SESI sesi ini: CLOSED (atau OPEN + "dilanjutkan di mana" bila disengaja)
3. Perbarui tanggal "terakhir disentuh" dan status sistem ini di _meta/INDEKS_SISTEM.md — pencatatan manual, TIDAK mengandalkan git history
4. Kalau kerja berlanjut lintas sesi: tinggalkan handoff di log sesi + STATUS supaya sesi baru melanjutkan tanpa ditanya ulang dari nol
5. Commit + push semua yang bermakna; buka PR dengan deskripsi lengkap (apa yang dikerjakan, gerbang yang diberikan/ditunda, nomor PR dicatat di commit terakhir). SEBELUM merge/close apa pun: pastikan semua sudah ter-push — setelah itu sesi ini TIDAK BISA push lagi (fakta platform); kerja lanjutan dari sesi baru yang dibuka dari main
6. Jalankan pembangkit prompt review repo induk (tools/review_prompt.py --pr <nomor>) dan tempel keluarannya sebagai SATU BLOK BERPAGAR di badan pesan chat TERAKHIR sesi — tanpa blok itu, penutupan dianggap belum dikerjakan dan PR belum boleh dinilai
7. Jangan pernah auto-merge — merge selalu keputusanku
```
