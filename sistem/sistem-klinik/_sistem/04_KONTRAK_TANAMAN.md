# Kontrak Tanaman (Sistem Klinik)

> **Dokumen Aturan (Rule Document)**
> Dokumen ini berisi terjemahan dari Kontrak Warisan Meta (W-01 s/d W-09) menjadi **Kontrak Tanaman**. Ini adalah standar minimum yang wajib ditanam oleh Sistem Klinik ke setiap sistem target agar dianggap sehat, terstandar, dan dapat dirawat kembali di masa depan secara idempoten.

## Prinsip Penanaman
1. **Idempoten:** Penanaman tidak boleh merusak sistem yang sudah ada. Jika tanaman sudah sehat, lewati. Jika basi, upgrade.
2. **Proporsional:** Sistem yang disuntik bisa berupa repo besar (ratusan file) atau sistem mini (satu file `app.py`). Kontrak tanaman ini menyediakan "bentuk sederhana" agar overhead pemeliharaan tidak membengkak di sistem mini.
3. **Dapat Diverifikasi:** Semua tanaman harus bisa diuji ketersediaannya secara mekanis (regex/grep/exit 0).

---

## Daftar Kontrak Tanaman

### W-01: Pegangan Pengguna
- **Apa yang ditanam:** File `PANDUAN_PENGGUNA.md` dan `PROMPT_ENTRI_UNIVERSAL.md` yang memuat aturan orientasi agent untuk repo target.
- **Bentuk sederhana (Sistem Mini):** Disatukan menjadi satu file `README.md` (atau `PANDUAN_PENGGUNA.md` tunggal) yang sudah mencakup blok prompt pembuka di paragraf pertama.
- **Cara Verifikasi per Tanaman:** Agent mengecek keberadaan file pegangan utama, dan memastikan terdapat header/instruksi yang secara eksplisit meminta agent baru membaca file tersebut. (Misal `grep "Prompt Pembuka" PANDUAN_PENGGUNA.md`).

### W-02: Pencatatan Sesi (LOG_SESI)
- **Apa yang ditanam:** Folder `_log-sesi/` dengan konvensi penamaan `LOG_SESI_YYYY-MM-DD.md` dan aturan status (`OPEN`/`CLOSED`).
- **Bentuk sederhana (Sistem Mini):** Satu file tunggal `LOG_SESI.md` di root repo yang menumpuk riwayat sesi (append-only), tanpa perlu folder khusus.
- **Cara Verifikasi per Tanaman:** Agent mengecek keberadaan `LOG_SESI.md` atau folder `_log-sesi/`, lalu memastikan format header (Keadaan Sesi, Kronologi) dan status yang sah.

### W-03: Field STATUS (Checkpoint)
- **Apa yang ditanam:** File `STATUS.md` yang berisi ringkasan *state* deterministik dari sistem (Status: aktif/rusak, Tahap terakhir, Risiko aktif).
- **Bentuk sederhana (Sistem Mini):** Bagian/header `# STATUS SISTEM` yang disisipkan ke dalam `README.md` atau di atas `LOG_SESI.md`.
- **Cara Verifikasi per Tanaman:** Cek regex `STATUS.*(aktif|dalam-pembangunan|rusak)` di `STATUS.md` atau `README.md`.

### W-04: Manifest Sistem
- **Apa yang ditanam:** File `SYSTEM_MANIFEST.md` berisi kartu identitas, versi, tahap, dan bentuk sistem (Flat/Siklus/dll).
- **Bentuk sederhana (Sistem Mini):** Tidak diubah, tetap satu file `SYSTEM_MANIFEST.md` yang disederhanakan isinya (cukup Nama, Tujuan, dan Versi).
- **Cara Verifikasi per Tanaman:** Uji keberadaan `SYSTEM_MANIFEST.md` dan parsing field Versi (`grep "Versi:" SYSTEM_MANIFEST.md`).

### W-05: Log Keputusan
- **Apa yang ditanam:** Tabel "Log Keputusan" yang mengikat riwayat asitektur. Biasanya diletakkan di akhir setiap dokumen aturan/ living document.
- **Bentuk sederhana (Sistem Mini):** Satu tabel Log Keputusan tunggal di `SYSTEM_MANIFEST.md` atau `README.md`.
- **Cara Verifikasi per Tanaman:** Cek regex `| Tanggal | Perubahan | Alasan |` pada file inti.

### W-06: QA 3-Lapis (Verifikasi Berlapis)
- **Apa yang ditanam:** File `ACCEPTANCE_TESTS.md` atau prosedur QA dan folder `_fixture/` untuk uji sistematis sebelum rilis.
- **Bentuk sederhana (Sistem Mini):** Satu bagian "Cara Pengujian (QA)" di `PANDUAN_PENGGUNA.md` atau shell script sederhana `test.sh`.
- **Cara Verifikasi per Tanaman:** Cek keberadaan file/skrip pengujian dan instruksi eksplisit kapan pengujian tersebut wajib dijalankan (mis. "jalankan sebelum merge").

### W-07: Batasan & Fakta Platform
- **Apa yang ditanam:** Dokumen yang mencatat batas platform lingkungan eksekusi (seperti token `lmarena` hilang pasca-merge, aturan non-blocking).
- **Bentuk sederhana (Sistem Mini):** Satu kalimat/paragraf "Fakta Platform" wajib di dalam `PANDUAN_PENGGUNA.md`.
- **Cara Verifikasi per Tanaman:** Grep kata kunci workaround seperti `lmarena` atau `fakta platform` di file panduan.

### W-08: Approval Bertingkat
- **Apa yang ditanam:** Klasifikasi gerbang persetujuan "Besar" (G-Rencana, G-Final) dan "Kecil" di dalam manifest atau panduan sistem target.
- **Bentuk sederhana (Sistem Mini):** Tidak ada gerbang kompleks, cukup satu "Titik Persetujuan Pemilik" sebelum `merge` atau rilis.
- **Cara Verifikasi per Tanaman:** Pengecekan ada tidaknya klausul persetujuan/gerbang sebelum eksekusi destruktif.

### W-09: Ringkasan LLM (Cadangan)
- **Apa yang ditanam:** File `RINGKASAN_[nama-sistem].md` yang membantu chat biasa (non-agent) mengerti konteks sistem.
- **Bentuk sederhana (Sistem Mini):** Tidak wajib jika repo tersebut bisa di-zip dan diberikan utuh ke Claude dalam sekali jalan.
- **Cara Verifikasi per Tanaman:** Keberadaan file dengan prefix `RINGKASAN_` atau status pengecualian eksplisit di manifest.

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-13 | Inisialisasi draf Kontrak Tanaman (W-01..W-09) | Memenuhi kebutuhan Tahap C (Tindakan) dalam rencana kerangka Klinik, menjabarkan bentuk proporsional untuk target besar maupun kecil. |
