# Log Bukti Acceptance Test — Sistem Klinik (AT-KL)

> Bukti eksekusi skenario `ACCEPTANCE_TESTS.md`. Bukti memakai struktur (berkas ada/hilang), pola (grep/regex), dan status kembalian alat (exit code) — BUKAN angka yang berubah-ubah (larangan C-04). Eksekusi: 2026-09-14, sesi arena/01a09fd5-pembangun-sistem (Langkah 7 rencana kerangka).

## Metode eksekusi (jujur)

- Uji dijalankan pada **salinan sandbox** `_fixture/sistem-kecil-sakit/` di `/tmp/atkl/` — fixture asli di repo TIDAK diubah agar tetap "sakit" untuk pengujian berikutnya; kit TIDAK pernah masuk git manapun (Kebijakan Lebur aturan 4 dihormati sampai di dalam uji sendiri).
- Target sandbox di-`git init` lokal tanpa remote — langkah "PR target terbuka" dilewati secara sadar (tidak ada remote); padanannya: commit peleburan tercatat lokal. Di run nyata langkah PR berlaku penuh.
- G-Rencana & G-Final run uji: mandat pemilik 14 Sep 2026 (pemilik memilih "Tuntaskan Langkah 7 dulu" — acceptance test pertama adalah isinya).

## AT-KL-01 — Idempotensi dan Penanaman Dasar

### Run 1 (suntik penuh) — LULUS

| Langkah | Hasil |
|---|---|
| Salin kit ke target | `kit/` v0.1.2 di sandbox target |
| Tahap A pendaftaran | kunjungan pertama; konvensi target: README ringkas + python → tanam bentuk sederhana per 04 |
| Tahap B diagnosis | C-05 temuan (checkpoint absen total); C-03/C-02 varian absen (tanpa log/manifest); C-01/C-04/C-06 n/a; kapabilitas: nihil-jujur |
| G-Rencana | mandat pemilik (uji fixture) |
| Tahap C tanam | README di-EXTEND (Prompt Pembuka + STATUS SISTEM + Fakta Platform + Titik Persetujuan + QA); CREATE LOG_SESI.md, SYSTEM_MANIFEST.md (mini + Log Keputusan), REKAM-KLINIK.md (cap v0.1.2); nol overwrite |
| Tahap D verifikasi | `kit/alat/validate_target.py` → `VALIDATION PASSED (TARGET)` exit 0; grep W-01/W-02/W-03(+field deterministik)/W-04/W-05/W-06/W-07/W-08 semua OK; `python3 app.py` exit 0 |
| Tahap E peleburan | `rm -rf kit` + commit — isi target akhir: README.md, LOG_SESI.md, REKAM-KLINIK.md, SYSTEM_MANIFEST.md, app.py (kit hilang; jejak = rekam + cap) |
| Tahap F panen | 1 temuan meta (aturan anti-kit-usang belum tertulis — lihat AT-KL-02); target ini sendiri nihil cacat baru |

### Run 2 (suntik kedua — idempoten) — LULUS

- REKAM-KLINIK dibaca dulu: cap v0.1.2 = kit yang dibawa v0.1.2 → tidak ada tawaran naik versi.
- Diagnosis ulang: detektor exit 0; seluruh mekanisme terverifikasi TERPASANG (verifikasi, bukan tanam ulang).
- Keputusan: rencana kosong; peleburan; **`git commit` menolak: "nothing to commit, working tree clean"** — bukti nol perubahan pada run kedua.

### Run 3 (detektor merah) — LULUS

- Field STATUS di README target disuntik `rusak` secara paksa.
- `validate_target.py` → `VALIDATION FAILED (TARGET): W-03: Field STATUS menunjukkan 'rusak'`, **exit 1**.
- (Konteks: kondisi "STATUS absen total" juga teruji merah exit 1 saat pre-audit di fixture asli, 14 Sep.)

## AT-KL-02 — Cek Kit Basi (Fail-Closed)

- **Temuan awal (pre-audit statis, 14 Sep):** ekspektasi skenario (agent menolak bekerja dengan kit usang) BELUM tertulis di aturan — 01 §1.3 + Tahap A.4 hanya mengatur arah cap < kit (tawaran naik versi). Ini cacat aturan sungguhan yang ditangkap acceptance test.
- **Perbaikan:** kalimat anti-kit-usang ditambahkan ke 01 §1.3 + Tahap A.4 (kit lebih tua dari cap → BERHENTI fail-closed, wajib sinkron dulu, dicatat di rekam); kit distamping ulang, versi 0.1.1 → 0.1.2; Log Keputusan 01 + manifest menerima baris perubahan ini.
- **Eksekusi ulang pasca-perbaikan — LULUS:** target dengan rekam cap v0.1.2 + kit palsu ber-stamp versi-kit 0.1.1 → stamp vs cap terdeteksi (0.1.1 < 0.1.2) → aturan 1.3 memicu: Tahap B ditolak, tuntutan sinkron kit dulu, nol byte ditulis ke target (bukti: `git status` target hanya menampilkan folder kit yang tak pernah masuk git).

## Verifikasi struktural sistem (bukan AT-KL, tapi satu baris per perubahan)

- `python3 _sistem/validate_system.py` → PASS (setelah START_DI_SINI didaftarkan ke REQUIRED).
- `python3 tools/validate_repo.py` → PASS 0 warning (88 dokumen aktif, 297 rujukan, 0 unresolved).
- `python3 tools/check_selfcontained.py --sistem sistem-klinik --report` → PASS exit 0.

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-14 | Bukti pertama AT-KL-01 (3 run) + AT-KL-02 dicatat; metode sandbox didokumentasikan | Langkah 7 rencana: acceptance test pertama di fixture (suntik-2x idempoten) — syarat sebelum run nyata sah |
| 2026-09-14 | AT-KL-02 menangkap cacat aturan → diperbaiki 01 §1.3/Tahap A.4 + kit v0.1.2 | Bukti bahwa katalog+uji bekerja: uji menemukan yang belum dipenuhi aturan, aturan diperbaiki, uji ulang lulus |
| 2026-09-14 | Koreksi pasca-review putaran 1 PR #51 (MERAH): angka korpus volatil dicabut dari bukti (baris "Verifikasi struktural" di atas), deviasi W-09 Run 1 dideklarasikan resmi, stamp kit disinkron 6/6 `versi-kit 0.1.2` | Review independen putaran 1: F-2 (angka 297 tidak terreproduksi — salah sejak ditulis), F-7 (deviasi W-09 tak dideklarasikan), F-3 (5/6 stamp masih 0.1.1), F-8 (run perilaku tak terverifikasi reviewer) — semuanya diterima; bukti yang sah = exit code + keberadaan struktur, bukan angka korpus (C-04/C5) |
| 2026-09-14 UTC / 15 Sep WIB | Re-run penuh AT-KL-01/02 + AT-KL-03 baru (varian rawat inap K-11) + regresi meta penuh — bukti di atas; deviasi W-09 + "penulis perubahan sebagai pelaksana" dideklarasikan | K-11 mengubah aturan inti 01 → trigger audit (c) terpicu; AT-KL-03 wajib ada supaya varian panggung baru terbukti mekanis seperti yang lama; satu temuan proses (rujukan backtick memecah R7 template) tertangkap & diperbaiki dalam sesi yang sama |

## Koreksi pasca-review independen — putaran 1 PR #51 (2026-09-14)

Reviewer putaran 1 memutuskan MERAH dengan 7 temuan + 1 hal tak terverifikasi. Semua diterima. Koreksi (append-only — entri lama tidak disunting; yang dicabut di bawah ini digantikan oleh catatan koreksi ini):

1. **(F-2) Angka korpus di atas dicabut.** Baris "297 rujukan" pada butir validate_repo di bagian "Verifikasi struktural sistem" SALAH sejak ditulis: 297 hanya benar pada commit `25a3dbb` (sebelum berkas bukti ini sendiri ditambahkan); pada commit `bbba3c3` yang menulis baris itu, aktualnya 295 — begitu juga di head. Bukti yang sah dan yang berlaku mulai sekarang: **status kembalian alat** (PASS, 0 warning, exit 0) dan keberadaan struktur — angka korpus berubah-ubah TIDAK dikutip lagi (larangan C-04 katalog ini sendiri + C5 meta + header berkas ini).
2. **(F-7) Deviasi W-09 pada Run 1 dideklarasikan resmi.** Run 1 menanam W-01..W-08 saja. Dasar pengecualian: 04_KONTRAK_TANAMAN butir W-09 bentuk sederhana — "tidak wajib jika repo tersebut bisa di-zip dan diberikan utuh ke Claude dalam sekali jalan"; target fixture = 2 berkas (muat satu konteks). Pengecualian ini tercatat di manifest target + REKAM-KLINIK run; yang kurang hanyalah deklarasinya di bagian "Metode eksekusi" — kini dideklarasikan di sini.
3. **(F-1) Klaim "§1.3 diperbaiki" sempat tidak benar — kini benar.** Edit §1.3 yang pertama (14 Sep) hilang karena dua suntingan paralel ke berkas yang sama (yang kedua menimpa yang pertama); reviewer menangkapnya lewat byte-diff baris 41. Kalimat anti-kit-usang kini BENAR-BENAR ada di §1.3 (judul butir kini "Idempoten dan anti-kit-usang"), diverifikasi token tak ambigu + daftar hunk. Konsekuensi: master 01 berubah lagi pasca-koreksi → stamp `kit/aturan/01` memakai sha baru; sha `bc8bb6a0…` yang dikutip di bukti run di atas adalah kit yang benar pada saat run dijalankan (rekam historis, tidak diubah).
4. **(F-3) Stamp kit disinkron.** Keenam `kit/aturan/*.md` kini ber-stamp `versi-kit 0.1.2` dengan sha cocok 6/6 terhadap master — tidak ada lagi kit yang menyatakan versi lebih tua dari `kit/VERSI.txt`/manifest (syarat fail-closed 06_RITME_KIT §2).
5. **(F-8) Status verifikasi run perilaku, atas keputusan pemilik:** Run 1 (tanam+lebur), Run 2 (idempoten), dan AT-KL-02 (fail-closed) dijalankan di sandbox penulis dan tidak memiliki artefak yang bisa diperiksa reviewer di head sha — klaim LULUS-nya tidak diratifikasi reviewer. Pemilik memutuskan 14 Sep: cukup perbaikan artefak + verifikasi ulang putaran 2; clean-run penuh oleh sesi netral menyatu dengan run pertama di dunia nyata (yang bergerbang G-Rencana + G-Final). Semantik detektor (Run 3) sudah direproduksi reviewer sendiri di /tmp — bagian itu terverifikasi.

## Audit trigger (c) + re-run acceptance pasca-K-11 — 2026-09-14 UTC / 15 Sep WIB (sesi arena/01a0a216-pembangun-sistem)

**Konteks:** perubahan aturan inti 01 (K-11: panggung bengkel dihapus, rawat inap = alur standar meta, kit eksklusif suntik) → trigger audit (c) terpicu + AT-KL-03 lahir. Seluruh skenario AT-KL di-re-run pada head kerja sesi ini (bukan di-klaim dari bukti 14 Sep di atas — bukti itu historis dan tidak diubah).

### Metode eksekusi (jujur)

- Sandbox `/tmp/atkl-k11/` — fixture asli di repo tidak disentuh; kit TIDAK pernah masuk git di semua sandbox (entri ignore kerja pada AT-KL-01, dihapus saat peleburan; pada AT-KL-03 tidak ada entri ignore sama sekali karena tidak ada kit).
- Target sandbox di-`git init` lokal tanpa remote — langkah "PR terbuka" disimulasikan: AT-KL-01 = commit peleburan lokal (padanan PR target); AT-KL-03 = artefak `PR-DESKRIPSI-SIMULASI.md` (padanan PR meta normal). Di run nyata langkah PR berlaku penuh.
- G-Rencana & G-Final run uji: mandat pemilik sesi ini (borongan 2 gerbang — arah K-11 + scope; "audit penuh + AT-KL-03" dipilih eksplisit).
- **Deklarasi deviasi (pola F-7):** (a) W-09 dikecualikan di kedua fixture — dasar: 04 butir W-09 bentuk sederhana ("tidak wajib jika repo bisa diberikan utuh dalam satu konteks"); target = 2 berkas; pengecualian tercatat di manifest + REKAM target. (b) Run perilaku dijalankan penulis perubahan (bukan pihak netral) — verifikasi pihak luar tetap pada review independen PR ini + run pertama nyata; dinyatakan jujur, bukan disembunyikan.

### AT-KL-01 (re-run, kit v0.2.0) — SEMUA LULUS

| Run | Langkah kunci | Hasil |
|---|---|---|
| 1 (suntik penuh) | detektor sebelum tanam | `VALIDATION FAILED (TARGET): W-03: Field STATUS tidak ditemukan...` **exit 1** (merah sesuai harapan) |
| 1 | tanam: EXTEND README (Prompt Pembuka, STATUS SISTEM + field deterministik `**Pekerjaan belum tersimpan:** Tidak ada`, Cara Pengujian QA, Fakta Platform, Titik Persetujuan) + CREATE LOG_SESI.md, SYSTEM_MANIFEST.md (mini + tabel Log Keputusan), REKAM-KLINIK.md (cap `0.2.0`, status "LULUS (suntik)") — nol overwrite | commit "tindakan" terbentuk |
| 1 | verifikasi: `validate_target.py` | `VALIDATION PASSED (TARGET)` **exit 0**; `python3 app.py` **exit 0**; grep penanda struktur: `## Prompt Pembuka`, field deterministik, `lmarena`, `Tidak ada auto-merge`, baris tabel `\| Tanggal \| Perubahan \| Alasan \|` — semua ketemu (struktur, bukan angka — C-04) |
| 1 | peleburan: `rm -rf kit` + bersihkan `.gitignore` kerja | `git status` **kosong** (exit 0); `git ls-files`: .gitignore, LOG_SESI.md, README.md, REKAM-KLINIK.md, SYSTEM_MANIFEST.md, app.py — **nol berkas kit** |
| 2 (idempoten) | rekam dibaca duluan (cap 0.2.0 = kit 0.2.0 → tidak ada tawaran naik versi); diagnosis ulang: detektor **exit 0**, seluruh penanda terverifikasi TERPASANG; rencana kosong | `git commit` menolak: **"nothing to commit, working tree clean"** — bukti nol perubahan |
| 3 (detektor merah) | STATUS di-`rusak` paksa | `VALIDATION FAILED (TARGET): W-03: Field STATUS menunjukkan 'rusak'` **exit 1** (pesan tepat); README dipulihkan, tree bersih |

### AT-KL-02 (re-run, kit basi fail-closed — hanya panggung suntik) — LULUS

- Kit PALSU dirakit dari kit v0.2.0: `VERSI.txt` → `0.1.1`, semua stamp `kit/aturan/*` → `versi-kit 0.1.1`.
- Target fix01 (rekam cap `0.2.0` dari Run 1): per aturan 01 §1.3 + Tahap A.4 — kit 0.1.1 **lebih tua** dari cap rekam 0.2.0 → **BERHENTI fail-closed**: Tahap B ditolak, tuntutan sinkron/naikkan kit dulu.
- Bukti nol byte ke target: `git status` sebelum keputusan = hanya `?? kit/` (tak pernah masuk git); sesudah keputusan = **sama** (nol perubahan target).

### AT-KL-03 (BARU — varian rawat inap K-11) — SEMUA LULUS

| Run | Langkah kunci | Hasil |
|---|---|---|
| 1 | sandbox fix03: salinan fixture, `git init` — **tanpa kit** (bukti: `test -e kit` = tidak ada); master dibaca in-place dari `_sistem/` repo | — |
| 1 | detektor (alat portabel stdlib-only dari repo, cwd=sandbox) sebelum tanam | `W-03: Field STATUS tidak ditemukan` **exit 1** |
| 1 | tanam (bentuk identik AT-KL-01 — butir 1.6: artefak dua panggung identik): EXTEND README + CREATE LOG_SESI.md, SYSTEM_MANIFEST.md, REKAM-KLINIK.md (cap `0.2.0`, status "LULUS (rawat inap)") + `PR-DESKRIPSI-SIMULASI.md` | commit "tindakan (rawat inap)" |
| 1 | **Bukti NOL JEJAK KIT:** (1) tidak ada folder `kit/`; (2) `grep -r "Sumber: _sistem"` = nihil (tanpa stamp turunan); (3) tidak ada `.gitignore` kerja; (4) `git ls-files \| grep -i kit` = nihil | semua ✓ |
| 1 | verifikasi | detektor `VALIDATION PASSED (TARGET)` **exit 0**; `app.py` **exit 0**; penanda `TANPA auto-merge — merge = keputusan pemilik` + "sistem TETAP di repo sebagai warga kelas satu" ada di PR simulasi |
| 2 (idempoten) | rekam dibaca duluan (cap 0.2.0 = versi berjalan 0.2.0 → tidak ada tawaran naik versi); seluruh penanda terverifikasi TERPASANG | `git commit` menolak **"nothing to commit, working tree clean"** — nol perubahan; tetap tanpa jejak kit |

### Verifikasi struktural (status kembalian alat — tanpa angka korpus, C-04)

- `python3 _sistem/validate_system.py` → **PASS**
- `python3 tools/validate_repo.py` → **PASS, WARNINGS: none**
- `python3 tools/test_failure_injection.py` → **PASSED** (58 skenario — termasuk R7 template bersih: satu temuan proses terjadi & diperbaiki sesi ini: rujukan entry point rawat inap di 3 berkas meta sempat ber-backtick → menambah warning tak terduga di template bersih → dikoreksi ke provenance tanpa backtick; FI hijau kembali. Terdiri dari: 15 sintetis + 9 unit nyata + 14 regresi review PR-11 + 10 regresi check_selfcontained + 10 regresi review_prompt)
- `python3 tools/backup_verify.py` → **BACKUP AND RESTORE TEST PASSED** (byte-per-byte)
- `python3 tools/build_template.py` → **TEMPLATE CLEAN BUILD PASSED**
- `python3 tools/check_selfcontained.py --semua --report` → **HASIL AKHIR: PASS** (semua sistem; rujukan historis tidak ditegakkan — wajar)
- Sinkron master→kit: 6/6 `kit/aturan/*` stamp `versi-kit 0.2.0` dengan sha = blob master aktual; `kit/VERSI.txt` = `0.2.0` = field Versi manifest.

## Panen C-07 + rilis kit v0.2.1 — 2026-09-16 (sesi arena/01a0a7d3-pembangun-sistem, PR #63)

**Konteks:** Tahap F (panen) run klinik ke-2 pada Sistem Building Aplikasi. Dua hal dikerjakan di sistem ini sendiri: (1) usulan C-07 dinaikkan dari katalog jadi **aturan tanam**; (2) cacat yang ditemukan di tengah jalan — **kit basi** — ditutup dengan gerbang, bukan hanya diperbaiki sekali.

### Temuan: kit BASI karena panen C-07 menyunting master tanpa sync

- Panen C-07 menambah butir `### C-07` ke master `_sistem/02_KATALOG_CACAT.md` (commit di PR #63) **tanpa** menyinkron `kit/aturan/02_KATALOG_CACAT.md`.
- Bukti mekanis (diukur sebelum perbaikan): blob SHA master `4e34ae99fa5bf297ea9e393c8b0b2bd36518dd36` ≠ SHA di stamp kit `8f6b199c761f33510f6fc669cee0623f0b7fdc1f`. Lima aturan lain masih sinkron; hanya katalog yang tertinggal.
- **Tidak ada gerbang yang menyala.** `python3 _sistem/validate_system.py` PASS, `python3 tools/validate_repo.py` PASS, `python3 tools/check_selfcontained.py --semua` PASS — karena AT-KL-02 hanya prosedur manual dan `check_kit()` hanya memeriksa **bentuk** stamp, bukan **isinya**. Ini pelanggaran 06_RITME_KIT §2 yang lolos diam-diam = persis pola C-07 (aturan tanpa gerbang) + F-8 (hijau karena tidak memeriksa apa pun).
- Ditemukan oleh **penulis perubahan sendiri** saat memverifikasi proposal C-07, bukan oleh alat — jadi celahnya nyata.

### Tindakan

1. `_sistem/03_KEBIJAKAN_LEBUR.md` Aturan 2: butir **"Pensiunkan, jangan hapus"** + baris tabel Benar/Salah + checklist butir 2 diperluas (jumlah butir checklist tetap).
2. `_sistem/04_KONTRAK_TANAMAN.md`: W-01 syarat pensiunkan dokumen lama yang digantikan; W-04 satu sumber angka terukur + klaim jumlah dibandingkan hitungan nyata oleh validator target, dibuktikan uji mutasi.
3. `_sistem/validate_system.py`: cek baru **`check_kit_segarkan`** — blob SHA dihitung **tanpa memanggil git** (`sha1("blob <len>\0" + isi)`, stdlib) supaya validator tetap portabel di panggung suntik/rawat inap.
4. `kit/` disinkron ulang 6/6 (stamp: sha blob master aktual, tanggal 2026-09-16, versi-kit 0.2.1) + `kit/VERSI.txt` → `0.2.1`; `SYSTEM_MANIFEST.md` Versi → `0.2.1` + Log Evolusi + field Status disegarkan.

### AT-KL-02 langkah 4-5 (invarian struktural + uji mutasi) — LULUS

Uji mutasi dijalankan di **salinan** `/tmp/klin` (pohon repo tidak disentuh), 10 skenario:

| # | Mutasi | Hasil |
|---|---|---|
| K1 | sunting master `_sistem/05_TAWARAN_KAPABILITAS.md` tanpa sync kit | **GAGAL** — "kit/aturan/05_TAWARAN_KAPABILITAS.md BASI: sha di stamp … != blob sha master saat ini" |
| K2 | `kit/VERSI.txt` → 0.1.9 | **GAGAL** — "kit BASI terhadap manifest: VERSI.txt = 0.1.9 tetapi manifest Versi = 0.2.1" |
| K3 | stamp `versi-kit` di satu turunan → 0.2.0 | **GAGAL** — "stamp versi-kit 0.2.0 != kit/VERSI.txt 0.2.1 — satu rilis kit = satu versi" |
| K4 | hapus `kit/aturan/06_RITME_KIT.md` | **GAGAL** — "turunan hilang — setiap aturan master wajib punya turunan berstempel" |
| K5 | ubah satu kata isi turunan ("Anatomi Perakitan" → "Anatomi Rakit") | **GAGAL** — "isi turunan tidak identik dengan master" |
| K6 | arahkan stamp turunan 01 ke sumber 06 | **GAGAL** — "stamp menunjuk sumber _sistem/06_RITME_KIT.md — seharusnya _sistem/01_ALUR_RUN.md" |
| K7 | rusak satu karakter sha di stamp | **GAGAL** — sha tidak cocok blob master |
| K8 | naikkan Versi manifest ke 0.3.0 tanpa rilis kit | **GAGAL** — "kit BASI terhadap manifest" |
| K9 | keadaan benar (kontrol negatif) | **PASS** |
| K10 | hapus folder `kit/` = panggung rawat inap (kontrol negatif) | **PASS** — cek melompat, sesuai K-11 (kit tidak ada di panggung rawat inap) |

### AT-KL-02 langkah 1-3 (keputusan agent, manual) — TIDAK DIJALANKAN ulang di putaran ini

Alasan (jujur, pola F-8 diumumkan): langkah 1-3 menguji **keputusan agent** pada panggung suntik dan butuh sandbox fixture + agen kedua; yang berubah di putaran ini adalah bagian **struktural** (langkah 4-5), dan itu yang diuji + dimutasi. Run suntik nyata berikutnya wajib menjalankan langkah 1-3 penuh dengan kit v0.2.1.

### Verifikasi struktural (tanpa angka korpus — C5/AT-16)

- `python3 _sistem/validate_system.py` → **PASS** (sebelum sync: **GAGAL** dengan 3 temuan kit basi — bukti ceknya menyala)
- `python3 tools/validate_repo.py` → **PASS, WARNINGS: none, 0 unresolved**
- `python3 tools/check_selfcontained.py --semua` → **HASIL AKHIR: PASS**
- `python3 tools/test_failure_injection.py` → **PASSED: 72 skenario**
- `python3 sistem/sistem-building-aplikasi/_sistem/validate_system.py` → **PASS** (target yang dipanen tetap hijau)
- Invarian rilis kit: 6/6 turunan berstamp sha blob master aktual, tanggal 2026-09-16, versi-kit 0.2.1; `kit/VERSI.txt` = `0.2.1` = field Versi manifest.
