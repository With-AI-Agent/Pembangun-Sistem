# Daftar Pekerjaan Terbuka

> **Satu-satunya tempat sah untuk menaruh pekerjaan yang belum selesai.** Dibuat 17 Sep 2026 atas
> pertanyaan pemilik: *"Nantinya semua nya diselesaikan dan dimatangkan tanpa ada yang terlupakan kan?"*
>
> Jawaban jujurnya: **tidak ada jaminan selama daftarnya hanya ada di ingatan agent atau tersebar di
> log sesi.** Jadi daftar ini dibuat sebagai **berkas**, dan **ditegakkan alat**:
>
> 1. Berkas ini terdaftar di inventaris inti statis (`CORE_REQUIRED`) — **menghapusnya membuat
>    validator gagal**, jadi utangnya tidak bisa hilang dengan cara dihilangkan.
> 2. Baris ber-status `SELESAI` **wajib menyebut sha commit** — `tools/validate_repo.py` memeriksanya.
>    **Menutup item tanpa bukti = error**, bukan warning.
> 3. **Baris tidak pernah dihapus.** Item yang batal diberi status `DITOLAK` + alasan, supaya sejarah
>    keputusannya tetap ada (prinsip append-only yang sama dengan log sesi dan laporan audit).
> 4. ID **unik** dan tidak dipakai ulang.

**Status yang sah:** `TERBUKA` (belum dikerjakan) · `TERTAHAN` (butuh keputusan/izin pemilik — **bukan**
kerja teknis) · `SELESAI` (wajib sha) · `DITOLAK` (wajib alasan).

> **JANGAN TERTUKAR:** item di berkas ini ber-ID **`T-nn` DENGAN strip** (T-01…T-24) dan artinya
> **pekerjaan yang belum selesai**. Tuntutan pemilik ber-ID **`T<n>` TANPA strip** (T1…T31) dan
> artinya **masukan yang harus direspons** — daftarnya di `_meta/TANGGAPAN_MASUKAN_PEMILIK.md`.
> Kedua namespace dibedakan oleh stripnya dan diperiksa alat, tetapi sengaja dinyatakan di sini
> karena kemiripannya mengundang salah baca.

**Prioritas:** `P1` merusak/memblokir · `P2` mekanisme tidak jalan sebagaimana dijanjikan · `P3` mutu,
gaya, atau utang yang tidak menghalangi · `P4` usulan.

---

## A. Butuh keputusan atau izin pemilik (TERTAHAN — tidak bisa kukerjakan sendiri)

| ID | Apa | Kenapa tertahan | Prioritas | Status | Bukti / sha |
|---|---|---|---|---|---|
| T-01 | **GAP M-1: W-03 (field checkpoint deterministik) tidak diterapkan di induk** | **Butuh keputusan pemilik**, bukan kerja teknis. Sudah **ditelusuri 17 Sep 2026** atas permintaan pemilik — hasilnya di bagian "Hasil penelusuran T-01" di bawah. Dua pilihan sah: **(a) adopsi** (tambah field hidup di manifest induk + tegakkan di validator) atau **(b) override tercatat** (alasan + dampak + tanggal + approval). Yang **tidak sah**: membiarkannya tanpa status | P2 | TERTAHAN | penelusuran selesai; keputusan belum ada |
| T-02 | **Kanal Issue untuk penyerahan hasil audit** | Token lingkungan ini **tidak punya `issues:write`** (terverifikasi: HTTP 403). Menghidupkannya = **mengubah izin token di sisi GitHub**, di luar kendali agent. Alternatif (kanal berkas ter-commit) **sudah dibangun dan berfungsi**, jadi ini tidak memblokir apa pun | P4 | TERTAHAN | `gh api repos/.../permissions` → semua izin `false` |
| T-03 | **GAP M-3: _cadangan-claude/RINGKASAN_meta.md tidak ada** | 4 sistem anak punya berkas RINGKASAN di folder cadangan; **induk tidak** (RINGKASAN_meta.md). Diusulkan 17 Sep 2026, **sengaja tidak dikerjakan diam-diam** karena menambah berkas ke folder cadangan mengubah cakupan `backup_verify.py` dan perlu persetujuan | P3 | TERTAHAN | diusulkan di tabel Warisan Meta manifest induk |
| T-04 | **Ratifikasi Standar Kelulusan Manual (R-01)** | Template + alat penjaring sudah jadi dan lulus uji-diri, tetapi **standar kelulusan adalah kebijakan**. Pemilik menetapkan kriteria *"bisa dipakai orang awam tanpa bertanya lagi"*; 5 syarat mekanisnya adalah **terjemahanku** atas kriteria itu dan perlu ratifikasi | P2 | TERTAHAN | `1cf43bd` (template 170 baris + `check_manuals.py`) |
| T-05 | **Review independen L1 atas perubahan struktural `_meta/` + `tools/`** | Per `PROTOKOL_REVIEW_INDEPENDEN.md` baris 17, perubahan struktural `_meta/`, menaikkan versi aturan, dan menyentuh `tools/` = **L1 wajib**. **Konflik kepentingan dinyatakan sadar**: commit yang bersangkutan **menambah jalur ke daftar pengadil**, jadi mengubah alat pengadil → **tidak boleh di-merge reviewer**, keputusan pemilik langsung | P1 | TERBUKA | prompt review bisa dibangkitkan `tools/review_prompt.py` |
| T-06 | **9 gap skill untuk `sistem-undangan`** (semula 8; **+ upscaling raster & vectorization** yang lahir dari keputusan G3) | **Cara pasang SUDAH DIKUNCI 17 Sep 2026** atas delegasi pemilik: **git clone + salin folder skill-nya + VENDOR project-scoped ke dalam repo** (`.claude/skills/` atau `skills/` di folder sistem), karena `/plugin` **tidak bisa dijalankan dari lingkungan ini** dan `npx skills` punya **preseden GAGAL-DIAM** di repo ini; vendor ke repo **satu-satunya yang persisten antar sesi**. **4 aturan keamanan wajib**: baca `SKILL.md` + semua skrip SEBELUM di-commit · catat provenance (repo sumber + **sha commit** + tanggal + lisensi) · tolak skill yang meminta data sensitif atau memanggil API eksternal (semuanya terblokir di sini) · **skill yang gagal diuji tidak boleh dinyatakan terpasang**. **Yang masih menahan:** pemilik pernah berkata akan mengirim link skill temuannya, dan tiap butir tetap butuh persetujuan sebelum dipasang — **tidak ada yang dipasang diam-diam** | P2 | TERTAHAN | riset cara pasang: DISKUSI_MENTAH bagian O (4 sumber); daftar 9 gap + lisensi: bagian 6 Rencana Kerangka |
| T-27 | **Rencana Kerangka `sistem-undangan` menunggu review pemilik (KATEGORI BESAR)** | Draft lengkap sudah ditulis di _meta/_internal/RENCANA_KERANGKA_DRAFT_sistem-undangan_2026-09-17.md — memuat bentuk dasar (BERTINGKAT 3 lapis + SIKLUS 7 tahap), 7 hal konsisten, 6 gerbang G0–G5 dalam 3 tingkat risiko, batasan platform, 8 gap skill, 20 dokumen terencana, status 6 prinsip + 10 butir warisan, dan **7 pertanyaan review**. **Tidak boleh dikunci agent sendiri**: alur `01_DISCOVERY_LEVEL_0.md` mewajibkan review isi lengkap oleh pemilik sebelum folder sistem dibuat. **Catatan provenance yang dinyatakan di draftnya:** bagian 2/3/4 adalah **rekonstruksi yang belum pernah tertulis di berkas mana pun** (grep: `BERTINGKAT` 0, `SIKLUS 7` 0, `7 hal konsisten` 0, `G5` 0) sedangkan fakta risetnya ADA (Cloudflare 12 sebutan, Remotion 8, AVIF 8, 300 DPI 6, RSVP 9) — jadi review paling teliti dibutuhkan di bagian itu | **P1** | TERTAHAN | draft 451 baris; **4 dari 7 pertanyaan review SUDAH DIJAWAB pemilik 17 Sep 2026 dan sudah dikunci ke draftnya** (bentuk dasar DIKUNCI · G3 DIROMBAK jadi 3 hasil · domain 3 fase · cara pasang skill). **Sisa 3** (7 hal konsisten, tingkat risiko gerbang, aset besar tidak masuk repo) dinyatakan "dipakai usulan agent kalau tidak ada keberatan". **Folder sistem belum dibuat** — menunggu konfirmasi final |
| T-28 | **Kelayakan upscaling raster + vectorization di lingkungan ini** | **SUDAH DIUJI 17 Sep 2026** (skrip tersimpan: `_meta/_internal/uji/uji_upscaling.py`, hasil lengkap: DISKUSI_MENTAH bagian P). **Hasil: BISA, dengan batas yang jelas.** FSRCNN_x2/ESPCN_x2 lewat `cv2.dnn_superres` jalan **2–4 dtk untuk A4@300 DPI**; **EDSR OOM-KILL** pada A5@300 dan **Real-ESRGAN gugur** (butuh PyTorch + bobot dari host terblokir); `vtracer` ✅ untuk gambar datar (SVG 23 KB) ❌ untuk foto (6,4 MB). **Tiga koreksi atas Rencana Kerangka sudah diterapkan**: alat diganti, klaim mutu diturunkan (keuntungan AI hanya +0,28…+0,55 dB atas lanczos4, SSIM praktis identik), cetak uji jadi **wajib untuk semua** LOLOS BERSYARAT (SSIM terukur 0,93 < ambang "sangat baik" 0,97). **Langkah 0 naik status jadi kesimpulan terukur**: PSNR guratan tipis 20,8–22,6 untuk semua metode, di bawah ambang 32 | **P1** | TERBUKA | hasil uji + 4 koreksi sudah masuk draft; **sha menyusul di baris ini pada commit berikutnya** |
| T-29 | **Bobot model super-resolution belum di-vendor + langkah pemasangan belum tertulis di dokumen sistem** | `pip install` **tidak bertahan antar sesi** (terkonfirmasi: semua paket kosong di awal giliran ini) dan `raw.githubusercontent.com` **DIBLOKIR**, jadi mengandalkan unduhan tiap sesi itu **rapuh**. **Usulan:** vendor `FSRCNN_x2.pb` (39 KB) + `ESPCN_x2.pb` (85 KB) = **124 KB total** ke folder sistem, dan tulis langkah `pip install` (~14 dtk) di pegangan pengguna. **Sengaja TIDAK di-commit sekarang**: Rencana Kerangka belum final dan pemilik belum menyetujui desain G3 yang baru — menaruh biner sebelum desainnya disetujui = artefak yang mungkin harus dicabut. **Provenance sudah dicatat** (URL codeload + sha256 + ukuran) di DISKUSI_MENTAH P.1 sehingga menunda tidak menghilangkan kemampuan mereproduksi | P2 | TERBUKA | provenance tercatat; biner belum di-commit (alasan di samping) |
| T-30 | **Ambang LOLOS BERSYARAT (≥150 DPI, ≤2×) menghasilkan SSIM 0,93 — di bawah ambang "sangat baik" repo (0,97)** | Dua pilihan: **(a)** pertahankan ≥150 DPI + **cetak uji wajib** (sudah diterapkan di draft) atau **(b)** **perketat jadi ≥200 DPI / ≤1,5×**. **Pilihan (b) belum bisa diputuskan karena ≥200 DPI BELUM DIUKUR** — dan draft sudah melarang ekstrapolasi dari tabel yang ada. Butuh pengukuran ulang + kemungkinan keputusan pemilik soal trade-off (lebih ketat = lebih banyak foto client ditolak) | P2 | TERBUKA | angka terukur di DISKUSI_MENTAH P.2; pengukuran ≥200 DPI belum ada |

---

## B. Utang mekanisme (TERBUKA — bisa dikerjakan, belum dikerjakan)

| ID | Apa | Kenapa terbuka | Prioritas | Status | Bukti / sha |
|---|---|---|---|---|---|
| T-07 | **W-10 turunan self-contained di 4 sistem anak** | Mekanisme audit-isi **jalan dari meta**, tetapi salinan protokol + penanaman ke manifest/pegangan **tiap sistem** belum ada. Keempat manifest sistem kini jujur menulis status **"diterapkan sebagian"** | P2 | TERBUKA | — |
| T-08 | **Belum ada alat yang memeriksa artefak W-10 turunan** | Konsekuensi T-07: klaim "diterapkan sebagian" **tidak ditegakkan mekanis**. Kalau turunan itu tidak pernah dibuat, tidak ada alat yang protes. Gap cek ini **dinyatakan di tabel Warisan Meta** | P2 | TERBUKA | — |
| T-09 | **Append-only di kanal berkas belum ditegakkan alat** | Di kanal Issue aturannya alami (komentar baru). Di kanal berkas, **tidak ada pemeriksaan** yang mencegah auditor menimpa laporan putaran pertama. Saat ini **hanya imbauan** di protokol | P2 | TERBUKA | — |
| T-10 | **Kanal berkas belum diuji lintas-sesi** | Baru terbukti terbaca oleh **sesi yang menulisnya**. Belum diuji: sesi **lain** di checkout **lain** mengambilnya sesudah `git pull` | P3 | TERBUKA | — |
| T-11 | **Audit ulang `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` oleh sesi terpisah** | Audit 17 Sep 2026 atas objek ini dijalankan oleh **sesi yang sama** yang membangun mekanismenya, jadi **independensi tidak terpenuhi** dan verdict-nya **PROVISIONAL**. Temuannya nyata, tetapi **penilaiannya harus diulang** oleh sesi yang benar-benar terpisah | P2 | TERBUKA | laporan provisional: `_meta/_internal/audit/AUDIT_PROTOKOL_REVIEW_INDEPENDEN_8be158f.md` |
| T-12 | **Inventaris inti tidak diperbarui otomatis saat alat/berkas inti baru ditambahkan** | Terbukti **pola, bukan kejadian tunggal**: `build_template.py` terdaftar, tetapi 5 berkas baru tidak. Agent harus ingat menambahkannya sendiri. **Usulan:** cek yang membandingkan isi `tools/` + protokol `_meta/` terhadap `CORE_REQUIRED` dan **bertanya** kalau ada yang tidak terdaftar | P2 | TERBUKA | — |
| T-13 | **Klaim inventaris inti di `03_KONTRAK_WARISAN.md` perlu dikualifikasi** | Klaim bahwa inventaris inti mencegah *"validator lupa didaftarkan"* **terlalu luas**: yang dicegah adalah **sistem** baru lupa didaftarkan, **bukan berkas inti** baru (lihat T-12) | P3 | TERBUKA | — |
| T-14 | **Presisi `tools/check_manuals.py` tidak diketahui di luar korpus penyetelannya** | Ambang batas disetel pada berkas-berkas repo ini. **Peringatan overfitting sudah tertulis di docstring alatnya**, tetapi belum ada korpus uji kedua untuk mengukur positif-palsu secara nyata | P3 | TERBUKA | — |
| T-15 | **A-03: konvensi prefiks rujukan tidak konsisten** | `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` baris 4 merujuk `QUALITY_ASSURANCE_AND_EVOLUTION.md` **tanpa prefiks**, sementara baris lain di berkas yang sama memakai prefiks root-relative. **Bukan rujukan mati** (resolve sefolder, validator tidak men-flag), jadi murni keterbacaan | P3 | TERBUKA | ditemukan audit 17 Sep 2026 |
| T-26 | **Masukan pemilik yang TIDAK PERNAH DICATAT tidak bisa dideteksi alat** | Cek validator hanya menegakkan *"yang tercatat wajib direspons"*. Kalau sebuah instruksi pemilik muncul di chat dan **tidak pernah** ditulis ke DISKUSI_MENTAH maupun ledger, **tidak ada alat yang bisa tahu** — karena alat tidak bisa membaca chat. **Gap nyata, bukan hypothetical**: instruksi S-15 hari ini nyaris hanya hidup di riwayat chat; yang menyelamatkannya adalah agent menulisnya ke ledger secara manual. **Usulan mitigasi:** jadikan "tulis masukan pemilik ke ledger SEBELUM mengerjakan apa pun" sebagai langkah wajib di awal sesi (sudah sebagian: sub-butir langkah 7), dan tambah pemeriksaan silang antara log sesi dan ledger — kalau log sesi mengutip kalimat pemilik yang tidak punya baris ledger, peringatkan | P2 | TERBUKA | — |

---

## C. Temuan audit manual Tahap 1 yang belum ditindak

| ID | Apa | Kenapa terbuka | Prioritas | Status | Bukti / sha |
|---|---|---|---|---|---|
| T-16 | **F-02, F-03, F-04** (temuan P2 audit manual) | Sesuai rencana yang disepakati: dikerjakan **sesudah R-01 diratifikasi pemilik** (T-04), supaya perbaikan mengikuti standar yang sudah disahkan, bukan standar sementara | P2 | TERTAHAN | audit `6218d1a` |
| T-17 | **F-05** (temuan P3 audit manual) | Dijadwalkan **sesudah** F-02–F-04 | P3 | TERTAHAN | audit `6218d1a` |

---

## D. Tujuan awal sesi (belum dimulai)

| ID | Apa | Kenapa terbuka | Prioritas | Status | Bukti / sha |
|---|---|---|---|---|---|
| T-18 | **Membangun `sistem-undangan`** | **Tujuan awal sesi ini.** 8+ giliran terpakai untuk pekerjaan meta (perbaikan manual + mekanisme audit/review + warisan ke induk), yang memang diamanatkan pemilik di giliran 5–6, tetapi **sistem undangannya belum satu baris pun**. Alurnya sudah jelas: Discovery Level-0 → rencana kerangka → folder + manifest di PR yang sama → prompt generator per dokumen | P1 | TERBUKA | riset pasar + arsitektur tersimpan di DISKUSI_MENTAH bagian A–M |

**Kritik yang tercatat atas urutanku sendiri:** fondasi yang tidak pernah dipakai membangun apa pun
tidak bisa dibuktikan benar. Rekomendasiku: **berhenti memperluas meta di sini** dan mulai T-18; sisa
utang meta dikerjakan kalau pembangunan benar-benar membutuhkannya.

---

## Sudah ditutup (jangan dihapus — ini jejak)

| ID | Apa | Prioritas | Status | Bukti / sha |
|---|---|---|---|---|
| T-19 | **A-01: 3 artefak mekanisme audit-isi tidak terdaftar di inventaris inti statis** — menghapusnya tidak membuat alat mana pun gagal | P2 | SELESAI | `e127cef` — penutupan diverifikasi dengan mengulang uji penghapusan: baseline hijau sebelum, `- missing required file: tools/audit_prompt.py` sesudah |
| T-20 | **A-02: `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` tidak terdaftar di inventaris inti statis** (pre-existing) | P3 | SELESAI | `e127cef` — penutupan diverifikasi: `- missing required file: _meta/PROTOKOL_REVIEW_INDEPENDEN.md` sesudah penghapusan di salinan repo penuh |
| T-21 | **F-06: pegangan root tidak punya penanda `agent_instruction` machine-readable** | P3 | SELESAI | `4cbd261` |
| T-22 | **GAP M-2: manifest induk tidak punya bagian Batasan Platform (W-07)** | P2 | SELESAI | `f48bd5c` |
| T-23 | **Induk dikecualikan dari kontrak warisannya sendiri** (3 butir tidak terdeteksi alat mana pun) | P1 | SELESAI | `f48bd5c` |
| T-24 | **Cek validator baru menghasilkan PASS palsu** (prosa memenuhi `\bW-nn\b`) | P1 | SELESAI | `f48bd5c` |
| T-25 | **Instruksi pemilik S-15: yang tercatat harus DIBACA + DIRESPONS/DIEKSEKUSI, bukan cuma dicatat** | P1 | SELESAI | `926bd36` — ledger `_meta/TANGGAPAN_MASUKAN_PEMILIK.md` (31 tuntutan + 15 instruksi berdiri) + 4 cek validator **diuji mutasi 6/6 terdeteksi, kontrol hijau** + 2 sub-butir wajib-baca di langkah 7 `_meta/NEXT_SESSION_PROMPT.md` + ledger masuk `CORE_REQUIRED` |

---

## Hasil penelusuran T-01 (W-03 di induk) — dikerjakan atas permintaan pemilik 17 Sep 2026

Pemilik memilih **"telusuri dulu, laporkan, baru putuskan perbaikannya"**. Ini hasilnya. **Tidak ada yang
diubah** — bagian ini murni laporan.

**Apa yang dituntut kontrak (W-03):** setiap unit kerja punya `STATUS.md` berisi field deterministik
`**Pekerjaan belum tersimpan:** Tidak ada` (exact) + `Waktu pembaruan`, dan **template** STATUS memuat
field itu. Verifikasinya: field ada di **semua** STATUS unit + template.

**Apa yang ditemukan:**

1. **Klaim di manifest induk sudah BENAR.** Induk menulis W-03 sebagai **"TIDAK DITERAPKAN"** + gap
   M-1 + dua pilihan sah. **Ini mengoreksi laporanku sendiri** kepada pemilik sebelumnya, yang menyebut
   ada butir "dinyatakan sudah diterapkan padahal buktinya tidak ada" — **untuk W-03 itu tidak benar**;
   butir itu sudah dinyatakan tidak diterapkan secara jujur. Yang benar adalah **tidak ada alat yang
   memeriksa** deklarasi itu, dan itu sudah diperbaiki terpisah.
2. **Induk PERNAH punya unit kerja ber-STATUS.md.** Field deterministik itu **hidup** di
   `_meta/_internal/arsip-pilot-002-2026-09-03/STATUS.md` dan subfolder run-awal-01a0679e di dalamnya. Jadi
   mekanismenya **pernah dijalankan di level induk**, lalu **mati** ketika cara kerja berubah menjadi
   menyunting `_meta/` langsung tanpa unit.
3. **Yang sekarang dipakai induk sebagai pengganti:** header **"Keadaan Sesi"** di log sesi (diperbarui
   tiap giliran) + field `Status`/`Versi` di manifest. Keduanya **berguna untuk manusia**, tetapi
   **tidak ada yang deterministik-exact sehingga bisa diperiksa alat** — dan justru itu inti W-03:
   field yang bisa di-grep dengan satu nilai sah, supaya sesi yang crash tahu persis apa yang belum
   tersimpan.
4. **Parser W-03 tidak memindai induk.** `checkpoint_core.py` mengumpulkan STATUS lewat
   `sys_dir.rglob("STATUS.md")` untuk **sistem terdaftar di INDEKS** saja. Induk bukan sistem terdaftar,
   jadi **tidak pernah diperiksa** — inilah mekanisme pengecualian strukturalnya.
5. **Menambah field ke manifest induk AMAN secara teknis** dari sisi parser W-03 (berkas itu tidak
   dipindai parser tersebut), **tetapi** ada dua risiko yang harus diuji kalau opsi (a) diambil:
   salinan `_meta/_internal/template_clean/` ikut berubah (bisa menggeser pin peringatan ekstrak), dan
   aturan fail-closed parser tentang **field ganda** kalau berkas itu kelak ikut dipindai.

**Rekomendasiku (keputusan tetap di pemilik): opsi (a) — ADOPSI.** Alasannya:

- **Opsi (b) override tercatat itu sah, tetapi melembagakan pengecualian** — sedangkan seluruh maksud
  koreksi pemilik di giliran 8 adalah **induk tidak boleh dikecualikan**. Memilih (b) berarti menjawab
  "induk juga tunduk" dengan "induk dikecualikan, tapi dengan surat izin".
- **Biayanya kecil**: beberapa baris field hidup di manifest induk + perluasan cek validator. Tidak ada
  migrasi, tidak ada perubahan perilaku alat yang ada.
- **Bukti nomor 2 menguntungkan**: mekanismenya bukan barang asing di induk, melainkan sesuatu yang
  pernah hidup dan bisa dihidupkan lagi.
- **Risiko yang harus dihadapi kalau (a) dipilih**: dua hal di butir 5, dan keduanya **teruji** oleh
  alat yang sudah ada (pin R7 akan merah kalau ekstrak bergeser) — jadi risikonya **terlihat**, bukan
  tersembunyi.

**Kalau pemilik memilih (b)**, yang wajib ada: alasan, dampak, tanggal, dan approval — ditulis di tabel
Warisan Meta manifest induk **dan** di Log Keputusan kontrak. Itu format override yang sudah berlaku.

---

## Log Keputusan

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-17 | Berkas ini dibuat sebagai **satu-satunya tempat sah** menaruh pekerjaan terbuka, dan **ditegakkan alat** (terdaftar di `CORE_REQUIRED` + baris `SELESAI` wajib sha) | Pertanyaan pemilik *"tanpa ada yang terlupakan kan?"* tidak bisa dijawab dengan janji. Yang bisa menjawab hanya **daftar yang tidak bisa dihapus tanpa alatnya protes** dan **tidak bisa ditutup tanpa bukti**. Sebelumnya utang tersebar di log sesi, tabel Warisan Meta, dan bagian "Yang belum terbukti" di tiga dokumen berbeda — **tidak ada satu pun yang bisa menjawab "apa saja yang masih terbuka?"** |
| 2026-09-17 | Item yang sudah ditutup **tetap ditulis**, tidak dihapus | Append-only. Jejak keputusan lebih berharga daripada kerapian tabel; dan menghapus baris `SELESAI` akan membuat daftar ini kehilangan kemampuan menunjukkan **laju** penyelesaian |
| 2026-09-17 | **T-19/T-20 dibiarkan ber-status `TERBUKA` satu commit lebih lama** walaupun fix-nya sudah ada di working tree | **Aturan "SELESAI wajib sha" diuji dengan cara dipatuhi, bukan dilonggarkan.** Sha commit yang memuat fix-nya belum ada saat baris itu ditulis, jadi menulis `SELESAI` akan berarti **menutup item tanpa bukti** — persis yang aturannya melarang. Commit berikutnya memindahkan keduanya ke `SELESAI` dengan sha nyata |
| 2026-09-17 (sore) | **T-19/T-20 dipindahkan ke `SELESAI` dengan sha `e127cef`** — dan bukti penutupannya adalah **pengulangan uji yang membongkarnya**, bukan pernyataan bahwa kodenya sudah ditulis | Menutup utang dengan "sudah kukerjakan" adalah bentuk lain dari menutup tanpa bukti. Yang dicantumkan adalah **keluaran alat sesudah penghapusan** (`- missing required file: …`), karena itulah yang membedakan "terdaftar" dari "benar-benar terlindungi" |
| 2026-09-17 | **T-18 (membangun `sistem-undangan`) diberi prioritas P1** dan kritik atas urutanku sendiri dicatat | Supaya daftar ini tidak jadi alat untuk **menunda** pekerjaan utama dengan alasan meta belum rapi. Pemilik berhak melihat bahwa tujuan awalnya belum dimulai |
