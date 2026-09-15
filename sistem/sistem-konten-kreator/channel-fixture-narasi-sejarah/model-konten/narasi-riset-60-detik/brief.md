# Model Konten Brief — Narasi Riset 60 Detik (Channel: Narasi Sejarah)

### Dokumen "hidup" milik SATU model konten dalam SATU channel. Hasil dari `07_MODEL_KONTEN_DISCOVERY_PROMPT.md`.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — draf pertama selesai 2026-09-14
- [x] **Reviewed** — direview lengkap oleh pengguna 2026-09-14
- [x] **Approved** — dikunci lewat gerbang **G2** 2026-09-14; **v2 dikunci lewat G2 2026-09-15** (target kata disinkron ke tempo Channel Brief v4)
- [x] **Merged** — masuk `main` lewat PR #52 pada 2026-09-14 (merge commit `2d39eea`); **v2 BELUM masuk `main`** — G3 menunggu keputusan pemilik (PR tanpa auto-merge)
- [x] **Operational** — sudah `Merged` dan seluruh dependency terpenuhi (2026-09-14)

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan: unit breakdown = **segmen narasi**
- [x] Override terhadap Channel Brief sudah dinyatakan eksplisit: tidak ada override persona/voice; model menambah alur riset dan aturan sumber
- [x] Gerbang tambahan sudah dicatat — G1 riset dan G1 pemilihan kandidat ide; G2/G3 bawaan tetap berlaku
- [x] Channel Brief induknya sudah berstatus `Operational`
- [x] Sudah `Merged` ke `main` (PR #52, merge commit `2d39eea`, 2026-09-14)

**Versi:** `2` — **Terakhir diperbarui:** `2026-09-15`

## Mewarisi dari: `channel-fixture-narasi-sejarah/channel-brief.md`

Semua yang sudah dikunci di Channel Brief — termasuk Persona & Voice, batasan klaim, dan gaya visual channel faceless — otomatis berlaku di sini. Brief ini hanya menambahkan alur riset, aturan sumber, dan detail produksi yang spesifik untuk model ini.

---

## 1. Identitas Model Konten

- **Nama model konten:** Narasi Riset 60 Detik
- **Definisi singkat (beda dari model konten lain di channel yang sama):** format narasi 55–65 detik yang memulai setiap produksi dari satu tema terbatas, melakukan riset web dan pencatatan sumber terlebih dahulu, lalu menghasilkan beberapa kandidat ide sebelum satu ide dipilih dan diteruskan ke pipeline standar. Berbeda dari `Narasi 60 Detik`, model ini tidak boleh masuk ke ideasi sebelum paket riset tersedia.

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** 55–65 detik; target 108–125 kata pada tempo channel 125 kata/menit dengan jeda 0,7 detik (disinkron dari Channel Brief v4; rentang dihitung dari rumus durasi repo — 108 kata + 5 jeda = 55,34 dtk, 125 kata + 7 jeda = 64,90 dtk).
- **Struktur konten khas format ini:** tema terbatas → paket riset dan peta fakta → beberapa kandidat ide → satu ide dipilih → pipeline standar untuk konsep/angle, naskah, breakdown segmen, asset, dan publish prep. Struktur naskah akhirnya tetap mewarisi pola model `Narasi 60 Detik`: benda/ruang sebagai pintu masuk, konteks kebiasaan, perubahan, lalu penutup yang kembali ke masa kini.
- **Platform paling cocok untuk format ini:** YouTube Shorts dan TikTok.

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** sama seperti Channel Brief dan model `Narasi 60 Detik`: b-roll netral, foto benda, footage arsip yang sah dipakai, warna hangat dan sedikit pudar, tekstur film.
- **Kalau ada elemen Konsistensi Visual dari channel — cara tampil di format ini:** tidak ada elemen Bank Konsistensi Visual yang berlaku; channel faceless dan tidak memiliki karakter/latar/props wajib. Riset web hanya menjadi dasar fakta dan arahan visual umum, bukan lisensi untuk menyalin foto atau footage sumber ke asset final.

## 4. Alur Kerja Produksi

**Mode:** [ ] Ikuti Kerangka Standar (dengan override ringan) / [x] Alur Kerja Kustom

### Kenapa model konten ini butuh alur kustom

Model ini berbeda dari akar pipeline standar karena sebelum Ideation harus ada riset yang mengumpulkan bahan dan fakta untuk satu tema, memeriksa keterlacakan klaim, dan mencatat sumber web sejak sumber pertama dipakai. Riset tersebut menghasilkan beberapa kandidat ide dalam satu produksi, tetapi tidak menjadi bank tema lintas produksi. Setelah satu kandidat ide dipilih, proses bertemu kembali dengan pipeline standar dan menghasilkan satu konten 60 detik.

### Tahapan alur kerja kustom

| No | Nama Tahap | Input | Proses/Tools | Output |
|---|---|---|---|---|
| 1 | Penetapan Tema Terbatas | Satu tema awal untuk satu produksi | Tegaskan batas tema agar cukup untuk satu video 55–65 detik; tetapkan benda/ruang sebagai pintu masuk dan batas waktu/cakupan bila diperlukan. Jangan memperluasnya menjadi bank tema untuk beberapa produksi. | `tema.md` berisi tema, batas cakupan, pertanyaan riset, dan kriteria tema selesai |
| 2 | Riset Web dan Pencatatan Sumber | `tema.md` | Cari bahan dan fakta melalui web; setiap sumber yang dipakai dicatat segera di `SUMBER.md` dengan URL atau judul/penerbit, tanggal akses, jenis bahan, status verifikasi, lisensi/hak, dan kebutuhan atribusi. Sumber harus dapat diakses lewat web. | `riset.md` + `SUMBER.md` yang terisi sejak sumber pertama digunakan |
| 3 | Verifikasi dan Peta Fakta | `riset.md`, `SUMBER.md` | Kelompokkan fakta menjadi klaim yang dapat dipakai, konteks pendukung, dan hal yang belum pasti. Klaim sejarah spesifik wajib memiliki minimal dua sumber independen yang dapat diakses lewat web. Bila detail hanya punya satu sumber, jangan memaksakan sumber kedua: turunkan bahasanya atau tandai `belum pasti`. Klaim yang tidak dapat diverifikasi tidak boleh ditulis sebagai kepastian. | `peta-fakta.md` yang memetakan klaim, sumber pendukung, status verifikasi, batas bahasa, dan celah fakta |
| 4 | Ideation Berbasis Riset | `peta-fakta.md`, `tema.md` | Bentuk beberapa kandidat ide yang semuanya bersumber dari paket riset; cek pengulangan topik terhadap `arsip-naskah/indeks.md`. Setiap kandidat harus memiliki benda/ruang sebagai pintu masuk, premis satu kalimat, fakta utama, dan potensi penutup masa kini. | `ideation.md` berisi daftar kandidat ide dan rekomendasi kandidat terkuat |
| 5 | Pemilihan Satu Ide | `ideation.md`, `peta-fakta.md` | Pilih satu kandidat untuk diproduksi. Kandidat lain tidak menjadi bank tema permanen; boleh tetap dicatat sebagai konteks di folder produksi, tetapi tidak boleh diperlakukan sebagai backlog lintas produksi tanpa keputusan baru. | satu ide terpilih yang dirujuk oleh `konsep-angle.md` |
| 6 | Pertemuan dengan Pipeline Standar | satu ide terpilih + seluruh paket riset/sumber | Setelah G1 pemilihan ide, ikuti `05_CONTENT_PRODUCTION_PIPELINE.md` mulai **Tahap 2 — Konsep & Angle**, lalu Tahap 3 Naskah, Tahap 4 Breakdown Output, Tahap 5 Generate/Acquire Assets, dan Tahap 6 Assembly & Publish Prep. `SUMBER.md` tetap menjadi sumber resmi fact-check sampai naskah diarsipkan. | output pipeline standar: `konsep-angle.md`, `naskah-draft.md`, `breakdown-output.md`, `assets/`, dan publish prep |

### Aturan sumber dan fact-check khusus model

1. Sumber eksternal pertama langsung dicatat di `SUMBER.md`; pencatatan tidak boleh direkonstruksi dari ingatan pada akhir produksi.
2. Klaim sejarah spesifik wajib memiliki minimal **dua sumber independen** yang dapat diakses lewat web.
3. Jika detail hanya didukung satu sumber web, tulis dengan bahasa yang diturunkan atau tandai `belum pasti`; jangan mengarang, jangan memaksakan pencarian sumber kedua yang tidak ada.
4. Klaim dengan status `Tidak bisa diverifikasi` tidak boleh dipakai sebagai fakta pasti dalam naskah.
5. Riset web tidak memberikan hak memakai foto, footage, musik, logo, atau karya terlindungi sebagai asset final. Asset final harus memiliki hak yang jelas atau dibuat/diperoleh melalui cara yang sah; halaman web hanya boleh menjadi rujukan fakta atau arahan gaya/komposisi.
6. Saat naskah dipindahkan ke arsip, `SUMBER.md` dipindahkan menjadi `arsip-naskah/[tanggal]-[judul]-sumber.md` sesuai pipeline standar.

### Gerbang tambahan model

G1/G2/G3 bawaan pipeline tidak dihapus. Model ini menambah dua checkpoint:

- **G1 Paket Riset — wajib sebelum Ideation:** paket `riset.md`, `SUMBER.md`, dan `peta-fakta.md` sudah cukup, setiap klaim punya status, dan celah verifikasi dilaporkan. Pertanyaan: *"Paket riset ini sudah sesuai dan boleh dipakai untuk menghasilkan kandidat ide?"*
- **G1 Pemilihan Ide — wajib sebelum Tahap 2 pipeline standar:** kandidat ide yang dipilih sesuai Channel Brief, tidak mengulang topik arsip secara tidak sadar, dan cukup konkret untuk satu konten 60 detik. Pertanyaan: *"Ide ini yang dipakai untuk masuk ke Konsep & Angle?"*

G1 pada paket riset tidak berarti G1 pemilihan ide, G2 naskah, G2 breakdown, G2 final, atau G3 merge. Semua gerbang tersebut tetap diminta terpisah dan dicatat di `STATUS.md`.

### Titik pertemuan dengan kerangka standar

Alur kustom bertemu dengan `05_CONTENT_PRODUCTION_PIPELINE.md` **setelah Tahap 5 alur kustom, yaitu setelah satu kandidat ide dipilih dan G1 Pemilihan Ide disetujui**. Dari titik itu, mulai Tahap 2 — Konsep & Angle, lalu lanjut Tahap 3 sampai Tahap 6 sesuai pipeline standar dan aturan sumber di atas. Tidak ada Tahap 1 Ideation standar yang diulang, karena Ideation sudah dilakukan di Tahap 4 alur kustom.

### Catatan tools yang belum pasti

- Mesin pencarian dan situs sumber dipilih saat eksekusi sesuai topik; yang wajib adalah akses web, keterlacakan, dan pencatatan tanggal akses.
- Cara memperoleh footage/foto final ditentukan pada Tahap 5 pipeline berdasarkan hak pakai yang dapat diverifikasi.

## 5. Contoh Konkret

Tema satu produksi: **jam dinding di ruang tamu**. Riset web mengumpulkan sejarah kebiasaan memakai jam rumah, perubahan ritme waktu keluarga, dan sumber pendukung; hasilnya dicatat dalam `SUMBER.md` lalu dipetakan di `peta-fakta.md`. Dari paket itu lahir beberapa kandidat: jam sebagai pengatur makan malam, jam sebagai benda yang membuat tamu merasa waktunya terlihat, dan jam sebagai penanda rumah yang tidak lagi dihuni. Satu kandidat dipilih, misalnya jam sebagai pengatur makan malam, lalu masuk ke Konsep & Angle. Naskah akhirnya tetap 55–65 detik, memakai jam sebagai pintu masuk, tidak menyebut klaim sejarah tanpa sumber, dan ditutup dengan hubungan benda itu terhadap cara orang mengatur waktu hari ini.

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-14 | Draf model diberi nama `Narasi Riset 60 Detik` dan memakai Mode Alur Kerja Kustom | Pengguna meminta tahap riset sebelum ideasi; pipeline standar tidak boleh dipaksa menangani urutan yang berbeda dari akar |
| 2026-09-14 | Satu produksi dimulai dari satu tema terbatas yang menghasilkan beberapa kandidat ide, bukan bank tema lintas produksi | Menjaga scope riset cukup untuk satu konten 60 detik dan mencegah output riset menjadi backlog yang tidak diminta |
| 2026-09-14 | Klaim sejarah spesifik memerlukan minimal dua sumber independen yang dapat diakses lewat web; satu sumber boleh dipakai hanya dengan bahasa diturunkan atau label `belum pasti` | Menjaga keterlacakan tanpa memaksakan sumber kedua yang memang tidak tersedia |
| 2026-09-14 | Alur bertemu dengan pipeline standar setelah satu kandidat ide dipilih dan G1 pemilihan ide disetujui, mulai Tahap 2 Konsep & Angle | Ideation sudah dijalankan di alur kustom berbasis riset |
| 2026-09-15 | v2 — target panjang naskah **130–145 kata → 108–125 kata**, dikunci lewat **G2** (persetujuan pemilik eksplisit); G3 menunggu | Bagian 2 brief ini menyebut tempo channel secara eksplisit, jadi ikut bergeser ketika Channel Brief v4 mengunci tempo 125 kata/menit + jeda 0,7 detik. Angka yang sama dipakai model `Narasi 60 Detik` v2 supaya dua model di channel yang sama tidak memakai rentang yang bertentangan. Struktur naskah, alur riset, dan aturan sumber tidak diubah |
