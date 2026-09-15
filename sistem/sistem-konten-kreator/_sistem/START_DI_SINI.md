# Start Di Sini

### Buka file ini setiap kali mau MEMBUAT sesuatu yang baru di sistem ini (bukan untuk produksi konten harian — untuk itu langsung ke `05_CONTENT_PRODUCTION_PIPELINE.md` via Channel Brief/Model Konten Brief yang relevan). File ini cuma peta pendek, bukan prompt itu sendiri. Ini file untuk agent (dibaca sebagai bagian dari sistem), untuk panduan lengkap cara mulai dari nol lihat `panduan/PANDUAN_PENGGUNA.md`.

---

## Mau generate apa?

**Belum punya Brand Core sama sekali (baru mulai dari nol total)**
→ Buka `01_BRAND_CORE.md`, jalankan prompt di dalamnya
→ Hasil: `_sistem/01_BRAND_CORE.md` terisi

**Punya ide channel baru** (channel = "saluran" konten dengan niche & voice sendiri, misal "Cerita Horor Malam")
→ Buka `02_CHANNEL_DISCOVERY_PROMPT.md`
→ Hasil: folder baru `channel-[nama]/` dengan `channel-brief.md` di dalamnya

**Channel sudah ada, mau bangun elemen visual yang harus konsisten** (Karakter Utama Tipe A, Latar/Lingkungan, Palet & Gaya Render, atau Props — sesuai checklist konsistensi di Channel Brief)
→ Buka `04_CHARACTER_BUILDER_KIT.md`
→ Hasil: `channel-[nama]/konsistensi-visual/[nama-elemen]/` terisi (atau `konsistensi-lintas-channel/[nama-elemen]/` kalau elemen ini dirancang untuk dipakai di lebih dari 1 channel — lihat bagian "Sebelum mulai" di file `04`)

**Channel sudah ada, mau tetapkan cara produksi/format baru untuk channel itu** (model konten = cara eksekusi spesifik, misal "animasi 60 detik" vs "gambar statis + narasi" dalam channel yang sama)
→ Buka `07_MODEL_KONTEN_DISCOVERY_PROMPT.md`
→ Hasil: folder baru `channel-[nama]/model-konten/[nama-model]/` dengan `brief.md` di dalamnya

**Karakter Tipe B (one-off, per-konten) muncul di tengah produksi**
→ Tidak perlu buka file terpisah, ini otomatis ditangani di alur produksi — lihat `06_PROMPT_LIBRARY.md` bagian A2. Agent akan otomatis cek arsip naskah channel dulu sebelum bikin karakter baru.

**Mau produksi konten (bukan bikin sistem baru)**
→ Entry Point Universal (lihat `00_CARA_PAKAI_SISTEM.md`) mewajibkan agent membaca konteks wajib untuk sesi produksi — Brand Core, Channel Brief, Model Konten Brief, pipeline, dan prompt library — sesuai tabel "Konteks Wajib per Jenis Sesi", lalu ikuti `05_CONTENT_PRODUCTION_PIPELINE.md`

**Mau cek apakah hasil kerja masih konsisten dengan yang sudah dikunci**
→ Panggil perintah "cek konsistensi" kapan saja — lihat `00_CARA_PAKAI_SISTEM.md`

**Mau menguji apakah sistem ini sendiri masih berperilaku benar** (setelah aturannya diubah, atau sebelum menaikkan status sistem)
→ Jalankan skenario di `ACCEPTANCE_TESTS.md` (di root sistem, bukan di `_sistem/`) dan isi tabel Rekaman Hasil

**Mau menutup pengecualian/gate (mis. F), menaikkan versi aturan, atau mengubah klaim di manifest (pekerjaan L1)?**
→ Review independen oleh SESI LAIN wajib sebelum klaim boleh masuk main — protokol varian KK di `PROTOKOL_REVIEW_INDEPENDEN.md` (root sistem) + induk _meta/PROTOKOL_REVIEW_INDEPENDEN.md di master (provenance); varian prompt reviewer siap tempel ada di `panduan/PANDUAN_PENGGUNA.md`

**Mau menjadikan sistem ini repo sendiri (terpisah dari repo master)?**

    python3 tools/check_selfcontained.py --sistem sistem-konten-kreator --report

Exit 0 = folder ini siap disalin apa adanya ke repo tujuan — folder = deliverable; tidak ada ZIP, tidak ada dist, tidak ada pemilihan file manual. Exit 1 = keluaran alat adalah daftar kerja di dalam folder ini (perbaiki foldernya, bukan hasil salinan sementara). Aturannya: _meta/PAKET_REPO_MANDIRI.md di master (provenance)

---

## Urutan wajar membangun sesuatu dari nol

```
0. Bikin repo GitHub baru, push skeleton folder + dokumen sistem ke main (sekali di awal)
1. 01_BRAND_CORE.md                    (sekali di awal)
2. 02_CHANNEL_DISCOVERY_PROMPT.md      (tiap channel baru)
3. 04_CHARACTER_BUILDER_KIT.md         (kalau channel itu butuh elemen konsistensi visual)
4. 07_MODEL_KONTEN_DISCOVERY_PROMPT.md (tiap cara produksi baru dalam channel itu)
5. 05_CONTENT_PRODUCTION_PIPELINE.md   (produksi harian, berulang terus)
```

Setiap sesi baru (kecuali lanjut di jendela chat yang sama), Entry Point Universal akan menuntun otomatis — cek PR menggantung, tanya tujuan sesi ini, baca file relevan sendiri. Lihat `00_CARA_PAKAI_SISTEM.md` untuk peta lengkap dan penjelasan setiap dokumen.
