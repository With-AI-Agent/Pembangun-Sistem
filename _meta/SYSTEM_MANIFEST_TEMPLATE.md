# System Manifest — [Nama Sistem]

> Manifest ini adalah kartu identitas dan kontrak navigasi sebuah sistem domain. Ini bukan pengganti dokumen instruksi atau living document.

## Identitas

- **Nama sistem:**
- **Tujuan utama:**
- **Pengguna/consumer:**
- **Pemilik keputusan:**
- **Versi:** `0.1.0`
- **Tahap:** kerangka — ubah ke `siap-pakai` saat sistem siap dipakai (cek W-01/W-02/W-03 kembali ketat; lihat `03_KONTRAK_WARISAN.md` bagian "Tahap pembangunan")
- **Status:** `Proposed`
- **Tanggal dibuat:**
- **Audit terakhir:**
- **Quality protocol:** dokumen QA turunan DI DALAM folder sistem ini (butir W-06 — wajib self-contained). Rujukan ke `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` hanyalah provenance (asal aturan), BUKAN aturan aktif (sistem harus tetap berfungsi penuh saat foldernya diunduh jadi repo sendiri — lihat `03_KONTRAK_WARISAN.md`)

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
- **Pegangan pengguna:** [`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` di dalam folder sistem — WAJIB, ikuti `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`]

## Prinsip

| Prinsip meta-sistem | Berlaku? | Cara diterapkan | Alasan jika di-override |
|---|---|---|---|
| Hierarki | | | |
| Chaining | | | |
| Approval bertingkat | | | |
| Checkpoint & verifikasi | | | |
| Log keputusan | | | |
| Quality assurance & evolusi (prinsip 6) | | | |

## Warisan (Kontrak)

Status butir `03_KONTRAK_WARISAN.md` untuk sistem ini — salin dari bagian "Warisan" di `00_RENCANA_KERANGKA.md`; default SEMUA diterapkan, yang di-override wajib menyebut approval pengguna:

| Butir | Status (diterapkan / override) | Letak di folder sistem | Override? |
|---|---|---|---|
| W-01 pegangan | | | |
| W-02 LOG_SESI | | | |
| W-03 field checkpoint STATUS | | | |
| W-04 manifest | | | |
| W-05 log keputusan | | | |
| W-06 QA 3-lapis | | | |
| W-07 fakta platform | | | |
| W-08 approval bertingkat | | | |
| W-09 ringkasan cadangan | | | |

Baris `override`: isi kolom Override dengan `alasan: ...; dampak: ...; tanggal: YYYY-MM-DD; approval: <kutipan keputusan pengguna>` — override tanpa keempatnya = error validator (lihat `03_KONTRAK_WARISAN.md`).

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
- **Jika Ya:** rujuk ke `_meta/PLATFORM_LMARENA.md` untuk fakta platform (branch arena otomatis dibuat, tidak bisa push setelah merge/close, sesi bisa crash). Terapkan checkpoint tiap tahap + **log sesi berkelanjutan (`LOG_SESI`)** — turunkan aturannya ke dalam folder sistem (self-contained). Alasan kausal: tanpa commit+push, sesi baru tidak bisa melanjutkan (FI-03); tanpa log sesi, konteks sesi (keputusan, koreksi, fakta penting) hilang permanen saat crash karena agent sesi baru tidak punya akses ke chat lama.
- **Jika Tidak:** tulis alasan override eksplisit (misal: sistem ini manual 100% Obsidian, tidak via agent) + approval

## Acceptance

- [ ] Semua dokumen wajib tersedia
- [ ] Semua dependency valid
- [ ] Status dan versi sudah diperbarui
- [ ] Approval yang diperlukan sudah ada
- [ ] Audit terakhir tercatat
- [ ] Ringkasan cadangan sinkron
- [ ] Pegangan pengguna tersedia di dalam folder sistem (prompt pembuka + prompt penutup)
