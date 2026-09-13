# Katalog Cacat Sistem (Sistem Klinik)

> **Dokumen Hidup (Living Document)**
> Katalog ini adalah basis pengetahuan (knowledge base) dan panduan diagnostik utama bagi Sistem Klinik. Katalog ini digunakan saat Tahap B Diagnosis untuk memeriksa kesehatan sebuah sistem target.

## Aturan Promosi Temuan Baru
1. **Sumber Wajib (Temuan Run):** Setiap kali Sistem Klinik menyelesaikan run di repo target (rawat-jalan/bengkel) dan menemui cacat struktural/prosedural, temuan tersebut wajib dipanen di Tahap F.
2. **Cek Duplikat:** Cek dulu apakah cacat yang sama sudah ada di katalog ini. Hanya cacat yang **belum ada** atau varian yang benar-benar berbeda yang boleh ditambahkan.
3. **Format Terkunci:** Cacat baru harus ditulis menggunakan field yang identik dengan yang ada (ID, Nama, Gejala, Cara Periksa, Pola Perbaikan, Bukti/Risiko).
4. **Mekanisme Promosi:** Agent menyertakan cacat baru tersebut sebagai usulan (PR) ke repo meta (sistem klinik), menambahkan entri ke tabel di bawah beserta Log Keputusan perubahannya.

---

## Daftar Cacat (Katalog)

### C-01: Kebocoran Ketergantungan Eksternal (Self-Containment Broken)
- **Gejala:** Sistem atau folder kit memiliki instruksi, aturan, atau alat yang bergantung pada file di luar foldernya (misalnya merujuk file di _meta/ dengan *backtick* tanpa menyediakannya di dalam sistem itu sendiri).
- **Cara Periksa (Diagnosis):** Cari pola rujukan absolut atau *backtick* ke luar folder sistem (misal `grep "_meta/"` atau `grep "tools/"`). Jalankan skrip uji kemandirian (jika tersedia).
- **Pola Perbaikan (Resep):** Salin file/aturan eksternal yang dirujuk ke dalam folder sistem, tandai sebagai turunan berlabel versi. Ubah rujukan asli menjadi provenance historis tanpa *backtick*.
- **Bukti / Risiko:** Sistem akan rusak dan tidak bisa dioperasikan saat diunduh (extracted) sebagai repo mandiri yang terpisah dari induknya.

### C-02: Manifest Basi (Drifted State)
- **Gejala:** Field `Versi`, `Tahap`, atau `Status` di `SYSTEM_MANIFEST.md` sudah tidak sesuai dengan kondisi aktual *working tree* (misal masih "Proposed" padahal PR kerangka sudah merged, atau "Belum dibangun" padahal dokumen sudah ada).
- **Cara Periksa (Diagnosis):** Bandingkan isi `SYSTEM_MANIFEST.md` dengan daftar file aktual (`ls`) dan histori PR terakhir yang merged.
- **Pola Perbaikan (Resep):** Sinkronisasikan field manifest dengan status sebenarnya. Tambahkan cek manifest pada alur verifikasi penutup.
- **Bukti / Risiko:** Kehilangan kepercayaan terhadap manifest; agent atau sistem lain akan mengambil keputusan berdasar konteks yang salah.

### C-03: Log Sesi Menggantung (Zombie Log)
- **Gejala:** Terdapat file `LOG_SESI_*.md` yang memiliki header `- **Keadaan:** \`OPEN\``, padahal pekerjaan sudah selesai, PR terkait sudah merged, atau branch sudah tidak ada.
- **Cara Periksa (Diagnosis):** Cari teks `Keadaan: \`OPEN\`` di dalam arsip log sesi, lalu cocokkan dengan status PR/branch menggunakan `gh pr list --state all`.
- **Pola Perbaikan (Resep):** Ubah status log tersebut secara retrospektif menjadi `CLOSED` dengan menambahkan catatan penutupan di bagian akhir log (append).
- **Bukti / Risiko:** Agent baru yang memulai sesi akan bingung menentukan *entry point* atau mencoba melanjutkan konteks pekerjaan yang sebenarnya sudah usai, menyebabkan tabrakan state.

### C-04: Bukti Pengujian Volatil
- **Gejala:** Laporan penerimaan (acceptance test) atau bukti QA mengandalkan angka-angka absolut yang mudah berubah secara natural, seperti "jumlah baris (line counts)" atau "jumlah kata" dari korpus yang terus berkembang.
- **Cara Periksa (Diagnosis):** Periksa file verifikasi atau bukti di dalam sistem. Apakah ada syarat kelulusan semacam "baris > 1500" atau angka hitungan file di korpus dinamis?
- **Pola Perbaikan (Resep):** Ganti metrik volatil dengan uji keberadaan struktur (file eksis), regex pola tertentu, atau status kembalian alat (exit 0). 
- **Bukti / Risiko:** Sistem akan sering mengalami *false negative* (ujian gagal padahal sistem tidak rusak) seiring pertumbuhan konten.

### C-05: Absennya Mekanisme Fail-Closed (Checkpoint Tidak Ditegakkan)
- **Gejala:** Sistem tidak berhenti saat terjadi anomali (misalnya alat validasi menghasilkan error/merah, tapi pekerjaan terus dilanjutkan sampai tahap merge).
- **Cara Periksa (Diagnosis):** Cek panduan pengguna dan alur kerja (pipeline/actions jika ada). Apakah ada gerbang eksplisit "jika X gagal, berhenti dan jangan merge"?
- **Pola Perbaikan (Resep):** Tanamkan kebijakan *fail-closed* di dokumen alur atau panduan utama, wajibkan gerbang validasi (contoh: *exit code* wajib 0 sebelum membuat PR).
- **Bukti / Risiko:** Kerusakan data persisten atau korupsi *state* sistem yang jauh lebih sulit diperbaiki.

### C-06: Penyumbatan Bengkel / Bengkak Aset
- **Gejala:** Branch perbaikan (bengkel) memuat commit berisi aset raksasa (gambar, video, DB) atau riwayat yang panjang tak berujung, yang pada akhirnya ikut tersimpan ke dalam penyimpanan `.git` repo induk meski tak di-merge.
- **Cara Periksa (Diagnosis):** Cek kebijakan pembentukan branch perbaikan. Apakah sistem langsung mengkopi semua direktori secara membabi-buta termasuk file biner statis?
- **Pola Perbaikan (Resep):** Batasi kebijakan penyalinan branch perbaikan. File *exclude* (misal `.gitignore` atau filter `.rsync`) wajib melompati aset berat. PR perbaikan diatur hanya berisi teks pelaporan/tindakan.
- **Bukti / Risiko:** Kapasitas repo bengkak secara permanen (bloat), memperlambat setiap operasi `git clone` dan `git fetch`.

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-13 | Seed awal katalog dibuat (C-01 sampai C-06) | Menyediakan tolok ukur awal bagi agent klinik untuk melakukan diagnosis sistem target (Langkah 3 rencana kerangka). |
