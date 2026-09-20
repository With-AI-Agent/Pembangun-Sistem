# DRAF TERSTAGING — 6 prompt Discovery detail `sistem-undangan`

| | |
|---|---|
| **Dibuat** | 2026-09-20, sesi `arena/01a0bca9-pembangun-sistem` (slot log 41) |
| **Status** | **DRAF TERSTAGING — belum di folder sistem, belum dijalankan** |
| **Dasar wewenang** | `sistem/sistem-undangan/00_RENCANA_KERANGKA.md` bagian 11 **langkah 6** + `_meta/01_DISCOVERY_LEVEL_0.md` bagian "Setelah selesai" **butir 3** |
| **Kenapa di sini, bukan di folder sistem** | Langkah 6 berbunyi *"**Sesudah merge**: tulis 6 prompt Discovery detail"* dan PR #74 **masih OPEN** (`mergeable_state=CLEAN`, head `3ea796a`) saat draf ini ditulis. Keputusan yang tercatat di log sesi: T-18 dijalankan **sesudah** PR #74 merge supaya **hanya satu garis** yang menyentuh folder itu. Preseden staging di `_meta/_internal/`: Log Keputusan `00_RENCANA_KERANGKA.md` 2026-09-17 — *"Draft ini ditulis di `_meta/_internal/`, bukan di folder sistem … Preseden: keputusan yang sama untuk DISKUSI_MENTAH."* |
| **Pindah ke mana** | Ke dalam folder sistem, subfolder `_sistem/` (preseden nama: `sistem/sistem-konten-kreator/_sistem/02_CHANNEL_DISCOVERY_PROMPT.md`). Satu commit, satu garis, sesudah merge. |

## Isi folder ini

| Berkas draf | Mengisi dokumen | Gerbang | Kategori approval |
|---|---|---|---|
| `PROMPT_DISCOVERY_01_IDENTITAS_PEMILIK.md` | `01_IDENTITAS_PEMILIK.md` (L1) | **G0** | Besar |
| `PROMPT_DISCOVERY_02_PROFIL_JENIS_ACARA.md` | `02_PROFIL_JENIS_ACARA.md` (L2) | **G1** | Besar |
| `PROMPT_DISCOVERY_05_DESAIN_DAN_FORMAT.md` | `05_DISCOVERY_DESAIN_PROMPT.md` (L3) | Tahap 3 SIKLUS | — |
| `PROMPT_DISCOVERY_06_ASET_DAN_G3.md` | `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` (lintas) | **G3** fail-closed | Besar |
| `PROMPT_DISCOVERY_09_PUBLISH_DAN_SERAH_TERIMA.md` | `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` | **G5** | Besar |
| `PROMPT_DISCOVERY_10_WEBSITE_INDUK.md` | `10_ARSITEKTUR_WEBSITE_INDUK.md` | — | Besar |

Lima dokumen lain **tidak** butuh prompt Discovery (kolom "Cara diisi" di masing-masing kerangka):
`03`, `04`, `11` = cukup template biasa; `07` = cukup template (risetnya sudah lengkap di bagian C
`00_RENCANA_KERANGKA.md`); `08` = cukup template + **1 keputusan pemilik** (lisensi Remotion).

## Bentuk yang diikuti

Pola `sistem/sistem-konten-kreator/_sistem/02_CHANNEL_DISCOVERY_PROMPT.md` **persis**: judul
`# … Discovery — Prompt` → baris `### Dipakai …` → `## Kapan pakai dokumen ini` → `## Prompt`
(blok kode yang **siap tempel** ke sesi lmarena) → `## Setelah selesai`. Setiap blok prompt memuat:
peran agent, perintah **baca repo dulu**, slot input mentah pemilik, larangan menyimpulkan prematur,
aturan **3–5 pertanyaan per giliran**, daftar hal yang harus tergali, insight sesudah tiap jawaban,
parkir ide sampingan, ringkasan checkpoint, dan **larangan menulis dokumen final sebelum pemilik
bilang "cukup, tulis draftnya"**.

## Jebakan yang ditemukan saat menyiapkan draf ini (belum tercatat di mana pun sebelumnya)

`sistem/sistem-undangan/_sistem/validate_system.py` memeriksa setiap dokumen kerangka dengan dua
syarat: memuat kata **`KERANGKA`** dan memuat bagian **`Log Keputusan`** — dengan alasan yang ditulis
sendiri oleh alatnya: anti-"kerangka yang menyamar jadi dokumen jadi".

**Akibatnya: mengisi dokumen kerangka yang pertama akan MEMERAHKAN validator sistem ini**, karena
banner `STATUS: KERANGKA — BELUM ADA ISI` harus dicabut supaya dokumen tidak membantah dirinya
sendiri (dan "satu berkas yang membantah dirinya sendiri adalah temuan review" — kalimat itu ada di
Log Keputusan `00_RENCANA_KERANGKA.md` 2026-09-17). Docstring alatnya sudah mengantisipasi:
*"Cakupan ini wajib diperluas saat Tahap naik ke `siap-pakai`."*

**Jadi pengisian dokumen pertama WAJIB satu commit dengan:** (a) perluasan cakupan
`_sistem/validate_system.py` (daftar dokumen kerangka menyusut saat dokumen lulus; pemeriksaan isi
ditambahkan untuk yang sudah terisi), dan (b) pembaruan `SYSTEM_MANIFEST.md` (Tahap/Versi) +
`STATUS.md`. Dicatat sebagai **T-69** di `_meta/DAFTAR_PEKERJAAN_TERBUKA.md` supaya tidak
ditemukan sebagai "kejutan" di tengah kerja.

**Catatan batas freeze:** keputusan pemilik 20 Sep 2026 (didelegasikan, diputuskan agent) membekukan
**meta level repo** (`_meta/` + `tools/`) sampai undangan pertama terbit. Validator **milik sistem**
(`sistem/sistem-undangan/_sistem/`) **tidak** ikut beku — ia bagian dari kerja domain, dan T-69 justru
mensyaratkan ia berubah bersama isi. Batas ini dinyatakan eksplisit supaya freeze-nya bisa ditegakkan
dan tidak jadi temuan "aturan yang membantah dirinya sendiri".
