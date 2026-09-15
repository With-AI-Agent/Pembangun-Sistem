# Model Konten Brief — Data 60 Detik (Channel: Kata Data)

### Dokumen "hidup" milik SATU model konten, dibaca BERSAMAAN dengan Channel Brief channel-nya.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — digali via Model Konten Discovery mode (b) 2026-09-15 (1 putaran, semua rekomendasi agen disetujui pemilik)
- [ ] **Reviewed** — sudah dibaca lengkap oleh pengguna, koreksi sudah masuk (belum tentu final)
- [ ] **Approved** — isi dikunci lewat gerbang **G2**, tapi masih di branch/PR
- [ ] **Merged** — PR sudah lewat gerbang **G3** dan masuk ke `main`
- [ ] **Operational** — sudah `Merged` DAN semua dependency wajibnya benar-benar ada (lihat Checklist Kelengkapan di bawah). Hanya status ini yang boleh dipakai untuk mulai produksi.

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan — unit kerjanya **frame** (lihat bagian 4)
- [x] Override terhadap Channel Brief sudah dinyatakan eksplisit — tidak ada override Persona & Voice; struktur 4 beat baku (hook → konteks → artinya → kartu sumber)
- [x] Gerbang tambahan sudah dicatat — tidak ada gerbang tambahan; G2/G3 bawaan tetap; fact-check gate di Tahap 0 dan Tahap 3 sesuai pipeline
- [ ] Channel Brief induknya sudah berstatus `Operational` — brief induk Approved, menunggu Merged
- [ ] Sudah `Merged` ke `main`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-15`

## Mewarisi dari: `channel-kata-data/channel-brief.md`

Semua yang dikunci di sana (Persona & Voice narator santai-cerdas 150-160 kata/menit, Konsistensi Visual `palet-gaya-data` Reference-Ready, aturan keras anti-hoaks data) berlaku di sini tanpa override, kecuali yang dinyatakan eksplisit di bawah.

---

## 1. Identitas Model Konten

- **Nama model konten:** Data 60 Detik
- **Definisi singkat:** satu angka/temuan data Indonesia terverifikasi per episode, dinarasikan voice over santai-cerdas 30-60 detik (±75-150 kata), visual murni motion-infografis dari elemen `palet-gaya-data` (angka hero, bar/donut, kartu sumber). Satu-satunya model konten channel ini untuk fase awal.

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** 30-60 detik, setara ±75-150 kata naskah pada tempo 150-160 kata/menit. Hook angka wajib di 0-3 detik.
- **Struktur konten khas format ini:** 4 beat baku, selalu urut: (1) Hook angka (0-3 dtk) — angka utama langsung, tanpa basa-basi; (2) Konteks (3-25 dtk) — datanya apa, dari mana, tahun berapa; (3) "Artinya" (25-50 dtk) — terjemahan angka ke hidup sehari-hari penonton (konversi satuan, perbandingan, "setara dengan"); (4) Kartu sumber + penutup (50-60 dtk) — kartu sumber on-screen + kalimat "Kata data, [kesimpulan]. Sumber: [lembaga, tahun]."
- **Platform paling cocok untuk format ini:** TikTok + Instagram Reels (sekunder: YouTube Shorts) — vertikal 9:16.

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** motion-infographic flat — tiap frame digambar ulang konsisten (bukan screenshot, bukan clip-art); generate via agent dengan Prompt Master + acuan `palet-gaya-data`; perakitan frame menjadi video final dikerjakan di tools eksternal (agent belum bisa generate video langsung).
- **Kalau ada elemen Konsistensi Visual dari channel:** elemen `palet-gaya-data` tampil sama seperti biasanya (Prompt Master + acuan `style-sheet.png` + `palet.png`); tidak ada penyesuaian — tidak ada folder `assets/` di model konten ini.

## 4. Alur Kerja Produksi

**Mode:** [ ] Ikuti Kerangka Standar (dengan override ringan)  /  [x] Alur Kerja Kustom

### Kalau Mode = Ikuti Kerangka Standar

Tidak berlaku — model ini memakai Alur Kerja Kustom (lihat bawah).

### Kalau Mode = Alur Kerja Kustom

- **Kenapa model konten ini butuh alur kustom (beda dari kerangka standar):** Setiap episode membawa angka statistik spesifik — klaim berisiko yang menurut `05_CONTENT_PRODUCTION_PIPELINE.md` wajib punya minimal 2 sumber independen. Pipeline standar baru melakukan fact-check di Tahap 3 (Naskah) sebagai gerbang G2, tapi untuk channel ini riset dan verifikasi harus terjadi SEBELUM ideation final dan konsep, supaya ide yang dipilih sudah berdiri di atas angka terverifikasi (bukan ide dulu baru cari data pembenaran). Jadi ada Tahap 0 Riset & Verifikasi Data yang mendahului Ideation. Ini bukan ekstraksi massal (1 sumber jadi banyak konten), tapi verifikasi data per episode. Preseden yang sama di repo: model Narasi 60 Detik (`channel-kamu-tau-ga`) dan model Narasi Riset (fixture narasi-sejarah).

- **Tahapan alur kerja:**

| No | Nama Tahap | Input | Proses/Tools | Output |
|---|---|---|---|---|
| 0 | Riset & Verifikasi Data | Topik dari Bank Ide Awal atau observasi baru | Web search (depth 2-3), kumpulkan minimal 2 sumber independen untuk angka utama; catat di SUMBER.md (klaim, sumber, tanggal akses, status verifikasi, lisensi, atribusi); turunkan bahasa/labeli tahun kalau data basi atau tak terverifikasi | `SUMBER.md` awal + ringkasan data terverifikasi (angka + satuan + sumber + tahun) + daftar yang belum terverifikasi (kalau ada) |
| 1 | Ideation | Ringkasan data terverifikasi + `arsip-naskah/indeks.md` (cek pengulangan topik) + Bank Ide | Pilih 1 angka utama + susun 2-3 opsi angle "artinya buat kamu" (konversi/perbandingan/setara-dengan); cek indeks topik serupa | 1 ide terpilih (angka + angle "artinya") |
| 2 | Konsep & Angle | Ide terpilih + Persona & Voice Channel | Susun kerangka 4 beat baku (hook-konteks-artinya-sumber), perkiraan durasi 30-60 dtk; JANGAN keluar dari Persona & Voice dan aturan keras brief | Kerangka konten (bukan naskah penuh) |
| 3 | Naskah/Script | Kerangka + SUMBER.md awal + Persona & Voice | Tulis naskah 75-150 kata, santai-cerdas, hook angka di awal, penutup "Kata data..."; sebelum G2: tiap klaim faktual wajib punya baris di SUMBER.md dengan status verifikasi terisi (fact-check gate) | `naskah-draft.md` + SUMBER.md final |
| 4 | Breakdown Output | Naskah final + SUMBER.md + `palet-gaya-data` | Pecah naskah jadi 4-6 frame (unit = frame 9:16: hook/konteks/artinya/sumber, boleh 2 frame untuk 1 beat panjang); tiap frame: nomor, bagian naskah, deskripsi visual, prompt generate (Prompt Master elemen + detail unit), file referensi (`style-sheet.png` + `palet.png`) | `breakdown-output.md` 4-6 frame (nama file boleh `breakdown-frame.md`) |
| 5 | Generate/Acquire Assets | Breakdown-output.md | Generate frame via agent (text-to-image + referensi elemen); audit tiap frame: palet sesuai, angka cocok dengan naskah/SUMBER.md (ejaan angka!), proporsi chart jujur, kartu sumber tepat, tanpa teks liar; simpan di `_produksi-aktif/[channel]-[judul]/assets/` + CATATAN-ASSET.md | 4-6 PNG frame + CATATAN-ASSET.md |
| 6 | Assembly & Publish Prep | Naskah + assets + SUMBER.md | Rakit di tools eksternal; buat 3-5 opsi judul hook, caption Persona & Voice, hashtag, konsep thumbnail jujur; pastikan kartu sumber on-screen + atribusi wajib masuk; pindahkan naskah final ke arsip, update indeks, buat metadata.md, arsip SUMBER.md | `publish-prep.md`, arsip naskah + indeks + metadata + sumber |

- **Titik pertemuan dengan kerangka standar:** Tahap 0 adalah tambahan di depan. Setelah Tahap 0 selesai, Tahap 1-6 di atas memetakan ke kerangka standar: Tahap 1 = Tahap 1 standar, Tahap 2 = Tahap 2, Tahap 3 = Tahap 3 (G1+G2), Tahap 4 = Tahap 4 (G1+G2), Tahap 5 = Tahap 5 (G1), Tahap 6 = Tahap 6 (G2+G3). Setelah Tahap 0, ikuti definisi gerbang di `05_CONTENT_PRODUCTION_PIPELINE.md`.

- **Catatan tools yang belum pasti:** Perakitan video final + voice-over TTS dikerjakan di tools eksternal (belum dikunci satu tools); naskah + frame PNG dari repo adalah bahan baku. Rasio 9:16.

## 5. Contoh Konkret

Konten "2 Jam Hilang di Jalan Tiap Hari":
- Tahap 0 Riset: angka rata-rata waktu tempuh komuter + 2 sumber independen (mis. survei + BPS/statistik terkait) → SUMBER.md + ringkasan (angka, satuan, tahun).
- Tahap 1 Ideation: angle terpilih — konversi ke hari per tahun ("setara N hari penuh setahun — sebulan penuh hilang di jalan").
- Tahap 2 Konsep: hook "2 JAM." → konteks (datanya + sumber-tahun) → artinya (konversi + perbandingan sehari-hari) → kartu sumber + "Kata data, ...".
- Tahap 3 Naskah: ±120 kata, santai-cerdas, fact-check gate sebelum G2.
- Tahap 4 Breakdown: 4 frame (hook angka hero, bar konteks, kalkulasi "artinya", kartu sumber).
- Tahap 5 Assets: 4 PNG frame + audit angka-vs-naskah.
- Tahap 6 Publish: judul, caption, hashtag #katadata #dataseharihari, arsip + metadata + sumber.

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-15 | Model Konten Brief v1 Draft — Data 60 Detik untuk Kata Data | Discovery mode (b) 1 putaran — 30-60 dtk, struktur 4 beat baku, unit frame, alur kustom + Tahap 0 Riset |
| 2026-09-15 | Mode Alur Kerja Kustom dipilih, bukan standar | Pemilik pilih `kustom_t0` — angka statistik = klaim berisiko, verifikasi 2 sumber harus sebelum ideation (preseden: Narasi 60 Detik) |
| 2026-09-15 | Unit breakdown = frame; tanpa folder assets/; tanpa gerbang tambahan | Pemilik pilih `frame` — 1 frame = 1 layar 9:16; elemen channel tampil apa adanya |
