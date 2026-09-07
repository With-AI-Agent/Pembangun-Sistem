# Ringkasan Sistem — Sistem Konten Kreator
### Untuk sesi Claude chat biasa (cadangan lmarena Agent). Dokumen ini BUKAN sistem itu sendiri — cuma ringkasan supaya Claude paham konteks tanpa perlu upload semua file.

## Sistem ini tentang apa
Sistem kerja untuk konten kreator berbasis AI — dari nentuin channel mau ngomongin apa, membangun karakter/elemen visual yang konsisten, sampai produksi konten harian yang siap publish. Dijalankan lewat lmarena Agent yang terhubung ke repo GitHub, bisa baca-tulis file dan generate gambar langsung (tidak bisa generate video).

## Bentuk dasar
**Gabungan Bertingkat + Siklus.** Bertingkat di level struktural: Brand Core (lintas semua channel) → Channel Brief (1 niche/positioning) → Model Konten Brief (1 cara produksi/format dalam channel itu). Siklus di level produksi harian: Pipeline 6 Tahap (Ideation → Konsep → Naskah → Breakdown Visual → Generate Asset → Assembly) yang diulang tiap kali bikin 1 konten baru.

## Struktur folder saat ini (disinkronkan 5 Sep 2026 — sebelumnya menunjuk lokasi lama, temuan M-09)
```
sistem-konten-kreator/
├── PROMPT_ENTRI_UNIVERSAL.md      ← prompt pembuka siap tempel (blok identik dgn panduan)
├── SYSTEM_MANIFEST.md             ← identitas + gate + Log Evolusi + tabel Warisan
├── QUALITY_ASSURANCE_AND_EVOLUTION.md   (turunan self-contained; induk _meta = provenance)
├── ACCEPTANCE_TESTS.md / ACCEPTANCE_TEST_LOG.md
├── PROTOKOL_REVIEW_INDEPENDEN.md        ← varian KK dari _meta/PROTOKOL_REVIEW_INDEPENDEN.md (meta v1.4.0, 6 Sep)
├── panduan/PANDUAN_PENGGUNA.md    ← pegangan pengguna (subfolder panduan/)
├── _sistem/  (12 dokumen: START_DI_SINI, 00_CARA_PAKAI_SISTEM [LOG_SESI + fakta
│            platform inline + 4 aturan recovery self-contained], 01_BRAND_CORE,
│            02_CHANNEL_DISCOVERY_PROMPT, 03_TEMPLATE_CHANNEL_BRIEF, 04_CHARACTER_BUILDER_KIT,
│            05_CONTENT_PRODUCTION_PIPELINE, 06_PROMPT_LIBRARY, 07_MODEL_KONTEN_DISCOVERY_PROMPT,
│            08_TEMPLATE_MODEL_KONTEN_BRIEF, 09_AUDIT_MIGRASI_GITHUB_AGENT [reference_only],
│            STATUS_TEMPLATE [field checkpoint deterministik])
├── channel-fixture-narasi-sejarah/          ← fixture uji (BUKAN channel produksi)
└── _produksi-aktif/fixture-…/               ← unit uji recovery (STATUS + naskah-draft)
```
11 dokumen `_sistem/` + pegangan 2-file + manifest + QA turunan + acceptance suite. Setelah dijalankan, sistem ini menghasilkan folder tambahan di repo produksi sebenarnya: `channel-[nama]/`, `konsistensi-lintas-channel/`, `_produksi-aktif/` — skeleton lengkap di `00_CARA_PAKAI_SISTEM.md` bagian "Struktur Repo".

## Prinsip yang berlaku
Mengikuti semua 5 Prinsip Universal dari `_meta/02_PRINSIP_UNIVERSAL.md` TANPA override — sistem ini justru yang jadi SUMBER dari prinsip-prinsip itu (dipilah dari sini ke level universal setelah terbukti works). Tambahan spesifik-domain: Pemisahan Konsistensi Visual vs Non-Visual (khusus konten kreator, tidak universal).

## Status sekarang
**`0.3.5` — kandidat sistem contoh; audit P0+P1 tertutup; recovery teruji nyata.** **F7 DITUTUP 6 Sep 2026** — AT-KK-05 / Run 7 + AT-KK-05b / Run 8 **LULUS** pada `0.3.4`, clean run di sesi agent baru (bukti: `ACCEPTANCE_TEST_LOG.md`; status/pointer saja, sesuai pola 6a). v0.3.5 (6 Sep): protokol review independen diwariskan dari meta v1.4.0 — file `PROTOKOL_REVIEW_INDEPENDEN.md` di root sistem + rujukan di `START_DI_SINI`/QA/`ACCEPTANCE_TESTS` (poin 7)/panduan; aturan 00/05/06 tidak berubah. Sisa gate: Brand Core channel nyata belum ada; pilot end-to-end (L-04) butuh 1 channel terisi penuh; acceptance AT-KK-01/02/03/03b/04/06/07/08 belum diuji; L-03 terbuka. Kontrak warisan meta v1.3.0: tabel Warisan W-01…W-09 tercatat di `SYSTEM_MANIFEST.md`, tanpa override.

## PENTING — hasil kerja sesi ini akan dibawa ke mana
Hasil dari sesi Claude ini akan di-paste manual oleh pengguna ke lokasi yang sesuai di Obsidian (sync otomatis ke GitHub via plugin git). Pastikan format/struktur yang dihasilkan KOMPATIBEL dengan 11 dokumen yang sudah ada — cek dulu dokumen terkait yang diupload bersama ringkasan ini sebelum menulis apa pun. Karena sistem ini mendekati status contoh resmi (gate pemakaian nyata masih terbuka), perubahan apapun ke sistem ini sebaiknya dianggap REVISI terhadap sesuatu yang sudah teruji — pertimbangkan matang-matang sebelum mengubah struktur besar yang sudah ada, kecuali memang ada kebutuhan nyata yang jelas.
