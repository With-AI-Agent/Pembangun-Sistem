> Sumber: _sistem/06_RITME_KIT.md sha 0a7f3d3d13c908972a3db4e9780b08e84a387d05 tanggal 2026-09-14 versi-kit 0.2.0

# Ritme dan Perakitan Kit Klinik

> **Dokumen Aturan (Rule Document)**
> Dokumen ini mengatur bagaimana sumber kebenaran (master di `_sistem/`) dirakit menjadi `kit/` portabel yang siap didistribusikan ke target. Kit adalah produk (deliverable) dari Sistem Klinik, bukan tempat bekerja/mengedit aturan langsung.

## 1. Anatomi Perakitan (Dokumen yang Ikut)
Folder `kit/` akan dikonstruksi secara mekanis. Isinya wajib *self-contained*:
- `PROMPT-ENTRI-KIT.md` & `PROMPT-PENUTUP-KIT.md` — interface manusia-ke-agent di repo target.
- `aturan/` — turunan statis (salinan) dari `01_ALUR_RUN.md` sampai `06_RITME_KIT.md`. Setiap file aturan di dalam `kit/` **wajib diberi header (stamp) versi**.
- `alat/` — *Subset portabel* dari alat-alat meta (contoh: validator `STATUS`, pemeriksa tautan *backtick*), wajib `stdlib-only` Python agar jalan di runtime apapun tanpa `pip install`.
- `TEMPLATE-REKAM-KLINIK.md`
- `TEMPLATE-LOG-SESI-TARGET.md` & `TEMPLATE-STATUS-TARGET.md`

## 2. Stamp Versi dan Sinkronisasi Master→Kit
Semua salinan di `kit/aturan/` harus memiliki penanda ini di baris teratas (ditegakkan oleh validator):
```md
> Sumber: _sistem/<berkas master> sha <40> tanggal <YYYY-MM-DD> versi-kit <x.y.z>
```
*(Catatan konvensi: `<40>` di atas merujuk secara persis pada **blob SHA** dari berkas master pada saat dikompilasi, sehingga target dapat memverifikasi isi persis dari berkas tersebut).*
- **Prosedur Sync (Manual/Skrip):** Jika aturan master `_sistem/` berubah, pemilik atau agent wajib mensinkronisasi ke `kit/` sebelum melakukan PR rilis.
- **Cek Kit Basi:** Acceptance Tests harus memeriksa apakah tanggal kompilasi/versi di `kit/` tertinggal dari versi manifest di `SYSTEM_MANIFEST.md`. Jika basi, build harus *fail-closed*.

## 3. Aturan Promosi Kemampuan (Rawat Inap → Portabel)
Prosedur berat yang hanya bisa dikerjakan di dalam repo meta — panggung rawat inap (K-11; misalnya skrip rumit untuk memulihkan git history besar) — bisa dipromosikan menjadi **alat portabel** di `kit/alat/` jika memenuhi syarat:
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
| 2026-09-14 UTC / 15 Sep WIB | §3 diberi redaksi ulang → "Rawat Inap → Portabel" (panggung bengkel dihapus; sumber K-9 diganti K-11); VERSI kit 0.1.2 → 0.2.0 + restamp berkas aturan yang berubah | K-11: panggung rawat inap kini membaca MASTER di tempatnya, bukan salinan kit — mekanisme kit (stamp/sync/naik-versi) hanya melayani suntik; promosi kemampuan dari rawat inap tetap jalur evolusi kit yang sah |
