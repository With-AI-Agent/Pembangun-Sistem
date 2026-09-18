# Cara Kerja Meta-Sistem

### Ini repo tunggal yang menampung BANYAK sistem berbeda — bukan cuma 1 sistem untuk 1 domain, tapi tempat membangun sistem APAPUN (konten kreator, ruang belajar, fondasi aplikasi, atau domain lain). File ini adalah peta besar: baca ini dulu sebelum menyentuh sistem manapun di repo ini.

---

## Kenapa repo ini ada

Setelah 1 sistem berhasil dibangun dan teruji (Sistem Konten Kreator — lihat `sistem-konten-kreator/`), muncul kebutuhan yang lebih besar: kemampuan membangun sistem SEJENIS untuk domain apapun, tanpa merancang ulang dari nol setiap kali, sambil tetap menjaga kualitas maksimal untuk tiap sistem yang dibangun (bukan dikompromikan demi keseragaman).

**Prinsip inti yang membedakan meta-sistem ini dari sekadar "kumpulan template":**

> **Isi/konten tiap sistem = SPESIFIK dan maksimal untuk kebutuhan itu saja.** Sistem TIDAK dibuat generik/abstrak dengan alasan "supaya gampang dijadikan template nanti". Kemampuan untuk dijadikan template atau diduplikasi adalah **efek samping dari struktur yang rapi**, bukan tujuan aktif yang dikejar saat membangun. Struktur/organisasi file yang konsisten rapi berlaku di semua sistem — itu yang membuat duplikasi/jadi-template bisa dilakukan kapan saja (baik direncanakan dari awal maupun muncul tiba-tiba bertahun-tahun kemudian) tanpa persiapan khusus di muka.

> **Setiap sistem dibangun SELF-CONTAINED karena akan dipisahkan.** (Prinsip tambahan, dinyatakan pengguna 5 Sep 2026.) Alur pakai nyata: setelah sebuah sistem jadi, pengguna **mengunduh folder sistem itu dan menjadikannya repo tersendiri yang hanya berisi sistem tersebut**, dipakai terpisah dari meta-sistem ini. Konsekuensi wajib saat membangun:
> - Semua yang dibutuhkan sistem saat dipakai (dokumen instruksi, aturan desain/isi, skrip build, template, aset) harus berada **di dalam folder sistem itu sendiri**, tidak bergantung pada file di `_meta/` saat runtime.
> - Rujukan ke `_meta/` boleh ada sebagai *provenance* (asal prinsip), tapi aturan yang benar-benar dipakai harus **disalin/diturunkan ke dalam folder sistem**, supaya hasil ekstraksi tetap berfungsi penuh.
> - Sejak 8 Sep 2026, **folder sistem itu sendiri adalah deliverable**: tidak ada ZIP/dist, tidak ada pemilahan file oleh pemilik, dan tidak ada rujukan `sistem-<nama>/...` ke dirinya sendiri. Rujukan ber-backtick ke `_meta/...` atau `tools/...` berarti salinan berlabelnya wajib ada di dalam folder sistem; provenance disebut tanpa backtick.
> - Exit 0 `python3 tools/check_selfcontained.py --sistem <nama> --report` adalah definisi mekanis bahwa folder sistem sudah mandiri.
> - Ini TIDAK bertentangan dengan prinsip di atas: isi tetap spesifik-maksimal; self-containment hanyalah memastikan hasil yang spesifik itu bisa dibawa keluar tanpa rusak.
> - **BUTIR 9 Sep 2026 (penunjuk, bukan ringkasan baru).** Butir-butir di atas adalah snapshot keputusan 8 Sep 2026 dan sengaja dibiarkan apa adanya. Norma yang hidup beserta cakupan penegakannya ada di `_meta/PAKET_REPO_MANDIRI.md` v2.1 — baca itu kalau ada yang perlu diputuskan: yang dinilai alat hanyalah **dokumen aktif** (dokumen bukti dan dokumen mentah tidak ditegakkan; rujukannya tetap dicetak alat sebagai rujukan historis), penyebutan area berbentuk direktori bukan janji bahwa satu berkas ikut, dan area yang tidak boleh keluar dari master (mis. `_meta/_internal/`) disebut sebagai provenance tanpa backtick, bukan disalin. Kalau suatu saat kalimat di blok ini berbeda dengan protokol itu, protokol yang menang dan perbedaan itu dilaporkan.

> **Setiap sistem wajib menyertakan PEGANGAN PENGGUNA (buku pedoman) di dalam foldernya.** (Prinsip tambahan, dinyatakan pengguna 5 Sep 2026.) Standar mudahnya: **sama dengan meta-sistem ini sendiri** — pengguna cukup membuka sesi dengan **SATU prompt pembuka universal** yang sudah disiapkan, lalu agent otomatis terorientasi penuh (apa sistemnya, cara kerja, ketentuan, kondisi repo, PR menggantung) tanpa perlu ditempel manual. Bentuknya dua file di dalam folder sistem: `PROMPT_ENTRI_UNIVERSAL.md` (satu blok prompt pembuka siap tempel) + `PANDUAN_PENGGUNA.md` (pedoman lengkap: prompt pembuka + **prompt penutup sesi**, istilah awam, kalimat per situasi, cara review & merge, kebiasaan). Ikuti struktur `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`. Preceden: meta-sistem sendiri (`PANDUAN_PENGGUNA.md` di root repo) dan `sistem-konten-kreator/` (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md`).

> **Pegangan pengguna + self-containment + checkpoint + log sesi diringkas menjadi KONTRAK WARISAN** (`03_KONTRAK_WARISAN.md`, 5 Sep 2026 — permintaan pengguna pasca audit menyeluruh). Semua butir yang wajib tertanam di SETIAP sistem (W-01…W-09) ada di satu daftar induk: **default aktif** — agent membangun menerapkan dan MELAPORKAN seluruhnya tanpa perlu diminta maupun menawarkan satu-satu; yang butuh keputusan pengguna hanyalah **penonaktifan** (override), yang wajib tercatat dengan alasan + approval. Butir yang bisa dicek mekanis ditegakkan `tools/validate_repo.py` untuk semua sistem terdaftar di `INDEKS_SISTEM.md` — termasuk yang belum lahir.

---

## Struktur Repo

```
repo-utama/
├── PANDUAN_PENGGUNA.md               ← pegangan pengguna meta-sistem (prompt
│                                        pembuka + penutup; standar utk semua sistem)
├── PROMPT_ENTRI_UNIVERSAL.md         ← blok prompt pembuka siap tempel (identik
│                                        dgn §1 PANDUAN — aturan 2-file berlaku
│                                        utk meta sendiri, M-15 audit 5 Sep)
│
├── _meta/
│   ├── SYSTEM_MANIFEST.md            ← manifest meta-sistem ini
│   ├── 00_CARA_KERJA_META.md         ← file ini
│   ├── 01_DISCOVERY_LEVEL_0.md       ← gali "sistem apa ini, struktur macam apa"
│   ├── 02_PRINSIP_UNIVERSAL.md       ← prinsip default untuk semua sistem
│   ├── 03_KONTRAK_WARISAN.md         ← butir WAJIB yang otomatis tertanam di
│   │                                    SEMUA sistem (dibangun oleh meta) — lihat
│   │                                    bagian "Kontrak Warisan" di file ini
│   ├── INDEKS_SISTEM.md              ← daftar semua sistem + status
│   ├── SYSTEM_MANIFEST_TEMPLATE.md   ← kontrak identitas tiap sistem
│   ├── PANDUAN_PENGGUNA_TEMPLATE.md  ← template pegangan pengguna tiap sistem
│   ├── TEMPLATE_LOG_SESI.md          ← format LOG_SESI (diturunkan ke sistem)
│   ├── TEMPLATE_RELEASE.md           ← definisi template bersih + cara build/verif
│   ├── NEXT_SESSION_PROMPT.md        ← prompt bootstrap sesi lanjutan
│   ├── DEFINITION_OF_DONE.md         ← kriteria selesai dan rilis
│   ├── PROTOKOL_CHECKPOINT_RECOVERY.md ← status persisten dan pemulihan
│   ├── PLATFORM_LMARENA.md           ← fakta platform vs policy (wajib baca)
│   ├── QUALITY_ASSURANCE_AND_EVOLUTION.md ← audit, upgrade, dan rollback tiga lapisan
│   ├── ACCEPTANCE_TESTS.md            ← skenario uji perilaku meta-sistem
│   ├── SESSION_REPORT_TEMPLATE.md     ← format laporan awal setiap sesi
│   ├── FAILURE_INJECTION_TESTS.md     ← uji jalur gagal dan state abnormal
│   └── _internal/                     ← audit & handoff HISTORIS (referensi,
│                                        bukan instruksi aktif; tdk ikut template)
│
├── tools/                            ← regression check struktural (stdlib-only):
│   ├── validate_repo.py              ← PASS wajib 0-warning; menegakkan kontrak
│   │                                    warisan generik utk tiap sistem di INDEKS
│   ├── test_failure_injection.py     ← cek fail-closed checkpoint
│   ├── backup_verify.py              ← backup esensial + uji restore byte-per-byte
│   ├── build_template.py             ← template bersih + guard kelengkapan
│   └── check_selfcontained.py        ← gerbang folder sistem = deliverable
│
├── sistem/
│   ├── sistem-[nama-1]/                  ← misal sistem-konten-kreator/
│   └── (struktur & jumlah file BEDA-BEDA per sistem, ditentukan hasil
│        Discovery, TIDAK dipaksa sama seperti sistem lain — TAPI butir
│        03_KONTRAK_WARISAN wajib tertanam, override hanya via approval)
│
│   └── sistem-[nama-2]/                  ← sistem lain, struktur sendiri
│
├── _log-sesi/                        ← semua LOG_SESI_*.md level repo/meta
│                                        (sesi lintas-sistem — bukan di root langsung)
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

## Batasan Platform lmarena (wajib paham, bukan aturan kita)

Platform lmarena Agent Mode memiliki perilaku otomatis yang mempengaruhi semua kerja di repo ini. Ini **fakta platform** (tidak bisa / otomatis), bukan policy yang bisa di-override. Detail lengkap ada di `PLATFORM_LMARENA.md` — baca itu.

Ringkasnya:

1. **Branch kerja otomatis:** Saat sesi dimulai, kamu boleh pilih base branch (misal `main`) di UI, tapi setelah itu lmarena **otomatis** membuat branch baru `arena/[id]-...` dan semua kerja agent terjadi di situ. `main` hanya berubah setelah PR di-merge. Karena itu branch aktif yang harus diverifikasi adalah `arena/...`, bukan asumsi `main`.

2. **Kehilangan akses push setelah merge/close:** Setelah PR di-merge atau di-close, platform mencabut token push untuk sesi tersebut. Sesi tersebut **tidak bisa** push lagi secara teknis — bukan "sebaiknya jangan". File yang dibuat setelah merge akan terjebak di sesi dan tidak bisa dibawa ke sesi baru (workaround resmi: tambah `/download-workspace` di akhir URL sesi untuk download zip).

3. **Sesi bisa crash di tengah jalan:** Chat tidak bisa lanjut, error halaman keluar sendiri. Arena sendiri mengakui dan sediakan workaround download. Karena itu diskusi panjang yang belum jadi file + commit bisa hilang.

**Implikasi untuk sistem:** Karena fakta #2 dan #3, maka policy "commit tiap tahap besar selesai" dan **log sesi berkelanjutan (`LOG_SESI`)** bukan birokrasi, tapi syarat fisik supaya sesi baru **bisa** melanjutkan (mencegah FI-03). Lihat `PLATFORM_LMARENA.md` bagian Policy (P2) dan `PROTOKOL_CHECKPOINT_RECOVERY.md` bagian "Log Sesi Berkelanjutan" untuk alasan kausal lengkap.

---

## Setup Repo Baru (SEKALI di awal, sebelum sesi agent pertama)

Berlaku sama seperti yang sudah terbukti penting di Sistem Konten Kreator: GitHub otomatis membuat branch `main` begitu repo baru dibuat — ini sudah otomatis, TIDAK perlu diusahakan manual. Yang WAJIB dilakukan secara sadar:

1. Setelah repo dibuat di GitHub, push semua isi meta-sistem ini (folder `_meta/`, `sistem-konten-kreator/`, `_cadangan-claude/`, `PANDUAN_PENGGUNA.md`) LANGSUNG ke `main` — baik lewat push manual, atau sesi agent pertama diarahkan eksplisit bekerja dari `main` yang sudah terisi.
2. **Jangan pernah hapus branch `main`** selama repo ini aktif dipakai — kalaupun ada kebutuhan restrukturisasi besar, itu keputusan sadar yang dicatat, bukan tindakan spontan.
3. Sebelum deploy/pakai hasil kerja apapun, selalu **merge dulu** PR yang relevan ke `main` — jangan asumsikan hasil kerja di suatu branch otomatis "sudah jadi" sebelum di-merge.

*(Alasan detail di balik 3 poin ini — termasuk kasus nyata yang jadi pelajaran (repo tes `resto-pro2`) — ada di `sistem/sistem-konten-kreator/_sistem/09_AUDIT_MIGRASI_GITHUB_AGENT.md` bagian "KATEGORI 0 — Langkah Persiapan Repo", dan konteks pemakaian sehari-harinya di `sistem/sistem-konten-kreator/_sistem/00_CARA_PAKAI_SISTEM.md`. Prinsipnya sama persis, cuma sekarang berlaku untuk SELURUH repo meta-sistem, bukan cuma 1 sistem.)*

---

## Kapan Pakai File yang Mana

**APAPUN tujuan sesi ini, WAJIB dilakukan dulu di awal (Entry Point tingkat repo):**
1. Buat laporan awal mengikuti `SESSION_REPORT_TEMPLATE.md`; verifikasi repo, branch, working tree, commit, dan PR.
2. Cek apakah ada PR yang masih terbuka/menggantung di repo ini — dari SISTEM MANAPUN, bukan cuma sistem yang mau dikerjakan sekarang. Karena repo ini menampung banyak sistem sekaligus, PR menggantung dari sistem lain bisa gampang terlupakan kalau tidak dicek di level repo, bukan cuma di level 1 sistem. Gunakan `gh pr list --state all --limit 20` — PR branch aktif yang sudah MERGED/CLOSED wajib terlihat supaya fakta platform #2 terdeteksi (lihat `PLATFORM_LMARENA.md` P3–P4).
3. Cek `INDEKS_SISTEM.md` untuk tahu sistem apa saja yang ada dan statusnya.
4. Cari `LOG_SESI_*.md` **terbaru** (folder `_log-sesi/` / folder sistem / folder unit kerja). Kalau yang terbaru berkeadaan `OPEN` → baca, laporkan keadaannya, dan konfirmasi ke pengguna sebelum lanjut — itu konteks yang tidak boleh ditanya ulang. (Langkah ini dulu hanya ada di dokumen lain; diselaraskan ke sini 5 Sep 2026, temuan M-05.)

Regresi struktural tersedia sebagai alat — jalankan saat menyentuh `_meta/`/`tools/` atau menyelesaikan audit: `python3 tools/validate_repo.py` (harus PASS 0 warning), `tools/test_failure_injection.py`, `tools/backup_verify.py`, `tools/build_template.py`, dan `tools/check_selfcontained.py --semua --report` untuk status deliverable folder sistem; `tools/checkpoint_core.py` adalah parser bersama yang diimpor validator & FI (tidak dijalankan langsung) (temuan M-07: blok struktur dulu tidak menyebut `tools/`).

Baru setelah itu, arahkan sesuai tujuan. Jika state tidak konsisten, gunakan `FAILURE_INJECTION_TESTS.md` sebagai aturan berhenti dan recovery:

**Mau bangun sistem BARU dari nol** → mulai dari `01_DISCOVERY_LEVEL_0.md`, ikuti alur di bagian "Alur Kerja: Membangun Sistem Baru dari Nol" di bawah.

**Mau lanjut/audit sistem yang SUDAH ADA** → dari `INDEKS_SISTEM.md` yang sudah dicek di atas, masuk ke folder `sistem/sistem-[nama]/` itu dan baca dokumen navigasi di dalamnya (analog `START_DI_SINI.md` di sistem konten kreator — tiap sistem punya dokumen serupa, isinya spesifik ke sistem itu). **JANGAN baca seluruh isi repo di awal** — cukup baca yang relevan dengan sistem yang dituju, baru baca lebih dalam sesuai kebutuhan aktual.

**Mau merawat sistem yang TINGGAL di repo ini (rawat inap via Sistem Klinik)** → entry point: jenis sesi 3 di berkas START_DI_SINI.md folder sistem klinik (foldernya tercatat di `INDEKS_SISTEM.md`; keputusan K-11, 14 Sep UTC/15 Sep WIB): alur standar meta (branch → PR → merge) dijalankan dengan aturan klinik (katalog cacat, dua gerbang, REKAM-KLINIK, cap versi); master aturan klinik dibaca in-place — kit hanya untuk suntik ke repo eksternal; sistem target TETAP di repo sebagai warga kelas satu, penghapusannya = keputusan sadar pemilik.

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

   **WAJIB-BERTAJUK (tawaran kapabilitas):** setelah Discovery, agent
   MENAWARKAN riset kapabilitas (plugin/skill/library) yang mungkin
   dibutuhkan sistem ini — tawaran, BOLEH DITOLAK; penolakan dicatat di
   Log Keputusan supaya tidak ditawari ulang tanpa alasan baru. Mekanisme
   lengkapnya: sistem/sistem-klinik/_sistem/05_TAWARAN_KAPABILITAS.md
   (satu-satunya sumber; meta tidak menyimpan salinan kedua — norma
   anti-dokumen-kembar). Ditulis tanpa backtick karena berkas itu tidak
   ikut dalam ekstrak template bersih (penjaga pin R7 di
   tools/test_failure_injection.py).

2. BUAT folder `sistem/sistem-[nama-baru]/` dan salin `SYSTEM_MANIFEST_TEMPLATE.md`
   menjadi manifest sistem tersebut (PR yang sama dengan rencana kerangka —
   manifest menyusul SETELAH merge adalah temuan M-14). Buat skeleton kosong
   sesuai rencana kerangka dari Langkah 1. Pastikan bagian **"Warisan"** pada
   rencana kerangka sudah memuat status tiap butir `03_KONTRAK_WARISAN.md`
   (diterapkan / override + approval) — defaultnya TERPASANG SEMUA, tanpa
   menawarkan butir satu-satu ke pengguna.

3. UNTUK TIAP DOKUMEN yang direncanakan: TULIS DULU prompt Discovery
   detailnya (dokumen generator, setara 01_BRAND_CORE.md/
   02_CHANNEL_DISCOVERY_PROMPT.md di sistem konten kreator — ini BELUM
   ADA untuk sistem baru manapun, harus ditulis dari nol berdasarkan
   rencana kerangka Langkah 1). Simpan di dalam folder sistem/sistem-[nama-baru]/
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

8. BUAT PEGANGAN PENGGUNA: `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` di dalam
   folder sistem (ikuti `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`) — WAJIB: prompt pembuka
   universal (satu prompt → agent langsung terorientasi) + prompt penutup sesi.
   Tanpa pegangan, sistem belum dianggap siap dipakai (lihat DEFINITION_OF_DONE.md).
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

2. Masuk ke folder sistem/sistem-[nama]/, baca dokumen navigasinya (analog
   START_DI_SINI.md), lanjutkan kerja sesuai kebutuhan.
   **WAJIB-BERTAJUK (tawaran kapabilitas):** di titik ini agent juga
   MENAWARKAN riset kapabilitas (plugin/skill/library) yang relevan —
   tawaran, BOLEH DITOLAK; penolakan dicatat di Log Keputusan supaya tidak
   ditawari ulang tanpa alasan baru (mekanisme: sistem/sistem-klinik/_sistem/05_TAWARAN_KAPABILITAS.md).

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

Status “selesai” tidak berarti file sudah ditulis. Status tersebut baru boleh digunakan setelah acceptance checklist terpenuhi, dependency diverifikasi, approval selesai, dan perubahan tersedia di branch/PR yang benar. Untuk klaim folder sistem mandiri, definisi mekanisnya adalah exit 0 `python3 tools/check_selfcontained.py --sistem <nama> --report`.

Dokumen audit dan draft di `_meta/_internal/` adalah referensi master, bukan instruksi kerja yang harus diikuti pada setiap sesi. Jika instruksi aktif bertentangan dengan catatan sejarah, instruksi aktif dan keputusan terbaru yang sudah disetujui menjadi acuan; konflik tetap harus dilaporkan, bukan ditebak.

## Prinsip yang Berlaku di Semua Sistem

Lihat `02_PRINSIP_UNIVERSAL.md` untuk daftar lengkap + penjelasan. Ringkasnya: Hierarki (kalau relevan), Rantai/Chaining, Approval Bertingkat, Checkpoint & Verifikasi Konsistensi (kalau relevan), Log Keputusan, serta Quality Assurance & Evolusi tetap dipertahankan. Semua ini DEFAULT berlaku, tapi tiap sistem boleh override kalau memang tidak cocok untuk domainnya — asal dicatat alasannya di dokumen sistem itu.

---

## Kebiasaan Umum yang Perlu Dijaga (dipakai ulang dari Sistem Konten Kreator, terbukti works)

- **Branch & merge**: tiap sesi kerja dapat branch sendiri (`arena/...` dibuat otomatis oleh platform, bukan manual), tidak pernah auto-merge, review sesuai Approval Bertingkat sebelum merge ke `main`. **Alasan kausal:** Setelah PR di-merge/close, sesi tersebut **tidak bisa** push lagi (platform cabut akses — lihat `PLATFORM_LMARENA.md`). Karena itu pastikan semua sudah push sebelum merge, dan buka sesi baru dari `main` untuk kerja lanjutan. Jangan lanjut kerja di sesi yang PR-nya sudah merge — file baru akan terjebak.
- **Entry Point**: di awal sesi baru, cek dulu status kerja yang menggantung, tanya tujuan sesi ini, baca file relevan sendiri — tidak perlu ditempel manual. Verifikasi branch aktif via `git branch --show-current` karena branch `arena/...` dibuat otomatis (fakta platform).
- **Log sesi berkelanjutan (`LOG_SESI`)**: Setiap sesi memelihara `LOG_SESI_YYYY-MM-DD.md` di folder scope kerja (unit/sistem, atau folder `_log-sesi/` untuk level repo/meta) — append + commit + push segera setelah tiap pertukaran yang menghasilkan informasi baru. Header "Keadaan Sesi" (di mana kita, apa yang disepakati, apa yang terbuka) selalu segar. **Yang dicatat:** keputusan/koreksi/kendala/preferensi pengguna (near-verbatim), proposal penting + dasarnya, kesepakatan & penolakan + alasan, fakta terverifikasi, state kerja, pertanyaan terbuka. **Yang TIDAK dicatat:** konfirmasi, basa-basi, ulang isi STATUS.md/Log, dump chat. **Alasan kausal:** Sesi bisa crash kapan saja (fakta platform #3) dan agent sesi baru tidak punya akses ke chat lama — ingatan yang bertahan hanya file. Mekanisme lama "checkpoint kalau >5 giliran" diganti karena berbasis ambang+judgment: sebelum ambang, tidak ada yang tercatat. Detail: `PROTOKOL_CHECKPOINT_RECOVERY.md` + format `TEMPLATE_LOG_SESI.md`.
- **1 dokumen direvisi/dibangun penuh dulu, baru lanjut ke dokumen berikutnya** — bukan banyak sekaligus, supaya kesalahan kecil tidak menyebar sebelum ketahuan
- **Checklist penutupan sesi:** PR dibuka → `tools/review_prompt.py --pr <N>` dijalankan dan keluarannya ditempel sebagai SATU BLOK BERPAGAR di badan pesan chat terakhir sesi (bukan keluaran perintah yang terlipat). Jika blok itu tidak ada di badan pesan, penutupan BELUM dikerjakan dan PR belum boleh dinilai; pemilik dapat membuka sesi baru dari main lalu menjalankan `python3 tools/review_prompt.py --pr <N>` sendiri (aturan lengkap: `PROTOKOL_REVIEW_INDEPENDEN.md` §"Sumber prompt"). **Penyerahannya wajib menyebut path absolut berkas + link-nya** (link PR, permalink head yang di-pin, daftar berkas yang berubah) — `tools/review_prompt.py` mencetak **BLOK SERAH TERIMA** itu sendiri ke ujung prompt dan ke stderr; agent tidak boleh menulis link dari ingatan (`PROTOKOL_REVIEW_INDEPENDEN.md` aturan 11, aturan tetap pemilik 18 Sep 2026). **Dan link yang dimaksud pemilik adalah link ke BERKAS PROMPT ITU SENDIRI, bukan hanya link ke PR** (penegasan giliran 20): tambahkan `--umumkan` supaya prompt ditempel ke kanal PR sebagai komentar penulis — bukan verdict, teruji lintas alat di regresi RP13 — lalu permalink-nya ikut tercetak di blok serah terima dan bisa dibuka siapa pun yang akan menjalankan sesi hakim (`python3 tools/review_prompt.py --pr <N> --out <path> --umumkan`)


### Bukti numerik permanen (C5)

Angka dalam Log Evolusi, manifest, atau indeks harus tetap benar setelah dokumen ditulis. Jumlah `rujukan` tidak stabil—entri `LOG_SESI` baru dapat mengubahnya—maka dilarang dikutip sama sekali. Verdict dan angka stabil (contoh: jumlah berkas wajib) tetap dikutip. Validator menegakkan aturan ini pada sel **Bukti** Log Evolusi; lihat AT-16. Empat siklus PR #21→#24 membuktikan bahwa mengejar angka bukti basi adalah masalah integritas, bukan gaya.
