> Sumber: _sistem/03_KEBIJAKAN_LEBUR.md sha 22552a52fd2a357f5c93ef29e2796ab5647bf402 tanggal 2026-09-16 versi-kit 0.2.1

# 03 — Kebijakan Lebur (Aturan Tanam Permanen)

> Enam aturan yang mengatur SETIAP byte yang ditulis ke repo target selama run — supaya hasil klinik "terlihat normal tapi terukur lebih baik", bukan terlihat seperti dijajah. Nama "lebur": kit datang, bekerja, lalu melebur ke dalam target tanpa meninggalkan badan asing.
> Sumber keputusan: 00_RENCANA_KERANGKA.md (jangkar konsistensi #2, di-merge PR #43 `a4331f8`) + Discovery Level-0 11 Sep 2026. Dipakai oleh Tahap C dan tahap verifikasinya di 01_ALUR_RUN §6–§7; berlaku penuh juga di panggung rawat inap (K-11).
> Provenance prinsip: dokumen meta di folder induk repo ini — aturan yang benar-benar dipakai saat run SELURUHNYA di dokumen ini dan turunannya di kit (folder sistem harus berfungsi penuh saat dibawa keluar).
> **Status berlaku:** menstandarkan desain; run nyata baru sah setelah kit dirakit (06_RITME_KIT) dan Tahap manifest = `siap-pakai`.

---

## Kapan dokumen ini dipakai

- Setiap kali run MENULIS apa pun ke target: file baru, tambahan isi, perbaikan, penghapusan — Tahap C tindakan, termasuk tanaman Kontrak Tanaman (04) dan instalasi kapabilitas (05).
- Aturan 2 dan 4 bersifat absolut (tidak punya jalur pengecualian selain jalur approval-nya sendiri). Bila konvensi target TAMPAK bertentangan dengan salah satunya, itu keadaan berhenti fail-closed (01 §13) — bukan alasan pengecualian.
- Melanggar satu aturan = run tidak boleh dinyatakan selesai (checklist 01 §15).

## Pohon keputusan tanam (ringkas)

```
MAU MENANAM SESUATU KE TARGET
│
├─ Apakah konten/targetnya yang sudah ada akan ditimpa/dihapus?
│   └─ YA  → berhenti: hanya sah bila item-nya diizinkan EKSPLISIT per-item (Aturan 2)
│
├─ Apakah target sudah punya padanan (panduan/log/status/aturan/rekam)?
│   ├─ YA  → EXTEND dokumen itu (Aturan 1); bentuknya ikut konvensi target (Aturan 3)
│   └─ TIDAK → buat file baru non-destruktif (Kecil — jalan + lapor di G-Final)
│
└─ Setelah selesai menanam:
    ├─ kit dan berkas kerja tidak ikut git (Aturan 4)
    ├─ istilah klinik tidak ikut menempel (Aturan 5)
    └─ rekam klinik mencatatnya (Aturan 6)
```

---

## Aturan 1 — Padanan dulu: EXTEND > CREATE

**Aturan.** Sebelum menanam artefak apa pun, cari dulu padanannya di target (panduan pengguna, log, STATUS, aturan, README, rekam). Padanan ADA → tambahkan ke dokumen itu. File baru hanya bila memang tidak ada padanannya.

**Cara menilai "padanan":** fungsi sama (mencatat status, mencatat riwayat, menjelaskan cara pakai), bukan nama sama. Target menyebutnya "CARA-PAKAI.md" sementara kit membawa "PANDUAN" — tetap padanan.

| Benar | Salah |
|---|---|
| Target punya `STATUS.md` sendiri (bentuk beda) → field deterministik klinik ditambahkan KE `STATUS.md` itu | Bikin `STATUS-KLINIK.md` terpisah → dua sumber kebenaran, run berikutnya baca yang salah |
| Target punya log keputusan di setiap dokumen → butir baru masuk tabel itu | Bikin dokumen "KEPUTUSAN-KLINIK.md" kembaran |
| Padanan mencakup separuh fungsi → extend + catat batasnya di tempat sama | Memakai alasan "padanannya tidak persis sama" untuk bikin kembaran |

**Padanan parsial/rusak:** tetap extend — jangan kembaran. Kualitas buruknya padanan jadi ITEM RENCANA tersendiri ("perbaiki padanan X"), diputuskan pemilik; bukan alasan diam-diam membuat pengganti.

**Kenapa:** dokumen kembar = amnesia terorganisir — dua sumber kebenaran, run berikutnya (idempotensi) membaca yang salah, dan pemilik mewarisi duplikat selamanya.

## Aturan 2 — Overwrite & hapus konten target: selalu per-item

**Aturan.** Konten target yang sudah ada TIDAK PERNAH ditimpa atau dihapus tanpa persetujuan EKSPLISIT per item — dijahit sejak G-Rencana (rencana memuat item per item, termasuk yang menimpa) atau diborong susulan bila muncul di tengah jalan (K-10). "Konten" = kalimat, bagian, format, nama — bukan cuma berkas utuh.

**Yang BUKAN overwrite:** menambah file baru non-destruktif; menambah bagian baru ke akhir dokumen tanpa menyentuh isi lama (tetap wajib Aturan 1).

**Wajib pada setiap overwrite yang diizinkan:** catat di rekam klinik — berkas, kondisi SEBELUM (kutipan/baris), kondisi SESUDAH, item rencana yang mengizinkan — supaya rollback bisa presisi (Quality & Evolution manifest: tidak pernah menghapus diam-diam).

**Pensiunkan, jangan hapus (panen C-07, 2026-09-16).** Dokumen target yang **digantikan** oleh tanaman run ini (pedoman lama vs pegangan yang ditanam, catatan usang vs manifest yang disegarkan) TIDAK boleh dibiarkan hidup tanpa penanda — dan tidak boleh dihapus diam-diam. Yang wajib: sisipkan **penanda di kepala berkas** ("VERSI LAMA — SUDAH DIGANTIKAN, JANGAN DIIKUTI") + penunjuk dokumen yang berlaku + tabel koreksi per topik bila ada angka/instruksi yang bertentangan; **isi asli di bawah penanda tidak disunting** (append-only). Aturan 2 sudah melarang overwrite/hapus; butir ini menutup celah **sebaliknya** — dokumen lama tanpa penanda tidak menimpa satu byte pun, tetapi tetap merusak **keputusan** pembaca yang kebetulan membukanya.

| Benar | Salah |
|---|---|
| Rencana item #3 menyebut eksplisit "ganti bagian X di `ATURAN.md` dengan Y" → disetujui → jalan + dicatat sebelum/sesudah | "Merapikan" kalimat/struktur target sekalian karena katanya lebih baik — TIDAK sah, bukan item rencana |
| Hapus mekanisme mati yang disepakati item #5, dengan catatan rollback | Hapus karena "kelihatannya tak terpakai" tanpa izin |
| Koreksi kecil melebihi lingkup item ditemukan → masuk borongan susulan K-10 | Menyelipkan koreksi "sekaliburasa" ke item lain |
| Dokumen target yang digantikan diberi penanda arsip + penunjuk dokumen berlaku; isi aslinya utuh di bawah penanda | Dokumen lama dibiarkan hidup tanpa penanda (pembaca mengikuti aturan usang), atau dihapus karena "sudah ada penggantinya" tanpa izin item |

**Kenapa:** ini wilayah pemilik; klinik tukang perbaikan, bukan pemilik rumah. Satu overwrite tak berizin cukup membuat seluruh hasil run tak bisa dipercaya.

## Aturan 3 — Konvensi target menang

**Aturan.** Artefak tertanam ikut BAHASA, PENAMAAN, FORMAT, dan STRUKTUR target — bukan format kit. Konvensi menang bahkan bila konvensi kit "lebih rapi".

**Urutan konvensi bila target belum punya:** (1) konvensi yang sudah tertanam run klinik sebelumnya di target itu (lihat rekam); (2) bila sama sekali belum ada — gunakan bentuk template kit sebagai USULAN konvensi, tandai eksplisit di rencana + rekam bahwa ini usulan yang boleh diganti pemilik.

| Benar | Salah |
|---|---|
| Semua dokumen target bahasa Indonesia + gaya singkat → tanaman ditulis begitu | Tanaman ditulis bahasa Inggris formal karena template kit begitu |
| Target menamai unit kerjanya "deck" → artefak memakai "deck" | Memaksa kosakata kit mengganti kosakata yang sudah hidup |
| Konvensi target menaruh log di `catatan/` → log target ditanam di situ | Menaruh di lokasi bawaan kit tanpa menoleh struktur target |

**Kenapa:** target yang terlihat "seperti dirinya sendiri" adalah definisi sukses peleburan (tujuan akhir, rencana §Untuk Siapa/Apa); format asing membuat pemilik target kehilangan rasa memiliki dan run berikutnya salah baca.

## Aturan 4 — Kit tidak pernah masuk git target

**Aturan.** Folder kit dan seluruh berkas kerja sementara TIDAK PERNAH di-commit/branch/PR ke repo target — bukan di commit "sementara", bukan di branch "biar aman". Selama run: entri ignore kerja (`.gitignore` lokal target atau padanannya) + disiplin staging; diverifikasi ulang saat peleburan (`git status` bersih dari kit). Di rawat inap: aturan ini tidak berlaku secara literal karena TIDAK ADA salinan kit (master dibaca di tempatnya — K-11); yang masuk git adalah perubahan tertanam + rekam, mengikuti alur standar meta (branch → PR → merge oleh pemilik, tanpa auto-merge).

**Yang sah sebagai "aman saat crash":** commit HASIL ke branch kerja + log run berkelanjutan (01 §6.7) + rekam — bukan meng-commit kit.

| Benar | Salah |
|---|---|
| Selesai item → commit hasil ke branch kerja run; kit tetap tak terlacak git | Commit folder kit "dulu, biar tidak hilang" → jejak asing permanen di histori target |
| Peleburan: kit hilang dari workspace + ignore bersih + `git status` membuktikan | Peleburan hanya menghapus folder, tanpa cek sisa entri ignore/berkas nyasar |

**Kenapa:** "melebur dan hilang" (K-2) hanya mungkin bila kit tak pernah masuk histori; sekali ter-commit, hilangnya meninggalkan mayat di log git selamanya.

## Aturan 5 — Istilah klinik tidak menular

**Aturan.** Kosakata klinik — run, kit, suntik, rawat inap, rekam klinik, panen, kontrak tanaman, lebur, G-Rencana/G-Final — tidak dipakai di dokumen harian target. KECUALI target sudah punya istilah serupa: punya target yang menang.

**Pengecualian sempit:** REKAM-KLINIK sendiri boleh memakai istilah klinik minimal (cap versi kit, dsb.) — dia artefak milik klinik yang memang tinggal di target; tapi bentuk/namanya tetap ikut konvensi target bila target punya padanan (Aturan 3). Nama yang ditanam untuk artefak baru dipilih dari kosakata target, bukan kosakata klinik.

| Benar | Salah |
|---|---|
| Panduan target yang diperluas menyebut "unit kerja" (istilah target) | Panduan target tiba-tiba menyebut "run klinik" — kosakata asing menular ke dokumen harian |
| Rekam klinik menyimpan cap "kit v0.1.0" (butir milik klinik) | Ganti judul log target menjadi "REKAM KLINIK" padahal target sudah punya konvensi lognya sendiri |
| Artefak baru dinamai mengikuti pola penamaan target | Artefak baru dinamai dengan prefiks klinik demi "biar kelihatan asalnya" |

**Kenapa:** kekhawatiran asli pemilik di Discovery (ide mentah 11 Sep); target harus tetap bisa dibaca warga target — pemakai harian tidak perlu tahu ada klinik.

## Aturan 6 — Rekam klinik wajib

**Aturan.** Setiap run berakhir dengan REKAM-KLINIK tertulis DI TARGET (atau extend ke padanan rekam yang target punya): tanggal, panggung, cap versi kit, temuan ringkas, daftar item + status keputusannya, yang DITOLAK + alasan, rollback yang berlaku. Tanpa rekam, run TIDAK boleh dinyatakan selesai (01 §15) — dan tanpa rekam, run berikutnya kehilangan dasar idempotensinya (01 §1.3).

**Cap versi = alat deteksi basi:** bila cap di rekam lebih tua dari versi kit saat ini, run berikutnya WAJIB menawarkan naik versi (pemilik boleh menolak; penolakan dicatat).

| Benar | Salah |
|---|---|
| Run kecil ("hanya verifikasi, tidak ada perubahan") tetap mencatat: nihil perubahan + hasil verifikasi | Run "kecil" dianggap tak perlu rekam → run berikutnya tidak tahu run ini pernah terjadi |
| Item yang pemilik TOLAK dicatat + alasannya | Penolakan tidak dicatat → ditawari ulang tanpa alasan baru (melanggar K-10) |

**Kenapa:** rekam adalah ingatan jangka panjang target — satu-satunya yang tersisa setelah kit lebur (K-2); tanpa itu setiap run mulai dari nol dan "idempoten" jadi slogan.

---

## Checklist pra-penyerahan per artefak (5 cek cepat)

1. Padanan sudah dicari — ini extend, bukan kembaran? (Aturan 1)
2. Ada konten lama yang tertimpa/dihapus? → diizinkan per-item + tercatat sebelum/sesudah? Ada dokumen target yang **digantikan** tanaman ini? → sudah berpenanda arsip + penunjuk dokumen berlaku, isi asli utuh? (Aturan 2, butir "Pensiunkan, jangan hapus")
3. Bahasa/nama/format/lokasi mengikuti target? (Aturan 3)
4. Ada bagian kit yang nyasar ke pohon git target? (Aturan 4)
5. Kosakatanya bersih dari istilah klinik (kecuali rekam itu sendiri)? (Aturan 5)

Gagal satu cek = kembali ke Tahap C untuk artefak itu (01 §7). Semua lolos → rekam klinik mencatatnya (Aturan 6).

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-13 | Dokumen ditulis (urutan Langkah 2 rencana; pasangan 01_ALUR_RUN) | Ditetapkan 00_RENCANA_KERANGKA.md "Langkah setelah rencana merge"; keenam aturan sudah diputuskan di Discovery (jangkar konsistensi #2 + ide mentah kekhawatiran istilah) — dokumen [ATURAN], bukan [GENERATOR] |
| 2026-09-13 | Aturan 2 & 4 dinyatakan absolut; konflik dgn konvensi target = berhenti fail-closed, bukan pengecualian | Tanpa ini, satu "konvensi aneh" bisa dipakai membuka lubang overwrite/commit-kit; jalur sahnya tetap ada (borongan K-10), bukan jalur diam-diam |
| 2026-09-13 | Urutan konvensi bila target belum punya: tanaman run sebelumnya → template kit sebagai usulan bertanda | Menutup celah "target kosong konvensi" yang belum dijawab rencana; tetap memegang prinsip konvensi-target-menang dengan fallback yang bisa dikoreksi pemilik |
| 2026-09-16 | Aturan 2 diberi butir **"Pensiunkan, jangan hapus"** + satu baris tabel Benar/Salah + checklist pra-penyerahan butir 2 diperluas (jumlah butir checklist tetap) | Panen C-07 run klinik ke-2 pada Sistem Building Aplikasi (PR #63): Kebijakan Lebur sudah melarang overwrite/hapus tanpa izin per-item, tetapi **tidak mewajibkan penanda arsip** pada dokumen target yang digantikan — 9 dari 20 temuan run itu satu keluarga ini (`PANDUAN_PEMAKAIAN.md` pra-standar hidup tanpa penanda dan menyuruh copy satu berkas; pemilik hampir mengikutinya di pemakaian pertama). Celah kit ditutup di aturannya, bukan hanya dikoreksi di target |
| 2026-09-14 UTC / 15 Sep WIB | Sinkron K-11: header (panggung), Aturan 4 (bengkel → rawat inap: tidak ada salinan kit di panggung in-repo), Aturan 6 (kosakata: "bengkel" → "rawat inap") | Panggung bengkel dihapus — rawat inap kini alur standar meta; "kit tidak pernah di-git" tetap absolut untuk suntik, dan untuk rawat inap dinyatakan secara literal (tanpa salin kit) agar tidak ada keambiguhan |
