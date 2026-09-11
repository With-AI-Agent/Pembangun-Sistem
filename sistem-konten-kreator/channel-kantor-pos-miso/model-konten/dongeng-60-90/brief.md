# Model Konten Brief — Dongeng 60-90 Detik (Channel: Kantor Pos Miso)

### Dokumen "hidup" milik SATU model konten, mengikuti `_sistem/08_TEMPLATE_MODEL_KONTEN_BRIEF.md`. Dibaca BERSAMAAN dengan Channel Brief `../../channel-brief.md` — tidak mengulang isinya.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — digali via Model Konten Discovery 2026-09-11_3 (1 putaran)
- [ ] **Reviewed** — dibaca lengkap oleh pemilik
- [ ] **Approved** — isi dikunci lewat gerbang **G2**
- [ ] **Merged** — PR belum G3
- [ ] **Operational** — menunggu Merged + Channel Brief induk Operational

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib terisi (tidak ada placeholder `[...]`)
- [x] Bentuk detail tiap tahap pipeline untuk model ini ditetapkan (unit kerja = shot/gambar ilustrasi)
- [x] Override terhadap Channel Brief dinyatakan eksplisit (tidak ada override Persona/Voice — hanya detail eksekusi)
- [x] Gerbang tambahan: tidak menambah; G2/G3 bawaan kerangka standar tetap utuh
- [ ] Channel Brief induknya berstatus `Operational` — saat ini `Approved`, naik setelah PR merged + Reference-Ready
- [ ] Sudah `Merged` ke `main`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-11`

## Mewarisi dari: `channel-kantor-pos-miso/channel-brief.md`

*(Persona & Voice (narator dongeng pihak ketiga, 120-130 kpm, tanpa hype), aturan bersuara Miso, Bank Konsistensi Visual 4 elemen, hal yang harus dihindari visual & non-visual — semuanya berlaku di sini tanpa diulang.)*

---

## 1. Identitas Model Konten

- **Nama model konten:** Dongeng 60-90 Detik
- **Definisi singkat:** video pendek vertikal berupa RANGKAIAN GAMBAR ILUSTRASI DIAM (6-8 gambar) + VO narator tunggal + musik ambient pelan (opsional di editor) — bukan animasi, bukan motion graphic. Setiap episode = 1 cerita standalone dari Bank Ide/ide baru, selalu berporos 1 kiriman, selalu menampilkan Miso.

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** 60-90 detik (target default 75 dtk). Naskah **150-190 kata** @120-130 kpm. Konversi cepat: jumlah kata ÷ 2 ≈ detik.
- **Struktur konten khas format ini:** 4-beat — (1) **Hook kota** ±3 detik: kalimat pembuka khas + gambar pertama; (2) **Kiriman datang**: surat/paket/kartu masuk cerita; (3) **Masalah kecil**: satu salah paham / keterlambatan / alamat hilang — skalanya sekecil mungkin; (4) **Ending hangat**: konflik selesai atau diterima, ditutup kalimat penutup khas. Opsi kelonggaran "1 kalimat Miso" (aturannya di Channel Brief §3) hanya boleh ditetapkan di beat 4.
- **Platform paling cocok untuk format ini:** YouTube Shorts / TikTok / IG Reels, rasio 9:16, gambar 1080×1920 (generate 768×1376 lalu di-upscale/di-crop di editor jika perlu).

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** rangkaian STILL IMAGE bergaya picture-book (mengunci Gaya Visual Channel §5) — tiap gambar digenerate via agent dengan reference image WAJIB dari `konsistensi-visual/`; gerakan hanya Ken Burns (pan/zoom pelan ≤6%) + crossfade 0,4-0,6 dtk yang dilakukan MANUSIA di editor eksternal; tanpa teks besar on-screen selain judul opsional di 3 detik pertama.
- **Cara tampil elemen Konsistensi Visual di format ini:** SAMA seperti biasanya (tidak ada override gaya). Aturan per-episode: **Miso wajib terlihat di ≥4 dari 6-8 gambar, termasuk gambar pertama dan terakhir**; props khas (tas merah) mengikuti Miso di semua gambar dia muncul; latar wajib salah satu sudut Kota Kanala yang ter-acuan (lihat `konsistensi-visual/kota-kanala/`).

## 4. Alur Kerja Produksi

**Mode:** [x] Ikuti Kerangka Standar (dengan override ringan) / [ ] Alur Kerja Kustom

- **Override Persona/Voice:** tidak ada — persis Channel Brief §3.
- **Bentuk konkret Tahap Breakdown untuk format ini:** **shot = 1 gambar ilustrasi** (file `breakdown-output.md`; tiap shot: nomor, kalimat naskahnya, deskripsi visual, prompt gabungan, daftar file referensi, arahan VO/ken-burns).
- **Override Ringan per Tahap:**
  - Tahap 1 (Ideation): ide wajib lolos tes "1 kiriman = 1 mesin cerita" — ide tanpa kiriman sebagai penggerak ditolak; cek `arsip-naskah/indeks.md` (topik) & Bank Ide Awal brief.
  - Tahap 2 (Konsep & Angle): wajib memutuskan struktur 4-beat + KETUKSAN: di episode ini apakah kelonggaran "1 kalimat Miso" dipakai (default: tidak).
  - Tahap 3 (Naskah/Script): 150-190 kata; cek ritme: hitung kata ÷ 2 ≈ detik, harus 60-90; konten fiksi — SUMBER.md hanya wajib bila memakai bahan eksternal nyata (jarang); G2 naskah mencakup cek checklist "ending hangat".
  - Tahap 4 (Breakdown Output): 6-8 shot; kolom referensi visual terisi dari Bank Konsistensi (tidak boleh kosong; kalau shot hanya menampilkan objek, tetap rujuk palet-gaya). Tipe B yang muncul: deskripsi A2 06-PROMPT_LIBRARY dipakai persis di semua shot episode itu.
  - Tahap 5 (Generate/Acquire Assets): generate per-shot via agent dengan `images` referensi (acuan utama Miso ± reference sheet, ± latar, ± props; maksimum praktis 3-4 file/generate); hasil JPG disimpan `assets/`; checklist konsistensi per gambar (wajah/bulu Miso, warna tas, palet) sebelum G1; audio VO diproduksi pemilik di luar (TTS sesuai karakteristik §3 brief atau rekaman sendiri) — agent hanya menyiapkan naskah VO ber-anotasi jeda.
  - Tahap 6 (Assembly & Publish Prep): editan digabung pemilik di editor eksternal (CapCut/dll) — agent menyiapkan publish-prep (judul, caption dongeng, hashtag #kantorposmiso #ceritamiso, konsep thumbnail = gambar terbaik + judul kecil), arsip naskah + metadata + indeks Tipe B, lalu G2 final → PR → G3.

## 5. Contoh Konkret

Episode "Surat yang Terlambat 30 Tahun": (T1) ambil ide dari Bank Ide #4, mesin cerita = surat tua kembali. (T2) 4-beat: hook kota "Kotak pos hari ini menyimpan sesuatu yang lebih tua dari Miso"; kiriman: surat tanpa prangko di laci arsip; masalah: alamatnya sudah jadi toko roti; ending hangat: Miso membacakannya di depan toko, pemilik toko tertawa lalu menangis sedikit. Kalimat Miso: tidak dipakai. (T3) naskah 168 kata ≈ 76 dtk. (T4) 7 shot: depan kantor 08.00 → laci arsip → close-up surat → Miso bersepeda → toko roti → Miso membaca di teras → kota senja. (T5) 7 JPG dengan acuan Miso + kota-kanala + props. (T6) publish-prep + arsip; indeks-karakter menambah baris "pemilik toko roti" bila dipakai lagi.

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-11 | Model "Dongeng 60-90 Detik": rangkaian 6-8 gambar diam + VO, bukan animasi | Pilihan pemilik `gambar_rangkaian` di Discovery — produksi termurah, konsistensi paling terjaga |
| 2026-09-11 | Naskah 150-190 kata, struktur 4-beat | Pilihan pemilik `patokan_kata` — pas 60-90 dtk pada 120-130 kpm brief |
| 2026-09-11 | Mode: kerangka standar + override ringan | Pilihan pemilik `standar_override` — tidak ada tahap ekstraksi/ekstrak sumber |
| 2026-09-11 | Aturan kerapatan Miso: ≥4 dari 6-8 gambar, termasuk gambar pertama & terakhir | Implementasi "Miso muncul di setiap konten" pada level unit visual — bisa diaudit per episode |
