# ACCEPTANCE TEST LOG — Sistem Presentasi

> Bukti per run. Lihat skenario di `ACCEPTANCE_TESTS.md`.

## Run 2026-09-05 — AT-SP-15 SIMULASI end-to-end (perkataan pemilik kiriman 2)
Input: `deck-aktif/presentasi-tesis-fikih-hiasan-wanita/PERKATAAN_PEMILIK_VERBATIM.md` (Arab, verbatim).

| Tahap | Hasil | Catatan |
|---|---|---|
| Brief (G1-gen) | verbatim disimpan; traceability 13 butir→slide; tujuan=alat sidang tesis | satu bagian=satu slide (permintaan eksplisit) |
| G1 Peta | kartu 13/13; pertanyaan diperbarui: Q1(ص٩٠)+Q3(ص١٤٦) verbatim, Q2 rekonstruksi berlabel | jalur VISI |
| G2 Outline+Visual | outline mengikuti urutan pemilik; palet A; aspect-safe; purpose-fit: temuan & pertanyaan menonjol, metode 1 slide/sesuai butir | disetujui pola v2-v6 |
| Produksi | `build_deck_v6.py` → 14 slide (judul + 13 butir) | satu bagian/slide; Q1–Q3 digabung tanpa jawaban |
| QA otomatis | `qa_deck.py` exit 0 (14 slide, 0 fail, 0 warn) | jalur (a) |
| QA manusia | preview `preview.html` (jalur b); putusan final = pemilik (jalur c) | Q2 & nama pembimbing menunggu tinjauan pemilik |
| G3 | diajukan; menunggu approval pemilik | |

**Temuan utk Log pelajaran:** heading "السؤال" tak terdeteksi ekstraksi → wajib VISI; jawaban Q1 sangat panjang sehingga Q2/Q3 di akhir Bab 4; pemilik akan menambah butir kemudian → struktur harus mudah ditambah slide.

---

## Run 2026-09-07 — AT-15 Paket repo mandiri (`sistem-presentasi`)

- **Tanggal:** 2026-09-07 (UTC) · **Versi sistem:** `0.4.2` · **Branch:** `arena/01a07a07-pembangun-sistem` (dari `main` `2de9409`) · **Commit sumber paket:** `430e69c` (pohon kerja bersih)
- **Skenario:** AT-15 di `_meta/ACCEPTANCE_TESTS.md`; protokol `_meta/PAKET_REPO_MANDIRI.md`. Paket dibangkitkan ke direktori sementara di luar repo dan TIDAK di-commit.
- **Verdict:** **LULUS** pada `0.4.2` — menunggu **review independen L1**; tidak ada gate lain yang ikut diklaim tertutup.

### Perintah dan keluaran

```
$ python3 tools/pack_repo.py sistem-presentasi --check
(d) DAFTAR PEMBLOKIR — 0
  (kosong — siap di-pack)
verifikasi kering di calon paket:
  validate_repo.py exit=0 | WARNINGS: 0 (warning tier, exit code unaffected)
  validate_system.py exit=0
CHECK HIJAU
exit=0

$ python3 tools/pack_repo.py sistem-presentasi --out <dir-sementara> --zip
PACK sistem-presentasi -> <dir-sementara>
  berkas: 86 | subset _meta: 21 | absent_refs_allowed: 10
--- python3 tools/validate_repo.py (DI DALAM hasil pack) ---
VALIDATION PASSED: 31 required files and Markdown invariants checked
COVERAGE: 50 active documents scanned, 145 path references checked, 0 unresolved
SYSTEMS CHECKED (inheritance contract): 1 registered + pilot excluded by design
WARNINGS: 0 (warning tier, exit code unaffected)
exit=0
--- python3 _sistem/validate_system.py (DI DALAM sistem-presentasi/) ---
deck ditemukan: ['presentasi-tesis-fikih-hiasan-wanita']
SAKTI/struktur lengkap? YA
temuan isi: 0
HASIL: PASS
exit=0
ZIP: <dir-sementara>.zip
PACK OK: <dir-sementara>
```

### Bukti pendukung

| Kriteria AT-15 | Cara diuji | Hasil |
|---|---|---|
| L1 paket berdiri sendiri | `validate_repo.py` dari DALAM paket | PASS, 0 warning, 145 rujukan diperiksa, 0 menggantung |
| L2 sistem sehat di dalam paket | `_sistem/validate_system.py` dari dalam folder sistem di paket | `HASIL: PASS`, 0 temuan isi, deck terdeteksi |
| L3 isi dokumen tidak ditulis ulang | `diff -r` folder sistem di master vs di dalam paket | **kosong** (exit 0) — nol selisih, termasuk PDF, gambar, dan skrip build deck |
| L4 deterministik | dua run ke dua direktori berbeda + `diff -r` | tidak ada selisih (exit 0); 0 direktori bytecode tertinggal |
| L5 fail-closed (validator sistem) | field checkpoint dihapus dari STATUS deck pada SALINAN | `temuan isi: 1` → `HASIL: FAIL`, exit 1 |
| L5 fail-closed (paket) | lima perusakan pada SALINAN paket (dokumen profil dihapus, validator sistem dihapus, rujukan menggantung disisipkan, entri daftar putih basi, profil menuntut berkas yang tidak ikut) | semuanya exit 1 dengan alasan spesifik; rinciannya dicatat di acceptance log sistem konten kreator agar tidak ada dua salinan bukti yang bisa berselisih |
| Arsip siap kirim | `--zip` | arsip terbentuk di samping folder paket (~6,5 MB, berisi bahan tesis + keluaran deck) |

Regresi terkunci: skenario P1–P2 di `tools/test_failure_injection.py` (lihat `_meta/FAILURE_INJECTION_TESTS.md`), keduanya diuji-mutasi.

### Batas klaim

Terbukti: paket bisa dibangkitkan, berdiri sendiri, lolos kedua validator, reproduktif byte-per-byte. Tidak terbukti di sini: upload GitHub sungguhan dan perilaku agent di repo hasil upload.

---

## Run 2026-09-08 — AT-15 Paket repo mandiri (`sistem-presentasi`) — ENTRY DIGANTIKAN

- **Tanggal:** 2026-09-08 (UTC) · **Versi sistem:** `0.4.2` · **Branch:** `arena/01a07ea8-pembangun-sistem` (dari `main` `7c6f528`) · **Commit sumber paket:** `0064fc1` (pohon kerja bersih)
- **Menggantikan entri 2026-09-07 (sha `430e69c`)**: angka lama (86 berkas / 21 subset / 31 required / 50 dokumen / 145 rujukan) TIDAK reproduktif di HEAD — akar masalahnya, benih subset `_meta/` memindai `ACCEPTANCE_TEST_LOG.md` sehingga menulis bukti mengubah isi paket. Perbaikan meta v1.6.0 (benih = dokumen aktif, satu definisi di `tools/checkpoint_core.py`) membuat bukti tidak lagi menggeser isi paket. Entri lama dibiarkan apa adanya, tidak disunting.
- **Skenario:** AT-15 di `_meta/ACCEPTANCE_TESTS.md` (kriteria L1–L6); protokol `_meta/PAKET_REPO_MANDIRI.md`. Paket dibangkitkan ke direktori sementara di luar repo dan TIDAK di-commit.
- **Verdict:** **LULUS** pada `0.4.2` — menunggu **review independen L1**; tidak ada gate lain yang ikut diklaim tertutup.

### Perintah dan keluaran

```text
$ python3 tools/pack_repo.py sistem-presentasi --check
(d) DAFTAR PEMBLOKIR — 0
  (kosong — siap di-pack)
verifikasi kering di calon paket:
  validate_repo.py exit=0 | WARNINGS: 0 (warning tier, exit code unaffected)
  validate_system.py exit=0
CHECK HIJAU
exit=0

$ python3 tools/pack_repo.py sistem-presentasi --out <dir-sementara>
PACK sistem-presentasi -> <dir-sementara>
  berkas: 84 | subset _meta: 19 | absent_refs_allowed: 10
--- python3 tools/validate_repo.py (DI DALAM hasil pack) ---
VALIDATION PASSED: 29 required files and Markdown invariants checked
COVERAGE: 49 active documents scanned, 169 path references checked, 0 unresolved
SYSTEMS CHECKED (inheritance contract): 1 registered + pilot excluded by design
WARNINGS: 0 (warning tier, exit code unaffected)
exit=0
--- python3 _sistem/validate_system.py (DI DALAM sistem-presentasi/) ---
deck ditemukan: ['presentasi-tesis-fikih-hiasan-wanita']
SAKTI/struktur lengkap? YA
temuan isi: 0
HASIL: PASS
exit=0
PACK OK: <dir-sementara>
```

### Bukti pendukung

| Kriteria AT-15 | Cara diuji | Hasil |
|---|---|---|
| L1 paket berdiri sendiri | `validate_repo.py` dari DALAM paket | PASS, 0 warning, 169 rujukan diperiksa, 0 menggantung |
| L2 sistem sehat di dalam paket | `_sistem/validate_system.py` dari dalam folder sistem di paket | `HASIL: PASS`, 0 temuan isi, deck terdeteksi |
| L3 isi dokumen tidak ditulis ulang | `diff -r` folder sistem di master vs di dalam paket | **kosong** (exit 0) — nol selisih, termasuk PDF, gambar, dan skrip build deck |
| L4 deterministik | dua run ke dua direktori berbeda + `diff -r` | tidak ada selisih (exit 0) |
| L5 fail-closed (validator sistem) | field checkpoint dihapus dari STATUS deck pada SALINAN | `temuan isi: 1` → `HASIL: FAIL`, exit 1 |
| L5 fail-closed (paket) | perusakan pada SALINAN paket (lihat `_meta/FAILURE_INJECTION_TESTS.md` P1–P3) | semua exit 1 dengan alasan spesifik |
| L6 angka bukti tidak basi | stabilitas C2 diuji: entri bukti karangan ditambahkan ke salinan kerja, paket dibangkitkan ulang | **daftar file paket identik** (84 berkas / 19 subset / 10 absent); rujukan karangan ke master-artefak TIDAK terseret, hanya tercatat di `PAKET_REPO.md` bagian "Rujukan yang tidak dijamin resolve" |

Regresi terkunci: skenario P1–P3 di `tools/test_failure_injection.py` (lihat `_meta/FAILURE_INJECTION_TESTS.md`), ketiganya diuji-mutasi.

### Catatan khusus kasus C3 (rujukan dokumen non-aktif)

`DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md` menunjuk `_meta/_internal/CABANG_MENGGANTUNG_2026-09-04.md`. Setelah benih = dokumen aktif, berkas `_meta/_internal/CABANG_MENGGANTUNG_2026-09-04.md` TIDAK lagi ikut sebagai lampiran (ia hanya dirujuk dokumen non-aktif). Dipastikan: (i) tidak ada dokumen aktif di paket yang menunjuknya; (ii) rujukan non-aktifnya tercatat di `PAKET_REPO.md`; (iii) validator di dalam paket tetap 0-warning.

### Batas klaim

Terbukti: paket bisa dibangkitkan, berdiri sendiri, lolos kedua validator, reproduktif byte-per-byte, dan bukti tidak lagi mengubah isi paket. Tidak terbukti di sini: upload GitHub sungguhan dan perilaku agent di repo hasil upload.

---

## Run 2026-09-08 — AT-15 Paket repo mandiri (`sistem-presentasi`) — menggantikan entri 0064fc1

- **Tanggal:** 2026-09-08 (UTC) · **Versi sistem:** `0.4.2` (isi sistem tidak berubah) · **Branch:** `arena/01a07ff1-pembangun-sistem` (PR #23) · **Commit sumber paket:** `3058ca5bf8bf50859defeaeaf7a632e42f7dcaac` (pohon kerja bersih; koreksi W2/W5 + D1)
- **Menggantikan entri 2026-09-08 sumber `0064fc1`:** entri itu tetap utuh di atas. Tiga angka luar (84 berkas / 19 subset / 10 absent) **sama**; yang tidak lagi berlaku sebagai angka di dalam paket: 169 rujukan dan sha256 per berkas di PAKET_REPO.md untuk dokumen `_meta` yang disunting PR #23 (dan D1). Itu **diharapkan**, bukan drift daftar berkas.
- **Skenario:** AT-15 di `_meta/ACCEPTANCE_TESTS.md`. Paket TIDAK di-commit.
- **Verdict angka L1–L6:** tuple di bawah. **L7 BELUM terpenuhi**. Tidak ada gate yang diklaim tertutup.

### Perintah dan keluaran (HEAD `3058ca5`)

```text
$ python3 tools/pack_repo.py sistem-presentasi --check
(a) DAFTAR FILE YANG AKAN IKUT — 84 berkas
(b) SUBSET _meta — 18 dokumen + 1 lampiran _internal
(c) absent_refs_allowed — 10 entri
(d) DAFTAR PEMBLOKIR — 0
CHECK HIJAU
exit=0

$ python3 tools/pack_repo.py sistem-presentasi --zip --out <dir-sementara>
PACK sistem-presentasi -> <dir-sementara>
  berkas: 84 | subset _meta: 19 | absent_refs_allowed: 10
--- python3 tools/validate_repo.py (DI DALAM hasil pack) ---
VALIDATION PASSED: 29 required files and Markdown invariants checked
COVERAGE: 49 active documents scanned, 172 path references checked, 0 unresolved
SYSTEMS CHECKED (inheritance contract): 1 registered + pilot excluded by design
WARNINGS: 0 (warning tier, exit code unaffected)
exit=0
--- python3 _sistem/validate_system.py (DI DALAM sistem-presentasi/) ---
deck ditemukan: ['presentasi-tesis-fikih-hiasan-wanita']
SAKTI/struktur lengkap? YA
temuan isi: 0
HASIL: PASS
exit=0
PACK OK
```

Tuple lengkap HEAD: **84 / 19 / 10 / 29 wajib / 49 dokumen / 172 rujukan / 0 warning / validate_system PASS**.

Pembanding base `e33dc059`: 84 / 19 / 10 / 29 / 49 / **169** / 0 / PASS. Beda vs HEAD = **+3 rujukan**. Beda vs perkiraan reviewer (172) = **0**.

### Batas klaim

Yang dicatat: seluruh tuple L6 pada sha di atas. Yang **tidak** berlaku lagi dari entri `0064fc1`: angka 169 rujukan dan sha256 berkas meta di berita acara paket. L7 BELUM.


### 2026-09-09 — Folder mandiri AT-17 (gerbang deliverable)

- **Tanggal:** 9 September 2026 (UTC).
- **Sha master (basis branch):** `5bdd28c418b56fdd7f65244fadf2cff21a5d7a1e` — tip `main`, merge PR #27.
- **Sha commit isi kerja:** `6cf6db114a0f01aabbd11dbab48d4d6aa1d21d76` — commit yang memuat seluruh suntingan folder sistem ini. Entri bukti ini sendiri ada di commit berikutnya di atasnya: sebuah commit tidak dapat memuat sha dirinya sendiri, jadi yang berlaku sebagai rujukan adalah commit isi di atas (pola pencatatan yang sama dipakai `LOG_SESI_2026-09-07.md`).
- **Perintah pembuktian (dijalankan dari root repo master):**

```text
python3 tools/check_selfcontained.py --sistem sistem-presentasi --report
python3 tools/check_selfcontained.py --semua --report
```

- **Hasil:** `exit=0` pada kedua perintah, dengan baris `HASIL SISTEM: PASS` dan `HASIL AKHIR: PASS`. Keluaran persis di bawah diukur pada commit isi kerja di atas, **sebelum** entri bukti ini ditulis; ukur ulang setelah entri ini tertulis ditempel utuh di body PR (putaran 2) dan verdictnya tidak berubah — menulis bukti tidak boleh mengubah hasil gerbang.

```text
== sistem-presentasi ==
salinan sementara: /tmp/check-selfcontained-sistem-presentasi-15r3zbtv/sistem-presentasi
$ python3 _sistem/validate_system.py
deck ditemukan: ['presentasi-tesis-fikih-hiasan-wanita']
SAKTI/struktur lengkap? YA
temuan isi: 0
HASIL: PASS
exit=0
salinan berlabel ditemukan: 2
  - _salinan-meta/PLATFORM_LMARENA.md <- _meta/PLATFORM_LMARENA.md (sha b2985f37eac2be8f1a812711751f8c0dce0f21b9; perbedaan: tidak ada)
  - _salinan-meta/PROTOKOL_REVIEW_INDEPENDEN.md <- _meta/PROTOKOL_REVIEW_INDEPENDEN.md (sha 40422f0f7c9cd2c2a750275f6686565c2d1a240f; perbedaan: tidak ada)
temuan: 0
rujukan historis (tidak ditegakkan): 42
  - 00_RENCANA_KERANGKA.md:3: `_meta/PLATFORM_LMARENA.md`
  - 00_RENCANA_KERANGKA.md:6: `_meta/01_DISCOVERY_LEVEL_0.md`
  - 00_RENCANA_KERANGKA.md:9: `_meta/00_CARA_KERJA_META.md`
  - 00_RENCANA_KERANGKA.md:242: `_meta/SYSTEM_MANIFEST_TEMPLATE.md`
  - 00_RENCANA_KERANGKA.md:308: `_meta/02_PRINSIP_UNIVERSAL.md`
  - 00_RENCANA_KERANGKA.md:319: `_meta/02_PRINSIP_UNIVERSAL.md`
  - 00_RENCANA_KERANGKA.md:370: `_meta/00_CARA_KERJA_META.md`
  - 00_RENCANA_KERANGKA.md:413: `_meta/`
  - 00_RENCANA_KERANGKA.md:430: `_meta/01_DISCOVERY_LEVEL_0.md`
  - 00_RENCANA_KERANGKA.md:432: `_meta/SYSTEM_MANIFEST_TEMPLATE.md`
  - 00_RENCANA_KERANGKA.md:432: `sistem-presentasi/SYSTEM_MANIFEST.md`
  - 00_RENCANA_KERANGKA.md:438: `_meta/INDEKS_SISTEM.md`
  - ACCEPTANCE_TEST_LOG.md:25: `_meta/ACCEPTANCE_TESTS.md`
  - ACCEPTANCE_TEST_LOG.md:25: `_meta/PAKET_REPO_MANDIRI.md`
  - ACCEPTANCE_TEST_LOG.md:71: `tools/test_failure_injection.py`
  - ACCEPTANCE_TEST_LOG.md:71: `_meta/FAILURE_INJECTION_TESTS.md`
  - ACCEPTANCE_TEST_LOG.md:82: `_meta/`
  - ACCEPTANCE_TEST_LOG.md:82: `tools/checkpoint_core.py`
  - ACCEPTANCE_TEST_LOG.md:83: `_meta/ACCEPTANCE_TESTS.md`
  - ACCEPTANCE_TEST_LOG.md:83: `_meta/PAKET_REPO_MANDIRI.md`
  - ACCEPTANCE_TEST_LOG.md:125: `_meta/FAILURE_INJECTION_TESTS.md`
  - ACCEPTANCE_TEST_LOG.md:128: `tools/test_failure_injection.py`
  - ACCEPTANCE_TEST_LOG.md:128: `_meta/FAILURE_INJECTION_TESTS.md`
  - ACCEPTANCE_TEST_LOG.md:132: `_meta/_internal/CABANG_MENGGANTUNG_2026-09-04.md`
  - ACCEPTANCE_TEST_LOG.md:132: `_meta/_internal/CABANG_MENGGANTUNG_2026-09-04.md`
  - ACCEPTANCE_TEST_LOG.md:144: `_meta/ACCEPTANCE_TESTS.md`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:3: `_meta/00_CARA_KERJA_META.md`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:3: `_meta/PLATFORM_LMARENA.md`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:6: `sistem-presentasi/`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:14: `sistem-presentasi/`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:18: `_meta/_internal/arsip-pilot-002-2026-09-03/`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:18: `_meta/_internal/CABANG_MENGGANTUNG_2026-09-04.md`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:140: `_meta/00_CARA_KERJA_META.md`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:143: `_meta/01_DISCOVERY_LEVEL_0.md`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:144: `_meta/SYSTEM_MANIFEST_TEMPLATE.md`
  - DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md:146: `_meta/INDEKS_SISTEM.md`
  - _salinan-meta/PLATFORM_LMARENA.md:90: `_meta/PLATFORM_LMARENA.md`
  - _salinan-meta/PROTOKOL_REVIEW_INDEPENDEN.md:20: `_meta/`
  - _salinan-meta/PROTOKOL_REVIEW_INDEPENDEN.md:36: `tools/review_prompt.py`
  - _salinan-meta/PROTOKOL_REVIEW_INDEPENDEN.md:44: `_meta/ACCEPTANCE_TESTS.md`
  - deck-aktif/presentasi-tesis-fikih-hiasan-wanita/PEMAHAMAN_BAHAN.md:71: `_meta/_internal/AUDIT_SISTEM_PRESENTASI_2026-09-05.md`
  - deck-aktif/presentasi-tesis-fikih-hiasan-wanita/STATUS.md:13: `_meta/_internal/AUDIT_SISTEM_PRESENTASI_2026-09-05.md`
sebutan area: 7
  - START_DI_SINI.md:3: `_meta/`
  - SYSTEM_MANIFEST.md:47: `_meta/`
  - SYSTEM_MANIFEST.md:47: `_meta/`
  - SYSTEM_MANIFEST.md:114: `_meta/`
  - _sistem/01_ATURAN_DESIGN_ISI_GAMBAR.md:3: `_meta/`
  - _sistem/01_ATURAN_DESIGN_ISI_GAMBAR.md:3: `_meta/`
  - _sistem/01_ATURAN_DESIGN_ISI_GAMBAR.md:37: `_meta/`
HASIL SISTEM: PASS
```

- **Salinan berlabel pada run ini:** dua berkas di direktori _salinan-meta/, masing-masing memuat tiga baris label wajib — `_meta/PLATFORM_LMARENA.md` (sha sumber `b2985f37eac2be8f1a812711751f8c0dce0f21b9`) dan `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` (sha sumber `40422f0f7c9cd2c2a750275f6686565c2d1a240f`). Keduanya lolos perbandingan isi byte terhadap sumbernya di master pada sha di atas, dan baris kedua label keduanya menyatakan perbedaan "tidak ada".
- **Dijadikan provenance tanpa backtick (tidak disalin):** induk protokol QA, protokol recovery, template pegangan pengguna, prinsip universal, indeks sistem, protokol kemandirian, acceptance & failure-injection meta, validator master, serta seluruh rujukan ke area _meta/_internal/ (laporan audit) — area itu tidak boleh keluar dari master, jadi menyalinnya adalah pelanggaran.
- **Rujukan ke diri sendiri** (bila ada pada putaran kerja ini) ditulis relatif terhadap folder sistem, bukan berprefiks nama foldernya sendiri.
- **Batas klaim:** entri ini adalah bukti kemandirian folder menurut AT-17, bukan klaim bahwa gerbang acceptance lain tertutup; tidak ada gate sistem yang ditutup di sini, dan penggabungan PR adalah keputusan pemilik langsung.
