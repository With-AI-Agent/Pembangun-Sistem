# Channel Brief — Narasi Sejarah (FIXTURE)

> **FIXTURE — bukan channel produksi sungguhan.** Bukan penutup temuan L-04.
>
> **Status uji:** AT-KK-05 / Run 4 **GAGAL**, `0.3.2-warisan-sync`; AT-KK-05 / Run 5 dan AT-KK-05b / Run 6 **dijadwalkan**, `0.3.3`. Rujukan: [ACCEPTANCE_TEST_LOG.md](../ACCEPTANCE_TEST_LOG.md).

### Dokumen "hidup" milik SATU channel, mengikuti struktur `_sistem/03_TEMPLATE_CHANNEL_BRIEF.md`.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — sudah digali
- [x] **Reviewed** — sudah dibaca lengkap, koreksi masuk
- [x] **Approved** — isi dikunci lewat gerbang **G2** 2026-09-04
- [x] **Merged** — masuk `main` lewat gerbang **G3** 2026-09-04
- [x] **Operational** — sudah `Merged` dan semua dependency wajib ada (lihat Checklist Kelengkapan)

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Semua pertanyaan di checklist konsistensi (bagian 6) sudah dijawab
- [x] Setiap elemen visual yang ditandai wajib sudah berstatus `Reference-Ready` — **tidak ada elemen visual yang ditandai wajib** untuk channel ini (lihat bagian 4), jadi tidak ada file acuan yang harus ada
- [x] `arsip-naskah/indeks.md` dan `arsip-naskah/indeks-karakter.md` sudah dibuat (boleh kosong) — keduanya ada di folder ini
- [x] Sudah `Merged` ke `main`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-04` — **Diwarisi dari:** `_sistem/01_BRAND_CORE.md`

> **Catatan dependency:** `_sistem/01_BRAND_CORE.md` di repo ini **masih template kosong** (belum pernah dijalankan sesi Brand Core). Brief fixture ini karena itu tidak benar-benar mewarisi apa pun dari Brand Core. Ini dicatat sadar, bukan disembunyikan — agent yang membaca brief ini wajib melaporkan gap tersebut, bukan berpura-pura konteksnya lengkap.

---

## 1. Identitas Channel

- **Nama channel:** Narasi Sejarah (fixture)
- **Platform utama:** YouTube Shorts + TikTok
- **Format teknis:** [x] Short-form

## 2. Niche & Positioning

- **Topik inti:** cerita kecil dari sejarah sehari-hari orang biasa — bukan tokoh besar, bukan tanggal perang, tapi benda, kebiasaan, dan ruang yang diam-diam membentuk hidup orang banyak.
- **Masalah/kebutuhan/hiburan yang dipenuhi:** penonton dapat rasa "ternyata hidupku punya sejarah juga" dalam 60 detik, tanpa perlu latar pengetahuan sejarah.
- **Target penonton:** orang 25-40 tahun yang suka cerita pendek bernuansa nostalgia, bukan penggemar sejarah akademis.
- **Apa yang bikin channel ini beda:** sudut pandangnya selalu dari benda/ruang, bukan dari peristiwa; tidak ada nama tokoh, tidak ada angka tahun sebagai hook.
- **Referensi/kompetitor yang relevan:** channel narasi nostalgia berbahasa Indonesia (dipelajari cara mereka menahan penonton di 10 detik pertama, bukan ditiru topiknya).

## 3. Persona & Voice Channel

- **Siapa "suara" di balik channel ini?** [x] Narator/voice over tanpa wujud visual tetap
- **Gaya bahasa:** santai tapi tertata, kalimat pendek, banyak jeda. Contoh: *"Meja itu tidak pernah pindah. Yang pindah, orang-orang yang duduk di sekitarnya."*
- **Tone emosional dominan:** hangat & agak melankolis, tanpa mendramatisir.
- **Kosakata/frasa khas:** "dulu", "konon", "yang tersisa", "tidak ada yang mencatat".
- **Karakteristik suara/voice:** suara dewasa, tempo lambat (± 130 kata/menit), jeda 0,5 detik tiap ganti gagasan.
- **Hal yang HARUS ADA di setiap konten:** satu benda atau ruang konkret sebagai pintu masuk cerita; penutup yang mengembalikan penonton ke masa kini.
- **Hal yang TIDAK BOLEH ADA:** klaim sejarah yang tidak bisa dirujuk; nama tokoh nyata; nada menggurui; clickbait yang menjanjikan sesuatu yang tidak ada di naskah.
- **Contoh kalimat pembuka/penutup khas:** pembuka — *"Ada satu benda yang…"*; penutup — *"Sekarang benda itu sudah tidak ada. Tapi caranya mengatur hari kita, masih."*

## 4. Konsistensi Visual

**Karakter — Tipe A (Karakter Utama Channel)**

> Tidak berlaku untuk channel ini — channel faceless, tidak ada karakter berwujud yang muncul berulang.

**Karakter — Tipe B (Karakter Per-Konten)**

> Catatan pengingat saja: kalau ada tokoh yang "diceritakan" dalam satu konten, dia Tipe B — dicek dulu ke `arsip-naskah/indeks-karakter.md` sebelum dibuat baru (lihat bagian A2 di `_sistem/06_PROMPT_LIBRARY.md`).

**Latar/Lingkungan**

> [x] Tidak berlaku untuk channel ini — visual memakai b-roll/netral, tidak ada satu setting tetap yang harus konsisten.

**Palet Warna & Gaya Render**

> [x] Tidak berlaku untuk channel ini sebagai **elemen Bank Konsistensi Visual** — tidak ada file acuan yang dikunci. Gaya visualnya cukup dinyatakan deskriptif di bagian 5, karena tidak ada karakter yang perlu dijaga kemiripannya antar konten.

**Props/Objek Berulang**

> [x] Tidak berlaku untuk channel ini — tiap konten punya bendanya sendiri, tidak ada props tetap lintas konten.

## 5. Gaya Visual

- **Referensi visual/mood:** footage arsip dan foto benda sehari-hari, warna cenderung hangat dan sedikit pudar, tekstur film.
- **Palet warna dominan:** cokelat kayu, krem, hijau tua pudar.
- **Pendekatan generate visual untuk channel ini:** b-roll netral + foto benda; tidak memakai reference image dari `konsistensi-visual/` karena tidak ada elemen yang dikunci di sana.
- **Hal yang harus dihindari secara visual:** wajah orang yang bisa dikenali, logo merek, teks besar di layar.

## 6. Area Berisiko Tinggi

- Gaya bahasa gampang jadi terlalu puitis/berbunga kalau prompt tidak menegaskan "kalimat pendek".
- Narator gampang terdengar menggurui kalau naskah memakai kalimat penjelasan panjang.
- Topik gampang bergeser jadi "sejarah tokoh besar" kalau tidak diingatkan bahwa pintu masuknya selalu benda/ruang.
- Klaim sejarah gampang menyusup tanpa sumber — setiap konten wajib lewat gerbang sumber eksternal di `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md`.

## 7. Bank Ide Awal

- Tiga benda di meja nenek yang mengatur ritme rumah
- Kenapa jam dinding dulu selalu dipasang di ruang tamu
- Seragam sekolah dan apa yang hilang dari foto kelas

## 8. Model Konten dalam Channel Ini

| Nama Model Konten | Folder | Status |
|---|---|---|
| Narasi 60 Detik | `model-konten/narasi-60-detik/` | `Operational` |

## 9. Arsip Naskah

Naskah final disimpan di `arsip-naskah/` folder ini. `indeks.md` (judul/tanggal/topik) dan `indeks-karakter.md` (karakter Tipe B) keduanya sudah dibuat dan masih kosong — channel fixture ini belum punya konten yang sampai Tahap 6.

## 10. Log Keputusan Channel

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-04 | Channel Brief fixture dikunci (G2) dan di-merge (G3) | Status dokumen: `Operational`, v1 |
| 2026-09-04 | Semua elemen Konsistensi Visual ditandai "tidak berlaku" | Channel faceless; tidak ada elemen visual yang mewajibkan file acuan |
