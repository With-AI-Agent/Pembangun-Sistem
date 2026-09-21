# Discovery Desain & Format — Prompt (Tahap 3 SIKLUS)

> **STATUS: ISI — DRAFT.** Diisi 2026-09-21 (UTC) lewat **ROADMAP JALAN PRODUKSI PERTAMA butir b2**
> (handoff log sesi slot 43/44; dikerjakan sesi slot 45) sebagai dokumen **generator** per
> `00_RENCANA_KERANGKA.md` bagian 7. Berbeda dari dokumen domain lain: dokumen ini **tidak memuat
> keputusan tentang sistem**, melainkan **prompt kerja yang menghadap CLIENT** saat Tahap 3 siklus —
> isinya = cara bertanya, menu yang ditawarkan, dan **batas janji**.
> Keputusan yang mengikat di dalamnya **disetujui pemilik 2026-09-21 lewat paket B1–B6** (bentuk
> dokumen · menu arah desain · batas format · lead time & revisi · moderasi & data ucapan · cara
> menyelesaikan konflik urutan dokumen 09 vs 10) — approval tercatat di Log Keputusan dokumen ini.
> Banner kerangka dicabut di commit yang sama dengan perluasan validator (mekanika T-69/prompt 02).

| | |
|---|---|
| **Berkas** | `05_DISCOVERY_DESAIN_PROMPT.md` |
| **Lapis** | L3 — Undangan Konkret (dijalankan **per undangan**, bukan sekali untuk sistem) |
| **Cara diisi** | **YA — prompt Discovery detail** (`_sistem/PROMPT_DISCOVERY_05_DESAIN_DAN_FORMAT.md`) — **sudah dijalankan 2026-09-21** dengan pola *delegasi + paket keputusan* (approval pemilik atas B1–B6) |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (siklus bagian 2.3 · gerbang bagian 4 · rencana dokumen bagian 7) + `01_IDENTITAS_PEMILIK.md` (§2 font · §3 palet · §4 ornament · §5 nada · §6 harga & masa aktif · §8 serah terima · §10 batasan mutlak) + `02_PROFIL_JENIS_ACARA.md` (§6 konvensi desain & 9 pantangan & katalog 8 model · §7 hal yang selalu konsisten · §8 siklus · §9 fitur) + `04_TEMPLATE_BRIEF_UNDANGAN.md` (bentuk brief) + approval pemilik atas paket B1–B6 (log sesi slot 45) |

## Fungsi dokumen ini

Prompt untuk **menggali desain & format bersama client** (Tahap 3 SIKLUS) — agent yang **bertanya dan
mengusulkan**, **bukan** menyuruh client mengisi formulir teknis. Hasil sesi ini =
**spesifikasi desain + daftar format target** untuk undangan itu, yang dikunci di gerbang **G2**.

## Catatan untuk yang mengisinya nanti

1. **Ini satu-satunya prompt di sistem ini yang menghadap CLIENT.** Prompt 01/02/06/10 menghadap pemilik.
   Karena itu bahasanya awam, dan **setiap tawaran wajib menyebut akibat visualnya** ("tamu akan lihat
   X saat membuka undangan di HP"), bukan istilah teknis.
2. **Wajib menghormati keputusan pemilik yang tidak ditawar ulang ke client:** desain
   **responsif-adaptif di semua layar** · **infrastruktur nol biaya bulanan** · **amplop digital =
   rekening + QRIS statis, tanpa payment gateway** · **teks dari font & ornament/logo wajib vektor**
   (Langkah 0 gerbang aset) · bahan milik pemilik di folder `Input-Pengguna/` **diperlakukan sebagai
   bahan**, dan bila foldernya kosong **dikatakan kosong** (jangan mengarang isi).
3. **Batas janji (§1), menu arah (§2), dan batas format (§3) mengikat agent.** Di luar itu = jangan
   berimprovisasi; catat sebagai **PERLU KEPUTUSAN PEMILIK** dan teruskan ke pemilik.
4. **Jangan menulis brief/spec final sebelum client (atau pemilik yang mewakilinya) bilang "cukup,
   tulis".** Ringkasan checkpoint (§6 langkah 4) adalah alatnya.

## Isi

### 1. Batas Janji Tahap 3 — apa yang boleh diucapkan agent

| Hal | Yang BOLEH dikatakan agent | Yang WAJIB "PERLU KEPUTUSAN PEMILIK" |
|---|---|---|
| **Format** | undangan **web** (selalu) + **flyer/poster statis** (portrait siap IG, landscape siap broadcast) | **video** & **cetak siap-cetak** — dokumennya belum ada (07/08 ditunda pemilik); jangan dijanjikan |
| **Waktu** | **3 hari kerja** untuk web, dihitung **sejak data lolos G1**; **revisi tak terbatas sebelum terbit**; revisi besar bisa menambah waktu; **jalur cepat** tersedia bila perlu (mis. hanya web, tanpa format tambahan) | tenggat yang lebih ketat dari 3 hari kerja · tenggat yang menabrak siklus sebar (H-30…H-14 digital) |
| **Harga** | fase **portofolio** (5 client pertama / 2 bulan): harga **fleksibel per client**; rentang acuan pasar Rp 50.000–500.000 boleh **disebut sebagai rujukan pasar**, bukan harga | **angka harga final untuk client ini** · paket mana (Basic/Premium/Luxury) · boleh gratis atau tidak |
| **Domain & hosting** | sekarang (fase 1) undangan terbit di **subdomain studio**: `lee-studio.pages.dev/<nama-undangan>`; **tanpa biaya bulanan** | siapa yang menanggung **domain sendiri** (fase 2/3) · pemindahan kepemilikan akun (ditolak default L1 §8 — client menerima link + arsip) |
| **Masa aktif** | **1 tahun** sejak acara · **perpanjangan gratis** · **tidak ada penonaktifan sepihak** | pengecualian apa pun di luar itu |
| **Aset client** | foto client **diperiksa dulu** terhadap syarat aset sebelum dijanjikan; ukuran asli + rencana pemakaian (seberapa besar di layar) **wajib ditanyakan** | janji lolos/ tidak lolos sebuah foto (gerbang aset **fail-closed**; lihat §8 soal dokumen 06) |
| **Musik** | boleh ada musik latar **hanya dengan tombol mati** (pantangan L2) — tidak autoplay | — |
| **Ucapan & RSVP** | lihat §5 (default publik tanpa moderasi; moderasi sesuai permintaan) | permintaan di luar §5 (mis. integrasi ke aplikasi lain) |

**Cara menyampaikannya ke client:** bukan sebagai daftar larangan, tetapi sebagai kalimat positif —
*"ini yang bisa saya kerjakan sekarang; yang ini saya catat dulu untuk pemilik studio"*.

### 2. Menu Arah Desain — 3 default + 2 sesuai permintaan

Ditawarkan **ke client, bukan ke pemilik**; semuanya berada di dalam batas L1/L2 (palet default
ivory/hitam/emas, font Playfair Display + Montserrat + Amiri, disiplin **maks 2 font · maks 3 warna ·
whitespace lega**).

| # | Arah | Palet & tipografi | Kapan ditawarkan |
|---|---|---|---|
| **A** | **Luxury gold klasik** | ivory/hitam/emas · Playfair Display + Montserrat · garis & bingkai tipis klasik | **selalu** (default & rekomendasi awal bila client tidak punya bayangan) |
| **B** | **Islami/Arab** | krem + emas · kaligrafi **Amiri** + arabesque/geometris, lengkung mihrab | **selalu** (khususnya acara Islami) |
| **C** | **Modern minimalis** | netral + **satu** aksen · Montserrat dominan, whitespace, nyaris tanpa ornament | **selalu** (khususnya client muda / minta simpel) |
| **D** | **Romantic floral** | pastel/ivory · Playfair + floral lembut | bila client **menyebut** bunga/lembut/pastel |
| **E** | **Nusantara elegan** | Jawa: coklat sogan/krem/emas (parang, truntum bentuk elegan) · Aceh/Minang: maroon/earthy + motif meukeutop/songket · **selalu bentuk elegan, bukan batik bermotif kuat** | bila client **menyebut** adat/daerah |

- **Alasan pemilihan menu (bukan katalog baru):** tiga arah default = tiga kelompok terkuat dari **17
  referensi yang pemilik pilih** di Discovery 01 (arah kesimpulan: *"elegan premium"*); dua arah
  "sesuai permintaan" tetap dilayani agar client daerah/floral tidak kehilangan jalur — pemilik
  menyatakan sendiri batik bermotif kuat & mega mendung **tidak** dijadikan default (data, bukan larangan).
- **Katalog 8 model di `02_PROFIL_JENIS_ACARA.md` §6 tetap berlaku** — statusnya **pilihan otomatis
  (fallback)** ketika client tidak memberi keterangan detail, **bukan aturan kaku** (koreksi pemilik
  20 Sep 2026). Menu di atas **tidak menggantikannya**; ia hanya menentukan **apa yang aktif ditawarkan**.
- **Model di luar menu = tetap dilayani.** Keinginan client menang (Prinsip Kerja Dasar L1). Yang wajib:
  penyimpangan dari palet/font L1 **dicatat di Log Keputusan unit + diberitahukan ke pemilik** (ia
  mempengaruhi konsistensi merek).
- **Penyajian ke client:** maksimal **3 arah** ditawarkan dalam satu waktu + **1 rekomendasi dengan
  alasan** — bukan delapan pilihan yang membuat client bingung.

### 3. Format yang Boleh Dijanjikan (fase portofolio)

| Format | Status sekarang | Catatan |
|---|---|---|
| **Undangan web** (satu halaman gulir, responsif-adaptif) | **BOLEH dijanjikan** | selalu ditawarkan; format utama fase ini |
| **Flyer/poster statis** (portrait + landscape) | **BOLEH dijanjikan** | PDF/PNG statis; asetnya dua tingkat (layar & cetak) bila dipakai untuk cetak |
| **Video animasi** | **BELUM** | `08_PIPELINE_VIDEO.md` belum diisi (ditunda pemilik sampai ada demand) + lisensi Remotion belum diputuskan → catat **PERLU KEPUTUSAN PEMILIK** |
| **Cetak siap-cetak** (bleed/CMYK/PDF-X) | **BELUM** | `07_SPESIFIKASI_CETAK_PREPRESS.md` belum diisi → catat **PERLU KEPUTUSAN PEMILIK** |
| **Story WA / square** | **boleh sebagai turunan flyer** | potongan dari flyer; bukan format baru |

Yang **sudah dijanjikan di brief (bagian B.2 dokumen 04) tetapi ternyata belum tersedia** wajib
**diberitahukan** ke client sebelum G2 — format yang dijanjikan lalu hilang tanpa tercatat = cacat
serah terima (dokumen 04 §3).

### 4. Waktu, Revisi, dan Masa Aktif — kalimat yang boleh dipakai

- *"Undangan web selesai dalam **3 hari kerja** setelah data acaranya lengkap dan lolos pemeriksaan."*
- *"Sebelum terbit, revisi **tak terbatas** — kita rapikan sampai Anda puas."*
- *"Sesudah terbit, perubahan kecil (typo, jam, tempat, foto, susunan acara, dress code) **gratis**;
  perubahan besar (model/warna/struktur baru) berbeda urusan."* (L1 §8; field yang bisa diubah sesudah
  terbit ada di `03_TEMPLATE_DATA_ACARA.md` §6)
- *"Tautan undangan **tetap sama** walau ada perubahan — teks WhatsApp untuk menyebar kita perbarui,
  jadi tamu tidak perlu tautan baru."*
- *"Masa aktif **1 tahun** sejak acara, perpanjangan **gratis**."*
- **Basis angka 3 hari kerja** (dinyatakan supaya tidak dikira karangan): praktik pasar Indonesia 2026 —
  penyedia template mengklaim <24 jam s/d 1–2 hari, penyedia custom 3–7 hari, dengan revisi tanpa batas
  dan masa aktif 1 tahun. 3 hari kerja = menjanjikan **lebih cepat dari custom pasar**, tanpa
  menjanjikan yang bisa gagal karena antrean. **Belum diukur di produksi nyata** → sesi pertama (uji
  coba internal) wajib mencatat waktu nyatanya, dan angka ini dikoreksi bila ternyata salah.

### 5. Ucapan & RSVP — Moderasi dan Data

| Hal | Default | Boleh diubah client? |
|---|---|---|
| Tampil ucapan/doa restu | **langsung tampil, tanpa moderasi** | ya — client boleh minta **moderasi** (disetujui dulu sebelum tampil) |
| RSVP (konfirmasi kehadiran) | **terbuka**, rekap diberikan ke client | ya — client boleh minta ditutup pada tanggal tertentu |
| Tempat penyimpanan data | **repo unit undangan itu** (Git = database; tanpa layanan pihak ketiga, tanpa biaya) | tidak (keputusan sistem) |
| Masa simpan | **selama masa aktif** (1 tahun + perpanjangan) + arsip di sisi studio | ya — client boleh minta **hapus data** kapan pun |
| Dibagikan ke pihak lain | **tidak pernah** | — |

Kalimat ke client (awam): *"ucapan & konfirmasi kehadiran tamu tersimpan di berkas undangan Anda
sendiri, tidak di layanan pihak lain; bisa saya hapuskan kapan pun Anda minta."*

### 6. Prompt Siap-Tempel untuk Sesi dengan Client

> Dipakai **per undangan**, sesudah brief Tahap 1–2 (dokumen 04) dan sesudah data acara lolos validasi
> (dokumen 03 §7). Isi kurung siku sebelum ditempel.

```
Peran kamu: Design Discovery Partner untuk SATU undangan. Yang kamu hadapi adalah CLIENT (orang yang
memesan undangan) — bisa langsung, bisa lewat pemilik sistem yang meneruskan jawabannya. Client TIDAK
punya basic desain dan TIDAK punya basic coding.

Aturan paling penting: JANGAN menyuruh client mengisi formulir teknis. Kamu yang bertanya dan
MENGUSULKAN; client tinggal memilih atau menolak. Setiap tawaran wajib kamu sebut AKIBAT VISUALNYA
dalam bahasa sehari-hari ("kalau ini dipilih, tamu akan lihat X waktu membuka undangan di HP"), bukan
istilah teknis.

Baca dulu (batas yang tidak boleh dilanggar):
- 01_IDENTITAS_PEMILIK.md — font & palet default, nada bahasa, batasan mutlak.
- 02_PROFIL_JENIS_ACARA.md — bagian jenis acara client ini: field default, kata baku, konvensi desain
  & 9 pantangan, fitur bawaan vs per-undangan.
- 03_TEMPLATE_DATA_ACARA.md + 04_TEMPLATE_BRIEF_UNDANGAN.md — data acara & bentuk brief.
- 05_DISCOVERY_DESAIN_PROMPT.md (dokumen ini) bagian 1–5 — BATAS JANJI, menu arah, batas format,
  waktu/revisi/masa aktif, dan aturan ucapan/RSVP. Bagian itu MENGIKAT: jangan berimprovisasi.

Keputusan pemilik yang TIDAK ditawar ulang ke client: desain responsif-adaptif di semua layar ·
infrastruktur nol biaya bulanan · amplop digital = rekening + QRIS statis tanpa payment gateway ·
teks dari font & ornament/logo wajib vektor (kalau client minta "tulisan nama dibuat jadi gambar",
tolak dengan penjelasan akibatnya: nama bisa pecah saat diperbesar dan tidak bisa diperbaiki setelah
undangan tersebar) · bahan milik pemilik di folder Input-Pengguna diperlakukan sebagai bahan; kalau
foldernya kosong, katakan kosong.

Bahan dari client:
"[TEMPEL DI SINI: data acara yang sudah terkumpul, permintaan client, referensi yang client kirim
(link/foto/contoh yang client suka), dan apa yang client bilang soal suasana]"

Jalannya diskusi:

1. Mulai dengan 3 pertanyaan pembuka yang MENGGALI RASA, bukan spesifikasi: undangan ini mau terasa
   seperti apa bagi tamu; ada tidak contoh yang client suka (dan APA yang disukai — warnanya?
   kesederhanaannya? fotonya?); ada tidak hal yang client pastikan TIDAK mau.

2. Tawarkan MAKSIMAL 3 arah desain dari menu dokumen ini bagian 2 (default: Luxury gold klasik ·
   Islami/Arab · Modern minimalis; Romantic floral & Nusantara elegan dibuka bila client menyebut
   bunga/pastel atau adat/daerah). Untuk tiap arah sebutkan: suasana, elemen, risiko. Beri SATU
   REKOMENDASI dengan alasan. Kalau client tidak punya keterangan apa pun, pakai katalog model L2
   sebagai fallback otomatis dan katakan itu pilihan awal yang gampang diubah.

3. Gali sampai jelas untuk undangan INI:
   - FORMAT: apa yang dilihat tamu pertama kali sebelum menggulir; urutan bagian (struktur bagian web
     sudah ada default di L2 §7 — yang digali di sini hanya perubahan/penambahan)
   - BAGIAN: dari daftar fitur per-undangan L2 §9 (musik, galeri/love story, amplop digital,
     countdown, QR check-in + layar sapa, dress code, live streaming, analitik) — mana yang dipakai,
     mana yang tidak, dan mana yang client minta tapi BELUM tersedia (video/cetak — jangan dijanjikan)
   - PALET & FONT: pakai default L1 atau menyimpang; kalau menyimpang, catat alasannya
   - FOTO & ASET: apa yang client punya, ukuran ASLINYA, dan akan dipakai SEBERAPA BESAR di layar;
     apa yang harus dibuat/dicari. Jangan menjanjikan lolos — pemeriksaannya ada di gerbang aset
   - APAKAH PERLU VERSI CETAK: kalau ya, sampaikan bahwa versi cetak belum tersedia sekarang
     (catat sebagai PERLU KEPUTUSAN PEMILIK), tetapi minta client menyimpan foto resolusi tinggi
   - MUSIK: dipakai atau tidak; kalau dipakai, wajib ada tombol mati, dan tanyakan eksplisit soal
     tamu yang membuka di tempat umum (kuota, baterai, rasa malu)
   - UCAPAN & RSVP: sesuai bagian 5 dokumen ini — tanyakan hanya apakah client mau moderasi
   - REVISI SESUDAH TAYANG: sampaikan yang bisa diubah sendiri vs yang lewat studio (L1 §8 + skema 03),
     dan kalimat "tautan tetap sama"
   - HAL PANTANG untuk acara ini, termasuk yang khusus keluarga (bukan hanya 9 pantangan umum L2)

4. Setiap beberapa putaran, kasih ringkasan checkpoint: "Sejauh ini undangan ini kelihatannya: ..." dan
   minta client mengiyakan. Jangan lanjut sebelum diiyakan.

5. JANGAN menjanjikan hal di luar bagian 1 dokumen ini (harga final, tenggat khusus, jumlah revisi
   khusus, siapa yang menanggung domain sendiri, video, cetak). Catat sebagai "PERLU KEPUTUSAN PEMILIK"
   dan teruskan — jangan menebak.

6. JANGAN tulis spec/brief final sebelum client (atau pemilik yang mewakilinya) bilang "cukup, tulis".

Setelah client bilang cukup: rangkum mengikuti struktur 04_TEMPLATE_BRIEF_UNDANGAN.md, lengkapi bagian
desain & format (arah yang dipilih, palet/font, daftar bagian, daftar format target, catatan aset &
ukuran foto, permintaan khusus, hal pantang), tulis bagian "PERLU KEPUTUSAN PEMILIK" secara eksplisit,
simpan di folder UNIT undangan ini, catat keputusannya di Log Keputusan unit, dan ajukan ke pemilik
untuk review G2 sebelum lanjut ke Tahap 4.
```

### 7. Hasil Tahap 3 dan Jalur ke G2

1. **Tempat hasil:** folder **unit undangan** (satu undangan = satu unit kerja, `04_TEMPLATE_BRIEF_UNDANGAN.md` §8) — **bukan** di folder sistem. Yang disimpan: brief terisi + **spesifikasi desain** (arah, palet/font, urutan bagian, daftar format target, daftar aset & ukuran pemakaian) + Log Keputusan unit.
2. **Penyimpangan wajib tercatat:** penyimpangan dari palet/font L1 · model di luar katalog · pantangan L2 yang dilanggar atas permintaan client · tenggat di bawah siklus.
3. **Gerbang G2 (Besar):** review isi **oleh pemilik** — yang dikunci: template/gaya, font, palet, dan **daftar format yang dijanjikan**. Sesudah G2, perubahan format = perubahan besar (tercatat + approval ulang).
4. **Urutan yang tidak boleh dibalik:** data acara lolos validasi (dokumen 03 §7) **sebelum** Tahap 3; aset diperiksa **sebelum** dijanjikan ke client (§8).

### 8. Kalau Dokumen 06 dan 10 Belum Terisi

- **Dokumen 06 (spesifikasi aset + gerbang G3) belum terisi** saat dokumen ini ditulis (ia dokumen berikutnya di roadmap). Selama belum terisi: **jangan menjanjikan nasib sebuah aset** ke client — yang boleh dikatakan hanya *"fotonya saya periksa dulu; kalau kurang tajam untuk ukuran pemakaiannya, saya kabari pilihan yang aman"*. Ambang angkanya ada di `00_RENCANA_KERANGKA.md` bagian 4.3–4.5 (dua tingkat aset, kebijakan fail-closed, ambang diperketat dari hasil uji).
- **Dokumen 10 (arsitektur website induk) ditunda** oleh pemilik sampai ada demand. Yang sudah pasti dan boleh dipakai: undangan terbit di **satu domain studio, undangan = subpath**, hosting Cloudflare Pages free tier, deploy via Git. Yang **belum** diputuskan (mis. bentuk antrean publish, batas plafon saat banyak undangan) **dinyatakan terbuka** di dokumen 09 — bukan dikarang di sini.

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-21 | **Dokumen diisi — ROADMAP b2, Discovery 05 (desain & format)**: prompt client-facing + batas janji + menu arah + jalur G2; banner kerangka dicabut; `_sistem/validate_system.py` diperluas (7 kerangka → **6 kerangka + 5 terisi**; diuji mutasi); manifest v0.6.0→**v0.7.0**; `STATUS.md` diperbarui — **satu commit** | ROADMAP JALAN PRODUKSI PERTAMA butir b2 (disetujui pemilik, log sesi slot 43/44) + pola *delegasi + paket keputusan*. Paket **B1–B6** diajukan agent (riset + pembacaan L1/L2/03/04/00/README) dan **disetujui pemilik seluruhnya** (*"Setuju semua (B1–B6)"*, log sesi slot 45). Review isi = PR normal tanpa auto-merge |
| 2026-09-21 | **B1** — bentuk dokumen: prompt final + **tabel batas janji** + aturan penyimpanan hasil & jalur G2 (bukan sekadar memindahkan draf staging) | Agent; disetujui pemilik. Alasan: satu-satunya prompt yang menghadap client harus punya pagar janji, supaya agent tidak mengarang di depan client |
| 2026-09-21 | **B2** — menu arah desain: **3 default** (Luxury gold klasik · Islami/Arab · Modern minimalis) + **2 sesuai permintaan** (Romantic floral · Nusantara elegan); katalog 8 model L2 **tetap** berlaku sebagai fallback otomatis | Agent; disetujui pemilik. Basis: 17 referensi pilihan pemilik (Discovery 01) + L2 §6. **Bukan aturan kaku** — model di luar menu tetap dilayani |
| 2026-09-21 | **B3** — batas format fase portofolio: **web (selalu) + flyer/poster statis boleh**; **video & cetak belum** (catat PERLU KEPUTUSAN PEMILIK) | Agent; disetujui pemilik. Alasan: dokumen 07 & 08 ditunda pemilik sampai ada demand — menjanjikan format yang dokumennya belum ada = janji yang tidak bisa dipenuhi |
| 2026-09-21 | **B4** — janji waktu: **3 hari kerja** untuk web (sejak data lolos G1) + **revisi tak terbatas sebelum terbit** + jalur cepat; **wajib diukur di produksi nyata pertama** dan dikoreksi bila meleset | Agent; disetujui pemilik. Basis riset pasar 21 Sep 2026 (wekita.id <24 jam · undweb.id template 1–2 hari / custom 3–7 hari · helloguest.id standar 2×24 jam, revisi maks 1×24 jam · ringvitation.com 1 jam) — sumber disebut supaya angkanya tidak dikira karangan |
| 2026-09-21 | **B5** — ucapan & RSVP: default **tanpa moderasi**, moderasi sesuai permintaan; data di **repo unit** (Git = database), arsip selama masa aktif, client boleh minta hapus, tidak dibagikan ke pihak lain | Agent; disetujui pemilik. Alasan: tidak menambah layanan pihak ketiga (infrastruktur nol biaya) dan tidak menahan data tamu lebih lama dari kebutuhannya |
| 2026-09-21 | **B6 — konflik urutan dilaporkan: `_sistem/README.md` mewajibkan 06 → 10 → 09 sedangkan ROADMAP menaruh 05 → 06 → 09 dan menunda 10.** Penyelesaian: dokumen **09 ditulis dengan mengutip keputusan 00 yang sudah dikunci** (satu domain + subpath + Cloudflare Pages + deploy via Git) dan **bagian yang benar-benar butuh dokumen 10 dinyatakan terbuka**; **10 tetap ditunda** sampai ada demand | Ditemukan agent 21 Sep 2026 saat membaca README; **dilaporkan, tidak ditebak** (norma repo: konflik dilaporkan). Disetujui pemilik sebagai bagian paket B1–B6. Risiko yang diterima: bagian 09 yang bergantung arsitektur induk bisa perlu ditinjau ulang kalau dokumen 10 nanti mengubah keputusan — risiko dibatasi karena 00 sudah mengunci keputusan besarnya |
