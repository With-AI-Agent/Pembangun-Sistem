# Prompt Pembangkitan: Seed Katalog Cacat (02A)

**Konteks & Tujuan:**
Kamu sedang membangun `_sistem/02_KATALOG_CACAT.md` untuk Sistem Klinik. Katalog Cacat adalah daftar hidup (living document) yang berisi pola cacat struktural, prosedural, atau desain yang sering ditemui pada sistem-sistem (baik di repo ini maupun di luar). Katalog ini menjadi panduan/tolok ukur (Diagnosis) bagi agent saat mengevaluasi sistem target.

Tugasmu:
1. Tambang ingatanmu dan arsip penemuan meta (misalnya LOG_SESI atau README bengkel, pengetahuan tentang fail-closed, bukti basi, self-containment, dll.) untuk menemukan 5-8 cacat awal (seed) yang realistis.
2. Terjemahkan cacat tersebut menjadi netral-domain (berlaku untuk sistem apa saja, bukan cuma spesifik sistem A).
3. Tulis `_sistem/02_KATALOG_CACAT.md` dengan struktur yang menyertakan:
   - Metadata dokumen (Tujuan, Aturan Promosi Cacat Baru)
   - Tabel/Daftar Cacat, masing-masing dengan:
     - **ID Temuan** (mis. `C-01`)
     - **Nama Cacat**
     - **Gejala (Symptom)** (apa yang terlihat oleh pengguna atau agent)
     - **Cara Periksa (Diagnosis)** (cara pasti memvalidasi keberadaan cacat ini)
     - **Pola Perbaikan (Resep/Tindakan)** (langkah perbaikannya)
     - **Bukti / Risiko** (mengapa ini penting, atau bukti nyata dampak cacat ini)
   - Log Keputusan di bagian bawah (W-05).

**Aturan Promosi Cacat Baru (dimasukkan dalam dokumen):**
Setiap kali Sistem Klinik berjalan (run nyata) dan menemukan cacat bentuk baru, cacat tersebut WAJIB dipanen (Tahap F Panen) ke katalog ini (lewat PR ke master klinik). Syarat masuk katalog:
1. **Sumber = Temuan Run Nyata** (bukan sekadar teori).
2. **Cek Duplikat:** Harus dipastikan cacat/pola tersebut belum ada di katalog saat ini.
3. **Format Terkunci:** Cacat baru harus ditulis menggunakan field yang identik (Nama, Gejala, Cara Periksa, Pola Perbaikan, Bukti/Risiko).

**Contoh Cacat (sebagai inspirasi, kembangkan jadi formal):**
- Referensi eksternal bocor (backtick ke luar folder sistem).
- Status/Versi di manifest basi tidak mencerminkan keadaan working tree.
- Log sesi menggantung (header OPEN tapi PR sudah merged).
- Bukti pengujian mengandalkan angka volatil (misal jumlah baris) yang gampang rusak.
- Sistem tidak memiliki mekanisme pemulihan fail-closed (tidak berhenti saat error).

Jalankan ekstraksi ini sekarang dan buat draf `02_KATALOG_CACAT.md`.
