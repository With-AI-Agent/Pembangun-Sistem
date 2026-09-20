# 6 prompt Discovery detail — indeks dan aturan pakainya

| | |
|---|---|
| **Fungsi folder ini** | Instrumentasi: prompt **generator** yang dipakai untuk menggali isi 6 dokumen sistem ini lewat diskusi dengan pemilik. Bukan isi sistemnya. |
| **Dasar** | `00_RENCANA_KERANGKA.md` bagian 11 **langkah 6** + bagian **7** (kolom "Perlu prompt Discovery detail?"), dan metode Discovery induk di area master (01_DISCOVERY_LEVEL_0.md, bagian "Setelah selesai" butir 3) |
| **Dibuat** | 2026-09-20 · draf terstaging lebih dulu di area internal master, dipindahkan ke sini sesudah PR #74 merge (`ed3abb6`, 06:01:32 UTC) — dicatat sebagai **T-70** |
| **Bentuk** | Mengikuti prompt Discovery sistem lain yang sudah jadi (channel discovery di sistem konten kreator) **persis**: judul → baris `### Dipakai …` → `## Kapan pakai dokumen ini` → `## Prompt` (blok kode siap tempel) → `## Setelah selesai` |

## Isi

| Berkas | Mengisi dokumen | Lapis | Gerbang | Kategori approval |
|---|---|---|---|---|
| `PROMPT_DISCOVERY_01_IDENTITAS_PEMILIK.md` | `01_IDENTITAS_PEMILIK.md` | L1 | **G0** | Besar |
| `PROMPT_DISCOVERY_02_PROFIL_JENIS_ACARA.md` | `02_PROFIL_JENIS_ACARA.md` | L2 | **G1** | Besar |
| `PROMPT_DISCOVERY_05_DESAIN_DAN_FORMAT.md` | `05_DISCOVERY_DESAIN_PROMPT.md` | L3 | Tahap 3 SIKLUS | — |
| `PROMPT_DISCOVERY_06_ASET_DAN_G3.md` | `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` | lintas | **G3** fail-closed | Besar |
| `PROMPT_DISCOVERY_09_PUBLISH_DAN_SERAH_TERIMA.md` | `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` | lintas | **G5** | Besar |
| `PROMPT_DISCOVERY_10_WEBSITE_INDUK.md` | `10_ARSITEKTUR_WEBSITE_INDUK.md` | lintas | — | Besar |

**Urutan yang wajib:** 01 → 02 → (06 sebelum aset apa pun dijanjikan ke client) → 10 → 09 → 05 per
undangan. Alasannya ada di tiap berkas: L2 mewarisi L1, cara publish ditentukan arsitektur induk, dan
G3 harus ada sebelum produksi supaya penolakan aset tidak terjadi di tengah jalan.

**Lima dokumen lain TIDAK butuh prompt Discovery** (kolom "Cara diisi" di masing-masing kerangka):
`03_TEMPLATE_DATA_ACARA.md`, `04_TEMPLATE_BRIEF_UNDANGAN.md`, `11_AMPLOP_DIGITAL.md` = cukup template
biasa; `07_SPESIFIKASI_CETAK_PREPRESS.md` = cukup template (risetnya sudah lengkap di bagian C
`00_RENCANA_KERANGKA.md`); `08_PIPELINE_VIDEO.md` = cukup template + **1 keputusan pemilik** (lisensi
Remotion — berbayar pada ≥4 karyawan).

## Jebakan yang WAJIB dibaca sebelum mengisi dokumen pertama (T-69)

`_sistem/validate_system.py` menuntut setiap dokumen kerangka memuat kata **KERANGKA** dan bagian
**Log Keputusan** — alasan yang ditulis alatnya sendiri: anti-"kerangka yang menyamar jadi dokumen
jadi". Padahal banner `STATUS: KERANGKA — BELUM ADA ISI` **wajib dicabut** saat dokumen diisi, supaya
dokumen tidak membantah dirinya sendiri.

**Akibatnya: mengisi dokumen kerangka yang pertama akan memerahkan validator sistem ini.** Itu bukan
kerusakan — docstring alatnya sudah mengantisipasi (*"Cakupan ini wajib diperluas saat Tahap naik ke
`siap-pakai`"*) — tetapi tanpa catatan akan dikira kegagalan. Karena itu pengisian dokumen pertama
**wajib satu commit** dengan:

1. perluasan cakupan `_sistem/validate_system.py` (daftar dokumen kerangka menyusut saat dokumen lulus;
   pemeriksaan isi ditambahkan untuk yang sudah terisi),
2. pembaruan `SYSTEM_MANIFEST.md` (field **Tahap** dan **Versi**),
3. pembaruan `STATUS.md`.

## Batasan yang dinyatakan jujur (W-07), jangan disembunyikan

Beberapa prompt di folder ini menyuruh agent membaca **riset yang tersimpan di area internal master**
(bagian A = baseline 7 situs pasar undangan Indonesia; bagian P = hasil uji upscaling; bagian H = plafon
free tier Cloudflare). Area itu **master-only**: ia **tidak ikut** kalau folder sistem ini diunduh atau
dipisah jadi repo berdiri sendiri.

Yang sudah dilakukan untuk menurunkan risikonya: angka-angka yang menentukan **dikutip langsung di dalam
prompt-nya** (ambang G3, hasil pengukuran PSNR, plafon D1/KV/R2), jadi prompt tetap bisa dijalankan tanpa
membuka area master. Yang **tidak** bisa diatasi dari dalam folder ini: riset baseline bagian A untuk
prompt 02 — karena itu prompt 02 memerintahkan *"PAKAI ITU, jangan riset ulang dari nol"*, dan kalau
area master tidak tersedia, agent yang menjalankannya **wajib mengatakan bahwa baseline-nya tidak ada**
lalu menggali dari pemilik, bukan mengarang angka pasar.

## Yang tidak boleh dilakukan saat menjalankan prompt-prompt ini

- **Menulis isi dokumen sebelum pemilik bilang "cukup, tulis draftnya"** — semua prompt memuat larangan ini.
- **Menilai sendiri kelulusan pegangan/gerbang** — Syarat 4 Standar Kelulusan Manual melarang penulis menilai sendiri; yang dicatat adalah keadaannya dan apa yang masih kurang.
- **Mengarang angka** — setiap angka di dokumen 06 dan 10 harus menyebut sumbernya di dalam dokumennya sendiri.
- **Menyalin materi master-only ke folder ini** — aturan area master menyatakan menyalin adalah pelanggaran yang sama dengan merujuk; bentuk yang benar adalah **provenance tanpa backtick**.
- **Membuat salinan berlabel dari dokumen master yang HIDUP** (daftar pekerjaan terbuka, metode Discovery induk) — salinan berlabel adalah solusi untuk dependensi operasional, dan dokumen-dokumen itu bukan dependensi operasional prompt di folder ini: ia **penunjuk konteks**. Menyalin dokumen hidup akan melahirkan sumber kebenaran kedua yang basi — persis penyakit yang membuat indeks sistem sempat menulis PR yang sudah merged sebagai masih menunggu. Karena itu rujukannya ditulis sebagai **provenance tanpa backtick**.
