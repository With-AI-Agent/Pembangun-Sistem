# Rencana Kerangka — Sistem `sistem-undangan`

> **STATUS: DRAFT untuk review pemilik — BELUM final, BELUM ada folder sistem yang dibuat.**
> Kategori **BESAR** per `_meta/02_PRINSIP_UNIVERSAL.md` (Prinsip 3): dokumen ini menentukan seluruh
> struktur sistem baru, jadi **WAJIB direview isi lengkapnya oleh pemilik sebelum merge**, bukan cukup
> konfirmasi ringan. Alur: `_meta/01_DISCOVERY_LEVEL_0.md`.
>
> **Sesudah kamu konfirmasi final**, langkah berikutnya (dalam **satu PR yang sama**, aturan M-14):
> buat `sistem/sistem-undangan/` + `00_RENCANA_KERANGKA.md` + `SYSTEM_MANIFEST.md` dari template +
> skeleton folder + daftar di `_meta/INDEKS_SISTEM.md` dengan **`Tahap: kerangka`**.

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

## 2. Bentuk Dasar — **GABUNGAN: BERTINGKAT 3 lapis + SIKLUS 7 tahap**

> **Rekonstruksi — belum pernah tertulis. Butuh review paling teliti.**

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

### 4.3 **G3 wajib fail-closed** — keputusan yang lahir dari koreksi pemilik

Bagian J.3 DISKUSI_MENTAH mencatat bahwa **usulan agent sendiri ("foto maks ~300 KB") DICABUT sebagai
salah** setelah pemilik keberatan dan aritmetikanya diperiksa: kompresi web dan kelayakan cetak adalah
**dua kebutuhan yang bertentangan** dan tidak bisa diatur satu angka.

Maka aturannya: **kalau sumber aset tidak memenuhi resolusi yang dibutuhkan ukuran cetak akhirnya,
format cetak DITOLAK** — agent **dilarang** menurunkan kualitas diam-diam, dilarang menjanjikan "siap
cetak" untuk aset yang tidak lolos, dan **wajib** melaporkan ke pemilik bahwa format cetak tidak bisa
dipenuhi beserta angka kekurangannya. **Gerbang yang bisa ditawar bukan gerbang.**

---

## 5. Batasan Platform (pertanyaan 5 — WAJIB)

**Dipakai via lmarena Agent Mode: YA.** Sumber fakta: `_meta/PLATFORM_LMARENA.md` (5 fakta + 6 policy).

| Fakta platform | Konsekuensi untuk sistem ini |
|---|---|
| Branch arena otomatis dibuat, tidak bisa asumsi kerja di `main` | semua kerja sistem lewat **PR**, tanpa auto-merge |
| **Tidak bisa push setelah PR merge/close** (platform cabut akses) | **checkpoint wajib di tiap gerbang**, bukan di akhir; pekerjaan yang belum ter-commit saat PR ditutup **hilang** |
| Sesi bisa crash kapan saja | turunan **`LOG_SESI` self-contained** (W-02) + `STATUS.md` per unit (W-03) + langkah recovery di prompt pembuka |
| **Semua API layanan eksternal terblokir** (hanya npm, PyPI, github.com) | **deploy harus Git-based**; tidak ada panggilan API runtime ke layanan AI/pihak ketiga dari dalam sesi |
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

**Mekanisme penawarannya** mengikuti preseden repo: pola `05_TAWARAN_KAPABILITAS.md` di
`sistem/sistem-klinik/_sistem/` — **WAJIB-BERTAJUK dan boleh ditolak**, bukan dipasang diam-diam.

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
| `10_LOG_SESI.md` | **W-02** | — | dari `_meta/TEMPLATE_LOG_SESI.md` |
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
| **W-02** Log sesi berkelanjutan | **diterapkan** | `10_LOG_SESI.md` dari `_meta/TEMPLATE_LOG_SESI.md`, **self-contained** + langkah recovery di prompt pembuka |
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
| **1** | **Bentuk dasar: BERTINGKAT 3 lapis + SIKLUS 7 tahap** — setuju? | **setuju** | kamu delegasikan di giliran 3; alasannya di 2.1 dan **bisa diuji** (ubah L1 → semua undangan belum-G2 ikut berubah, yang sudah terbit tidak) |
| **2** | **7 hal yang harus konsisten** (bagian 3) — ada yang kurang atau berlebih? | pertahankan 7 | yang **sengaja tidak** dikunci juga sudah kusebut, supaya tidak semua undangan jadi kembar |
| **3** | **6 gerbang + tingkat risikonya** — setuju **G0, G2, G5 dan perubahan L1 = review isi lengkap olehmu**? | setuju | sisanya bisa diwakilkan agent supaya kamu tidak kelelahan menyetujui hal-hal kecil |
| **4** | **G3 fail-closed**: kalau aset kurang resolusi, **format cetak DITOLAK** dan dilaporkan — bukan diturunkan diam-diam. Setuju? | **setuju, dan ini yang paling penting** | lahir dari koreksimu sendiri (bagian J.3). Gerbang yang bisa ditawar bukan gerbang |
| **5** | **Website induk: satu domain + undangan sebagai subpath**, hosting di **akun client**, repo Git sebagai database | setuju | pola yang terbukti di pasar (bagian A/B) dan **nol biaya bulanan**. **Konsekuensi yang harus kamu terima: client (atau kamu) harus membeli domain** — itu satu-satunya biaya yang tidak bisa nol |
| **6** | **Aset besar TIDAK masuk repo** (resep + sumber kecil saja yang masuk) | setuju | plafon artefak sesi ±128 MB / 10.000 berkas; melanggar ini membuat pekerjaan **tidak bisa di-commit** |
| **7** | **8 gap skill** (T-06): kamu kirim link, atau izinkan aku pilih dan pasang? | **kirim link dulu untuk yang kamu punya**, sisanya aku usulkan per butir sebelum memasang | kamu bilang akan mengirim link; dan memasang skill = memasukkan kode pihak ketiga, jadi **tidak kulakukan diam-diam** |

**Satu hal yang tidak kutanyakan karena sudah kamu putuskan:** acara pertama = **pernikahan**, nama =
**`sistem-undangan`**, skala = **solo/≤3 orang**. Ketiganya kupakai sebagai masukan tetap.

---

## 11. Langkah berikutnya sesudah draft ini dikonfirmasi

1. Buat `sistem/sistem-undangan/` + salin rencana ini sebagai `00_RENCANA_KERANGKA.md`.
2. Salin `_meta/SYSTEM_MANIFEST_TEMPLATE.md` → `SYSTEM_MANIFEST.md`, isi identitas awal, **`Tahap: kerangka`**,
   bagian **Batasan Platform** (W-07) dan **Warisan** 10 butir.
3. Buat **skeleton folder** sesuai bagian 7 (dokumen generator masih berupa kerangka, bukan isi).
4. Daftarkan di `_meta/INDEKS_SISTEM.md` dengan **`Tahap: kerangka`** — wajib, karena folder
   `sistem-*/` yang tidak terdaftar = **error validator**.
5. **Satu PR** untuk semuanya (aturan M-14), **tanpa auto-merge**, direview **L1** (perubahan
   struktural + sistem baru).
6. **Sesudah merge**: tulis **6 prompt Discovery detail** (bagian 7) — **bukan** langsung menulis isi
   sistemnya.

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
