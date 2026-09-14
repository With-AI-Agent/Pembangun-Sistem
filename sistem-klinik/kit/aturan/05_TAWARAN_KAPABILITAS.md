> Sumber: _sistem/05_TAWARAN_KAPABILITAS.md sha 251f90289ae0c35f8a0cf914566531fd84a8a805 tanggal 2026-09-14 versi-kit 0.1.1

# Mekanisme Tawaran Kapabilitas Eksternal

> **Dokumen Aturan (Rule Document)**
> Dokumen ini adalah panduan baku (Mekanisme) bagi Agent Klinik untuk secara proaktif menawarkan penambahan alat eksternal (skill/plugin/vendor-script) ke sistem target. Aturan ini wajib dijalankan di Tahap B (Diagnosis/Pendaftaran) sebelum beranjak ke eksekusi.

## 1. Pemetaan Kebutuhan
Sebelum melakukan pencarian, Agent harus membaca `SYSTEM_MANIFEST.md`, struktur direktori target, dan `PANDUAN_PENGGUNA.md` untuk menebak *pain points* (titik lemah). Contoh:
- Sistem mengolah banyak teks markdown? Tawarkan linter/markdown-formatter.
- Sistem sering berurusan dengan web-scraping? Tawarkan library parser HTML yang lebih baik (mis. BeautifulSoup versi vendor).
- Sistem pembuat gambar? Tawarkan plugin optimasi gambar.

## 2. Riset Kandidat (Internet Search)
Agent **wajib** menggunakan kapabilitas *web_search* atau pengetahuannya untuk meriset 3-5 plugin/skill terbaik yang:
- Relevan dengan domain target.
- Cocok dengan environment yang dideklarasikan.
- Stabil dan memiliki dependensi minimal.

## 3. Format Penawaran (Borongan K-10)
Sesuai aturan K-10 dari pemilik (anti bertele-tele), agent **dilarang** menanyakan kapabilitas satu per satu. Agent wajib menyajikannya dalam **Tabel Rekomendasi Borongan** (maksimal 5 item per pesan).

Format Tabel Rekomendasi (wajib ditunjukkan ke pengguna):
| Nama Kapabilitas | Fungsi / Tujuan | Alasan Butuh | Cara Install | Risiko Pasang | Alternatif Lokal | Konsekuensi Ditolak |
|---|---|---|---|---|---|---|
| (Nama alat/plugin) | (Deskripsi ringkas) | (Mengapa sistem INI butuh) | (lmarena / Claude Code) | (Keamanan / bengkak) | (Skrip buatan sendiri) | (Kerja manual / lambat) |

Di bawah tabel, agent **wajib** menyertakan satu pertanyaan terbuka:
> *"Apakah ada fungsi, skill, atau plugin lain yang kamu butuhkan tetapi belum ada di daftar di atas?"*

## 4. Semantik "Install" Berdasarkan Runtime Target
Agent tidak boleh berasumsi "install" berarti `npm install -g` atau mengubah OS, karena batasan platform.

- **Pada lmarena (Agent Mode):**
  Platform direset setiap sesi baru. Oleh karena itu, *install* berarti **mengunduh dan menyimpan skrip/binary vendor ke dalam repo git target** (contoh: di folder alat target). Dependensi harus terikat dengan repo (terlokalisasi), bukan terinstal di environment OS.
- **Pada Claude Code / Antigravity:**
  Install biasanya berarti memodifikasi `.claude.json` atau meregistrasikan *MCP tool / bash script* lokal di konfigurasi folder.

## 5. Prosedur Penanaman & Registrasi
Jika pemilik membalas "Setuju untuk alat A dan C", agent akan:
1. **Menanam (Install):** Melakukan eksekusi instalasi sesuai *runtime*. Skrip diletakkan dan diuji langsung (exit 0).
2. **Registrasi Target:** Menambahkan nama alat, versi, dan folder lokasinya ke bagian "Dependency eksternal" di `SYSTEM_MANIFEST.md` repo target.
3. **Log Keputusan Target:** Menambahkan tabel Log Keputusan di repo target yang mencatat alasan pengadopsian.
4. **Rekam Klinik:** Memasukkan tindakan ini ke dalam `REKAM-KLINIK.md` sebagai bagian dari jejak perawatan.

*Penolakan dari pemilik juga dicatat di Log Keputusan target dengan alasan "Ditolak saat run klinik", sehingga agent berikutnya tidak cerewet menawarkan ulang benda yang sama tanpa pembaruan.*

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-13 | Inisialisasi mekanisme Tawaran Kapabilitas | Mengunci alur borongan (K-10) dan membedakan semantik instalasi lintas-runtime agar plugin persisten dan bisa berfungsi (terutama untuk lmarena). |
