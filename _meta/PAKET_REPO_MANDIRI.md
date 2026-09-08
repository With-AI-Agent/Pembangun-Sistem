# Paket Repo Mandiri

### Protokol folder mandiri: satu folder sistem adalah deliverable. Yang disalin = yang dipakai; tidak ada ZIP, tidak ada dist, tidak ada tahap lem manual oleh pemilik.

> Gerbang mekanis: `python3 tools/check_selfcontained.py --sistem <folder> --report` atau `python3 tools/check_selfcontained.py --semua --report`. Exit 0 dari alat itu adalah definisi baru bahwa folder sistem sudah mandiri.

---

## Kenapa protokol ini berubah

Putusan pemilik 8 September 2026 mengganti model lama "paket repo mandiri" menjadi model yang lebih murah dipertahankan: **folder sistem itu sendiri adalah hasil akhir yang disalin dan dipakai**. Pemilik tidak lagi melakukan kerja penyatuan/glue: tidak memilih berkas mana yang ikut, tidak membongkar ZIP, tidak membaca daftar subset meta, dan tidak menebak rujukan mana yang aman diabaikan.

Konsekuensi normatifnya sederhana:

1. Folder `sistem-<nama>/` harus memuat semua yang ia perlukan saat dipakai.
2. Semua rujukan di dalam folder sistem relatif terhadap folder itu sendiri.
3. Rujukan berformat `sistem-<nama>/...` dari folder itu ke dirinya sendiri adalah salah; tulis `README.md`, `_sistem/...`, `panduan/...`, dan seterusnya.
4. Rujukan ber-backtick ke `_meta/...` atau `tools/...` adalah janji operasional bahwa salinan berlabel dari sumber itu ikut berada di dalam folder sistem.
5. Provenance/histori boleh disebut tanpa backtick. Riwayat lengkap tetap di master; folder sistem tidak wajib membawa cerita "kenapa" selama aturan kerja yang dipakai sudah ada di dalam folder.

---

## 1. Definisi mandiri

Sebuah folder sistem disebut mandiri hanya bila seluruh syarat ini benar:

| # | Syarat | Cara membuktikan |
|---|---|---|
| F1 | Validator sistem hidup hanya dari folder sistem | alat master menyalin hanya folder itu ke direktori sementara, lalu menjalankan `python3 _sistem/validate_system.py` dari salinan |
| F2 | Tidak ada rujukan ke diri sendiri dengan prefiks folder | tidak ada backtick berisi `sistem-<nama>/...` di dalam folder sistem itu |
| F3 | Semua rujukan operasional ke master ikut sebagai salinan berlabel | setiap backtick yang menunjuk `_meta/...` atau `tools/...` punya berkas salinan di dalam folder dengan label sumber yang sesuai |
| F4 | Salinan tidak basi | badan salinan sama byte dengan sumber di master, kecuali salinan menyatakan sendiri perbedaannya tepat di bawah label |
| F5 | Tidak ada berkas turunan tanpa label | berkas yang berada di area salinan/turunan atau dipakai untuk memenuhi rujukan master harus memuat label wajib pada tiga baris pertama |

Alat yang menegakkan syarat di atas adalah `tools/check_selfcontained.py`. Alat itu alat master: bila dijalankan di folder mandiri yang tidak punya `_meta/`, ia mencetak pesan bahwa ia alat master dan keluar 2. Tidak ada mode tersembunyi.

---

## 2. Dua kelas rujukan

### A. Dipakai untuk bekerja

Jika sebuah aturan, template, validator, pedoman, atau skrip benar-benar dibutuhkan saat sistem dipakai, ia harus berada di dalam folder sistem. Bila sumbernya berasal dari master, vendor sebagai salinan berlabel. Rujukan ber-backtick ke `_meta/...` atau `tools/...` selalu masuk kelas ini; jangan menuliskannya kalau berkasnya tidak ikut.

### B. Sejarah / provenance

Jika sebuah nama hanya menjelaskan asal-usul keputusan, bukti historis, atau konteks lama, sebut tanpa backtick dan jangan jadikan dependensi. Contoh bentuk yang benar: "prinsip ini berasal dari 03_KONTRAK_WARISAN.md di master". Bentuk itu memberi jejak manusia tanpa membuat janji bahwa berkas master tersedia di folder sistem.

---

## 3. Format salinan berlabel

Setiap berkas salinan turunan wajib memiliki label pada tiga baris pertama, dan ketiga baris itu wajib dimulai dengan `> `.

Baris pertama wajib persis mengikuti pola:

    > Salinan turunan. Sumber: <jalur-di-master> sha <40 karakter hash isi sumber> tanggal <YYYY-MM-DD> versi-meta <x.y.z>

Baris kedua wajib menyebut perbedaan:

    > Perbedaan: tidak ada

atau, bila salinan memang tidak bisa identik byte karena disunat/diadaptasi:

    > Perbedaan: <jelaskan ringkas apa yang berbeda dan kenapa>

Baris ketiga bebas selama tetap diawali `> `; gunakan untuk tujuan pemakaian salinan.

Badan berkas setelah tiga baris label harus sama byte dengan sumber di master. Jika badan tidak sama byte, salinan harus menyatakan perbedaannya di baris label, dan PR yang menambahkan salinan itu harus mendaftarkan kasus tersebut di body PR. Perbedaan tanpa label adalah error; label tanpa sumber yang ada di master juga error.

---

## 4. Cara pakai gerbang mandiri

Dari root repo master:

    python3 tools/check_selfcontained.py --sistem sistem-nama --report
    python3 tools/check_selfcontained.py --semua --report

Arti hasil:

- Exit 0: folder sistem adalah deliverable mandiri menurut protokol ini.
- Exit 1: folder sistem belum mandiri; keluaran alat adalah daftar kerja yang harus diperbaiki di dalam folder sistem, bukan di hasil salinan sementara.
- Exit 2: alat tidak bisa berjalan karena dipanggil di tempat yang salah atau inputnya tidak sah.

Untuk PR yang menyelesaikan kemandirian sebuah sistem, bukti yang diterima adalah keluaran utuh `--report` pada sistem itu. Untuk PR meta yang hanya mengubah alat/protokol, keluaran `--semua --report` boleh merah pada sistem domain yang memang belum menjadi scope PR tersebut; merah itu daftar kerja PR berikutnya, bukan alasan melonggarkan alat.

---

## 5. Hubungan dengan validator lain

- `tools/validate_repo.py` tetap validator master untuk struktur repo, kontrak warisan, indeks, parser checkpoint, dan larangan angka korpus di sel Bukti.
- Validator sistem di `_sistem/validate_system.py` tetap milik tiap folder sistem dan harus self-contained.
- `tools/check_selfcontained.py` menyatukan keduanya pada batas deliverable: ia menyalin hanya folder sistem, menjalankan validator sistem di salinan, lalu memeriksa rujukan dan salinan berlabel dari sisi master.

---

## 6. Yang dipensiunkan

Pensiun berlaku mulai 8 September 2026. Commit terakhir sebelum pensiun: 453210164a4c4c7135cf61d2d48bf89841665950.

Alasan pemilik: mekanisme lama memindahkan kerja ke pemilik; folder sebagai deliverable lebih murah dipertahankan.

Kemampuan yang dicabut:

| Mekanisme lama | Status | Alasan pensiun |
|---|---|---|
| tools/pack_repo.py sebagai pembangkit paket | pensiun; berkas dihapus dengan jejak | pemilik tidak lagi menerima deliverable berupa paket yang perlu dibongkar atau disatukan ulang |
| ZIP dan folder dist sebagai keluaran sistem | pensiun | deliverable adalah folder sistem yang langsung disalin |
| Repo profile / PAKET_REPO.json | pensiun | daftar kewajiban tidak lagi dipersempit oleh profil hasil bangkitan; folder sistem membawa sendiri kewajibannya |
| absent_refs_allowed / daftar putih rujukan-absen | pensiun | rujukan master yang dipakai harus punya salinan berlabel; rujukan sejarah disebut tanpa backtick |
| Penulisan ulang indeks di hasil paket | pensiun | tidak ada lagi hasil paket dengan indeks yang disunat |
| Subset `_meta/` berbasis rujukan | pensiun | yang dibutuhkan sistem divendor ke folder sistem sebagai salinan berlabel, bukan dihitung saat pengemasan |
| Berita acara PAKET_REPO.md hasil bangkitan | pensiun | bukti selesai kini keluaran `tools/check_selfcontained.py --report` |

Jejak historis tetap boleh disebut di master tanpa backtick. Jangan menghidupkan kembali mekanisme di atas sebagai "pengaman tambahan" tanpa keputusan pemilik baru.

---

## 7. Hubungan dengan protokol lain

- **Definition of Done.** Syarat "siap dipakai produksi" menunjuk exit 0 `tools/check_selfcontained.py`; detailnya ada di dokumen ini.
- **Acceptance test.** AT-15 lama ditandai pensiun dan digantikan AT-17.
- **Review independen.** Perubahan pada dokumen ini atau alat gerbang mandiri adalah perubahan struktural meta dan wajib review independen L1.
- **Indeks sistem.** Sistem yang belum lolos alat ini harus ditulis jujur sebagai belum mandiri, dengan perintah yang harus dijalankan.

## Log keputusan

| Tanggal | Perubahan | Alasan | Approval |
|---|---|---|---|
| 2026-09-07 | Dokumen dibuat (v1) untuk mekanisme paket repo mandiri lama | Putusan saat itu: satu perintah menghasilkan folder repo siap upload | Putusan pemilik 7 Sep 2026; kini menjadi riwayat pensiun |
| 2026-09-08 | v1.1 dan v1.2 menambah definisi dokumen aktif serta protokol pemindahan paket lama | Mengatasi bukti basi dan hambatan pemindahan pada mekanisme lama | Putusan pemilik 8 Sep 2026; kini menjadi riwayat pensiun |
| 2026-09-08 | v2.0: protokol ditulis ulang menjadi "folder sistem = deliverable"; mekanisme paket lama dipensiunkan; gerbang baru adalah `tools/check_selfcontained.py` | Keputusan pemilik final: yang disalin = yang dipakai, tanpa kerja penyatuan/glue oleh pemilik | Putusan pemilik PR A, 8 Sep 2026 |
