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
