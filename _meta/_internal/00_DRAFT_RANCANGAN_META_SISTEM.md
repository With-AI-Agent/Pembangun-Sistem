# Draft Rancangan — Meta-Sistem Pembangun Sistem

### Dokumen diskusi/audit, BUKAN dokumen final. Tujuannya: sepakati kerangka besar dulu sebelum dieksekusi jadi file sungguhan (sama seperti pola `09_AUDIT_MIGRASI_GITHUB_AGENT.md` untuk sistem konten kreator).

---

## Latar Belakang & Tujuan

Setelah berhasil membangun **Sistem Konten Kreator** (10+1 dokumen, terverifikasi lewat 2 putaran audit), muncul kebutuhan level lebih tinggi: bukan cuma 1 sistem untuk 1 domain, tapi **1 meta-sistem yang bisa dipakai membangun sistem APAPUN** — konten kreator, ruang belajar, fondasi aplikasi, atau domain lain yang belum terpikirkan.

Sistem konten kreator yang sudah jadi akan menjadi **bukti/contoh pertama** yang dipakai untuk menguji meta-sistem ini bekerja atau tidak — bukan dirancang dari nol tanpa contoh nyata.

---

## Prinsip Dasar yang Sudah Disepakati

1. **1 repo (tersambung Obsidian 2 arah, terverifikasi berhasil) menampung BANYAK sistem** — bukan 1 repo per sistem. Sinkronisasi 2 arah: lmarena push ke GitHub → Obsidian pull otomatis; Obsidian edit → push balik ke GitHub. GitHub tetap 1 sumber kebenaran.

2. **Isi/konten tiap sistem = SPESIFIK dan maksimal untuk kebutuhan itu saja** — TIDAK dibuat generik/abstrak dengan alasan "supaya gampang dijadikan template nanti". Kemampuan untuk dijadikan template adalah **efek samping dari struktur yang rapi**, bukan tujuan aktif yang dikejar saat membangun. (Ini koreksi penting dari asumsi awal yang keliru — lihat Log Diskusi di bagian akhir.)

3. **Struktur/organisasi file = konsisten rapi di SEMUA sistem** — bukan supaya "siap jadi template", tapi karena itu praktik baik yang berlaku universal, terlepas dari sistem itu nanti dijadikan template atau tidak.

4. **Duplikasi/jadi-template bisa dipicu KAPAN SAJA** — baik direncanakan dari awal maupun muncul tiba-tiba (bahkan bertahun-tahun kemudian). Karena strukturnya sudah konsisten rapi sejak awal (prinsip 3), ini otomatis bisa dilakukan kapan pun tanpa persiapan khusus di muka.

5. **Audit ulang sistem lama = manual, dipicu kontekstual** (bukan terjadwal otomatis) — agent menawarkan audit begitu pengguna MEMBUKA/menyentuh lagi sistem yang sudah lama tidak disentuh, bukan mengganggu di waktu acak tanpa alasan. Status "terakhir disentuh" dicatat MANUAL oleh agent (bukan mengandalkan pembacaan git history yang belum terverifikasi kemampuannya).

6. **2 metode kerja saling melengkapi:** lmarena Agent (utama, akses baca-tulis repo langsung) dan Claude chat biasa (cadangan, ketika lmarena kurang maksimal) — hasil kerja dari metode manapun harus bisa masuk ke sistem yang sama tanpa banyak penyesuaian manual.

---

## Kerangka Struktur Repo (Draft)

```
repo-utama/
├── _meta/
│   ├── 00_CARA_KERJA_META.md         ← peta besar: cara pakai seluruh repo ini
│   ├── 01_DISCOVERY_LEVEL_0.md       ← gali "sistem apa ini, struktur macam apa yang dia butuh" (BARU, belum ada di sistem lama)
│   ├── 02_PRINSIP_UNIVERSAL.md       ← prinsip yang terbukti works, berlaku default ke semua sistem (bisa di-override per sistem)
│   └── INDEKS_SISTEM.md              ← daftar semua sistem + status/tanggal terakhir disentuh (dicatat manual)
│
├── sistem-[nama-1]/                  ← misal sistem-konten-kreator/ (sudah ada, dipindah ke sini)
│   └── (struktur & jumlah file BEDA-BEDA per sistem, ditentukan hasil Discovery Level-0 + Discovery detail,
│        TIDAK dipaksa sama seperti sistem lain)
│
├── sistem-[nama-2]/                  ← sistem baru berikutnya, struktur sendiri
│
├── _pegangan-kamu/                   ← file milik pengguna, boleh ikut repo, ditandai eksplisit "bukan instruksi
│                                        kerja agent" supaya tidak membingungkan
│
└── _cadangan-claude/                 ← 1 file ringkas per sistem untuk sesi Claude chat biasa
    ├── RINGKASAN_sistem-nama-1.md
    └── RINGKASAN_sistem-nama-2.md
```

---

## Alur Kerja: Membangun Sistem Baru dari Nol

```
1. DISCOVERY LEVEL-0 (BARU — belum ada di sistem konten kreator)
   Jalankan 01_DISCOVERY_LEVEL_0.md di _meta/
   → Gali: sistem ini tentang apa, siapa yang pakai, apakah berhierarki
     (seperti Brand Core→Channel→dst) atau flat/siklus/struktur lain,
     kira-kira butuh berapa "level"/dokumen, apa yang harus konsisten
     (analog checklist konsistensi di sistem konten kreator, tapi
     mungkin bukan soal visual sama sekali — bisa progress belajar,
     bisa state aplikasi, dst tergantung domain)
   → Output: dokumen rencana kerangka sistem baru ini (BUKAN sistem itu
     sendiri, BUKAN JUGA prompt Discovery detailnya — cuma peta "sistem
     ini akan terdiri dari dokumen apa saja, dengan fungsi apa, dan
     level/urutan apa saja yang perlu digali lebih dalam nanti")

2. BUAT FOLDER sistem-[nama-baru]/, dengan skeleton KOSONG sesuai rencana
   kerangka dari Langkah 1 — bisa 3 file, bisa 15 file, bisa berbeda
   struktur total dari sistem konten kreator

3. UNTUK TIAP DOKUMEN yang direncanakan Langkah 1: TULIS DULU prompt
   Discovery detailnya (dokumen generator, setara 01_BRAND_CORE.md/
   02_CHANNEL_DISCOVERY_PROMPT.md di sistem konten kreator — INI BELUM
   ADA untuk sistem baru manapun, harus ditulis dari nol berdasarkan
   rencana kerangka Langkah 1, sebelum bisa dijalankan). Simpan prompt
   generator ini di dalam folder sistem-[nama-baru]/ itu sendiri (bukan
   di _meta/, karena isinya spesifik ke sistem ini, beda dari
   01_DISCOVERY_LEVEL_0.md yang generik untuk semua sistem)

4. BARU SETELAH prompt generator di Langkah 3 ada: jalankan Discovery
   detailnya (pola sama seperti menjalankan 01_BRAND_CORE/
   02_CHANNEL_DISCOVERY dulu — gali lewat diskusi, checkpoint, baru
   ditulis final)

5. AUDIT MENYELURUH (seperti yang dilakukan untuk sistem konten kreator)
   sebelum dianggap selesai — baca ulang semua dokumen, cross-check
   konsistensi rujukan, verifikasi tidak ada yang hilang/kontradiktif

6. UPDATE INDEKS_SISTEM.md — tambah entri sistem baru ini, tanggal dibuat

7. BUAT RINGKASAN_sistem-[nama-baru].md di _cadangan-claude/ — supaya
   kalau nanti perlu bantuan Claude chat biasa, tidak perlu upload semua
```

**Catatan penting soal Langkah 3:** ini beda dari sistem konten kreator, di mana `01_BRAND_CORE.md` dkk sudah tersedia siap pakai sejak awal (karena kita tahu di depan domainnya konten kreator). Untuk sistem BARU dengan meta-sistem ini, prompt generatornya BELUM ADA — jadi ada 1 langkah tambahan (menulis prompt generator itu sendiri) yang tidak ada di alur sistem konten kreator. Ini konsekuensi wajar dari sifat "general" meta-sistem ini — TIDAK bisa dilewati atau diasumsikan otomatis ada.

## Alur Kerja: Melanjutkan/Mengaudit Sistem Lama

```
1. Entry Point Universal (prinsip dari sistem konten kreator, dipakai
   ulang di sini) jalan seperti biasa

2. TAMBAHAN BARU: agent cek INDEKS_SISTEM.md — kalau sistem yang mau
   disentuh punya tanggal "terakhir disentuh" yang sudah lama, TAWARKAN
   audit dulu sebelum lanjut kerja ("sistem ini terakhir disentuh
   [tanggal], mau saya audit dulu sebelum lanjut, atau langsung saja?")

3. Begitu selesai kerja (apapun jenisnya), UPDATE tanggal di
   INDEKS_SISTEM.md — ini WAJIB, jangan sampai lupa dicatat manual
```

## Alur Kerja: Menggunakan Claude Chat Biasa sebagai Cadangan

```
1. Upload ke sesi Claude: RINGKASAN_sistem-[nama].md (dari
   _cadangan-claude/) + dokumen SPESIFIK yang mau dikerjakan/direvisi
   saat itu (TIDAK perlu semua file sistem itu)

2. Claude baca ringkasan → paham struktur, prinsip, dan KE MANA hasil
   kerja ini akan dibawa (supaya keputusan/asumsi yang diambil sudah
   memperhitungkan itu, bukan mengasumsikan konteks yang salah)

3. Claude kerja seperti biasa (diskusi/audit/revisi)

4. Pengguna paste manual hasil kerja Claude ke lokasi yang sesuai di
   Obsidian (yang otomatis sync ke GitHub via plugin git)

5. Update RINGKASAN_sistem-[nama].md kalau ada perubahan besar pada
   struktur (supaya sesi Claude berikutnya tidak baca ringkasan usang)
```

---

## Keputusan Final untuk 4 Poin (diputuskan langsung oleh Claude, atas permintaan pengguna — 1 September 2026)

### 1. Isi `01_DISCOVERY_LEVEL_0.md` — pertanyaan inti yang harus digali

Pola diskusi bertahap sama seperti Brand Core/Channel Discovery (gali lewat percakapan, checkpoint berkala, tulis final setelah dikonfirmasi). Pertanyaan yang WAJIB dijawab sebelum sistem baru boleh masuk ke tahap perencanaan struktur:

1. **Untuk siapa/apa sistem ini** — siapa/apa yang akan "memakai" hasil sistem ini (pengguna sendiri, audiens publik, atau sistem/proses lain)
2. **Bentuk dasar sistem ini** (paling krusial, menentukan semua keputusan berikutnya):
   - **BERTINGKAT** — ada hierarki turunan, level atas mewarisi ke level bawah (seperti Brand Core → Channel → Model Konten → Produksi)
   - **FLAT** — semua bagian sejajar, tidak ada yang "mewarisi" yang lain
   - **SIKLUS** — berulang dalam 1 alur yang sama tiap kali dipakai (seperti Pipeline Produksi 6 tahap)
   - Boleh gabungan lebih dari satu bentuk di level berbeda (contoh nyata: sistem konten kreator itu BERTINGKAT di level struktural, tapi produksi hariannya SIKLUS)
3. **Apa yang HARUS KONSISTEN di sistem ini** — analog checklist konsistensi visual/non-visual di sistem konten kreator, tapi digeneralisasi ke domain apapun (bisa "gaya penilaian" untuk ruang belajar, bisa "state/skema data" untuk aplikasi, bisa hal lain sama sekali)
4. **Kapan 1 siklus/unit kerja di sistem ini dianggap "selesai" dan perlu dikunci** — dasar untuk menentukan Approval Bertingkat versi sistem ini nanti

Output Discovery Level-0: dokumen rencana kerangka (bukan sistem itu sendiri) — daftar dokumen apa saja yang akan dibangun, dengan fungsi masing-masing, berdasarkan jawaban di atas.

### 2. Isi `02_PRINSIP_UNIVERSAL.md` — mana yang benar-benar lintas-domain

Dipilah dari 5 prinsip inti sistem konten kreator:

| Prinsip | Status | Alasan |
|---|---|---|
| **Prinsip Hierarki** (level atas dikunci dulu, level bawah mewarisi) | ✅ UNIVERSAL, tapi HANYA berlaku kalau Discovery Level-0 sistem itu menjawab bentuknya BERTINGKAT | Konsepnya generik (pewarisan keputusan), tidak spesifik ke konten kreator |
| **Prinsip Rantai/Chaining** (agent baca-tulis sendiri antar tahap, bukan copy-paste manual) | ✅ UNIVERSAL, berlaku ke sistem manapun yang punya bentuk SIKLUS | Ini soal cara kerja agent dengan repo, bukan soal domain |
| **Pemisahan Visual vs Non-Visual** | ❌ SPESIFIK konten kreator, TIDAK universal | Prinsip ini soal jangkar visual vs teks — cuma relevan kalau sistemnya melibatkan elemen visual sama sekali. Sistem lain (misal ruang belajar berbasis teks) tidak butuh ini |
| **Approval Bertingkat** (kategori Besar/Kecil) | ✅ UNIVERSAL | Konsep "sebagian perubahan berisiko tinggi, sebagian rendah" berlaku ke semua sistem, kriteria "Besar vs Kecil"-nya yang beda-beda per sistem |
| **Checkpoint & Verifikasi Konsistensi** | ✅ UNIVERSAL, tapi HANYA relevan kalau sistem itu punya sesi kerja yang bisa panjang/berlapis | Tidak semua sistem akan punya sesi sepanjang produksi konten — kalau sistemnya sederhana, prinsip ini boleh disederhanakan/tidak dipakai |
| **Log Keputusan tetap dipertahankan (tidak digantikan git history)** | ✅ UNIVERSAL | Alasannya (beda level detail antara commit message dan alasan keputusan) berlaku ke semua sistem |

`02_PRINSIP_UNIVERSAL.md` berisi tabel ini plus penjelasan tiap prinsip secara generik (tidak memakai istilah "karakter"/"channel" dari konten kreator) — dan instruksi eksplisit: prinsip ini DEFAULT berlaku, tapi Discovery Level-0 sistem baru BOLEH override kalau memang tidak cocok untuk domain itu, asal dicatat alasannya.

### 3. Format Ringkasan untuk Claude — template baku

```markdown
# Ringkasan Sistem — [Nama Sistem]
### Untuk sesi Claude chat biasa (cadangan lmarena Agent). Dokumen ini
BUKAN sistem itu sendiri — cuma ringkasan supaya Claude paham konteks
tanpa perlu upload semua file.

## Sistem ini tentang apa
[1-2 kalimat]

## Bentuk dasar
[Bertingkat / Flat / Siklus / gabungan — sesuai hasil Discovery Level-0]

## Struktur folder saat ini
[skeleton folder sistem ini, bukan isi lengkap tiap file]

## Prinsip yang berlaku
[rujuk ke _meta/02_PRINSIP_UNIVERSAL.md + sebutkan override spesifik
sistem ini kalau ada]

## Status sekarang
[bagian mana yang sudah selesai, bagian mana yang sedang/belum dikerjakan]

## PENTING — hasil kerja sesi ini akan dibawa ke mana
Hasil dari sesi Claude ini akan di-paste manual oleh pengguna ke lokasi
yang sesuai di Obsidian (sync otomatis ke GitHub). Pastikan format/struktur
yang dihasilkan KOMPATIBEL dengan dokumen sistem yang sudah ada — cek
dulu dokumen terkait yang diupload bersama ringkasan ini sebelum menulis
apa pun.
```

Pengguna update file ini setiap kali ada perubahan STRUKTURAL besar pada sistem terkait (bukan tiap perubahan kecil) — supaya sesi Claude berikutnya tidak baca ringkasan yang sudah usang.

### 4. Pemindahan Sistem Konten Kreator ke struktur baru

**Keputusan: dipindah APA ADANYA, tanpa diubah isinya.** Sistem itu sudah melalui 2 putaran audit menyeluruh dan terbukti solid — mengubah lagi isinya sekarang cuma demi "supaya cocok pola meta-sistem baru" berisiko merusak sesuatu yang sudah teruji tanpa manfaat nyata. Cukup:
1. Pindahkan 11 file yang sudah ada ke folder `sistem-konten-kreator/` di repo baru
2. Buat `RINGKASAN_sistem-konten-kreator.md` di `_cadangan-claude/` (dokumen baru, mengikuti template poin 3 di atas)
3. Tambahkan 1 baris di `INDEKS_SISTEM.md` untuk sistem ini

---

## Log Diskusi & Keputusan

- **1 September 2026:** Ide awal meta-sistem dicetuskan. Diputuskan 5 poin besar (Prinsip Dasar 1-6 di atas) lewat diskusi dan tanya-jawab.
- **1 September 2026 (koreksi penting):** Rancangan awal sempat menyimpulkan "sistem harus dibuat generik supaya gampang dijadikan template nanti" — INI KELIRU, dikoreksi oleh pengguna. Kesimpulan yang benar: isi tetap spesifik/maksimal, kemampuan jadi-template datang dari struktur rapi, bukan dari konten yang digeneralisasi. Ini prinsip inti yang harus dijaga konsisten di seluruh dokumen meta-sistem nanti.
- **1 September 2026 (keputusan final 4 poin terbuka):** Atas permintaan eksplisit pengguna ("aku ga paham, kamu putuskan yang terbaik"), Claude memutuskan semua 4 poin yang tadinya masih terbuka: (1) pertanyaan inti Discovery Level-0, (2) pemilahan prinsip universal vs spesifik konten-kreator, (3) template Ringkasan untuk Claude cadangan, (4) sistem konten kreator dipindah apa adanya tanpa modifikasi. **Kerangka rancangan meta-sistem sekarang LENGKAP, siap dieksekusi jadi file sungguhan** — belum dieksekusi, masih dalam bentuk dokumen rancangan ini.
- **1 September 2026 (koreksi celah sebelum eksekusi):** Sebelum mulai eksekusi, ditemukan 1 celah nyata di "Alur Kerja: Membangun Sistem Baru dari Nol" — draft sebelumnya mengasumsikan prompt Discovery detail (setara `01_BRAND_CORE.md`/`02_CHANNEL_DISCOVERY_PROMPT.md`) sudah otomatis ada untuk sistem baru manapun, padahal itu BELUM ADA dan harus ditulis dari nol berdasarkan hasil Discovery Level-0. Alur diperbaiki dari 6 langkah jadi 7 langkah — ditambahkan langkah eksplisit "tulis dulu prompt Discovery detail" SEBELUM langkah "jalankan Discovery detailnya", dengan lokasi penyimpanan yang jelas (di dalam folder sistem itu sendiri, bukan di `_meta/`, karena isinya spesifik per sistem). Ini konsekuensi wajar dari sifat general meta-sistem — tidak bisa diasumsikan otomatis tersedia seperti di sistem konten kreator yang domainnya sudah diketahui sejak awal.
- **2 September 2026 (EKSEKUSI SELESAI):** Semua file meta-sistem berhasil ditulis: `_meta/00_CARA_KERJA_META.md`, `_meta/01_DISCOVERY_LEVEL_0.md`, `_meta/02_PRINSIP_UNIVERSAL.md`, `_meta/INDEKS_SISTEM.md` — 1 dokumen per giliran, disync ke outputs setiap selesai, sesuai kebiasaan kerja yang sudah terbukti works. Sistem Konten Kreator (11 file) dipindahkan APA ADANYA ke `sistem-konten-kreator/`, diverifikasi identik byte-per-byte dengan versi teraudit sebelum dipindah — tidak ada perubahan isi. `_cadangan-claude/RINGKASAN_sistem-konten-kreator.md` dibuat, statusnya diverifikasi konsisten dengan `INDEKS_SISTEM.md`. Audit cross-reference dilakukan: semua rujukan nama file antar 4 dokumen `_meta/` diverifikasi valid (baik yang mengarah ke file lain di `_meta/`, maupun yang mengarah ke `sistem-konten-kreator/` sebagai contoh). **Meta-sistem sekarang siap dipakai untuk membangun sistem baru pertama.**
- **2 September 2026 (AUDIT MENYELURUH, atas permintaan eksplisit pengguna):** Dilakukan audit penuh dengan metode sama seperti 2 putaran audit Sistem Konten Kreator — cek placeholder, struktur markdown, cross-reference rujukan nama file (diverifikasi eksistensi tiap file yang dirujuk, termasuk membedakan rujukan ke file lain di `_meta/` vs rujukan contoh ke `sistem-konten-kreator/`), baca ulang UTUH kelima file (4 dokumen `_meta/` + 1 ringkasan), dan cross-check skeleton folder yang didokumentasikan vs struktur folder AKTUAL di disk.

  **Ditemukan dan diperbaiki:** 1 inkonsistensi kecil di `01_DISCOVERY_LEVEL_0.md` — 2 baris memakai prefix `_meta/` untuk merujuk file yang sebenarnya ada di folder yang sama (`_meta/`), sementara baris lain di dokumen yang sama tidak memakai prefix untuk rujukan serupa. Bukan bug fatal (agent tetap bisa paham), tapi diperbaiki demi konsistensi maksimal — prefix dihapus di kedua baris.

  **Diverifikasi AMAN (tidak ada masalah lain):** tidak ada placeholder/TODO tersisa; semua heading markdown well-formed; semua rujukan nama file di 5 dokumen (kecuali `00_RENCANA_KERANGKA.md` yang memang belum ada karena belum ada sistem baru yang dibangun — ini wajar, bukan bug) terverifikasi mengarah ke file yang benar-benar ada; skeleton folder di `00_CARA_KERJA_META.md` cocok 100% dengan struktur folder aktual di disk (4 folder: `_meta`, `sistem-konten-kreator`, `_pegangan-kamu`, `_cadangan-claude`); status sistem konten kreator konsisten antara `INDEKS_SISTEM.md` dan `RINGKASAN_sistem-konten-kreator.md`; klaim rujukan silang (misal "skeleton produksi ada di `00_CARA_PAKAI_SISTEM.md` bagian Struktur Repo") diverifikasi benar-benar akurat.

  **Kesimpulan:** meta-sistem sudah diperiksa menyeluruh, 1 masalah kecil ditemukan dan diperbaiki, tidak ada masalah besar. Siap dipakai — dengan catatan (disebutkan sejak awal sebelum audit ini) bahwa audit paling bermakna akan terjadi setelah 1 sistem baru benar-benar dicoba dibangun dengan meta-sistem ini, karena baru di situ akan ketemu masalah nyata dari pemakaian, bukan cuma masalah teoretis dari membaca dokumen.

- **2 September 2026 (celah nyata #1 — pengalaman pemakaian, ditemukan oleh pengguna):** Pengguna menanyakan apakah sistem sudah benar-benar mudah dipakai — bisa cukup 1 prompt siap-pakai di awal sesi, kapan pun (pertama kali atau sudah lama). Dicek: **TIDAK ADA** file berisi prompt universal seperti itu. Audit sebelumnya memeriksa konsistensi ANTAR dokumen yang sudah ada, tapi tidak pernah memeriksa dari sudut pandang "apakah pengalaman pemakaian ujung-ke-ujung semudah yang diminta". Dibuat `PANDUAN_PENGGUNA.md` baru (untuk pengguna, bukan diupload sebagai instruksi agent, sama seperti pola di sistem konten kreator) — isinya 1 prompt universal yang berlaku di SEMUA situasi (baca `00_CARA_KERJA_META.md`, cek status, lalu balik bertanya ke pengguna), plus beberapa jalan pintas opsional untuk situasi spesifik.

- **2 September 2026 (celah nyata #2 — cek PR di level repo, ditemukan oleh pengguna):** Pengguna menanyakan apakah agent otomatis tahu histori/PR/seluruh isi repo yang relevan. Dicek: prompt universal yang BARU dibuat (celah #1) **TIDAK menyebut cek PR menggantung sama sekali** — padahal itu prinsip inti yang terbukti krusial di sistem konten kreator (kasus `resto-pro2`: PR lupa di-merge menyebabkan branch saling menyimpang). Risiko ini LEBIH BESAR di meta-sistem karena 1 repo menampung banyak sistem sekaligus — PR menggantung dari sistem lain bisa terlupakan kalau tidak dicek di level REPO, bukan cuma di level 1 sistem. **Akar masalah:** `00_CARA_KERJA_META.md` sendiri tidak pernah punya bagian "Entry Point tingkat repo" yang eksplisit — cek PR cuma disebut di alur "Melanjutkan Sistem Lama" (level 1 sistem), bukan sebagai langkah wajib universal. Diperbaiki di 2 tempat: (1) `00_CARA_KERJA_META.md` ditambahkan bagian "Kapan Pakai File yang Mana" dengan 2 langkah WAJIB duluan sebelum apapun lain (cek PR menggantung dari sistem manapun + cek `INDEKS_SISTEM.md`), sekaligus ditegaskan JANGAN baca seluruh isi repo di awal — cukup baca yang relevan, baru perdalam sesuai kebutuhan; (2) `PANDUAN_PENGGUNA.md` prompt universal diperbarui mencantumkan langkah cek PR eksplisit. Bagian "Alur Kerja: Melanjutkan/Mengaudit Sistem Lama" disesuaikan catatannya supaya jelas bahwa cek PR sudah terjadi di Entry Point tingkat repo, bukan diulang di situ.

  **Pola yang perlu diwaspadai ke depannya:** kedua celah ini ditemukan justru dari pertanyaan pengguna tentang PEMAKAIAN NYATA (bukan dari audit dokumen oleh Claude sendiri). Audit "konsistensi antar dokumen" TIDAK CUKUP untuk menjamin sistem benar-benar mudah dan aman dipakai — perlu secara eksplisit disimulasikan/dibayangkan dari sudut pandang "kalau saya baru buka sesi sekarang, apa saja yang saya butuh tahu, dan apakah itu semua sudah tercakup". Setiap kali ada file BARU ditambahkan setelah audit selesai (seperti `PANDUAN_PENGGUNA.md` kemarin), file itu WAJIB diaudit ulang — audit sebelumnya tidak otomatis mencakup file yang belum ada saat itu.

- **2 September 2026 (audit putaran ke-3, dengan SIMULASI PEMAKAIAN NYATA, bukan cuma cek konsistensi):** Atas permintaan pengguna untuk audit menyeluruh sekali lagi sebelum download, Claude menjalankan 2 lensa: (1) cek ulang konsistensi dokumen (placeholder, heading, cross-reference) — bersih; (2) **simulasi berperan sebagai agent yang benar-benar menjalankan prompt universal dari `PANDUAN_PENGGUNA.md` langkah demi langkah**, bukan cuma membaca dokumen sepintas. Simulasi ini yang menemukan 2 celah lagi:

  **Celah #3 — Setup repo baru hilang di level meta:** Prinsip penting dari sistem konten kreator (Kategori 0 di audit lama: push commit awal ke `main`, jangan pernah hapus `main`, selalu merge sebelum pakai hasil kerja — pelajaran dari kasus nyata `resto-pro2`) TIDAK PERNAH dipindahkan/disebut ulang di level meta-sistem manapun. Ditemukan lewat simulasi Langkah 2 (cek PR menggantung) — muncul pertanyaan "bagaimana kalau ini benar-benar repo baru yang baru pertama kali diisi", dan jawabannya ternyata tidak terdokumentasikan sama sekali di level meta. Diperbaiki: ditambahkan bagian baru "Setup Repo Baru" di `00_CARA_KERJA_META.md`, merujuk balik ke penjelasan detail/alasan di sistem konten kreator (tidak menulis ulang semuanya, cukup rujuk + ringkas 3 poin inti).

  **Celah #4 — Approval Bertingkat tidak eksplisit di Discovery Level-0:** `01_DISCOVERY_LEVEL_0.md` menyuruh membuat PR dan "direview sebelum merge", tapi tidak pernah eksplisit menyatakan ini KATEGORI BESAR — padahal `00_RENCANA_KERANGKA.md` yang dihasilkan jelas menentukan seluruh struktur sistem baru (setara Channel Brief di sistem konten kreator, yang eksplisit kategori Besar). Prinsip Approval Bertingkat sudah dinyatakan universal di `02_PRINSIP_UNIVERSAL.md`, tapi tidak konsisten diterapkan eksplisit di dokumen yang seharusnya memakainya. Diperbaiki: ditambahkan penegasan eksplisit "INI KATEGORI BESAR" di instruksi akhir `01_DISCOVERY_LEVEL_0.md`.

  Setelah kedua perbaikan disync, dilakukan verifikasi ulang: placeholder bersih, heading bersih, struktur folder aktual masih cocok skeleton, dokumen navigasi sistem konten kreator (`START_DI_SINI.md`) terverifikasi ada dan sesuai klaim di `RINGKASAN`, klaim rujukan silang (`00_CARA_PAKAI_SISTEM.md` bagian Struktur Repo) diverifikasi ulang masih akurat.

  **Kesimpulan audit putaran ke-3:** metode simulasi pemakaian nyata (bukan cuma baca sepintas) terbukti jauh lebih efektif menemukan celah dibanding audit konsistensi dokumen semata — 2 dari 2 celah kali ini ditemukan lewat cara itu. Setelah perbaikan ini, tidak ditemukan celah baru di verifikasi ulang. Status: **siap didownload**, dengan pengingat yang sama seperti sebelumnya — pengujian paling bermakna tetap akan terjadi saat benar-benar dipakai membangun sistem baru pertama kali.
