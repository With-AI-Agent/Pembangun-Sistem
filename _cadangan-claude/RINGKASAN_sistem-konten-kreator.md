# Ringkasan Sistem — Sistem Konten Kreator
### Untuk sesi Claude chat biasa (cadangan lmarena Agent). Dokumen ini BUKAN sistem itu sendiri — cuma ringkasan supaya Claude paham konteks tanpa perlu upload semua file.

## Sistem ini tentang apa
Sistem kerja untuk konten kreator berbasis AI — dari nentuin channel mau ngomongin apa, membangun karakter/elemen visual yang konsisten, sampai produksi konten harian yang siap publish. Dijalankan lewat lmarena Agent yang terhubung ke repo GitHub, bisa baca-tulis file dan generate gambar langsung (tidak bisa generate video).

## Bentuk dasar
**Gabungan Bertingkat + Siklus.** Bertingkat di level struktural: Brand Core (lintas semua channel) → Channel Brief (1 niche/positioning) → Model Konten Brief (1 cara produksi/format dalam channel itu). Siklus di level produksi harian: Pipeline 6 Tahap (Ideation → Konsep → Naskah → Breakdown Visual → Generate Asset → Assembly) yang diulang tiap kali bikin 1 konten baru.

## Struktur folder saat ini
```
sistem-konten-kreator/
├── _sistem/
│   ├── START_DI_SINI.md
│   ├── 00_CARA_PAKAI_SISTEM.md
├── 01_BRAND_CORE.md
├── 02_CHANNEL_DISCOVERY_PROMPT.md
├── 03_TEMPLATE_CHANNEL_BRIEF.md
├── 04_CHARACTER_BUILDER_KIT.md
├── 05_CONTENT_PRODUCTION_PIPELINE.md
├── 06_PROMPT_LIBRARY.md
├── 07_MODEL_KONTEN_DISCOVERY_PROMPT.md
├── 08_TEMPLATE_MODEL_KONTEN_BRIEF.md
└── PANDUAN_PENGGUNA.md  (untuk pengguna, bukan diupload ke repo GitHub asli sistem konten kreator itu sendiri — tapi tetap disimpan di sini sebagai arsip)
```
Ini 10 dokumen SISTEM (instruksi kerja untuk agent) + 1 dokumen panduan pengguna. Setelah dijalankan, sistem ini akan menghasilkan folder tambahan di repo produksi yang sebenarnya: `channel-[nama]/`, `konsistensi-lintas-channel/`, `_produksi-aktif/` — skeleton lengkapnya ada di `00_CARA_PAKAI_SISTEM.md` bagian "Struktur Repo".

## Prinsip yang berlaku
Mengikuti semua 5 Prinsip Universal dari `_meta/02_PRINSIP_UNIVERSAL.md` TANPA override — sistem ini justru yang jadi SUMBER dari prinsip-prinsip itu (dipilah dari sini ke level universal setelah terbukti works). Tambahan spesifik-domain: Pemisahan Konsistensi Visual vs Non-Visual (khusus konten kreator, tidak universal).

## Status sekarang
**Kandidat sistem contoh — sedang diperbaiki.** Audit independen 3 September 2026 menemukan beberapa celah operasional yang harus ditutup sebelum sistem ini ditetapkan sebagai contoh resmi meta-sistem atau dipakai produksi nyata.

## PENTING — hasil kerja sesi ini akan dibawa ke mana
Hasil dari sesi Claude ini akan di-paste manual oleh pengguna ke lokasi yang sesuai di Obsidian (sync otomatis ke GitHub via plugin git). Pastikan format/struktur yang dihasilkan KOMPATIBEL dengan 11 dokumen yang sudah ada — cek dulu dokumen terkait yang diupload bersama ringkasan ini sebelum menulis apa pun. Karena sistem ini sudah final dan teraudit, perubahan apapun ke sistem ini sebaiknya dianggap REVISI terhadap sesuatu yang sudah teruji — pertimbangkan matang-matang sebelum mengubah struktur besar yang sudah ada, kecuali memang ada kebutuhan nyata yang jelas.
