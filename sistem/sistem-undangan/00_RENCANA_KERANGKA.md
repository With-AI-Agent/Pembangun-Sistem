# Rencana Kerangka — Sistem `sistem-undangan`

> **STATUS: FINAL — dikonfirmasi pemilik 17 September 2026.** Folder sistem dibuat dalam **PR yang
> sama** dengan dokumen ini (aturan M-14). `Tahap: kerangka` — **isi sistem belum ada**, yang ada baru
> kerangka + manifest + skeleton. Kategori **BESAR** per `_meta/02_PRINSIP_UNIVERSAL.md` (Prinsip 3).
>
> **Rekaman konfirmasi pemilik (verbatim):** *"Lanjutkan sesuai yang menurutmu terbaik"* lalu memilih
> **"Setuju — finalisasi dan buat PR-nya"** untuk pertanyaan *"Apakah ini sudah final sehingga folder
> sistem boleh dibuat?"*. Untuk ambang G3 pemilik menjawab *"Aku ikut yang terbaik menurut kamu"* →
> **diukur**, hasilnya di bagian **4.5**, bukan dipilih dari dua usulan.
>
> **3 pertanyaan review yang tadinya menggantung** (#2 7 hal konsisten, #3 tingkat risiko gerbang,
> #6 aset besar tidak masuk repo) **dinyatakan diterima** karena pemilik mengonfirmasi final tanpa
> keberatan — sebelumnya sudah ditulis *"kalau tidak ada keberatan, kupakai usulanku"*. **Ini bukan
> persetujuan yang dipaksakan**: kalau pemilik ingin mengubah ketiganya, dokumen ini masih bisa direvisi
> dan revisinya wajib masuk Log Keputusan di bawah.

---

## ⚠️ Catatan kejujuran soal asal-usul dokumen ini (baca dulu)

Dokumen ini **menutup sebuah gap nyata**, dan gap-nya perlu kamu ketahui supaya kamu tahu bagian mana
yang harus direview paling teliti.

**Yang sudah punya dasar tertulis di repo** (disimpan di DISKUSI_MENTAH sistem-pembuat-undangan
2026-09-17, diverifikasi dengan menghitung sebutan):

| Fakta riset | Sebutan di berkas | Bagian |
|---|---|---|
| Cloudflare free tier (Pages/Workers/D1/KV/R2) + plafonnya | 12 | H |
| Remotion + jebakan lisensinya | 8 | D |
| AVIF/WebP + hasil uji kompresi terukur | 8 | J.1 |
| Spesifikasi cetak 300 DPI | 6 | C |
| Fitur RSVP (baseline 7 situs pasar Indonesia) | 9 | A |
| Amplop digital / QRIS | 3 | A, E |
| Pola satu domain + undangan sebagai subpath | 4 | A, B |
| bleed / PDF-X / Decap-Sveltia / Input-Pengguna / kaligrafi / i18n | 4 / 2 / 1 / 3 / 2 / 1 | B, C, F |

**Yang TIDAK ada di berkas mana pun** — hanya hidup di analisis sesi agent (dihitung dengan grep, hasil
`0` semua): `BERTINGKAT` · `SIKLUS 7 tahap` · `7 hal konsisten` · `gerbang G0–G5`.

**Artinya: risetnya tahan lama, tetapi keputusan desain yang dibangun di atasnya tidak pernah
dituliskan.** Itu persis kegagalan yang pemilik keluhkan 17 Sep 2026 (*"jangan cuma dicatat tapi juga
harus direspon/dieksekusi"*) dalam bentuk lain: **bukan tercatat-lalu-diam, melainkan diputuskan-lalu-
tidak-tercatat.** Karena itu:

- Bagian **2, 3, dan 4** di bawah adalah **rekonstruksi + perumusan baru**. **Kamu belum pernah
  melihatnya.** Review-nya harus paling teliti di sana.
- Bagian **5, 6** dan semua angka teknis **menunjuk ke riset yang sudah tersimpan**, jadi bisa dicek.

---

## 1. Untuk Siapa/Apa

**Siapa yang memakai sistem ini:** pemilik sendiri, **skala solo / ≤3 orang** (keputusan pemilik
giliran 2), **tidak punya basic coding** (T8 — kendala mengikat semua dokumen: bahasa awam, standar
kelulusan *"bisa dipakai orang awam tanpa bertanya lagi"*).

**Siapa yang menerima hasilnya — tiga lapis penerima, dan ini penting karena kebutuhannya berbeda:**

| Penerima | Yang mereka butuhkan | Konsekuensi desain |
|---|---|---|
| **Pemilik** (operator sistem) | alur yang menuntun dari satu prompt, tidak perlu mengambil keputusan teknis | sistem **bertanya dan mengusulkan**, bukan menyodorkan pilihan kosong |
| **Client pemilik** (pengantin / keluarga / panitia) | undangan jadi, bisa direvisi, tahu statusnya | perlu **pratinjau + titik persetujuan** (gerbang G4) dan **serah terima yang jelas kepemilikannya** |
| **Tamu undangan** (audiens akhir) | undangan yang terbuka cepat di HP, RSVP mudah, tidak membingungkan | **responsif-adaptif semua layar** (keputusan pemilik giliran 3), aset ringan untuk web |

**Tujuan akhir kalau sistem dipakai dengan benar:** dari **satu prompt pembuka**, agent menuntun sampai
undangan **jadi dalam format apa pun yang dibutuhkan** (laman web, video, flyer, siap cetak, lainnya)
lalu **terbit atau diserahkan ke client** — dengan **biaya bulanan nol** dan **tanpa kecacatan yang
lolos diam-diam**.

**Cakupan acara:** **kebutuhan apa pun** — pernikahan, khitanan, webinar, dan lainnya (T1). Acara
**pertama yang dibangun: pernikahan** (keputusan pemilik giliran 3), tetapi **struktur tidak boleh
mengunci ke pernikahan**: jenis acara adalah **data di Lapis 2**, bukan asumsi di kode.

---

## 2. Bentuk Dasar — **GABUNGAN: BERTINGKAT 3 lapis + SIKLUS 7 tahap** ✅ DIKUNCI

> **DIKUNCI oleh pemilik 17 Sep 2026** (pertanyaan review #1: *"Setuju — kunci bentuk ini"*).
> Sebelumnya bagian ini rekonstruksi yang belum pernah tertulis; sekarang sudah disetujui, jadi statusnya
> naik dari usulan menjadi keputusan. Yang **masih** perlu review teliti: bagian **3** (7 hal konsisten)
> dan **4** (gerbang + tingkat risiko) — pemilik belum memutuskannya eksplisit.

### 2.1 Kenapa gabungan, dan bukan salah satu

Presedennya ada di repo ini: sistem konten kreator **BERTINGKAT** di level struktural tetapi **SIKLUS**
di level produksi harian. Undangan punya kebutuhan yang sama persis, dan alasannya konkret:

- Pemilik akan memakai sistem ini **berulang kali untuk banyak client** → butuh **SIKLUS** dengan tahap
  yang sama setiap kali, supaya tidak mulai dari nol dan tidak ada tahap yang terlewat.
- Tetapi setiap undangan **harus mewarisi** hal yang sama: identitas usaha pemilik, font/palet default,
  kebijakan serah terima, rekening untuk amplop digital → butuh **BERTINGKAT**, karena kalau tidak,
  tiap undangan akan mengulang keputusan yang seharusnya dikunci sekali.

**Konsekuensi praktis yang bisa diuji:** mengubah satu keputusan di Lapis 1 (misalnya font default)
**wajib** berdampak ke semua undangan yang belum dikunci di G2, dan **wajib tidak** mengubah diam-diam
undangan yang sudah terbit. Kalau perilaku itu tidak terjadi, bentuk dasarnya salah dirancang.

### 2.2 BERTINGKAT — 3 lapis (level atas dikunci dulu, bawah mewarisi)

| Lapis | Isi | Seberapa sering diisi | Dikunci di gerbang |
|---|---|---|---|
| **L1 — Identitas & Preferensi Pemilik** | merek/nama usaha pemilik, font & palet default, gaya ornament bawaan, bahasa & nada default, kebijakan harga & masa aktif, **rekening + QRIS statis** untuk amplop digital, kebijakan serah terima ke client, daftar skill & plugin yang dipakai | **sekali**, diperbarui jarang | perubahan L1 = **risiko BESAR** (diwarisi semua undangan) |
| **L2 — Profil Jenis Acara** | per jenis (pernikahan, khitanan, webinar, dst): **daftar field info default yang boleh kurang atau lebih** (T5), konvensi desain & etika per jenis (mis. kaligrafi/transliterasi Islami untuk khitanan dan pernikahan Muslim), format keluaran yang lazim, kata-kata baku (undangan, RSVP, ucapan) | **sekali per jenis acara**, lalu dipakai ulang | **G0** |
| **L3 — Undangan Konkret** | satu client / satu acara: data nyata, desain final, aset, keluaran per format, daftar tamu & tautan personal | **setiap kali pakai** | **G1–G5** |

**Aturan warisan yang mengikat:** L3 **boleh menyimpang** dari L2/L1, tetapi penyimpangan **wajib
dicatat di Log Keputusan unit itu** dengan alasan — **tidak boleh diam-diam**. Ini Prinsip 1 (Hierarki)
dipakai apa adanya.

### 2.3 SIKLUS — 7 tahap produksi per undangan

| # | Tahap | Keluaran tahap | Gerbang di ujungnya |
|---|---|---|---|
| 1 | **Intake** — dibuka dengan **satu prompt pembuka** (T4 = W-01); agent menuntun, bukan menyodorkan formulir kosong; **tawaran kapabilitas** disampaikan di sini | brief awal + jenis acara terpilih (L2) | **G0** |
| 2 | **Data Acara** — field adaptif dari L2; **boleh kurang boleh lebih**; yang kurang **dinyatakan sadar**, bukan diisi diam-diam dengan nilai karangan | data acara tervalidasi terhadap skema | **G1** |
| 3 | **Desain & Format** — pilih template/gaya, **input milik pemilik** (font, template, contoh, referensi — T14), tentukan format keluaran yang dijanjikan | spesifikasi desain + daftar format target | **G2** |
| 4 | **Aset** — generate/olah/kompres; **dua tingkat aset** (web & cetak) karena keduanya bertentangan; **gerbang resolusi fail-closed** | aset siap pakai per tingkat + laporan gerbang | **G3** |
| 5 | **Rakit & Pratinjau** — **satu sumber data → banyak format** (web, video, flyer, cetak); pratinjau responsif semua layar | pratinjau semua format yang dijanjikan | **G4** |
| 6 | **Terbit** — publish web (Cloudflare Pages, undangan sebagai **subpath** dari satu domain) **atau** serah cetak (PDF siap cetak) **atau** render video | artefak terbit + catatan versi | — |
| 7 | **Serah Terima & Rawat** — hosting di **akun client**, CMS untuk client non-coder, **repo Git sebagai database**, masa aktif & cara perpanjangan, cara revisi setelah tayang | paket serah terima + STATUS unit ditutup | **G5** |

**Kenapa 7 dan bukan 6:** tahap **Serah Terima & Rawat** dipisahkan dari **Terbit** karena keduanya
punya pemilik risiko yang berbeda — *Terbit* adalah tindakan teknis, *Serah Terima* adalah perpindahan
**kepemilikan akun dan tanggung jawab** ke client. Mencampur keduanya adalah cara paling umum client
kehilangan akses ke situsnya sendiri. Riset bagian B menunjuk persis risiko ini.

---

## 3. Yang Harus Konsisten — **7 hal**

> **Rekonstruksi — belum pernah tertulis.**
>
> Catatan: `_meta/02_PRINSIP_UNIVERSAL.md` menyatakan **"Pemisahan Konsistensi Visual vs Non-Visual"**
> sebagai prinsip **TIDAK universal** (spesifik konten kreator), dan secara eksplisit berkata sistem lain
> *"MUNGKIN SAJA butuh jenis konsistensi lain yang analog (misal konsistensi skema data) yang perlu
> digali sendiri saat Discovery Level-0"*. **Itulah yang dilakukan di sini** — domain ini butuh
> **keduanya**: konsistensi visual (undangan adalah benda visual) **dan** konsistensi skema data (satu
> sumber data menghasilkan banyak format).

| # | Yang dikunci | Kalau tidak dikunci, apa yang rusak | Dikunci di lapis |
|---|---|---|---|
| 1 | **Skema data acara** — nama field, tipe, wajib/opsional, satuan | **paling berbahaya**: satu sumber data dipakai untuk web + cetak + video + RSVP. Kalau nama field bergeser, **semua turunan rusak sekaligus** dan kerusakannya tidak terlihat sampai formatnya dibuka | L2 |
| 2 | **Identitas visual pemilik** — font, palet, logo, gaya ornament | tiap undangan terlihat seperti buatan orang berbeda; merek usaha pemilik tidak terbentuk | L1 |
| 3 | **Satuan & resolusi aset** — px / mm / DPI + profil warna **per tingkat aset** | kesalahan **paling mahal**: aset web dipakai untuk cetak. Terbukti terukur di bagian J.2: foto 768 px **kurang 2,4×** untuk A5 full-bleed @300 DPI | L1 + gerbang G3 |
| 4 | **Zona aman, bleed, margin cetak** — bleed 3 mm, safe zone 3–5 mm, crop marks, batas tinta | hasil cetak terpotong di percetakan, dan **kerusakannya baru terlihat setelah dicetak** (tidak bisa diulang gratis) | L2 per format cetak |
| 5 | **Penamaan berkas & struktur folder per undangan** | website induk tidak bisa mengelola, backup tidak bisa diverifikasi, aset tertukar antar-client | L1 |
| 6 | **Struktur URL & pola subpath di website induk** | tautan yang sudah disebar ke tamu **berubah** → tamu mendapat halaman mati. Ini tidak bisa diperbaiki setelah undangan disebar | L1 |
| 7 | **Bahasa, nada, dan i18n** — termasuk transliterasi/kaligrafi | salah sebut gelar keluarga atau salah tulis nama adalah **cacat yang tidak bisa dimaafkan client**, walaupun secara teknis situs berfungsi | L2 per jenis acara |

**Hal yang sengaja TIDAK dimasukkan ke daftar konsisten:** pilihan template per undangan, komposisi
foto, dan urutan galeri. Itu **memang harus boleh berbeda** tiap undangan — menguncinya akan membuat
semua undangan kembar.

---

## 4. Titik Penguncian / Approval — **6 gerbang (G0–G5)** dalam **3 tingkat risiko**

> **Rekonstruksi — belum pernah tertulis.**

### 4.1 Gerbang

| Gerbang | Apa yang dikunci | Kenapa di sini | Kalau dilewati diam-diam |
|---|---|---|---|
| **G0** | Brief + **jenis acara** (L2 terpilih) + field default disetujui | menentukan seluruh turunannya | salah jenis acara = seluruh data & desain salah arah |
| **G1** | **Data acara lengkap & valid** terhadap skema; yang kurang **dinyatakan sadar** | data adalah sumber tunggal semua format | nama/tanggal salah tercetak di ratusan undangan |
| **G2** | **Desain & format dikunci** (template, font, palet, daftar format yang dijanjikan) | **harus sebelum aset diproduksi massal** | aset diproduksi ulang = kerja dua kali |
| **G3** | **Aset lolos gerbang resolusi** — **fail-closed** | cetak tidak bisa ditoleransi | **lihat 4.3** |
| **G4** | **Pratinjau semua format disetujui** client/pemilik | persetujuan client adalah bukti, bukan asumsi | client menolak setelah terbit |
| **G5** | **Terbit / serah terima** — deploy atau PDF diserahkan, **kepemilikan akun client jelas** | perpindahan tanggung jawab | client kehilangan akses ke situsnya sendiri |

### 4.2 Tiga tingkat risiko (Prinsip 3 dipakai apa adanya)

| Tingkat | Ciri | Contoh di sistem ini | Perlakuan |
|---|---|---|---|
| **BESAR** | sulit/tidak bisa dibalik, berdampak ke banyak unit | **G0, G2, G5**; **perubahan apa pun di L1**; mengubah struktur URL | **review isi lengkap oleh pemilik**, tercatat di Log Keputusan, tidak boleh diwakilkan agent |
| **SEDANG** | bisa dibalik dengan kerja nyata | **G1, G3, G4**; menambah field baru di L2 | konfirmasi ringkas + catatan |
| **KECIL** | gampang diperbaiki, dampak lokal | teks ucapan, urutan galeri, tweak warna turunan | agent boleh lanjut, dicatat di log unit |

### 4.3 G3 — gerbang aset: **3 hasil, dialihkan menurut jenis isi**

> **DIUBAH 17 Sep 2026 atas masukan pemilik.** Rumusan semula **2 hasil** (lolos / tolak, fail-closed
> mutlak). Pemilik keberatan: *"jangan terlalu ketat, tapi bukan berarti ngentengin … kita kan bisa
> mensiasati nya, misalnya dengan melakukan upscaling dan penjernihan dan enhanchement dengan tenaga ai.
> Iya kan? … Gimana menurut kamu?"* — dan **meminta penilaian**, bukan persetujuan.
>
> **Verdict agent (sesuai gerbang T25 dan instruksi berdiri *"kritisi, jangan asal meng-iya-kan"*): ide
> pemilik DITERIMA SEBAGIAN dan DIPERTAJAM — bukan ditolak, bukan diiyakan mentah-mentah.** Riset lengkap
> dengan 6 sumber: DISKUSI_MENTAH bagian **N**.

**Yang membenarkan pemilik:** untuk **konten fotografis**, *"a 150 DPI photo upscaled 2x with AI tools can
often reach acceptable quality at 300 DPI for most print uses"*. Alat gratisnya ada: **Upscayl**
(open-source, berbasis Real-ESRGAN). Jadi menolak mutlak memang **terlalu kaku** untuk foto.

**Yang mengoreksi pemilik:** *"Fine text, logos with thin strokes, and geometric line art upscale poorly
… can introduce artefacts or rounded edges on letterforms"*, dan lebih keras lagi: *"AI upscalers can
mangle text, turning legible words into AI-hallucinated gibberish."* **Undangan justru didominasi teks
dan ornament garis halus** — nama pengantin, tanggal, kaligrafi, bingkai. Menaikkan resolusi di sana
bukan memperbaiki, melainkan **mengarang**, dan yang dikarang bisa **nama orang**.

#### Langkah 0 — hapus masalahnya secara STRUKTUR, sebelum gerbang apa pun

Ini bagian yang paling penting, dan **tidak diminta siapa pun**:

| Jenis isi | Aturan | Akibatnya |
|---|---|---|
| **Teks** | **WAJIB di-render dari font**, dilarang ditempel sebagai gambar | **tidak pernah masuk gerbang resolusi** — teks vektor tajam di ukuran berapa pun |
| **Ornament, logo, garis, bingkai** | **WAJIB vektor (SVG)**, atau divektorkan | *"For flat graphics and logos, vectorization is a complete fix — the output is infinitely scalable."* Tes praktis: zoom 400%, tepi bersih = bisa divektorkan |
| **Foto** | satu-satunya yang boleh raster | **hanya foto yang butuh gerbang resolusi** |

**Jadi gerbang ini menyempit dengan sengaja:** alih-alih "semua aset harus 300 DPI", aturannya jadi
"teks dan ornament **tidak boleh** raster, hanya foto yang diuji". Masalahnya bukan diselesaikan —
**tidak pernah muncul** untuk dua dari tiga jenis isi.

#### Lalu, untuk tiap aset FOTO, salah satu dari 3 hasil

| Hasil | Syarat | Yang terjadi |
|---|---|---|
| **LOLOS** | sumber **≥300 DPI** pada ukuran cetak akhirnya | lanjut tanpa catatan |
| **LOLOS BERSYARAT** *(jalur yang diminta pemilik — **TERBUKSI BISA**, dan **sudah DIPERKETAT oleh hasil uji**, lihat 4.4 + 4.5)* | konten **fotografis** (wajah, gedung, dekorasi foto) **DAN** sumber **≥200 DPI** pada ukuran akhir **DAN** kenaikan yang dibutuhkan **≤1,5×** **DAN** **bukan** format besar (baliho/banner) | **resize `Lanczos4`** → lanjut, tetapi **wajib keempatnya**: (a) tercatat di Log Keputusan unit + provenance aset ditandai **"diperbesar dari sumber beresolusi lebih rendah"**; (b) **CETAK UJI (proof) WAJIB untuk SEMUA kasus**, bukan hanya oplah besar; (c) client diberi tahu dalam bahasa awam bahwa hasilnya **berisiko terlihat lembut pada cetakan jarak dekat**; (d) **dilarang** melabeli hasilnya "sangat baik" — SSIM terukur **0,9566**, di bawah ambang "sangat baik" repo **0,97**. **Upscale AI (`cv2.dnn_superres` + FSRCNN/ESPCN) hanya PENYEMPURNAAN OPSIONAL** — terukur **tidak** memberi keuntungan pada foto |
| **DITOLAK** | **selain itu**: sumber **<200 DPI** · butuh kenaikan **>1,5×** · aset **berisi teks/garis halus/logo** · format besar (baliho/banner, *"no upscaling tool creates the 155 megapixels needed from a 1-megapixel source"*) · atau **masih kurang sesudah diproses** | **ditolak + dilaporkan dengan angka kekurangannya**, dan **wajib ditawarkan 3 jalan keluar**: (1) minta foto lebih besar ke client, (2) ganti aset, (3) **batalkan format cetak saja** — web & video tetap jalan karena tingkat asetnya berbeda |

#### Yang TIDAK ikut dilonggarkan

*"Upscaling fixes resolution only — color mode, bleed, and dimensions are separate issues."* Maka
**CMYK + profil ICC, bleed 3 mm, safe zone, crop marks, batas tinta, dan PDF/X tetap gerbang terpisah
yang berdiri sendiri.** Meloloskan resolusi **tidak** meloloskan prepress.

#### Kenapa ini bukan "ngentengin"

Yang harus ditolak **tetap ditolak**, dan penolakannya kini **spesifik per jenis isi** karena ancamannya
memang berbeda: foto yang di-upscale 2× dari 150 DPI **tidak** berisiko mengubah isi; teks yang
di-upscale **bisa mengubah nama orang** jadi huruf karangan, dan itu **tidak bisa diperbaiki setelah
dicetak**. Gerbang yang membedakan ancaman **lebih ketat** dari gerbang yang seragam, bukan lebih longgar.

**Skill yang dibutuhkan** (permintaan pemilik: *"Klo butuh skill untuk ini, kamu bisa siapkan skill nya"*):
upscaling raster + vectorization → **gap #9** di bagian 6. **Kelayakannya SUDAH DIUJI 17 Sep 2026** — hasilnya
di bagian **4.4** dan rincian lengkapnya di DISKUSI_MENTAH bagian **P**.

#### 4.4 Hasil uji T-28 — apa yang terbukti, dan apa yang harus dikoreksi dari draft ini

**Skrip ujinya disimpan** di `_meta/_internal/uji/uji_upscaling.py` supaya **bisa direproduksi**; metriknya
PSNR + SSIM Gaussian 11×11 σ=1.5 — **mengikuti preseden repo bagian J.1**, bukan metrik karangan baru.

| Pertanyaan | Jawaban terukur |
|---|---|
| **Bisakah dijalankan di lingkungan ini?** | **BISA.** `opencv-contrib-python-headless` → cv2 5.0.0 dengan `dnn_superres`; `vtracer`; `svgwrite`. Total pemasangan **~14 detik** — tetapi **`pip install` tidak bertahan antar sesi**, jadi langkahnya **wajib tertulis** di dokumen sistem |
| **Bobot model dari mana?** | **`raw.githubusercontent.com` DIBLOKIR** (HTTP 000 dalam 0,03 dtk). Yang terbuka: `github.com`, `api.github.com`, **`codeload.github.com`**, npm, PyPI. Jadi model diambil lewat **tarball repo di codeload**. Provenance (URL + sha256 + ukuran) dicatat di DISKUSI_MENTAH P.1 |
| **Cepat enough untuk ukuran cetak nyata?** | **YA untuk FSRCNN/ESPCN**: A4@300 DPI dari sumber 150 DPI = **3,7 dtk** (FSRCNN) / **2,0 dtk** (ESPCN). **TIDAK untuk EDSR**: **OOM-KILL** pada A5@300, dan 126 dtk pada *setengah* A5 |

**Empat hal yang MENGOREKSI draft ini sendiri:**

1. **Alat diganti.** Draft semula menyebut "Upscayl/Real-ESRGAN" (dari riset web). **Real-ESRGAN butuh
   PyTorch** (ratusan MB–GB) dan bobotnya dari GitHub Releases; **EDSR — model terdekat yang bisa dimuat —
   justru OOM.** Yang dipakai: **`cv2.dnn_superres` + FSRCNN_x2 (39 KB) / ESPCN_x2 (85 KB)**.
2. **Keuntungan AI atas resampling biasa ternyata KECIL, jadi klaimnya diturunkan.** Terukur pada foto:
   ESPCN **+0,55 dB** dan FSRCNN **+0,28 dB** atas lanczos4; **SSIM praktis identik** (0,9263–0,9266 vs
   0,9281). Satu-satunya yang unggul berarti (EDSR +1,12 dB) **tidak bisa jalan**. **Maka sistem ini DILARANG
   menjual "peningkatan AI" sebagai perubahan mutu.**
3. **Cetak uji jadi wajib untuk SEMUA LOLOS BERSYARAT** (semula hanya oplah besar). Alasannya angka: pada
   kondisi ambang (150 DPI, 2×) SSIM terukur **0,93**, sedangkan skala repo sendiri menyebut "sangat baik"
   baru di **≥0,97**. Melabeli hasil ini "sangat baik" = mengutip skala repo untuk klaim yang tidak
   didukung angkanya. **Ini memperketat draft, bukan melonggarkan.**
4. **Langkah 0 NAIK STATUS dari anjuran menjadi KESIMPULAN TERUKUR.** Pada guratan tipis/bentuk mirip huruf,
   **SEMUA metode** menghasilkan PSNR **20,8–22,6 dB** — jauh di bawah ambang **32** milik repo sendiri
   ("degradasi mulai terlihat"). AI memang terbaik di antara yang buruk (FSRCNN 22,61; SSIM 0,9137→0,9358),
   tetapi **tidak ada metode yang membuat guratan tipis layak cetak**. Jadi "teks wajib dari font, ornament
   wajib vektor" **bukan preferensi desain — itu satu-satunya pilihan yang tersisa**.

**Vektorisasi terkonfirmasi bisa, dengan batas yang jelas:** `vtracer` pada gambar garis/ornament 512×512 →
**SVG 23,0 KB** (wajar); pada **foto nyata** → **SVG 6,4 MB** (tidak berguna). **Jangan pernah memvektorkan foto.**

**Yang masih belum teruji dan dinyatakan sadar:** font sungguhan (font sistem kosong — yang diuji **guratan
tipis**, bukan tipografi nyata) · mutu cetak fisik (tidak ada printer; PSNR/SSIM hanya **proksi**) · sumber
**≥200 DPI** (kalau ambang kelak diperketat, **wajib diukur ulang**, tidak boleh diekstrapolasi) · foto client
yang sudah terkompresi JPEG berat · dan **CMYK/bleed/PDF-X sama sekali tidak disentuh upscaling**.

#### 4.5 Keputusan T-30 — ambang DIPERKETAT, dan AI KELUAR dari jalur kritis

Pemilik mendelegasikan keputusan ini (*"Aku ikut yang terbaik menurut kamu"*). Yang terbaik bukan memilih
salah satu dari dua usulan, melainkan **mengukurnya** — dan tooling-nya masih terpasang di sesi itu.

| Kondisi | Metode | PSNR dB | SSIM |
|---|---|---|---|
| FOTO **150 DPI (2,0×)** | lanczos4 | 36,91 | 0,9281 |
| | FSRCNN → lanczos | 37,09 | **0,9263** ↓ |
| | ESPCN → lanczos | 37,19 | **0,9266** ↓ |
| FOTO **200 DPI (1,5×)** | **lanczos4** | **39,28** | **0,9566** |
| | FSRCNN → lanczos | 39,14 ↓ | 0,9524 ↓ |
| | ESPCN → lanczos | 39,02 ↓ | 0,9514 ↓ |
| GARIS 150 DPI (2,0×) | lanczos4 / FSRCNN | 24,18 / **25,67** | 0,9431 / **0,9551** |
| GARIS 200 DPI (1,5×) | lanczos4 / FSRCNN | 26,11 / **28,10** | 0,9657 / **0,9752** |

**Tiga kesimpulan:**

1. **Memperketat 150 → 200 DPI berharga besar untuk foto: +2,37 dB dan SSIM 0,9281 → 0,9566.** Tetapi
   **masih di bawah 0,97**. **Satu-satunya cara mencapai ≥0,97 adalah tidak memperbesar sama sekali** —
   yaitu jalur **LOLOS** (sumber ≥300 DPI).
2. **AI TIDAK memberi keuntungan pada FOTO, di kedua kondisi.** Pada 2,0× PSNR naik sedikit tetapi
   **SSIM justru turun**; pada 1,5× **AI lebih buruk di kedua metrik**.
3. **AI hanya unggul pada GARIS HALUS (+1,5 s.d. +2,0 dB) — padahal konten itu justru DILARANG Langkah 0**,
   dan di bagian 4.4 terbukti tetap di bawah ambang 32 untuk semua metode.

> **KEPUTUSAN: AI upscaling KELUAR dari jalur kritis. "LOLOS BERSYARAT" diimplementasikan dengan
> `Lanczos4`, ambang DIPERKETAT ≥150 → ≥200 DPI, kenaikan dibatasi ≤2× → ≤1,5×.**
>
> Alasannya satu kalimat: **AI tidak membantu pada satu-satunya jenis isi yang boleh masuk gerbang (foto),
> dan hanya membantu pada jenis isi yang dilarang (garis halus).**

**Konsekuensi yang menguntungkan, muncul dari bukti dan tidak direncanakan:**
- **Ketergantungan `pip install` HILANG dari jalur kritis** — penting karena `pip install` **tidak bertahan
  antar sesi** di lingkungan ini. `Lanczos4` tersedia di Pillow/OpenCV dasar.
- **Tidak perlu vendor bobot model ke repo** (item T-29 turun jadi opsional) → repo tetap ringan.
- Waktu proses per aset turun dari **2–4 detik jadi 0,01 detik**.
- **AI tetap ada sebagai penyempurnaan opsional**, **dilabeli jujur** bahwa keuntungannya tidak terukur
  berarti — **dilarang dijual sebagai peningkatan mutu**.

**⚠️ Confound metodologis yang wajib dinyatakan:** angka **GARIS di tabel ini tidak bisa dibandingkan**
dengan angka GARIS di bagian 4.4 (20,85–22,61). Run ini menambah **langkah resize akhir** yang menghaluskan
sehingga **menaikkan** PSNR secara artifisial, dan dimensinya ganjil (511/255 vs 512/256). **Angka GARIS
yang sah untuk disimpulkan adalah yang di 4.4** (perbandingan langsung): **20,8–22,6 dB, di bawah ambang
32**. Angka GARIS di 4.5 hanya sah untuk **membandingkan antar-metode di dalam tabel yang sama**.
**Angka FOTO konsisten antar-run** (lanczos4 = 36,91/0,9281 di keduanya) → sah disimpulkan.

**Yang belum diukur dan dinyatakan sadar:** sumber **≥250 DPI**; foto client yang sudah terkompresi JPEG
berat; dan **font sungguhan** (font sistem kosong di lingkungan ini — yang teruji guratan tipis).

---

## 5. Batasan Platform (pertanyaan 5 — WAJIB)

**Dipakai via lmarena Agent Mode: YA.** Sumber fakta: `_meta/PLATFORM_LMARENA.md` (5 fakta + 6 policy).

| Fakta platform | Konsekuensi untuk sistem ini |
|---|---|
| Branch arena otomatis dibuat, tidak bisa asumsi kerja di `main` | semua kerja sistem lewat **PR**, tanpa auto-merge |
| **Tidak bisa push setelah PR merge/close** (platform cabut akses) | **checkpoint wajib di tiap gerbang**, bukan di akhir; pekerjaan yang belum ter-commit saat PR ditutup **hilang** |
| Sesi bisa crash kapan saja | turunan **`LOG_SESI` self-contained** (W-02) + `STATUS.md` per unit (W-03) + langkah recovery di prompt pembuka |
| **Semua API layanan eksternal terblokir** (hanya npm, PyPI, github.com) | **deploy harus Git-based**; tidak ada panggilan API runtime ke layanan AI/pihak ketiga dari dalam sesi |
| **Kebijakan domain 3 fase** (keputusan pemilik 17 Sep 2026, verbatim: *"Untuk masa percobaan gpp pake subdomain dulu yang gratis. Nanti waktu bener bener mulai rilis, baru pake domain yang cukup satu domin untuk semua undangan, kecuali klo client nya mau domain sendiri maka dia yang tanggung biaya nya") | **Fase 1 percobaan:** subdomain gratis bawaan platform (`nama.pages.dev/<undangan>`) — nol biaya. **Fase 2 rilis:** **satu domain untuk semua undangan** + subpath. **Fase 3 pengecualian:** client yang mau domain sendiri **menanggung biayanya sendiri** → sistem **wajib mendukung custom domain per undangan sebagai OPSI, bukan asumsi**. **Konsekuensi rancangan yang mengikat:** **PATH wajib stabil lintas fase** (`/<nama-undangan>` sama di ketiga fase, hanya host yang berubah). Kalau path ikut berubah saat naik fase, **semua tautan yang sudah disebar ke tamu jadi mati** — dan itu tidak bisa diperbaiki setelah undangan beredar |
| **T12 — fakta pembatas yang mengunci arah:** lmarena tidak menyediakan API key | **AI-nya = agent di sesi, BUKAN layanan runtime di website.** Website hasil bersifat **statik**; tidak ada fitur "AI menjawab tamu" di situs yang diserahkan ke client |
| Plafon artefak sesi (±128 MB / 10.000 berkas) | **aset besar TIDAK disimpan di repo.** Repo menyimpan **resep + sumber berukuran kecil + catatan provenance**; aset produksi di penyimpanan eksternal (R2) atau dihasilkan ulang dari resep |

---

## 6. Kapabilitas Eksternal (pertanyaan 6 — WAJIB)

**Sudah terpasang dan terpetakan ke kebutuhan sistem ini** — 56 skill di `sistem/sistem-building-aplikasi/skills/`,
pemetaannya di DISKUSI_MENTAH bagian **G**. Yang paling relevan sebagai **gerbang**: `brainstorming`
(*"You MUST use this before any creative work"* → cocok jadi gerbang Tahap 3 Desain), plus
`web-design-guidelines`, `agent-browser`, `security-review`, `verification-before-completion`,
`verification-loop`, `systematic-debugging`, `tdd-workflow`.

**8 gap yang belum terpasang** (riset bagian I; status di `_meta/DAFTAR_PEKERJAAN_TERBUKA.md` item
**T-06**, menunggu link dari pemilik atau izin memilih):

| # | Gap | Kenapa dibutuhkan | Catatan lisensi/biaya yang sudah diverifikasi |
|---|---|---|---|
| 1 | **video / Remotion** | format video (T2) | Remotion **gratis** untuk individu & perusahaan **≤3 karyawan** termasuk komersial; **≥4 karyawan wajib bayar** → pemilik berada di sisi gratis (skala solo/≤3). Alternatif bebas: **Motion Canvas (MIT)**, **HyperFrames (Apache 2.0)** |
| 2 | **prepress CMYK** | format siap cetak (T2) | **browser menghasilkan PDF RGB, bukan CMYK** (terverifikasi). Jalur yang **terbukti berhasil di lingkungan ini**: PDF CMYK **tanpa Ghostscript** — bukti bagian I |
| 3 | **generate gambar** | aset dekorasi PNG (T15) | dibutuhkan untuk ornament; **wajib** dicatat provenance-nya |
| 4 | **QR code** | QR check-in + tautan personal per tamu | pola pasar (bagian A) |
| 5 | **font subsetting** | font Arab/kaligrafi berukuran wajar | lisensi font: **Google Fonts aman komersial** (OFL/Apache 2.0); **risiko tagihan retroaktif nyata** untuk font non-bebas (bagian F) |
| 6 | **WhatsApp** | template pesan & pengiriman undangan | kanal utama penyebaran di Indonesia (bagian A) |
| 7 | **pembayaran / amplop digital** | fitur amplop digital | diputuskan **rekening + QRIS statis** — **tanpa payment gateway**, jadi **tanpa biaya per transaksi dan tanpa biaya bulanan** |
| 8 | **i18n + kaligrafi Islami** | khitanan/pernikahan Muslim, multi-bahasa | bagian F |
| 9 | **upscaling raster + vectorization** *(BARU — lahir dari keputusan G3, bukan dari daftar awal)* | mitigasi foto kurang resolusi + membuat ornament jadi vektor | **TERUJI 17 Sep: `cv2.dnn_superres` + FSRCNN_x2 (39 KB) / ESPCN_x2 (85 KB) BISA**, 2–4 dtk untuk A4@300. **Real-ESRGAN & EDSR GUGUR** (butuh PyTorch / OOM-KILL). `vtracer` untuk vektorisasi gambar datar ✅ (23 KB), ❌ untuk foto (6,4 MB). Rincian: bagian 4.4 + DISKUSI_MENTAH P |

### 6.1 Cara memasang skill — **DIKUNCI** (jawab atas delegasi pemilik)

Pemilik: *"Aku kurang paham… akan lebih baik klo kamu melakukan riset di internet mengenai cara pasng
skill dan plugin yang paling maksimal dan terbik."* Riset lengkap: DISKUSI_MENTAH bagian **O**.

**Jalur yang dipilih: `git clone` + salin folder skill-nya saja + VENDOR ke dalam repo (project-scoped).**

| Jalur yang tersedia | Dipakai? | Alasan |
|---|---|---|
| `/plugin marketplace add` + `/plugin install` | **TIDAK** | slash command Claude Code CLI — **tidak bisa dijalankan agent dari shell di lingkungan ini** |
| `npx skills add` / `npx skillstore add` | **TIDAK sebagai jalur utama** | npm terjangkau, tetapi repo ini punya **preseden buruk: `npx skills find` GAGAL-DIAM** (skills.sh terblokir). Tidak boleh dipercaya tanpa diuji |
| **`git clone` + vendor ke repo** | **YA** | **satu-satunya yang sudah terbukti** di lingkungan ini (github.com terjangkau) |
| ZIP manual | cadangan | provenance-nya lebih lemah (tidak ada sha sumber) |

**Kenapa di-vendor ke dalam repo, bukan dipasang di `~/.claude/skills/`:**

1. **Bertahan antar sesi** — pemasangan di luar repo (dan `pip install`) **terbukti tidak persisten** di
   lingkungan ini. Skill yang hilang tiap sesi = mekanisme yang tidak bisa diandalkan.
2. **Self-contained** — sesuai filosofi repo ini (W-07 + `check_selfcontained.py`).
3. **Bisa diaudit dan di-rollback** — versinya tercatat di git, bukan "terpasang suatu hari".
4. **Preseden yang sudah berjalan**: `sistem/sistem-building-aplikasi/skills/` berisi 56 skill.
5. **Standar Agent Skills lintas alat** (`agentskills.io`): `SKILL.md` dipakai bersama oleh Claude Code,
   Codex CLI, OpenCode, Cursor — tidak mengunci ke satu alat.

**Aturan keamanan yang WAJIB** (sumber: *"Skills can execute arbitrary code in Claude's environment. Only
install skills from trusted sources. Review SKILL.md and all scripts before enabling"*):

1. **Baca `SKILL.md` + semua skripnya SEBELUM di-commit** — bukan sesudah.
2. **Catat provenance per skill**: repo sumber, **sha commit** yang disalin, tanggal, **lisensi**. Tanpa
   sha, "skill X terpasang" tidak bisa direproduksi.
3. **Tolak skill yang meminta akses data sensitif** atau memanggil layanan eksternal — semua API eksternal
   **terblokir** di sini, jadi skill semacam itu **memang tidak akan jalan**.
4. **Skill yang gagal diuji tidak boleh dinyatakan terpasang** — statusnya *"ada di repo, belum terbukti
   jalan"*, ditulis apa adanya.

**Alurnya untuk 9 gap:** agent **mengusulkan per butir** (repo sumber + lisensi + alasan) → pemilik
**setujui atau ganti** → agent **clone + review + vendor + catat provenance + uji** → baru dinyatakan
terpasang. **Tidak ada yang dipasang diam-diam.**

**Mekanisme penawarannya** tetap mengikuti preseden repo: pola `05_TAWARAN_KAPABILITAS.md` di
`sistem/sistem-klinik/_sistem/` — **WAJIB-BERTAJUK dan boleh ditolak**.

---

## 7. Rencana Dokumen

Kolom terakhir menentukan apakah dokumen perlu **prompt Discovery detail tersendiri** (dokumen
generator — harus digali lewat diskusi) atau **cukup template biasa** (langsung diisi).

| Dokumen | Fungsi | Lapis | Perlu prompt Discovery detail? |
|---|---|---|---|
| `00_RENCANA_KERANGKA.md` | dokumen ini, setelah final | — | tidak (sudah) |
| `01_IDENTITAS_PEMILIK.md` | isi Lapis 1: merek, font/palet default, kebijakan serah terima, rekening+QRIS | **L1** | **YA — generator** |
| `02_PROFIL_JENIS_ACARA.md` | isi Lapis 2 **per jenis acara**: field default, konvensi desain & etika, kata baku | **L2** | **YA — generator** |
| `03_TEMPLATE_DATA_ACARA.md` | skema data acara (hal konsisten #1) — diisi per undangan | L3 | cukup template |
| `04_TEMPLATE_BRIEF_UNDANGAN.md` | brief Tahap 1–2 | L3 | cukup template |
| `05_DISCOVERY_DESAIN_PROMPT.md` | menggali desain & format bersama client (Tahap 3) | L3 | **YA — generator** |
| `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` | **dua tingkat aset + gerbang G3 fail-closed** (hal konsisten #3) | lintas | **YA — generator** (isinya keputusan berisiko, bukan isian) |
| `07_SPESIFIKASI_CETAK_PREPRESS.md` | CMYK/300 DPI/bleed 3 mm/safe zone/crop marks/PDF-X/batas tinta (hal konsisten #4) | lintas | **cukup template** — risetnya sudah lengkap di bagian C |
| `08_PIPELINE_VIDEO.md` | render video + keputusan lisensi Remotion vs alternatif | lintas | cukup template + **1 keputusan pemilik** (lisensi) |
| `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` | Tahap 6–7: deploy, hosting di akun client, CMS non-coder, masa aktif, cara revisi setelah tayang | lintas | **YA — generator** (T7: pemilik minta arahan) |
| `10_ARSITEKTUR_WEBSITE_INDUK.md` | T11: satu domain + undangan sebagai subpath; Cloudflare Pages/Workers/D1/KV/R2; plafon terukur | lintas | **YA — generator** (keputusan arsitektur besar) |
| `11_AMPLOP_DIGITAL.md` | rekening + QRIS statis, tanpa payment gateway | lintas | cukup template |
| `Input-Pengguna/` (folder) | T14: tempat pemilik menaruh font, template, contoh, referensi | lintas | cukup struktur folder + README |
| `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` | **W-01** — satu pedoman INDUK lengkap (T16/T17) | — | dari `_meta/PANDUAN_PENGGUNA_TEMPLATE.md` (sudah memuat Standar Kelulusan Manual 5 syarat) |
| `SYSTEM_MANIFEST.md` | **W-04** | — | dari `_meta/SYSTEM_MANIFEST_TEMPLATE.md` |
| `12_LOG_SESI.md` | **W-02** | — | dari `_meta/TEMPLATE_LOG_SESI.md`. **Dinomori 12, bukan 10** — nomor 10 sudah dipakai `10_ARSITEKTUR_WEBSITE_INDUK.md` dan bentrokannya baru ketahuan saat skeleton dibuat |
| `STATUS.md` (per unit kerja) | **W-03** | — | dari template STATUS (field deterministik exact) |
| `QUALITY_ASSURANCE_AND_EVOLUTION.md` | **W-06** | — | pola sistem anak yang sudah ada |
| `ACCEPTANCE_TESTS.md` + log-nya | uji penerimaan | — | pola sistem-klinik |
| turunan `PROTOKOL_AUDIT_ISI` | **W-10** — mekanisme audit isi self-contained di dalam folder | — | **belum ada turunannya di sistem anak mana pun** → item **T-07** |

**Jumlah: 4 dokumen generator** (01, 02, 05, 06) **+ 2 generator lintas** (09, 10) = **6 prompt
Discovery detail** yang harus ditulis sesudah rencana ini di-merge — **bukan** langsung menulis isi
sistemnya (peringatan eksplisit di `_meta/01_DISCOVERY_LEVEL_0.md` bagian "Setelah selesai" butir 3).

---

## 8. Prinsip yang Dipakai / Di-override

Sumber: `_meta/02_PRINSIP_UNIVERSAL.md` (6 prinsip).

| Prinsip | Status | Bagaimana dipakai di sistem ini |
|---|---|---|
| **1. Hierarki** | **DIPAKAI apa adanya** | 3 lapis L1→L2→L3; penyimpangan boleh tetapi **wajib tercatat**, tidak boleh diam-diam |
| **2. Rantai / Chaining** | **DIPAKAI apa adanya** | **satu sumber data → banyak format** (web, video, flyer, cetak). Ini alasan hal konsisten #1 paling berbahaya |
| **3. Approval Bertingkat** | **DIPAKAI apa adanya** | 6 gerbang + 3 tingkat risiko (bagian 4) |
| **4. Checkpoint & Verifikasi Konsistensi** | **DIPAKAI + DIPERKUAT** | checkpoint **di tiap gerbang**, bukan di akhir — dipaksa oleh fakta platform "tidak bisa push setelah PR merge/close". Penguatannya: **gerbang resolusi fail-closed** (4.3) |
| **5. Log Keputusan** | **DIPAKAI apa adanya** | di setiap dokumen hidup + per unit kerja |
| **6. QA & Evolusi 3-lapis** | **DIPAKAI apa adanya** | batas pentingnya dihormati: **audit menghasilkan temuan, tidak otomatis mengubah keputusan yang sudah dikunci** |
| **Pemisahan Konsistensi Visual vs Non-Visual** (dinyatakan **TIDAK universal**) | **DIPAKAI, dengan alasan eksplisit** | dokumen sumbernya sendiri berkata sistem lain *"mungkin saja butuh jenis konsistensi lain yang analog … yang perlu digali sendiri saat Discovery Level-0"*. **Digali di bagian 3**: domain ini butuh **keduanya** — visual (undangan adalah benda visual) **dan** skema data (satu sumber → banyak format). Jadi ini **bukan mewarisi definisi konten kreator**, melainkan hasil penggalian sendiri |

**Tidak ada prinsip yang di-override.** Kalau nanti ada yang harus di-override, wajib dicatat di sini
beserta alasan, dampak, dan approval pemilik — **bukan diabaikan diam-diam**.

---

## 9. Warisan (Kontrak) — W-01 … W-10

Sumber: `_meta/03_KONTRAK_WARISAN.md`. **DEFAULT: semua diterapkan.** Tidak ada butir yang
di-override di rencana ini.

| Butir | Status untuk `sistem-undangan` | Bagaimana |
|---|---|---|
| **W-01** Pegangan pengguna 2-file | **diterapkan** | `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` dari template meta. **Ini juga jawaban T4** ("satu prompt pembuka") dan **T16/T17** (satu pedoman INDUK lengkap) |
| **W-02** Log sesi berkelanjutan | **diterapkan** | `12_LOG_SESI.md` dari `_meta/TEMPLATE_LOG_SESI.md`, **self-contained** + langkah recovery di prompt pembuka |
| **W-03** Kontrak checkpoint unit kerja | **diterapkan** | `STATUS.md` per unit kerja (1 undangan = 1 unit) dengan field deterministik exact |
| **W-04** Manifest sistem | **diterapkan** | `SYSTEM_MANIFEST.md` dari template, dibuat **dalam PR yang sama** dengan rencana ini (aturan M-14) |
| **W-05** Log Keputusan di dokumen hidup | **diterapkan** | di tiap dokumen generator + per unit |
| **W-06** QA & evolusi 3-lapis | **diterapkan** | `QUALITY_ASSURANCE_AND_EVOLUTION.md` di folder sistem |
| **W-07** Fakta platform lmarena | **diterapkan** | bagian **Batasan Platform** inline di manifest (bagian 5 dokumen ini jadi sumbernya) |
| **W-08** Approval Bertingkat | **diterapkan** | 6 gerbang G0–G5 + 3 tingkat risiko (bagian 4) |
| **W-09** Ringkasan cadangan | **diterapkan** | RINGKASAN di `_cadangan-claude/` saat sistem siap-pakai |
| **W-10** Audit isi + pengiriman hasil | **diterapkan, dengan catatan jujur** | mekanisme **tersedia dari meta** (`tools/audit_prompt.py --objek sistem/sistem-undangan` + `tools/ambil_verdict.py`). **Turunan self-contained di dalam folder BELUM ADA — dan belum ada di sistem anak mana pun** → item **T-07** di `_meta/DAFTAR_PEKERJAAN_TERBUKA.md`. Sistem ini **tidak boleh mengklaim W-10 penuh** sebelum turunan itu dibuat |

---

## 10. Yang harus kamu putuskan (7 pertanyaan review)

Ini **kategori BESAR**, jadi aku tidak menguncinya sendiri. Urut dari yang paling menentukan:

| # | Pertanyaan | Usulanku | Kenapa |
|---|---|---|---|
| **1** | ~~Bentuk dasar~~ → **DIJAWAB PEMILIK: "Setuju — kunci bentuk ini"** ✅ | **DIKUNCI** | kamu delegasikan di giliran 3; alasannya di 2.1 dan **bisa diuji** (ubah L1 → semua undangan belum-G2 ikut berubah, yang sudah terbit tidak) |
| **2** | **7 hal yang harus konsisten** (bagian 3) — ada yang kurang atau berlebih? | pertahankan 7 | yang **sengaja tidak** dikunci juga sudah kusebut, supaya tidak semua undangan jadi kembar |
| **3** | **6 gerbang + tingkat risikonya** — setuju **G0, G2, G5 dan perubahan L1 = review isi lengkap olehmu**? | setuju | sisanya bisa diwakilkan agent supaya kamu tidak kelelahan menyetujui hal-hal kecil |
| **4** | ~~G3 fail-closed~~ → **DIJAWAB PEMILIK: jangan terlalu ketat, siasati dengan upscaling AI** ✅ | **DIROMBAK jadi 3 hasil + pengalihan menurut jenis isi** (4.3), lalu **DIPERKETAT oleh hasil uji** (4.4 + 4.5) | ide pemilik **diterima sebagian dan dipertajam**: upscaling **sah untuk foto ≤2× dari ≥150 DPI**, tetapi **mengarang detail untuk teks/garis halus** dan undangan didominasi keduanya. Ditambah **langkah 0** yang menghapus masalahnya secara struktur: teks wajib dari font, ornament wajib vektor → hanya foto yang masuk gerbang |
| **5** | ~~Website induk / domain~~ → **DIJAWAB PEMILIK: subdomain gratis dulu, satu domain saat rilis, client yang mau domain sendiri menanggung biayanya** ✅ | **DIKUNCI sebagai kebijakan 3 fase** (bagian 5) | usulan agent semula ("harus beli domain") **dikoreksi pemilik** dan koreksinya **lebih baik**: fase percobaan jadi benar-benar nol biaya. **Konsekuensi rancangan yang mengikat dan kutambahkan sendiri: PATH wajib stabil lintas fase**, supaya tautan yang sudah disebar ke tamu tidak mati saat naik fase |
| **6** | **Aset besar TIDAK masuk repo** (resep + sumber kecil saja yang masuk) | setuju | plafon artefak sesi ±128 MB / 10.000 berkas; melanggar ini membuat pekerjaan **tidak bisa di-commit** |
| **7** | ~~8 gap skill~~ → **DIJAWAB PEMILIK: delegasi + mandat riset cara pasang** ✅ | **DIKUNCI: git clone + vendor project-scoped ke repo**, usul per butir sebelum memasang (6.1) | riset menunjukkan `/plugin` **tidak bisa dijalankan dari sini** dan `npx skills` punya **preseden gagal-diam** di repo ini; vendor ke repo **satu-satunya yang persisten antar sesi**. Daftar gap jadi **9 butir** (upscaling+vektorisasi ditambah dari keputusan #4) |

**SEMUA 7 PERTANYAAN SELESAI (17 Sep 2026).** #2, #3, #6 diterima lewat konfirmasi final pemilik tanpa keberatan (sebelumnya sudah dinyatakan *"kalau tidak ada keberatan, kupakai usulanku"*). #4 melahirkan uji T-28 (bagian 4.4) dan T-30 (bagian 4.5) yang **memperketat** usulan awalnya.

**Satu hal yang tidak kutanyakan karena sudah kamu putuskan:** acara pertama = **pernikahan**, nama =
**`sistem-undangan`**, skala = **solo/≤3 orang**. Ketiganya kupakai sebagai masukan tetap.

---

## 11. Langkah berikutnya sesudah draft ini dikonfirmasi

1. ✅ **SELESAI 17 Sep 2026** — `sistem/sistem-undangan/` dibuat + rencana ini disalin sebagai
   `00_RENCANA_KERANGKA.md`.
2. ✅ **SELESAI** — `SYSTEM_MANIFEST.md` dari template, **`Tahap: kerangka`**, `Versi 0.1.0`,
   `Status Proposed`, bagian **Batasan Platform** (W-07) dan **Warisan** 10 butir.
3. ✅ **SELESAI** — skeleton 11 dokumen + `Input-Pengguna/` + validator sistem sendiri
   (`_sistem/validate_system.py`). **Semua dokumen masih KERANGKA, belum ada isi.**
4. ✅ **SELESAI** — didaftarkan di `_meta/INDEKS_SISTEM.md`. **Catatan konflik aturan yang ditemukan:**
   kalimat "Cara pakai" di INDEKS berkata baris baru ditambah **sesudah merge**, tetapi
   `tools/validate_repo.py` menjadikan folder `sistem-*/` yang tidak terdaftar sebagai **ERROR** —
   jadi barisnya **wajib** ada di PR yang sama. **Validator yang menang** (ia yang bisa menegakkan),
   dan konfliknya dilaporkan sebagai temuan, tidak didiamkan.
5. ⏳ **PR dibuat, tanpa auto-merge** — menunggu review **L1** pemilik (perubahan struktural + sistem baru).
6. ⏳ **Sesudah merge**: tulis **6 prompt Discovery detail** (bagian 7) — **bukan** langsung menulis isi
   sistemnya. **Yang juga belum ada dan sengaja tidak dibuat sekarang:** `PANDUAN_PENGGUNA.md` +
   `PROMPT_ENTRI_UNIVERSAL.md` (W-01) — alur menaruhnya di langkah 6 sesudah dokumen, dan membuatnya
   setengah jadi akan melanggar **Standar Kelulusan Manual 5 syarat**. Di tahap `kerangka` ketiadaan
   keduanya **dilonggarkan jadi warning** oleh validator, bukan disembunyikan.
   **KOREKSI 18 Sep 2026 (keadaan terkini — menutup temuan hakim putaran 3 PR #74):** kalimat "yang juga
   belum ada dan sengaja tidak dibuat sekarang" di atas adalah **keadaan saat langkah 6 ini ditulis**, dan
   dipertahankan apa adanya sebagai riwayat. Keadaan sekarang: `PANDUAN_PENGGUNA.md` dan
   `PROMPT_ENTRI_UNIVERSAL.md` **SUDAH dibuat 18 Sep 2026** (keduanya ada di folder ini, blok prompt-nya
   identik), tercatat di Log Keputusan di bawah dan di `SYSTEM_MANIFEST.md` (baris *Entry point* dan
   *Pegangan pengguna*). Yang **belum boleh dinyatakan adalah KELULUSANNYA** (Standar Kelulusan Manual
   syarat 4) — bukan keberadaannya. Jangan membaca kalimat riwayat itu sebagai keadaan sekarang: satu
   berkas yang membantah dirinya sendiri adalah temuan review, dan itu yang terjadi di sini.

**Yang menutup utang kalau ini jalan:** item **T-18** (tujuan awal sesi) dan **6 tuntutan ber-status
`TERJADWAL`** di ledger tanggapan — **T1, T2, T5, T6, T11, T13, T14, T15** semuanya mengalir ke
dokumen-dokumen di bagian 7, plus **T-06** terjawab lewat pertanyaan review #7.

---

## Log Keputusan

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-17 | Draft ini ditulis di `_meta/_internal/`, **bukan** di folder sistem | Folder `sistem-*/` yang tidak terdaftar di INDEKS = **error validator**, dan alur melarang membuat folder sebelum rencana kerangka dikonfirmasi final. Preseden: keputusan yang sama untuk DISKUSI_MENTAH |
| 2026-09-17 | **Bagian 2, 3, 4 ditandai sebagai rekonstruksi** dan dipisah dari bagian yang punya dasar riset | **Kejujuran soal provenance.** Grep membuktikan `BERTINGKAT`, `SIKLUS 7`, `7 hal konsisten`, `G5` **tidak muncul sekali pun** di berkas repo, sementara fakta risetnya muncul 2–12 kali. Pemilik berhak tahu bagian mana yang **belum pernah dia lihat** supaya review-nya teliti di tempat yang benar |
| 2026-09-17 | **G3 dibuat fail-closed**, bukan peringatan | Lahir dari **koreksi pemilik** yang terbukti benar oleh aritmetika (bagian J.2/J.3): usulan agent "foto maks ~300 KB" **dicabut sebagai salah**. Gerbang yang bisa ditawar bukan gerbang |
| 2026-09-17 | **Tahap Serah Terima dipisahkan dari Terbit** (7 tahap, bukan 6) | Keduanya punya pemilik risiko berbeda: Terbit = tindakan teknis, Serah Terima = **perpindahan kepemilikan akun**. Mencampurnya adalah cara paling umum client kehilangan akses ke situsnya sendiri |
| 2026-09-17 | **Tidak ada prinsip universal yang di-override**, dan prinsip "tidak universal" (visual vs non-visual) **dipakai dengan alasan eksplisit** | Dokumen sumbernya sendiri memerintahkan menggali jenis konsistensi yang analog **sendiri**, bukan mewarisi definisi konten kreator. Hasil galiannya di bagian 3: domain ini butuh **keduanya** |
| 2026-09-17 | **W-10 ditulis "diterapkan, dengan catatan jujur"**, bukan "diterapkan" | Turunan self-contained belum ada di sistem anak mana pun (item T-07). Mengklaim penuh akan mengulangi **persis** kesalahan yang ditemukan di induk: mengklaim kepatuhan tanpa artefak |
| 2026-09-17 (sore) | **Bentuk dasar DIKUNCI** — BERTINGKAT 3 lapis + SIKLUS 7 tahap | Persetujuan eksplisit pemilik pada pertanyaan review #1 |
| 2026-09-17 (sore) | **G3 DIROMBAK dari 2 hasil jadi 3 hasil + pengalihan menurut jenis isi**, dan ditambah **langkah 0** (teks wajib dari font, ornament wajib vektor) | Masukan pemilik + riset 6 sumber. **Bukan melonggarkan gerbang**: yang ditolak tetap ditolak, tetapi ancamannya kini dibedakan karena memang berbeda — foto yang di-upscale 2× tidak berisiko mengubah isi, teks yang di-upscale **bisa mengubah nama orang**. Langkah 0 membuat dua dari tiga jenis isi **tidak pernah masuk gerbang sama sekali** |
| 2026-09-17 (sore) | **Kebijakan domain 3 fase DIKUNCI**, dan agent menambahkan syarat **PATH stabil lintas fase** | Kalimat pemilik sendiri. Syarat path stabil **tambahan dari agent**: kalau path berubah saat naik fase, semua tautan yang sudah disebar ke tamu mati dan **tidak bisa diperbaiki setelah undangan beredar** |
| 2026-09-17 (sore) | **Cara pasang skill DIKUNCI: git clone + vendor project-scoped**, dengan 4 aturan keamanan wajib | Delegasi + mandat riset pemilik. `/plugin` tidak bisa dijalankan dari lingkungan ini; `npx skills` punya preseden **gagal-diam** di repo ini; vendor ke repo satu-satunya yang **persisten antar sesi** dan sesuai filosofi self-contained |
| 2026-09-17 (sore) | **Gap skill jadi 9 butir** — upscaling raster + vectorization ditambahkan | Kebutuhan ini **lahir dari keputusan G3**, bukan ada di daftar awal. Mencatatnya sebagai gap baru lebih jujur daripada menyelipkannya ke butir "generate gambar" |
| 2026-09-17 (malam) | **G3 jalur LOLOS BERSYARAT DIPERTAHANKAN, tetapi alatnya diganti, klaim mutunya diturunkan, dan cetak uji diwajibkan untuk semua kasus** | **Hasil uji T-28, bukan pendapat.** EDSR OOM-KILL; Real-ESRGAN butuh PyTorch; FSRCNN/ESPCN jalan 2–4 dtk. Keuntungan AI atas lanczos4 hanya +0,28…+0,55 dB dengan SSIM praktis identik → **menjanjikan lebih dari itu ke client = menjanjikan hal yang tidak didukung bukti** |
| 2026-09-17 (malam) | **Langkah 0 naik status jadi kesimpulan terukur** | PSNR guratan tipis **20,8–22,6 dB untuk SEMUA metode**, di bawah ambang 32 milik repo sendiri. Teks/ornament **tidak punya jalur raster yang layak cetak** — jadi mewajibkan font+vektor bukan soal selera |
| 2026-09-17 (final) | **Ambang LOLOS BERSYARAT DIPERKETAT ≥150 → ≥200 DPI dan ≤2× → ≤1,5×; AI upscaling KELUAR dari jalur kritis, diganti `Lanczos4`** | **Hasil pengukuran, bukan pilihan dari dua usulan** (bagian 4.5). AI terukur **tidak memberi keuntungan pada foto** (pada 1,5× lebih buruk di kedua metrik) dan **hanya unggul pada garis halus — jenis isi yang justru dilarang Langkah 0**. Bonus yang tidak direncanakan: **ketergantungan `pip install` hilang dari jalur kritis**, padahal `pip install` tidak bertahan antar sesi di lingkungan ini |
| 2026-09-17 (final) | **Dokumen ini FINAL; folder sistem dibuat dalam PR yang sama** | Konfirmasi eksplisit pemilik: *"Setuju — finalisasi dan buat PR-nya"*. Kategori BESAR → review isi lengkap, bukan konfirmasi ringan |
| 2026-09-17 (final) | **`10_LOG_SESI.md` dinomori ulang jadi `12_LOG_SESI.md`** | Bentrok nomor dengan `10_ARSITEKTUR_WEBSITE_INDUK.md` — **ditemukan saat skeleton dibuat**, bukan saat direncanakan. Bukti bahwa rencana di atas kertas tetap harus dibenturkan ke kenyataan folder |
| 2026-09-17 (final) | **Baris INDEKS dimasukkan di PR yang sama, menyimpang dari kalimat "Cara pakai" INDEKS sendiri** | `tools/validate_repo.py` menjadikan folder sistem tak terdaftar sebagai **ERROR**, sedangkan kalimat INDEKS berkata "sesudah merge". **Yang bisa menegakkan yang diikuti**, dan konfliknya **dilaporkan sebagai temuan** (tuntutan T31), tidak didiamkan |
| 2026-09-18 | **Pegangan pengguna W-01 dibuat, dan validator mandiri diperketat untuk menegakkannya dari dalam folder sendiri** | Menutup temuan **R1** review independen PR #74: validator repo mengeluarkan 2 peringatan karena pegangan belum ada, sehingga syarat penerimaan "lulus tanpa peringatan" tidak terpenuhi. Ada dua jalan: melonggarkan syarat pemeriksa, atau membuat pegangannya. **Yang dipilih yang kedua** — melonggarkan syarat alat penilai demi pekerjaan penulis yang belum selesai adalah pola menggeser gawang, dan pegangan pengguna justru inti tuntutan pemilik sejak awal (satu prompt pembuka, satu pedoman induk, pemilik tidak punya basic coding). Sekalian ditemukan ketidakkonsistenan: **validator benih yang dibangkitkan build_template.py sudah mewajibkan kedua berkas manual, sedangkan validator sistem nyata tidak** — benih lebih ketat dari sistemnya. Daftar wajib validator mandiri ditambah 2 → 4 berkas, **diuji mutasi** (hapus satu manual → exit 1). **Kelulusan pegangan sengaja TIDAK dinyatakan di dokumen mana pun**: Syarat 4 Standar Kelulusan Manual melarang penulis menilai sendiri, jadi yang dicatat adalah keadaannya (sudah dibuat, 0 kandidat dari alat penjaring dengan kontrol positif) dan yang masih kurang (audit lensa kemudahan pakai + uji pemakaian nyata oleh pemilik) |
