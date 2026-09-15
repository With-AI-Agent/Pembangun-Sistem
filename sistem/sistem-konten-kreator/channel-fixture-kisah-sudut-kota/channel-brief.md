# Channel Brief — Kisah Sudut Kota (FIXTURE)

> **FIXTURE — bukan channel produksi sungguhan.** Bagian dari state uji backlog G-1 (clean-run 0.3.10) — channel kedua milik sistem ini. Rujukan state: `ACCEPTANCE_TEST_LOG.md` (bagian "Persiapan G-1").
>
> **Gap warisan: SUDAH DITUTUP 2026-09-15.** Channel ini pernah menyatakan gap warisan `indeks-karakter.md` (arsip disiapkan sebelum aturan indeks karakter berlaku). Berkas `arsip-naskah/indeks-karakter.md` kemudian benar-benar dibuat pada **2026-09-11** (dipicu Tahap 6 konten "Jumat Tanpa Jagung di Sudut Stasiun") dan kini berisi 1 entri karakter Tipe B. Pernyataan gap di header, kotak checklist, dan bagian 9 baru disinkron pada **2026-09-15** (G2-c) — selama 4 hari dokumen ini menyatakan gap yang sebenarnya sudah tidak ada. Catatan historis di `ACCEPTANCE_TEST_LOG.md`, `UJI_G1_CLEAN_RUN_2026-09-09.md`, dan `SYSTEM_MANIFEST.md` **tidak diubah** karena merekam keadaan pada tanggalnya masing-masing.

### Dokumen "hidup" milik SATU channel, mengikuti struktur `_sistem/03_TEMPLATE_CHANNEL_BRIEF.md`.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — sudah digali
- [x] **Reviewed** — sudah dibaca lengkap, koreksi masuk
- [x] **Approved** — isi dikunci lewat gerbang **G2** 2026-09-09
- [x] **Merged** — masuk `main` lewat gerbang **G3** 2026-09-09 — git-true setelah PR prep di-merge (pola fixture Run-1)
- [x] **Operational** — sudah `Merged` dan seluruh dependency ada; pengecualian gap warisan **ditutup 2026-09-15** (lihat header)

> **Catatan fixture (pola Run-1):** klaim `Merged`/`Operational` di dokumen ini git-true setelah PR persiapan di-merge ke `main`. Sampai merge, berkas ini masih di branch.

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Semua pertanyaan di checklist konsistensi (bagian 6) sudah dijawab
- [x] Setiap elemen visual yang ditandai wajib sudah berstatus `Reference-Ready` — **tidak ada elemen visual yang ditandai wajib** untuk channel ini (lihat bagian 4), jadi tidak ada file acuan yang harus ada
- [x] `arsip-naskah/indeks.md` dan `arsip-naskah/indeks-karakter.md` sudah dibuat (boleh kosong) — **dua-duanya sudah ada**: `indeks.md` 1 entri naskah, `indeks-karakter.md` 1 entri karakter Tipe B (dibuat 2026-09-11)
- [x] Sudah `Merged` ke `main` — git-true setelah PR prep di-merge (pola fixture Run-1)

**Versi:** `3` — **Terakhir diperbarui:** `2026-09-15` — **Diwarisi dari:** `_sistem/01_BRAND_CORE.md`

> **Catatan dependency:** `_sistem/01_BRAND_CORE.md` di repo ini **masih template kosong** (belum pernah dijalankan sesi Brand Core). Brief fixture ini karena itu tidak benar-benar mewarisi apa pun dari Brand Core. Ini dicatat sadar, bukan disembunyikan — agent yang membaca brief ini wajib melaporkan gap tersebut, bukan berpura-pura konteksnya lengkap.

---

## 1. Identitas Channel

- **Nama channel:** Kisah Sudut Kota (fixture)
- **Platform utama:** YouTube Shorts + TikTok
- **Format teknis:** [x] Short-form

## 2. Niche & Positioning

- **Topik inti:** cerita kecil dari sudut-sudut kota — warung, lorong, halte, gerbang gang — dan orang-orang biasa yang menempel di sudut itu; bukan tokoh besar, bukan sejarah resmi.
- **Masalah/kebutuhan/hiburan yang dipenuhi:** penonton merasa kotanya sendiri dikenali lagi — "ternyata sudut itu punya cerita" — dalam 60 detik, tanpa perlu pengetahuan khusus.
- **Target penonton:** orang 20-35 tahun yang hidup di kota, suka cerita pendek yang membuat mereka berhenti sebentar.
- **Apa yang bikin channel ini beda:** sudut pandangnya selalu dari SUKUT (tempat), bukan dari orang; tokoh hanya lewat sebagai bagian dari sudut itu, bukan pembicaranya.
- **Referensi/kompetitor yang relevan:** kanal dokumenter jalanan pendek berbahasa Indonesia (dipelajari cara mereka memotret sudut tanpa menggurui, bukan ditiru topiknya).

## 3. Persona & Voice Channel

- **Siapa "suara" di balik channel ini?** [x] Narator/voice over tanpa wujud visual tetap
- **Gaya bahasa:** netral-warm, kalimat pendek, tanpa basa-basi. Contoh: *"Halte itu tidak pernah ramai. Yang ramai selalu orang-orang yang menunggu di sana."*
- **Tone emosional dominan:** tenang, sedikit kagum, tanpa dramatisasi.
- **Kosakata/frasa khas:** "sudut", "menempel", "yang lewat", "tanpa nama", "kota yang sama".
- **Karakteristik suara/voice:** suara dewasa muda, tempo sedang (± 130 kata/menit), jeda 0,5 detik tiap ganti gagasan.
- **Hal yang HARUS ADA di setiap konten:** satu sudut kota konkret sebagai pintu masuk; penutup yang mengajak penonton melihat sudut terdekatnya sendiri.
- **Hal yang TIDAK BOLEH ADA:** klaim faktual yang tidak bisa dirujuk (angka, tanggal pasti, nama resmi); nama tokoh nyata; nada menggurui; clickbait yang menjanjikan sesuatu yang tidak ada di naskah.
- **Contoh kalimat pembuka/penutup khas:** pembuka — *"Di sudut [tempat], ada satu kebiasaan yang tidak pernah berubah."*; penutup — *"Lain kali kamu lewat situ, lihat pelan-pelan. Kota ini tidak pernah bercerita dua kali."*

## 4. Konsistensi Visual

**Karakter — Tipe A (Karakter Utama Channel)**

> Tidak berlaku untuk channel ini — channel faceless, tidak ada karakter berwujud yang muncul berulang.

**Karakter — Tipe B (Karakter Per-Konten)**

> Catatan pengingat saja: kalau ada tokoh yang "diceritakan" dalam satu konten, dia Tipe B — dicek dulu ke `arsip-naskah/indeks-karakter.md` sebelum dibuat baru (lihat bagian A2 di `_sistem/06_PROMPT_LIBRARY.md`).

**Latar/Lingkungan**

> [x] Tidak berlaku sebagai **elemen Bank Konsistensi Visual** — tiap konten punya sudut kotanya sendiri; tidak ada satu setting tetap yang dikunci.

**Palet Warna & Gaya Render**

> [x] Tidak berlaku untuk channel ini sebagai **elemen Bank Konsistensi Visual** — tidak ada file acuan yang dikunci. Gaya visualnya cukup dinyatakan deskriptif di bagian 5, karena tidak ada karakter yang perlu dijaga kemiripannya antar konten.

**Props/Objek Berulang**

> [x] Tidak berlaku untuk channel ini — tiap sudut punya benda miliknya sendiri, tidak ada props tetap lintas konten.

## 5. Gaya Visual

- **Referensi visual/mood:** foto jalanan pagi, cahaya lembut, bayangan panjang; tekstur film ringan, warna tidak jenuh.
- **Palet warna dominan:** abu aspal, kuning pagi, biru pudar, oranye lampu sodium.
- **Pendekatan generate visual untuk channel ini:** b-roll sudut kota + siluet/latar belakang orang (dari belakang/samping, wajah tidak detail); tidak memakai reference image dari `konsistensi-visual/` karena tidak ada elemen yang dikunci di sana.
- **Hal yang harus dihindari secara visual:** wajah orang yang bisa dikenali, logo merek, teks besar di layar.

## 6. Area Berisiko Tinggi

- Tokoh gampang jadi "pahlawan kecil" yang didramatisasi — jaga agar sudut yang bercerita, orangnya hanya menempel.
- Elemen kota yang spesifik (nama jalan, halte resmi) gampang lolos sebagai klaim faktual — hindari nama resmi; pakai gambaran umum.
- Gaya bahasa gampang jadi sinetron kalau kalimatnya terlalu panjang — kunci "kalimat pendek".

## 7. Bank Ide Awal

- Warung kopi yang pindah tiga kali tanpa ganti nama
- Lorong belakang halte yang lebih ramai dari haltenya
- Gerbang gang yang selalu terbuka, padahal tidak ada yang jaga
- Juru parkir tua yang masih mencatat dengan buku kertas

## 8. Model Konten dalam Channel Ini

| Nama Model Konten | Folder | Status |
|---|---|---|
| Narasi 60 Detik | `model-konten/narasi-60-detik/` | `Operational` |
| Kartu Teks 8–10 | `model-konten/kartu-teks-8-10/` | `Approved` |

## 9. Arsip Naskah

Naskah final disimpan di `arsip-naskah/` folder ini. Kedua indeks **sudah ada dan sudah berisi**:

- `indeks.md` — 1 entri: *Jumat Tanpa Jagung di Sudut Stasiun* (2026-09-11).
- `indeks-karakter.md` — dibuat 2026-09-11 (menutup gap warisan), 1 entri: *Nenek Penjual Jagung Rebus* (Tipe B).

> **Koreksi 2026-09-15 (G2-c):** bagian ini sebelumnya masih menulis "`indeks.md` … masih kosong" dan "`indeks-karakter.md` belum pernah dibuat". Dua-duanya sudah tidak benar sejak 2026-09-11. Diperbaiki setelah diverifikasi langsung terhadap berkasnya, bukan dari ingatan. Lihat header untuk jejak gap warisan.

## 10. Log Keputusan Channel

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-09 | Channel Brief fixture dikunci (G2) dan di-merge (G3) | Status dokumen: `Operational` dengan pengecualian terdakwa; klaim Merged git-true setelah PR prep di-merge (pola fixture Run-1) |
| 2026-09-09 | Semua elemen Konsistensi Visual ditandai "tidak berlaku" | Channel faceless; tidak ada elemen visual yang mewajibkan file acuan |
| 2026-09-09 | Gap warisan dinyatakan: indeks-karakter.md belum pernah dibuat | Arsip disiapkan sebelum aturan indeks karakter berlaku; dinyatakan apa adanya di header + bagian 9 |
| 2026-09-15 | Channel Brief v2 — tambah entri model `Kartu Teks 8–10` pada tabel Model Konten (status `Draft`) | Model konten teks-only baru (8–10 kartu teks, tanpa gambar/video/audio) hasil `07_MODEL_KONTEN_DISCOVERY_PROMPT.md`; status masih `Draft` karena menunggu G2 pemilik dan belum `Merged`. Mengikuti pola penambahan model `Narasi Riset 60 Detik` di channel `channel-fixture-narasi-sejarah` |
| 2026-09-15 | Channel Brief v3 — **gap warisan `indeks-karakter.md` DITUTUP**; header, kotak checklist, dan bagian 9 disinkron ke keadaan sebenarnya (**G2-c**) | Berkas `arsip-naskah/indeks-karakter.md` sudah benar-benar ada sejak **2026-09-11** (1 entri: Nenek Penjual Jagung Rebus) dan `indeks.md` sudah berisi 1 naskah, tetapi dokumen ini selama 4 hari tetap menyatakannya sebagai gap yang belum ditutup. Ditemukan saat entry point sesi `arena/01a0a448`; diperbaiki setelah pemilik memilih "perbaiki sekarang". Aman terhadap `validate_system.py`: marker `GAP_WARISAN_MARKER` hanya dibaca kalau `indeks-karakter.md` **tidak ada** (baris 166–170), jadi pencabutan pernyataan gap tidak melonggarkan gerbang — diverifikasi dengan menjalankan ulang validator, bukan diasumsikan. Catatan historis di `ACCEPTANCE_TEST_LOG.md` / `UJI_G1_CLEAN_RUN_2026-09-09.md` / `SYSTEM_MANIFEST.md` sengaja tidak diubah (append-only, merekam keadaan pada tanggalnya) |
