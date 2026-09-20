# Profil Jenis Acara

> **STATUS: ISI — DRAFT G1.** Diisi 2026-09-20 lewat **Discovery 02** (prompt `_sistem/PROMPT_DISCOVERY_02_PROFIL_JENIS_ACARA.md`;
> sesi `_log-sesi/LOG_SESI_2026-09-20_43.md`). Jenis acara pertama: **PERNIKAHAN** (cakupan umum — keputusan pemilik).
> Gerbang **G1**: prompt Discovery 02 menetapkan pengisian ini kategori **BESAR** — dokumen ini dinyatakan lulus **hanya oleh
> pemilik** lewat review isi lengkap pada PR-nya, tanpa auto-merge. **BENTURAN DOKUMEN DILAPORKAN TERBUKA, tidak diputuskan
> diam-diam:** manifest sistem mencantumkan G1 sebagai approval *Kecil* (boleh diwakilkan agent) dan `00_RENCANA_KERANGKA.md`
> bagian 4 memakai G1 sebagai gerbang *produksi* per-undangan (data acara, risiko *Sedang*) — dua-duanya lebih longgar dari
> prompt 02. Jalur yang dijalankan = yang paling ketat (review isi lengkap pemilik); klasifikasi di dokumen lain TIDAK diubah
> sepihak, pemilik yang memutuskan saat review. Banner kerangka dicabut di commit yang sama dengan perluasan validator
> (aturan mekanika T-69/prompt 02).

| | |
|---|---|
| **Berkas** | `02_PROFIL_JENIS_ACARA.md` |
| **Lapis** | L2 — Profil Jenis Acara |
| **Cara diisi** | **YA — perlu prompt Discovery detail** (`_sistem/PROMPT_DISCOVERY_02_PROFIL_JENIS_ACARA.md`) — **sudah dijalankan 2026-09-20** untuk jenis acara pertama (pernikahan); diulang per jenis acara berikutnya |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (rencana induk) + jawaban & approval per butir pemilik di Discovery 02 (log sesi 2026-09-20_43) + riset terukur sesi itu (kata baku/etika/siklus/pantangan — sumber per bagian di bawah) + baseline pasar 6–7 penyedia Indonesia (DISKUSI_MENTAH bagian A, 17 Sep 2026 — dipakai, tidak diriset ulang) |

## Fungsi dokumen ini

Isi Lapis 2 **per jenis acara** (pernikahan, khitanan, webinar, ulang tahun, dsb.): **daftar field info acara default** (boleh kurang/lebih — **adaptif, tidak kaku**), konvensi desain & etika tiap jenis acara, dan **kata baku** (mis. "akad" vs "pemberkatan").

## Catatan untuk yang mengisinya nanti

Gerbang **G1**. Riset baseline 7 situs pasar undangan Indonesia sudah tersimpan di DISKUSI_MENTAH bagian A — **jangan riset ulang dari nol**.

## Isi

> **Cara membaca dokumen ini (semantik L2 — mengikat semua bagian di bawah):** semua isi di sini adalah **DEFAULT per jenis
> acara**, bukan aturan kaku — L3 (undangan konkret) **boleh kurang atau lebih**; yang kurang **dinyatakan sadar**, tidak
> diisi nilai karangan (aturan Tahap 2 `00_RENCANA_KERANGKA.md`). Koreksi pemilik 20 Sep 2026 (near-verbatim, untuk katalog
> model dan diberlakukan umum ke seluruh dokumen ini — dinyatakan sadar, pemilik boleh menolak saat review): *"itu bukan
> sebagai aturan kaku, melainkan sekedar pilihan otomatis ketika ga ada keterangan detail"*. Keinginan client selalu menang
> (Prinsip Kerja Dasar L1); L2 hanya berlaku saat client tidak memberi keterangan. Benturan dengan L1 (font, palet, nada,
> batasan mutlak) **wajib dilaporkan, tidak diputuskan diam-diam**.
>
> Jenis acara berikutnya **DITAMBAHKAN** sebagai bagian sendiri di bawah ini (prompt 02 diulang per jenis — jangan dicampur,
> jangan menimpa bagian yang sudah ada).

### Jenis Acara 1: PERNIKAHAN

#### 1. Cakupan dan Prinsip Umum

- **Cakupan: UMUM** — semua bentuk pengesahan (Islami, Kristen Protestan, Katolik, sipil, adat, campuran) dan **semua variasi
  dicakup sejak awal** (keputusan pemilik: *"semu variasi itu dicakup sejak awal, karena memang semuanya mungkin terjadi"*).
- Struktur profil: **default umum + matriks variasi** (bagian 4) — bukan satu cetakan tunggal.
- Variasi yang benar-benar langka = **kerja custom per client** — sah per prinsip adaptif, bukan kegagalan profil (catatan
  riset L1: katalog undangan khas Aceh & Sunda tidak ditemukan di pencarian umum → peluang diferensiasi).
- Warisan L1 yang tidak ditawar di L2: palet default ivory/krem + hitam/abu gelap + aksen emas; font Playfair Display
  (judul) + Montserrat (isi) + Amiri (Arab/Islami); nada elegan-khidmat-baku; pembuka Islami **hanya** untuk acara Islami;
  batasan mutlak; credit Lee-Studio (default tampil kecil, paket premium dihapus).

#### 2. Bentuk Pengesahan dan Kata Baku

Salah pilih kata di undangan = menyinggung keluarga dan tidak bisa diperbaiki setelah undangan tersebar (prompt 02). Tabel
ini **kata baku default**; preferensi keluarga selalu menang (dikonfirmasi — bagian 3).

| Bentuk | Nama acara yang ditulis di undangan | Keterangan |
|---|---|---|
| Islami | **Akad Nikah** | "Ijab kabul" = ucapan inti **di dalam** akad (ijab oleh wali, kabul oleh mempelai pria) — **bukan** nama acara (liputan6.com/feeds/read/5771933; swanvara.com/blog/perbedaan-akad-dan-resepsi) |
| Islami (perayaan) | **Resepsi Pernikahan** — opsi **Walimatul Ursy** | Keputusan pemilik: default "Resepsi Pernikahan" (lebih umum dikenal), "Walimatul Ursy" (istilah syar'i jamuan syukur — liputan6.com/islami/read/6099259) **ditawarkan sebagai opsi**, bukan dipaksa |
| Kristen Protestan | **Pemberkatan** | Prosesi pengesahan di gereja — padanan akad (swanvara.com; kampungkb.kemendukbangga.go.id) |
| Katolik | **Holy Matrimony** / **Pemberkatan** | mengikuti istilah gereja setempat — konfirmasi keluarga |
| Sipil / beda agama | **Pencatatan Sipil** | sering dipilih pasangan beda agama |
| Adat | **nama prosesi adat setempat** | dari client/keluarga — tidak dipatok studio |

**Varian antar-mazhab/denominasi — aturan eksplisit prompt 02: JANGAN anggap satu rumusan cocok untuk semua.** Pendekatan
yang dikunci pemilik: **daftar kandidat kecil per agama + pilihan final per undangan + konfirmasi keluarga** untuk yang
sensitif. Kandidat pembuka (default L2, pilihan per undangan):

- Islami: Bismillah + ayat — kandidat umum **QS Ar-Rum 21**; frasa waktu lazim *"yang Insya Allah dilaksanakan pada…"*
  (pola contoh undangan — rabiyuk.com).
- Kristen/Katolik: ayat — kandidat **1 Korintus 13** atau **Markus 10:6-9**; ikuti tradisi gereja setempat.
- Sipil/umum: kalimat netral elegan (kunci L1: acara non-Islami tidak dipaksa pembuka religius).

#### 3. Etika Penulisan dan Titik Sensitif

**Pola tuan rumah (siapa yang mengundang) — dua pola baku:**

1. **Pola orang tua (paling umum):** nama kedua mempelai di atas + daftar **"Turut Mengundang"**: orang tua mempelai **pria
   dahulu**, lalu orang tua mempelai wanita, lalu opsional saudara kandung, kakek/nenek, keluarga besar, instansi
   (rabiyuk.com; kitaberdua.wedding; acaranya.id; nicewedding.id). **Jujur — sumber berbeda:** wikiHow (id.wikihow.com/
   Menulis-Undangan-Pernikahan) menulis pihak **wanita** lebih dulu bila orang tua wanita tuan rumahnya; pasangan beda
   agama/suku lazim memakai **dua kolom setara** kiri-kanan (nicewedding.id). → Karena sumbernya berbeda dan isunya
   sensitif: **urutan SELALU dikonfirmasi ke client/keluarga per undangan** — default hanya titik mulai, bukan keputusan
   studio.
2. **Pola mempelai sendiri (modern/minimalis):** hanya nama kedua mempelai sebagai tuan rumah, tanpa daftar turut mengundang.

**Nama & gelar:** nama **lengkap** + gelar ditulis **utuh** (H., Hj., Dr., S.Pd, dst.) — tidak disingkat tanpa persetujuan
keluarga (rabiyuk.com).

**Kasus sensitif — format bakunya ada, tetapi WAJIB konfirmasi keluarga, TIDAK PERNAH diasumsikan** (nicewedding.id):

- Orang tua **bercerai** → nama ditulis **baris terpisah tanpa "&"**.
- Orang tua **meninggal** → wali ditulis *"(selaku Wali Nikah)"*, atau penulisan alm./almh. — sesuai keinginan keluarga.
- **Beda agama/suku** → dua kolom setara; istilah acara mengikuti bentuk yang dipilih pasangan (bagian 2).

**Sapaan tamu:** default L1 *"Kepada Yth. Bapak/Ibu/Saudara/i"* + **personalisasi nama tamu** per tautan (fitur bawaan —
bagian 9). Variasi hangat = permintaan client.

**Bahasa & nada:** Indonesia baku, elegan, khidmat (L1); client selalu boleh menyesuaikan.

#### 4. Matriks Variasi

Semua kombinasi di bawah mungkin terjadi (keputusan pemilik) — undangan konkret memilih titik di matriks ini saat brief
(Tahap 1–2):

| Sumbu | Nilai yang dicakup | Konsekuensi |
|---|---|---|
| **1. Bentuk pengesahan** | Islami · Protestan · Katolik · sipil · adat · campuran | kata baku (bagian 2), pembuka, etika |
| **2. Jumlah acara/waktu/lokasi** | satu acara · akad+pemberkatan & resepsi satu hari satu lokasi · satu hari dua lokasi · dua hari/lebih | undangan **wajib menulis tanggal+jam+tempat PER acara** agar tamu tidak salah datang (swanvara.com); field acara = daftar, bukan tunggal |
| **3. Skala tamu** | intimate (≤50) · menengah · besar (500+) | acara besar → QR check-in + layar sapa relevan (opsional, bagian 9) |
| **4. Adat (lapis opsional)** | Jawa · Sunda · Aceh · Minang · Batak · dst. | detail adat **selalu dari client/keluarga**; katalog studio belum ada untuk Aceh & Sunda (riset L1) → jalur custom = peluang diferensiasi |

#### 5. Daftar Field Default

Prinsip: **adaptif, tidak kaku** — boleh kurang boleh lebih; yang kurang dinyatakan sadar (Tahap 2 kerangka); skema teknis
dan aturan satu-sumber ditegakkan di `03_TEMPLATE_DATA_ACARA.md` (L3).

**WAJIB (7) — tanpa ini undangan tidak terbit; diverifikasi di gerbang data:**

1. Nama lengkap + nama panggilan kedua mempelai.
2. Pola tuan rumah: nama + gelar kedua orang tua (dan daftar "turut mengundang" bila dipakai) ATAU pola mempelai sendiri — termasuk konfirmasi eksplisit titik sensitif (urutan, gelar, alm./wali, cerai).
3. Bentuk acara (akad/pemberkatan/holy matrimony/sipil/adat, dengan/tanpa resepsi; istilah resepsi terpilih).
4. Hari + tanggal (+ tahun) **per acara**.
5. Jam mulai (+ selesai) **per acara**.
6. Tempat: nama venue + alamat lengkap + tautan/koordinat peta **per acara**.
7. **Zona waktu** (WIB/WITA/WIT) — selalu ditulis (hal konsisten, bagian 7).

**OPSIONAL (14) — ditanya saat brief, tidak dipaksa:**

tanggal Hijriah (bentuk Islami) · susunan/rundown acara · dress code · batas waktu RSVP + kontak · amplop digital
(rekening/QRIS **client** — default tanpa nominal, L1) · galeri foto/love story · musik latar (dengan tombol off) ·
countdown (default target: mulai acara inti) · tautan live streaming · hashtag acara · QR check-in + layar sapa · info
parkir/akomodasi (tamu luar kota/destinasi) · format tambahan (video/cetak/story WA — format L1) · catatan khusus keluarga.

**TIDAK BERLAKU (otomatis per bentuk — bukan pilihan):** pembuka/istilah Islami untuk acara non-Islami dan sebaliknya
(kunci L1) · display mahar (tidak baku; permintaan = custom).

#### 6. Konvensi Desain dan Pantangan

**Suasana:** akad/pemberkatan = **khidmat & tenang** (sakral, tamu terbatas — swanvara.com); resepsi = **hangat & meriah
tetapi bermartabat**. Payung semuanya = disiplin premium L1: **maks 2 font, maks 3 warna, whitespace lega, footer
konsisten, transisi 0,3–0,5 detik** (video) — ditegakkan di gerbang G2/G3 produksi.

**Elemen yang lazim:** floral lembut (mawar, **melati** — identik pernikahan Jawa/Sunda), garis emas tipis, bingkai/lengkung
klasik, ornamen sesuai bentuk (arabesque/geometris Islami; motif daerah dalam bentuk elegan), inisial/nama mempelai besar
(Playfair Display), cincin/merpati opsional. **Tanpa foto = sah** → desain ornament-driven (lazim di sebagian keluarga
Islami).

**PANTANGAN / hati-hati (9 butir):**

1. **Font sambung/dekoratif untuk daftar nama** — nama & gelar = konten paling sensitif, wajib terbaca jelas (nicewedding.id).
2. **Latar hitam dominan** — asosiasi duka di sebagian tradisi (liputan6.com/regional/read/5573170) → tier *konfirmasi client*; hitam sebagai teks/aksen di atas ivory tetap aman (palet L1).
3. **Sesak / warna lebih dari 3** — melanggar disiplin premium L1.
4. **Watermark/merek orang lain** — batasan mutlak L1.
5. **Foto resolusi rendah** — ditolak gerbang aset G3 (fail-closed; `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md`).
6. **Khusus format cetak:** font dekoratif hairline bisa hilang di offset/foil, wajib bleed 3 mm, hitam rich-black bukan K:100 (uprint.id — wilayah `07_SPESIFIKASI_CETAK_PREPRESS.md`, risetnya sudah ada; L2 hanya menandai).
7. **Musik autoplay tanpa tombol off** — mengganggu tamu.
8. **Humor/meme kasual di bagian sakral** — hanya atas permintaan eksplisit client.
9. **Konten tak selaras kekhidmatan untuk bentuk Islami** (mis. foto terlalu kasual) — konfirmasi keluarga.

**Katalog model awal (8) — status: PILIHAN OTOMATIS (fallback) ketika client tidak memberi keterangan detail; BUKAN aturan
kaku (koreksi pemilik 20 Sep 2026).** Pemilihan model per undangan terjadi di Tahap 3 bersama client
(`05_DISCOVERY_DESAIN_PROMPT.md`); L2 menyimpan konvensinya agar L3 tidak mulai dari nol. Font khusus per model **sah** —
L1 mendelegasikannya ("font khusus per model = L2/L3") dengan aturan lisensi L1 (peringatan, bukan block; OFL disarankan).

| Model | Palet | Tipografi & ornamen |
|---|---|---|
| Islami/Arab | krem + emas | kaligrafi Amiri, arabesque/geometris, lengkung mihrab |
| Luxury gold | ivory/hitam/emas | Playfair Display, garis & bingkai tipis klasik |
| Modern minimalis | netral + 1 aksen | Montserrat dominan, whitespace, nyaris tanpa ornamen |
| Romantic floral | pastel/ivory | Playfair + floral lembut |
| Jawa tradisional elegan | coklat sogan/krem/emas | motif batik (parang, truntum) bentuk elegan |
| Aceh/Minang/Nusantara | maroon/earthy/emas | motif meukeutop/songket bentuk elegan |
| Korean/pastel | pastel lembut | bersih, foto-driven |
| Animasi/video | mengikuti model induk | transisi 0,3–0,5 dtk (disiplin L1) |

Model di luar katalog = dilayani (keinginan client menang); katalog Aceh & Sunda yang lebih dalam = jalur custom (riset L1:
belum ditemukan di pencarian umum).

#### 7. Hal yang Selalu Konsisten (tidak ditanya ulang ke client)

1. **Struktur bagian undangan web:** pembuka → mempelai (+tuan rumah/orang tua) → info acara **per acara** (tanggal/jam/tempat) → susunan acara → peta → *[fitur opsional]* → ucapan & RSVP → penutup + credit.
2. Kata baku mengikuti tabel bagian 2 (istilah per bentuk tidak ditawar ulang — kecuali preferensi keluarga, yang dikonfirmasi).
3. Sapaan tamu default L1 + personalisasi nama tamu per tautan.
4. **Zona waktu selalu ditulis.**
5. **Satu sumber data** — nama/tanggal/jam/tempat mengalir dari satu skema ke semua format (web/video/flyer/cetak); tidak boleh ada salinan nilai yang bisa berbeda (`03_TEMPLATE_DATA_ACARA.md`).
6. Disiplin desain premium L1 (2 font/3 warna/whitespace/transisi) — ditegakkan G2/G3.
7. Credit Lee-Studio sesuai paket (L1: default tampil kecil & elegan, warna undangan, ≤10–15% bidang; premium dihapus).
8. Alur revisi & serah terima L1 (revisi tak terbatas sebelum terbit; 5 item serah terima; arsip studio gratis).
9. **Item sensitif SELALU dikonfirmasi** (urutan keluarga, gelar, alm./wali, cerai, beda agama) — yang konsisten adalah *prosedur konfirmasinya*, bukan isinya.

#### 8. Waktu dan Siklus

Riset siklus (nicewedding.id/sebar-undangan-h-berapa; rindangcatering.id; invidoto.com; lemon8):

- **Client biasanya order:** undangan umumnya mulai disiapkan **±3 bulan sebelum hari-H** (timeline pasar: pesan
  undangan/souvenir H-3 bulan); **jalur cepat mungkin** karena produksi digital lincah.
- **Sebar undangan:** digital ideal **H-30 s.d. H-14**; cetak **H-45 s.d. H-30**; tamu luar kota/destinasi **H-60 s.d.
  H-45**; **reminder H-7 s.d. H-1** — kekuatan digital: reminder cukup kirim ulang tautan.
- **Perubahan sesudah tayang (spesifikasi untuk G5 / `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md`):** field yang **wajib bisa
  diubah setelah terbit**: jam, tempat/gedung, koordinat peta, foto, susunan acara, dress code — plus **mekanisme sebar
  ulang** (tautan tetap sama — syarat path stabil kebijakan domain 3 fase; teks WA diperbarui). Perubahan **nama/gelar** =
  sensitif: bisa, lewat konfirmasi.
- **Revisi tak terbatas sebelum terbit** (nilai jual L1 terhadap harga pasar Rp 50–500rb).

#### 9. Fitur: Bawaan L2 vs Per-Undangan

Sumber: baseline fitur 6–7 penyedia pasar Indonesia (DISKUSI_MENTAH bagian A, 17 Sep 2026 — dipakai, tidak diriset ulang);
pembagian disetujui pemilik 20 Sep 2026.

**BAWAAN L2 (selalu ada di setiap undangan pernikahan — tidak perlu diminta):**

1. Data kedua mempelai (nama panggilan besar + nama lengkap) + orang tua/tuan rumah.
2. Tanggal + jam + zona waktu **per acara**.
3. Tempat + alamat lengkap + tautan Google Maps **per acara**.
4. Susunan acara sederhana.
5. Pembuka sesuai bentuk (bagian 2).
6. Sapaan + personalisasi nama tamu.
7. Ucapan & doa restu (buku tamu publik).
8. RSVP (+ rekap untuk client).
9. Teks WA siap salin + QR untuk sebar (serah terima L1).
10. Kalimat penutup/terima kasih.
11. Credit Lee-Studio (L1; hilang di paket premium).

**PER-UNDANGAN (ditanya saat brief — daftar opsi, bukan paksaan):** musik latar (toggle) · galeri/love story · **amplop
digital** (aktif hanya bila client memberikan rekening/QRIS; default tanpa nominal — L1) · countdown · QR check-in + layar
sapa (acara besar) · dress code · tautan live streaming · format tambahan (video/cetak/story WA) · analitik kunjungan.

#### 10. Catatan untuk L3 (diparkir — TIDAK diputuskan di L2, aturan prompt 02 butir 4)

- Data satu undangan pernikahan nyata (nama/tanggal/tempat satu client) → unit L3 masing-masing; tidak pernah masuk dokumen ini.
- Kecepatan/mood transisi detail per model → L3 + `08_PIPELINE_VIDEO.md`.
- Detail prosesi adat per client → L3 (sumbu 4 matriks variasi).
- **Catatan bisnis (bukan isi L2 — direkam agar tidak hilang):** teman pemilik (konten kreator pernikahan & pengurus WO)
  **tidak membuat undangan** → jasa ini **melengkapi** mereka = **kanal referral**; order berpotensi datang *via* WO/reseller,
  yang bersinggungan dengan kebijakan credit L1 (premium = hapus) dan **website pengelola T-63** (register pekerjaan terbuka
  di area meta — provenance; status TERTAHAN, menunggu 4 keputusan: urutan, hosting, bentuk antrean). Pemilik bertanya di
  sesi ini apakah website pengelola + editor visual terhubung GitHub "sudah masuk" — **jawabannya: di luar cakupan L2**;
  rumahnya = **Discovery 10** (`10_ARSITEKTUR_WEBSITE_INDUK.md`) + T-63; kontribusi L2 untuk itu = spesifikasi **field yang
  wajib bisa diubah setelah tayang** (bagian 8) sebagai kebutuhan yang harus dipenuhi editor visual tersebut.

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-20 | **Dokumen diisi — jenis acara 1: PERNIKAHAN (cakupan umum)**; banner kerangka dicabut; `_sistem/validate_system.py` diperluas (10 kerangka → 9 kerangka + 2 terisi; bagian isi wajib 02 ditegakkan; diuji mutasi); manifest v0.3.0→**v0.4.0**; `STATUS.md` diperbarui — **satu commit** | Frasa pemicu prompt 02 dari pemilik (near-verbatim): *"Baik. Cukup, tulis draft nya."* + aturan mekanika penulisan prompt 02/T-69. G1 = review isi lengkap pemilik di PR, tanpa auto-merge |
| 2026-09-20 | **Cakupan pernikahan = UMUM** (Islami maupun bentuk lainnya) | Approval pemilik (near-verbatim): *"Ya, umum, mencakup yang islami maupun yang lain nya"* |
| 2026-09-20 | **Semua variasi dicakup sejak awal** → default adaptif + matriks variasi 4 sumbu | Approval pemilik (near-verbatim): *"Ya, sebaiknya semu variasi itu dicakup sejak awal, karena memang semuanya mungkin terjadi"* |
| 2026-09-20 | **Kata baku & etika penulisan** (bagian 2–3): nama acara per bentuk; dua pola tuan rumah; gelar utuh; titik sensitif selalu konfirmasi; urutan default pihak pria dulu sebagai pola terumum dengan laporan jujur bahwa sumber berbeda | Usulan agent dari riset (sumber tercatum per bagian); approval pemilik: *"Setuju"* |
| 2026-09-20 | **Waktu & siklus** (bagian 8): sebar digital H-30..H-14, cetak H-45..H-30, luar kota H-60..H-45, reminder H-7..H-1; field wajib-ubah-setelah-tayang | Pemilik: *"Aku juga kurang tau soal ini"* → agent eksplor+riset sesuai Prinsip Kerja Dasar L1; approval atas usulan: *"Setuju"* |
| 2026-09-20 | **Sortir fitur bawaan L2 (11) vs per-undangan (9)** (bagian 9) | Baseline pasar bagian A + usulan agent; approval pemilik: *"Setuju"* |
| 2026-09-20 | **Konvensi desain + 9 pantangan** (bagian 6) | Usulan agent (riset pantangan: nicewedding/liputan6/uprint); approval pemilik: *"Setuju"* |
| 2026-09-20 | **Katalog 8 model = PILIHAN OTOMATIS (fallback) saat tidak ada keterangan detail — BUKAN aturan kaku** | **Koreksi pemilik** (near-verbatim): *"Setuju, tapi itu bukan sebagai aturan kaku, melainkan sekedar pilihan otomatis ketika ga ada keterangan detail"* |
| 2026-09-20 | **Hal konsisten 9 butir** (bagian 7) | Usulan agent; approval pemilik: *"Setuju"* |
| 2026-09-20 | **Daftar field default: WAJIB 7 · OPSIONAL 14 · TIDAK BERLAKU per bentuk** (bagian 5) | Usulan agent; approval pemilik: *"Setuju"* |
| 2026-09-20 | **Terminologi resepsi Islami: default "Resepsi Pernikahan", opsi "Walimatul Ursy"** + pendekatan antar-mazhab/denominasi = daftar kandidat kecil + pilihan per undangan + konfirmasi keluarga | Usulan agent (aturan eksplisit prompt 02 "jangan anggap satu rumusan cocok untuk semua"); approval pemilik: *"Setuju"* |
| 2026-09-20 | **Semantik fallback digeneralisasi ke SELURUH isi dokumen** (bukan hanya katalog model) = **catatan agent, dinyatakan sadar** | Konsisten dengan semantik L2 prompt 02 ("L2 = DEFAULT; L3 boleh kurang/lebih") + Prinsip Kerja Dasar L1; pemilik belum mengoreksi — status: terbuka untuk ditolak saat review G1 |
| 2026-09-20 | **Benturan klasifikasi G1 dilaporkan, tidak diputuskan sepihak**: prompt 02 = BESAR (review isi penuh pemilik) vs manifest = approval Kecil vs `00_RENCANA_KERANGKA.md` bagian 4 = gerbang produksi per-undangan (Sedang) | Norma repo: konflik dilaporkan, bukan ditebak. Jalur paling ketat yang dijalankan; klasifikasi di dokumen lain tidak diubah — **keputusan di tangan pemilik saat review PR ini** |
