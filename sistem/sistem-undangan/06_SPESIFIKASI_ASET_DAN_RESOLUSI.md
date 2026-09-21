# Spesifikasi Aset Dan Resolusi

> **STATUS: ISI — DRAFT.** Diisi 2026-09-21 (UTC) lewat **ROADMAP JALAN PRODUKSI PERTAMA butir b2**
> (handoff log sesi slot 43/44; dikerjakan sesi slot 45) sebagai **dokumen generator** per
> `00_RENCANA_KERANGKA.md` bagian 7 (*"isinya keputusan berisiko, bukan isian"*).
> **Angka di dokumen ini TIDAK ditulis ulang dari ingatan** — semuanya dikutip dari sumber yang
> disebut di §11, dan setiap angka menyebut bagian sumbernya di tempat ia dipakai.
> Keputusan berisiko di dalamnya **disetujui pemilik 2026-09-21 lewat paket C1–C6** (dua tingkat aset &
> siapa membuat ekspor · definisi *fotografis* · nasib aset ditolak · cetak uji & batas janji cetak +
> CMYK ditunda · sumber ornament vektor · penegakan G3 & penggantian foto sesudah tayang) — approval
> tercatat di Log Keputusan dokumen ini.
> Banner kerangka dicabut di commit yang sama dengan perluasan validator (mekanika T-69/prompt 02).

| | |
|---|---|
| **Berkas** | `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` |
| **Lapis** | lintas semua lapis |
| **Cara diisi** | **YA — prompt Discovery detail** (`_sistem/PROMPT_DISCOVERY_06_ASET_DAN_G3.md`) — **sudah dijalankan 2026-09-21** dengan pola *delegasi + paket keputusan* (approval pemilik atas C1–C6) |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` **§4.3 · §4.4 · §4.5** (angka terukur — dipakai apa adanya) + `01_IDENTITAS_PEMILIK.md` (§10 batasan mutlak · §6 biaya produksi) + `02_PROFIL_JENIS_ACARA.md` (§6 pantangan) + `05_DISCOVERY_DESAIN_PROMPT.md` (§1 batas janji · §8 keadaan dokumen) + approval pemilik atas paket C1–C6 (log sesi slot 45) |

## Fungsi dokumen ini

**Dua tingkat aset** (layar vs cetak) + **gerbang G3** dengan **3 hasil**: LOLOS (≥300 DPI) / LOLOS
BERSYARAT (fotografis, ≥200 DPI, ≤1,5×, `Lanczos4`, cetak uji wajib) / DITOLAK. Plus **Langkah 0**:
teks wajib di-render dari font, ornament/logo wajib vektor — **hanya foto yang boleh raster**.

## Catatan untuk yang mengisinya nanti

1. **Angkanya sudah terukur dan sudah dikunci pemilik.** Jangan menulis ulang dari ingatan, jangan
   menghitung ulang, jangan mengusulkan angka baru. Kalau ada angka yang bertentangan dengan
   `00_RENCANA_KERANGKA.md` §4.3–4.5, **laporkan bentrokannya**, jangan pilih sendiri.
2. **Skrip uji + diskusi mentahnya tinggal di area internal master** (provenance — tidak ikut kalau
   folder sistem ini dipisah). Yang dipakai di sini adalah **angkanya, dikutip dengan sumber**;
   menyalin berkas master ke folder ini **dilarang**.
3. **G3 hanya mengurus resolusi.** CMYK, bleed, safe zone, crop marks, batas tinta, dan PDF/X adalah
   gerbang prepress tersendiri (`07_SPESIFIKASI_CETAK_PREPRESS.md`) — meloloskan resolusi **tidak**
   meloloskan prepress.

## Isi

### 1. Langkah 0 — kenapa teks & ornament tidak masuk gerbang sama sekali

| Jenis isi | Aturan | Akibatnya |
|---|---|---|
| **Teks** | **WAJIB di-render dari font**, dilarang ditempel sebagai gambar | tidak pernah masuk gerbang resolusi — tajam di ukuran berapa pun |
| **Ornament, logo, garis, bingkai** | **WAJIB vektor (SVG)**, atau divektorkan | skala tak terbatas; tidak pernah "diperbesar" |
| **Foto** | satu-satunya yang boleh raster | hanya foto yang butuh gerbang resolusi |

**Status Langkah 0 = kesimpulan terukur, bukan preferensi desain** (`00_RENCANA_KERANGKA.md` §4.4):
pada guratan tipis/bentuk mirip huruf, **semua** metode yang diuji menghasilkan **PSNR 20,8–22,6 dB** —
jauh di bawah ambang **32 dB** milik repo sendiri ("degradasi mulai terlihat"). Tidak ada metode yang
membuat guratan tipis layak cetak. Jadi "teks dari font, ornament vektor" adalah **satu-satunya pilihan
yang tersisa**, bukan gaya.

**Konsekuensi untuk client:** permintaan *"tulisan nama dibuat jadi gambar"* **ditolak** dengan
penjelasan awam — nama orang bisa pecah/kacau saat diperbesar dan **tidak bisa diperbaiki sesudah
undangan tersebar**.

### 2. Dua Tingkat Aset — apa bedanya, dan siapa yang membuat

| Jenis isi | Tingkat **LAYAR** | Tingkat **CETAK** | Satu berkas melayani keduanya? | Siapa yang membuat |
|---|---|---|---|---|
| **Teks** | dirender dari font (woff2 subset + fallback sistem) | dirender dari font di berkas cetak | **YA** — selalu dari font (Langkah 0) | studio (agent) |
| **Ornament / logo / garis / bingkai** | SVG | SVG | **YA** — vektor | studio (agent) |
| **Latar / pola** | SVG atau gradien CSS | SVG | **YA** | studio (agent) |
| **Foto** | raster diringankan — **target operasional agent: sisi terpanjang ≤ 2000 px dan ± ≤ 300 KB per foto** (angka operasional, **bukan** hasil uji — boleh dikoreksi saat uji coba nyata; lihat Log Keputusan C1) | raster **≥300 DPI** pada ukuran cetak akhir, atau jalur LOLOS BERSYARAT (§4) | **TIDAK selalu** — dibuat **dua ekspor** dari **satu master** milik client | studio (agent) mengekspor; **client hanya menyediakan master** (foto asli) |
| **Peta** | **tautan** Google Maps (default L2) — bukan gambar | bila perlu gambar peta: dari penyedia peta statis beresolusi cukup | — | studio (agent) |

**Aturan pembagian kerja (keputusan pemilik, C1):** client **tidak pernah** diminta membuat ekspor,
mengubah ukuran, atau mengurus format berkas. Yang diminta dari client hanya **bahan asli** — dan bila
bahannya kurang, itu dibicarakan lewat jalur §5, bukan dengan menyalahkan client.

**Kenapa dua tingkat itu bertentangan (dikutip, bukan dirumuskan ulang):** `00_RENCANA_KERANGKA.md`
bagian 2.3 baris Tahap 4 — *"dua tingkat aset (web & cetak) karena keduanya bertentangan"*. Ringkasnya:
undangan harus **ringan** untuk dibuka tamu di HP murah, dan **tajam** untuk dicetak — satu berkas tidak
bisa optimal untuk keduanya.

### 3. Definisi "Fotografis" — siapa yang boleh masuk jalur LOLOS BERSYARAT

**MASUK kategori fotografis** (boleh masuk jalur bersyarat §4, kalau angka DPI-nya memenuhi):

1. Foto hasil kamera — potret orang, gedung/lokasi, dekorasi, makanan, pemandangan.
2. Foto dari HP (termasuk mode potret/kamera ponsel).
3. **Foto yang sudah lewat WhatsApp** — **tetap fotografis**, tetapi diberi catatan tambahan: artefak
   kompresinya ikut terlihat, sehingga **cetak uji wajib** dan client **diberi tahu** (cap "diperbesar
   dari sumber beresolusi lebih rendah" tidak cukup menggambarkan artefak kompresi).
4. Hasil render 3D/gambar digital yang **bersih dari teks dan garis halus** (mis. mockup dekorasi tanpa tipografi).

**TIDAK MASUK** (dilarang masuk jalur bersyarat; wajib diperbaiki di sumber atau diganti):

1. Semua yang **berisi teks** — termasuk tulisan di spanduk papan bunga, papan nama, layar HP.
2. **Garis halus / line art / ilustrasi garis** (alasannya angka §1).
3. **Logo** (wajib vektor).
4. **Screenshot / tangkapan layar** apa pun (selalu mengandung elemen antarmuka/teks).
5. **Render 3D atau gambar digital yang mengandung tipografi/garis tipis**.
6. Peta hasil tangkapan layar (pakai tautan atau peta statis beresolusi cukup — §2).

**Kalau sebuah gambar punya dua sifat** (mis. foto orang yang fotonya memuat papan bertulisan): yang
berlaku adalah **sifat yang paling ketat** — selama ada teksnya, ia **bukan** fotografis untuk keperluan
gerbang ini. **Jangan pernah memvektorkan foto** — terukur: vektorisasi pada gambar garis 512×512
menghasilkan SVG 23,0 KB (wajar), sedangkan pada foto nyata menghasilkan SVG **6,4 MB** (tidak berguna).

### 4. Gerbang G3 — Tiga Hasil dan Ambangnya

| Hasil | Syarat | Yang terjadi |
|---|---|---|
| **LOLOS** | sumber **≥300 DPI** pada ukuran cetak akhirnya | lanjut tanpa catatan |
| **LOLOS BERSYARAT** | konten **fotografis** (§3) **DAN** sumber **≥200 DPI** **DAN** kenaikan yang dibutuhkan **≤1,5×** **DAN** bukan format besar (baliho/banner) | **resize `Lanczos4`** → lanjut, tetapi **wajib keempatnya**: (a) tercatat di Log Keputusan unit + provenance ditandai *"diperbesar dari sumber beresolusi lebih rendah"*; (b) **CETAK UJI WAJIB untuk semua kasus** (§6); (c) client diberi tahu dalam bahasa awam bahwa hasilnya **berisiko terlihat lembut pada cetakan jarak dekat**; (d) **dilarang** melabeli hasilnya "sangat baik" — SSIM terukur **0,9566**, di bawah ambang "sangat baik" repo **0,97** |
| **DITOLAK** | selain itu: sumber **<200 DPI** · kenaikan **>1,5×** · berisi teks/garis halus/logo · format besar · atau masih kurang sesudah diproses | ditolak **dengan angka kekurangannya**, lalu wajib ditawarkan **3 jalan keluar** (§5) |

**Ambang ini sudah DIPERKETAT oleh hasil uji** (keputusan T-30, `00_RENCANA_KERANGKA.md` §4.5):
**≥150 → ≥200 DPI** dan **≤2× → ≤1,5×**, implementasi **`Lanczos4`**. Alasannya angka: memperketat
150→200 DPI memberi **+2,37 dB** dan SSIM **0,9281 → 0,9566** pada foto.

**AI upscaling KELUAR dari jalur kritis** (keputusan T-30). Terukur pada foto: ESPCN +0,55 dB dan
FSRCNN +0,28 dB di atas `lanczos4` dengan **SSIM praktis identik**, dan pada 1,5× **AI lebih buruk di
kedua metrik**. Satu-satunya yang unggul berarti (EDSR +1,12 dB) **tidak bisa jalan** (OOM-KILL).
Di satu-satunya jenis isi yang dilarang Langkah 0 (garis halus), AI memang lebih baik (+1,5 s.d. +2,0 dB)
tetapi tetap di bawah ambang 32 — tidak berguna. **AI tetap ada sebagai penyempurnaan opsional** dan
**dilarang dijual sebagai peningkatan mutu**.

**Yang TIDAK ikut dilonggarkan:** *"Upscaling fixes resolution only — color mode, bleed, and dimensions
are separate issues."* Karena itu **CMYK + profil ICC, bleed 3 mm, safe zone, crop marks, batas tinta, dan
PDF/X tetap gerbang terpisah** (`07_SPESIFIKASI_CETAK_PREPRESS.md`).

**Tingkat risiko G3 = SEDANG** (`00_RENCANA_KERANGKA.md` §4.2): perlakuan = **konfirmasi ringkas +
catatan**. Tetapi hasil **DITOLAK bersifat fail-closed** — tidak bisa ditawar di tengah produksi.

### 5. Nasib Aset Ditolak — tiga jalan keluar, siapa menanggung, cara memberi tahu

**Tiga jalan keluar yang WAJIB ditawarkan** (bukan opsional, bukan pilihan agent):

1. **Minta foto lebih besar/lebih baik** ke client (panduan awam: kirim **berkas asli** dari galeri
   kamera/Google Drive, **jangan** lewat WhatsApp bila bisa dihindari).
2. **Ganti aset** — pakai foto lain, atau ganti elemen raster itu dengan **ornament vektor**.
3. **Batalkan hanya format cetaknya** — undangan web (dan flyer layar) tetap jalan, karena tingkat
   asetnya berbeda (§2).

**Siapa menanggung (keputusan pemilik, C3):** penggantian desain/ornament **ditanggung studio** — biaya
produksi studio Rp 0 (L1 §6) dan biaya bahan studio tidak dibebankan ke client. Client **tidak dikenai
biaya tambahan**; fase portofolio juga membuat revisi sebelum terbit gratis (L1 §8). Keterlambatan
ditangani dengan **jalur cepat** (dokumen 05 §1), bukan dengan memotong mutu.

**Cara memberi tahu client (aturan bahasa):**

- Mulai dari **tujuan client**, bukan dari angka: *"supaya hasil cetaknya tetap bagus…"*.
- Sebut **angka itu sebagai fakta netral** tentang berkasnya, bukan kesalahan client: *"fotonya 1200×800
  piksel; untuk dicetak sebesar ini kami butuh ±3600×2400"*.
- **Selalu sertakan ketiga jalan keluar** dengan akibat awam masing-masing.
- **Jangan** menyalahkan, **jangan** menyebut perangkat/platform yang dipakai client, **jangan** memakai
  kata "gagal" untuk berkasnya — yang gagal adalah *pencocokan antara berkas dan ukuran pemakaian*.

### 6. Cetak Uji Wajib & Batas Janji Cetak

**Untuk SEMUA kasus LOLOS BERSYARAT, cetak uji (proof) wajib** — ini yang memperketat aturan dari
"hanya oplah besar" menjadi "selalu", atas dasar angka (SSIM 0,93 pada kondisi ambang 150 DPI/2×
vs skala repo "sangat baik" ≥0,97 — `00_RENCANA_KERANGKA.md` §4.4).

| Pertanyaan | Jawaban |
|---|---|
| Siapa mencetak | **client/keluarga** di percetakan pilihannya untuk undangan yang memang akan dicetak (mereka yang mencetak); **studio menyiapkan berkas cetak ujinya** + panduan |
| Siapa membayar | **client** membayar cetak ujinya sebagai bagian dari cetak undangannya (bukan biaya tambahan jasa studio). Untuk uji internal studio di fase portofolio: **pemilik** menanggung cetak kecil (sekali, murah) |
| Apa yang dinilai | (1) ketajaman **foto** pada jarak baca normal, (2) ketajaman **teks & ornament**, (3) kecocokan **warna** dengan pratinjau, (4) **potongan/bleed** tidak memakan isi |
| Kalau cetak uji gagal | aset itu **tidak dipakai di cetak**: turun jadi **layar-saja** atau diganti; hasilnya dicatat di Log Keputusan unit. Tidak ada janji cetak untuk aset itu |
| Apakah sistem menjanjikan hasil cetak? | **TIDAK.** Sistem menyerahkan **berkas siap cetak + panduan cetak uji**. Mutu hasil cetak fisik ada di tangan percetakan client |

**CMYK ditunda (keputusan pemilik, C4):** jalur cetak sekarang memakai **berkas RGB resolusi tinggi yang
diserahkan ke percetakan**, dan **konversi CMYK dilakukan percetakan** — **jangan menjanjikan CMYK**.
Konversi/PDF-X lewat Ghostscript **belum diuji di lingkungan ini** dan jalur prepress-nya baru akan
ditetapkan di dokumen 07 (dokumen yang memang belum diisi). Batas ini konsisten dengan dokumen 05 §1
(di sana: *cetak siap-cetak belum dijanjikan*).

### 7. Sumber Ornamen & Logo Vektor — empat jalur, urut prioritas

| # | Jalur | Catatan jujur |
|---|---|---|
| 1 | **Dibuat sendiri oleh agent** (SVG dari bentuk dasar geometris, arabesque, garis/lengkung) | **jalur utama**; biaya Rp 0; lisensi milik studio (L1 §4) |
| 2 | **Vektorisasi dari gambar garis** memakai `vtracer` | hanya untuk **gambar garis/ornament**, **jangan pernah untuk foto** (bukti: 23,0 KB vs 6,4 MB, §3). Pemasangannya **sekali pakai dan tidak bertahan antar sesi** — langkah pemasangan wajib ditulis di laporan tahap, bukan diasumsikan ada |
| 3 | **Bahan berlisensi dari luar** | wajib **provenance + status lisensi** dicatat per aset; aturan L1 §10 berlaku: **lisensi = peringatan, bukan block**, keputusan pemilik menutup |
| 4 | **Dari client** (mis. logo keluarga) | tetap wajib vektor; bila yang diberikan raster → jalur 2 (gambar garis) atau dibuat ulang sebagai vektor |

**Gap yang dinyatakan terbuka, bukan diasumsikan ada (keputusan pemilik, C5):** kemampuan
**vectorization** masih **belum terpasang sebagai skill** (gap di daftar pekerjaan terbuka area master,
butir T-06 nomor 9 — statusnya **terbuka**). Skill apa pun **belum terpasang** di sistem ini (L1 §9: 0
skill terpasang; pemasangan selalu **per butir + approval pemilik + provenance**). Karena itu jalur 1
(membuat sendiri) adalah yang **paling pasti bisa dijalankan sekarang**.

### 8. Penegakan G3 — siapa, alat, kapan, bukti

- **Siapa:** **agent** (bukan client, bukan percetakan).
- **Alat:** penghitungan **resolusi efektif** (piksel sumber ÷ ukuran pemakaian dalam inci) + pengecilan/
  pembesaran **`Lanczos4`**. Alat bantu yang dipakai saat pengukuran asal (OpenCV `dnn_superres`, `vtracer`)
  **bukan** bagian jalur kritis — `lanczos4` tersedia di perkakas dasar (**ketergantungan `pip install`
  hilang dari jalur kritis**, `00_RENCANA_KERANGKA.md` §4.5).
- **Kapan (dua momen):**
  1. **Tahap 3 (pra-janji)** — pemeriksaan **cepat** supaya agent tidak menjanjikan aset yang akan
     ditolak (dokumen 05 §1 baris "Aset client"); hasilnya belum formal.
  2. **Tahap 4 (formal)** — gerbang **G3** sesungguhnya, **sebelum** aset masuk rakitan. Aset yang belum
     lewat G3 tidak boleh dirakit.
- **Bukti (WAJIB, per aset)** — satu baris di **Log Keputusan unit**:

  `nama-aset · sumber/provenance · jenis isi (fotografis/teks/vektor) · ukuran pemakaian (cm pada cetak / px pada layar) · resolusi efektif (DPI) · kenaikan yang dibutuhkan (×) · hasil (LOLOS/LOLOS BERSYARAT/DITOLAK) · tindakan · catatan cetak uji`

- **Gerbang tanpa bukti = diklaim hijau tanpa pernah dijalankan.** Itu kelas temuan yang sudah berulang
  di repo ini; karena itu bukti di atas **syarat**, bukan pelengkap. Laporan G3 juga menutup satu baris
  ringkas: berapa aset diperiksa, berapa tiap hasil, dan aset mana yang bergantung pada cetak uji.

### 9. Perubahan Aset Sesudah Tayang

1. **Foto diganti sesudah undangan tersebar → G3 dijalankan ULANG untuk foto itu** (dengan bukti baris §8).
   Perubahan ini tetap **gratis** sebagai perubahan kecil (L1 §8), tetapi **tidak boleh** melewati gerbang.
2. **Tautan undangan tetap sama** (syarat path stabil, kebijakan domain 3 fase) — tamu tidak perlu tautan baru.
3. **Tamu yang sudah membuka undangan bisa masih melihat foto lama beberapa jam** karena simpanan
   sementara di HP-nya; dinyatakan apa adanya ke client (tidak ada notifikasi otomatis ke tamu).
4. **Undangan yang sudah dicetak tidak berubah** — berkas cetak yang sudah diserahkan adalah versi yang berlaku.
5. Semua penggantian aset + hasil G3 ulang dicatat di **Log Keputusan unit**.

### 10. Yang Belum Diukur / Dinyatakan Sadar (jangan diisi dengan dugaan)

1. **Font sungguhan belum diuji** — font sistem kosong di lingkungan pengukuran; yang diuji adalah
   **guratan tipis**, bukan tipografi nyata (`00_RENCANA_KERANGKA.md` §4.4).
2. **Mutu cetak fisik tidak diukur** — tidak ada printer di lingkungan ini; PSNR/SSIM hanyalah **proksi**.
   Itulah sebabnya **cetak uji wajib** dan sistem **tidak menjanjikan hasil cetak** (§6).
3. **Sumber ≥250 DPI belum diukur** — kalau ambang suatu saat diperketat lagi, **wajib diukur ulang**,
   tidak boleh diekstrapolasi.
4. **Foto client yang sudah terkompresi JPEG berat belum diuji** — perlakuan sementaranya ada di §3 butir 3
   (tetap fotografis + cetak uji + pemberitahuan); hasil uji nyata pertama **menimpa** catatan ini lewat
   Log Keputusan.
5. **CMYK/bleed/PDF-X tidak disentuh upscaling** — jalur prepress ditunda (§6) dan menjadi urusan
   dokumen 07.
6. **Vektorisasi belum punya alat terpasang** (§7) — jangan berasumsi bisa.
7. **Confound metodologis** yang sudah dinyatakan di sumber: angka GARIS di tabel §4.5 **tidak bisa
   dibandingkan** dengan angka GARIS §4.4 (ada langkah resize akhir yang menaikkan PSNR secara artifisial);
   angka GARIS yang sah untuk disimpulkan adalah **20,8–22,6 dB** (§4.4). Angka FOTO konsisten antar-run.

### 11. Angka & Sumbernya (supaya bisa diaudit tanpa membaca riwayat diskusi)

| Angka | Nilai | Sumbernya |
|---|---|---|
| Ambang LOLOS | **≥300 DPI** pada ukuran cetak akhir | `00_RENCANA_KERANGKA.md` §4.3 (tabel 3 hasil) |
| Ambang LOLOS BERSYARAT | **≥200 DPI** · kenaikan **≤1,5×** · fotografis · bukan format besar | `00_RENCANA_KERANGKA.md` §4.3 + §4.5 (keputusan T-30, DIPERKETAT dari ≥150 / ≤2×) |
| Implementasi | **`Lanczos4`** (AI keluar dari jalur kritis) | `00_RENCANA_KERANGKA.md` §4.5 |
| PSNR guratan tipis (semua metode) | **20,8–22,6 dB** — di bawah ambang repo **32 dB** | `00_RENCANA_KERANGKA.md` §4.4 |
| Keuntungan AI atas `lanczos4` pada foto | **+0,28 dB** (FSRCNN) · **+0,55 dB** (ESPCN) · SSIM praktis identik; pada 1,5× AI lebih buruk di kedua metrik | `00_RENCANA_KERANGKA.md` §4.4 + §4.5 |
| SSIM kondisi ambang | **0,9281** (150 DPI/2,0×) → **0,9566** (200 DPI/1,5×) — keduanya di bawah ambang "sangat baik" repo **0,97** | `00_RENCANA_KERANGKA.md` §4.4 + §4.5 |
| EDSR / Real-ESRGAN | **OOM-KILL** pada A5@300 · butuh PyTorch | `00_RENCANA_KERANGKA.md` §4.4 |
| Vektorisasi | garis 512×512 → **SVG 23,0 KB** · foto nyata → **SVG 6,4 MB** | `00_RENCANA_KERANGKA.md` §4.4 |
| Waktu proses (kalau AI dipakai) | FSRCNN **3,7 dtk** · ESPCN **2,0 dtk** untuk A4@300 dari sumber 150 DPI · `lanczos4` **0,01 dtk** | `00_RENCANA_KERANGKA.md` §4.4 + §4.5 |
| Riset + skrip uji asal angka-angka ini | disimpan di **area internal master** (skrip uji upscaling + diskusi mentah bagian P) — **provenance, tidak ikut** kalau folder ini dipisah, dan **tidak disalin** ke sini | `00_RENCANA_KERANGKA.md` §4.4 (penunjuk sumber) |
| Target ukuran foto layar (≤2000 px sisi terpanjang, ± ≤300 KB) | **operasional agent, bukan hasil uji** | Log Keputusan dokumen ini (C1) — boleh dikoreksi saat uji coba nyata |

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-21 | **Dokumen diisi — ROADMAP b2, Discovery 06 (aset & gerbang G3)**: dua tingkat aset + definisi fotografis + nasib aset ditolak + cetak uji & batas janji + sumber ornament vektor + penegakan G3 + angka & sumbernya; banner kerangka dicabut; `_sistem/validate_system.py` diperluas (6 kerangka → **5 kerangka + 6 terisi**; diuji mutasi); manifest v0.7.0→**v0.8.0**; `STATUS.md` diperbarui — **satu commit** | ROADMAP JALAN PRODUKSI PERTAMA butir b2 (disetujui pemilik, log sesi slot 43/44) + pola *delegasi + paket keputusan*. Paket **C1–C6** diajukan agent dan **disetujui pemilik seluruhnya** (*"Setuju semua (C1–C6)"*, log sesi slot 45). **Angka G3 tidak diusulkan ulang** — dikutip dari `00_RENCANA_KERANGKA.md` §4.3–4.5 (aturan pertama prompt 06) |
| 2026-09-21 | **C1** — client hanya menyediakan **bahan asli**; **studio membuat dua ekspor** (layar & cetak) dari satu master. Target operasional foto layar: sisi terpanjang ≤2000 px, ± ≤300 KB/foto — **ditandai sebagai angka operasional agent, bukan hasil uji** | Agent; disetujui pemilik. Alasan: client non-teknis tidak boleh diminta mengurus ekspor; angka layar belum diukur → dijujurkan, bukan disamarkan sebagai hasil uji |
| 2026-09-21 | **C2** — definisi **fotografis**: foto kamera/HP **termasuk foto lewat WhatsApp** (dengan artefak kompresi + cetak uji + pemberitahuan); **bukan** fotografis: berisi teks, garis halus, logo, screenshot, render 3D bertipografi, peta tangkapan layar. Gambar bersifat ganda → **sifat paling ketat yang berlaku** | Agent; disetujui pemilik. Dasar angka: guratan tipis 20,8–22,6 dB di bawah ambang 32 (§1) + AI bisa "mengarang" teks — dan yang dikarang bisa **nama orang** |
| 2026-09-21 | **C3** — aset DITOLAK selalu ditawarkan **3 jalan keluar** (foto lebih besar · ganti aset · batalkan hanya format cetak); penggantian **ditanggung studio** (biaya produksi Rp 0); client **tidak dikenai biaya**; cara memberi tahu = bahasa tujuan + angka netral + tanpa menyalahkan | Agent; disetujui pemilik. Dasar: `00_RENCANA_KERANGKA.md` §4.3 (3 jalan keluar sudah bagian gerbang) + L1 §6/§8 |
| 2026-09-21 | **C4** — **cetak uji wajib untuk semua LOLOS BERSYARAT**; cetak fisik oleh **client/keluarga** (studio menyiapkan berkas + panduan); uji internal fase portofolio ditanggung **pemilik**; **sistem tidak menjanjikan hasil cetak**; **CMYK ditunda** (berkas RGB → percetakan; jangan menjanjikan CMYK) | Agent; disetujui pemilik. Dasar angka: SSIM 0,93 pada kondisi ambang (§4.4) — melabeli "sangat baik" tidak didukung angka. CMYK ditunda karena dokumen 07 belum ada dan Ghostscript belum diuji di lingkungan ini |
| 2026-09-21 | **C5** — sumber ornament/logo: **4 jalur berurut** (buat sendiri = utama · vektorisasi `vtracer` untuk gambar garis saja · bahan berlisensi dengan provenance · minta client); **gap vektorisasi (T-06 butir 9) tetap TERBUKA dan tidak diasumsikan ada**; 0 skill terpasang di sistem ini | Agent; disetujui pemilik. Dasar: L1 §9 (0 skill; pemasangan per butir) + L1 §4 (ornament Rp 0 dibuat sendiri) + angka vektorisasi §4.4 |
| 2026-09-21 | **C6** — penegakan G3: **agent**, dua momen (pra-janji Tahap 3 cepat; formal Tahap 4), alat = hitung DPI efektif + `Lanczos4`, **bukti wajib per aset di Log Keputusan unit**; **foto diganti sesudah tayang → G3 ulang**, tautan tetap, cache beberapa jam dinyatakan apa adanya | Agent; disetujui pemilik. Alasan: *gerbang tanpa bukti = diklaim hijau tanpa dijalankan* — kelas temuan yang sudah berulang di repo; karena itu bukti ditetapkan sebagai syarat |
| 2026-09-21 | **Confound metodologis dinyatakan ulang** (bukan koreksi baru): angka GARIS di §4.5 tidak sebanding dengan §4.4; yang sah untuk disimpulkan adalah **20,8–22,6 dB** | Sudah tercatat di `00_RENCANA_KERANGKA.md` §4.5; dokumen ini mengulangnya supaya angka tidak dipakai lewat jalur yang salah |
