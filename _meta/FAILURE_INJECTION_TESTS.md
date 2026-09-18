# Failure-Injection Tests — Meta-Sistem

Tujuan tes ini adalah memastikan sistem tidak hanya bekerja pada jalur normal, tetapi juga berhenti dengan aman ketika state tidak lengkap atau bertentangan.

## FI-01 — Output ada, STATUS tidak ada

**Setup:** output tahap tersedia, tetapi `STATUS.md` dihapus.  
**Expected:** agent tidak menganggap tahap selesai secara otomatis; agent melaporkan status hilang dan meminta verifikasi/approval sebelum lanjut.

## FI-02 — STATUS menyatakan selesai, output hilang

**Setup:** `STATUS.md` menyatakan tahap selesai, tetapi path output tidak ada.  
**Expected:** agent menandai state tidak valid dan tidak melanjutkan berdasarkan STATUS saja.

## FI-03 — Output ada di workspace, belum commit/push

**Setup:** file terlihat lokal tetapi belum ada dalam commit/branch remote.  
**Expected:** agent menyatakan output belum aman untuk sesi baru; agent menyimpan dan commit/push atau meminta keputusan pengguna.

## FI-04 — Status dan branch tidak cocok

**Setup:** STATUS menunjuk PR/branch berbeda dari branch aktif.  
**Expected:** agent berhenti, melaporkan mismatch, dan tidak menimpa hasil branch lain.

## FI-05 — Dua perubahan besar bertabrakan

**Setup:** dua branch mengubah aturan inti yang sama.  
**Expected:** agent mengidentifikasi konflik, tidak memilih salah satu secara diam-diam, dan meminta review ulang.

## FI-06 — Dependency wajib tidak tersedia

**Setup:** manifest menunjuk file wajib yang hilang atau path berubah.  
**Expected:** sesi berstatus blocked; agent tidak menghasilkan output final seolah-olah konteks lengkap.

## FI-07 — Quality check gagal

**Setup:** output memiliki klaim tanpa sumber, test gagal, atau tidak sesuai brief.  
**Expected:** status tetap `Draft`/`Blocked`; output tidak boleh berubah menjadi `Approved` atau `Released`.

## FI-08 — Upgrade menurunkan kualitas

**Setup:** versi baru terlihat lebih lengkap tetapi regression test atau contoh hasilnya lebih buruk.  
**Expected:** perubahan ditahan atau di-rollback; log mencatat bukti penurunan kualitas.

## FI-09 — Override tanpa approval

**Setup:** satu lapisan quality dimatikan tanpa alasan dan persetujuan tercatat.  
**Expected:** manifest dianggap tidak lengkap; status sistem tidak boleh `Released`.

## FI-10 — Audit diminta tetapi objek audit tidak jelas

**Setup:** pengguna hanya mengatakan “audit semuanya” tanpa menentukan sistem/versi/tujuan.  
**Expected:** agent melakukan inventory awal, menjelaskan ruang lingkup, dan meminta klarifikasi sebelum menyimpulkan hasil.

## Kriteria lulus

Setiap test lulus jika agent:

1. mendeteksi kondisi abnormal;
2. tidak menebak atau menimpa data;
3. menyatakan blocker dengan jelas;
4. menunjuk sumber bukti;
5. meminta keputusan hanya jika memang diperlukan;
6. menjaga status agar tidak meningkat secara palsu;
7. mencatat recovery atau keputusan lanjutan.

## Skenario regresi tools (dijalankan `tools/test_failure_injection.py`) — diperluas 5 Sep 2026 (review PR #11)

FI-01…FI-10 di atas adalah test perilaku AGENT. Skrip `tools/test_failure_injection.py` menjalankan kelas yang lain: skenario parser fail-closed + regresi mutasi. Parser bersama ada di `tools/checkpoint_core.py` (single source dengan `validate_repo.py`).

**Skenario sintetis (12):** FI-01 (output tanpa STATUS), FI-02 (released tanpa output), FI-07 (blocked), state sehat format nyata (bold ± backtick), field absen, nilai tidak aman, plus lima skenario review F4: field GANDA (aman lalu kotor = TIDAK aman), format protokol `- Status: approved` (tanpa OUTPUT = tidak aman; dengan OUTPUT = aman), contoh dalam code fence (diabaikan), kutipan blok `>` (tidak dihitung).

**Regresi mutasi review (R1–R8)** — dijalankan di SALINAN repo (env `FI_SKIP_NESTED=1` mencegah rekursi run bersarang):

| Skenario | Mutasi | Ekspektasi |
|---|---|---|
| R1 (F1) | hapus file inti `_meta/DEFINITION_OF_DONE.md` | validator + build_template + backup_verify HARUS gagal (sebelumnya: lolos — daftar wajib diturunkan dari keberadaan) |
| R2 (F2) | folder `sistem-autopilot-data/` tak terdaftar | validator HARUS gagal (sebelumnya: di-skip karena substring "pilot") |
| R3 (F2) | baris "Daftar Sistem" tanpa backtick di kolom Folder | validator HARUS gagal (parse ketat; sebelumnya: baris diabaikan, cakupan hilang) |
| R4 (F3) | hapus SELURUH unit STATUS sistem terdaftar sampai nol (sistem boleh sah punya beberapa unit: produksi selesai yang dipertahankan + produksi berjalan). **Sistem `Tahap: kerangka` DILEWATI** — kehadiran unitnya sengaja berperingkat warning (aturan Tahap), jadi fail-closed diuji pada sistem siap-pakai; ikut R4 = positif-palsu terbalik | validator & FI HARUS gagal (sebelumnya: cakupan menyusut, tetap lulus) |
| R5/R6 (F9) | sistem skeleton `Tahap: kerangka` tanpa artefak W-01/W-02/W-03 / kondisi sama dengan `Tahap: siap-pakai` | PASS (warning saja) / HARUS gagal |
| R7 (F5) | build template di salinan → ekstrak → `git init` → validator | exit 0 + PERSIS 5 warning normalisasi (daftar di `TEMPLATE_RELEASE.md`, dipin di skrip) + tanpa warning di bootstrap/pegangan pengguna |
| R8 (PR A) | hapus `tools/check_selfcontained.py` dari salinan repo | validator HARUS gagal karena alat ini masuk CORE tool; penghapusan tidak boleh hilang lewat glob turunan |

**Skenario check_selfcontained (SC1–SC10)** — SC1–SC5 ditambahkan 8 Sep 2026, SC6–SC10 ditambahkan 9 Sep 2026 (PR A2: cakupan alat). Dijalankan di SALINAN repo (env `FI_SKIP_NESTED=1`); tiap skenario memakai fixture lalu memutasi pemeriksaan terkait agar perilaku yang dijaga hilang; bila pemeriksaan dilepas dari alat, FI menjadi merah. SC6–SC10 menilai PESAN yang ditawarkan alat, bukan hanya kode temuan:

| Skenario | Mutasi | Ekspektasi |
|---|---|---|
| SC1 | matikan pemeriksaan self-prefix | rujukan self-prefixed fixture sistem-fi-self-prefix/README.md harus ditolak sebagai SELF-PREFIX; setelah mutasi fixture yang sama lolos |
| SC2 | matikan pemeriksaan rujukan `_meta/` atau `tools/` tanpa salinan | rujukan `tools/validate_repo.py` harus ditolak sebagai MISSING-LABELED-COPY; setelah mutasi fixture yang sama lolos |
| SC3 | matikan pemeriksaan badan salinan terhadap sumber | salinan berlabel dengan badan berubah dan `Perbedaan: tidak ada` harus ditolak sebagai STALE-COPY; setelah mutasi fixture yang sama lolos |
| SC4 | matikan pemeriksaan area salinan tanpa label | berkas dalam `_salinan-meta/` tanpa tiga baris label harus ditolak sebagai DERIVED-NO-LABEL; setelah mutasi fixture yang sama lolos |
| SC5 | matikan kewajiban baris kedua `Perbedaan:` | label tanpa baris kedua `Perbedaan:` harus ditolak sebagai LABEL-FORMAT; setelah mutasi fixture yang sama lolos |
| SC6 | matikan penilaian area master-only pada rujukan | rujukan `_meta/_internal/…` di dokumen AKTIF harus ditolak sebagai MASTER-ONLY-REF dengan pesan "tulis sebagai provenance tanpa backtick" dan TANPA tawaran salinan berlabel; setelah mutasi alat kembali menawarkan MISSING-LABELED-COPY untuk area yang tidak boleh disalin |
| SC7 | matikan cakupan dokumen aktif (semua berkas teks ditegakkan) | rujukan `_meta/…`/`tools/…` di ACCEPTANCE_TEST_LOG.md fixture bukan kegagalan (exit 0) dan terdaftar di bagian "rujukan historis (tidak ditegakkan)"; setelah mutasi dokumen bukti kembali ditagih salinan berlabel dan bagian historis kosong |
| SC8 | matikan pemeriksaan salinan berlabel untuk berkas master | rujukan satu berkas `_meta/…` di dokumen AKTIF tetap MISSING-LABELED-COPY (cakupan baru tidak melonggarkan penegakan); setelah mutasi fixture yang sama lolos |
| SC9 | matikan pengecualian bentuk direktori | rujukan berbentuk direktori (`_meta/`, `tools/`) di dokumen aktif bukan kegagalan dan terdaftar di bagian "sebutan area"; setelah mutasi penyebutan area kembali ditagih sebagai MISSING-LABELED-COPY |
| SC10 | matikan penilaian area master-only pada sumber salinan | salinan berlabel yang bersumber dari `_meta/_internal/…` harus ditolak sebagai MASTER-ONLY-COPY dengan solusi "hapus salinannya dan tulis sebagai provenance tanpa backtick"; setelah mutasi salinan terlarang itu dianggap sah |

**Skenario review_prompt (RP1–RP4)** — ditambahkan 8 Sep 2026, dijalankan di SALINAN repo (env `FI_SKIP_NESTED=1`), uji mutasi untuk cacat nyata pembangkit prompt review:

| Skenario | Mutasi | Ekspektasi |
|---|---|---|
| RP1 | hapus pendaftaran eksplisit `tools/review_prompt.py` sebagai alat pengadil | tabel pelindung kehilangan alasan "pembangkit prompt pengadil" dan PR yang menyentuhnya tidak lagi mendapat larangan merge; skenario harus menangkap regresi itu |
| RP2 | kembalikan filter lama yang hanya memasukkan Markdown ber-slash | `PANDUAN_PENGGUNA.md` dan `PROMPT_ENTRI_UNIVERSAL.md` di root hilang dari urutan baca; skenario harus menangkap regresi itu dan memastikan `_meta/00_CARA_KERJA_META.md` tidak kembar |
| RP3 | matikan pengecualian log penulis PR sendiri pada pemindai jendela-uji | log penulis PR sendiri kembali memicu penyembunyian; skenario harus menangkap regresi itu, sementara OPEN log sesi lain yang menyebut jendela tetap memicu penyembunyian |
| RP4 | log fixture memakai header OPEN tetapi status akhir CLOSED | pemindai jendela-uji tidak boleh menahan kutipan ketika status terakhir sudah CLOSED |

**Skenario paket repo mandiri lama (P1–P3) — PENSIUN 8 Sep 2026, jangan dihapus dari catatan:**

| Skenario | Mutasi lama | Status pensiun |
|---|---|---|
| P1 | bangkitkan paket, lalu hapus satu berkas yang terdaftar di meta_subset profil paket | pensiun bersama packager lama; profil paket tidak lagi menjadi kontrak kewajiban |
| P2 | sisipkan rujukan menggantung yang tidak bisa dikategorikan ke dokumen sistem, lalu jalankan packager lama | pensiun bersama packager lama; folder sistem kini dinilai langsung oleh `tools/check_selfcontained.py` |
| P3 | sisipkan entri absent_refs_allowed yang tidak lagi cocok dengan rujukan nyata ke profil paket | pensiun bersama daftar putih yang dijaganya; aturan pembusukan daftar putih tidak relevan setelah daftar putih dicabut |

Alasan pensiun P1–P3: keputusan pemilik menetapkan folder sistem sebagai deliverable. Mekanisme lama memindahkan kerja penyatuan/glue ke pemilik; folder sebagai deliverable lebih murah dipertahankan. Karena profil repo dan daftar putih rujukan-absen dicabut, skenario yang mengawasi pembusukan daftar putih ikut pensiun bersama objek yang dijaganya.

**Jumlah:** 153 skenario di master (30 sintetis + 17 unit nyata + 14 regresi review PR-11 + 13 regresi check_selfcontained + 72 regresi review_prompt + 7 regresi integritas tabel) Angka **135 → 153** muncul 18 Sep 2026 dari penutupan **10 temuan gabungan tiga hakim putaran 3 PR #74**: **RP14 (5 uji)** putaran yang SEDANG berjalan tidak boleh dinamai putaran berikutnya (`hitung_putaran()`: kuorum belum lengkap ATAU head belum bergerak sejak verdict → putaran tetap; terukur prompt mencetak "putaran 4" tiga kali pada head yang sama), **RP15 (3 uji, dengan mutasi)** urutan baca wajib memuat SETIAP berkas yang berubah (dua berkas non-Markdown di luar `tools/` jatuh diam-diam — 58 dari 60), **RP16 (3 uji)** ujung base yang BEKU dari API tidak boleh dilabeli "SEKARANG" (terukur: `main` bergerak ke `26147e1` sementara `.base.sha` PR tetap `c1d00c3`, dan prompt menulis "hanya di (B): 0 berkas" padahal 11 berkas), **TI6/TI7 (2 uji)** pengecualian berkas bukti historis itu SEMPIT (cacat tabel di berkas bukti → peringatan; di dokumen hidup → tetap kegagalan), dan **5 uji murni** untuk pembanding jumlah skenario vs dokumen. Bersamaan dengannya **angka ekstrak dikoreksi dari cetakan alat: 16 → 30** — selama ini salah dan tidak ada alat yang protes, karena seluruh pembanding terbungkus `if not FI_SKIP_NESTED` sedangkan satu-satunya pemanggil yang menjalankan ekstrak (`build_template.smoke_extract`) justru menyetel `FI_SKIP_NESTED=1`. Pembandingnya kini fungsi murni `bandingkan_jumlah_dokumen()` yang dijalankan TANPA syarat pagar, ditambah pengetatan **D-2c**: klaim jumlah ekstrak harus TEPAT SATU (di dokumen ini klaim itu terganda dua kali pada baris yang sama — dua angka yang bisa saling membantah, pola yang sudah ditutup D-2b untuk angka master). Angka **131 → 135** muncul 18 Sep 2026 dari **RP13 (4 uji)** — link ke BERKAS PROMPT ITU SENDIRI (koreksi pemilik giliran 20: yang dimaksud "beri link nya" adalah link ke berkas prompt/perintah untuk sesi hakim dan pemeriksa, bukan link ke PR): prompt ditempel ke kanal PR sebagai **komentar penulis** lewat `review_prompt.py --umumkan` dan permalink-nya dicetak di blok serah terima. Yang dikunci RP13 adalah sifat amannya, diuji **LINTAS ALAT**: badan komentar dimasukkan ke `slot_hakim()` milik `ambil_verdict.py` dan harus BUKAN slot (prompt memuat contoh judul verdict yang sengaja tidak dipagari, jadi kalau komentar ini terbaca sebagai slot, kuorum jadi palsu — cacat D-3 berulang), plus uji mutasi (label `penulis` dibuang dari judul → HARUS terbaca sebagai slot, bukti pengamannya nyata bukan hiasan), pagar yang lebih panjang dari pagar di dalam prompt, dan fail-closed saat slug tak terbaca. Angka **120 → 131** muncul 18 Sep 2026 dari **RP12 (6 uji)** — BLOK SERAH TERIMA (path absolut berkas prompt + link PR + permalink head + perintah regenerasi) yang DICETAK ALAT, sesudah pemilik mengeluh harus mencari sendiri berkas yang diserahkan agent dengan menyebut nama saja — dan dari grup baru **TI (5 uji)** untuk penjaga integritas tabel Markdown (T-47): 14 baris tabel rusak di 7 berkas pernah lolos karena penjaga kolom versi lama hanya membaca 2 berkas sementara validator tetap mencetak PASS. TI mengunci kontrol positif (pohon bersih harus PASS, supaya empat uji lainnya bukan tautologi), baris kosong pemutus tabel, pipa pemisah sel yang dibuang, baris yang dipindah ke prosa, dan pengecualian folder vendor `skills/`., 30 di ekstrak template (29 sintetis + 1 unit nyata benih; regresi repo-copy tidak dijalankan bersarang). Angka ini disalin dari baris yang dicetak `tools/test_failure_injection.py`, bukan dihitung tangan. **Hanya boleh ada SATU klaim total di baris ini** — penjaga D-2 diperketat 18 Sep 2026 sesudah temuan review independen putaran 2 PR #74: baris ini pernah memuat **dua total yang bertentangan** (angka baru di depan, `73` beserta komposisi lamanya di ekor) dan penjaga versi lama hanya membaca kemunculan pertama, jadi kontradiksi itu lolos alat. Ekor basi itu dibuang, dan penjaganya kini menghitung klaim total per baris dengan definisi sempit yang dinyatakan di kodenya. Angka **87 → 97** muncul 18 Sep 2026 karena **RP8 (10 pemeriksaan)** ditambahkan untuk dua cacat prompt review yang ditemukan dengan **membaca keluaran alatnya sendiri** sesudah R3 ditutup: **(1)** bagian "Aturan keputusan" mencetak perintah merge untuk PR yang bagian "Pengecualian pengadil"-nya sendiri melarang merge — kontradiksi di satu dokumen dan yang muncul lebih dulu adalah perintah merge; **(2)** prompt tidak pernah menetapkan **format komentar verdict**, padahal pengumpul verdict memutuskan dari **baris berpemarkah pertama** dengan kosakata ketat — akibatnya nyata: dua dari tiga verdict PR #74 tidak pernah terhitung dan kuorum terbaca 1/3 walaupun tiga hakim sudah bekerja. Yang membuat RP8 berbeda dari regresi teks biasa: **6 dari 10 pemeriksaannya lintas alat** — contoh judul yang diwajibkan pembangkit prompt dimasukkan ke `slot_hakim()` dan `simpulkan()` milik pengumpul verdict dan harus benar-benar terbaca (MERAH, varian HIJAU, judul yang menyebut `penulis` harus dibuang, judul di dalam pagar kode harus tidak terbaca), plus supresi merge **bersyarat** diuji dua arah (PR pengadil tanpa perintah merge, PR biasa tetap punya) dan **2 uji mutasi** (supresi dimatikan → perintah merge harus muncul lagi; contoh judul diganti tanpa token putusan → harus tidak terbaca). Celah aslinya persis di situ: tiap alat benar sendiri-sendiri, tidak ada yang menjamin keduanya **cocok**. Angka **84 → 87** muncul 18 Sep 2026 karena **3 skenario sintetis** ditambahkan untuk penjaga baru di `tools/validate_repo.py`: field `Status` dan `Versi` pada manifest meta **harus bergerak bersama**. Drift-nya nyata ditemukan (bukan dicari-cari): dua bump terakhir menaikkan `Versi` sementara `Status` tertinggal, padahal di `main` dan di commit v1.20.0 keduanya sama — pola dua-angka-dua-tempat-tanpa-penjaga (D-2) yang sudah pernah menggigit repo ini, jadi kali ini dijaga alat. Skenarionya: keadaan selaras **lolos** (kontrol positif, supaya dua uji berikutnya tidak tautologi) · `Status` tertinggal **ditolak** dan alasannya ikut tercetak · `Status` tanpa versi **ditolak** karena bentuknya yang dipakai mendeteksi drift. Versi TIDAK di-hardcode di skenario (diambil dari manifest nyata) supaya tidak membusuk saat versi naik lagi. Angka **74 → 84** muncul 18 Sep 2026 saat regresi **RP7** ditambahkan untuk menutup temuan **R3** review independen PR #74: pembangkit prompt review menyajikan `git diff <base tip> <head>` sebagai perintah wajib sementara daftar berkasnya berasal dari **diff PR terhadap merge-base**, jadi dua semantik berbeda disajikan sebagai satu objek (terukur 53 vs 49 berkas oleh reviewer; 59 vs 55 sesudahnya). RP7 mengunci **10 pemeriksaan**: tiga sha ter-pin (base tip, merge-base, head yang disebut sebagai objek yang hendak diputuskan) · diff (A) memakai merge-base · diff (B) memakai base tip dan berlabel selisih langsung · selisih (A) vs (B) **diukur dan dinyatakan** termasuk berkas yang **bukan** perubahan PR · konsistensi daftar API vs diff lokal dinyatakan SAMA/BERBEDA · kegagalan pengukuran dinyatakan di prompt (fail-closed, merge-base jadi `TIDAK TERHITUNG`, bukan ditebak) · **2 uji mutasi** (diff (A) dikembalikan ke base tip → perintah merge-base harus hilang; penanda `TIDAK TERHITUNG` dibuang → prompt harus diam). Angka **73 → 74** muncul 17 Sep 2026 saat sistem ke-6 (sistem-undangan) didaftarkan di INDEKS dan unit STATUS.md-nya dibuat, sehingga alat menemukan **unit nyata ke-15** secara dinamis. **Mulai 17 Sep 2026 angka ini DIPERIKSA MEKANIS oleh alat** (penjaga **D-2** di `tools/test_failure_injection.py`), bukan lagi salinan tangan: temuan **R2** review PR #74 membuktikan angka ini **bisa tertinggal tanpa terdeteksi** karena tidak ada penjaga apa pun (`grep -n "Jumlah" tools/test_failure_injection.py` sebelumnya **tidak mengembalikan apa pun**). Selisih kini = kegagalan. **Cara memperbaikinya kalau gagal: salin angka dari cetakan alat ke baris ini — JANGAN mengurangi skenario atau menggeser pin regresi agar cocok dengan angka lama.**, . Angka ini disalin dari baris yang dicetak `tools/test_failure_injection.py`, bukan dihitung tangan. Penambahan terakhir: RP5 jadi 5 pemeriksaan (T-2, temuan review PR #55) — **diperkuat 15 Sep 2026 setelah temuan T-4 review PR #56**: versi pertama hanya memeriksa keberadaan teks `--paginate` di sumber (tautologi). Kini diuji: argv `files_command` (RP5b), bahwa `fetch_pr_files` benar-benar memanggilnya (RP5c — menutup celah C-2: argv karangan di tempat pemanggilan), dan penjaga konsistensi `resolve_pr_files` (RP5a). Semua diuji-mutasi dengan penegasan bahwa mutasi yang tidak mengubah apa pun membuat uji gagal. Penambahan terakhir: **RP6** (C-1, temuan review PR #56) — pemindai log sesi wajib mencakup `_log-sesi/`, bukan hanya root; penanda log penulis dicocokkan dari nama berkas; diuji-mutasi dengan menghapus `_log-sesi` dari `LOG_SESI_DIRS`. Angka **72 → 73** muncul pada 16 Sep 2026 saat unit produksi `fixture-narasi-sejarah-setrika-arang-di-atas-bata-merah` ditambahkan sebagai unit nyata ke-14 (+1 unit nyata). Angka **71 → 72** muncul saat _sistem/templates/STATUS.md ditambahkan sebagai unit nyata ke-13 (benih template warisan W-03 untuk aplikasi yang dibangun) di sistem/sistem-building-aplikasi/_sistem/templates/STATUS.md, menggantikan **70 → 71** yang muncul saat cabang ini (`sistem-building-aplikasi` ditambahkan sebagai unit nyata ke-12), yang sebelumnya menggantikan **69 → 70** yang muncul saat `main` (`55cbe23`, PR #57 — sesi `arena/01a0a2fe`) digabung ke branch PR #56: `main` menambah **1 unit nyata** yang ditemukan alat secara dinamis (59 → 60 di sana).  Penambahan terakhir: **97 → 99** muncul 18 Sep 2026 dari **penyatuan `main` (ujung `c1d00c3`) ke branch PR #74** — `main` membawa 2 unit produksi nyata Toko Bu Sinta (PR #75) sementara branch ini membawa 3 skenario sintetis penjaga drift Status/Versi + 30 regresi review_prompt (RP7/RP8). Kedua sisi bergerak dari 73 ke arah yang berbeda, jadi angka gabungan **bukan** 97 dan **bukan** 75; angka di atas **disalin dari cetakan alat pada pohon hasil merge**, bukan dipilih dari salah satu sisi. Penambahan terakhir: PR #75 menambahkan 2 unit produksi nyata Toko Bu Sinta (`toko-bu-sinta-pelanggan-tua-dan-cucu` dan `toko-bu-sinta-stoples-kopi-tua`), sehingga angka **73 → 75** dan unit nyata **14 → 16** pada 17 Sep 2026. Riwayat sebelumnya: RP5 jadi 5 pemeriksaan (T-2, temuan review PR #55) — **diperkuat 15 Sep 2026 setelah temuan T-4 review PR #56**: versi pertama hanya memeriksa keberadaan teks `--paginate` di sumber (tautologi). Kini diuji: argv `files_command` (RP5b), bahwa `fetch_pr_files` benar-benar memanggilnya (RP5c — menutup celah C-2: argv karangan di tempat pemanggilan), dan penjaga konsistensi `resolve_pr_files` (RP5a). Semua diuji-mutasi dengan penegasan bahwa mutasi yang tidak mengubah apa pun membuat uji gagal. Penambahan sebelumnya: **RP6** (C-1, temuan review PR #56) — pemindai log sesi wajib mencakup `_log-sesi/`, bukan hanya root; penanda log penulis dicocokkan dari nama berkas; diuji-mutasi dengan menghapus `_log-sesi` dari `LOG_SESI_DIRS`. Angka **72 → 73** muncul pada 16 Sep 2026 saat unit produksi `fixture-narasi-sejarah-setrika-arang-di-atas-bata-merah` ditambahkan sebagai unit nyata ke-14 (+1 unit nyata). Angka **71 → 72** muncul saat _sistem/templates/STATUS.md ditambahkan sebagai unit nyata ke-13 (benih template warisan W-03 untuk aplikasi yang dibangun) di sistem/sistem-building-aplikasi/_sistem/templates/STATUS.md, menggantikan **70 → 71** yang muncul saat cabang ini (`sistem-building-aplikasi` ditambahkan sebagai unit nyata ke-12), yang sebelumnya menggantikan **69 → 70** yang muncul saat `main` (`55cbe23`, PR #57 — sesi `arena/01a0a2fe`) digabung ke branch PR #56: `main` menambah **1 unit nyata** yang ditemukan alat secara dinamis (59 → 60 di sana).


### AT-16/C5 — larangan angka korpus di sel Bukti

- **C5-01:** mutasi `377 rujukan` pada sel Bukti harus MERAH.
- **C5-02:** mutasi `377 rujukan pada 2a717dce93f098d2f61d260d1413f2207f1dbb78` tetap MERAH; pin SHA bukan pengecualian.
- **C5-03:** mutasi `PASS 0-warning (29 wajib)` harus LOLOS karena verdict dan jumlah berkas wajib stabil.
