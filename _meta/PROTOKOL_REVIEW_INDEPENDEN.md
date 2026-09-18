# Protokol Review Independen (Sesi Lain)

## Tujuan
Verifikasi akhir atas pekerjaan yang berdampak permanen dilakukan oleh SESI AI LAIN yang tidak mengerjakan dan tidak menilai dirinya sendiri. Prinsip: yang mengerjakan tidak memutus; yang memutus tidak punya kepentingan. Ini lapisan eksternal dari `QUALITY_ASSURANCE_AND_EVOLUTION.md` — bukan pengganti validator/FI, melainkan penutup yang memutuskan apakah bukti boleh masuk main.

## Prinsip inti
1. Pemutus eksternal: verdict atas acceptance run, klaim DONE, atau perubahan terkunci dibuat oleh sesi yang berbeda dari penulis/subjek/pencatat (pola: pencatat ≠ subjek).
2. Reviewer hanya memverifikasi dari artefak (git tree, commit, log, API), bukan dari narasi pihak yang direview. Klaim pihak reviewed = objek pemeriksaan, bukan bukti.
3. Aturan merge: reviewer TIDAK meng-merge/menyetujui atas namanya sendiri, KECALI pemilik pekerjaan mengizinkan eksplisit di prompt. Tidak ada auto-merge, kapan pun.
4. Independensi: reviewer tidak menulis di branch subjek/penulis; read-only terhadap branch orang lain.
5. Batas jendela (6d generalisasi): selama jendela run/uji atau proses lain yang sedang berjalan, artefak yang dipublikasikan reviewer (komentar PR, log, branch) tidak boleh memuat rumusan jawaban/kriteria yang belum tertutup uji; gunakan pointer SHA+baris.
6. Proporsional: kedalaman review mengikuti level trigger di bawah; review bukan ritual untuk pekerjaan remeh.
7. Putaran terbatas: maksimal 2 putaran (review → koreksi → review ulang). Putaran ke-2 gagal = eskalasi ke pemilik untuk keputusan final (termasuk opsi membatalkan).
8. Append-only: hasil review dicatat apa adanya, termasuk RED FLAG dan verdict yang merevisi verdict sebelumnya; jangan menghapus riwayat, jangan menghaluskan.

## Level trigger
- L1 WAJIB review independen: menutup pengecualian/gate acceptance (mis. F-closed), menaikkan versi aturan (00/05/06 atau setara), perubahan struktural `_meta/`, operasi riwayat (reset/revert/fungsi-forcing), merge yang mengubah klaim DONE/manifest.
- L2 DISARANKAN review ringkas (checklist, tanpa formalitas prompt panjang): PR dokumentasi besar, perubahan template yang diwarisi sistem lain, sanitasi/redaksi.
- L3 TIDAK perlu: commit rutin produksi, typo, housekeeping reversibel, PR hygiene kecil tanpa perubahan aturan. Override dari L1 ke L3 wajib dicatat pemiliknya di log dengan alasan.

## Anatomi prompt reviewer (wajib berisi)
1. Identitas: "kamu reviewer independen PR #N; kamu memutuskan, bukan melanjutkan".
2. Objek ter-pin: nomor PR + **TIGA sha** — base sha (ujung base SEKARANG), **merge-base sha** (titik
   branch dibuat), dan head sha yang wajib disebut sebagai **OBJEK YANG HENDAK DIPUTUSKAN** — beserta
   **DUA diff berlabel**: **(A)** merge-base ke head = perubahan yang diperkenalkan PR, dan **(B)** base sha
   ke head = selisih langsung yang **ikut memuat perubahan yang masuk ke base SESUDAH branch dibuat**.
   **Sebab aturan ini diperketat (temuan R3 review independen PR #74, nyata terjadi):** butir ini dulu hanya
   berbunyi "SHA basis + SHA head", lalu prompt menyajikan diff **(B)** sebagai perintah wajib sementara
   daftar berkasnya diambil dari diff **(A)** — **dua semantik berbeda disajikan sebagai satu objek**.
   Selisihnya **terukur 4 berkas** (53 vs 49 saat reviewer mengukurnya; 59 vs 55 sesudahnya), dan reviewer
   menghabiskan tenaga mencurigai **penghapusan bukti yang tidak pernah terjadi**.
   **Kewajiban reviewer: nyatakan di verdict diff mana yang kamu pakai.** Cek append-only dan
   kelengkapan-vs-isi-PR dilakukan pada **(A)**; delesi yang hanya muncul di **(B)** pada berkas yang tidak
   ada di **(A)** **BUKAN** penghapusan oleh penulis PR melainkan base yang bergerak. Kalau merge-base tidak
   bisa dihitung (objek tidak ada lokal, riwayat git terpotong), pembangkit prompt **wajib menyatakannya**
   dan reviewer **tidak boleh** menggantinya dengan tebakan.
3. Daftar pemeriksaan terverifikasi-able (append-only diff, grep audit, jalankan tools, cek status via API) — bukan pertanyaan opini.
4. Bila ada sengketa penilaian (mis. materialitas paparan): pertanyaan yang harus dijawab EKSPLISIT + kalimat "kamu satu-satunya pemutus; jangan menelan mentah penilaian pihak yang dinilai".
5. Batasan: aturan 6d di atas; larangan menyentuh branch orang; larangan mengutip jawaban selama jendela terbuka.
6. Mekanika putusan: hijau → komentar (status+pointer) lalu merge hanya jika diizinkan; merah → jangan merge apa pun, laporkan + perintah reproduksi, PR dibiarkan OPEN, keputusan ke pemilik.

## Sumber prompt (disetujui pemilik 8 Sep 2026)

Alasan perubahan: **mekanisme harus bisa dipakai tanpa perantara sesi.** Sebelum ini, pemilik hanya punya prompt review kalau ada sesi perantara yang mengarangnya — artinya pihak yang direview menulis instruksi bagi pengadilnya, dan matinya satu sesi berarti tidak ada prompt sama sekali.

1. **Prompt review dibangkitkan alat, bukan dikarang.** Sumber resminya `tools/review_prompt.py`. Semua nomor PR, base sha, head sha, dan daftar berkas berasal dari data PR di GitHub + isi pohon kerja, bukan dari narasi siapa pun.
2. **Sesi yang membuka PR WAJIB menempel keluaran alat itu sebagai SATU BLOK BERPAGAR di badan pesan chat terakhir sesi** (`python3 tools/review_prompt.py --pr <N>`), utuh, tanpa disunting. Keluaran perintah yang terlipat bukan bukti; kalau blok itu tidak ada di badan pesan, langkah penutupan BELUM dikerjakan dan PR belum boleh dinilai. Kalau blok itu tidak ada, pemilik harus membuka sesi baru dari main dan membangkitkan sendiri dengan `python3 tools/review_prompt.py --pr <N>`.
3. **Kalau sesi mati sebelum sempat**, pemilik membangkitkannya sendiri dengan perintah yang sama — tidak perlu menunggu sesi perantara, tidak perlu menulis ulang prompt.
4. **Larangan:** sesi yang direview TIDAK boleh mengarang, menambah, memotong, atau menyunting isi prompt review untuk dirinya sendiri. Kalau ia merasa reviewer butuh konteks tambahan, konteks itu masuk ke **body PR** (objek yang diperiksa), bukan ke prompt (instruksi pengadil).
5. Pemilik juga tidak perlu menulis ulang prompt: versi placeholder siap tempel ada di `PANDUAN_PENGGUNA.md` §"Minta Review, Tanpa Perantara", dibangkitkan `python3 tools/review_prompt.py --generic`.
6. Alat itu deterministik untuk data PR yang sama, tidak menulis berkas apa pun kecuali diminta `--out`, dan gagal keras (exit non-zero) daripada mencetak prompt dengan sha kosong.

## Penulisan hasil
- Meta: bagian baru di `_meta/ACCEPTANCE_TESTS.md` (log review per peristiwa singkat) atau `LOG_SESI` sesi reviewer; yang substantif di log acceptance sistem terkait.
- Sistem domain: subbagian append-only di ACCEPTANCE_TEST_LOG.md-nya ("Koreksi pasca-review independen" adalah pola yang benar).
- **Komentar verdict di GitHub dibaca ALAT, bukan manusia** (`tools/ambil_verdict.py`): baris pertama harus
  judul Markdown yang memuat kata putusan (`MERAH` / `HIJAU` / `BERSIH` / `ADA TEMUAN` / `TIDAK BISA
  DISIMPULKAN` / `APPROVE` / `REQUEST_CHANGES`), **tidak** memuat kata `penulis` / `koreksi terbuka` /
  `tanggapan penulis`, dan **tidak** berada di dalam pagar kode. **Sebab aturan ini:** prompt pembangkit tidak
  pernah menyebut syarat baca alat pengumpul, jadi verdict yang **sampai tetapi melenceng formatnya** tidak
  terhitung sebagai slot dan kuorum gagal **diam-diam** (tanpa pesan error). **Batas klaim, diukur pada PR #74:**
  kanal PR itu memuat 6 komentar — 5 milik penulis (benar digolongkan BUKAN SLOT) dan 1 verdict hakim (terbaca
  MERAH) — jadi dua verdict yang hilang pada putaran pertama **tidak pernah ditempel sama sekali**, bukan gagal
  dibaca. Aturan format ini menutup **modus kegagalan yang berbeda dan belum sempat terjadi**; ia **tidak**
  menjelaskan kuorum 1/3 yang lama dan tidak boleh diklaim sebagai penjelasannya. Formatnya dicetak pembangkit
  sebagai bagian 6a (termasuk kewajiban mengganti nomor putaran, bukan menyalin `putaran 1` mentah), dan
  **kesepakatannya diuji lintas alat** — contoh judul yang diwajibkan prompt harus benar-benar terbaca oleh
  `slot_hakim()` dan `simpulkan()`, bukan hanya terlihat benar di mata.
- **Kalau PR menyentuh alat pengadil, perintah merge di prompt DIGANTI larangan.** Sebelum perbaikan ini
  bagian "Aturan keputusan" mencetak `gh pr merge <N> --merge` untuk PR yang bagian "Pengecualian pengadil"-nya
  sendiri **melarang** merge — kontradiksi di dalam satu dokumen, dan yang muncul lebih dulu adalah perintah
  merge. Supresinya **bersyarat**: PR yang tidak menyentuh alat pengadil tetap memakai aturan merge normal,
  dan **kedua arah** itu diuji (supresi tanpa syarat akan melumpuhkan review PR biasa).
- Aturan lama penulis tetap berlaku: yang dilarang tetap dilarang (6a/6b/6d), reviewer hanya menambah lapisan verifikasi, tidak menghapus kewajiban self-check sebelum review.

## Warisan ke sistem domain
Setiap sistem yang dibangun meta ini mengemban Protokol Review Independen dengan cara: (1) mendaftar L1/L2/L3 versinya di dokumen QA sistemnya; (2) menyebut "review independen" sebagai langkah wajib pada alur yang menutup klaim DONE/gate; (3) menyiapkan varian 1-baris trigger review di PROMPT_ENTRI/panduan penggunanya ("untuk [kategori pekerjaan], buka sesi baru dan tempel prompt reviewer sesuai protokol"). Sistem boleh menurunkan level hanya dengan override tercatat di manifest.

---

## Beberapa hakim sekaligus (ditambahkan 17 Sep 2026 atas keputusan pemilik)

**Sebab bagian ini ada:** pemilik mengerahkan **3 sesi agent** untuk mereview PR #74, dan protokol ini
**tidak punya satu pun ketentuan** tentang beberapa hakim atau verdict yang bertentangan — terhitung
**0 sebutan** untuk kata "beberapa / multi / tiga / bertentangan / konflik / quorum / mayoritas".
Aturan yang tidak ada akan diimprovisasi **sesudah** verdict masuk, yaitu saat paling buruk untuk
mengarang aturan. Jadi ditulis **sebelum** verdict ke-2 dan ke-3 tiba.

**Keputusan pemilik (verbatim):** *"Selagi ada yang merah, maka harus diperbaiki."*

1. **Agregasi FAIL-CLOSED.** Beberapa verdict digabung dengan aturan: **satu saja bukan hijau → gabungan
   MENAHAN merge.** **Tidak ada mayoritas, tidak ada rata-rata, tidak ada "2 dari 3 setuju".** Yang dicari
   dari reviewer independen adalah **alasan untuk menolak**, bukan suara terbanyak — dua hakim yang puas
   tidak membatalkan temuan terukur hakim ketiga.
2. **"Tidak terbaca" BUKAN bersih.** Verdict yang tidak bisa ditentukan statusnya **menahan** merge,
   sama seperti verdict merah. Alasannya sama dengan aturan repo yang lain: *ketiadaan bukti bukan bukti
   ketiadaan masalah.*
3. **Cakupan parsial tidak bisa dinaikkan jadi hijau oleh verdict lain.** Kalau seorang hakim menyatakan
   laporannya **parsial** ("bukan review lengkap"), bagian yang belum diperiksanya **tetap belum
   diverifikasi** — tidak menjadi hijau karena hakim lain lulus. Statusnya: **belum terverifikasi**.
4. **Setiap verdict WAJIB menyebut SHA head yang dinilainya.** Head bisa bergerak selama review berjalan
   (terjadi nyata di PR #74: reviewer menilai `3543612` sementara head sudah `17ada02`). Verdict tanpa
   SHA head **tidak bisa dipetakan** ke keadaan mana pun dan harus diperlakukan sebagai **belum terverifikasi**.
5. **Koreksi DITUNGGU sampai semua hakim masuk, lalu SATU putaran.** Alasannya: butir 7 di atas membatasi
   **maksimal 2 putaran**. Mengoreksi tiap kali satu verdict masuk akan menghabiskan jatah putaran dan
   membuat objek review hakim lain basi. Pengecualian: **perbaikan pada instrumen pengukur verdict itu
   sendiri boleh segera** (kalau alatnya salah membaca, semua verdict berikutnya ikut salah terbaca).
6. **Format verdict WAJIB terbaca mesin.** Putusan ditulis pada **baris judul Markdown** atau pada
   **baris deklarasi eksplisit** berbentuk `**VERDICT:** MERAH` / `**VERDICT:** HIJAU`.
   **Jangan menggantungkan putusan pada kata di dalam prosa.**
   **Sebab aturan ini ada (cacat D-1, nyata terjadi):** alat penjemput verdict mengambil kecocokan
   **pertama di mana saja**, dan kosakatanya **tidak memuat kata MERAH/HIJAU sama sekali** — akibatnya
   laporan berjudul *"MERAH … Jangan merge"* terbaca sebagai **BERSIH** karena kata "bersih" muncul di
   dalam **kalimat larangan** pada karakter ke-5646, sedangkan kata "MERAH" ada di karakter ke-35.
   **Itu fail-open pada instrumen keselamatan.** Sudah diperbaiki + **diuji-mutasi**
   (`python3 tools/ambil_verdict.py --uji`).
7. **Alatnya:** `python3 tools/ambil_verdict.py --pr <N>` mencetak verdict per hakim **dan agregasi
   fail-closed**-nya. **Membaca verdict ≠ menyetujuinya** — bertindak atas temuan tetap butuh keputusan
   pemilik, dan PR yang mengubah alat pengadil **tidak boleh di-merge oleh reviewer**.
8. **Verdict WAJIB mendarat di kanal tahan lama — komentar di utas PR — sebelum sesi hakim ditutup.**
   **Sebab aturan ini ada (kejadian nyata 18 Sep 2026):** pemilik mengerahkan **3 hakim** untuk PR #74,
   tetapi **hanya 1 verdict yang sampai ke GitHub**. Pencarian menyeluruh di **63 ref** (semua branch)
   tidak menemukan jejak dua verdict lainnya: tidak ada komentar, tidak ada review resmi, tidak ada
   komentar baris, tidak ada commit, tidak ada berkas log sesi. Hakim yang menyimpan laporannya hanya di
   `/tmp` dan di chat sesinya **tidak meninggalkan bukti yang bisa diverifikasi oleh siapa pun** —
   termasuk oleh pemiliknya sendiri, dan termasuk oleh sesi berikutnya yang harus menindaklanjuti.
9. **Kuorum DIHITUNG, bukan diasumsikan.** Yang mengumpulkan verdict WAJIB menjalankan
   `python3 tools/ambil_verdict.py --pr <N> --harapkan <jumlah hakim yang dikerahkan>`. Bila slot yang
   terbaca kurang dari jumlah itu, alat melaporkan **KUORUM BELUM TERPENUHI** dan hasilnya **tidak pernah
   hijau** — hakim yang tidak menyerahkan laporan **bukan hakim yang puas**.
   **Sebab aturan ini ada (cacat D-3, nyata terjadi):** alat lama menganggap **setiap komentar sebagai
   slot hakim**, jadi 3 komentar penulis PR #74 ikut terhitung dan keluarannya berbunyi *"1 dari 4 verdict
   bukan hijau"*. Itu terdengar seperti tiga hakim lain tidak menemukan apa-apa; yang sebenarnya terjadi
   adalah **2 verdict hilang**. **Keheningan terbaca sebagai persetujuan** — persis kebalikan fail-closed.
   Perbaikannya diuji-mutasi, dan `--uji` kini **memanggil fungsi kanal sungguhan** (regresi D-4: kanal
   `--issue` dan kanal utama `--terbaru` dulu **crash `NameError`** setiap kali isunya punya komentar, dan
   lolos dari `--uji` karena uji lama hanya menguji fungsi murni, tidak pernah fungsi kanal).
10. **Verdict yang hilang = pekerjaan belum dilakukan, dan WAJIB diulang pada head yang berlaku.** Tidak
    ada jalur "dianggap hijau karena tidak ada kabar", dan tidak ada jalur "sudah terlanjur, pakai yang
    ada". Bila dua hakim memakai **branch atau slot log yang sama**, push yang datang kemudian **menimpa**
    yang lebih dulu — karena itu tiap hakim wajib memakai branch/slot lognya sendiri, dan **menempel
    verdictnya sebagai komentar PR sebelum sesi ditutup** (butir 8), supaya hasilnya tidak bergantung pada
    umur branch mana pun.
