# Bukti Uji Coba b3 — `rina-dimas-1226`

> **Apa ini:** hasil menjalankan **ROADMAP JALAN PRODUKSI PERTAMA butir (2) b3** — satu undangan
> pernikahan **fiktif/sendiri** dari Tahap 1 sampai pratinjau terbit, memakai **sistem sebagaimana
> tertulis** (dokumen 03/04/05/06/09/11), supaya tiga daftar periksa sistem **diuji di dunia nyata**,
> bukan diklaim.
> **Aturan penulisan berkas ini:** apa adanya. Yang gagal/gagal-diuji ditulis sebagai gagal-diuji.
> Kosong **bukan** "lulus" dan juga bukan "gagal" — ia "belum diukur", dan ditulis begitu.

- **Tanggal:** 2026-09-21 (UTC) · sesi slot 45
- **Pelaksana:** agent (langkah mekanis) + **pemilik** (langkah yang butuh mata & HP — masih menunggu)
- **Lingkungan:** sandbox sesi; server pratinjau nyata di `https://8080-i2b08gpk69xbcgdahr1nq.e2b.app`
  (bind `0.0.0.0:8080`); **Cloudflare TIDAK bisa dijangkau** dari sini (API eksternal diblokir — item
  terbuka yang sudah tercatat)
- **Data:** seluruhnya fiktif, ditandai pita **"MODE UJI COBA b3"** di bagian paling atas halaman dan
  di `web/data-acara.json` bagian `meta.peringatan_uji`

---

## 1. Gerbang & alat — hasil terukur (exit code dibaca eksplisit)

| Perintah | Hasil terukur |
|---|---|
| `python3 sistem/sistem-undangan/_sistem/validate_unit.py` | **rc=0 PASS** — `gerbang data 03 bagian 7 lulus · bukti aset 06 bagian 8 lengkap/NA` |
| **Uji mutasi alat baru 3/3** — (a) `titik_sensitif_terkonfirmasi.ya=false`, (b) `galeri` kosong tanpa `galeri_alasan_kosong`, (c) berkas raster di `web/aset/` tanpa baris di `daftar-aset.json` | (a) **rc=1**, (b) **rc=1**, (c) **rc=1**; pemulihan **rc=0**, sha berkas data **identik** |
| `node …/uji/uji-render.js …/web` (**uji render di DOM nyata, jsdom**) | **rc=0 — 30 lulus, 0 gagal** (daftar lengkap: bagian 6) |
| `python3 web/buat-flyer.py --periksa` | **rc=0 FLYER SINKRON** — kedua flyer masih cocok dengan `data-acara.json` |
| `node web/buat-qr.js --periksa` | **rc=0 QR SINKRON** — `qr-sebar.svg` cocok dengan alamat di `data-acara.json` |
| `node --check app.js` · `node --check buat-qr.js` | sintaks JS sah |
| Server pratinjau: 11 berkas diunduh (`index.html`, `style.css`, `app.js`, `data-acara.json`, `qr-sebar.svg`, pustaka QR, provenance, 2 flyer, 2 SVG aset) | **semuanya HTTP 200** |

**Alat baru yang lahir dari b3:** `_sistem/validate_unit.py` — gerbang data (03 bagian 7) dan aturan
bukti aset (06 bagian 8) yang sebelumnya **hanya kalimat tertulis**, kini ditegakkan mekanis per unit.

---

## 2. Daftar periksa TERBIT (10 butir — `09` bagian 4 Langkah D)

| # | Butir | Status | Bukti / sebab |
|---|---|---|---|
| 1 | Tautan dibuka di **HP biasa**, terbuka < 5 detik | **BELUM DIUJI — menunggu pemilik** | butuh mata & HP pemilik di tautan pratinjau |
| 2 | Dibuka di **jaringan lambat**: teks langsung terbaca | **sebagian terukur** | berat total yang diunduh tamu **85.128 byte (83 KB)** termasuk pustaka QR; **0 aset raster**; font dari CDN (penyimpangan yang dinyatakan di `spesifikasi-desain.md` bagian 3) |
| 3 | Semua isi **dari data** (nama, tanggal, jam, tempat, peta) sama dengan yang disetujui | **LULUS secara mekanis** | 20 pemeriksaan render (bagian 6) membandingkan **halaman hasil render** dengan `data-acara.json` — nama, 4 orang tua, turut mengundang, 2 larik acara (tanggal panjang, jam+zona waktu, venue, alamat, tautan peta), susunan acara, dress code, pembuka, credit, teks WA |
| 4 | Baca balik **digit per digit nomor rekening** | **N/A — amplop tidak diaktifkan (E3)** | yang diuji: (a) **data kosong → bagian amplop tidak dirender** (LULUS, pemeriksaan negatif), (b) jalur uji `?uji=amplop` menampilkan nomor jelas fiktif + label **JALUR UJI** (LULUS, 3 pemeriksaan) |
| 5 | **QRIS** dipindai ≥2 aplikasi | **N/A** | tidak ada QRIS pada uji coba (tidak ada rekening) |
| 6 | **Musik**: tombol mati berfungsi, tidak berbunyi sendiri | **LULUS (lebih kuat dari syaratnya)** | halaman **tidak punya elemen audio sama sekali** (diperiksa otomatis) — tidak ada autoplay yang mungkin terjadi |
| 7 | **Ucapan & RSVP**: kirim satu ucapan percobaan | **sebagian** | form + daftar ucapan ada di halaman dan **ditandai di layar** sebagai mode uji (localStorage). Pengiriman nyata lewat jari **menunggu pemilik**; penyimpanan permanen **belum ada** (dokumen 10) |
| 8 | **Layar kecil**: tidak ada tulisan terpotong | **sebagian** | viewport + tipografi `clamp()` + satu kolom maks 34rem; **pemeriksaan mata di HP menunggu pemilik** |
| 9 | **Flyer** terbuka rapi | **LULUS secara berkas** | `flyer-portrait.svg` + `flyer-landscape.svg` ada, XML sah, **sinkron dengan data** (rc=0); **pandangan mata menunggu pemilik** |
| 10 | **Catatan versi** disimpan di folder unit | **LULUS** | `catatan-versi.md` v1 (tanggal + isi + penyetuju + artefak); versi juga di `data-acara.json` → `publikasi.catatan_versi` |

**Ringkas:** **4 butir LULUS**, **1 N/A sah** (amplop/QRIS), **4 sebagian** (terukur mesin, menunggu mata
pemilik), **1 belum diuji** (butir 1, HP biasa).

---

## 3. Daftar periksa SERAH TERIMA (7 butir — `09` bagian 6)

| # | Butir | Status | Bukti / sebab |
|---|---|---|---|
| 1 | "Client" menerima **5 item** dan membukanya dari HP | **2 dari 5 item siap, menunggu pemilik** | **item 1 tautan** = ADA (pratinjau) · **item 2 video** = **N/A** (format video tidak dijanjikan — dokumen 08 ditunda) · **item 3 flyer** = ADA (2 orientasi, SVG) · **item 4 QR + teks WA** = ADA (`qr-sebar.svg` vektor + teks WA yang dihasilkan dari rekaman + tombol salin) · **item 5 info rekening** = **N/A** (tidak menghimpun dana) |
| 2 | Tautan disimpan client & dikirim ulang | **menunggu pemilik** | — |
| 3 | Teks WA diuji tempel client | **menunggu pemilik** | teks sudah dihasilkan dari data (bukan ketikan manual) dan memuat tautan (diperiksa otomatis) |
| 4 | Client tahu **cara minta perubahan** | **menunggu pemilik** | jalur WA→studio→diberi tahu tertulis di `09` bagian 7 |
| 5 | Client tahu tidak ada penonaktifan sepihak + arsip gratis | **menunggu pemilik** | kunci L1 bagian 6/8 |
| 6 | **Catatan serah terima** di Log Keputusan unit | **BELUM** — ditulis setelah pemilik menyelesaikan butir 1–5 | gerbang: unit **belum boleh** ditutup sebelum 7 butir beres |
| 7 | **Arsip studio** bisa dibuka | **BELUM** — arsip = repo + berkas unit; pengujian nyata menunggu pemilik melakukan deploy | dicatat apa adanya, tidak diklaim |

**Sifat Tahap 7 pada b3: LATIHAN.** Tidak ada client nyata, jadi tidak ada perpindahan apa pun ke luar.
Yang diuji: apakah **panduannya bisa diikuti** dan apakah **artefaknya lengkap**.

---

## 4. Amplop digital (5 butir — `11` bagian 10)

| # | Butir | Status |
|---|---|---|
| 1 | Nomor tampil persis seperti disetujui | **uji tampilan LULUS** (jalur uji, nomor jelas fiktif) · **verifikasi nyata BELUM** (tidak ada rekening) |
| 2 | Tombol salin → digit murni | **BELUM DIUJI** — butuh jari (klip papan) di peramban pemilik |
| 3 | QRIS dipindai ≥2 aplikasi | **N/A** — tidak ada QRIS |
| 4 | Bagian amplop **tidak muncul** saat data kosong | **LULUS** (pemeriksaan negatif otomatis) |
| 5 | Pengalaman tamu terasa sopan | **menunggu pemilik** |

---

## 5. Yang BELUM bisa diuji dari lingkungan ini (dinyatakan, bukan disembunyikan)

1. **Deploy Cloudflare (Tahap 6 sesungguhnya)** — API eksternal diblokir dari sandbox. Pratinjau nyata
   sudah jalan; **deploy dijalankan pemilik** mengikuti `09` bagian 4. **Sampai itu, "terbit di
   `lee-studio.pages.dev/...`" belum boleh diucapkan.**
2. **Gerbang resolusi G3** — unit ini **0 aset raster**, jadi tidak ada yang bisa dinilai DPI. Yang teruji
   hanyalah **aturan bukti per aset** (validator menolak raster tanpa baris di `daftar-aset.json`).
   **Alat hitung DPI efektif + `Lanczos4` masih belum dibuat** (tetap terbuka).
3. **Pemeriksaan mata pemilik**: HP biasa (butir 1), jaringan lambat (butir 2), layar kecil (butir 8),
   flyer (butir 9), pengalaman amplop (butir 5 bagian 4), tombol salin (butir 2 bagian 4).
4. **Penyimpanan ucapan/RSVP yang sebenarnya** — keputusan dokumen 10 (ditunda). Mode uji memakai
   localStorage dan itu **ditulis di layar**, bukan disembunyikan.
5. **Font woff2 lokal (subset)** — belum ada; halaman memakai CDN + fallback (tercatat di
   `spesifikasi-desain.md` bagian 3 dan `log-keputusan-unit.md`).
6. **Ukuran minimal QR pada cetak** — belum diukur (`06` bagian 10).

---

## 6. Uji render otomatis — 30 pemeriksaan, daftar apa adanya

Alat: `uji/uji-render.js` (jsdom, dijalankan dari akar repo; jsdom **tidak** di-vendor, dipasang di `/tmp`).
Yang **lulus (30)**: judul · nama lengkap 2 mempelai · 4 nama orang tua · turut mengundang ·
untuk **masing-masing** dari 2 acara: tanggal panjang Indonesia (`Sabtu, 12 Desember 2026`), jam+zona
waktu, venue+alamat, tautan peta · susunan acara · dress code · pembuka · credit `Lee-Studio` ·
sapaan baku L1 · hitung mundur 4 satuan · form ucapan & RSVP · catatan mode uji tampil · teks WA memuat
tautan · **QR dirender sebagai SVG (vektor)** · pita "MODE UJI COBA" · **amplop tidak dirender saat data
kosong** · **tidak ada elemen audio** · jalur `?uji=amplop` (3 pemeriksaan) · `?tamu=Nama` (personalisasi
dari parameter tautan).
Yang **gagal: 0**.

---

## 7. Langkah pemilik sesudah berkas ini (supaya b3 benar-benar tuntas)

1. Buka `https://8080-i2b08gpk69xbcgdahr1nq.e2b.app` **di HP** — jalankan butir 1, 2, 7, 8 daftar
   periksa Terbit dengan mata sendiri.
2. Buka `?uji=amplop` dan `?tamu=Nama Anda` — periksa tampilan amplop uji + personalisasi.
3. Buka `web/flyer-portrait.svg` & `web/flyer-landscape.svg` (butir 9).
4. Kalau sudah oke: **jalankan deploy Cloudflare** mengikuti `09` bagian 4 (klik-klik, tanpa terminal) —
   sesudah itu Tahap 6 yang sesungguhnya tuntas dan barisnya dicatat di `catatan-versi.md`.
5. Kalau ada yang ganjil: tulis di sini / chat — **jangan diperbaiki langsung** supaya jejaknya jelas.
