# RINGKASAN CADANGAN — Sistem Klinik

> Ringkasan untuk sesi cadangan (Claude chat biasa) bila lmarena Agent tidak maksimal. **Sumber kebenaran tetap repo** — ringkasan ini hanya peta, bukan pengganti dokumen. Entry point: `sistem/sistem-klinik/START_DI_SINI.md`. Dibuat 15 September 2026 (W-09); folder sistem saat itu berada di `sistem/sistem-klinik/` (dipindah dari root repo oleh PR #55, 15 Sep 2026).

## Cara pakai ringkasan ini (sesi cadangan)

1. Upload ringkasan ini + **hanya dokumen spesifik** yang mau dikerjakan/direvisi (jangan semua file sistem).
2. Claude bekerja seperti biasa; hasilnya kamu tempel manual ke lokasi yang sesuai (Obsidian → sinkron ke GitHub).
3. Update ringkasan ini hanya bila ada perubahan **struktural** (bukan tiap perubahan kecil).

## Identitas

- **Versi:** `0.2.0` · **Status:** `siap-pakai` · **Tahap:** siap-pakai · **Pemilik keputusan:** pemilik repo (semua gerbang + merge di tangannya).
- **Tujuan:** merawat sistem-sistem mandiri milik pemilik, segala umur — **1 run = 1 kunjungan perawatan ke 1 sistem target**. Kit datang, bekerja, melebur, hilang; target "terlihat normal tapi terukur lebih baik", dan bisa diulang (idempoten).
- **Dua panggung (K-11, 14 Sep 2026):**
  - **SUNTIK (rawat jalan — DEFAULT):** target di **repo eksternal**; folder `kit/` disalin ke workspace target, **tidak pernah di-commit ke git target**; PR terjadi di repo target.
  - **RAWAT INAP:** target adalah **folder sistem di repo meta ini** (`sistem/sistem-<nama>/`); jalan sebagai alur standar meta (branch → PR tanpa auto-merge → merge pemilik); aturan dibaca dari **master `_sistem/01–06` di tempatnya** — tanpa salin kit, tanpa stamp, tanpa peleburan. Sistem pasca-rawat tetap warga kelas satu di INDEKS (hapus = keputusan sadar pemilik).
- **Satu siklus (identik dua panggung):** A Pendaftaran → B Diagnosis (read-only) → **[G-Rencana]** → C Tindakan → D Verifikasi → E Catatan (REKAM-KLINIK + cap versi) → F Panen → **[G-Final]** → peleburan & serah-terima.
- **Bukti kematangan:** AT-KL-01/02 (suntik di fixture, termasuk uji idempotensi) dan AT-KL-03 (varian rawat inap: tanpa kit, artefak identik, nol jejak kit) — bukti di `ACCEPTANCE_TEST_LOG.md`. PR #51 (matang penuh v0.1.2) dan PR #53 (K-11 + AT-KL-03) keduanya **MERGED**, PR #53 = review independen **HIJAU** putaran 1/2.

## Struktur inti (folder `sistem/sistem-klinik/`)

| Bagian | Isi |
|---|---|
| `START_DI_SINI.md` | entry point — 5 jenis sesi: (1) lanjut bangun/kerangka, (2) siap & jalankan run SUNTIK, (3) jalankan run RAWAT INAP, (4) audit/evolusi kit, (5) review PR klinik |
| `SYSTEM_MANIFEST.md` | identitas, bentuk (flat + siklus), titik gerbang, tabel Warisan W-01…W-09, Quality & Evolution, trigger audit (a–d) |
| `STATUS.md` | status kerja; field deterministik `Pekerjaan belum tersimpan: Tidak ada` (dipindai validator meta) |
| `00_RENCANA_KERANGKA.md` | sumber keputusan (K-1…K-11), peta dokumen, urutan bangun 10 langkah, Bagian B (patch meta) |
| `_sistem/01_ALUR_RUN.md` | aturan run: Tahap A–F, dua gerbang, adaptasi dua panggung, aturan berhenti fail-closed, definisi selesai 1 run |
| `_sistem/02_KATALOG_CACAT.md` | daftar hidup cacat: ID, gejala, cara periksa, pola perbaikan, risiko — **satu-satunya tolok ukur diagnosis** |
| `_sistem/03_KEBIJAKAN_LEBUR.md` | 6 aturan tanam: extend>create · overwrite per-item · konvensi target menang · **kit tak pernah masuk git target** · istilah klinik tak menular · rekam klinik wajib |
| `_sistem/04_KONTRAK_TANAMAN.md` | syarat minimum "sistem sudah dirawat" (turunan W-01…W-09) + cara verifikasi per tanaman |
| `_sistem/05_TAWARAN_KAPABILITAS.md` | mekanisme tawaran plugin/skill: pemetaan kebutuhan → kandidat → tabel rekomendasi → keputusan pemilik → tanam → registrasi di manifest target |
| `_sistem/06_RITME_KIT.md` | perakitan kit, stamp sha, cek "kit tidak basi", ritme rilis & tawaran naik-versi |
| `_sistem/validate_system.py` | validator lokal folder (harus PASS sebelum PR yang menyentuh aturan) |
| `kit/` | hasil rakitan untuk **suntik**: `aturan/01–06` (salinan ber-stamp sha master), `alat/validate_target.py`, `PROMPT-ENTRI-KIT.md`, `PROMPT-PENUTUP-KIT.md`, 3 template, `VERSI.txt` (`0.2.0`) |
| `_fixture/sistem-kecil-sakit/` | mini-sistem dummy sengaja cacat, untuk acceptance test; **bukan** target rawat inap |
| `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` | pegangan pengguna (blok prompt harus identik) — prompt pembuka + penutup |
| `10_LOG_SESI.md` | aturan log sesi self-contained; file log hidup di `_log-sesi/` level repo |

## Cara pakai, ringkas

**SUNTIK (target di repo luar):**
1. Di repo meta: cek kit tidak basi — stamp sha `kit/aturan/*` harus = blob sha master `_sistem/*`, dan `kit/VERSI.txt` = field Versi manifest (aturan `06_RITME_KIT.md` §2). Beda → sinkron dulu.
2. Baca `_sistem/01_ALUR_RUN.md` penuh.
3. Di repo target: salin folder `kit/` ke workspace (**jangan di-`git add`**), kirim isi `kit/PROMPT-ENTRI-KIT.md` sebagai prompt pembuka.
4. G-Rencana sebelum menyentuh target; G-Final sebelum peleburan/PR. Overwrite & install kapabilitas selalu per-item, ditanya diborong (K-10).
5. Tahap F **Panen wajib**: temuan cacat/celah aturan dilaporkan balik ke repo meta (boleh nihil — tapi diam tidak sah).

**RAWAT INAP (target di repo ini):**
1. Pemilik meletakkan folder sistem target di repo ini (`sistem/sistem-<nama>/`) — sumber path satu-satunya: `INDEKS_SISTEM.md`, tidak di-hardcode.
2. Sesi baru dari `main`, tempel `PROMPT_ENTRI_UNIVERSAL.md`.
3. Agent orientasi (manifest/STATUS/log target) lalu **BERTANYA** (audit / perbaiki / upgrade) **sebelum menyentuh apa pun** — G-Rencana berlaku utuh.
4. Hasil = PR meta normal tanpa auto-merge; sistem tetap terdaftar di INDEKS.

## Pelajaran keras (jangan dilanggar)

- **Kit ≠ sumber kebenaran.** Master = `_sistem/01–06`. Kit adalah turunan ber-stamp; kalau beda, kit yang salah.
- **Kit tidak pernah masuk git target** (Aturan 4, absolut) — sekali ter-commit, "melebur" meninggalkan mayat permanen di histori target. Salin ke workspace target = BOLEH dan memang wajib; `git add kit/` = TIDAK.
- **Anti-kit-usang dua arah** (01 §1.3): cap rekam < versi kit → wajib tawarkan naik versi; kit yang dibawa lebih tua dari cap rekam → **berhenti fail-closed**, sinkron dulu.
- **Idempotensi dibuka dari REKAM-KLINIK**, bukan dari audit ulang: yang sudah terpasang diverifikasi; yang pernah DITOLAK pemilik tidak ditawari ulang tanpa alasan baru.
- **K-10 model tanya:** semua keputusan per-item ditanya **diborong** (maks ±5 butir per pesan), tiap tawaran kapabilitas memuat APA→fungsi→alasan→cara pasang→risiko→alternatif→konsekuensi bila tidak; selalu ada slot usulan pemilik.
- **F-8 (catatan jujur):** AT-KL dijalankan penulis perubahannya sendiri — verifikasi pihak luar menyatu dengan **run pertama nyata** (sampai sekarang belum pernah terjadi).
- **T-2 (15 Sep 2026):** `tools/review_prompt.py` pernah buta pada PR >100 berkas (`gh pr view --json files` terpotong 100) → sudah diperbaiki dengan `gh api --paginate` + uji mutasi RP5. PR besar kini terbaca utuh.

## Bagian yang BELUM selesai (per 15 September 2026)

1. **Run pertama di dunia nyata belum pernah** — panggung & target menunggu pilihan pemilik (suntik ke repo eksternal, atau rawat inap dengan meletakkan/menunjuk folder sistem di repo ini).
2. **Laporan audit tersendiri** belum ada — bukti audit berbentuk eksekusi (AT-KL + ACCEPTANCE_TEST_LOG.md + LOG_SESI), dinyatakan sebagai keadaan, bukan disembunyikan.
3. **PR meta Bagian B** — **SELESAI 15 Sep 2026** (tawaran kapabilitas jadi langkah WAJIB-BERTAJUK di dua alur meta; meta v1.14.0). Penyimpangan tercatat: meta tidak menyimpan salinan kedua `05_TAWARAN_KAPABILITAS.md` (norma anti-dokumen-kembar) — bisa dibalik bila pemilik minta.
4. **RINGKASAN cadangan (W-09)** — berkas ini; **SELESAI 15 Sep 2026**.
5. Bersihan administratif pasca-PR #55 (status/INDEKS/rujukan path) — **SELESAI 15 Sep 2026**.
