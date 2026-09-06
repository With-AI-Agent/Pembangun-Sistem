# Model Konten Brief — Narasi 60 Detik (Channel: Narasi Sejarah) (FIXTURE)

> **FIXTURE — bukan model konten produksi sungguhan.** Status uji: AT-KK-05 / Run 4 **GAGAL**, `0.3.2-warisan-sync`; AT-KK-05 / Run 5 **GAGAL-metode** (koreksi pasca-review 6 Sep), `0.3.3`; Run 6 lama **void**; AT-KK-05 / Run 7 **LULUS**, `0.3.4`; AT-KK-05b / Run 8 **dijadwalkan**, `0.3.4`; F7 TERBUKA. Rujukan: [ACCEPTANCE_TEST_LOG.md](../../../ACCEPTANCE_TEST_LOG.md).

### Dokumen "hidup" milik SATU model konten, dibaca BERSAMAAN dengan Channel Brief channel-nya.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft**
- [x] **Reviewed**
- [x] **Approved** — dikunci lewat gerbang **G2** 2026-09-04
- [x] **Merged** — masuk `main` lewat gerbang **G3** 2026-09-04
- [x] **Operational** — sudah `Merged` dan semua dependency wajib ada

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan — unit kerjanya **segmen narasi** (lihat bagian 4)
- [x] Override terhadap Channel Brief sudah dinyatakan eksplisit — tidak ada override
- [x] Gerbang tambahan sudah dicatat — **tidak ada gerbang tambahan**; G2/G3 bawaan tetap berlaku
- [x] Channel Brief induknya sudah berstatus `Operational`
- [x] Sudah `Merged` ke `main`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-04`

## Mewarisi dari: `channel-fixture-narasi-sejarah/channel-brief.md`

Semua yang dikunci di sana (Persona & Voice, bagian 4-6) berlaku di sini tanpa override.

---

## 1. Identitas Model Konten

- **Nama model konten:** Narasi 60 Detik
- **Definisi singkat:** satu cerita benda/ruang, dinarasikan voice over, durasi ± 60 detik, visual berupa b-roll netral. Satu-satunya model konten channel ini saat ini.

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** 55-65 detik (± 130-145 kata naskah pada tempo 130 kata/menit)
- **Struktur konten khas format ini:** benda sebagai pintu masuk (0-8 dtk) → konteks kebiasaan yang menempel pada benda itu (8-35 dtk) → yang berubah (35-52 dtk) → penutup yang mengembalikan ke masa kini (52-60 dtk)
- **Platform paling cocok:** YouTube Shorts, TikTok

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** b-roll netral + foto benda; tidak ada animasi, tidak ada karakter.
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
  - Tahap 5 (Generate/Acquire Assets): asset dikumpulkan (b-roll/stok berlisensi), bukan digenerate dari prompt karakter
  - Tahap 6 (Assembly & Publish Prep): tidak ada override

### Kalau Mode = Alur Kerja Kustom

Tidak berlaku — model ini mengikuti kerangka standar.

## 5. Contoh Konkret

Konten "Tiga Benda di Meja Nenek": pintu masuk = radio tua di sudut meja; konteks = kebiasaan mendengar siaran pagi yang mengatur jam bangun satu rumah; yang berubah = radio diganti ponsel, tapi urutan paginya sama; penutup = *"Sekarang radionya sudah tidak ada. Tapi caranya mengatur pagi kami, masih."*

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-04 | Model Konten Brief fixture dikunci (G2) dan di-merge (G3) | Sesi produksi wajib membaca Model Konten Brief; tanpa itu konteks wajib tabel "Produksi konten" tidak lengkap |
| 2026-09-04 | Unit breakdown ditetapkan sebagai "segmen narasi", bukan "shot" | Format ini narasi + b-roll, bukan video bershot; menetapkan bentuk unit di depan mencegah agent mengasumsikan "shot" (lihat `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md` Tahap 4) |
