# Prompt Pembangkitan: Kontrak Tanaman (04A)

**Konteks & Tujuan:**
Kamu sedang membangun `_sistem/04_KONTRAK_TANAMAN.md` untuk Sistem Klinik. Dokumen ini mendefinisikan syarat minimum agar sebuah sistem target (baik besar maupun "mini/kecil") diakui sebagai "sistem yang terawat/sehat". Syarat minimum ini adalah terjemahan dari Kontrak Warisan meta (W-01 sampai W-09) yang disesuaikan untuk repo mandiri hasil ekstrak.

Tugasmu:
1. Terjemahkan kesembilan butir W (W-01 hingga W-09) menjadi **Kontrak Tanaman** yang wajib ditanam agent saat klinik bekerja (Tahap C Tindakan).
2. Tulis `_sistem/04_KONTRAK_TANAMAN.md` dengan struktur:
   - **Tujuan Dokumen & Pengantar**
   - **Daftar Butir Tanaman (W-01 s/d W-09)**, untuk SETIAP butir, jelaskan:
     - **Apa yang ditanam:** (Bentuk/dokumen/field aslinya apa)
     - **Bentuk sederhana:** (Jika target adalah sistem mini/skrip tunggal, bagaimana bentuk sederhananya agar tidak overkill? misal: alih-alih folder log, cukup 1 file log tunggal)
     - **Cara Verifikasi:** (Bagaimana agent di masa depan mengecek bahwa tanaman ini sehat/tidak basi)
   - **Log Keputusan** di bagian bawah.

**Catatan Khusus (W-01...W-09 dari 03_KONTRAK_WARISAN):**
- W-01: Pegangan Pengguna (Prompt Entri + Panduan)
- W-02: LOG_SESI (Pencatatan sesi persisten)
- W-03: Field STATUS (Checkpoint persisten)
- W-04: Manifest (Kartu identitas sistem)
- W-05: Log Keputusan (Tabel jejak historis)
- W-06: QA 3-Lapis (Aturan verifikasi berlapis)
- W-07: Fakta Platform (Workaround/batas platform mis. batas branch/token lmarena)
- W-08: Approval Bertingkat (Gerbang verifikasi besar/kecil)
- W-09: Ringkasan Cadangan (Ringkasan LLM untuk konteks sekunder)

**Aksi:**
Jalankan ekstraksi ini sekarang, ambil keputusan terjemahan bentuk sederhana untuk tiap butir secara logis dan proporsional, lalu buat draf `04_KONTRAK_TANAMAN.md`. Pastikan tidak ada asumsi yang tidak bisa diuji secara mekanis (exit 0).
