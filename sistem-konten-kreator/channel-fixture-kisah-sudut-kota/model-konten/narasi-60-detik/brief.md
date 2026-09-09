# Model Konten Brief — Narasi 60 Detik (Channel: Kisah Sudut Kota) (FIXTURE)

> **FIXTURE — bukan model konten produksi sungguhan.** Bagian dari state uji backlog G-1 (clean-run 0.3.9). Rujukan state: `ACCEPTANCE_TEST_LOG.md` (bagian "Persiapan G-1").

### Dokumen "hidup" milik SATU model konten, dibaca BERSAMAAN dengan Channel Brief channel-nya.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft**
- [x] **Reviewed**
- [x] **Approved** — dikunci lewat gerbang **G2** 2026-09-09
- [x] **Merged** — masuk `main` lewat gerbang **G3** 2026-09-09
- [x] **Operational** — sudah `Merged` dan semua dependency wajib ada

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan — unit kerjanya **segmen narasi** (lihat bagian 4)
- [x] Override terhadap Channel Brief sudah dinyatakan eksplisit — tidak ada override
- [x] Gerbang tambahan sudah dicatat — **tidak ada gerbang tambahan**; G2/G3 bawaan tetap berlaku
- [x] Channel Brief induknya sudah berstatus `Operational`
- [x] Sudah `Merged` ke `main`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-09`

## Mewarisi dari: `channel-fixture-kisah-sudut-kota/channel-brief.md`

Semua yang dikunci di sana (Persona & Voice, bagian 4-6) berlaku di sini tanpa override.

---

## 1. Identitas Model Konten

- **Nama model konten:** Narasi 60 Detik
- **Definisi singkat:** satu cerita sudut kota, dinarasikan voice over, durasi ± 60 detik, visual berupa b-roll sudut kota + siluet/latar belakang orang (wajah tidak detail). Satu-satunya model konten channel ini saat ini.

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** 55-65 detik (± 130-145 kata naskah pada tempo 130 kata/menit)
- **Struktur konten khas format ini:** sudut kota sebagai pintu masuk (0-8 dtk) → kebiasaan yang menempel di sudut itu (8-35 dtk) → yang berubah (35-52 dtk) → penutup yang mengajak penonton melihat sudut terdekatnya (52-60 dtk)
- **Platform paling cocok:** YouTube Shorts, TikTok

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** b-roll sudut kota + siluet/latar belakang orang (dari belakang/samping, wajah tidak detail); tidak ada animasi, tidak ada karakter tetap.
- **Elemen Konsistensi Visual dari channel:** tidak ada yang perlu ditampilkan — channel ini tidak mengunci elemen visual apa pun.

## 4. Alur Kerja Produksi

**Mode:** [x] Ikuti Kerangka Standar (dengan override ringan)

### Kalau Mode = Ikuti Kerangka Standar

- **Override Persona/Voice:** tidak ada — sama seperti Channel Brief.
- **Bentuk konkret Tahap Breakdown untuk format ini:** **segmen narasi** — naskah dipecah per potongan narasi yang cocok dengan satu potongan b-roll (bukan shot, bukan panel). File breakdown disimpan sebagai `breakdown-output.md` di folder produksi.
- **Override Ringan per Tahap:**
  - Tahap 1 (Ideation): tidak ada override
  - Tahap 2 (Konsep & Angle): tidak ada override
  - Tahap 3 (Naskah/Script): tidak ada override, plus batasan panjang 130-145 kata
  - Tahap 4 (Breakdown Output): unit = **segmen narasi**; kolom prompt generate dan file referensi visual diisi deskripsi b-roll, bukan prompt generate karakter
  - Tahap 5 (Generate/Acquire Assets): asset digenerate sebagai b-roll sudut kota (still frame), bukan dari prompt karakter
  - Tahap 6 (Assembly & Publish Prep): tidak ada override

### Kalau Mode = Alur Kerja Kustom

Tidak berlaku — model ini mengikuti kerangka standar.

## 5. Contoh Konkret

Belum ada konten — channel fixture ini baru disetup. Contoh struktur yang diharapkan: pintu masuk = sudut warung kopi; konteks = kebiasaan pemiliknya mencatat pesanan di buku kertas; yang berubah = buku itu makin tebal, pelanggan makin sedikit; penutup = *\"Lain kali kamu lewat situ, lihat pelan-pelan.\"*

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-09 | Model Konten Brief fixture dikunci (G2) dan di-merge (G3) | Sesi produksi wajib membaca Model Konten Brief; tanpa itu konteks wajib tabel \"Produksi konten\" tidak lengkap |
| 2026-09-09 | Unit breakdown ditetapkan sebagai \"segmen narasi\", bukan \"shot\" | Format ini narasi + b-roll, bukan video bershot; menetapkan bentuk unit di depan mencegah agent mengasumsikan \"shot\" (lihat `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md` Tahap 4) |
