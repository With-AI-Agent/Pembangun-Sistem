# System Manifest — Meta-Sistem Pembangun Sistem

- **Status:** `Released — v1.4.0`
- **Versi:** `1.4.0`
- **Tujuan:** merancang, membangun, mengaudit, memperbaiki, dan memelihara sistem kerja untuk berbagai domain.
- **Consumer:** pengguna dan agent yang bekerja pada repository.
- **Pemilik keputusan:** pengguna
- **Entry point pengguna:** `PANDUAN_PENGGUNA.md` (+ prompt siap-salin: `PROMPT_ENTRI_UNIVERSAL.md` — blok harus identik)
- **Entry point agent:** `00_CARA_KERJA_META.md`
- **Kontrak warisan:** `03_KONTRAK_WARISAN.md` — butir W-01…W-09 yang otomatis tertanam di semua sistem; ditegakkan `tools/validate_repo.py` berbasis INDEKS
- **Regression tools:** `tools/validate_repo.py`, `tools/test_failure_injection.py`, `tools/backup_verify.py`, `tools/build_template.py`, `tools/checkpoint_core.py` (parser bersama fail-closed — diimpor validator & FI, bukan dijalankan langsung)
- **Index:** `INDEKS_SISTEM.md`
- **Quality protocol:** `QUALITY_ASSURANCE_AND_EVOLUTION.md`
- **Definition of done:** `DEFINITION_OF_DONE.md`
- **Acceptance tests:** `ACCEPTANCE_TESTS.md`
- **Checkpoint/recovery:** `PROTOKOL_CHECKPOINT_RECOVERY.md`
- **Review independen (sesi lain):** `PROTOKOL_REVIEW_INDEPENDEN.md` (v1.4.0 — pemutus eksternal untuk gate/klaim permanen; reviewer memverifikasi dari artefak, tidak ada auto-merge)
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
| Kontrak warisan (pegangan, LOG_SESI, checkpoint, manifest, W-01…W-09) | **Ya — default aktif** | Dirawat di `03_KONTRAK_WARISAN.md`; ditegakkan mekanis oleh `tools/validate_repo.py` untuk semua sistem terdaftar; penonaktifan hanya via approval pengguna tercatat |

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

## Gate Rilis v1.3.0 — Audit Menyeluruh 5 Sep 2026 (19 temuan M-01…M-19)

- [x] Kontrak Warisan dibuat (`03_KONTRAK_WARISAN.md`) + ditanam ke 00/01/DoD/manifest-template/TEMPLATE_RELEASE + ACCEPTANCE (AT-14) — permintaan eksplisit pengguna 5 Sep ("hal wajib harus otomatis tertanam juga pada sistem yang AKAN dibangun; desain: kontrak default-aktif" — dipilih dari 3 opsi, 16:50 WIB)
- [x] M-01 ditutup: `build_template.py` + `backup_verify.py` berbasis glob semua `_meta/*.md`/`tools/*.py` + guard kelengkapan (build GAGAL bila rujukan aktif tidak ikut) + backup verifikasi byte penuh
- [x] M-02/M-03 ditutup: parser fail-closed disatukan dengan format nyata (bold+backtick toleran, field-absen = tidak aman; pasca review: parser bersama `checkpoint_core.py` + format protokol + penolakan duplikat/kutipan) + konsistensi unit nyata; field checkpoint diturunkan ke `T6_STATUS.md` + STATUS deck presentasi (nilai template dinormalkan exact `Tidak ada`); C-01 divalidator digeneralisasi ke semua sistem via INDEKS (unit diharapkan, bukan hanya ditemukan)
- [x] M-04…M-08, M-10, M-14…M-17 ditutup (perintah `gh pr list --state all`; langkah LOG_SESI di entry point 00; baris LOG_SESI di laporan awal; tools/ didaftarkan; lensa audit + klasifikasi dikodifikasi di QA protocol; Q-O2/Q-O3 ditutup dengan aturan minimal; "5 hal"; manifest-dalam-PR; PROMPT_ENTRI root; banner manifest template; path panduan di PANDUAN root)
- [x] Regresi penuh hijau: validate_repo PASS 0-warning (25 required); failure-injection 29 skenario (12 sintetis + 4 unit nyata + 13 regresi review R1–R7; 24 skenario di ekstrak template); template build + smoke test ekstrak PASS (4 warning normalisasi tersisa — histori master berlabel, dipin di FI); backup verify PASS (byte-exact, 30 file); diff blok prompt pembuka PANDUAN↔PROMPT_ENTRI identik
- [x] Review independen PR #11 dijawab — 16 temuan (7×P1, 7×P2, 1×P3, 1×P4) semua diperbaiki di PR ini; 4 PASS palsu yang terbukti (hapus file inti / folder tak terdaftar / baris INDEKS tanpa backtick / field duplikat) di-pin sebagai regresi R1–R7 (perincian: Log Evolusi baris terakhir + laporan audit Addendum 2)
- [ ] M-18 (hapus 2 branch yatim yang sudah diarsipkan) — BUKAN wewenang agent; menunggu keputusan pengguna

## Risiko Utama

- Agent melewatkan konteks karena “relevan” tidak didefinisikan cukup deterministik.
- Perubahan quality protocol memperberat sistem tanpa meningkatkan hasil.
- Master dan template berkembang tidak sinkron. **PERNAH TERJADI (M-01, 5 Sep 2026)** dan kini dijaga guard kelengkapan `build_template.py` (rujukan aktif yang tidak ikut template = build gagal) — daftar INCLUDE/ESSENTIAL manual tidak dipakai lagi.
- Audit historis disalahartikan sebagai instruksi aktif.
- Pilot struktural dianggap bukti produksi sebelum diuji pengguna.

## Log Evolusi

| Tanggal | Perubahan | Alasan | Bukti | Approval |
|---|---|---|---|---|
| 2026-09-03 | Menambahkan quality assurance tiga lapisan, pilot, dan acceptance tests | Menutup kebutuhan self-improvement dan verifikasi output | Audit dan pilot struktural | Pending review pengguna |
| 2026-09-04 | Behavioral audit nyata + recovery test nyata via pilot-002-behavioral | Menutup B-03 dan B-04 dari BEHAVIORAL_AUDIT_2026-09-03, memenuhi gate rilis behavioral & recovery | `sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral/OUTPUT.md`, `RECOVERY_TEST_LOG.md`, `_meta/_internal/BEHAVIORAL_AUDIT_2026-09-04_PILOT_002.md`, `tools/validate_repo.py PASS`, `tools/test_failure_injection.py PASS`, commit 6fcc371 | Menunggu approval pengguna |
| 2026-09-04 | Fix C-01 deterministik field Pekerjaan belum tersimpan + backup & template bersih + approval pilot | Maksimalisasi setelah approval: tutup fragile field, backup verify, template clean AT-10, semua gate rilis centang | `tools/validate_repo.py PASS` (14 refs checked), `tools/test_failure_injection.py PASS`, `tools/backup_verify.py PASS`, `tools/build_template.py PASS`, `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` update, `_meta/TEMPLATE_RELEASE.md` NEW | Disetujui pengguna 2026-09-04 |
| 2026-09-04 | Tambah PLATFORM_LMARENA.md + tanam ke sistem turunan + bahasa kausal tidak bisa vs harus | Menutup gap asumsi agent tentang lifecycle sesi lmarena (branch arena otomatis, tidak bisa push setelah merge, sesi bisa crash). Bedakan fakta platform (tidak bisa/otomatis) vs policy (harus/jangan + alasan kausal) agar asumsi agent tepat. Tanam ke SYSTEM_MANIFEST_TEMPLATE, 01_DISCOVERY, 02_PRINSIP, 00_CARA_PAKAI, WORKFLOW, QUALITY, manifest pilot & konten kreator | `tools/validate_repo.py PASS` (28 files, 16 docs, 37 refs), `tools/backup_verify.py PASS`, `tools/build_template.py PASS`, `_meta/PLATFORM_LMARENA.md` NEW, 8 file update dengan bahasa kausal | Disetujui pengguna 2026-09-04 |
| 2026-09-05 | v1.0.0 → v1.1.0: **pegangan pengguna jadi WAJIB untuk semua sistem** — template baru `PANDUAN_PENGGUNA_TEMPLATE.md`; aturan ditanam ke 00_CARA_KERJA (prinsip + langkah 8 alur sistem baru), SYSTEM_MANIFEST_TEMPLATE (field + gate acceptance), 01_DISCOVERY (langkah 6), DEFINITION_OF_DONE (checklist sistem domain); prompt penutup sesi ditambahkan ke `PANDUAN_PENGGUNA.md` root; cakupan `tools/validate_repo.py` diperluas ke `sistem-presentasi/` (AP-11) | Permintaan pengguna 5 Sep 2026: tiap sistem harus bisa dipakai cukup dengan SATU prompt pembuka universal (agent otomatis terorientasi penuh: konteks, cara kerja, ketentuan, cek PR menggantung) + butuh prompt penutup sesi; standar = sama mudahnya dengan meta-sistem ini | Perubahan additive (template + checklist + 1 langkah alur); regression: sistem konten kreator sudah patuh (punya `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md`; prompt penutup ditambahkan), sistem presentasi dibuat patuh di sesi yang sama (v0.3.0) | Disetujui pengguna 2026-09-05 (sesi `arena/01a0706d`). Rollback: revert commit perubahan ini (additive, tidak ada migrasi data) |
| 2026-09-05 | v1.1.0 → v1.2.0: **log sesi berkelanjutan (`LOG_SESI`) menggantikan "checkpoint diskusi ringan >5 giliran"** — mekanisme ingatan persisten per sesi untuk mitigasi crash: template format `TEMPLATE_LOG_SESI.md`, policy di `PROTOKOL_CHECKPOINT_RECOVERY.md` + `PLATFORM_LMARENA.md` (P2) + `02_PRINSIP_UNIVERSAL` + `00_CARA_KERJA` (kebiasaan) + `NEXT_SESSION_PROMPT` + `SYSTEM_MANIFEST_TEMPLATE` + `PANDUAN_PENGGUNA_TEMPLATE` (prompt pembuka: langkah recovery log; prompt penutup: langkah menutup log) + `DEFINITION_OF_DONE` (checklist) + `ACCEPTANCE_TESTS` (AT-13). Diturunkan ke sistem-presentasi (v0.4.0, `_sistem/11_LOG_SESI.md`) & sistem-konten-kreator (section di `00_CARA_PAKAI_SISTEM.md` + prompt di panduannya) | Masalah nyata pengguna 5 Sep 2026: sesi sering crash (error, tidak bisa dibuka lagi); konteks penting (keputusan, koreksi, fakta — tidak hanya diskusi) hilang karena belum jadi file; agent sesi baru tidak punya akses ke chat lama. Aturan lama (ambang >5 giliran + judgment "mendekati keputusan") digantikan karena sebelum ambang tercapai tidak ada yang tercatat. Filter anti-bising (catat yang penting, bukan dump chat) adalah bagian dari policy — menjawab kekhawatiran overkill pengguna: biaya over-recording = detik; under-recording = jam | Perubahan policy (mengganti aturan lama yang ada di 13 titik aktif — semua diupdate konsisten; dokumen historis/pilot sengaja tidak disentuh). Regression: semua tool tetap PASS (validator meta 38 files, failure-injection 4 skenario, validate_system, qa_deck); mekanisme langsung diuji live di sesi yang sama (`LOG_SESI_2026-09-05.md` di root repo) | Disetujui pengguna 2026-09-05 (sesi `arena/01a0706d`: "Ya" + ekstensi "semua sistem harus mengandung mekanisme ini" + generalisasi "bukan hanya saat diskusi"). Rollback: revert commit v1.2.0 (aturan lama masih ada di git history; file LOG_SESI yang sudah dibuat tidak membahayakan — arsip) |
| 2026-09-05 | v1.2.0 → **v1.3.0: audit menyeluruh meta + kontrak warisan** — laporan `_meta/_internal/AUDIT_META_SISTEM_2026-09-05.md` (18 temuan M-01…M-18: 3×P1, 9×P2, 6×P3; klasifikasi B/A/G/N/P). Ditambah: `03_KONTRAK_WARISAN.md` (W-01…W-09, default aktif — penonaktifan saja yang butuh konfirmasi pengguna; ditanam ke 00/01/02/DoD/manifest-template/TEMPLATE_RELEASE/ACCEPTANCE AT-14 + ditegakkan validator berbasis INDEKS). Diubah: `build_template.py` & `backup_verify.py` dari daftar statis → glob dinamis + guard kelengkapan + verifikasi byte penuh; `test_failure_injection.py` parser toleran-format + skenario format nyata + field-absen + konsistensi unit riil; `validate_repo.py` refactor (required dari glob, cek pegangan/LOG_SESI/field-checkpoint per sistem via INDEKS, whitelist artefak → baseline 0-warning); `PLATFORM_LMARENA` P3 + `PROTOKOL` recovery #4 → `gh pr list --state all`; entry point 00 dapat langkah LOG_SESI + daftar tools; `SESSION_REPORT_TEMPLATE` dapat baris LOG_SESI; `QUALITY_ASSURANCE_AND_EVOLUTION` dapat tabel 7 lensa + klasifikasi temuan wajib (M-08); Q-O2 (kriteria alasan sah) & Q-O3 (interval Waktu pembaruan) DITUTUP di PROTOKOL; `01_DISCOVERY` "5 hal" + bagian Warisan + manifest-dalam-PR-yang-sama; meta kini punya `PROMPT_ENTRI_UNIVERSAL.md` root (standar 2-file berlaku utk meta sendiri); `TEMPLATE_RELEASE` diselaraskan + smoke test wajib; salinan manifest di template diberi banner (M-16). Turunan: `sistem-presentasi` 0.4.1 (field checkpoint di `T6_STATUS.md`+STATUS deck, wording provenance manifest, ringkasan cadangan disinkronkan), `sistem-konten-kreator` wording provenance + ringkasan cadangan disinkronkan | Permintaan pengguna 5 Sep 2026: audit maksimal tanpa cacat + "hal wajib harus otomatis tertanam pada sistem yang AKAN dibangun, bukan hanya yang sudah ada"; desain kontrak-berhenti-hanya-untuk-override dipilih pengguna (16:50); delegasi penuh "lakukan yang terbaik" untuk scope & mode eksekusi (17:00) | `validate_repo.py` PASS 0-warning (regression), FI 11 skenario PASS (7 sintetis + 4 unit nyata — label lama "6 sintetis/10 skenario" salah hitung, dikoreksi 5 Sep), template build+smoke ekstrak PASS, backup byte-exact PASS; bukti per-temuan di laporan audit (M-01/M-02 diukur langsung sebelum-sesudah) | Disetujui pengguna 5 Sep 2026 via delegasi scope+mode (jawaban ask_user 16:50 & 17:00); review isi PR = approval final pra-merge. Rollback: revert commit v1.3.0 (dapat per layer: tools / meta / turunan — semua additive, tanpa migrasi data); file `LOG_SESI` & arsip tak terdampak; tools: parser diperluas formatnya (pengetatan duplikat/kutipan menyusul di baris review) |
| 2026-09-05 | **Perbaikan hasil review independen PR #11 (16 temuan F1–F16)** — `tools/checkpoint_core.py` BARU (parser bersama + inventaris inti statis `CORE_REQUIRED`); validator: parse INDEKS ketat (backtick+exact, tanpa except substring), sistem tak terdaftar = error, unit STATUS diharapkan per sistem terdaftar, template STATUS harus parse exact, Warisan 9 butir wajib + override tervalidasi + `Tahap: kerangka/siap-pakai`, resolusi rujukan di-scope per-sistem, URI dikecualikan; FI: 29 skenario (duplikat field, format protokol, fence/kutipan, + regresi R1–R7 = mutasi reviewer dipin permanen); build_template: transformasi bootstrap self-contained (idempotent) + guard berbasis core; backup: core inventory; 3 template STATUS dinormalkan (nilai exact `Tidak ada`, petunjuk dipindah); `03_KONTRAK_WARISAN`: bagian "Tahap pembangunan & override tervalidasi"; `02_PRINSIP`: precedence SELURUH W-01…W-09; PROTOKOL: Q-O2 "alasan ≠ approval" + parser bersama; INDEKS: versi `0.4.1`/`0.3.2-warisan-sync`/`1.3.0`; manifest presentasi: self-audit via validate_system.py lokal folder (klaim self-contained dikoreksi) + Q-O2/Q-O3 selaras + Tahap; manifest KK: `Tahap` + klaim F7 dikoreksi (perubahan aturan `00` diakui, clean-run acceptance dijadwalkan sesi berikutnya); Discovery "kelima"; ringkasan KK 12 dokumen; TEMPLATE_RELEASE: daftar normalisasi 4 warning dipin + transformasi | Review independen (sesi agent terpisah, VERDICT REQUEST_CHANGES) membuktikan PASS palsu: required-list glob-derived (hapus sumber → lolos), except substring "pilot", unit discovery (hapus STATUS → cakupan 0), first-match parser (field ganda/kutipan lolos), 2 dependensi aktif hilang di template, klaim self-containment presentasi & "aturan 00 tidak berubah" salah | `validate_repo.py` PASS 0-warning (25 required); FI 29 skenario PASS (master) / 24 (ekstrak); backup 30 file byte-exact; template build + smoke ekstrak PASS (persis 4 warning normalisasi); `validate_system.py` presentasi PASS; per-temuan: laporan audit Addendum 2 + body PR | Reviewer independen (sesi lain) + penulis; dikerjakan di branch PR #11 yang sama (belum merged). Rollback: revert commit layer review ini |
| 2026-09-06 | v1.3.0 → **v1.4.0: Protokol Review Independen (sesi lain)** — file baru `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` (8 prinsip, level trigger L1/L2/L3, anatomi prompt reviewer, penulisan hasil, warisan ke sistem domain); rujukan 1 baris di `QUALITY_ASSURANCE_AND_EVOLUTION.md` (lapisan eksternal, di bawah tabel kedalaman pemeriksaan); file didaftarkan di `INDEKS_SISTEM.md` + pointer di manifest ini. Turunan: `sistem-konten-kreator` v0.3.5 (dokumen protokol varian KK + rujukan di `START_DI_SINI`/QA/`ACCEPTANCE_TESTS` poin 7 + varian 1-baris di panduan; dokumen `00`/`05`/`06` TIDAK diubah → regresi AT-KK tidak terpicu), `sistem-presentasi` rujukan + level trigger 3 baris di `ACCEPTANCE_TESTS.md`, `sistem-pilot-catatan-belajar` mewarisi via meta tanpa perubahan file (dicatat di log sesi — belum punya acceptance test) | Permintaan pengguna 6 Sep 2026 pasca-F7: verifikasi akhir pekerjaan berdampak permanen dilakukan SESI LAIN (yang mengerjakan tidak memutus; pola pencatat ≠ subjek). Implementasi prompt reviewer contoh sudah terbukti di `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md` Run 7/8 (rujukan, bukan salinan narasi) | `validate_repo.py` PASS 0-warning (26 required); `test_failure_injection.py` 29 skenario PASS; grep klausul expected result KK di jalur orientasi + file protokol baru = 0 hit di luar `ACCEPTANCE_TESTS.md`/`ACCEPTANCE_TEST_LOG.md`; diff `00`/`05`/`06` KK = 0 baris | Pending review pengguna — PR tanpa auto-merge; trigger review **L1** (perubahan struktural `_meta/` + klaim gate). Rollback: revert commit v1.4.0 (semua additive, tanpa migrasi data) |
