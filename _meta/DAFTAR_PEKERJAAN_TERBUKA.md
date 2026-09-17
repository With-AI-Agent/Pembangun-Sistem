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
| T-27 | **Rencana Kerangka `sistem-undangan` menunggu review pemilik (KATEGORI BESAR)** | **SELESAI secara substansi 17 Sep 2026** — pemilik mengonfirmasi final (*"Setuju — finalisasi dan buat PR-nya"*), **semua 7 pertanyaan review terjawab**, dan **folder sistem sudah dibuat dalam PR yang sama** (aturan M-14): `sistem/sistem-undangan/` berisi `00_RENCANA_KERANGKA.md` (555 baris, FINAL), `SYSTEM_MANIFEST.md` (Tahap kerangka, Versi 0.1.0, Warisan 10 butir), `STATUS.md`, 11 dokumen kerangka, `Input-Pengguna/`, dan validator mandiri `_sistem/validate_system.py`. **3 pertanyaan yang tadinya menggantung** (#2, #3, #6) diterima lewat konfirmasi final tanpa keberatan, dan **dicatat sebagai penerimaan bersyarat** — pemilik masih boleh mengubahnya dan revisinya wajib masuk Log Keputusan | **P1** | SELESAI | `3543612` — PR **#74**. Bukti penutupan = foldernya ada dan bisa diperiksa: `sistem/sistem-undangan/` (15 berkas), validator mandiri PASS, `check_selfcontained --semua` PASS 0 temuan, terdaftar di INDEKS |
| T-28 | **Kelayakan upscaling raster + vectorization di lingkungan ini** | **SUDAH DIUJI 17 Sep 2026** (skrip tersimpan: `_meta/_internal/uji/uji_upscaling.py`, hasil lengkap: DISKUSI_MENTAH bagian P). **Hasil: BISA, dengan batas yang jelas.** FSRCNN_x2/ESPCN_x2 lewat `cv2.dnn_superres` jalan **2–4 dtk untuk A4@300 DPI**; **EDSR OOM-KILL** pada A5@300 dan **Real-ESRGAN gugur** (butuh PyTorch + bobot dari host terblokir); `vtracer` ✅ untuk gambar datar (SVG 23 KB) ❌ untuk foto (6,4 MB). **Tiga koreksi atas Rencana Kerangka sudah diterapkan**: alat diganti, klaim mutu diturunkan (keuntungan AI hanya +0,28…+0,55 dB atas lanczos4, SSIM praktis identik), cetak uji jadi **wajib untuk semua** LOLOS BERSYARAT (SSIM terukur 0,93 < ambang "sangat baik" 0,97). **Langkah 0 naik status jadi kesimpulan terukur**: PSNR guratan tipis 20,8–22,6 untuk semua metode, di bawah ambang 32 | **P1** | SELESAI | `64f2f4b` — skrip uji `_meta/_internal/uji/uji_upscaling.py` + hasil lengkap DISKUSI_MENTAH bagian P + **4 koreksi sudah diterapkan ke draft** Rencana Kerangka bagian 4.3/4.4. Bukti penutupan = **angka terukur**, bukan pernyataan sudah diuji |
| T-29 | **Bobot model super-resolution: VENDORDOWN-GRADE jadi OPSIONAL** | **Turun prioritas karena bukti, bukan karena ditunda.** Hasil uji T-30 menunjukkan **AI upscaling tidak memberi keuntungan pada foto** (pada 1,5× justru lebih buruk di PSNR *dan* SSIM) dan hanya unggul pada **garis halus — jenis isi yang dilarang Langkah 0**. Maka **AI keluar dari jalur kritis**, gerbang G3 diimplementasikan dengan `Lanczos4`, dan **tidak perlu vendor biner ke repo**. **Efek samping menguntungkan: ketergantungan `pip install` hilang dari jalur kritis** — penting karena `pip install` tidak bertahan antar sesi di platform ini. Yang tersisa di item ini **hanya opsional**: kalau kelak AI dipakai sebagai penyempurnaan, vendor FSRCNN_x2 (39 KB) + ESPCN_x2 (85 KB) dan tulis langkah pemasangannya; provenance (URL codeload + sha256) **sudah tercatat** di DISKUSI_MENTAH P.1 | P3 | TERBUKA | hasil uji P.6; biner tidak di-commit (tidak lagi dibutuhkan jalur kritis) |
| T-30 | **Ambang LOLOS BERSYARAT: ≥150 DPI menghasilkan SSIM di bawah ambang "sangat baik" repo** | **DIPUTUSKAN BERDASAR PENGUKURAN 17 Sep 2026.** Pemilik mendelegasikan (*"Aku ikut yang terbaik menurut kamu"*) → yang terbaik **mengukur**, bukan memilih dari dua usulan. Hasil: memperketat 150→200 DPI **berharga besar** (+2,37 dB; SSIM 0,9281→0,9566) tetapi **masih di bawah 0,97**; dan **AI tidak membantu pada foto di kedua kondisi**. **KEPUTUSAN: ambang DIPERKETAT ≥150→≥200 DPI dan ≤2×→≤1,5×; implementasi `Lanczos4`; AI keluar dari jalur kritis; cetak uji wajib untuk semua kasus.** **Confound metodologis dinyatakan**: angka GARIS antar-run tidak sebanding (run kedua menambah resize akhir yang menaikkan PSNR secara artifisial + dimensi ganjil), sedangkan angka FOTO konsisten antar-run → hanya FOTO yang sah disimpulkan | **P1** | SELESAI | `3543612` — PR **#74**. Bukti penutupan = **tabel terukur** di DISKUSI_MENTAH P.6 + keputusan tertulis di sistem/sistem-undangan/00_RENCANA_KERANGKA.md bagian 4.5 (ambang ≥200 DPI / ≤1,5×, `Lanczos4`, cetak uji wajib semua kasus) |
| T-31 | **Pembangunan isi `sistem-undangan` sesudah PR kerangka di-merge** | **Satu sumber kebenaran: sistem/sistem-undangan/STATUS.md field "Tahap berikutnya"** — sengaja TIDAK diduplikasi ke register ini supaya dua daftar tidak bisa berbeda isi. Ringkasnya: (a) PR direview L1 + di-merge pemilik (tanpa auto-merge); (b) **6 prompt Discovery detail** untuk dokumen 01, 02, 05, 06, 09, 10 — **bukan** langsung menulis isi sistemnya; (c) **pegangan pengguna** (W-01) + 12_LOG_SESI.md (W-02) + turunan QA (W-06) = **syarat naik ke `siap-pakai`**; (d) **1 keputusan pemilik masih terbuka: lisensi Remotion** vs alternatif MIT/Apache; (e) turunan audit isi self-contained (W-10) = item **T-07** | **P1** | TERBUKA | sistem/sistem-undangan/STATUS.md |
| T-32 | **Pola "R7 bergeser" SUDAH TERJADI 7× — imbauan tertulis terbukti TIDAK mencegahnya (kejadian ke-7 dibuat 12 menit sesudah item ini ditulis), butuh pencegahan mekanis** | Gejalanya selalu sama: **rujukan ber-backtick ke path yang tidak ada di ekstrak template** membuat pin R7 bergeser dan `test_failure_injection.py` FAIL. Terjadi lagi 17 Sep 2026 saat menulis baris Log Evolusi v1.19.0 + baris T-31 (2 rujukan baru: validator sistem undangan dan STATUS.md sistem itu). **Sudah 5× sebelumnya tercatat, dan peringatan tertulis di log tidak mencegahnya** → ini bukti bahwa **aturan yang hanya berupa imbauan tidak bekerja**; repo ini sudah sampai pada kesimpulan yang sama untuk hal lain ("TERCATAT bukan status yang sah"). **Usulan pencegahan mekanis:** `tools/build_template.py` **sudah tahu persis** apa yang masuk ekstrak, jadi ia bisa **melaporkan rujukan yang akan menggantung** saat membangun — geser deteksinya dari *sesudah* (FI gagal) ke *sebelum* (pembangun memperingatkan). **MODUS KEGAGALAN KEDUA (lebih serius, terjadi 12 menit SESUDAH item ini ditulis):** **pesan commit ditulis lebih dulu, alat dijalankan sesudahnya, dan commit tetap dilakukan walaupun alatnya FAIL** — sehingga commit `feb11e8` sempat memuat klaim **"9 ALAT PASS" yang PALSU**. Rantainya: `for … done && git commit` **tidak memutus rantai** karena loop `for` selalu exit 0. **Ini bukan salah ketik, ini cacat urutan**: klaim lahir sebelum buktinya ada, persis kegagalan yang sudah dinyatakan repo ini sebagai *"TERCATAT bukan status yang sah"*. **Usulan tambahan untuk pencegahan mekanis:** (a) alat dijalankan **SETELAH** semua suntingan dan **SEBELUM** pesan commit ditulis; (b) kegagalan alat **wajib memutus rantai** (`set -e` + periksa exit code tiap alat, bukan loop `for`); (c) `build_template.py` melaporkan rujukan yang akan menggantung **saat membangun**. **Butuh mandat tersendiri** karena menyentuh alat, dan aturan repo melarang menambah mekanisme tanpa alatnya | **P1** | TERBUKA | kejadian ke-6 terverifikasi: warning ekstrak kembali persis 5 sesudah 2 rujukan di-provenance-kan |
| T-33 | **Temuan R1 review PR #74: 2 warning validator karena pegangan pengguna (W-01) belum ada** | Reviewer benar bahwa ini **bukan penyembunyian** (sudah dideklarasikan di badan PR) — yang bertabrakan adalah **syarat penerimaan review "PASS, 0 warning"** vs keadaan Tahap kerangka. **Dua jalan:** (a) sahkan warning kerangka + selaraskan syarat di pembangkit prompt review, atau (b) **buat pegangan penggunanya sekarang** supaya 0 warning terpenuhi sungguhan. **Saran agent ke pemilik: jalan (b)** — karena (a) berarti **mengubah syarat alat penilai demi menyesuaikan pekerjaan penulis yang belum selesai**, pola yang sama dengan menggeser pin; dan karena pegangan pengguna justru **inti tuntutan pemilik sejak awal** (T4 "satu prompt pembuka", T16/T17 "satu pedoman INDUK lengkap"), jadi membuatnya bukan kerja tambahan. **Reviewer juga sudah memperingatkan**: *"Jangan sekadar menyembunyikan warning atau membuat manual kosong demi lolos"* → wajib ikut Standar Kelulusan Manual 5 syarat dan diverifikasi check_manuals.py. **Menunggu keputusan pemilik** | **P1** | TERTAHAN | verdict R1 di komentar PR #74; **menunggu keputusan pemilik** antara jalan (a) dan (b); saran agent tercatat di baris ini |
| T-34 | **Temuan R3 review PR #74: pembangkit prompt review mencampur dua definisi objek diff** | tools/review_prompt.py menghasilkan daftar berkas dari **diff PR terhadap merge-base** tetapi menuliskannya sebagai **perintah diff langsung base-tip ke head**; keduanya **berbeda 4 berkas** (terukur oleh reviewer: 53 vs 49). Akibatnya syarat append-only **tidak bisa dinyatakan hijau** tanpa menyelesaikan ketidakcocokan definisi itu. **Reviewer secara eksplisit TIDAK menuduh penulis menghapus bukti** — dan penulis setuju. **Yang harus diperbaiki:** pembangkit prompt wajib **membedakan** base-tip, merge-base, dan perubahan PR, menyebut **head yang hendak diputuskan secara eksplisit**, lalu membangkitkan ulang pin/daftar/perintah yang konsisten. **Dilarang** menghapus atau menyunting bukti historis agar diff terlihat rapi | **P1** | TERBUKA | verdict R3 di komentar PR #74 (angka 53 vs 49 terukur oleh reviewer) |

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
