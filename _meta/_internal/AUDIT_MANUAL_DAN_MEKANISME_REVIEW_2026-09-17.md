# Audit Manual Pengguna & Mekanisme Review — 2026-09-17

**Sifat:** TAHAP 1 — **audit + lapor. TIDAK ADA perbaikan yang dieksekusi di laporan ini.**
**Mandat:** pemilik, giliran 5–6 sesi `arena/01a0ae7a-pembangun-sistem`. Pilihan pemilik eksplisit:
*"Audit dulu semua manual, laporkan, baru putuskan perbaikannya"* — dan perluasan mandat:
*"aku mau ini juga diterapkan pada meta sistem pembangun sistem ini dan kemudian dapat diwariskan ke
sistem-sistem yang dibangun oleh nya, baik yang udh dibangun maupun yang akan."*
**Standar yang dipakai:** 4 syarat kelulusan T26 (dirumuskan sesi ini) + 7 bagian wajib
`_meta/PANDUAN_PENGGUNA_TEMPLATE.md` + butir W-01/W-07 `_meta/03_KONTRAK_WARISAN.md` + lensa #5
`_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` (kemudahan pakai, kacamata awam).
**Aturan yang mengikat laporan ini:** **ATURAN CAKUPAN** (L.3 berkas DISKUSI_MENTAH sesi ini) —
*cakupan membatasi rencana pencarian dan klaim, tidak pernah membatasi laporan.* Karena itu bagian 4
memuat temuan **di luar cakupan** yang tetap wajib dilaporkan.

---

## 1. Metode — supaya bisa diulang, bukan dipercaya

Objek: **12 berkas manual** (±1.300 baris) di root + 4 sistem terdaftar + template meta.

| Langkah | Cara | Kenapa |
|---|---|---|
| 1 | **Pemindaian mekanis 3 lapis** (skrip di `/tmp/audit-manual/pindai{,2,3}.py`, read-only) — v1: penanda wajib + 7 seksi + arah bicara + kolom tabel; v2: tabel kembar + portabilitas prompt + seksi yang cuma rujukan silang; v3: residu chat | Biar ada bukti objektif bernomor baris, bukan kesan |
| 2 | **Verifikasi adversarial** — **setiap** kandidat dibaca di sumbernya, dinilai konteksnya, lalu diputuskan *nyata* / *positif palsu* | Riset yang jadi dasar desain ini: analisis statis mentah menghasilkan **>90% positif palsu**; verifikasi adversarial memangkasnya drastis. Melaporkan kandidat mentah = **cry-wolf** |
| 3 | **Klasifikasi** memakai skema repo sendiri: `B` bug / `A` ambiguitas / `G` gap proses / `N` kebutuhan baru / `P` preferensi, + prioritas `P1–P3`, + dasar bukti | Wajib per `QUALITY_ASSURANCE_AND_EVOLUTION.md` |
| 4 | **Positif palsu dicabut secara terbuka** di bagian 5, bukan dibuang diam-diam | Prinsip #8 append-only: *jangan menghaluskan*. Pemilik berhak tahu rasio sinyal:derau audit ini |

**Hasil pemindaian (dihitung ulang, bukan diperkirakan):** v1 = 21 kandidat, v2 = 8, v3 = 14 →
**43 kandidat mentah** (sebagian adalah pemicu berganda pada baris yang sama). Setelah verifikasi adversarial:
**8 temuan nyata dalam cakupan** (bagian 2) + **6 temuan di luar cakupan** (bagian 4, dari pembacaan dokumen —
bukan dari pemindai) → **28 kandidat DICABUT sebagai positif palsu** (daftar lengkap bagian 5).
**28 dari 43 = ~65% kandidat pemindai adalah positif palsu.** Angka ini dilaporkan apa adanya dan **menjadi
temuan sendiri** (F-08): pemindai mekanis **tidak layak** dipakai sebagai pemberi putusan, hanya sebagai
**penjaring kandidat**.

---

## 2. TEMUAN DALAM CAKUPAN — manual pengguna

### F-01 · `B` · **P1** · Tabel kembar yang **sudah menyimpang** — `sistem-klinik`

**Lokasi:** `sistem/sistem-klinik/PANDUAN_PENGGUNA.md` baris **53** (§4) dan baris **77** (§7).
**Bukti:** dua tabel berheader identik `| Situasi | Yang terjadi |`. Tabel §4 punya **7 baris**, tabel §7 punya
**6 baris**. **6 baris sama; 1 baris hanya ada di §4** — baris *"Agent butuh keputusan kamu (banyak persetujuan
per-item) → TANYANYA DIBORONG, bukan dicicil (K-10)"*. **Aturan K-10 hilang dari salinan §7.**
**Kenapa P1:** ini bukan kosmetik. Template sudah memperingatkan pola ini persis:
*"selisih diam-diam pernah terjadi dan jadi temuan audit — cek diff keduanya setiap kali mengubah salah satu"*
(preseden **M-15**). Bedanya: M-15 soal 2 **berkas**; ini **2 tabel dalam 1 berkas yang sama**, dan **sudah
terjadi**. Satu sumber disalin dua kali → menyimpang → pembaca yang kebetulan baca §7 **tidak pernah tahu
aturan K-10 ada**.
**Akar masalah (penting untuk Tahap 2):** template memerintahkan *"cek diff keduanya"* — yaitu **pemeriksaan
manual yang bergantung ingatan**. `03_KONTRAK_WARISAN.md` kolom verifikasi W-01 menulis
*"validator: keberadaan kedua file; **audit: diff blok prompt**"* — artinya **bagian diff-nya BELUM mekanis**.
F-01 adalah **bukti lapangan bahwa yang belum mekanis itu memang bocor**.

### F-02 · `B` · **P2** · Prompt penutup **tidak portabel** — `sistem-klinik`

**Lokasi:** langkah 3 prompt penutup, muncul di **2 berkas sekaligus** (salinan identik):
`sistem/sistem-klinik/PANDUAN_PENGGUNA.md` §3 dan `sistem/sistem-klinik/PROMPT_ENTRI_UNIVERSAL.md`.
**Bukti:** *"Perbarui tanggal 'terakhir disentuh' dan status sistem ini di **`_meta/INDEKS_SISTEM.md`**"*.
Prompt pembuka juga menyebut *"`00_CARA_KERJA_META.md` di folder `_meta`"*.
**Kenapa cacat:** template catatan-kualitas mewajibkan *"Prompt pembuka/penutup harus **portabel**: memakai path
relatif folder sistem, **tidak menggandeng path repo meta** — supaya tetap benar saat sistem berdiri sebagai repo
standalone."* Sistem Klinik justru **dirancang untuk disuntikkan ke repo eksternal** (mode rawat jalan:
*"kamu salin folder `kit/` dari sini ke repo target"*) — jadi di repo target **tidak ada folder `_meta/`** dan
langkah 3 **putus**. Ini dilaporkan sebagai **1 cacat di 2 lokasi**, bukan 2 cacat.

### F-03 · `A` · **P2** · Seksi yang isinya **hanya rujukan silang** — `sistem-klinik` §6

**Lokasi:** `sistem/sistem-klinik/PANDUAN_PENGGUNA.md` baris 71, §*"6. Cara review & merge"*.
**Bukti (kutipan lengkap, isinya memang hanya ini):** *"Sama seperti repo induk: buka PR → review isi (kamu
pemilik keputusan) → merge sendiri → sesi lama tidak bisa push lagi setelah itu (fakta platform — buka sesi baru
dari main untuk lanjut). Jangan minta agent auto-merge."*
**Kenapa cacat (lensa #5):** judulnya menjanjikan **cara**, isinya menyuruh pembaca **pergi ke dokumen lain**.
Tidak ada langkah bernomor; tidak ada *"kalau review menemukan masalah, apa yang kulakukan"*; tidak ada
*"kalau merge konflik"*. **Bukti pembanding internal:** `sistem-presentasi` §"Cara Review & Merge" membahas
topik yang sama dengan **5 langkah bernomor**, termasuk peringatan pasca-merge **dan** jalur unduh berkas di
lmarena. Jadi standar yang lebih baik **sudah ada di repo ini** — F-03 bukan keterbatasan yang tak terelakkan.

### F-04 · `A` · **P2** · Langkah yang mengandaikan pengalaman — `sistem-konten-kreator`

**Lokasi:** `sistem/sistem-konten-kreator/panduan/PANDUAN_PENGGUNA.md` baris 98,
§*"Langkah 2 — Hubungkan lmarena Agent ke Repo"*.
**Bukti:** isinya *"Ikuti cara lmarena menghubungkan ke repo GitHub (**sesuai yang sudah pernah kamu lakukan
sebelumnya**)."*
**Kenapa cacat:** ini **langkah bernomor 2** dalam alur mulai pakai. Bagi pengguna yang **sudah pernah**,
kalimatnya berguna. Bagi pengguna **baru** — yaitu target standar kelulusan T26, *"bisa dipakai orang awam tanpa
bertanya lagi"* — kalimat ini **nol informasi** dan memaksa bertanya. Judul berjanji "cara menghubungkan",
isi mengandaikan sudah bisa.

### F-05 · `A` · **P2** · **Residu chat** jadi isi dokumen — `sistem-building-aplikasi`

**Lokasi:** `sistem/sistem-building-aplikasi/PANDUAN_PENGGUNA.md` baris **154** dan **167**.
**Bukti (kutipan apa adanya):**
> baris 154: `> **Aku jujur:** ide kamu ini **sangat penting dan benar**. Tanpa ini, agent akan kaku pakai bahasa Indonesia teknis untuk semua orang…`
> baris 167: `> **Jujur:** kamu benar — tanpa mekanisme hidup, sistem akan mati setelah rilis. Sekarang sudah tertanam eksplisit di AGENT_SYSTEM.md…`

**Kenapa cacat:** ini **balasan agent dari sesi masa lalu** yang tertinggal di dalam manual. Tiga masalah
sekaligus: (a) **suara orang-pertama agent** ("Aku", "ku") di dokumen yang seharusnya bersuara netral atau
berbicara ke pembaca; (b) **merujuk percakapan yang tidak ada di dokumen** — *"ide kamu ini"*: ide yang mana?
Pembaca baru tidak punya konteksnya; (c) **tidak bisa kedaluwarsa secara terlihat** — kalau keputusannya berubah,
kalimat pujian ini tetap di sana sebagai fosil.
**Hubungan ke T26:** pemilik mencurigai *"ada prompt yang kata-katanya ditujukan ke pengguna, bukan ke agent"*.
**Ini bentuk terbaliknya, dan nyata:** bukan prompt yang salah arah, melainkan **jawaban chat yang membeku jadi
isi panduan**. Keduanya gejala dari **ketiadaan aturan arah bicara** (lihat F-07 butir 3).

### F-06 · `A` · **P3** · Penanda `agent_instruction` root tidak machine-readable

**Lokasi:** `PANDUAN_PENGGUNA.md` (root meta) baris 3.
**Bukti:** root menyatakan niatnya **dalam prosa**: *"Dokumen ini UNTUK KAMU sendiri … (ditandai jelas ini bukan
instruksi kerja untuk agent)"*. Sementara **keempat manual sistem** memakai **frontmatter YAML**:
`agent_instruction: IGNORE for execution — USER GUIDE ONLY`.
**Kenapa cacat (kecil tapi nyata):** template §1 mensyaratkan penanda itu. Niatnya **terpenuhi**, bentuknya
**tidak konsisten**. Konsekuensinya teknis: agent/alat bisa **grep frontmatter** dengan andal, tapi **tidak bisa**
mendeteksi maksud yang dinyatakan dalam prosa. Jadi dokumen root **tidak terlindungi secara mekanis** dari
diperlakukan sebagai instruksi eksekusi.

### F-07 · `G` · **P2** · Template **tidak memuat** 4 syarat kelulusan T26 — *dilaporkan SEKALI, bukan 5×*

**Lokasi:** `_meta/PANDUAN_PENGGUNA_TEMPLATE.md` (58 baris) — **sumber warisan W-01**.
**Bukti:** template sudah punya 7 bagian wajib + 4 catatan kualitas. Yang **tidak ada** di sana:

1. **Syarat 6 bidang per mekanisme** — apa / kapan / cara bernomor / prompt siap tempel / apa yang terjadi
   sesudahnya / kalau gagal bagaimana. (T26a: *"prompt tanpa panduan"*.)
2. **Syarat 5 kolom per perintah mesin** — perintah / fungsi / kapan dipakai / keluaran diharapkan / kalau gagal.
   (T26b: *"tabel perintah tanpa penjelasan fungsi dan cara"*.)
3. **ATURAN ARAH BICARA** — blok prompt yang ditempel ke agent wajib berkalimat perintah ke agent; **dilarang**
   berkalimat ke manusia; **dan prosa dokumen dilarang bersuara orang-pertama agent** (F-05 adalah buktinya).
4. **Standar kelulusan + audit independen** — *"bisa dipakai orang awam tanpa bertanya lagi"*, dan **tidak boleh
   dinyatakan sendiri oleh penulisnya**: wajib diaudit sesi independen dengan **lensa #5**.

**Cara pelaporan yang sengaja dipilih:** pemindai v1 menandai "standar kelulusan tidak disebut" di **kelima**
manual. Melaporkannya 5× akan mengesankan 5 manual rusak. **Yang benar: 1 gap di TEMPLATE**, yang otomatis
mengalir ke semua sistem karena template itulah sumber warisannya. **Memperbaiki template = memperbaiki 5 manual
sekaligus untuk sistem masa depan.** Ini penerapan langsung prinsip anti-cry-wolf.

### F-08 · `G` · **P2** · Tidak ada **alat pemeriksa mekanis** untuk manual

**Bukti:** kolom "Cara verifikasi" W-01 di `03_KONTRAK_WARISAN.md` = *"validator: keberadaan kedua file;
**audit: diff blok prompt**"*. Yang **mekanis** hanya *keberadaan file*. Yang **bergantung ingatan manusia**:
diff blok prompt, kesamaan tabel, portabilitas, arah bicara.
**Bukti bahwa ketergantungan itu gagal:** **F-01** (tabel kembar yang sudah menyimpang di sistem yang
pegangannya dibuat 15 Sep dan sudah lewat run klinik + review independen PR #63). **Dua lapis pemeriksaan
manusia sudah lewat, cacatnya tetap lolos.**
**Catatan kapasitas:** pemindai yang kubuat untuk audit ini sudah membuktikan **3 dari 4** cek itu bisa
dimekaniskan (diff blok prompt, tabel kembar, portabilitas, arah bicara). **Rasio positif palsunya terukur ~65% pada corpus ini (28 dari 43)** — jadi
alatnya boleh **menjaring kandidat**, tetapi **putusan tetap harus verifikasi manusia/agent**. Merancangnya
sebagai **pemberi verdict otomatis** akan mengulangi kesalahan yang didokumentasikan riset (>90% positif palsu).

---

## 3. Ringkasan terklasifikasi

| ID | Kelas | Prioritas | Objek | Satu kalimat |
|---|---|---|---|---|
| F-01 | B | **P1** | sistem-klinik | Tabel kembar §4/§7 sudah menyimpang; aturan K-10 hilang dari §7 |
| F-02 | B | P2 | sistem-klinik (2 berkas) | Prompt penutup menggandeng `_meta/` → putus saat jadi repo mandiri |
| F-03 | A | P2 | sistem-klinik §6 | "Cara review & merge" isinya cuma "sama seperti repo induk" |
| F-04 | A | P2 | sistem-konten-kreator | Langkah 2 berisi "sesuai yang sudah pernah kamu lakukan sebelumnya" |
| F-05 | A | P2 | sistem-building-aplikasi | Balasan chat agent ("Aku jujur: ide kamu ini…") membeku jadi isi manual |
| F-06 | A | P3 | root meta | Niat `agent_instruction` ada di prosa, tidak dalam frontmatter yang bisa digrep |
| F-07 | **G** | P2 | **template meta** | 4 syarat kelulusan T26 belum ada di sumber warisan |
| F-08 | **G** | P2 | **kontrak warisan** | Verifikasi manual W-01 belum mekanis; F-01 bukti bocornya |

**Peringkat objek (jujur, termasuk yang bagus):** `sistem-presentasi` **paling sehat** (0 temuan B/A; punya
frontmatter, pembuka "Apa ini", 5 langkah review bernomor, jalur unduh di lmarena) → **layak jadi acuan** saat
Tahap 2 menaikkan template, **bukan mengarang standar baru**. `root meta` sehat (1 temuan P3).
`sistem-klinik` **paling banyak temuan** (1×P1, 2×P2) padahal paling muda — masuk akal: dibuat cepat,
diperluas saat flip siap-pakai 14 Sep.

---

## 4. TEMUAN DI LUAR CAKUPAN — **tetap dilaporkan** per ATURAN CAKUPAN

Cakupan audit ini = **manual pengguna**. Enam hal berikut **ketemu saat mengerjakannya**, **di luar cakupan**,
dan **wajib dilaporkan** — tetapi **tidak kutindak** (menemukan ≠ memperbaiki; butuh mandat pemilik).

| ID | Kelas | Prioritas | Temuan di luar cakupan | Bukti |
|---|---|---|---|---|
| X-01 | **G** | **P1** | **Fakta platform ke-4 BELUM TERCATAT: allowlist jaringan lmarena.** `PLATFORM_LMARENA.md` hanya memuat **3** fakta (branch otomatis, tak bisa push pasca-merge, sesi bisa crash). **Tidak menyebut** bahwa hanya `registry.npmjs.org`, `pypi.org`, `api.github.com`, `github.com` yang terjangkau, dan bahwa **semua API layanan eksternal terblokir** | Diukur 18 host dengan `curl`, sesi ini; bukti lengkap bagian M berkas DISKUSI_MENTAH. **Konsekuensi:** pemilik sudah mengonfirmasi produksi = **lmarena**, jadi ini **batasan produksi nyata**, bukan keterbatasan sementara agent |
| X-02 | **G** | P2 | **W-07 mewariskan hanya 3 fakta platform.** Kalau X-01 jadi fakta #4, **isi W-07 berubah** → semua sistem terdaftar wajib memuatnya | `03_KONTRAK_WARISAN.md` butir W-07: *"berisi **3** fakta platform"* |
| X-03 | **G** | P2 | **Tidak ada butir warisan untuk mekanisme audit-isi.** T29/T30 pemilik belum punya tempat di kontrak warisan, jadi tidak akan otomatis mengalir ke sistem masa depan | Daftar butir W-01…W-09: W-06 = QA 3-lapis (self-audit), **tidak** mencakup prompt audit yang dibangkitkan alat + pengiriman hasil otomatis |
| X-04 | **G** | P2 | **`tools/review_prompt.py` hanya terikat PR** (`--pr` / `--generic`). **Tidak ada mode audit isi.** Akibatnya prompt audit isi harus **dikarang tangan** → pihak yang diaudit menulis instruksi untuk pengadilnya sendiri, melanggar prinsip protokol yang sudah ada | `add_argument` baris 616–618; alat berhenti kalau tak ada PR (baris 198–220) |
| X-05 | **N** | P2 | **Tidak ada pengambilan hasil otomatis.** Verdict jadi komentar PR sudah praktik nyata, tetapi sesi penulis **tidak bisa mengambilnya sendiri** — pemilik yang harus memberi tahu | Permintaan pemilik T30; praktik verdict-dalam-komentar-PR tercatat di `_log-sesi/LOG_SESI_2026-09-16_7.md` |
| X-06 | **P** | P3 | **`gh issue create` belum diuji di lingkungan ini.** Yang terbukti baru kemampuan **baca** (`gh api`, `gh pr view`). Kanal issue untuk audit non-PR **belum dibuktikan bisa ditulis** | Rate limit terbaca (sisa 4.984); pengujian tulis = membuat artefak nyata di repo → **butuh izin pemilik** |

---

## 5. POSITIF PALSU YANG DICABUT — dilaporkan terbuka, bukan dibuang diam-diam

**28 kandidat dicabut** (dihitung dari tabel di bawah: 3+2+2+1+1+2+1+1+11+4). Ini bagian yang membuat audit bisa dipercaya: kalau hanya temuan yang ditampilkan,
pemilik tidak bisa menilai apakah daftarnya dilebih-lebihkan.

| Kandidat (dari pemindai) | Kenapa DICABUT |
|---|---|
| 3× "blok prompt tanpa satu pun kalimat perintah" (building-aplikasi b.97, konten-kreator b.169, `00_CARA_PAKAI_SISTEM.md` b.85) | Dua pertama **punya** perintah — daftarku tidak memuat kata *"Ikuti"* dan *"Tolong ulang"*. Yang ketiga **bukan prompt sama sekali**: itu **diagram pohon folder** |
| 2× "instruksi pakai prompt, bukan isi prompt" (klinik b.28 & b.33, kata *tempel*) | Justru **perintah ke agent**: *"Jalankan … `review_prompt.py --pr <nomor>` dan **tempel** keluarannya sebagai SATU BLOK BERPAGAR"*. Yang menempel = **agent**. Arahnya sudah benar |
| 2× "seksi 1 Pembuka tidak ditemukan" (presentasi, konten-kreator) | **Ada**, dengan heading berbeda: presentasi memakai **"Apa ini:"** + *"Consumer akhir = audiens presentasimu"*. Regex-ku yang sempit, bukan dokumennya yang kosong |
| 1× "seksi 2 Prompt Pembuka tidak ditemukan" (root) | **Ada** sebagai `## 1 Prompt Universal — Pakai Ini SETIAP KALI Mulai Sesi Baru`. Namanya beda |
| 1× "18 rujukan `_meta/`" (root) | Aturan self-contained berlaku untuk **folder sistem** yang bisa diekstrak jadi repo mandiri. **Root meta manual bukan folder sistem** — merujuk `_meta/` memang benar di sana |
| 2× "kolom penjelas tabel perintah hilang" (building-aplikasi §Cara review & merge, presentasi §Cara Review & Merge) | Keduanya **punya langkah bernomor lengkap**. Versi presentasi bahkan memuat **peringatan pasca-merge** dan **jalur unduh di lmarena** — yaitu bidang "kalau gagal" yang dituduhkan hilang |
| 1× "bidang penjelasan hilang" (building-aplikasi §Mekanisme Hidup) | Isinya **kaya**: memisahkan hidup-sistem vs hidup-aplikasi, memberi kalimat pemicu, menyebut alat yang dijalankan. Yang benar-benar tidak ada hanya "kalau gagal" |
| 1× "fakta platform lmarena tidak disebut" (klinik) | Substansinya **ada** — *"(fakta platform — buka sesi baru dari main)"* dan *"setelah itu sesi ini TIDAK BISA push lagi (fakta platform)"*. Yang tidak ada hanya **kata** "lmarena". W-07 sendiri dicek di **manifest**, bukan di panduan → bukan pelanggaran W-07 |
| 11× kandidat "residu chat" | Pemakaian "kamu" yang **memang benar** ke pembaca: *"daftar file yang harus **kamu pilih** manual"*, *"tanpa perlu **kamu minta** satu-satu"*, *"tiap kali **kamu minta** agent kerja"*, *"jawab dengan **jujur**"* (itu nasihat ke pengguna, bukan suara agent), *"**kamu jawab** sekali, agent kerjakan sekali"* (isi aturan K-10), *"sudah **kuletakkan**"* (di dalam **contoh kalimat untuk ditempel pengguna** — suara manusia memang benar di situ), *"[tulis **ide kamu** di sini]"* (placeholder) |
| 4× "standar kelulusan tidak disebut" (di 4 manual, selain yang sudah digabung ke F-07) | **Digabung jadi 1 temuan di level template** (F-07). Melaporkannya per-manual mengesankan 5 manual rusak; padahal sumbernya satu |

---

## 6. Batasan audit ini — apa yang **TIDAK** diperiksa (jangan dibaca sebagai "sudah")

1. **Hanya 12 berkas manual + 1 template.** Dokumen cara-pakai lain di dalam `_sistem/` tiap sistem
   (mis. `START_DI_SINI.md`, `AGENT_SYSTEM.md`) **tidak diaudit** — kecuali `00_CARA_PAKAI_SISTEM.md`
   konten-kreator yang ikut terpindai karena berperan sebagai pegangan.
2. **Keterbacaan oleh orang awam dinilai oleh agent, bukan oleh orang awam.** Lensa #5 menuntut kacamata
   pengguna; agent **bukan** pengguna. **Standar kelulusan T26 ("bisa dipakai tanpa bertanya lagi") belum bisa
   dinyatakan lulus oleh siapa pun** sampai pemilik sendiri mencoba. Ini batas kejujuran, bukan kelalaian.
3. **Tidak ada berkas yang diubah.** Audit ini read-only. Skrip pemindai ada di `/tmp/` (tidak ikut ter-commit)
   karena statusnya alat bantu sementara; **kalau pemilik memutuskan Tahap 2 jalan, skrip itu harus dipromosikan
   jadi `tools/` yang teruji** — bukan ditulis ulang dari ingatan.
4. **Belum memeriksa konsistensi antar-manual** (mis. apakah istilah "gerbang" dipakai sama di 4 sistem) —
   itu lensa #1/#2, di luar cakupan lensa #5 yang dimandatkan.
5. **Angka "19% sinyal" berlaku untuk pemindai ini pada corpus ini**, bukan klaim umum tentang alat analisis statis.

---

## 7. Rekomendasi (BELUM dieksekusi — menunggu keputusan pemilik)

| # | Rekomendasi | Menjawab | Level |
|---|---|---|---|
| R-01 | **Naikkan `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`** dengan 4 syarat T26 (6 bidang, 5 kolom, aturan arah bicara, standar kelulusan + wajib audit lensa #5 oleh sesi independen). **Pakai `sistem-presentasi` sebagai acuan bentuk**, bukan mengarang baru | F-07 | **meta → otomatis diwarisi sistem masa depan** |
| R-02 | **Mekaniskan verifikasi W-01**: promosi skrip audit ini jadi `tools/` — cek diff blok prompt antar-2-berkas, deteksi tabel kembar menyimpang, deteksi `_meta/` di dalam blok prompt, deteksi arah bicara. **Dirancang sebagai penjaring kandidat + wajib verifikasi, BUKAN pemberi verdict** (rasio positif palsu ~65% terukur: 28 dari 43) | F-08, F-01, F-02 | **meta + `tools/`** |
| R-03 | **Perbaiki 5 temuan objek** (F-01…F-05) — masing-masing kecil dan terlokalisasi. **F-01 paling mendesak** (aturan K-10 hilang dari satu salinan) | F-01…F-05 | **4 sistem yang sudah ada** |
| R-04 | **Tambah fakta platform #4 (allowlist jaringan) ke `PLATFORM_LMARENA.md`** + perbarui **W-07** jadi 4 fakta + policy baru (desain untuk jalur git-push, aset dibundel lokal, tanpa API dari sisi agent) | X-01, X-02 | **meta → diwarisi semua sistem** |
| R-05 | **Bangun mekanisme audit-isi** (generator prompt audit + kanal pengiriman + alat pengambil verdict) lalu **daftarkan sebagai butir warisan baru** supaya mengalir ke sistem yang sudah ada maupun yang akan datang | X-03, X-04, X-05 | **meta + `tools/` + kontrak warisan** |
| R-06 | **Uji `gh issue create` sekali** dengan izin pemilik, untuk membuktikan kanal pengiriman X-05/X-06 sebelum dirancang lebih jauh | X-06 | **`tools/`** |

**Catatan urutan:** R-01 & R-02 dikerjakan **lebih dulu** daripada R-03. Alasannya kausal: memperbaiki 5 manual
sebelum standarnya dinaikkan berarti memperbaikinya terhadap standar yang **belum disahkan** — lalu harus
diulang. Sebaliknya R-04 bersifat **independen** dan bisa jalan paralel.

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Laporan audit dibuat; **tidak ada perbaikan dieksekusi** | Pilihan pemilik eksplisit: *"audit dulu, laporkan, baru putuskan perbaikannya"*. Menerapkan ATURAN CAKUPAN: temuan di luar cakupan dilaporkan (bagian 4), tidak ditindak |
| 2026-09-17 | **28 kandidat dicabut terbuka** sebagai positif palsu (bagian 5) | Prinsip #8 *"jangan menghaluskan"* + bukti riset: cry-wolf adalah alasan utama alat review ditinggalkan. Menampilkan hanya temuan akan membuat daftar ini tak bisa dinilai kejujurannya |
| 2026-09-17 | F-07 dilaporkan **sekali di level template**, bukan 5× per manual | Sumber warisannya satu; memperbaiki template memperbaiki semua sistem masa depan sekaligus. Melaporkannya 5× = membesar-besarkan |
| 2026-09-17 | R-01 memakai **`sistem-presentasi` sebagai acuan**, bukan mengarang standar baru | Sistem itu 0 temuan B/A dan sudah mempraktikkan yang dituntut T26 — bukti internal bahwa standarnya bisa dicapai |
