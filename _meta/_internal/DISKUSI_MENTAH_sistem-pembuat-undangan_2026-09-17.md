# DISKUSI MENTAH — Discovery Level-0 Sistem Pembuat Undangan (nama sementara)

> **Sifat berkas ini:** rekaman **verbatim** masukan pemilik, disimpan atas permintaan eksplisit pemilik
> supaya tidak ada satu pun yang terlewat/terlupakan. **Bukan dokumen aturan, bukan instruksi aktif.**
> Preseden pola: `sistem/sistem-presentasi/DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md`.
>
> **Kenapa di `_meta/_internal/`, bukan di folder sistem:** folder `sistem/sistem-*/` yang ada di disk
> tetapi belum terdaftar di `INDEKS_SISTEM.md` = **error** validator (parse INDEKS ketat, anti-lubang
> review PR #11), sedangkan aturan INDEKS melarang mendaftar sistem baru sebelum `00_RENCANA_KERANGKA.md`
> di-merge. Jadi folder sistem **belum boleh dibuat** di tahap ini.
>
> **Umur berkas:** sementara. Setelah folder sistem dibuat (Langkah 2 alur bangun sistem baru), isi
> berkas ini **dipindah/diserap** ke `DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md` di dalam folder sistem itu,
> lalu berkas ini **boleh dihapus** — sesuai permintaan pemilik ("bisa dihapus di kemudian setelah tidak
> diperlukan lagi"). Penghapusan = tindakan sadar yang dicatat di LOG_SESI.
>
> **Bagian di bawah garis ini adalah kutipan UTUH tanpa suntingan** (ejaan, singkatan, dan tanda baca
> pemilik dipertahankan apa adanya). Yang ditambah hanya penanda giliran.

---

## Giliran 1 — 2026-09-17 (sesi `arena/01a0ae7a-pembangun-sistem`), jawaban Discovery Level-0 pertanyaan 1–3 + tambahan

Jawaban ku akan panjang. Aku ga mau ada satu hal pun yang terlupakan. Jadi aku rasa sebaiknya kamu simpan chat aku ini agar ga ada sedikitpun yang terlewat dan terlupakan, lalu bisa dihapus di kemudian setelah tidak diperlukan lagi

1. Sistem pembuat undangan. Untuk berbagai kebutuhan, tidak hanya wedding, tidak hanya khitanan, tidak hanya webinar, melainkan untuk kebutuhan apapun. Dan format nya juga bisa untuk format apa saja yang dibutuhkan, baik itu format laman web, ataupun video, ataupun flyer, ataupun siap cetak, ataupun lain nya. Aku rasa sebaiknya kamu melakukan riset di internet soal ini agar mendapat arah yang presisi kemudian kita bisa diskusikan lebih lanjut tanpa membuat aku harus berpikir keras dan bingung.
2. Aku belum punya gambaran sempurna soal ini. Aku akan sampaikan gambaran mentah nya aja, setelah itu kamu bisa perbaiki dan sempurnakan. Aku mau nanti setiap kali aku mau pake sistem ini, aku cukup buka sesi dengan suatu prompt. Setelah itu agent akan bawa ke arah mana yang aku inginkan. Nanti ada sesi aku jelasin info-info tentang undangan nya, acaranya, pemilik acara nya, tanggal nya, dan apapun info yang diperlukan. Mungkin untuk hal ini kamu perlu siapkan semacam list info apa aja yang diperlukan sebagai default, biarpun nanti di lapangan bisa aja ada info yang ga diperlukan atau sebaliknya ada info lebih dari biasanya. Terus ada sesi juga untuk tentukan desain nya dan format nya. Dan seterusnya sampe siap publish atau diserahkan ke client. Aku juga kurang paham gimana cara serahin ke client nya, khusus nya jika berupa website. Apakah aku harus buat semacam database dan domain khusus dulu untuk kebutuhan ini atau gimana. Aku minta arahan dari kamu. Jujur, aku ga punya basic di coding ataupun programming, jadi aku perlu arahan dan saran terbaik dari kamu. Inilah gambaran umum cara kerja sistem ini. Supaya lebih baik, aku rasa kita sebaiknya lakukan diskusi dan penggalian lebih mendalam dan kamu juga bisa melakuakn riset mendalam di internet atau dengan kemampuan berpikir kamu.
3. AKu rasa blm ada yang mirip dengan sistem ini. Tapi klo sekedar kemiripan, mungkin sistem building aplikasi, sistem persentasi, itu semua punya kemiripan.



Aku mau sistem ini dibekali dengan berbagai skill. Nanti kamu bisa melakukan riset di internet untuk mengumpulkan skill-skill terbaik yang dibutuhkan untuk memaksimalkan sistem ini. Nanti aku juga akan beri link beberapa skill yang aku temukan. Mungkin skill-skill yang berada di sistem building aplikasi juga bisa dipake di sitem ini. Dan kamu harus buat sistem ini betul-betul memaksimalkan skill-skill dan plugin-plugin yang diinstall.

Mekanisme-mekanisme yang diperlukan juga harus tertanam. Kamu tau kan apa aja mekanisme-mekanisme yang harus tertanam itu?

Aku juga mau ada semacam website induk untuk aku dapat mengelola semua undangan dan data yang udh dibuat. Karena sebenernya awalnya aku mau buat ini semacam website pembuat undangan yang ditenagai oleh AI. Namun aku merasa lmarena agent lebih andal dalam hal ini. Namun sayangnya lmarena agent ga bisa dipake sebagai ai yang mentenagai website, karena ga ada semacam api key. Jadi aku terpikir untuk buat sistem aja.

Dan untuk selebihnya (seperti terkait database nya mau seperti apa, sistem keamanan nya seperti apa, dan lain-lain) aku rasa itu perlu diskusi dan penggalian serta pemikira dan riset mendalam. Jadi tolong bantu yaa..

Aku juga mau di sistem ini ada semacam mekanisme di mana aku bisa input hal-hal yang ingin aku input, misalnya font, template, contoh, referensi, dan sebagainya.

Aku juga mau sistem ini dibekali kemampuan untuk generate aset-aset yang dibutuhkan, misalnya gambar-gambar png untuk kebutuhan dekorasi undangan wedding, dan sebagainya.

---

## Peta tuntutan yang diekstrak agent dari kutipan di atas

*(bagian ini BUKAN kutipan — ringkasan kerja agent supaya tidak ada tuntutan yang hilang; tiap butir
menunjuk kembali ke kalimat pemilik. Bagian ini yang dipakai sebagai daftar cek saat Discovery dan saat
menulis rencana kerangka.)*

| # | Tuntutan pemilik | Sumber kalimat | Status |
|---|---|---|---|
| T1 | Sistem pembuat undangan untuk **kebutuhan apa pun** (wedding, khitanan, webinar, dst — tidak terbatas) | poin 1 | terbuka — digali di Discovery |
| T2 | Output **multi-format**: laman web, video, flyer, siap cetak, dan lainnya | poin 1 | terbuka — butuh riset spesifikasi teknis per format |
| T3 | **Riset internet** oleh agent supaya arah presisi, pemilik tidak perlu berpikir keras | poin 1, poin 2, paragraf skill, paragraf terakhir | **dimandatkan** |
| T4 | Pemakaian dimulai dengan **satu prompt pembuka** → agent menuntun arah | poin 2 | sudah = butir warisan **W-01** |
| T5 | Sesi **pengumpulan info** undangan/acara/pemilik acara/tanggal + **daftar info default** yang boleh kurang atau lebih di lapangan | poin 2 | terbuka — inti Discovery poin 2 & 3 |
| T6 | Sesi **penentuan desain + format**, lanjut sampai **siap publish / diserahkan ke client** | poin 2 | terbuka — inti Discovery poin 2 (bentuk SIKLUS?) |
| T7 | **Arahan cara serah terima ke client**, khususnya website; apakah perlu database + domain khusus | poin 2 | terbuka — pemilik minta arahan |
| T8 | **Pemilik tidak punya basic coding/programming** → butuh arahan & saran terbaik, bahasa awam | poin 2 | **kendala mengikat untuk SEMUA dokumen sistem** (analog `PROFIL_PENGGUNA.md`) |
| T9 | Sistem **dibekali berbagai skill**; agent riset skill terbaik; pemilik akan memberi link tambahan; **skill di sistem building aplikasi mungkin bisa dipakai ulang**; sistem harus **betul-betul memaksimalkan** skill & plugin terpasang | paragraf skill | terbuka — mekanisme: `05_TAWARAN_KAPABILITAS.md` klinik (WAJIB-BERTAJUK, boleh ditolak) |
| T10 | **Mekanisme yang harus tertanam** — pemilik bertanya apakah agent tahu daftarnya | paragraf mekanisme | **terjawab**: Kontrak Warisan **W-01…W-09** (default aktif) + 6 prinsip universal |
| T11 | **Website induk** untuk mengelola semua undangan + data yang sudah dibuat | paragraf website induk | terbuka — keputusan arsitektur besar |
| T12 | Niat awal = website pembuat undangan bertenaga AI; **lmarena agent dinilai lebih andal**, tetapi **tidak bisa dipakai sebagai AI yang mentenagai website karena tidak ada API key** → diputuskan membuat sistem | paragraf website induk | **fakta pembatas yang mengunci arah**: AI-nya = agent di sesi, bukan layanan runtime di website |
| T13 | **Database, keamanan, dan lain-lain** perlu diskusi + penggalian + pemikiran + riset mendalam | paragraf terakhir | terbuka |
| T14 | **Mekanisme input dari pemilik**: font, template, contoh, referensi, dan sebagainya | paragraf input | terbuka — preseden: folder `Input-Pengguna/` di repo ini |
| T15 | **Kemampuan generate aset**, mis. gambar PNG untuk dekorasi undangan wedding | paragraf terakhir | terbuka |

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Berkas dibuat | Permintaan eksplisit pemilik di giliran 1 Discovery Level-0: simpan chat verbatim supaya tidak ada yang terlewat, boleh dihapus kemudian |
| 2026-09-17 | Ditaruh di `_meta/_internal/`, bukan di folder sistem | Folder `sistem-*/` tak terdaftar di INDEKS = error validator; INDEKS melarang mendaftar sistem sebelum rencana kerangka di-merge → folder sistem belum boleh dibuat di tahap Discovery |

---

# HASIL RISET AGENT (giliran 1, 2026-09-17) — memenuhi tuntutan T3

> Bagian ini **bukan** kutipan pemilik. Ini fakta hasil riset internet + pemetaan aset repo, disimpan supaya
> tidak hilang (sesi bisa crash). Angka harga/limit **berubah sewaktu-waktu** — sebelum dipakai sebagai
> keputusan terkunci, verifikasi ulang. Sumber dicantumkan sebagai URL, bukan dipercaya dari ingatan.

## A. Baseline fitur undangan digital di pasar Indonesia

Diperoleh dari 6 penyedia nyata (enviory.com, joyrsvp.com, lovelink.id, acaranya.id, undanganlink.id,
undanganmu.id, sannubari.com). **Ini bahan langsung untuk T5 (daftar info default) dan T6 (tahapan).**

**Fitur yang jadi standar pasar (hampir semua penyedia punya):**
- RSVP / konfirmasi kehadiran otomatis → masuk **dashboard**, rekap bisa **diunduh ke Excel**
- **Tautan personal per tamu** (nama tamu muncul di URL, mis. `domain.com/namamempelai?to=Nama+Tamu`) — tamu **unlimited**
- **QR Code check-in** di pintu + **Layar Sapa** (nama tamu tampil setelah check-in) + Buku Tamu Digital
- Google Maps / peta navigasi lokasi
- Musik latar (bisa **unggah sendiri**), autoplay
- Galeri foto (& video), love story / profil mempelai, **rundown/susunan acara**, dress code
- Ucapan & doa restu (buku tamu publik) + **amplop digital / e-gift / donasi** (cashless, QR)
- Countdown timer menuju hari-H
- **Template pesan WhatsApp siap pakai** untuk membagikan
- Notifikasi RSVP ke **email** + dashboard
- **Analitik kunjungan**
- **Autosave** + **boleh diubah setelah publikasi**
- Live streaming (Zoom/YouTube) — opsional
- Mobile friendly / responsif (dibuka dari browser HP, tanpa install aplikasi)
- Masa aktif: 3 / 6 / 12 bulan / lifetime — **ini model bisnis, bukan teknis**
- Jumlah revisi: 1x / 3x / tak terbatas — **ini model bisnis, bukan teknis**

**Pola arsitektur yang dipakai pasar:** SATU domain, BANYAK undangan sebagai **subpath**
(`joyrsvp.com/namamempelai`), terbentuk **instan** begitu nama terisi. Ini penting untuk **T11
(website induk)**: "induk" = dashboard pengelola + domain tunggal; tiap undangan = subpath/subdomain.

**Rentang harga pasar (per undangan, sekali bayar):** Rp 50.000 – Rp 500.000
(basic Rp 50–150K, standard Rp 150–300K, premium Rp 300–500K termasuk custom domain).
**Implikasi untuk sistem:** nilai jualnya = kecepatan + jumlah revisi tak terbatas + multi-format,
karena harga pasar sudah murah. (Analisis agent, bukan kutipan.)

**Cakupan acara di pasar:** pernikahan, khitan/aqiqah, ulang tahun, seminar/webinar, event umum —
**mengonfirmasi T1 pemilik** bahwa multi-jenis-acara memang arah pasar, bukan ide menyimpang.

## B. Cara serah terima ke client TANPA basic coding (menjawab T7 + T8)

Pola yang berulang di semua sumber (praktisi web dev + panduan 2026):

1. **Situs statik = kunci biaya nol.** Situs yang di-render jadi HTML/CSS/JS saat build, tanpa server
   backend yang berjalan terus → bisa hidup **gratis tanpa batas waktu** di infrastruktur gratis
   (Cloudflare Pages / Netlify / Vercel / GitHub Pages).
2. **Repo Git = database-nya.** Setiap edit jadi commit berversi → punya riwayat, rollback, audit trail.
   Kalau pindah developer/platform: serahkan repo, selesai. **Tidak ada proyek migrasi.**
3. **CMS bawaan di `/admin`** (Decap CMS / Sveltia CMS) supaya pemilik non-teknis bisa edit teks & ganti
   foto tanpa menyentuh kode — **tanpa biaya bulanan**.
4. **Hosting di akun CLIENT, bukan akun kita.** Kita yang setup, konfigurasi custom domain + SSL, semua
   di bawah login mereka → kepemilikan bersih, tidak ada sandera.
5. **Domain: client yang beli.** Pola paling aman menurut praktisi: **kembangkan dulu di domain/subdomain
   kita sendiri** (`proyek.domainkita.com`), **pindahkan ke domain client SETELAH lunas**. Kalau client
   belum punya domain, kita boleh belikan, tapi kepemilikan harus bisa diserahkan.
6. **Kalau butuh database sungguhan** (RSVP, buku tamu, analitik): Supabase/Postgres, atau pola tanpa-DB
   (form → Google Sheets / Edge Function → email).
7. **Model penyerahan alternatif:** transfer ownership project (client bikin akun sendiri, kita dipindah
   sebagai editor) — dipakai kalau platform-nya SaaS. Untuk sistem kita (repo + hosting statis) pola 1–5
   lebih cocok dan lebih murah.

**Rekomendasi agent untuk pemilik non-coder:** mulai dari pola **1 domain induk + subpath per undangan +
hosting gratis di akun pemilik**, database hanya untuk fitur interaktif (RSVP/ucapan/check-in).
Belum dikunci — perlu diskusi (lihat pertanyaan terbuka).

## C. Spesifikasi "siap cetak" (menjawab T2 untuk format cetak)

Standar prepress yang konsisten di 5 sumber:

| Item | Syarat |
|---|---|
| Mode warna | **CMYK** (bukan RGB) + ICC profile tertanam (FOGRA39 / ISO Coated v2 untuk kertas coated, GRACoL/SWOP untuk uncoated — **tanya percetakannya**) |
| Resolusi | **300 DPI** pada ukuran cetak final (foto/gradien); **600–1200 DPI** untuk line art 1-bit; large format (>A1, banner, dilihat dari jauh) boleh 150 DPI |
| Bleed | **3 mm (0.125")** di semua sisi — contoh A5 148×210 mm → dokumen jadi 154×216 mm |
| Safe zone | konten penting (teks, logo) minimal **3–5 mm di dalam** garis potong (10 mm untuk sisi jilid) |
| Font | **semua tertanam** (embedded) atau di-outline; tidak boleh font ter-link |
| Transparansi | di-flatten (PDF/X-1a) atau dipertahankan (PDF/X-4) |
| Format ekspor | **PDF/X-1a** (kompatibilitas maksimal, diterima hampir semua percetakan) atau **PDF/X-4** (lebih modern, ISO 15930-7) |
| Crop marks | ada, offset 3 mm, tebal 0.25 pt |
| Hitam | teks = K:100 murni (overprint); bidang hitam besar = **rich black C60 M40 Y40 K100** |
| Total tinta | ≤ 300% (coated) / ≤ 260% (uncoated) |
| Preflight | laporan bersih, tanpa error |

**⚠️ BATASAN TEKNIS PENTING (harus jujur ke pemilik, jangan dijanjikan muluk):**
Browser/headless Chrome (Puppeteer) **menghasilkan PDF RGB**, dan bahkan **mengonversi gambar CMYK jadi
RGB** (isu puppeteer/puppeteer#6480). Artinya HTML/CSS **tidak bisa** langsung menghasilkan PDF CMYK
siap cetak. Jalur yang terbukti: **2 tahap** — (1) render HTML → PDF lewat headless browser, (2) konversi
RGB → CMYK pakai **Ghostscript** (`-sDEVICE=pdfwrite -sColorConversionStrategy=CMYK
-sProcessColorModel=DeviceCMYK -dPDFSETTINGS=/printer -dUseBleedBox -dColorImageResolution=300`) atau
**ImageMagick** (`convert -density 300 -colorspace CMYK`). Konsekuensi desain: warna di layar **tidak
akan identik** dengan hasil cetak; bukti akhir tetap **proof fisik dari percetakan**. Alternatif kalau
Ghostscript tidak tersedia di lingkungan kerja: serahkan PDF RGB 300 DPI + catatan ke percetakan (banyak
percetakan digital Indonesia menerima ini), tapi **jangan diklaim sebagai "CMYK siap cetak"**.

## D. Format video (menjawab T2 untuk format video) — ⚠️ ADA JEBAKAN LISENSI

**Remotion** = framework bikin video MP4/WebM secara programatik dengan komponen React. Cocok persis
untuk kasus kita: **satu template → isi data berbeda → render ratusan video undangan personal**.
Ada **81 template efek gratis** (reactvideoeditor/remotion-templates): text (9), background (9),
cinematic (9), transition (9), dst — Ken Burns, parallax, film burn, letterbox reveal.
Alur AI-friendly: agent tulis komponen React → preview di Remotion Studio → render MP4.
Perintah mulai: `npx create-video@latest` / `npm init video`.

**⚠️ LISENSI (harus diputuskan sadar, bukan diasumsikan gratis):**
- **GRATIS** untuk: individu, non-profit, dan **perusahaan for-profit dengan ≤ 3 karyawan** — **termasuk
  pemakaian komersial** (boleh kirim kerjaan client berbayar, render unlimited, self-hosted Lambda).
- **WAJIB BAYAR** begitu perusahaan for-profit punya **≥ 4 karyawan**. Pemicunya **jumlah kepala
  perusahaan**, BUKAN berapa orang yang menyentuh Remotion.
- Harga 2026: **Creators $25/seat/bulan** (tanpa minimum) · **Automators $0.01/render, minimum
  $100/bulan** · **Enterprise mulai $500/bulan**. Beberapa sumber menyebut "mulai ~$100/bln".
- **Alternatif bebas lisensi:** **Motion Canvas** (MIT, gratis untuk semua ukuran perusahaan),
  **HyperFrames** (Apache 2.0). Fitur lebih muda, tapi nol risiko lisensi.
- **Alternatif nol-dependency:** render frame → rakit pakai **ffmpeg** (bebas, GPL/LGPL) — lebih banyak
  kerjaan, tanpa risiko lisensi sama sekali.

**Konsekuensi untuk sistem ini:** format video butuh **satu keputusan lisensi yang dicatat di manifest**
(W-08/kategori Besar), karena kalau usaha pemilik nanti punya ≥4 orang, biaya lisensi muncul tiba-tiba.

## E. Database / backend (menjawab T11 + T13)

**Supabase free tier (2026):** 500 MB database Postgres · 1 GB file storage · 5 GB bandwidth/bulan ·
50.000 MAU (auth) · 500.000 invokasi Edge Function/bulan · **maksimal 2 project aktif** ·
**⚠️ project DI-PAUSE setelah 1 minggu tidak aktif** · **tanpa backup** · support komunitas saja.
Pro = **$25/bulan** (8 GB DB, 100 GB storage, 250 GB bandwidth, tanpa pause).
Pembanding: Firebase Spark = 1 GB Firestore, 5 GB storage, 10 GB bandwidth, auth gratis unlimited,
**tidak di-pause**, tapi NoSQL & tidak open source.

**⚠️ Risiko yang harus diangkat:** aturan **pause setelah 1 minggu tidak aktif** berbahaya untuk
undangan yang harus tetap hidup sampai hari-H (apalagi masa aktif 3–12 bulan). Kalau undangan = situs
statik di Cloudflare Pages (tanpa DB), risiko ini hilang; DB hanya perlu untuk RSVP/ucapan/check-in.
**Rekomendasi agent:** pisahkan — **undangan statis (murah, tahan lama, tanpa DB)** vs **fitur interaktif
(butuh DB)**. Kalau fitur interaktif dimatikan untuk sebagian undangan, tidak ada biaya dan tidak ada
risiko pause. Belum dikunci — perlu diskusi.

## F. Aset gambar / dekorasi (menjawab T15) + lisensi font (risiko hukum)

**Generate aset PNG dekorasi:** lingkungan kerja agent ini menyediakan alat **`generate_image`**
(text-to-image + edit gambar, simpan ke `.png`/`.jpg`) — relevan langsung untuk ornamen undangan,
dekorasi wedding, latar, elemen bunga/kaligrafi. **Batas kejujuran yang harus dicatat:** (a) alat ini
menghasilkan **AI-generated imagery**, bukan vektor; (b) **transparansi (alpha channel) tidak dijamin**
— PNG hasil model gambar sering datang dengan latar, jadi perlu langkah pemisahan latar atau prompt yang
meminta latar polos; (c) ketersediaan alat **bergantung platform**, jadi sistem tidak boleh mengasumsikan
ada — perlu jalur cadangan (aset stok/vektor yang diinput pemilik, lihat T14); (d) hasil AI **tidak cocok
untuk line art cetak 600–1200 DPI** tanpa vektorisasi.

**⚠️ LISENSI FONT (risiko hukum nyata untuk usaha komersial):**
- **Google Fonts = AMAN.** Seluruh katalog dirilis open source: mayoritas **SIL Open Font License (OFL)**,
  sebagian **Apache 2.0**. Boleh: dipakai di situs komersial, kerjaan client berbayar, di-embed di web
  app, **dicetak** di buku/merch/packaging, dipakai di logo yang dijual ke client, dimodifikasi.
  **Tanpa biaya, tanpa royalti, tanpa izin, tanpa atribusi wajib** di produk akhir. Client otomatis
  menerima hak penuh dari lisensi open source — **tidak perlu dokumen serah-terima lisensi font**.
- **Satu-satunya larangan OFL:** menjual **file font mentah** sebagai produk berdiri sendiri, dan memakai
  **Reserved Font Name** untuk versi modifikasi.
- **Self-hosting disarankan** (unduh `.woff2`, sajikan dari domain sendiri) — legal, lebih cepat, dan
  menghindari isu privasi GDPR (putusan pengadilan Jerman 2022: CDN Google meneruskan IP pengunjung).
- **⚠️ JEBAKAN yang harus ditanam sebagai aturan sistem:** font dari luar Google Fonts punya
  **lisensi berbeda per kanal** — lisensi *desktop* (Photoshop/Illustrator → gambar statis) **TIDAK**
  memberi hak *web* (`@font-face`), dan hak **document embedding di PDF** harus dicek terpisah (sebagian
  hanya boleh PDF "Read Only"). Ada juga klausul **larangan dipakai melatih model AI**.
- **Risiko nyata yang terdokumentasi:** cease & desist + tagihan lisensi retroaktif berpenalti; satu
  kasus ditemukan $10.000 → settle $2.000, ada yang sampai $50.000+; **Font Bureau vs NBCUniversal
  $2 juta**. **Client juga bisa ikut dituntut**, lalu menuntut balik ke kita. Situs "font gratis" banyak
  menampung versi bajakan → crawler foundry bisa menemukan file proprieternya di server kita.
- **Konsekuensi untuk sistem:** mekanisme input font milik pemilik (T14) **WAJIB** disertai pencatatan
  lisensi per font (nama, sumber, lisensi, kanal yang diizinkan: web/desktop/PDF-embed) — dan default
  paling aman = **hanya Google Fonts (OFL/Apache 2.0)** kecuali pemilik menyatakan punya lisensinya.

## G. Pemetaan 56 skill TERPASANG di `sistem-building-aplikasi/skills/` ke kebutuhan sistem ini (T9)

**Langsung terpakai, nilai tinggi:**
- `banner-design` — desain banner untuk sosmed/iklan/hero web/kreatif **dan print**; multi art direction. **Paling dekat ke flyer undangan.**
- `design` — brand identity, design tokens, **logo generation (55 gaya)**, corporate identity (50 deliverable, CIP mockup)
- `design-system` — arsitektur token 3 lapis (primitive→semantic→component), CSS variables, skala spacing/tipografi, spesifikasi komponen
- `brand` — brand voice, identitas visual, konsistensi brand, style guide → **cocok untuk "Brand Core" sistem undangan**
- `ui-ux-pro-max` — inteligensi desain UI/UX web/mobile/desktop
- `frontend-designer` + `frontend-designer-lite` — arsitektur CSS, token, UI responsif, aksesibilitas, motion
- `ui-styling` — shadcn/ui (Radix + Tailwind), desain visual berbasis canvas
- `web-design-guidelines` — review UI vs Web Interface Guidelines, audit aksesibilitas/UX
- `building-components` — komponen UI modern, aksesibel, composable, design tokens
- `agent-browser` — **otomasi browser + screenshot** → kunci untuk **verifikasi visual** undangan & uji responsif HP
- `slides` — presentasi HTML strategis + Chart.js + design tokens + layout responsif
- `excalidraw-diagram` — diagram JSON untuk alur/arsitektur
- `find-skills` — **discover & install skill saat dibutuhkan** → mekanisme resmi untuk T9 (skill baru tanpa riset manual)

**Infrastruktur & publikasi (menjawab T7/T11):**
- `cloudflare` (arsitektur + pemilihan produk) · `wrangler` (CLI deploy Cloudflare) · `vercel-deploy` · `next-best-practices` · `next-upgrade` · `next-cache-components` · `vercel-react-best-practices` · `agents-sdk` · `workflow` (durable/resumable workflows)
- `supabase` · `supabase-postgres-best-practices` (**wajib dibaca sebelum menyentuh Postgres**)
- `security-review` — auth, input pengguna, secrets, API endpoint, pembayaran → **menjawab T13 (keamanan)**

**Google Workspace (menjawab fitur pasar: export Excel, notifikasi email, kalender):**
- `google-sheets` (rekap tamu/RSVP) · `gmail` (notifikasi RSVP) · `google-calendar` (tanggal acara/pengingat) · `google-drive` · `google-docs` · `google-slides` · `google-chat`

**Proses & kualitas (menjawab T10, mekanisme tertanam):**
- `brainstorming` — **"You MUST use this before any creative work"** → cocok jadi gerbang Discovery/desain
- `writing-plans` · `prd-taskmaster` · `product-management` (user story, acceptance criteria, sprint) · `product-discovery`
- `systematic-debugging` · `tdd-workflow` · `test-driven-development` · `verification-loop` · `verification-before-completion` (**larang klaim sukses sebelum menjalankan verifikasi**)

**AI/SDK:** `ai-sdk` · `ai-elements` (UI chat) · `streamdown`

**TIDAK relevan untuk sistem ini (jangan ikut disalin, hemat bobot folder):**
`ios-agent`, `alibaba-java`, `tsbs-benchmark`, `ucp`, `vercel-react-native-skills`, `vercel-composition-patterns`, `next-cache-components` (kecuali pakai Next.js)

**GAP — skill yang BELUM ada dan perlu diriset/ditawarkan (bahan tawaran kapabilitas, W-08):**
1. **Video/Remotion** — tidak ada skill video terpasang sama sekali (padahal T2 minta format video)
2. **Prepress/PDF cetak** — tidak ada skill CMYK/bleed/PDF-X (padahal T2 minta siap cetak)
3. **Generate gambar/aset** — tidak ada skill; andalkan alat platform `generate_image` + perlu jalur cadangan
4. **QR code** — tidak ada (padahal QR check-in = fitur standar pasar)
5. **Font management / subsetting `.woff2`** — tidak ada (padahal F di atas menunjukkan risiko lisensinya nyata)
6. **WhatsApp** — tidak ada (padahal distribusi utama undangan = share via WA + template pesan WA)
7. **Pembayaran / amplop digital** — tidak ada (padahal amplop digital/e-gift = fitur standar pasar; `security-review` menyebut payment tapi bukan integrasi)
8. **i18n / bahasa daerah + kaligrafi Islami** — tidak ada (padahal pasar minta template Islami/Jawa)

## Log Keputusan (lanjutan)

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Bagian "Hasil riset agent" ditambahkan (A–G) | Tuntutan T3 pemilik: agent yang riset internet supaya arah presisi dan pemilik tidak perlu berpikir keras. Hasil riset disimpan sebagai berkas, bukan cuma chat, karena sesi bisa crash (fakta platform #3) |
| 2026-09-17 | 3 risiko dicatat eksplisit: lisensi Remotion (≥4 karyawan berbayar), HTML→PDF tidak bisa CMYK langsung (perlu Ghostscript), Supabase free tier pause 7 hari | Ketiganya bisa membuat janji sistem meleset dari kenyataan; aturan repo menuntut batas kejujuran dicatat, bukan dihaluskan |

## H. Arsitektur nol-biaya: verifikasi Cloudflare free tier (giliran 2)

**Kenapa Cloudflare, bukan Supabase:** pemilik mensyaratkan *"maksimalkan sejak awal tanpa perlu biaya dan
tanpa ada resiko kekurangan dan kecacatan"*. Supabase free **di-pause setelah 1 minggu tidak aktif** dan
**tanpa backup** → gagal syarat untuk undangan yang harus hidup sampai hari-H. Cloudflare free **tidak
tidur**, dan STATUS sistem-building-aplikasi sudah mencatat preferensi pemilik: **"suka Cloudflare"**.

| Layanan | Batas gratis (terverifikasi 2026) | Cukup untuk usaha undangan solo? |
|---|---|---|
| **Pages** (hosting statis) | permintaan aset statik **gratis & tak terbatas**, bandwidth **tanpa meter**, **500 build/bulan**, 1 build serentak, 20.000 berkas/situs, **25 MiB/berkas**, 100 custom domain/proyek, 100 proyek/akun | ✅ jauh lebih dari cukup |
| **Workers** (fungsi dinamis: form RSVP, check-in) | **100.000 permintaan/hari**, 10 ms CPU/permintaan, 50 subrequest, 128 MB memori, bundle **64 MiB** (naik dari 3 MB per 4 Sep 2026) | ✅ 1 undangan × 1.000 tamu ≈ ribuan permintaan; 100 undangan serentak masih aman |
| **D1** (database SQL) | **5 juta baris dibaca/hari**, **100 ribu baris ditulis/hari**, **5 GB total**, **tanpa kartu kredit** | ✅ data teks RSVP/ucapan/tamu; 5 GB = jutaan baris |
| **KV** | 1 GB, 100 ribu baca/tulis per hari | ✅ counter analitik, token check-in |
| **R2** (storage media) | **10 GB**, 1 juta operasi/bulan, **tanpa biaya egress** | ⚠️ foto/musik — **perlu anggaran aset** (lihat risiko) |
| **Analytics Engine / Web Analytics** | termasuk, kardinalitas tak terbatas | ✅ analitik kunjungan |
| **Durable Objects** | 400 ribu GB-detik, 1 juta permintaan/bulan | ✅ Layar Sapa realtime (opsional) |

**⚠️ 6 plafon yang WAJIB dicatat sebagai risiko aktif (bukan disembunyikan):**
1. **Sejak 1 Sep 2026 D1 free tier jadi HARD FAIL** — melewati 5 juta baca / 100 ribu tulis per hari = query **gagal dengan error** sampai reset 00:00 UTC (sebelumnya enforcement-nya lunak). Mitigasi: index yang benar, pantau `meta.rows_read`, alarm di 80% (4 juta).
2. **Cloudflare Pages §2.8 Self-Serve Agreement melarang memakai layanan TERUTAMA untuk menyajikan video/berkas non-HTML besar.** Tidak ada angka GB yang dipublikasikan; penegakannya **diskresioner** (historisnya berupa email suruh pindah ke Stream/upgrade/pergi). **Mitigasi wajib: media besar (musik, video) ke R2, JANGAN jadikan Pages sebagai CDN video.**
3. **Pages free: tanpa SLA uptime, tanpa dukungan prioritas.** Untuk hari-H pernikahan ini risiko nyata. Mitigasi jujur: situs statik di-cache di edge = sangat tahan banting, tetapi **tidak ada jaminan kontraktual**; SLA 100% baru ada di Business $250/zone/bulan.
4. **R2 10 GB gratis cepat habis oleh foto.** Perlu **anggaran aset yang dikunci sebagai aturan sistem** (mis. foto tamu/galeri maks 300 KB setelah kompresi → ±33.000 foto; musik maks 2 MB → ±5.000 lagu).
5. **Istilah free tier BERUBAH — terbukti.** Sepanjang 1–4 Sep 2026 Cloudflare mengubah 3 hal sekaligus (D1 hard-fail, WAF SQLi log→block, Workers bundle 3 MB→64 MiB). Satu sumber menyimpulkan: *"the free tier is being redrawn as a development environment, not a production substrate"*. Mitigasi: **jalur keluar $5/bulan** (Workers Paid: 10 juta permintaan + 30 juta CPU-ms) dicatat di manifest sebagai rencana naik-tingkat, dan data harus **selalu bisa diekspor** (repo Git + dump D1 + export ke Google Sheets).
6. **Batas 25 MiB/berkas dan 20.000 berkas/situs** di Pages — menentukan cara menyusun satu proyek untuk banyak undangan (subpath, bukan proyek terpisah per undangan).

**Amplop digital tanpa biaya:** tampilkan nomor rekening + gambar QRIS statis + tombol "sudah transfer" yang
dicatat ke D1. **Nol biaya.** Gateway pembayaran sungguhan (Midtrans/Xendit) = **MDR per transaksi**, jadi
itu fitur premium berbayar, bukan bagian jalur nol-biaya.

## I. VERIFIKASI TOOLCHAIN di lingkungan agent — bukti terukur, bukan asumsi (giliran 2)

Dijalankan langsung di sandbox sesi ini. **Inilah lingkungan tempat sistem nanti benar-benar bekerja.**

**✅ ADA:** `node v22.22.3` · `npm 10.9.8` · `npx` · `python3 3.11.2` · `pip 23.0.1` · `convert` (ImageMagick 6.9.11-60) · `zip`/`unzip` · `curl` · **`sudo` passwordless** · `apt-get` tersedia.
**✅ Jaringan:** registry **npm hidup** (`npm view remotion version` → **4.0.525**), **PyPI hidup** (`pip3 download qrcode` berhasil).
**❌ TIDAK ADA:** `ghostscript`/`gs` · `ffmpeg` · `chromium`/`chrome` · `rsvg-convert` · `inkscape` · `pdftk`/`qpdf` · `exiftool`.
**❌ Diblokir kebijakan:** **ImageMagick TIDAK BISA menulis/membaca PDF** — `convert-im6.q16: attempt to perform an operation not allowed by the security policy 'PDF'` (policy.xml Debian pasca-CVE Ghostscript). Berkas 0 byte dihasilkan. **Jalur "Ghostscript/ImageMagick untuk CMYK" di bagian C TIDAK tersedia di lingkungan ini.**
**✅ Aset tak terduga di repo:** **54 font TTF** sudah ada di `sistem/sistem-building-aplikasi/skills/ui-styling/canvas-fonts/` (ArsenalSC, BigShoulders, Boldonse, BricolageGrotesque, …). **Font sistem `/usr/share/fonts` kosong** (`fc-list` = 0) → font untuk cetak **harus** datang dari repo atau unduhan, bukan dari sistem.

### Bukti penentu: PDF CMYK siap cetak TANPA Ghostscript — **BERHASIL**

Jalur pengganti yang terbukti: **ReportLab** (`pip install reportlab`, terpasang 5.0.1) + `pypdf` 6.19.0 untuk verifikasi independen.

Uji nyata di `/tmp/uji_cmyk.py` → `/tmp/undangan-uji-cmyk.pdf`, hasil **dibaca balik oleh pypdf, bukan diklaim**:

| Yang diuji | Target prepress | Hasil terukur | Verdict |
|---|---|---|---|
| Ukuran halaman | A5 + bleed 3 mm = 154×216 mm | `154.0 x 216.0 mm` | ✅ |
| Trim size | 148×210 mm (A5) | `148.0 x 210.0 mm` | ✅ |
| Ruang warna | CMYK, **nol** RGB | **4 operator `k`/`K`**, **0 operator `rg`/`RG`**, **0 operator `g`/`G`** | ✅ |
| Rich black | C60 M40 Y40 K100 | `.6 .4 .4 1 k` — **persis** | ✅ |
| Crop marks | 4 sudut, offset 3 mm, 0.25 pt | 16 operator moveto/lineto (4 sudut × 2 garis × 2 op) | ✅ |
| Font tertanam | wajib embedded/subset | `/F2+0` BaseFont `AAAAAA+ArsenalSC-Regular`, Subtype `/TrueType`, **FontFile2: TERTANAM** | ✅ |
| Bobot berkas | — | **14.3 KB** | ✅ |

**⚠️ 1 temuan jujur dari uji ini:** sumber daya font juga mendaftarkan `/F1 Helvetica` (Type1, **tidak tertanam**)
— artefak font bawaan ReportLab. Tidak dipakai menggambar teks (semua teks pakai font tertanam), tetapi
**preflight percetakan bisa menandainya**. Aturan sistem wajib: **pastikan hanya font tertanam yang dirujuk**,
dan verifikasi tidak ada BaseFont standard-14 terpakai sebelum berkas disebut "siap cetak".

**Konsekuensi arsitektur yang lahir dari bukti ini (penting):** PDF CMYK **tidak bisa** dihasilkan dari
HTML/CSS (browser menghasilkan RGB — bagian C). Jadi **format cetak = jalur render terpisah** dari format web.
Supaya tidak mendesain dua kali, **desain harus didefinisikan di atas kedua renderer** sebagai **design token**
(warna dinyatakan berpasangan RGB *dan* CMYK, ukuran, spasi, skala tipografi) — persis yang disediakan skill
`design-system` (token 3 lapis primitive→semantic→component). **Satu sumber desain → dua mesin cetak.**

**⚠️ Batas yang belum diverifikasi (jangan diklaim siap):** (a) `pip install` **tidak bertahan antar sesi** →
sistem wajib punya langkah "siapkan toolchain" di awal sesi, atau vendor dependensinya; (b) **video via Remotion
belum diuji render nyata** — npm-nya tersedia, tetapi Remotion perlu mengunduh headless shell Chromium (±ratusan MB)
dan render-nya berat/lambat; **ini harus diuji di fase tersendiri, bukan dijanjikan sekarang**; (c) `ffmpeg` tidak ada
di sistem — Remotion membawa ffmpeg sendiri, tapi belum dibuktikan di lingkungan ini; (d) `generate_image` adalah alat
platform, ketersediaannya bergantung platform (sudah dicatat di bagian F).

## Log Keputusan (lanjutan)

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Bagian H (Cloudflare) + I (verifikasi toolchain) ditambahkan | Pemilik mensyaratkan maksimal sejak awal **tanpa biaya dan tanpa risiko**; syarat itu hanya bisa dijawab dengan bukti, bukan janji. Supabase gugur karena pause 7 hari + tanpa backup |
| 2026-09-17 | **Jalur CMYK bagian C DIKOREKSI**: Ghostscript/ImageMagick **tidak tersedia** di lingkungan ini; diganti **ReportLab** (terbukti dengan bukti terukur di atas) | Kejujuran: bagian C ditulis dari riset internet sebelum lingkungan diverifikasi. Setelah diuji, ImageMagick diblokir policy untuk PDF dan Ghostscript tidak terpasang. Koreksi dicatat, bukan dihapus diam-diam (append-only) |
| 2026-09-17 | Prinsip arsitektur dikunci sementara: **satu sumber design token → dua jalur render (web RGB / cetak CMYK)** | Lahir dari bukti bahwa HTML tidak bisa menghasilkan CMYK; tanpa ini desain akan dikerjakan dua kali dan berisiko tidak konsisten (Discovery poin 3) |
