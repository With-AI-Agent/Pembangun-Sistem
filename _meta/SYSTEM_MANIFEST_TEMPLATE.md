# System Manifest — [Nama Sistem]

> Manifest ini adalah kartu identitas dan kontrak navigasi sebuah sistem domain. Ini bukan pengganti dokumen instruksi atau living document.

## Identitas

- **Nama sistem:**
- **Tujuan utama:**
- **Pengguna/consumer:**
- **Pemilik keputusan:**
- **Versi:** `0.1.0`
- **Status:** `Proposed`
- **Tanggal dibuat:**
- **Audit terakhir:**
- **Quality protocol:** `QUALITY_ASSURANCE_AND_EVOLUTION.md` (default aktif)

## Bentuk Sistem

- **Bentuk:** [ ] Bertingkat  [ ] Flat  [ ] Siklus  [ ] Gabungan
- **Unit kerja utama:**
- **Kriteria satu unit selesai:**
- **Titik approval Besar:**
- **Titik approval Kecil:**

## Dokumen Navigasi

- **Entry point:**
- **Dokumen instruksi aktif:**
- **Living documents:**
- **Log keputusan:**
- **Ringkasan cadangan:**
- **Laporan audit:**

## Prinsip

| Prinsip meta-sistem | Berlaku? | Cara diterapkan | Alasan jika di-override |
|---|---|---|---|
| Hierarki | | | |
| Chaining | | | |
| Approval bertingkat | | | |
| Checkpoint & verifikasi | | | |
| Log keputusan | | | |

## Quality & Evolution

- **Lapisan self-audit sistem:**
- **Lapisan verifikasi output:**
- **Trigger audit:**
- **Level audit default:** Ringan / Sedang / Mendalam
- **Prosedur rollback:**
- **Override quality protocol:** Tidak ada / [jelaskan dan sertakan approval]

## Dependency dan Risiko

- **Dependency eksternal:**
- **Data yang wajib ada:**
- **Risiko utama:**
- **Batasan yang diketahui:**
- **Prosedur recovery:**

## Batasan Platform

- **Dipakai via lmarena?** Ya / Tidak
- **Jika Ya:** rujuk ke `_meta/PLATFORM_LMARENA.md` untuk fakta platform (branch arena otomatis dibuat, tidak bisa push setelah merge/close, sesi bisa crash). Terapkan checkpoint tiap tahap + checkpoint diskusi ringan jika diskusi >5 giliran mendekati keputusan. Alasan kausal: tanpa commit+push, sesi baru tidak bisa melanjutkan (FI-03); tanpa checkpoint diskusi, diskusi panjang bisa hilang saat crash.
- **Jika Tidak:** tulis alasan override eksplisit (misal: sistem ini manual 100% Obsidian, tidak via agent) + approval

## Acceptance

- [ ] Semua dokumen wajib tersedia
- [ ] Semua dependency valid
- [ ] Status dan versi sudah diperbarui
- [ ] Approval yang diperlukan sudah ada
- [ ] Audit terakhir tercatat
- [ ] Ringkasan cadangan sinkron
