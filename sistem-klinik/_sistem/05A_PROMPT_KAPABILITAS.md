# Prompt Pembangkitan: Tawaran Kapabilitas (05A)

**Konteks & Tujuan:**
Kamu sedang membangun `_sistem/05_TAWARAN_KAPABILITAS.md` untuk Sistem Klinik. Dokumen ini adalah mekanisme yang **wajib ditawarkan** (oleh agent) setiap kali Klinik dijalankan pada suatu repo target. Fitur ini dirancang agar agent proaktif meriset dan menawarkan plugin/skill eksternal (kapabilitas baru) yang relevan dengan domain sistem tersebut.

Tugasmu:
1. Gali dan rumuskan alur mekanisme penawaran kapabilitas yang solid (sesuai kerangka).
2. Tulis `_sistem/05_TAWARAN_KAPABILITAS.md` yang memuat elemen-elemen berikut:
   - **Pemetaan Kebutuhan:** Cara agent mendiagnosis repo untuk menebak "kapabilitas eksternal apa yang berguna untuk sistem ini".
   - **Riset Internet & Kandidat:** Panduan riset untuk mencari vendor/plugin.
   - **Tabel Rekomendasi (Format Penawaran):** Agent harus menyajikan tabel penawaran berisi: Apa fungsinya, Dari mana, Cara pasang (install), Risiko jika dipasang, Konsekuensi jika ditolak, dan Alternatif Lokal/Standard-library. Format penawaran ini WAJIB borongan (≤±5 item per pesan) dan memberi slot "usulan pemilik" (Aturan K-10 dari Manifest).
   - **Prosedur Instalasi per Runtime (Sangat Penting!):** Jangan berasumsi cara pasang itu sama. Definisikan perbedaan mendasar semantik "install" di:
     - *lmarena (Agent Mode):* Vendor/skrip harus masuk ke *repo* dalam folder vendor, karena runtime ini statis/di-clone per sesi.
     - *Claude Code / Antigravity:* Skill/plugin masuk ke konfigurasi environment global atau `.claude.json`.
   - **Registrasi & Penanaman:** Setiap kapabilitas yang disetujui untuk dipasang wajib diregistrasikan di manifest sistem target dan *Log Keputusan*.
   - **Log Keputusan** sistem di akhir dokumen.

**Aksi:**
Jalankan rumusan ini secara logis, jangan berasumsi alat eksternal pasti jalan tanpa di-test, dan patuhi K-10 (borongan). Buat draf `05_TAWARAN_KAPABILITAS.md` sekarang.
