# Identitas Pemilik

> **STATUS: ISI — DRAFT G0.** Diisi 2026-09-20 lewat **Discovery 01** (prompt `_sistem/PROMPT_DISCOVERY_01_IDENTITAS_PEMILIK.md`;
> sesi `_log-sesi/LOG_SESI_2026-09-20_42.md`, giliran 1–5). Gerbang **G0** = approval **Besar**: dokumen ini dinyatakan
> lulus **hanya oleh pemilik** lewat review isi lengkap pada PR-nya (Syarat 4 Standar Kelulusan Manual melarang penulis
> menilai sendiri). Banner kerangka dicabut di commit yang sama dengan perluasan validator (aturan T-69).

| | |
|---|---|
| **Berkas** | `01_IDENTITAS_PEMILIK.md` |
| **Lapis** | L1 — Identitas Pemilik |
| **Cara diisi** | **YA — prompt Discovery detail** (`_sistem/PROMPT_DISCOVERY_01_IDENTITAS_PEMILIK.md`) — **sudah dijalankan 2026-09-20** (5 giliran) |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (rencana induk) + jawaban & approval per butir dari pemilik di Discovery 01 (log sesi 2026-09-20_42) |

## Fungsi dokumen ini

Isi Lapis 1 yang **dikunci sekali dan diwarisi semua undangan**: merek/nama usaha pemilik, font & palet default,
gaya ornament bawaan, nada bahasa, kebijakan harga & masa aktif, data amplop digital (rekening + QRIS statis),
kebijakan serah terima, batasan mutlak, dan konsekuensi perubahan. **Perubahan di dokumen ini = risiko BESAR** →
kewajiban memeriksa ulang semua undangan yang **belum lewat G2** (bagian "Konsekuensi Perubahan" di bawah).

> **Bagian tambahan — dinyatakan sesuai aturan prompt** ("jangan tambah/kurangi bagian tanpa bilang"):
> `Cakupan Usaha` (fakta baru dari pemilik, giliran 3), `Prinsip Kerja Dasar` (kandidat kunci giliran 1, dikonfirmasi
> giliran 2), `Catatan untuk L2/L3` (diwajibkan aturan prompt butir 4), dan `Belum Ditentukan` (item **data** — bukan
> keputusan — yang sengaja tidak dikunci di G0).

## Cakupan Usaha

- Bukan hanya pernikahan: **semua jenis undangan acara + flyer** — pernikahan, acara keagamaan (maulid, majelis, dst),
  acara sosial, acara profesional/bisnis. Kata pemilik (giliran 3, near-verbatim): *"Sistem ini bukan cuma buat
  undangan wedding. Ini juga buat undangan lain lain nya. Bahkan juga buat bikin flyer acara macam macam."*
- Format keluaran: **web multi-halaman, video animasi, flyer/poster statis** (portrait untuk cetak/IG + landscape
  untuk broadcast), story WA, square.
- Bukti arah dari pemilik: 2 flyer maulid Al-Bahjah Cirebon (terlampir di chat giliran 3; isi + provenance dicatat di
  log sesi; file aslinya tidak persist di workspace — bila perlu diarsip, pemilik lampirkan ulang).
- Profil per jenis acara (termasuk **acara keagamaan**) = tugas **L2** (`02_PROFIL_JENIS_ACARA.md`), bukan dokumen ini.

## Prinsip Kerja Dasar (dikunci — konfirmasi pemilik giliran 2: "Ya, benar")

- **Default = sesuai keinginan client.** Agent **hanya** mengeksplor sendiri **kalau client bilang "terserah"**;
  dasar eksplorasi: daerah asal pengantin, jabatan/posisi, konteks acara — riset internet bila perlu.
- Prinsip ini yang membuat palet/font L1 di bawah berfungsi sebagai **jaring pengaman**, bukan paksaan.

## Isi

### 1. Merek / Nama

- **Nama penerbit: `Lee-Studio`** (approval pemilik giliran 2: *"Setuju 'Lee-Studio'"*).
  Kandidat awal "Lee-Productions" digugurkan atas rekomendasi agent: "studio" = identitas kreatif multi-format
  (web + video + cetak/flyer), "productions" terdengar agensi video; lebih pendek = mudah disebut di WhatsApp dan
  lebih pendek untuk domain fase 2 (satu domain, undangan = subpath — kebijakan domain 3 fase di `00_RENCANA_KERANGKA.md`).
- **Tagline: TIDAK ADA** (default agent — tidak pernah diganggu pemilik; credit cukup nama. Perubahan = perubahan L1, minor).
- **Penulisan:** `Lee-Studio` (capital L, capital S, tanda hubung) — konsisten di semua keluaran.
- **Tampil (credit) — dikunci giliran 2 (pemilik: *"Klo memang itu yang terbaik, aku Setuju"*):**
  - **Default: credit KECIL & ELEGAN di halaman akhir / footer** — satu baris "Lee-Studio", **menggunakan warna
    undangan itu sendiri** (bukan warna brand), lebar **≤10–15%** bidang, tipis. Paket dasar **tetap bagus** dengan
    credit (syarat eksplisit pemilik: *"kalopun client ga mau bayar lebih, hasilnya tetep bagus"*).
  - **Paket premium: credit dihapus** — ide paket harga pemilik, terdukung riset giliran 1 (diizinkan pemilik):
    "tanpa nama vendor" di pasar adalah fitur **premium**; credit kecil di footer adalah praktik standar komunitas
    desain web yang dilaporkan **membawa klien baru** (detail + sumber di log sesi).
  - Penempatan per format: web = baris terakhir halaman akhir · video = frame terakhir (±2 dtk) · flyer/poster =
    sudut (dua penempatan format terakhir = default agent, tidak pernah diganggu).
  - **Nama juga tampil di URL fase 1:** `lee-studio.pages.dev/<nama-undangan>` (konsekuensi kebijakan domain 3 fase).
- **Kontak studio untuk credit: BELUM DITENTUKAN** (WA/IG pemilik — diisi saat produksi nyata pertama; sampai saat itu
  credit cukup teks "Lee-Studio"). Lihat bagian *Belum Ditentukan*.
- **Cerita asal** (untuk materi profil studio, bukan untuk undangan): pemilik punya teman konten kreator bidang
  pernikahan & kekeluargaan dan teman yang mengurus WO → jasa ini lahir dari lingkaran tersebut (giliran 1).

### 2. Font Default

(Dikunci giliran 4 — delegasi pemilik: *"Terserah yang menurutmu terbaik dalam hal ini"*. Kandidat dinilai langsung
di galeri live bagian "Test Font", giliran 2.)

| Peran | Font | Lisensi | Catatan |
|---|---|---|---|
| **Judul** | **Playfair Display** | OFL (Google Fonts) — gratis komersial | Kontras tinggi; klasik untuk judul pernikahan & majelis |
| **Isi** | **Montserrat** | OFL (Google Fonts) — gratis komersial | Paling terbaca di ukuran kecil di HP |
| **Arab / acara Islami** | **Amiri** | OFL (Google Fonts) — gratis komersial | Naskh klasik; standar undangan Islam |

- **Mekanisme (ditanyakan & dipastikan ke pemilik, giliran 3):** undangan web memakai **web font** (woff2) — file
  font **ikut terkirim** dengan halaman undangan dan diunduh otomatis browser tamu; **tidak perlu terinstall** di HP
  tamu. Fallback hanya untuk kasus pinggir (offline / loading lambat): kandidat dipilih agar tetap rapi saat HP
  menggantikannya; subset (hanya karakter yang dipakai) → puluhan KB, bukan MB. Format **video/flyer**: teks
  ter-bake ke gambar/video → 100% tetap.
- **Aturan teknis (dari kerangka, bagian Langkah 0 G3):** teks wajib dari font; woff2 + subset; `display=swap`;
  fallback stack sistem untuk sesaat saat loading.
- Font khusus per model (mis. kaligrafi untuk model Arab) = **L2/L3** — bagian *Catatan untuk L2/L3*.
- Font milik pemilik di `Input-Pengguna/font/` (bila nanti dititipkan) diperlakukan sebagai **BAHAN**: lisensinya
  diperiksa & dilaporkan, bukan diam-diam dipakai (aturan prompt).

### 3. Palet Default

(Dikunci giliran 2 — *"Setuju klo memang itu yang terbaik"*.)

- **Default (jaring pengaman saat client tanpa preferensi): latar ivory/krem · teks hitam/abu gelap · aksen emas**
  — aturan pakai: latar = bidang utama, teks = isi, aksen = garis/ornament/judul.
- **Override: BOLEH per undangan dan per client — tanpa batas keras**: keinginan client selalu menang (Prinsip
  Kerja Dasar); palet L1 hanya berlaku saat client tidak punya preferensi. Konvensi palet per model (mis. Aceh →
  maroon/earthy; modern → netral + satu aksen) = **L2**.
- **Arah estetika default (dari 17 referensi yang dipilih pemilik, giliran 2):** **"elegan premium"** — gold/ivory/
  hitam + ornamen klasik (Arab, Jawa, Aceh), modern minimalis, floral lembut. Daftar lengkap + provenance tiap
  referensi: `Input-Pengguna/referensi/pilihan-arah-l1.md`. Batik bermotif kuat (Cirebon) & mega mendung **tidak
  dipilih** sebagai default — data, bukan larangan (tetap bisa dilayani per client).

### 4. Gaya Ornament Bawaan

- **Gaya: elegan premium** — ornament vektor klasik (arabesque/kaligrafi Arab, ornamen daerah dalam bentuk elegan —
  Aceh *meukeutop*, Jawa), floral lembut, garis tipis, **tidak sesak**.
- **Sumber ornament: dibuat/digenerate sendiri (SVG vektor) — Rp 0** (bagian dari kunci biaya produksi, bawah).
  Ornament dari luar wajib lewat aturan lisensi (bagian 10).
- Aturan G3 (kerangka bagian 4): ornament **wajib vektor** — resolusi/print ditangani gerbang.

### 5. Nada Bahasa

(Dikunci giliran 3 — konfirmasi pemilik giliran 4: *"a. Ya"*. Dasar: delegasi + batasan pemilik giliran 3:
*"default nya harus kata kata yang elegant dan penuh khidmat"*.)

- **Default: elegan, khidmat, bahasa Indonesia baku** — hangat tapi bermartabat.
- **Pembuka Islami (Bismillah + ayat/hadits): default HANYA untuk acara Islami** (pernikahan Islam, maulid, majelis,
  dst). Acara non-Islami (profesional/sipil/bisnis) mendapat pembuka sekuler yang tetap elegan — tidak dipaksa.
- **Sesuai keadaan (permintaan pemilik):** tiap jenis acara punya vokabulari sendiri (ditegaskan di L2):
  maulid → *"Hadir & Syiarkan"* + penghormatan kepada habaib/ulama · pernikahan → *"menghormat mengundang"* ·
  korporat → *"dengan hormat mengundang"*. **Client selalu boleh menyesuaikan.**
- Sapaan baku tamu default: *"Kepada Yth. Bapak/Ibu/Saudara/i"* (formal elegan; variasi hangat = L2/client).

### 6. Kebijakan Harga & Masa Aktif

- **Harga: BELUM DITENTUKAN — kebijakan fase portofolio** (dikunci giliran 4; pemilik: *"aku masih blm bisa nentuin
  denagn pasti. Karena aku blm tau nanti klien nya seperti apa"*; aturan prompt butir 6: pemilik belum bisa tentukan
  = wajib alternatif):
  1. **5 client nyata pertama ATAU 2 bulan** (mana yang dulu) = **fase portofolio** — harga fleksibel (boleh di
     bawah acuan, boleh gratis untuk client pertama demi portofolio).
  2. Setelahnya: **fix harga 3 paket** + update dokumen ini (tercatat di Log Keputusan). Struktur paket (bukan
     angka): **Basic** (web + credit studio) · **Premium** (web + video + flyer, **credit dihapus**) · **Luxury**
     (lengkap: buku tamu, maps, musik, countdown, dst).
  3. **Rentang acuan yang dicatat: Rp 50.000–500.000 sekali bayar** (baseline pasar 6–7 penyedia, DISKUSI_MENTAH
     bagian A — sumber, bukan riset ulang).
- **Masa aktif (bukan alat harga — usulan agent, tanpa keberatan pemilik):** default **1 tahun**; perpanjangan
  **gratis** (biaya nol, teknis tanpa batas); **tidak ada penonaktifan sepihak**.
- Pembayaran jasa studio = transfer bank ke rekening pemilik (QRIS studio opsional — nanti).

### 7. Amplop Digital

(Berlaku umum: rekening + **QRIS statis**, **TANPA payment gateway** — kunci pemilik Level-0, tidak ditawar ulang.
Detail teknis: `11_AMPLOP_DIGITAL.md`.)

- **Default: rekening + QRIS milik CLIENT** — diberikan client saat order (yang mengirim = tamu client). Pelurusan
  pemilik giliran 4: *"bukan nya qris dan rekening itu pake punya klien ya?"*
- **Versi percobaan/demo (undangan milik sendiri): rekening PEMILIK** (transfer biasa) — pemilik: *"klo untuk versi
  percobaan, gpp pake punya aku dulu"*; nomor diisi saat dibutuhkan (*Belum Ditentukan*).
- **QRIS milik pemilik: NANTI — bukan blocker.** Cara mendapatnya (bahasa awam): buka rekening bank (bisa rekening
  bisnis) → minta ke account officer atau pakai fitur "buat QRIS" di aplikasi m-banking — umumnya gratis, hitungan
  hari.
- **Nominal: default TANPA nominal** (default agent — sub-butir tidak dijawab pemilik); boleh ditampilkan per
  undangan bila client mau.
- **Pola acuan nyata:** footer 2 flyer maulid milik pemilik (giliran 3) memuat No. Rek + QRIS **INFAQ** → untuk
  acara keagamaan, peruntukan amplop = **infaq** (bukan "selamatan pernikahan").

### 8. Kebijakan Serah Terima

(Dikunci giliran 4 — *"b. ya"*. Gerbang teknisnya = G5 di `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md`; keputusan
lahir di sini sesuai aturan prompt.)

- **Yang diserahkan ke client (semua bisa diunduh dari HP client, tanpa langkah teknis):**
  (1) link undangan aktif (+ password bila client minta — **default: tanpa password**);
  (2) file video (jika format video dipilih);
  (3) flyer/poster statis (portrait + landscape bila dipakai);
  (4) gambar QR + **teks WA siap salin** untuk disebar ke tamu;
  (5) info rekening/QRIS (bila client menghimpun dana).
- **Kapan:** **setelah terbit** — client sudah menyetujui versi publikasi. Tahap Serah Terima **dipisahkan** dari
  Tahap Terbit (kunci Level-0; keduanya punya pemilik risiko berbeda).
- **Arsip:** disimpan di sisi studio — **bisa diminta ulang, gratis** (mengatasi risiko klasik serah terima:
  kehilangan akses — kerangka bagian 4).
- **Revisi:** **tak terbatas SEBELUM terbit** (nilai jual vs pasar baseline). Sesudah terbit: perubahan kecil
  (typo, waktu, tempat, foto) = **gratis**; perubahan besar (model/warna/struktur baru) = **bayar tambahan**.
- **Akun hosting:** undangan terbit di akun studio (Cloudflare Pages free tier — terukur 2026: request & bandwidth
  statis tanpa batas, tanpa biaya bulanan). Client menerima **link + arsip, bukan kepemilikan akun** — pemindahan
  kepemilikan akun adalah penyebab paling umum client kehilangan situsnya sendiri (alasan kerangka Level-0).

### 9. Skill / Plugin

- **0 skill terpasang** (kunci T-06: pemasangan selalu **per butir** + approval pemilik + provenance dulu).
- Discovery 01 memakai alat bawaan platform (web search + image search) — **bukan** skill repo.
- 10 ZIP skill di `Input-Pengguna/` (root repo) **masih menunggu cek pemilik** (*"Aku blm sempet cek"*) — item
  terbuka, bukan bagian pipeline produksi.

### 10. Batasan Mutlak

(Dikunci giliran 4 — *"b. ya, setuju"* + modifikasi lisensi oleh pemilik.)

Hal yang **tidak boleh** muncul di karya mana pun, untuk client mana pun:

1. **Info palsu / salah** — tanggal, waktu, tempat, nama, dan **nomor rekening wajib cross-check di G2/G5**
   (rekening salah = uang tamu masuk ke tempat yang salah — kesalahan termahal di sistem ini).
2. **Watermark / merek orang lain.**
3. **Konten yang melanggar kesusilaan / hukum.**
4. **Lisensi = PERINGATAN, BUKAN BLOCK** (modifikasi pemilik, giliran 4 — near-verbatim di log sesi):
   - Pemakaian aset eksternal **selalu boleh** — termasuk aset yang agent temukan dan anggap cocok untuk kerjaan.
   - Setiap aset dicatat **provenance + status lisensi** (sumber, tanggal, apa yang diketahui).
   - Status tidak jelas → **ingatkan pemilik sekali + catat** — pekerjaan **tidak dihentikan**.
   - **Keputusan pemilik MENUTUP** — termasuk *"aku sudah punya lisensinya"*: **tanpa perlu pembuktian, dan agent
     tidak menunjukkannya ke siapa pun** (yang dicatat hanya fakta keputusannya, tanpa detail — kerahasiaan dijaga;
     alasan pemilik: kadang sudah memegang lisensi tapi tidak ingin diketahui siapa pun).
   - **Daftar aset "terperingatkan" bisa dicek pemilik SATU KALI sebelum terbit** (penyempurnaan agent, diterima
     lewat *"silahkan"*).
   - Catatan batas: aturan ini memberi **checkpoint**, bukan **kekebalan** — kewajiban etis tetap pada pemilik
     sebagai pihak yang bertanggung jawab ke client.

### 11. Konsekuensi Perubahan L1

(Dikunci giliran 4 — *"c. Ya, boleh"* + modifikasi oleh pemilik.)

Perubahan di dokumen ini (nama, font, palet, nada, kebijakan) = **risiko BESAR**:

1. **Wajib (sistem):** **periksa ulang semua undangan yang BELUM lewat G2** — daftar undangan terdampak selalu
   ditunjukkan ke pemilik.
2. **Kontak ke client terdampak = KONFIRMASI PEMILIK, tidak otomatis** — **default: biarkan saja seperti
   sebelumnya** (undangan yang sudah dibangun tetap memakai identitas lama). Modifikasi pemilik (giliran 4):
   *"sangat mungkin aku ga mau ribet kontak sama klien nya dan mau biakan langsung seperti sebelumnya aja"*.
3. Setiap perubahan tercatat di **Log Keputusan dokumen ini + log sesi** (W-05).

## Catatan untuk L2/L3 (di-parkir sesuai aturan prompt butir 4 — bukan diputuskan di sini)

- **Font/palet per model desain** — intuisi pemilik (giliran 1) dibenarkan riset: model Arab → kaligrafi + krem/
  emas; Aceh → maroon/earthy; modern → netral + satu aksen. Diatur di `02_PROFIL_JENIS_ACARA.md` (L2).
- **Profil acara keagamaan (maulid/majelis)** — vokabulari *"Hadir & Syiarkan"*, hierarki pembicara (habaib/ulama
  + gelar), kotak narasi singkat, blok ikon tanggal/jam/lokasi, footer = sosmed penyelenggara + kontak + live
  streaming + QRIS INFAQ (pola dari 2 flyer lampiran pemilik).
- **Animasi/transisi** — referensi R33–R35 (thumbnail undangan animasi; statis di galeri) ditandai pemilik
  *"keliatan menarik"* → kecepatan/mood transisi per model = L3; pipeline video = `08_PIPELINE_VIDEO.md`
  (keputusan lisensi = item terbuka (e) di `STATUS.md`; data terukur 2026-09-20: Remotion free license ≤3 orang
  **membolehkan komersial** — verifikasi final saat build).
- **Model "khas daerah" lain** (Minang, Sunda, dst) — katalog per daerah = L2; catatan riset: katalog Aceh & Sunda
  belum ditemukan di pencarian umum (kemungkinan **kerja custom per client** = peluang diferensiasi).
- **Perluasan flyer ke format bisnis/profesional** — profil & contoh = L2/L3.

## Belum Ditentukan (data — bukan keputusan; sengaja tidak dikunci di G0)

| Item | Status | Kapan diisi |
|---|---|---|
| Nomor rekening pemilik (versi percobaan) | kosong | produksi demo pertama |
| QRIS pemilik | belum ada — bukan blocker | saat pemilik membuatnya (m-banking/account officer) |
| Kontak studio untuk credit (WA/IG) | kosong | produksi nyata pertama (credit cukup "Lee-Studio" sampai saat itu) |
| Angka harga 3 paket | fase portofolio berjalan | setelah 5 client / 2 bulan → update Log Keputusan dokumen ini |
| File asli 2 flyer maulid (arsip repo) | tidak persist di workspace | bila pemilik mau diarsip — lampirkan ulang (referensi arah, bukan aset produksi) |

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-20 | **Dokumen diisi** — banner kerangka dicabut; `_sistem/validate_system.py` diperluas (T-69a); manifest v0.2.0→**v0.3.0**, Tahap kerangka→**draft**, Status Proposed→**Draft** (T-69b); `STATUS.md` diperbarui (T-69c) — **satu commit** | Aturan T-69 (register DAFTAR_PEKERJAAN_TERBUKA.md di area _meta — provenance tanpa backtick agar folder ini tetap self-contained) + bagian "PENTING soal mekanika penulisan" prompt Discovery 01. Approval: pemilik *"Aku rasa cukup. Tapi ... klo kamu merasa masih ada yang kurang silahkan sampaikan. Klo memang udah cukup ya silahkan"* (giliran 5) |
| 2026-09-20 | **Scope = multi-acara + flyer** (bukan hanya wedding) | Fakta baru pemilik giliran 3 (near-verbatim) + 2 flyer maulid Al-Bahjah terlampir sebagai bukti arah |
| 2026-09-20 | **Nama = `Lee-Studio`; credit kecil & elegan by default (halaman akhir/footer, warna undangan, ≤10–15%); paket premium = hapus; tagline tidak ada** | Ide paket harga pemilik (giliran 1) + riset praktik pasar yang diizinkannya; approval giliran 2: *"Setuju 'Lee-Studio'"* + *"Klo memang itu yang terbaik, aku Setuju"* |
| 2026-09-20 | **Prinsip kerja dasar: default = keinginan client; "terserah" → agent eksplor** (daerah asal, jabatan, dst) | Kandidat kunci giliran 1; konfirmasi pemilik giliran 2: *"Ya, benar"* |
| 2026-09-20 | **Palet default ivory+hitam+emas; override per undangan BOLEH tanpa batas keras** | Delegasi + setuju bersyarat giliran 2: *"Setuju klo memang itu yang terbaik"*; arah dari 17 referensi pilihan pemilik (tercatat) |
| 2026-09-20 | **Font = Playfair Display (judul) + Montserrat (isi) + Amiri (Arab)** — OFL, woff2, fallback | Delegasi pemilik giliran 4: *"Terserah yang menurutmu terbaik dalam hal ini"* — alasan pemilihan di bagian Isi 2; teknis web font dikonfirmasi ke pemilik giliran 3 |
| 2026-09-20 | **Nada = elegan-khidmat-baku; pembuka Islami hanya untuk acara Islami; sesuai keadaan; client boleh sesuaikan** | Delegasi + batasan pemilik giliran 3: *"default nya harus kata kata yang elegant dan penuh khidmat"*; konfirmasi giliran 4: *"a. Ya"* |
| 2026-09-20 | **Amplop: default = rekening+QRIS client; versi percobaan = rekening pemilik; QRIS pemilik = nanti (bukan blocker); nominal = default tanpa** | Pelurusan pemilik giliran 4 (near-verbatim); QRIS statis tanpa payment gateway = kunci Level-0 |
| 2026-09-20 | **Serah terima: 5 item (link, video, flyer, QR+teks WA, rekening bila ada) + setelah terbit + arsip di studio gratis + revisi tak terbatas sebelum terbit / kecil-gratis, besar-tambahan sesudahnya** | Usulan agent giliran 3; approval pemilik giliran 4: *"b. ya"* |
| 2026-09-20 | **Harga: fase portofolio (5 client / 2 bulan) lalu fix 3 paket; rentang acuan 50–500 rb; masa aktif default 1 tahun + perpanjangan gratis, bukan alat harga** | Pemilik giliran 4: *"blm bisa nentuin ... blm tau nanti klien nya seperti apa"* → alternatif sesuai aturan prompt butir 6; approval: *"Setuju kebijakan yang kamu usulkan"* |
| 2026-09-20 | **Batasan mutlak (3 butir) + lisensi = PERINGATAN bukan BLOCK** (aset boleh dipakai; provenance+status dicatat; tidak jelas → ingatkan sekali; keputusan pemilik menutup, tanpa pembuktian, kerahasiaan dijaga; daftar terperingatkan bisa dicek sekali sebelum terbit) | Approval *"b. ya, setuju"* + modifikasi lisensi pemilik giliran 4 (near-verbatim di log sesi); opini agent diminta & dicatat |
| 2026-09-20 | **Konsekuensi perubahan L1: re-check semua undangan belum-G2 (wajib) + kontak client = konfirmasi pemilik (default: biarkan saja)** | Approval *"c. Ya, boleh"* + modifikasi giliran 4 (near-verbatim) |
| 2026-09-20 | **Biaya produksi per undangan = Rp 0; bulanan = Rp 0** — hosting statis free (Cloudflare Pages, terukur 2026), font OFL, ornament SVG buatan sendiri, foto & musik dari client, video via Remotion free (≤3 orang, komersial boleh — terukur 2026) | Jawaban atas pertanyaan pemilik *"kira2 bisa kan klo semua undangan ini kita produksi secara gratis tapi hasilnya tetap sangat bagus dan sangat premium ... tolong pastikan"* (giliran 4); "terasa premium" = disiplin desain (maks 2 font, maks 3 warna, whitespace, foto HD, transisi 0.3–0.5 dtk, footer konsisten) → akan ditegakkan di gerbang G2/G3; catatan jujur: biaya riil = waktu; lisensi video final = item terbuka (e) |
