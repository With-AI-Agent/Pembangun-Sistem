> Sumber: _sistem/04_KONTRAK_TANAMAN.md sha 98a9183dcfba99c6b0844a5e0c20e1fbb72a9faa tanggal 2026-09-16 versi-kit 0.2.1

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
- **Syarat tambahan (panen C-07, 2026-09-16):** bila target sudah punya dokumen pegangan/pemakaian **lama yang digantikan** tanaman ini, dokumen lama WAJIB dipensiunkan — penanda arsip di kepalanya + penunjuk dokumen yang berlaku, isi asli di bawah penanda tidak disunting (Kebijakan Lebur Aturan 2 butir "Pensiunkan, jangan hapus"). Verifikasi tambahan: `grep -c "SUDAH DIGANTIKAN" <dokumen lama target>` minimal 1, dan dokumen lama itu **tidak** lagi menyebut instruksi yang bertentangan dengan dokumen berlaku.

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
- **Syarat tambahan (panen C-07, 2026-09-16):** angka terukur di manifest (ukuran folder, jumlah direktori/berkas, jumlah template, daftar dokumen wajib) wajib punya **SATU sumber kanonik** — dokumen lain **menunjuk** ke sana, bukan menyalin angkanya; dan setiap klaim jumlah dibandingkan dengan **hitungan nyata** oleh validator target (bukan angka beku yang bisa basi). Angka yang dihitung dari korpus dokumen repo induk dilarang masuk bukti permanen (aturan meta C5). Verifikasi tambahan: validator target memuat cek pembanding klaim-vs-hitungan-nyata, dan cek itu **dibuktikan menyala dengan uji mutasi** (ubah klaimnya → validator GAGAL); gerbang hijau tanpa uji mutasi bisa jadi hijau karena tidak memeriksa apa pun (pola F-8).

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
| 2026-09-16 | W-01 + W-04 diberi **"Syarat tambahan (panen C-07)"**: pensiunkan dokumen target yang digantikan (penanda arsip) dan satu sumber angka terukur + klaim jumlah dibandingkan hitungan nyata oleh validator target yang dibuktikan uji mutasi | Panen C-07 run klinik ke-2 (PR #63): manifest target menyebut jumlah template dan ukuran folder yang tidak cocok kenyataan, angka salinannya bertentangan antar dokumen, dan **tidak ada gerbang** yang membandingkannya dengan hitungan nyata. Resepnya dinaikkan jadi kontrak tanaman supaya run berikutnya menanam gerbangnya, bukan hanya mengoreksi angkanya sekali |
| 2026-09-13 | Inisialisasi draf Kontrak Tanaman (W-01..W-09) | Memenuhi kebutuhan Tahap C (Tindakan) dalam rencana kerangka Klinik, menjabarkan bentuk proporsional untuk target besar maupun kecil. |
