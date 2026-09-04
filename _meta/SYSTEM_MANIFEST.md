# System Manifest — Meta-Sistem Pembangun Sistem

- **Status:** `Released — v1.0.0`
- **Versi:** `1.0.0`
- **Tujuan:** merancang, membangun, mengaudit, memperbaiki, dan memelihara sistem kerja untuk berbagai domain.
- **Consumer:** pengguna dan agent yang bekerja pada repository.
- **Pemilik keputusan:** pengguna
- **Entry point pengguna:** `PANDUAN_PENGGUNA.md`
- **Entry point agent:** `00_CARA_KERJA_META.md`
- **Index:** `INDEKS_SISTEM.md`
- **Quality protocol:** `QUALITY_ASSURANCE_AND_EVOLUTION.md`
- **Definition of done:** `DEFINITION_OF_DONE.md`
- **Acceptance tests:** `ACCEPTANCE_TESTS.md`
- **Checkpoint/recovery:** `PROTOKOL_CHECKPOINT_RECOVERY.md`
- **Platform constraints:** `PLATFORM_LMARENA.md` (fakta vs policy, wajib baca)
- **Override:** tidak ada

## Bentuk Sistem

- **Bentuk struktural:** adaptif; dapat membangun sistem bertingkat, flat, siklus, atau gabungan.
- **Bentuk operasional:** siklus discovery → design → build → audit → release → observe → evolve.
- **Unit kerja:** satu sistem domain atau satu perubahan pada meta-sistem.

## Tiga Lapisan Quality

| Lapisan | Objek | Artefak |
|---|---|---|
| Meta | Meta-sistem ini sendiri | `_internal/` audit, log, acceptance tests, release history |
| Sistem domain | Sistem yang dihasilkan | manifest, quality protocol, self-audit, log evolusi |
| Output | Artefak sistem domain | status Draft → Checked → Approved → Released → Observed |

## Prinsip Universal

| Prinsip | Berlaku? | Catatan |
|---|---|---|
| Hierarki | Kondisional | Hanya jika bentuk sistem memiliki pewarisan level |
| Chaining | Kondisional | Jika sistem memiliki alur multi-tahap |
| Approval bertingkat | Ya | Kriteria konkret ditentukan per sistem |
| Checkpoint & recovery | Kondisional | Wajib untuk sesi atau workflow yang bisa terputus/panjang |
| Log keputusan | Ya | Untuk setiap dokumen hidup dan keputusan evolusioner |
| Quality assurance & evolusi | Ya secara default | Kedalaman mengikuti risiko; override wajib dicatat |

## Gate Rilis Master — FINAL v1.0.0

- [x] Fondasi arsitektur tersedia
- [x] Quality protocol tiga lapisan tersedia
- [x] Definition of Done tersedia
- [x] Acceptance tests tersedia
- [x] Pilot non-kreator tersedia
- [x] Behavioral audit dengan sesi agent nyata selesai — pilot-002-behavioral 2026-09-04, level Sedang, 14 sumber konteks, RECOVERY_TEST_LOG.md
- [x] Recovery test nyata selesai — FI-01 s/d FI-04 + FI-07 LULUS fail-closed, commit 6fcc371 sebagai checkpoint persisten, `tools/test_failure_injection.py` PASS
- [x] Executable fail-closed check lulus (4 skenario)
- [x] Pilot disetujui pengguna — disetujui 2026-09-04 (OUTPUT.md + RECOVERY_TEST_LOG.md + BEHAVIORAL_AUDIT_2026-09-04_PILOT_002.md)
- [x] Backup lokal terverifikasi — `tools/backup_verify.py` PASS, backup di `_meta/_internal/backups/backup_essential.zip`
- [x] Template bersih dirilis — `tools/build_template.py` PASS, template di `_meta/_internal/template_clean.zip`, AT-10 verified, docs di `_meta/TEMPLATE_RELEASE.md`
- [x] Platform awareness — `_meta/PLATFORM_LMARENA.md` fakta vs policy, bahasa kausal tidak bisa vs harus, tanam ke template & sistem turunan
- [x] PR #3 merged ke main via merge commit 5f9a162

## Risiko Utama

- Agent melewatkan konteks karena “relevan” tidak didefinisikan cukup deterministik.
- Perubahan quality protocol memperberat sistem tanpa meningkatkan hasil.
- Master dan template berkembang tidak sinkron.
- Audit historis disalahartikan sebagai instruksi aktif.
- Pilot struktural dianggap bukti produksi sebelum diuji pengguna.

## Log Evolusi

| Tanggal | Perubahan | Alasan | Bukti | Approval |
|---|---|---|---|---|
| 2026-09-03 | Menambahkan quality assurance tiga lapisan, pilot, dan acceptance tests | Menutup kebutuhan self-improvement dan verifikasi output | Audit dan pilot struktural | Pending review pengguna |
| 2026-09-04 | Behavioral audit nyata + recovery test nyata via pilot-002-behavioral | Menutup B-03 dan B-04 dari BEHAVIORAL_AUDIT_2026-09-03, memenuhi gate rilis behavioral & recovery | `sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral/OUTPUT.md`, `RECOVERY_TEST_LOG.md`, `_meta/_internal/BEHAVIORAL_AUDIT_2026-09-04_PILOT_002.md`, `tools/validate_repo.py PASS`, `tools/test_failure_injection.py PASS`, commit 6fcc371 | Menunggu approval pengguna |
| 2026-09-04 | Fix C-01 deterministik field Pekerjaan belum tersimpan + backup & template bersih + approval pilot | Maksimalisasi setelah approval: tutup fragile field, backup verify, template clean AT-10, semua gate rilis centang | `tools/validate_repo.py PASS` (14 refs checked), `tools/test_failure_injection.py PASS`, `tools/backup_verify.py PASS`, `tools/build_template.py PASS`, `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` update, `_meta/TEMPLATE_RELEASE.md` NEW | Disetujui pengguna 2026-09-04 |
| 2026-09-04 | Tambah PLATFORM_LMARENA.md + tanam ke sistem turunan + bahasa kausal tidak bisa vs harus | Menutup gap asumsi agent tentang lifecycle sesi lmarena (branch arena otomatis, tidak bisa push setelah merge, sesi bisa crash). Bedakan fakta platform (tidak bisa/otomatis) vs policy (harus/jangan + alasan kausal) agar asumsi agent tepat. Tanam ke SYSTEM_MANIFEST_TEMPLATE, 01_DISCOVERY, 02_PRINSIP, 00_CARA_PAKAI, WORKFLOW, QUALITY, manifest pilot & konten kreator | `tools/validate_repo.py PASS` (28 files, 16 docs, 37 refs), `tools/backup_verify.py PASS`, `tools/build_template.py PASS`, `_meta/PLATFORM_LMARENA.md` NEW, 8 file update dengan bahasa kausal | Disetujui pengguna 2026-09-04 |
