# Cara Kerja Meta-Sistem

### Ini repo tunggal yang menampung BANYAK sistem berbeda — bukan cuma 1 sistem untuk 1 domain, tapi tempat membangun sistem APAPUN (konten kreator, ruang belajar, fondasi aplikasi, atau domain lain). File ini adalah peta besar: baca ini dulu sebelum menyentuh sistem manapun di repo ini.

---

## Kenapa repo ini ada

Setelah 1 sistem berhasil dibangun dan teruji (Sistem Konten Kreator — lihat `sistem-konten-kreator/`), muncul kebutuhan yang lebih besar: kemampuan membangun sistem SEJENIS untuk domain apapun, tanpa merancang ulang dari nol setiap kali, sambil tetap menjaga kualitas maksimal untuk tiap sistem yang dibangun (bukan dikompromikan demi keseragaman).

**Prinsip inti yang membedakan meta-sistem ini dari sekadar "kumpulan template":**

> **Isi/konten tiap sistem = SPESIFIK dan maksimal untuk kebutuhan itu saja.** Sistem TIDAK dibuat generik/abstrak dengan alasan "supaya gampang dijadikan template nanti". Kemampuan untuk dijadikan template atau diduplikasi adalah **efek samping dari struktur yang rapi**, bukan tujuan aktif yang dikejar saat membangun. Struktur/organisasi file yang konsisten rapi berlaku di semua sistem — itu yang membuat duplikasi/jadi-template bisa dilakukan kapan saja (baik direncanakan dari awal maupun muncul tiba-tiba bertahun-tahun kemudian) tanpa persiapan khusus di muka.

---

## Struktur Repo

```
repo-utama/
├── _meta/
│   ├── SYSTEM_MANIFEST.md            ← manifest meta-sistem ini
│   ├── 00_CARA_KERJA_META.md         ← file ini
│   ├── 01_DISCOVERY_LEVEL_0.md       ← gali "sistem apa ini, struktur macam apa"
│   ├── 02_PRINSIP_UNIVERSAL.md       ← prinsip default untuk semua sistem
│   ├── INDEKS_SISTEM.md              ← daftar semua sistem + status
│   ├── SYSTEM_MANIFEST_TEMPLATE.md   ← kontrak identitas tiap sistem
│   ├── DEFINITION_OF_DONE.md         ← kriteria selesai dan rilis
│   ├── PROTOKOL_CHECKPOINT_RECOVERY.md ← status persisten dan pemulihan
│   ├── QUALITY_ASSURANCE_AND_EVOLUTION.md ← audit, upgrade, dan rollback tiga lapisan
│   ├── ACCEPTANCE_TESTS.md            ← skenario uji perilaku meta-sistem
│   ├── SESSION_REPORT_TEMPLATE.md     ← format laporan awal setiap sesi
│   └── FAILURE_INJECTION_TESTS.md    ← uji jalur gagal dan state abnormal
│
├── sistem-[nama-1]/                  ← misal sistem-konten-kreator/
│   └── (struktur & jumlah file BEDA-BEDA per sistem, ditentukan hasil
│        Discovery, TIDAK dipaksa sama seperti sistem lain)
│
├── sistem-[nama-2]/                  ← sistem lain, struktur sendiri
│
├── _pegangan-kamu/                   ← file milik pengguna, boleh ikut repo,
│                                        BUKAN instruksi kerja untuk agent
│
└── _cadangan-claude/                 ← ringkasan tiap sistem untuk sesi
                                          Claude chat biasa (cadangan lmarena Agent)
    ├── RINGKASAN_sistem-nama-1.md
    └── RINGKASAN_sistem-nama-2.md
```

**Kenapa dipisah begini:** `_meta/` berisi instruksi yang berlaku LINTAS semua sistem (cara membangun sistem apapun) — dipisah dari `sistem-*/` yang isinya spesifik per sistem, supaya prinsip umum tidak perlu ditulis ulang tiap kali bikin sistem baru, tapi tiap sistem tetap bebas override kalau prinsip umum itu tidak cocok untuk domainnya.

---

## Setup Repo Baru (SEKALI di awal, sebelum sesi agent pertama)

Berlaku sama seperti yang sudah terbukti penting di Sistem Konten Kreator: GitHub otomatis membuat branch `main` begitu repo baru dibuat — ini sudah otomatis, TIDAK perlu diusahakan manual. Yang WAJIB dilakukan secara sadar:

1. Setelah repo dibuat di GitHub, push semua isi meta-sistem ini (folder `_meta/`, `sistem-konten-kreator/`, `_cadangan-claude/`, `PANDUAN_PENGGUNA.md`) LANGSUNG ke `main` — baik lewat push manual, atau sesi agent pertama diarahkan eksplisit bekerja dari `main` yang sudah terisi.
2. **Jangan pernah hapus branch `main`** selama repo ini aktif dipakai — kalaupun ada kebutuhan restrukturisasi besar, itu keputusan sadar yang dicatat, bukan tindakan spontan.
3. Sebelum deploy/pakai hasil kerja apapun, selalu **merge dulu** PR yang relevan ke `main` — jangan asumsikan hasil kerja di suatu branch otomatis "sudah jadi" sebelum di-merge.

*(Alasan detail di balik 3 poin ini — termasuk kasus nyata yang jadi pelajaran — ada di `sistem-konten-kreator/00_CARA_PAKAI_SISTEM.md` bagian Kategori 0, dan di dokumen audit sistem itu. Prinsipnya sama persis, cuma sekarang berlaku untuk SELURUH repo meta-sistem, bukan cuma 1 sistem.)*

---

## Kapan Pakai File yang Mana

**APAPUN tujuan sesi ini, WAJIB dilakukan dulu di awal (Entry Point tingkat repo):**
1. Buat laporan awal mengikuti `SESSION_REPORT_TEMPLATE.md`; verifikasi repo, branch, working tree, commit, dan PR.
2. Cek apakah ada PR yang masih terbuka/menggantung di repo ini — dari SISTEM MANAPUN, bukan cuma sistem yang mau dikerjakan sekarang. Karena repo ini menampung banyak sistem sekaligus, PR menggantung dari sistem lain bisa gampang terlupakan kalau tidak dicek di level repo, bukan cuma di level 1 sistem.
3. Cek `INDEKS_SISTEM.md` untuk tahu sistem apa saja yang ada dan statusnya.

Baru setelah itu, arahkan sesuai tujuan. Jika state tidak konsisten, gunakan `FAILURE_INJECTION_TESTS.md` sebagai aturan berhenti dan recovery:

**Mau bangun sistem BARU dari nol** → mulai dari `01_DISCOVERY_LEVEL_0.md`, ikuti alur di bagian "Alur Kerja: Membangun Sistem Baru dari Nol" di bawah.

**Mau lanjut/audit sistem yang SUDAH ADA** → dari `INDEKS_SISTEM.md` yang sudah dicek di atas, masuk ke folder `sistem-[nama]/` itu dan baca dokumen navigasi di dalamnya (analog `START_DI_SINI.md` di sistem konten kreator — tiap sistem punya dokumen serupa, isinya spesifik ke sistem itu). **JANGAN baca seluruh isi repo di awal** — cukup baca yang relevan dengan sistem yang dituju, baru baca lebih dalam sesuai kebutuhan aktual.

**Mau pakai Claude chat biasa sebagai cadangan** (karena lmarena Agent kurang maksimal saat itu) → lihat bagian "Alur Kerja: Menggunakan Claude Chat Biasa sebagai Cadangan" di bawah.

---

## Alur Kerja: Membangun Sistem Baru dari Nol

```
1. DISCOVERY LEVEL-0
   Jalankan 01_DISCOVERY_LEVEL_0.md
   → Gali: sistem ini tentang apa, siapa yang pakai, apakah berhierarki/
     flat/siklus, apa yang harus konsisten, kapan 1 unit kerja dianggap
     selesai
   → Output: dokumen rencana kerangka (BUKAN sistem itu sendiri, BUKAN
     JUGA prompt Discovery detailnya — baru peta dokumen apa saja yang
     akan dibangun, dengan fungsi masing-masing)

2. BUAT folder `sistem-[nama-baru]/` dan salin `SYSTEM_MANIFEST_TEMPLATE.md`
   menjadi manifest sistem tersebut. Buat skeleton kosong sesuai rencana
   kerangka dari Langkah 1.

3. UNTUK TIAP DOKUMEN yang direncanakan: TULIS DULU prompt Discovery
   detailnya (dokumen generator, setara 01_BRAND_CORE.md/
   02_CHANNEL_DISCOVERY_PROMPT.md di sistem konten kreator — ini BELUM
   ADA untuk sistem baru manapun, harus ditulis dari nol berdasarkan
   rencana kerangka Langkah 1). Simpan di dalam folder sistem-[nama-baru]/
   itu sendiri — bukan di _meta/, karena isinya spesifik ke sistem ini

4. BARU SETELAH prompt generator di Langkah 3 ada: jalankan Discovery
   detailnya (gali lewat diskusi, checkpoint berkala, tulis final setelah
   dikonfirmasi)

5. AUDIT MENYELURUH sebelum dianggap selesai — baca ulang semua dokumen,
   cross-check konsistensi rujukan, verifikasi tidak ada yang hilang/
   kontradiktif, jalankan `DEFINITION_OF_DONE.md`, dan uji recovery.
   Lakukan lebih dari 1 putaran kalau sistemnya kompleks — lihat pengalaman
   audit Sistem Konten Kreator sebagai acuan seberapa dalam ini perlu dilakukan.

6. UPDATE `INDEKS_SISTEM.md` — tambah entri sistem baru ini, tanggal dibuat

7. BUAT RINGKASAN_sistem-[nama-baru].md di _cadangan-claude/
```

**Catatan penting soal Langkah 3:** ini beda dari sistem konten kreator, di mana `01_BRAND_CORE.md` dkk sudah tersedia siap pakai sejak awal (karena domainnya sudah diketahui dari awal). Untuk sistem baru dengan meta-sistem ini, prompt generatornya belum ada — jadi ada 1 langkah tambahan yang tidak boleh dilewati atau diasumsikan otomatis ada.

---

## Alur Kerja: Melanjutkan/Mengaudit Sistem Lama

*(Entry Point tingkat repo di atas — cek PR menggantung & INDEKS_SISTEM — sudah dilakukan duluan sebelum alur ini dimulai)*

```
1. Dari INDEKS_SISTEM.md yang sudah dicek — kalau sistem yang mau
   disentuh punya tanggal "terakhir disentuh" yang sudah lama, TAWARKAN
   audit dulu sebelum lanjut kerja ("sistem ini terakhir disentuh
   [tanggal], mau saya audit dulu sebelum lanjut, atau langsung saja?")

2. Masuk ke folder sistem-[nama]/, baca dokumen navigasinya (analog
   START_DI_SINI.md), lanjutkan kerja sesuai kebutuhan

3. Begitu selesai kerja (apapun jenisnya), UPDATE tanggal "terakhir
   disentuh" di INDEKS_SISTEM.md — WAJIB, jangan sampai lupa dicatat
   manual (pencatatan ini manual, TIDAK mengandalkan pembacaan git
   history)
```

---

## Alur Kerja: Menggunakan Claude Chat Biasa sebagai Cadangan

```
1. Upload ke sesi Claude: RINGKASAN_sistem-[nama].md (dari
   _cadangan-claude/) + dokumen SPESIFIK yang mau dikerjakan/direvisi
   saat itu (TIDAK perlu semua file sistem itu)

2. Claude baca ringkasan → paham struktur, prinsip, dan KE MANA hasil
   kerja ini akan dibawa

3. Claude kerja seperti biasa (diskusi/audit/revisi)

4. Pengguna paste manual hasil kerja Claude ke lokasi yang sesuai di
   Obsidian (sync otomatis ke GitHub via plugin git)

5. Update RINGKASAN_sistem-[nama].md kalau ada perubahan STRUKTURAL
   besar (bukan tiap perubahan kecil) — supaya sesi Claude berikutnya
   tidak baca ringkasan yang sudah usang
```

---

## Lapisan Kendali dan Definition of Done

Selain dokumen instruksi aktif, setiap sistem baru wajib mewarisi mekanisme pemeriksaan, audit, evolusi, dan verifikasi output tiga lapisan dari `QUALITY_ASSURANCE_AND_EVOLUTION.md`, kecuali override eksplisit dicatat di manifest. Setiap sistem baru juga wajib memiliki manifest dan status kerja yang dapat dibaca lintas sesi. Gunakan `SYSTEM_MANIFEST_TEMPLATE.md` sebagai dasar, `DEFINITION_OF_DONE.md` untuk menentukan apakah hasil benar-benar selesai, dan `PROTOKOL_CHECKPOINT_RECOVERY.md` untuk menyimpan progres serta memulihkan sesi yang terputus.

Status “selesai” tidak berarti file sudah ditulis. Status tersebut baru boleh digunakan setelah acceptance checklist terpenuhi, dependency diverifikasi, approval selesai, dan perubahan tersedia di branch/PR yang benar.

Dokumen audit dan draft di `_meta/_internal/` adalah referensi master, bukan instruksi kerja yang harus diikuti pada setiap sesi. Jika instruksi aktif bertentangan dengan catatan sejarah, instruksi aktif dan keputusan terbaru yang sudah disetujui menjadi acuan; konflik tetap harus dilaporkan, bukan ditebak.

## Prinsip yang Berlaku di Semua Sistem

Lihat `02_PRINSIP_UNIVERSAL.md` untuk daftar lengkap + penjelasan. Ringkasnya: Hierarki (kalau relevan), Rantai/Chaining, Approval Bertingkat, Checkpoint & Verifikasi Konsistensi (kalau relevan), Log Keputusan, serta Quality Assurance & Evolusi tetap dipertahankan. Semua ini DEFAULT berlaku, tapi tiap sistem boleh override kalau memang tidak cocok untuk domainnya — asal dicatat alasannya di dokumen sistem itu.

---

## Kebiasaan Umum yang Perlu Dijaga (dipakai ulang dari Sistem Konten Kreator, terbukti works)

- **Branch & merge**: tiap sesi kerja dapat branch sendiri, tidak pernah auto-merge, review sesuai Approval Bertingkat sebelum merge ke `main`
- **Entry Point**: di awal sesi baru, cek dulu status kerja yang menggantung, tanya tujuan sesi ini, baca file relevan sendiri — tidak perlu ditempel manual
- **1 dokumen direvisi/dibangun penuh dulu, baru lanjut ke dokumen berikutnya** — bukan banyak sekaligus, supaya kesalahan kecil tidak menyebar sebelum ketahuan
