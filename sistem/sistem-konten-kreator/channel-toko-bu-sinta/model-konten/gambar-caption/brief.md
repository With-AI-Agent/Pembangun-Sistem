# Model Konten Brief — Gambar Statis & Caption (Channel: Toko Bu Sinta)

### Dokumen "hidup" milik SATU model konten dalam SATU channel. Hasil dari `07_MODEL_KONTEN_DISCOVERY_PROMPT.md` ditulis mengikuti struktur ini, disimpan sebagai `channel-toko-bu-sinta/model-konten/gambar-caption/brief.md`. **Dibaca BERSAMAAN dengan Channel Brief channel-nya** di setiap sesi produksi konten format ini — dokumen ini TIDAK mengulang isi Channel Brief, hanya menambahkan yang spesifik di level ini.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — digali via Model Konten Discovery 2026-09-17 (slot log 20)
- [x] **Reviewed** — disajikan untuk dibaca lengkap oleh pemilik via viewer
- [x] **Approved** — isi dikunci lewat gerbang **G2** 2026-09-17 oleh pemilik
- [ ] **Merged** — PR sudah lewat gerbang **G3** dan masuk ke `main`
- [ ] **Operational** — sudah `Merged` DAN semua dependency wajibnya benar-benar ada

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder tersisa)
- [x] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan (unit kerja: 1 frame gambar visual tunggal + naskah caption 3–6 baris)
- [x] Override terhadap Channel Brief dinyatakan eksplisit (mewarisi penuh, tidak ada override tone/voice)
- [x] Gerbang tambahan dicatat (tetap mempertahankan G1/G2 standar pipeline)
- [ ] Channel Brief induknya sudah berstatus `Operational` (saat ini `Approved` di branch aktif)
- [ ] Sudah `Merged` ke `main`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-17`

## Mewarisi dari: `channel-toko-bu-sinta/channel-brief.md`

*(Semua yang sudah dikunci di sana — Persona & Voice, Konsistensi Visual Bu Sinta — otomatis berlaku di sini kecuali dinyatakan override eksplisit di bawah.)*

---

## 1. Identitas Model Konten

- **Nama model konten:** Gambar Statis & Caption
- **Definisi singkat:** Format unggahan Instagram Feed berupa 1 gambar ilustrasi flat (rasio 1:1) yang didampingi narasi caption pendek 3–6 baris bernuansa *slice-of-life* hangat, berfokus pada sudut pandang mikro keseharian toko kelontong.

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** 1 gambar statis (persegi 1:1) + teks caption 3–6 baris (sekitar 30–65 kata). Tanpa video, tanpa audio / voice over.
- **Struktur konten khas format ini:**
  - *Baris 1–2:* Pengamatan detail pada benda fisik atau suasana toko (misal: stoples kaca, timbangan beras, bunyi bel, pantulan cahaya).
  - *Baris 3–4:* Interaksi kecil atau ucapan singkat bersahaja dari Bu Sinta.
  - *Baris 5–6:* Refleksi penutup pendek yang hangat, tenang, tanpa ajakan bertindak (hard CTA) yang agresif.
- **Platform paling cocok untuk format ini:** Instagram post feed (rasio aspek 1:1, square image).

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** Ilustrasi 2D flat (*flat illustration*), warna lembut teredam (*soft muted earth tones*: mustard, krem, kayu hangat, hijau sage, aksen selendang merah), pencahayaan alami hangat pagi atau sore hari.
- **Kalau ada elemen Konsistensi Visual dari channel (Bu Sinta) — cara tampil di format ini:** Bu Sinta WAJIB tampil di setiap gambar post. Wujud visual Bu Sinta mengacu langsung ke Bank Konsistensi Visual (`konsistensi-visual/bu-sinta/`) dengan Prompt Master dan gambar referensi `acuan-utama.png`. Latar toko dan printilan benda hadir alami sebagai pendukung adegan tanpa folder reference pack terpisah.

## 4. Alur Kerja Produksi

**Mode:** [x] Ikuti Kerangka Standar (dengan override ringan)  /  [ ] Alur Kerja Kustom

### Kalau Mode = Ikuti Kerangka Standar

- **Override Persona/Voice:** Tidak ada override. Mewarisi penuh Persona & Voice di Channel Brief (narator orang ketiga yang hangat seperti teman lama, santai, bersahaja, tanpa bahasa gaul).
- **Bentuk konkret Tahap Breakdown untuk format ini:** Unit kerja adalah **Post Visual Tunggal** (`unit-1`, 1 gambar ilustrasi flat 1:1). Berkas dinamai `breakdown-output.md`.
- **Override Ringan per Tahap:**
  - **Tahap 1 (Ideation):** Mengambil atau mengembangkan 1 ide dari Bank Ide Awal / observasi mikro toko kelontong, selalu memeriksa `arsip-naskah/indeks.md` untuk menghindari duplikasi topik.
  - **Tahap 2 (Konsep & Angle):** Menentukan fokus benda/interaksi kecil, momen kehadiran Bu Sinta, dan suasana waktu (pagi/siang/sore).
  - **Tahap 3 (Naskah/Script):** Menulis naskah caption pendek (3–6 baris) dengan struktur 3 ketukan (pengamatan benda, ucapan Bu Sinta, refleksi penutup). Jika melibatkan tokoh pelanggan baru (Tipe B), deskripsikan secara ringkas dan cek `arsip-naskah/indeks-karakter.md`.
  - **Tahap 4 (Breakdown Output):** Menyusun 1 unit visual di `breakdown-output.md` berisi nomor unit, kutipan naskah, deskripsi adegan visual 1:1, prompt generate gambar terintegrasi (Prompt Master Bu Sinta + deskripsi situasi spesifik), dan file acuan yang wajib disertakan (`acuan-utama.png`).
  - **Tahap 5 (Generate/Acquire Assets):** Menjalankan `generate_image` untuk menghasilkan 1 berkas gambar di `_produksi-aktif/[channel]-[judul]/assets/`. Catat prompt, file referensi, dan output ke log sesi & STATUS.
  - **Tahap 6 (Assembly & Publish Prep):** Finalisasi caption Instagram, rekomendasi 3–5 hashtag relevan, pengarsipan naskah ke `arsip-naskah/[tanggal]-[judul].md` dan metadata reproduksibilitas ke `arsip-naskah/[tanggal]-[judul]-metadata.md`.

## 5. Contoh Konkret

- **Judul/Tema:** Stoples Kopi Tua
- **Visual:** Bu Sinta berdiri tersenyum tipis di balik meja kasir kayu, tangannya sedang memegang toples kaca tua berisi biji kopi hitam. Di atas meja ada cangkir seng berbingkai hijau dan timbangan kuno. Cahaya sore keemasan menerangi butiran debu di udara toko.
- **Naskah Caption (5 baris):**
  > Stoples kaca di sudut meja kasir ini sudah ada bahkan sebelum cat kusen pintu diganti.
  > Biji kopi di dalamnya tidak pernah benar-benar habis; Bu Sinta selalu mengisi ulang sebelum dasarnya tampak.
  > "Pelan-pelan aja," ucapnya sambil menyendok dua takar ke kantong kertas, "kopi yang buru-buru itu hilang sedapnya."
  > Sore mulai turun dan lampu jalan di depan toko berkedip menyala.
  > Di toko kami, waktu selalu berjalan sedikit lebih tenang.

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-17 | Inisiasi Model Konten Brief "Gambar Statis & Caption" (folder: `gambar-caption/`) | Format unggulan channel Toko Bu Sinta di Instagram feed. |
| 2026-09-17 | Mode: Kerangka Standar dengan unit breakdown 1 Post Visual Tunggal | Alur linear dan sederhana, cocok untuk produksi feed harian berbasis 1 gambar + caption 3-6 baris. |
| 2026-09-17 | G1 Lulus & G2 Approved — Model Konten Brief v1 dikunci resmi | Pemilik menyetujui penuh draft tanpa revisi. |
