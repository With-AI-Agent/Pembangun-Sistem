# System Manifest — Meta-Sistem Pembangun Sistem

- **Status:** `master blueprint — under validation`
- **Versi:** `0.3.0-pilot`
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

## Gate Rilis Master

- [x] Fondasi arsitektur tersedia
- [x] Quality protocol tiga lapisan tersedia
- [x] Definition of Done tersedia
- [x] Acceptance tests tersedia
- [x] Pilot non-kreator tersedia
- [ ] Behavioral audit dengan sesi agent nyata selesai
- [ ] Recovery test nyata selesai
- [ ] Pilot disetujui pengguna
- [ ] Backup lokal terverifikasi
- [ ] Template bersih dirilis

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
