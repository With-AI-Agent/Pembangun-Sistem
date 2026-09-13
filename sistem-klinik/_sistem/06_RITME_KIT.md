# Ritme dan Perakitan Kit Klinik

> **Dokumen Aturan (Rule Document)**
> Dokumen ini mengatur bagaimana sumber kebenaran (master di `_sistem/`) dirakit menjadi `kit/` portabel yang siap didistribusikan ke target. Kit adalah produk (deliverable) dari Sistem Klinik, bukan tempat bekerja/mengedit aturan langsung.

## 1. Anatomi Perakitan (Dokumen yang Ikut)
Folder `kit/` akan dikonstruksi secara mekanis. Isinya wajib *self-contained*:
- `PROMPT-ENTRI-KIT.md` & `PROMPT-PENUTUP-KIT.md` — interface manusia-ke-agent di repo target.
- `aturan/` — turunan statis (salinan) dari `01_ALUR_RUN.md` sampai `06_RITME_KIT.md`. Setiap file aturan di dalam `kit/` **wajib diberi header (stamp) versi**.
- `alat/` — *Subset portabel* dari `tools/` meta (contoh: validator `STATUS`, pemeriksa tautan *backtick*), wajib `stdlib-only` Python agar jalan di runtime apapun tanpa `pip install`.
- `TEMPLATE-REKAM-KLINIK.md`
- `TEMPLATE-LOG-SESI-TARGET.md` & `TEMPLATE-STATUS-TARGET.md`

## 2. Stamp Versi dan Sinkronisasi Master→Kit
Semua salinan di `kit/aturan/` harus memiliki penanda ini di baris teratas:
```md
> **DOKUMEN TURUNAN - JANGAN DIEDIT**
> Asal: Sistem Klinik v[VERSION] | Kompilasi: [TANGGAL]
```
- **Prosedur Sync (Manual/Skrip):** Jika aturan master `_sistem/` berubah, pemilik atau agent wajib mensinkronisasi ke `kit/` sebelum melakukan PR rilis.
- **Cek Kit Basi:** Acceptancce Tests harus memeriksa apakah tanggal kompilasi/versi di `kit/` tertinggal dari versi manifest di `SYSTEM_MANIFEST.md`. Jika basi, build harus *fail-closed*.

## 3. Aturan Promosi Kemampuan (Bengkel → Portabel)
Sesuai K-9, prosedur berat yang masuk ke panggung `_bengkel/` (misalnya skrip rumit untuk memulihkan git history besar) bisa dipromosikan menjadi **alat portabel** di `kit/alat/` jika memenuhi syarat:
- Sering ditemui (sudah ada di `02_KATALOG_CACAT`).
- Bisa dipersingkat menjadi satu file Python statis (tanpa lib eksternal).
- Ringan (tidak memakan kuota context token berlebih).

## 4. Ritme Rilis dan Tawaran Naik Versi
Klinik adalah sistem yang hidup (K-8). 
- Setiap pembaruan kit (ada cacat baru di katalog, aturan tanam baru, atau perbaikan bug) akan menghasilkan **kenaikan versi** (mis. `v0.1.1` ke `v0.2.0`).
- **Tawaran Naik Versi:** Ketika agent klinik menyuntik sebuah sistem lama, hal pertama yang dibaca adalah `REKAM-KLINIK.md` target. Jika target terakhir dirawat menggunakan "kit v0.1.0" sementara kit saat ini "v0.2.0", agent **wajib menjalankan upgrade** mengikuti *changelog* evolusi klinik secara transparan sebelum melakukan audit rutin.

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-13 | Inisialisasi Ritme Kit | Menjawab K-8 (Sistem hidup) dengan memastikan kit yang beredar bisa disinkronkan kembali, dan memiliki stamp penanda agar target tahu versi terakhir ia dirawat. |
