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
4. Rujukan ber-backtick ke SATU BERKAS `_meta/...` atau `tools/...` di dokumen aktif adalah janji operasional bahwa salinan berlabel dari sumber itu ikut berada di dalam folder sistem.
5. Provenance/histori boleh disebut tanpa backtick. Riwayat lengkap tetap di master; folder sistem tidak wajib membawa cerita "kenapa" selama aturan kerja yang dipakai sudah ada di dalam folder.
6. **Cakupan penegakan = dokumen aktif, satu definisi.** Yang dinilai alat hanyalah dokumen aktif menurut definisi bersama `dokumen_aktif()` di tools/checkpoint_core.py — definisi yang SAMA dengan yang dipakai validator master. Dokumen bukti dan dokumen mentah (`ACCEPTANCE_TEST_LOG.md`, `LOG_SESI*`, `DISKUSI_MENTAH*`, rencana kerangka, state kerja per unit, dan apa pun yang sudah dikecualikan definisi itu) TIDAK ditegakkan: menulis bukti tidak boleh mengubah hasil gerbang. Rujukannya tidak dibuang — alat mendaftarkannya di bagian "rujukan historis (tidak ditegakkan)" saat `--report`, supaya informasinya tetap terbaca orang berikutnya.
7. **Penyebutan area bukan janji berkas.** Rujukan ber-backtick yang berakhir dengan garis miring (mis. `_meta/` atau `tools/`) adalah penyebutan area, bukan janji bahwa satu berkas ada di dalam folder — bukan kegagalan. Alat mendaftarkannya di bagian "sebutan area" saat `--report`.
8. **Area yang tidak boleh keluar dari master tidak pernah ditawari salinan.** Rujukan ke `_meta/_internal/**` dan ke area lain yang memang ditolak verifikasi template bersih (AT-10) tidak boleh diselesaikan dengan salinan berlabel, karena menyalinnya adalah pelanggaran itu sendiri. Satu definisinya: `master_only_reason()` di tools/checkpoint_core.py, dipakai bersama oleh tools/build_template.py dan alat gerbang ini. Bentuk yang benar untuk kasus ini: **tulis sebagai provenance tanpa backtick** — berlaku juga untuk dokumen operasional. Kalau ada yang sudah terlanjur menyalin berkas dari area itu ke folder sistem, itu temuan (`MASTER-ONLY-COPY`): perbaiki dengan menghapus salinannya dan menulis provenance tanpa backtick.

Tiga pembedaan terakhir (butir 6–8) adalah CAKUPAN, bukan pelonggaran. Perilaku yang ditegakkan untuk dokumen aktif tidak berubah sedikit pun: rujukan ke diri sendiri berprefiks folder, rujukan berkas operasional tanpa salinan berlabel, salinan basi, turunan tanpa label, dan label tanpa baris kedua `Perbedaan:` semuanya tetap gagal.

---

## 1. Definisi mandiri

Sebuah folder sistem disebut mandiri hanya bila seluruh syarat ini benar:

| # | Syarat | Cara membuktikan |
|---|---|---|
| F1 | Validator sistem hidup hanya dari folder sistem | alat master menyalin hanya folder itu ke direktori sementara, lalu menjalankan `python3 _sistem/validate_system.py` dari salinan |
| F2 | Tidak ada rujukan ke diri sendiri dengan prefiks folder | tidak ada backtick berisi `sistem-<nama>/...` di dalam folder sistem itu |
| F3 | Semua rujukan operasional ke master ikut sebagai salinan berlabel | setiap backtick yang menunjuk SATU BERKAS `_meta/...` atau `tools/...` **di dokumen aktif** punya berkas salinan di dalam folder dengan label sumber yang sesuai |
| F4 | Salinan tidak basi | badan salinan sama byte dengan sumber di master, kecuali salinan menyatakan sendiri perbedaannya tepat di bawah label |
| F5 | Tidak ada berkas turunan tanpa label | berkas yang berada di area salinan/turunan atau dipakai untuk memenuhi rujukan master harus memuat label wajib pada tiga baris pertama |
| F6 | Cakupan penilaian = dokumen aktif (satu definisi) | alat mengambil cakupan dari `dokumen_aktif()` di tools/checkpoint_core.py, definisi yang sama dengan validator master; alat ini tidak membawa daftar glob sendiri. Rujukan dari dokumen di luar definisi itu terdaftar di bagian "rujukan historis (tidak ditegakkan)" pada `--report` dan bukan temuan |
| F7 | Penyebutan area bukan kegagalan | backtick berbentuk direktori (berakhir garis miring) terdaftar di bagian "sebutan area" pada `--report` dan bukan temuan |
| F8 | Area yang tidak boleh keluar dari master tidak pernah disalin | tidak ada temuan yang menawarkan salinan berlabel untuk `_meta/_internal/**` atau area lain yang ditolak verifikasi template (satu definisi: `master_only_reason()`); pesannya meminta provenance tanpa backtick, dan salinan yang terlanjur dibuat dari area itu adalah temuan `MASTER-ONLY-COPY` |

Alat yang menegakkan syarat di atas adalah `tools/check_selfcontained.py`. Alat itu alat master: bila dijalankan di folder mandiri yang tidak punya `_meta/`, ia mencetak pesan bahwa ia alat master dan keluar 2. Tidak ada mode tersembunyi.

Kode temuan yang dicetak alat, dan solusi yang benar untuk masing-masing:

| Kode | Arti | Solusi yang benar |
|---|---|---|
| `VALIDATOR` | validator sistem gagal di salinan folder | perbaiki isi folder sistem sampai validatornya PASS |
| `SELF-PREFIX` | rujukan ke folder sendiri memakai prefiks folder | tulis relatif terhadap folder sistem |
| `MISSING-LABELED-COPY` | dokumen aktif merujuk satu berkas `_meta/...`/`tools/...` yang tidak ikut | vendor sebagai salinan berlabel (format: bagian 3), atau tulis sebagai provenance tanpa backtick bila memang bukan dependensi |
| `MASTER-ONLY-REF` | dokumen aktif merujuk area yang tidak boleh keluar dari master | tulis sebagai provenance tanpa backtick — JANGAN menyalin |
| `MASTER-ONLY-COPY` | ada salinan berlabel yang bersumber dari area yang tidak boleh keluar dari master | hapus salinannya, tulis sebagai provenance tanpa backtick |
| `STALE-COPY` | salinan basi terhadap sumber di master | sinkronkan ulang badannya, atau nyatakan perbedaannya di baris kedua label dan daftarkan kasusnya di body PR |
| `LABEL-SOURCE` | sumber label tidak ada/absolut/naik direktori | perbaiki jalur sumber label |
| `LABEL-FORMAT` | tiga baris label tidak lengkap/tidak sesuai format (termasuk baris kedua `Perbedaan:`) | perbaiki labelnya |
| `DERIVED-NO-LABEL` | berkas di area salinan/turunan tanpa tiga baris label | tambahkan label wajib |

---

## 2. Kelas rujukan dan cakupan penegakan

### A. Dipakai untuk bekerja

Jika sebuah aturan, template, validator, pedoman, atau skrip benar-benar dibutuhkan saat sistem dipakai, ia harus berada di dalam folder sistem. Bila sumbernya berasal dari master, vendor sebagai salinan berlabel. Rujukan ber-backtick ke SATU BERKAS `_meta/...` atau `tools/...` di dokumen aktif selalu masuk kelas ini; jangan menuliskannya kalau berkasnya tidak ikut.

### B. Sejarah / provenance

Jika sebuah nama hanya menjelaskan asal-usul keputusan, bukti historis, atau konteks lama, sebut tanpa backtick dan jangan jadikan dependensi. Contoh bentuk yang benar: "prinsip ini berasal dari 03_KONTRAK_WARISAN.md di master". Bentuk itu memberi jejak manusia tanpa membuat janji bahwa berkas master tersedia di folder sistem.

Kelas ini **wajib** — bukan pilihan — untuk area yang tidak boleh keluar dari master (audit/handoff internal dan area lain yang ditolak verifikasi template bersih). Untuk area itu, salinan berlabel bukan solusi yang boleh ditawarkan alat maupun penulis, karena menyalinnya adalah pelanggaran yang sama dengan yang dilarang verifikasi template.

### C. Penyebutan area

Backtick yang berakhir dengan garis miring (`_meta/`, `tools/`) menyebut AREA, bukan satu berkas. Ia tidak menjanjikan bahwa berkas tertentu ikut, jadi ia bukan kegagalan; alat mendaftarkannya di bagian "sebutan area" pada `--report`. Yang tetap salah adalah menyebut area yang tidak boleh keluar dari master sebagai dependensi operasional — untuk itu pakai bentuk B.

### D. Cakupan: dokumen aktif saja

Penegakan A–C hanya berlaku pada **dokumen aktif**, yaitu dokumen yang dikembalikan `dokumen_aktif()` di tools/checkpoint_core.py — satu definisi yang sama dengan validator master, termasuk pengecualiannya (area internal, state kerja per unit, rencana kerangka, log bukti acceptance, diskusi mentah). Dokumen bukti dan dokumen mentah tidak ditegakkan supaya menulis bukti tidak mengubah hasil gerbang; rujukannya tetap dicatat alat di bagian "rujukan historis (tidak ditegakkan)" pada `--report`. Alat gerbang ini tidak boleh membawa daftar glob atau daftar pengecualian sendiri — kalau cakupan berubah, ubah definisi bersama itu, bukan alatnya.

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

**Acuan bentuk yang benar (jangan mengarang format baru):** sistem benih yang dibangkitkan tools/build_template.py sudah membawa satu contoh salinan berlabel nyata — berkas `_meta/TEMPLATE_LOG_SESI.md` dari master dibawa ke dalam folder sistem-benih di direktori _salinan-meta dengan nama berkas yang sama. Tiga baris labelnya ditulis pembangun dari sumber yang benar-benar ada (jalur sumber, sha isi sumber, tanggal, versi meta yang berlaku), baris keduanya `> Perbedaan: tidak ada`, dan badannya sama byte dengan sumber. Kalau sebuah dokumen master memang dibutuhkan sistem, salin dengan bentuk itu; kalau tidak dibutuhkan, jangan buat salinannya.

---

## 4. Cara pakai gerbang mandiri

Dari root repo master:

    python3 tools/check_selfcontained.py --sistem sistem-nama --report
    python3 tools/check_selfcontained.py --semua --report

Arti hasil:

- Exit 0: folder sistem adalah deliverable mandiri menurut protokol ini.
- Exit 1: folder sistem belum mandiri; keluaran alat adalah daftar kerja yang harus diperbaiki di dalam folder sistem, bukan di hasil salinan sementara.
- Exit 2: alat tidak bisa berjalan karena dipanggil di tempat yang salah atau inputnya tidak sah.

Keluaran `--report` memuat empat daftar per sistem, dan hanya daftar kedua yang membuat merah:

1. **salinan berlabel ditemukan** — salinan yang ada di dalam folder, lengkap dengan sumber, sha, dan perbedaan yang dinyatakan.
2. **temuan** — pelanggaran yang membuat exit 1 (kode dan solusinya: tabel di bagian 1).
3. **rujukan historis (tidak ditegakkan)** — rujukan keluar folder dari berkas yang berada di luar definisi dokumen aktif (dokumen bukti, dokumen mentah, state kerja per unit, skrip). Bukan kegagalan; dicatat supaya jejaknya tetap terbaca dan tidak ada yang mengira rujukan itu hilang dari penilaian karena kelalaian.
4. **sebutan area** — backtick berbentuk direktori (berakhir garis miring). Bukan kegagalan; bila areanya termasuk yang tidak boleh keluar dari master, barisnya sekaligus menyebut bahwa area itu harus disebut sebagai provenance tanpa backtick.

Untuk PR yang menyelesaikan kemandirian sebuah sistem, bukti yang diterima adalah keluaran utuh `--report` pada sistem itu. Untuk PR meta yang hanya mengubah alat/protokol, keluaran `--semua --report` boleh merah pada sistem domain yang memang belum menjadi scope PR tersebut; merah itu daftar kerja PR berikutnya, bukan alasan melonggarkan alat.

---

## 5. Hubungan dengan validator lain

- `tools/validate_repo.py` tetap validator master untuk struktur repo, kontrak warisan, indeks, parser checkpoint, dan larangan angka korpus di sel Bukti.
- Validator sistem di `_sistem/validate_system.py` tetap milik tiap folder sistem dan harus self-contained.
- `tools/check_selfcontained.py` menyatukan keduanya pada batas deliverable: ia menyalin hanya folder sistem, menjalankan validator sistem di salinan, lalu memeriksa rujukan dan salinan berlabel dari sisi master.
- Dua penilaian dipakai bersama lewat tools/checkpoint_core.py, bukan disalin per alat: **cakupan dokumen aktif** (`dokumen_aktif()`, sama dengan validator master) dan **area yang tidak boleh keluar dari master** (`master_only_reason()`, sama dengan verifikasi template bersih AT-10 di tools/build_template.py). Pelajaran yang dijaga di sini: norma dan alat tidak boleh berbeda (temuan T-8 review PR #26), dan dua daftar salinan akan meleset satu sama lain (akar masalah v1.6.0).

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
| 2026-09-09 | v2.1: tiga pembedaan CAKUPAN ditulis apa adanya (butir 6–8, syarat F6–F8, kelas rujukan C–D, tabel kode temuan, empat daftar `--report`, acuan bentuk salinan dari sistem benih) | Dua tabrakan aturan: (1) alat menegakkan rujukan di dokumen bukti/mentah padahal definisi dokumen aktif bersama mengecualikannya, dan memperlakukan penyebutan area sebagai janji berkas; (2) alat menawarkan salinan berlabel untuk area yang tidak boleh keluar dari master, padahal menyalinnya adalah pelanggaran yang sama dengan yang ditolak verifikasi template. Norma dan alat tidak boleh berbeda (temuan T-8 review PR #26) | Putusan pemilik PR A2, 9 Sep 2026 |
