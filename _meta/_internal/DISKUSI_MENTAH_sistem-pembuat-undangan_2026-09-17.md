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

## J. Pipeline aset foto: bukti terukur (giliran 3) + KOREKSI atas usulan agent sendiri

**Pemicu:** pemilik menolak usulan "anggaran aset maks ~300 KB" dengan alasan jujur — *"yang aku tau yang
namanya foto yang bagus itu kan biasanya ukuran nya besar, bukan cuma setengah mb"* — dan meminta mekanisme:
pemilik upload foto, agent memproses supaya **tetap bagus, tidak burik, tapi ukurannya kecil**.

**Lingkungan terverifikasi:** ImageMagick 6.9.11-60 di sandbox ini mendukung **WEBP (libwebp 1.2.4)** dan
**AVIF/HEIC 1.15.1)** (rw+). `Pillow 12.3.0` mendukung **WebP=True, AVIF=True**. `numpy 2.4.6` terpasang.
`cwebp`/`avifenc` CLI **tidak ada** (tidak diperlukan — Pillow/ImageMagick sudah cukup).

### J.1 Hasil uji kompresi (foto nyata dari repo, diukur dengan PSNR + SSIM implementasi sendiri)

Bahan: `sistem/sistem-konten-kreator/_produksi-aktif/narasi-sejarah-sumur-di-belakang-rumah/assets/S3-ember-berjejer.png`
— **768×1376, 2.937 KB, PNG lossless**. Metrik: PSNR (dB) + SSIM Gaussian 11×11 σ=1.5 per kanal, rata-rata 3 kanal.

| Varian | Ukuran | Hemat | PSNR (dB) | SSIM | Penilaian |
|---|---|---|---|---|---|
| WebP q85 | 285 KB | 90,3% | **37,39** | **0,9791** | sangat baik — aman untuk gambar utama (hero) |
| WebP q78 | 218 KB | 92,6% | 35,15 | 0,9673 | baik |
| WebP q70 | 182 KB | 93,8% | 33,80 | 0,9577 | mulai turun |
| WebP q60 | 164 KB | 94,4% | 33,02 | 0,9516 | mulai turun |
| **AVIF q62** | **139 KB** | **95,3%** | **34,09** | **0,9625** | **rasio ukuran/kualitas terbaik** |
| AVIF q50 | 93 KB | 96,8% | 31,56 | 0,9407 | degradasi mulai terlihat |
| AVIF q40 | 64 KB | 97,8% | 29,41 | 0,9117 | degradasi jelas — jangan dipakai |
| JPEG q85 | 311 KB | 89,4% | 36,08 | 0,9747 | fallback browser lama |
| JPEG q75 | 236 KB | 92,0% | 34,14 | 0,9643 | fallback |

**Skala penilaian yang dipakai (standar umum, bukan karangan):** PSNR ≥40 & SSIM ≥0,99 = nyaris tak
terbedakan · PSNR 35–40 & SSIM 0,97–0,99 = sangat baik, aman untuk layar · PSNR <32 = degradasi mulai terlihat.

**⚠️ Batas kejujuran angka "Hemat":** bahan ujinya **PNG lossless**, jadi persentase hemat terlihat sangat besar.
Foto kiriman client di dunia nyata biasanya **sudah JPEG**, sehingga penghematan riil terhadap JPEG asal akan
**jauh lebih kecil** (khas 25–50% untuk WebP/AVIF pada kualitas setara). Angka di atas **tidak boleh** dikutip
sebagai "hemat 95% untuk foto client". Uji ulang dengan foto asli client **wajib** dilakukan saat implementasi.

**Rekomendasi berbasis bukti:** titik manis = **AVIF q62** (139 KB, PSNR 34,09) untuk gambar pendukung, dan
**WebP q85** (285 KB, PSNR 37,39) untuk gambar utama/hero; **JPEG q85 sebagai fallback**; disajikan dengan
`<picture>` + `srcset` (AVIF → WebP → JPEG) supaya browser memilih sendiri.

### J.2 TEMUAN PENENTU: aset web **TIDAK BISA** dipakai untuk cetak

Perhitungan aritmetik dari bahan uji yang sama (768 px lebar) terhadap syarat 300 DPI:

| Lebar cetak | Butuh px @300 DPI | Punya | Verdict |
|---|---|---|---|
| A5 + bleed 3 mm (full bleed) | **1.819 px** | 768 px | **KURANG 2,4×** |
| A5 trim | 1.748 px | 768 px | **KURANG 2,3×** |
| Kartu 100 mm | 1.181 px | 768 px | **KURANG 1,5×** |
| Elemen kecil 50 mm | 591 px | 768 px | CUKUP |

**Foto 768 px hanya layak cetak sampai lebar 65 mm @300 DPI.**

### J.3 KOREKSI atas usulan agent sendiri (jujur, bukan dibela)

Usulan agent di giliran 2 — **"anggaran aset: foto maks ~300 KB"** — **SALAH** dan dicabut. Alasannya:
angka itu menyatukan dua kebutuhan yang **saling bertentangan**. Kompresi yang membuat foto ringan untuk HP
**justru menghancurkan** kelayakannya untuk cetak. **Keberatan pemilik benar.**

**Aturan pengganti (kandidat kuat untuk Discovery poin 3): DUA tingkat aset, bukan satu anggaran.**
1. **ASET INDUK (original)** — disimpan **apa adanya, tidak pernah dikompresi**, diarsipkan terpisah.
   **Hanya ini yang boleh dipakai untuk format cetak.** Wajib lolos **gerbang resolusi** sebelum format cetak dijanjikan.
2. **ASET TURUNAN WEB** — dibuat otomatis dari induk: beberapa lebar (mis. 480/768/1200/1600 px) dalam
   AVIF + WebP + JPEG fallback, disajikan lewat `srcset`. **Tidak pernah** dipakai untuk cetak.

**Gerbang resolusi (fail-closed, bukan fail-open):** saat intake, agent **mengukur** lebar×tinggi tiap foto dan
**membandingkan** dengan ukuran cetak yang diminta. Kalau kurang → sistem **MENOLAK menjanjikan format cetak**
dan melaporkan kekurangannya berapa kali lipat, **bukan** diam-diam mencetak foto burik. Kalau client hanya punya
foto kecil, pilihannya dinyatakan terbuka: (a) naikkan kualitas dengan alat upscale (hasil **tidak setara** foto
asli resolusi tinggi — harus dinyatakan), (b) cetak pada ukuran lebih kecil, (c) ganti foto, (d) batalkan format cetak.

**Mekanisme input yang diminta pemilik (T14) jadi konkret:** pemilik menaruh foto ke folder input
(preseden repo: `Input-Pengguna/` atau `_input/` per undangan) → agent menjalankan pipeline: **inventarisasi
(ukur dimensi+byte) → validasi resolusi vs target cetak → simpan induk ke arsip → hasilkan turunan web →
ukur PSNR/SSIM tiap turunan → tulis manifest aset berisi angka terukur**. Pemilik tidak perlu paham apa pun
soal kompresi; yang dilihat pemilik hanyalah **tabel hasil: nama foto, layak cetak ya/tidak, ukuran sebelum/sesudah**.

## Log Keputusan (lanjutan)

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Bagian J ditambahkan: bukti uji kompresi (9 varian, PSNR+SSIM) + perhitungan kelayakan cetak | Pemilik menyatakan tidak paham dan tidak bisa memastikan batas yang agent tetapkan → dijawab dengan angka terukur, bukan penegasan ulang |
| 2026-09-17 | **Usulan agent "foto maks ~300 KB" DICABUT sebagai salah**; diganti aturan **dua tingkat aset + gerbang resolusi fail-closed** | Keberatan pemilik terbukti benar oleh aritmetika: foto 768 px kurang 2,4× untuk A5 full-bleed @300 DPI. Kompresi web dan kelayakan cetak adalah dua kebutuhan yang bertentangan, tidak bisa diatur satu angka |
| 2026-09-17 | Batas kejujuran angka "hemat 95%" dicatat eksplisit | Bahan uji PNG lossless, bukan JPEG kiriman client; mengutipnya sebagai penghematan riil akan menyesatkan |

---

## Giliran 2 — 2026-09-17, tuntutan tambahan: MANUAL BOOK INDUK + MEKANISME REVIEW INDEPENDEN

> **Kutipan UTUH tanpa suntingan** (ejaan, singkatan, tanda baca pemilik dipertahankan apa adanya).
> Pemilik membuka giliran ini dengan: *"Ini chat panjang, pastikan ga ada yang terlupakan."*

Ini chat panjang, pastikan ga ada yang terlupakan.



aku mau di sistem ini ada satu file untuk pengguna yang betul-betul isinya lengkap. Ada segala hal yang perlu dijelaskan dan perlu dipahami pengguna, termasuk mekanisme audit dan pemeriksaan, dan juga ada semua prompt yang dibutuhkan. Memang boleh saja kita buat setiap mekanisme ada buku panduan nya tersendiri untuk pengguna. Tapi file pedoman pengguna yang udh ada dari awal sistem ini dipake, itu harus betul-betul jadi induk dan lengkap, sekiranya kapanpun pengguna mau pake dan mau cari tau cara melakukan sesuatu maka dia cukup liat buku panduan itu dan di dalam nya udh ada semuanya. Jadi semacam manual book gitu loh. Paham kan maksud aku?



aku juga mau melakukan dan menanamkan mekanisme audit, pemeriksaan, analisis dan review independen yang sangat teliti dan sangat cerdas. Pastikan agent independen betul-betul jeli dan bisa betul-betul menemukan masalah (klo memang ada) dan betul betul melakukan secara sempurna tanpa terlewat hal sekecil apapun. Dan aku mau mekanisme ini betul-betul menyeluruh, bukan hanya file fondasi sistem, tapi juga termasuk file pendoman pengguna, dan juga semua file yang perlu untuk diperiksa, karena itu sangat penting untuk terus diperbaiki saat diperlukan. Klo ada skill yang bisa mendukung mekanisme ini, pastikan agent independen menggunakan nya. Dan klo perlu riset di internet untuk ini, pastikan agent independen melakukan nya. kamu harus tanamkan mekanisme ini dalam sistem ini, tapi tentunya harus dimatangkan dulu. Maka klo untuk membuat mekanisme ini perlu riset mendalam dan searching di internet, silahkan lakukan. Aku mau setelah mekanisme ini tertanam, di panduan pengguna dijelaskan cara ketika aku mau melakukan ini. Paham kan maksud aku? Tapi sebelum eksekusi, kamu harus pastikan dulu, apakah ide aku bagus atau tidak. Jika tidak, jangan lakukan

## Peta tuntutan tambahan (ekstraksi agent)

| # | Tuntutan pemilik | Sumber kalimat | Catatan agent |
|---|---|---|---|
| T16 | **SATU berkas pedoman pengguna yang jadi INDUK dan LENGKAP** — berisi segala hal yang perlu dijelaskan & dipahami pengguna, **termasuk mekanisme audit/pemeriksaan**, dan **semua prompt yang dibutuhkan** | paragraf 1 | Bersinggungan langsung dengan butir warisan **W-01** (sudah wajib) — jadi ini **penguatan**, bukan hal baru |
| T17 | Pedoman per-mekanisme **boleh** ada tersendiri, **tetapi** induknya harus lengkap: kapan pun pengguna mau melakukan sesuatu, **cukup lihat satu buku itu** dan semuanya ada di dalamnya — *"semacam manual book"* | paragraf 1 | ⚠️ **Berpotensi bentrok dengan norma anti-dokumen-kembar** yang berlaku di repo ini — harus diselesaikan secara struktural, bukan diabaikan |
| T18 | **Tanamkan mekanisme audit, pemeriksaan, analisis, dan review independen** yang sangat teliti dan sangat cerdas | paragraf 2 | Repo ini **SUDAH PUNYA** `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` + `tools/review_prompt.py` yang sudah terpakai nyata di puluhan PR → jawaban yang benar **mewarisi & mengadaptasi**, bukan mengarang baru |
| T19 | Agent independen harus **betul-betul jeli**, menemukan masalah kalau memang ada, dan bekerja **"sempurna tanpa terlewat hal sekecil apapun"** | paragraf 2 | ⚠️ **Rumusan tidak bisa diuji (unfalsifiable)** — harus diterjemahkan jadi cakupan + checklist + perintah yang bisa direproduksi |
| T20 | Cakupan review **menyeluruh**: bukan hanya file fondasi sistem, **tetapi juga pedoman pengguna** dan semua file yang perlu diperiksa, karena penting untuk terus diperbaiki | paragraf 2 | Setuju arah, tapi **wajib berjenjang risiko** — kalau tidak, perubahan kecil memicu review raksasa dan sistem jadi tidak terpakai |
| T21 | Kalau ada **skill** yang bisa mendukung mekanisme ini, agent independen **wajib memakainya** | paragraf 2 | Kandidat terpasang: `security-review`, `verification-before-completion`, `verification-loop`, `systematic-debugging`, `web-design-guidelines`, `agent-browser`, `tdd-workflow` |
| T22 | Kalau perlu **riset internet**, agent independen **wajib melakukannya** | paragraf 2 | Perlu aturan: riset oleh reviewer **read-only terhadap branch yang direview**, dan sumber wajib dikutip (bukan diingat) |
| T23 | Mekanisme ini **harus dimatangkan dulu**; kalau butuh riset mendalam + searching internet untuk membuatnya, **silakan lakukan** | paragraf 2 | Mandat riset untuk **merancang** mekanismenya — diberikan sebelum eksekusi |
| T24 | Setelah mekanisme tertanam, **cara memakainya dijelaskan di pedoman pengguna** | paragraf 2 | Mengikat T16 dengan T18: manual book wajib memuat cara menjalankan review independen |
| T25 | **GERBANG: "sebelum eksekusi, kamu harus pastikan dulu, apakah ide aku bagus atau tidak. Jika tidak, jangan lakukan"** | paragraf 2 | **Pemilik meminta penilaian kritis, bukan pelaksanaan.** Agent **DILARANG** mengeksekusi sebelum memberi verdict jujur per ide. Ini juga sejalan dengan permintaan giliran sebelumnya: *"Aku mau kamu kritisi, bukan asal meng-iya-kan saja"* |

## Log Keputusan (lanjutan)

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Tuntutan T16–T25 dicatat + kutipan verbatim giliran 2 disimpan | Permintaan eksplisit pemilik: "pastikan ga ada yang terlupakan". T25 dicatat sebagai **gerbang**: agent tidak boleh mengeksekusi sebelum verdict jujur disampaikan |

---

# K. VERDICT JUJUR atas T16–T25 (gerbang T25: "pastikan dulu apakah ide aku bagus, jika tidak jangan lakukan")

> Bagian ini adalah **penilaian**, bukan pelaksanaan. Sesuai gerbang T25, **tidak ada mekanisme yang dieksekusi**
> sebelum pemilik memutuskan atas koreksi yang diajukan di sini.

## K.0 Fakta yang mengubah jawaban: repo ini SUDAH punya mekanismenya

Sebelum menilai, agent memeriksa apa yang sudah ada — supaya tidak mengarang mekanisme baru yang lebih lemah
dari yang sudah teruji. Hasilnya:

| Sudah ada | Isi | Bukti terpakai nyata |
|---|---|---|
| `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` (46 baris) | **8 prinsip inti** + **level trigger L1/L2/L3** + **anatomi prompt reviewer (6 bagian wajib)** + aturan penulisan hasil + **cara diwariskan ke sistem domain (3 langkah)** | Dipakai di puluhan PR; verdict MERAH/HIJAU per putaran tercatat di banyak LOG_SESI |
| `tools/review_prompt.py` (**653 baris**) | Prompt review **dibangkitkan alat, bukan dikarang** — nomor PR, base sha, head sha, daftar berkas diambil dari data PR GitHub + pohon kerja; **deterministik**; **gagal keras (exit non-zero)** daripada mencetak prompt dengan sha kosong | Menjadi sumber resmi sejak disetujui pemilik 8 Sep 2026 |
| `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` (225 baris) | QA & evolusi **3 lapis** (butir W-06) | — |
| Salinan berlabel di sistem domain | `sistem/sistem-konten-kreator/PROTOKOL_REVIEW_INDEPENDEN.md`, `sistem/sistem-presentasi/_salinan-meta/PROTOKOL_REVIEW_INDEPENDEN.md` | Preseden **cara mewarisi** ke sistem baru |

**Delapan prinsip yang sudah ada (ringkas):** (1) pemutus eksternal — yang mengerjakan tidak memutus;
(2) reviewer memverifikasi **dari artefak** (git tree, commit, log, API), **bukan dari narasi** pihak yang direview —
klaim pihak reviewed = **objek pemeriksaan, bukan bukti**; (3) reviewer tidak merge atas namanya sendiri kecuali
diizinkan eksplisit, **tidak pernah auto-merge**; (4) read-only terhadap branch orang lain; (5) batas jendela 6d;
(6) **proporsional — kedalaman mengikuti trigger, review bukan ritual untuk pekerjaan remeh**; (7) **maksimal 2
putaran**, putaran ke-2 gagal = **eskalasi ke pemilik**; (8) **append-only**, termasuk RED FLAG dan verdict yang
merevisi verdict sebelumnya — jangan dihaluskan.

**Konsekuensi untuk T18:** jawaban yang benar adalah **MEWARISI + MENGADAPTASI** protokol ini ke folder
`sistem-undangan/` (salinan berlabel, self-contained), lalu **MEMPERKUAT**nya dengan temuan riset di K.2 —
**BUKAN** menulis mekanisme baru dari nol. Mengarang baru berisiko menghasilkan mekanisme yang lebih lemah
dari yang sudah teruji di puluhan PR.

## K.1 VERDICT T16–T17 (manual book induk): **BAGUS — dilaksanakan, dengan 1 koreksi struktural**

**Bagus, dan bukan hal baru:** ini persis butir **W-01** (sudah wajib default), dan `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`
sudah menetapkan **7 bagian wajib**: (1) pembuka + penanda `agent_instruction: IGNORE for execution — USER GUIDE ONLY`,
(2) **Prompt Pembuka Universal** di paling atas, (3) **Prompt Penutup Sesi**, (4) istilah versi awam, (5) kalimat
pembuka per situasi (minimal 3), (6) cara review & merge, (7) kebiasaan yang dijaga. Preseden nyata:
`PANDUAN_PENGGUNA.md` root repo (**209 baris**). Jadi permintaan pemilik = **penguatan W-01**, bukan pekerjaan tambahan.

**⚠️ KOREKSI STRUKTURAL (wajib, kalau tidak akan menimbulkan cacat yang sudah pernah terjadi di repo ini):**
Rumusan *"cukup liat buku panduan itu dan di dalamnya udah ada semuanya"* kalau diartikan **semua ISI disalin ke
satu berkas** akan **bertabrakan dengan norma anti-dokumen-kembar** yang berlaku di repo ini. Buktinya bukan teoretis:
- Template pegangan sendiri mencatat **insiden nyata**: *"`PROMPT_ENTRI_UNIVERSAL.md` dan blok prompt di
  `PANDUAN_PENGGUNA.md` §2 **wajib identik** (dua file, satu sumber); **selisih diam-diam pernah terjadi dan jadi
  temuan audit**"*.
- INDEKS mencatat norma yang sama untuk mekanisme lain: *"Sumber mekanisme tunggal: … **sengaja tidak ada salinan
  kedua di `_meta/`** (norma anti-dokumen-kembar)"*.

Dua salinan isi yang sama **pasti** menyimpang seiring waktu, dan versi yang menyimpang itu yang akan diikuti
pengguna. **Jadi "lengkap" harus didefinisikan ulang tanpa mengorbankan maksud pemilik:**

> **Manual book = LENGKAP sebagai SATU-SATUNYA TEMPAT MENCARI, bukan sebagai satu-satunya tempat MENYIMPAN.**

Bentuk konkretnya (ini yang akan dibangun):
1. **Daftar isi + tabel "kalau kamu mau X → lihat bagian Y"** di paling atas — satu lompatan ke jawaban.
2. **SEMUA PROMPT yang dibutuhkan pemilik ada UTUH di dalam manual** (pembuka, penutup, per-situasi, prompt review
   independen) — ini bagian yang **wajib disalin utuh**, karena prompt adalah yang paling sering dibutuhkan mendadak.
   **Aturan penjaga:** prompt yang juga ada di berkas lain **wajib byte-identik** dan **dicek alat**, bukan diingat.
3. **Tiap mekanisme: ringkasan cukup untuk bertindak (kapan dipakai, apa hasilnya, apa risikonya) + pointer ke
   dokumen detailnya.** Isi teknis detail **tidak disalin** — ditunjuk.
4. **Setiap pointer wajib bisa diselesaikan** (tidak ada rujukan menggantung) — dicek alat, konsisten dengan cara
   `tools/validate_repo.py` memeriksa 369 rujukan path di repo ini.
5. **Cara menjalankan audit/review independen dijelaskan di manual** (T24) — sebagai bagian "kalau kamu mau X",
   lengkap dengan perintah dan prompt siap tempel.

**Keputusan agent:** T16–T17 **DITERIMA dengan koreksi di atas**. Maksud pemilik ("kapan pun mau cari tahu, cukup
buka satu buku") **terpenuhi sepenuhnya**; yang ditolak hanya bentuk implementasi yang akan menciptakan dokumen kembar.

## K.2 VERDICT T18–T22 (review independen sangat teliti): **ARAHNYA BENAR — tapi 3 rumusan HARUS dikoreksi**

**T18 (tanamkan mekanisme review independen): DITERIMA** — dengan cara **mewarisi** protokol yang sudah ada (K.0).

**⚠️ T19 ("sempurna tanpa terlewat hal sekecil apapun"): DITOLAK sebagai rumusan, dan ini penolakan berbasis bukti.**

Bukan karena agent tidak mau bekerja keras, tetapi karena **rumusan itu tidak bisa diuji** dan **kalau dipaksakan
akan merusak sistemnya**. Bukti dari riset (pemilik memberi mandat riset di T23):

1. **Bias reviewer AI itu SISTEMATIS, bukan kebetulan.** Penelitian menyimpulkan bias-bias ini *"not random noise but
   systematic artefacts of training"*: **position bias** (memihak yang disebut lebih dulu), **verbosity bias**
   (menganggap jawaban panjang = lebih baik), **self-preference bias** (menilai keluaran sendiri lebih tinggi —
   terdokumentasi pada GPT-4o dan Claude 3.5 Sonnet), dan **family bias** (memihak model satu penyedia).
2. **Hakim AI papan atas GAGAL menjaga konsistensi di ±25% kasus sulit** — melanggar transitivitas logika
   (memilih A>B dan B>C, lalu memilih C>A). **Flip rate 20–35%**, kesalahan verbosity >20%.
3. **Perubahan kecil pada susunan kata prompt bisa mengubah hasil** (sensitivitas in-context learning).
4. **Uji akademis independen: semua alat review AI melewatkan sebagian besar kerentanan nyata.** Dan
   **71% developer tetap tidak mau merge kode AI tanpa review manusia.** Tidak ada benchmark yang mendukung
   kesimpulan bahwa review AI bisa menggantikan review manusia.
5. **⚠️ BAHAYA TERBESAR dari menuntut "jangan sampai ada yang terlewat": EFEK SERIGALA MENANGIS (cry-wolf).**
   Ini terdokumentasi sebagai *"the most common reason teams abandon these tools"*. Mekanismenya: supaya terlihat
   teliti, reviewer memperbanyak temuan → **positif palsu naik** → pemilik belajar **mengabaikan semua temuan tanpa
   membaca** → **masalah yang asli ikut terlewat**. Sebagai pembanding nyata: generasi awal alat review AI
   menghasilkan **9 positif palsu untuk setiap 1 bug asli**, dan itu *"destroys trust"*. Analisis statis mentah bisa
   mencapai **>90% positif palsu** di beberapa benchmark akademis.

**Konflik dengan aturan repo yang sudah terbukti (WAJIB dilaporkan, tidak boleh ditebak/ditimpa diam-diam):**
T19 versi harfiah **bertentangan langsung** dengan prinsip **#6 (Proporsional — "review bukan ritual untuk pekerjaan
remeh")** dan **#7 (maksimal 2 putaran, lalu eskalasi ke pemilik)** pada `PROTOKOL_REVIEW_INDEPENDEN.md` yang sudah
teruji di puluhan PR. Aturan repo sendiri memerintahkan: *"konflik tetap harus dilaporkan, bukan ditebak"*.
**Agent tidak akan menimpa prinsip #6/#7 tanpa keputusan eksplisit pemilik.**

**✅ PENGGANTI yang mencapai MAKSUD pemilik (ketelitian nyata) tanpa bahayanya:**
"Tanpa terlewat" diterjemahkan dari **kata sifat** menjadi **cakupan yang dideklarasikan dan bisa diverifikasi ulang**:
- Reviewer **wajib melaporkan cakupan satu-satu**: berkas apa saja yang diperiksa, pemeriksaan apa yang dijalankan,
  dan **hasilnya apa** — bukan kesimpulan umum "sudah saya periksa semua".
- Reviewer **wajib menyatakan yang TIDAK diperiksa beserta alasannya.** Kejujuran cakupan menggantikan klaim kesempurnaan.
- Setiap temuan **wajib disertai perintah reproduksi** (sudah jadi aturan repo: "merah → laporkan + perintah reproduksi").
- **Kedalaman berjenjang risiko** (L1/L2/L3 diwarisi, lalu diberi isi konkret untuk domain undangan — lihat K.3).

**⚠️ T20 (cakupan menyeluruh termasuk pedoman pengguna): DITERIMA — dan ini justru menutup GAP nyata di protokol yang ada.**
Daftar L1 protokol saat ini berfokus pada aturan/manifest/riwayat; **pedoman pengguna tidak disebut eksplisit**.
Permintaan pemilik **benar dan bernilai**, karena **instruksi yang salah di manual lebih berbahaya daripada dokumen
salah di tempat lain** — pengguna **bertindak** berdasarkan manual. Insiden "selisih diam-diam" dua berkas prompt
(K.1) membuktikan risiko ini nyata, bukan hipotetis. **Maka: pedoman pengguna MASUK cakupan L1**, dengan 2 pemeriksaan
khusus yang bisa dimekanisasi: (a) **prompt di manual byte-identik dengan sumbernya**, (b) **setiap pointer di manual
bisa diselesaikan**.

**✅ T21 (wajib pakai skill yang mendukung): DITERIMA.** Kandidat dari 56 skill terpasang: `security-review`
(auth, input pengguna, secrets, endpoint, pembayaran), `verification-before-completion` (**melarang klaim sukses
sebelum menjalankan verifikasi** — persis anti-klaim kosong), `verification-loop`, `systematic-debugging`,
`web-design-guidelines` (audit aksesibilitas/UX), `agent-browser` (**bukti runtime**: screenshot undangan di
berbagai ukuran layar), `tdd-workflow`/`test-driven-development`. Riset skill tambahan digabung ke scope riset 8 gap.

**✅ T22 (wajib riset internet bila perlu): DITERIMA, dengan 2 pagar** — (a) riset reviewer **read-only terhadap
branch yang direview** (prinsip #4 yang sudah ada), (b) **sumber wajib dikutip sebagai URL dan disimpan ke berkas**,
bukan diingat dan bukan diringkas bebas (preseden: bagian A–J berkas ini).

## K.3 EMPAT penguatan dari riset yang akan ditanam (ini jawaban atas "supaya betul-betul jeli")

Ketelitian **tidak bisa diperintahkan lewat kata sifat**; yang bisa adalah **memberi alat + memaksa verifikasi**.
Empat mekanisme dengan bukti terkuat:

1. **VERIFIKASI ADVERSARIAL — reviewer WAJIB mencoba MEMBANTAH temuannya sendiri dulu.** Ini temuan paling
   berdampak: hanya temuan yang **selamat dari pembantahan** yang boleh masuk laporan. Bukti angkanya: generasi awal
   alat AI menghasilkan **9 positif palsu per 1 bug asli**; dengan lapisan verifikasi, positif palsu yang ditolak
   developer turun ke **<1%**. Diterjemahkan ke aturan sistem: *setiap temuan wajib diuji ulang dengan perintah/berkas
   nyata sebelum dilaporkan; kalau tidak bisa direproduksi, temuan itu DIBUANG, bukan dilemahkan.*
2. **AI paling terbukti berguna untuk MEMBUNUH DERAU, bukan untuk mendeteksi.** Bukti terkuat: penyaringan ulang
   oleh LLM memangkas positif palsu analisis statis dari **>92% menjadi serendah 6,3%**. Maka reviewer dipakai sebagai
   **lapis saring** atas keluaran alat mekanis (validator, preflight, screenshot) — bukan sebagai sumber kebenaran tunggal.
3. **HAKIM HARUS DARI KELUARGA MODEL YANG BERBEDA dari pembuatnya** — mitigasi terdokumentasi untuk self-preference
   dan family bias. Aturan repo sudah mewajibkan **sesi berbeda**; yang **ditambahkan**: **model reviewer dicatat di
   verdict**, supaya bias satu-keluarga bisa dikenali kemudian. (Pemilik bisa memilih model di Arena.)
4. **VERIFIKASI RUNTIME MENGALAHKAN REVIEW BACA-SAJA.** Bukti: review yang hanya membaca kode **melewatkan** masalah
   yang baru terlihat saat alur dijalankan, dan **menuduh** hal yang tampak berbahaya tapi sebenarnya tidak bisa
   dieksploitasi. Diterjemahkan ke domain undangan: reviewer **WAJIB menjalankan** validator/preflight dan **MEMBUKA**
   undangan yang sudah dirender (screenshot HP + tablet + PC via `agent-browser`), **bukan hanya membaca dokumen**.
   Ini juga yang membuat prinsip #2 ("verifikasi dari artefak, bukan narasi") jadi konkret dan bisa ditaati.

**Tambahan: temuan wajib menjelaskan MENGAPA, bukan hanya BAHWA.** Alat yang menampilkan alasan (*"explaining why a
pattern is problematic, not just that it is"*) mendapat tingkat penyelesaian temuan **jauh lebih tinggi**; tanpa itu,
pengguna tidak nyaman mengandalkan temuan yang konsekuensial.

## K.4 SATU hal yang tidak diminta pemilik tetapi WAJIB diwarisi: pengecualian pengadil

Kalau yang diubah adalah **mekanisme review itu sendiri**, reviewer **dilarang merge** walau seluruh pemeriksaan lulus.
Preseden nyata di repo ini: **PR #56 dibiarkan `OPEN` bukan karena cacat** — verdict review putaran 2/2 **nihil temuan**
— melainkan **semata-mata karena PR itu menyentuh alat pengadil** (`tools/review_prompt.py`,
`tools/test_failure_injection.py`); merge tetap keputusan pemilik. **Alasannya kausal:** pengadil tidak boleh
memutuskan nasib aturan yang memberi wewenang kepada pengadil itu. **Wajib diwarisi ke sistem-undangan.**

## K.5 RINGKASAN VERDICT (untuk keputusan pemilik)

| Tuntutan | Verdict | Yang berubah |
|---|---|---|
| T16 manual book induk lengkap | ✅ **BAGUS — dilaksanakan** | Sudah = W-01 + template 7 bagian; **diperkuat** jadi manual induk |
| T17 "semuanya ada di dalam satu buku" | ⚠️ **BAGUS maksudnya, SALAH bentuknya** | Dikoreksi: **lengkap sebagai tempat MENCARI, bukan tempat MENYIMPAN** — semua **prompt** utuh di dalam, isi teknis **ditunjuk** bukan disalin (norma anti-dokumen-kembar + insiden selisih diam-diam yang sudah pernah jadi temuan audit) |
| T18 tanamkan review independen | ✅ **BAGUS — dilaksanakan** | **Mewarisi** protokol + alat yang sudah ada, **bukan** mengarang baru |
| T19 "sempurna tanpa terlewat sekecil apa pun" | ❌ **DITOLAK sebagai rumusan** | Tidak bisa diuji; memicu **cry-wolf** (>90% positif palsu di alat mentah; 9 positif palsu per bug di generasi awal); **bertentangan dengan prinsip #6 & #7 yang sudah teruji**. Diganti: **cakupan terdefinisi + wajib menyatakan yang TIDAK diperiksa + perintah reproduksi per temuan** |
| T20 cakupan termasuk pedoman pengguna | ✅ **BAGUS — menutup gap nyata** | Pedoman pengguna **masuk L1** + 2 cek mekanis (prompt byte-identik, pointer terselesaikan) |
| T21 wajib pakai skill | ✅ **BAGUS** | 7 skill terpasang dipetakan; riset tambahan digabung ke 8 gap |
| T22 wajib riset internet | ✅ **BAGUS + 2 pagar** | read-only terhadap branch yang direview; sumber dikutip sebagai URL dan disimpan ke berkas |
| T23 matangkan dulu + mandat riset | ✅ **DILAKSANAKAN** | Bagian K ini adalah hasil maturasi + riset itu |
| T24 cara pakai dijelaskan di manual | ✅ **BAGUS** | Mengikat T16 ↔ T18: manual wajib memuat cara menjalankan review |
| T25 gerbang: nilai dulu sebelum eksekusi | ✅ **DIPATUHI** | **Tidak ada mekanisme yang dieksekusi.** Bagian K ini adalah verdict-nya; eksekusi menunggu keputusan pemilik |
| *(tidak diminta)* pengecualian pengadil | ➕ **WAJIB diwarisi** | Preseden PR #56: pengadil tidak boleh memutus nasib aturan yang memberinya wewenang |

## Log Keputusan (lanjutan)

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Bagian K (verdict) ditulis; **T19 ditolak sebagai rumusan**, T17 dikoreksi bentuknya, sisanya diterima | Gerbang T25 pemilik: *"sebelum eksekusi, kamu harus pastikan dulu, apakah ide aku bagus atau tidak. Jika tidak, jangan lakukan"* — dan permintaan giliran sebelumnya: *"Aku mau kamu kritisi, bukan asal meng-iya-kan saja"* |
| 2026-09-17 | Konflik T19 vs prinsip #6/#6–#7 `PROTOKOL_REVIEW_INDEPENDEN.md` **DILAPORKAN, tidak ditimpa** | Aturan repo: *"konflik tetap harus dilaporkan, bukan ditebak"*; menimpa prinsip yang sudah teruji di puluhan PR tanpa keputusan eksplisit pemilik = pelanggaran |
| 2026-09-17 | Keputusan: **mewarisi** protokol + `tools/review_prompt.py`, bukan menulis mekanisme baru | Mekanisme yang ada lebih canggih dari yang dibayangkan (prompt dibangkitkan alat, deterministik, gagal keras, larangan pihak yang direview mengarang prompt pengadilnya sendiri); mengarang baru berisiko lebih lemah |
| 2026-09-17 | 4 penguatan berbasis riset dicatat sebagai kandidat aturan: verifikasi adversarial, AI sebagai penyaring derau, model reviewer beda keluarga + dicatat, verifikasi runtime wajib | Semuanya punya bukti angka, bukan preferensi gaya |

---

## Giliran 3 — 2026-09-17: persetujuan bersyarat + KOREKSI PEMILIK atas klaim agent + 2 tuntutan baru + 1 anekdot

> **Kutipan UTUH tanpa suntingan.** Pemilik membuka dengan: *"Jawaban nya panjang, pastikan ga ada yang
> terlupakan dan terlewat."* Tanda kutip ganda di dalam kutipan adalah milik pemilik (menyoroti klaim agent).

Jawaban nya panjang, pastikan ga ada yang terlupakan dan terlewat.

1. Klo memang itu yang terbaik, aku setuju. Tapi aku harus sampaikan sebuah info. DI sebuah sistem lain, aku pernah mengalami hal berikut. Aku udh liat buku panduan pengguna. Aku berterimakasih karena dia udh membuatnya lebih lengkap. Tapi harus aku katakan bahwa isi nya masih banyak kurang dan cacat. Di antara nya adalah banyak hal berkaitan cara tidak disertakan di situ. Misalnya cara jika pengguna mau melakukan audit independen (dia hanya nyediakan prompt tapi ga ngasih panduan nya), cara ketika auditor independen udh ngasih hasil (dia juga cuma ngasih prompt nya), cara ketika mau pekerjaan lama diulang (dia juga cuma tulis prompt nya), ada juga Perintah mesin yang boleh pengguna minta agent jalankan (disebut dan ditulis rapi dalam tabel tapi ga dijelasin fungsi dan cara pake nya). Bahkan aku juga merasa curiga, aku menduga ada beberapa prompt yang justru isi kata-katanya bukan ditujukan untuk agent, melainkan untuk pengguna. Dan masih banyak lagi masalah yang lain. Sehingga waktu itu Aku minta dia baca ulang semuanya dan perbaiki lagi semuanya. Pastikan lebih sistematis, lebih mudah dipahami, semua fungsi dan tujuan serta caranya dijelasin dengan bahasa yang mudah buat aku pahami.
2. Aku kurang paham soal hal tersebut. Aku minta yang terbaik dari kamu.
3. Ya, lakukan yang terbaik.



Kamu bilang "**Hal pertama yang harus kamu tahu: mekanisme ini SUDAH ADA di repomu, dan lebih canggih dari yang kamu gambarkan**". Tapi yang aku tau, yang udh ada itu mekanisme review PR. Dan memang aku mau itu juga ditanam. Tapi yang aku maksud saat ini adalah mekanisme review isi repo, isi sistem, dan semua hal yang perlu diperiksa. Bukan soal PR dan bukan soal merge. Paham kan maksud aku? Apakah aku salah? Klo salah sampaikan aja. Aku lebih suka diluruskan jika memang salah, dan dibenarkan jika memang benar, bukan asal diiyakan saja. 

Dan untuk mekanisme audit ini (baik audit/review PR maupun yang bukan PR), aku mau itu dibuat otomatis terkirim ke github, sehingga ketika review/audit udh selesai, aku ga perlu laporin hasilnya ke agent sesi yang lagi jalan (yang meniapan review/audit independen), melainkan aku cukup bilang bahwa review/audit udh selesai, dan dia otomatis tau semua hasilnya.



Aku juga mau ceritakan satu hal. Sempat terjadi di sebuah sesi,..

salah satu sesi review independen bilang begini:

```
Saya baca dulu aturan pemeriksa laporan supaya laporannya memenuhi syarat tanpa melebih-lebihkan cakupan.
```

Aku merasa janggal. Aku rasa seharusnya jika memang ada yang perlu dilaporkan maka seharusnya itu tetap dilaporkan biarpun tidak masuk dalam cakupan yang diminta. Iya kan? Apakah aku yang salah paham atau gimana ya? Coba tolong pastikan.

## Peta tuntutan giliran 3 (ekstraksi agent)

| # | Tuntutan/pernyataan pemilik | Catatan agent |
|---|---|---|
| T26 | **T17 disetujui** ("Klo memang itu yang terbaik, aku setuju") — **tetapi disertai bukti pengalaman nyata** dari sistem lain: pedoman yang "sudah lebih lengkap" pun **masih banyak kurang dan cacat** | Ini **bukti empiris** bahwa koreksi agent di K.1 **belum cukup**. Daftar cacat yang dilaporkan pemilik jadi **daftar periksa wajib** untuk manual sistem-undangan |
| T26a | Cacat #1: **banyak "cara" tidak disertakan** — contoh konkret: cara melakukan audit independen (**hanya diberi prompt, tanpa panduan**), cara ketika auditor sudah memberi hasil (**hanya prompt**), cara mengulang pekerjaan lama (**hanya prompt**) | Pola cacatnya spesifik: **prompt tanpa prosedur**. Prompt = apa yang ditempel; prosedur = langkah sebelum/sesudah, apa yang diharapkan, apa yang dilakukan kalau gagal |
| T26b | Cacat #2: **perintah mesin yang boleh diminta pengguna** ditulis rapi dalam tabel **tetapi tidak dijelaskan fungsi dan cara pakainya** | Tabel perintah tanpa kolom "untuk apa" + "kapan dipakai" + "apa yang terjadi kalau gagal" = tidak bisa dipakai orang awam |
| T26c | Cacat #3 (kecurigaan pemilik): **ada prompt yang kata-katanya justru ditujukan untuk PENGGUNA, bukan untuk AGENT** | ⚠️ Cacat serius dan **bisa dideteksi mekanis**: prompt yang ditempel ke agent wajib berkalimat perintah ke agent ("baca…", "verifikasi…", "laporkan…"), bukan kalimat ke manusia ("kamu bisa…", "silakan…") |
| T26d | **Instruksi pemilik:** agent wajib **baca ulang semuanya dan perbaiki semuanya** — lebih sistematis, lebih mudah dipahami, **semua fungsi + tujuan + cara dijelaskan dengan bahasa yang mudah dipahami pemilik** | Standar kelulusan manual: **bukan "lengkap"**, tetapi **"bisa dipakai orang awam tanpa bertanya lagi"** |
| T27 | Poin 2 (keputusan atas penolakan T19 / override prinsip #6&#7) **didelegasikan**: *"Aku kurang paham soal hal tersebut. Aku minta yang terbaik dari kamu."* | Agent memutuskan; wajib melaporkan alasan + tetap boleh dibalik pemilik |
| T28 | Poin 3 **disetujui**: *"Ya, lakukan yang terbaik."* → riset 8 gap skill + skill pendukung audit dijalankan | Scope riset diperluas: termasuk skill pendukung mekanisme audit/review (T21) |
| T29 | **KOREKSI PEMILIK atas klaim agent:** yang sudah ada itu **mekanisme review PR**; yang pemilik maksud adalah **mekanisme review ISI repo, ISI sistem, dan semua hal yang perlu diperiksa — bukan soal PR dan bukan soal merge**. Pemilik meminta dinilai jujur: *"Apakah aku salah? Klo salah sampaikan aja. Aku lebih suka diluruskan jika memang salah, dan dibenarkan jika memang benar, bukan asal diiyakan saja."* | ⚠️ **Klaim agent di K.0 harus diuji ulang terhadap dokumen, bukan dibela.** Agent wajib membaca `QUALITY_ASSURANCE_AND_EVOLUTION.md`, `_meta/ACCEPTANCE_TESTS.md`, `_meta/FAILURE_INJECTION_TESTS.md`, arsip `AUDIT_*`, dan mekanisme audit Sistem Klinik sebelum menjawab |
| T30 | **TUNTUTAN BARU:** hasil audit/review (**baik PR maupun non-PR**) **otomatis terkirim ke GitHub**, sehingga pemilik **tidak perlu melaporkan hasil ke sesi yang sedang berjalan** — cukup bilang "review/audit sudah selesai", dan sesi itu **otomatis tahu semua hasilnya** | Butuh: kanal publikasi hasil + **mekanisme penemuan otomatis** oleh sesi penulis. Sebagian kecil sudah dipraktikkan (verdict sebagai komentar PR), tetapi **pengambilan otomatis oleh sesi penulis belum ada** |
| T31 | **ANEKDOT + permintaan verifikasi:** sebuah sesi review independen berkata *"Saya baca dulu aturan pemeriksa laporan supaya laporannya memenuhi syarat tanpa melebih-lebihkan cakupan."* Pemilik merasa **janggal**: *"seharusnya jika memang ada yang perlu dilaporkan maka seharusnya itu tetap dilaporkan biarpun tidak masuk dalam cakupan yang diminta. Iya kan? Apakah aku yang salah paham atau gimana ya? Coba tolong pastikan."* | Harus dijawab tegas: **pemilik benar atau salah?** Agent wajib memilah dua makna kalimat itu dan memberi aturan yang tidak ambigu |

## Log Keputusan (lanjutan)

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Giliran 3 disimpan verbatim + T26–T31 dipetakan | Permintaan pemilik: "pastikan ga ada yang terlupakan dan terlewat" |
| 2026-09-17 | **T29 dicatat sebagai KOREKSI atas klaim agent di K.0** — agent wajib menguji ulang klaimnya terhadap dokumen sebelum menjawab, dan **wajib mengakui kalau over-claim** | Pemilik meminta diluruskan kalau salah; norma repo: konflik/kesalahan dilaporkan, bukan dihaluskan (prinsip #8 append-only, "jangan menghaluskan") |

---

# L. VERDICT atas T26–T31 — termasuk KOREKSI atas klaim agent sendiri

## L.1 T29 — **PEMILIK BENAR. Klaim agent di K.0 OVER-CLAIM dan dikoreksi di sini.**

Agent menulis: *"mekanisme ini SUDAH ADA di repomu, dan lebih canggih dari yang kamu gambarkan"* sambil menunjuk
`PROTOKOL_REVIEW_INDEPENDEN.md` + `tools/review_prompt.py`. **Itu keliru untuk maksud pemilik**, dan pemilik
benar menangkapnya. Bukti dari dokumen, bukan dari ingatan:

- **Protokol itu memang terikat PR.** Bagian "Anatomi prompt reviewer (wajib berisi)" butir 2 mensyaratkan
  **"Objek ter-pin: nomor PR + SHA basis + SHA head"**. Butir mekanika putusannya berbicara tentang **merge**.
- **Alatnya juga terikat PR.** `tools/review_prompt.py` hanya punya `--pr <N>`, `--generic`, `--out`
  (diperiksa langsung dari `add_argument` di baris 616–618). **Tidak ada mode audit isi.** Kalau tidak ada PR,
  alat itu bahkan berhenti dan menyuruh menulis nomor PR manual (baris 198–220).

**Jadi: untuk "review ISI repo/sistem, bukan PR dan bukan merge", mekanisme yang agent tunjuk TIDAK berlaku.
Pemilik tidak salah paham. Agent yang menyamakan dua hal berbeda.**

### Tetapi — supaya koreksinya juga akurat: mekanisme audit ISI **memang ada**, hanya **tidak terpadu**

Ini bagian yang tetap benar dari K.0, dan penting supaya tidak dibangun duplikat:

| Sudah ada untuk audit ISI | Isi | Bukti pernah dijalankan |
|---|---|---|
| `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` (226 baris) | **QA 3 lapis**: (1) meta-sistem, (2) sistem domain memeriksa dirinya, (3) verifikasi output. **Kedalaman berbasis risiko**: Ringan / Sedang / Mendalam. **7 LENSA AUDIT** (dikodifikasi 5 Sep 2026, temuan M-08). **Klasifikasi temuan WAJIB**: `B` bug / `A` ambiguitas / `G` gap proses / `N` kebutuhan baru / `P` preferensi-housekeeping, **+ prioritas P1–P3 + dasar bukti**. **Batasan anti-recursion**: objek, trigger, kedalaman, acceptance criteria, **kondisi berhenti**, pemilik approval. **Regression check wajib** 7 pertanyaan. **Rollback** 7 langkah | 8 arsip audit nyata di `_meta/_internal/`: `AUDIT_META_SISTEM_2026-09-03/05/09`, `AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03`, `AUDIT_SISTEM_PRESENTASI_2026-09-05`, `BEHAVIORAL_AUDIT_2026-09-03`, `BEHAVIORAL_AUDIT_2026-09-04_PILOT_002`, `REGRESSION_AUDIT_2026-09-03` |
| `_meta/ACCEPTANCE_TESTS.md` + `_meta/FAILURE_INJECTION_TESTS.md` + `_meta/DEFINITION_OF_DONE.md` | uji perilaku, uji jalur gagal, kriteria selesai | dijalankan alat: `test_failure_injection.py` (73 skenario, PASS di sesi ini) |
| `tools/` (5 alat) | `validate_repo.py` · `check_selfcontained.py` · `test_failure_injection.py` · `build_template.py` · `backup_verify.py` | semua PASS diukur di sesi ini |
| **Sistem Klinik** (`sistem/sistem-klinik/_sistem/`) | `01_ALUR_RUN.md` · **`02_KATALOG_CACAT.md`** · `03_KEBIJAKAN_LEBUR.md` · `04_KONTRAK_TANAMAN.md` · `05_TAWARAN_KAPABILITAS.md` · `06_RITME_KIT.md` · `validate_system.py` | run ke-2 = **"audit menyeluruh seluruh berkas folder atas permintaan pemilik"** (PR #63) |

**Catatan penting untuk T26:** lensa audit **#5** sudah persis tentang keluhan pemilik —
**"Kemudahan pakai (kacamata pengguna awam) — cukup satu prompt? Apakah dokumen yang ditempel pengguna adalah
versi terbaru?"**, dengan contoh nyata terdokumentasi: *"prompt pembuka PANDUAN vs entry point 00 berbeda langkah
— M-05/M-15"*. **Jadi repo ini SUDAH punya lensanya; sistem lain yang pemilik ceritakan gagal MENERAPKANNYA.**

### Yang BENAR-BENAR BELUM ADA (permintaan pemilik valid dan baru)

1. **Tidak ada prompt audit-isi yang DIBANGKITKAN ALAT.** `review_prompt.py` membangkitkan prompt review **PR**;
   **tidak ada padanannya untuk audit isi** yang mem-pin objek (folder/sistem, sha commit, daftar berkas).
   **Akibatnya fatal dan persis yang alat itu dibuat untuk mencegah:** hari ini prompt audit isi harus **dikarang
   tangan** — artinya **pihak yang diaudit menulis instruksi untuk pengadilnya sendiri**. Prinsip yang sudah ada
   (*"pihak yang direview TIDAK boleh mengarang/menambah/memotong/menyunting prompt review untuk dirinya sendiri"*)
   **tidak bisa ditaati** untuk audit isi karena alatnya belum ada.
2. **Tidak ada pengiriman/pengambilan hasil secara otomatis (T30)** — baik untuk PR maupun non-PR. Praktik yang
   ada: verdict diterbitkan sebagai **satu komentar PR** (terdokumentasi di `_log-sesi/LOG_SESI_2026-09-16_7.md`),
   tetapi **pengambilan otomatis oleh sesi penulis belum ada** — pemilik yang harus memberi tahu.
3. **Sistem Klinik terlalu berat untuk kebutuhan ini.** Klinik adalah **run perawatan** (diagnosis → rencana →
   tindakan → verifikasi → catatan → panen) dengan gerbang **G-Rencana** & **G-Final** dan katalog cacat — dirancang
   untuk **MEMPERBAIKI** sistem. Yang pemilik mau juga mencakup mode **ringan**: "audit isi → laporkan temuan",
   tanpa wajib masuk jalur tindakan.

**Keputusan agent:** warisi **7 lensa + klasifikasi B/A/G/N/P + prioritas P1–P3 + kedalaman berbasis risiko +
batas anti-recursion** dari protokol QA yang sudah ada, lalu **BANGUN 3 hal yang belum ada** di atas.
**Bukan** menulis mekanisme audit baru dari nol (itu akan lebih lemah dari yang sudah teruji), dan **bukan**
mengklaim yang sudah ada itu cukup (itu over-claim yang sudah dikoreksi).

## L.2 T30 — hasil audit otomatis terkirim ke GitHub: **DITERIMA, rancangan konkret**

**Yang sudah ada (sebagian):** verdict sebagai **satu komentar PR** — sudah jadi praktik nyata.
**Yang belum ada:** (a) **pengambilan otomatis** oleh sesi yang sedang berjalan, (b) **kanal untuk audit non-PR**.

**Rancangan yang diusulkan (belum dieksekusi — menunggu keputusan pemilik):**

1. **Kanal audit non-PR = GitHub ISSUE, satu issue per run audit.** Alasan memilih issue (bukan branch/gist):
   `api.github.com` **terjangkau dan terautentikasi** dari sandbox (diverifikasi: `gh api rate_limit` → sisa 4.984),
   punya **URL permanen** yang bisa pemilik buka, mendukung **komentar append** (cocok untuk putaran 2),
   dan **bisa diambil mekanis** dengan `gh issue view --comments`.
2. **Konvensi penemuan otomatis** supaya tidak perlu diberi tahu: **label tetap** (mis. `audit-independen`) +
   **pola judul tetap** yang memuat **objek + sha** (mis. `AUDIT sistem-undangan @<sha>`). Dengan konvensi itu,
   sesi penulis cukup mengambil **verdict terbaru** tanpa pemilik menyebutkan nomor/URL.
3. **Alat pengambil** (analog `review_prompt.py`, mis. `tools/ambil_verdict.py --terbaru`): mencetak verdict +
   seluruh temuan + status putaran. **Alur pemilik jadi satu kalimat**: pemilik bilang *"review/audit sudah selesai"*
   → sesi menjalankan alat itu → **otomatis tahu semua hasilnya**, tanpa pemilik menyalin apa pun. **Ini persis
   yang diminta T30.**
4. **Untuk audit PR:** tetap pakai komentar PR (sudah terbukti), dan alat pengambil yang sama membaca
   `gh pr view --comments`. **Satu alat, dua kanal** — menghindari dokumen/alat kembar.
5. **Pagar yang WAJIB ikut diwarisi:** prinsip **#5 batas jendela (6d)** tetap berlaku — selama jendela run/uji
   terbuka, artefak yang dipublikasikan reviewer **tidak boleh memuat rumusan jawaban/kriteria yang belum tertutup
   uji**; pakai pointer SHA+baris. Kanal otomatis **tidak boleh** jadi jalan bocor untuk itu.
6. **Batas kejujuran:** `gh issue create` **belum diuji** di sesi ini (menguji = membuat artefak nyata di repo,
   butuh izin pemilik). Yang sudah diverifikasi baru **kemampuan baca** (`gh api`, `gh pr view`).

## L.3 T31 — anekdot "tanpa melebih-lebihkan cakupan": **PEMILIK BENAR.**

Kalimat reviewer itu: *"Saya baca dulu aturan pemeriksa laporan supaya laporannya memenuhi syarat tanpa
melebih-lebihkan cakupan."* Kalimat ini **ambigu**, dan **kejanggulan pemilik sah**:

- **Makna terbaik (benar):** reviewer tidak mau **MENGKLAIM** cakupan lebih luas dari yang benar-benar dikerjakan.
  Itu disiplin kejujuran yang **memang diwajibkan** repo ini.
- **Makna terburuk (berbahaya):** reviewer akan **menyaring/membuang** temuan supaya laporan "muat" dalam cakupan
  yang diminta. **Ini yang pemilik khawatirkan, dan kekhawatiran itu benar.**

Agent **tidak bisa memastikan niat reviewer** dari satu kalimat — jadi yang agent putuskan adalah **aturannya**,
supaya ambiguitas ini tidak bisa muncul lagi:

> ### ATURAN CAKUPAN (dikunci sebagai calon aturan sistem)
> **Cakupan membatasi RENCANA PENCARIAN dan KLAIM. Cakupan TIDAK PERNAH membatasi LAPORAN.**
>
> - **Yang dibatasi cakupan:** apa yang dicari **secara sistematis** (checklist wajib), dan apa yang boleh
>   **DIKLAIM** sudah diperiksa.
> - **Yang TIDAK BOLEH dibatasi cakupan:** apa yang boleh **DILAPORKAN**.
> - **WAJIB:** temuan di luar cakupan **tetap dilaporkan**, diberi label **"di luar cakupan"**, lengkap dengan
>   klasifikasi `B/A/G/N/P` + prioritas `P1–P3` + **dasar bukti**.
> - **DILARANG:** (a) **mengklaim** cakupan lebih luas dari yang dikerjakan; (b) **membuang atau menghaluskan**
>   temuan karena tidak diminta; (c) **bertindak/memperbaiki** atas temuan di luar cakupan **tanpa mandat**
>   — karena **menemukan ≠ memperbaiki** (prinsip QA #2: *"Pemeriksaan tidak sama dengan perubahan"*).
> - **WAJIB:** kalau reviewer menyadari telah membaca sesuatu di luar jalur yang diizinkan → **ungkapkan
>   (disclosure)**, jangan disembunyikan.

**Aturan ini bukan karangan agent — repo ini sudah mempraktikkannya, dan itu bukti terkuat bahwa pemilik benar:**

| Preseden di repo ini | Apa yang terjadi |
|---|---|
| `_log-sesi/LOG_SESI_2026-09-15_3.md` | *"Log OPEN-basi milik sesi lain **DITEMUKAN tapi TIDAK DISENTUH** (aturan sesi ini): hanya **dicatat di log ini + dilaporkan**"* → temuan di luar cakupan **dilaporkan**, tidak dibuang, tidak ditindak |
| `_log-sesi/LOG_SESI_2026-09-16_11.md` + body PR #35 | **"disklor paparan"**: sesi **mengungkapkan** bahwa ia membuka berkas di luar jalur baca wajib **sebelum** keputusan pertama ter-commit → **diungkapkan, bukan disembunyikan** |
| `_meta/_internal/HOUSEKEEPING_2026-09-16.md` | Sesi menemukan **5 branch diverged + log OPEN milik sesi lain** di luar mandatnya → **dilaporkan lengkap dengan rekomendasi**, tanpa menghapus/menindak apa pun |
| `QUALITY_ASSURANCE_AND_EVOLUTION.md` | *"Temuan tanpa bukti terverifikasi **dicatat sebagai 'dugaan'** dan tidak boleh langsung jadi perbaikan"* → temuan lemah pun **dicatat**, bukan dibuang |
| Skema klasifikasi `B/A/G/N/P` | Adanya kategori **`N` (kebutuhan baru)** dan **`P` (preferensi/housekeeping)** = **slot struktural** untuk temuan yang bukan objek utama. Skema ini **hanya masuk akal** kalau temuan di luar cakupan memang **ditampung** |
| Prinsip #8 protokol review | **append-only**, *"jangan menghapus riwayat, **jangan menghaluskan**"* |

**Kesimpulan untuk pemilik: kamu TIDAK salah paham. Prinsipmu benar dan sudah jadi praktik di repo ini.**
Yang salah adalah **kalimat reviewer itu** — paling ringan: **dirumuskan buruk** sehingga terdengar seperti
penyaringan; paling berat: **sinyal bahwa temuan akan disaring**. Dua-duanya layak dijadikan temuan.

## L.4 T26 — bukti lapangan pemilik jadi **DAFTAR PERIKSA WAJIB** manual book

Koreksi agent di K.1 ("lengkap = tempat mencari, bukan menyimpan") **belum cukup**. Pengalaman pemilik di sistem
lain membuktikan ada **kelas cacat yang tidak tertangkap** oleh koreksi itu. Keempat cacat yang dilaporkan pemilik
diubah jadi **syarat kelulusan**:

| Cacat yang dilaporkan pemilik (bukti lapangan) | Syarat kelulusan yang ditanam | Bisa dicek mekanis? |
|---|---|---|
| **Prompt tanpa prosedur** — cara audit independen, cara setelah auditor memberi hasil, cara mengulang pekerjaan lama: **hanya diberi prompt** | **Setiap mekanisme wajib punya 6 bidang:** (1) **Apa** itu, (2) **Kapan** dipakai, (3) **Cara** — langkah bernomor, (4) **Prompt siap tempel**, (5) **Apa yang terjadi sesudahnya**, (6) **Kalau gagal bagaimana**. Prompt tanpa 5 bidang lainnya = **cacat** | ✅ sebagian — kehadiran 6 bidang bisa dihitung alat |
| **Tabel perintah tanpa penjelasan** — ditulis rapi tapi **fungsi dan cara pakainya tidak dijelaskan** | **Setiap perintah mesin wajib punya 5 kolom:** perintah · **fungsi (untuk apa)** · **kapan dipakai** · **keluaran yang diharapkan** · **kalau gagal** | ✅ kehadiran kolom bisa dihitung alat |
| **Prompt yang kata-katanya ditujukan ke PENGGUNA, bukan ke AGENT** (kecurigaan pemilik) | **Aturan arah bicara:** blok prompt yang akan **ditempel ke agent** wajib berkalimat **perintah ke agent** ("baca…", "verifikasi…", "laporkan…", "jangan…"). **Dilarang** berkalimat ke manusia ("kamu bisa…", "silakan…", "anda akan…"). **Alasan kausal:** prompt yang salah arah membuat agent mengira sedang membaca penjelasan, bukan instruksi — dan agent bisa **tidak mengerjakan apa pun** | ✅ **bisa dideteksi lint** (pola kata) — kandidat cek validator baru |
| *"dan masih banyak lagi masalah yang lain"* | **Standar kelulusan manual BUKAN "lengkap", melainkan: "bisa dipakai orang awam tanpa bertanya lagi."** Dan **tidak boleh dinyatakan sendiri oleh penulisnya** — wajib **diaudit sesi independen dengan lensa #5** (kacamata pengguna awam) | ⚠️ sebagian — sisanya penilaian manusia |

**Instruksi pemilik yang mengikat (T26d):** *"baca ulang semuanya dan perbaiki lagi semuanya … lebih sistematis,
lebih mudah dipahami, semua fungsi dan tujuan serta caranya dijelasin dengan bahasa yang mudah buat aku pahami."*
→ Ini jadi **gerbang G0-manual**: manual tidak boleh dinyatakan selesai sebelum (a) 4 syarat di atas lulus,
(b) **diuji pakai nyata** oleh pemilik dengan menjalankan 1 alur dari manual tanpa bertanya, dan (c) **diaudit
lensa #5 oleh sesi independen**.

## L.5 T27 — keputusan agent atas delegasi pemilik (prinsip #6 & #7)

**KEPUTUSAN: prinsip #6 (Proporsional) dan #7 (maksimal 2 putaran, lalu eskalasi ke pemilik) TETAP DIPERTAHANKAN.
Agent TIDAK memakai delegasi pemilik untuk menimpanya.**

Alasan (berbasis bukti di K.2, bukan preferensi):
1. Kedalaman tak terbatas **tidak menghasilkan kebenaran lebih**, melainkan **derau** — cry-wolf terdokumentasi
   sebagai penyebab utama alat review ditinggalkan; generasi awal menghasilkan **9 positif palsu per 1 bug asli**.
2. Hakim AI papan atas **gagal konsisten di ±25% kasus sulit** dengan **flip rate 20–35%** — menambah putaran
   tanpa batas berarti menambah **peluang verdict berubah-ubah**, bukan menambah ketepatan.
3. Prinsip #7 (eskalasi ke pemilik) justru **pengaman terakhir**: keputusan final tetap di manusia, sesuai bukti
   bahwa **71% developer tidak mau merge kode AI tanpa review manusia**.
4. **Ketelitian dinaikkan lewat 4 penguatan di K.3 (verifikasi adversarial, saring derau, model beda keluarga,
   verifikasi runtime) — yaitu di DALAM batas #6/#7, bukan dengan membongkarnya.**

**Satu penegasan yang menghubungkan T27 dengan T31 (penting, supaya tidak salah dibaca):**
> **Batas 2 putaran membatasi LOOP review, BUKAN cakupan laporan.** Putaran boleh habis, tetapi
> **temuan di luar cakupan tetap wajib dilaporkan** (aturan cakupan L.3). Keduanya tidak bertentangan.

---

# M. TEMUAN LINGKUNGAN yang MENGUBAH ARSITEKTUR — allowlist jaringan sandbox

Ditemukan saat mengerjakan T28 (riset skill). **Ini temuan paling berdampak di sesi ini**, karena sebagian
rekomendasi agent di bagian H **tidak memperhitungkannya**.

## M.1 `find-skills` TIDAK BERFUNGSI di sandbox ini — dan agent hampir salah menyimpulkan

`npx skills find` mengembalikan **"No skills found"** untuk `audit`, `code review`, `security audit`,
`documentation`, `accessibility`. **Agent tidak langsung menyimpulkan "tidak ada skill audit"**, melainkan
menjalankan **uji kontrol** dengan kueri yang pasti ada hasilnya:

- `npx skills find react` → **"No skills found"**
- `npx skills find nextjs` → **"No skills found"**

**Uji kontrol gagal → alatnya yang rusak, bukan hasilnya yang kosong.** Penyebabnya teridentifikasi:
**`skills.sh` TERBLOKIR** (`curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL`, HTTP 000).

**Kesimpulan yang jujur: agent TIDAK BISA mengklaim "tidak ada skill untuk audit".** Yang benar:
**mekanisme pencarian skill resmi tidak bisa dijalankan dari lingkungan ini**, jadi pencarian skill harus
lewat jalur lain (GitHub / npm) atau lewat alat platform.

## M.2 Peta jangkauan jaringan (diukur dengan `curl`, bukan diasumsikan)

| ✅ TERJANGKAU | HTTP | ❌ TERBLOKIR (SSL_ERROR_SYSCALL) |
|---|---|---|
| `registry.npmjs.org` | 200 | `skills.sh` (registry skill) |
| `pypi.org` | 200 | `raw.githubusercontent.com` |
| `api.github.com` (`gh api`, sisa rate 4.984) | 200 | `fonts.google.com`, `fonts.gstatic.com` |
| `github.com` (web + git clone/push/fetch) | 200 | `developers.cloudflare.com`, `api.cloudflare.com`, `dash.cloudflare.com` |
| — | — | `api.supabase.com`, `api.vercel.com` |
| — | — | `api.whatsapp.com`, `graph.facebook.com`, `midtrans.com` |
| — | — | `unpkg.com`, `cdn.jsdelivr.net`, `objects.githubusercontent.com` |
| — | — | `google.com` (dan situs umum lain) |

**Pola yang terbaca: sandbox ini hanya mengizinkan registry paket (npm, PyPI) + GitHub.** Semua situs/API lain
diblokir di tingkat TLS. **Alat platform `web_search` / `fetch_page` TETAP berfungsi** (dipakai sepanjang sesi ini)
karena jalurnya berbeda dari `curl` proses sandbox.

## M.3 ENAM koreksi arsitektur yang WAJIB (akibat langsung M.2)

1. **PUBLIKASI = lewat GIT, bukan lewat API.** `api.cloudflare.com` **terblokir** → `wrangler deploy`
   **tidak bisa dijalankan agent dari sandbox**. **Jalur yang tetap hidup:** Cloudflare Pages/Vercel/Netlify
   **terhubung ke repo GitHub dan membangun otomatis setiap push** — dan `git push` ke `github.com` **berfungsi**.
   Jadi: **agent push → platform hosting membangun → situs tayang.** Penyambungan awal (hosting ↔ GitHub) adalah
   **setup sekali oleh pemilik di browser**, bukan kerja agent. **Ini menyelamatkan seluruh arsitektur bagian H.**
2. **WAKTU-PAKAI ≠ WAKTU-BANGUN.** API yang terblokir bagi **agent** tidak terblokir bagi **tamu**. Saat undangan
   tayang, yang berbicara ke Supabase/Cloudflare/WhatsApp adalah **browser tamu**, bukan sandbox agent.
   **Jadi RSVP, buku tamu, dan analitik tetap berfungsi** walau `api.supabase.com` terblokir dari sandbox.
   **Konsekuensi:** provisioning (bikin DB, pasang secret) = **tindakan pemilik di browser**; agent hanya
   menyiapkan kode + migrasi + instruksi.
3. **SEMUA ASET HARUS DIBUNDEL LOKAL — DILARANG bergantung CDN.** `unpkg.com`, `cdn.jsdelivr.net`,
   `fonts.gstatic.com` **terblokir** → undangan yang memuat font/lib dari CDN **akan rusak saat dibangun di sandbox**.
   **Jalur font yang terbukti hidup:** paket npm **`@fontsource/*`** — diverifikasi `npm view @fontsource/playfair-display version`
   → **5.3.0 tersedia**. Ini sekaligus **jalan keluar dari `fonts.google.com` yang terblokir**, dan memang
   **self-hosting yang disarankan** (bagian F: lebih cepat + menghindari isu privasi GDPR).
4. **QR CODE dibuat LOKAL, bukan lewat API.** `api.qrserver.com` **terblokir** → pakai `qrcode` dari **PyPI**
   (terjangkau; unduhan uji berhasil di sesi ini) atau `qrcode` dari npm. **Lebih baik juga secara privasi:**
   data tamu tidak pernah dikirim ke pihak ketiga hanya untuk membuat gambar QR.
5. **WhatsApp & pembayaran TANPA API.** `api.whatsapp.com`, `graph.facebook.com`, `midtrans.com` **terblokir** →
   konfirmasi **desain yang sudah dipilih di bagian A**: distribusi lewat **tautan `wa.me` + teks pesan siap kirim**
   (persis pola pasar: "template pesan WhatsApp siap pakai"), dan **amplop digital = nomor rekening + gambar QRIS
   statis + tombol konfirmasi tercatat**. **Nol kebutuhan API, nol biaya.** Gateway pembayaran = fitur premium
   yang **memang tidak bisa** dijalankan dari sandbox.
6. **T22 (riset internet oleh reviewer) HARUS lewat alat platform, bukan `curl`.** Karena situs umum terblokir,
   aturan "agent independen wajib riset internet" **wajib dirumuskan sebagai**: riset dijalankan dengan
   **alat `web_search`/`fetch_page` milik platform**, dan **hasilnya disimpan ke berkas beserta URL sumbernya**.
   **Dilarang** merancang mekanisme yang bergantung pada `curl`/`wget` ke situs umum — **itu akan gagal diam-diam
   atau keras di lingkungan nyata**. (Semua riset di bagian A–K sesi ini memang dijalankan lewat alat platform,
   jadi ini sudah terbukti bisa.)

**Kandidat skill tambahan yang belum terverifikasi:** `npx skills add <owner/repo@skill>` **mungkin** tetap berfungsi
karena ia mengambil dari **GitHub** (terjangkau), bukan dari `skills.sh`. **BELUM DIUJI** — pengujian berarti
memasang sesuatu, jadi butuh izin pemilik. Jalur cadangan yang **sudah terbukti hidup**: `git clone` langsung dari
`github.com` (persis cara 10 ZIP di `Input-Pengguna/` dulu diproses).

## M.4 TEMUAN platform ke-3: clone **jadi shallow LAGI** di tengah sesi

Saat hendak merge `origin/main`, git menolak: **"refusing to merge unrelated histories"**. Diagnosis:
`.git/shallow` **muncul kembali** (82 byte, stempel waktu di antara giliran) → `origin/main` **hanya terlihat
1 commit**, `git merge-base HEAD origin/main` **kosong**, dan `eff7afa` **tidak lagi terbaca sebagai leluhur**
`origin/main`. **Pemulihan:** `git fetch --unshallow --prune` → 583/584 commit terbaca, merge-base = `eff7afa`,
lalu merge **bersih 0 konflik**.

**Aturan kerja yang diperbarui (menggantikan pelajaran insiden #1 dan #2):**
> **SEBELUM operasi apa pun yang bergantung riwayat** (merge, rebase, `merge-base`, cek leluhur, `git log` lintas-branch),
> **WAJIB periksa 3 hal:** (1) `git rev-parse --is-shallow-repository` harus `false`, (2) HEAD lokal harus
> **mengandung** sha remote branch (`git ls-remote`), (3) `git rev-list --count origin/main` masuk akal (ratusan, bukan 1).
> Kalau salah satu gagal → **pulihkan dulu** (`git fetch --unshallow`, atau `git reset --mixed <sha remote>`),
> **baru** lanjut. **Jangan pernah** `merge --allow-unrelated-histories` untuk mengatasi gejala ini.

## M.5 KOREKSI atas laporan awal sesi ini: temuan #3 sudah BASI

Laporan awal (giliran entry point) melaporkan unit `fixture-narasi-sejarah-setrika-arang-di-atas-bata-merah`
sebagai **`blocked` menunggu G2**. **Itu sudah tidak berlaku.** `main` bergerak saat sesi ini berjalan:
**PR #71 MERGED** (`b6a4b7e`), dan sesi lain (`arena/01a0ae4c`, log slot `_14`) mencatat:
**G2 naskah final, G1 Tahap 4, dan G2 breakdown SEMUA DIBERIKAN pemilik 2026-09-17**, lalu **produksi dihentikan
pemilik sebelum Tahap 5**. Keadaan unit akhir: **`abandoned`** — berhenti **sadar** di Tahap 4 dengan gerbang valid
sampai tahap itu (**bukan kegagalan, bukan kelalaian**). **T-3 tetap tanpa mandat.** Log sesi lain **tidak disentuh**
(79 baris, utuh setelah merge).

**Pelajaran yang dicatat:** laporan awal adalah **snapshot pada sha tertentu** (`eff7afa`). Karena `main` bisa
bergerak selama sesi berjalan, **temuan tentang state unit/PR wajib diberi sha acuannya** dan **dicek ulang
sebelum dipakai mengambil keputusan** — bukan dipercaya dari laporan awal sesi.

## Log Keputusan (lanjutan)

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | **Klaim agent di K.0 DIKOREKSI sebagai over-claim**; T29 diputuskan **pemilik benar** | Bukti dokumen: protokol + alat review terikat PR (anatomi butir 2, `--pr`/`--generic` saja). Agent menyamakan review PR dengan audit isi — dua hal berbeda |
| 2026-09-17 | T31 diputuskan **pemilik benar**; **ATURAN CAKUPAN** dirumuskan (cakupan membatasi pencarian & klaim, **tidak pernah** membatasi laporan) | Kalimat reviewer ambigu; 6 preseden repo membuktikan temuan di luar cakupan **dilaporkan, tidak dibuang, tidak ditindak** |
| 2026-09-17 | T26 (4 cacat manual) diubah jadi **syarat kelulusan mekanis** + gerbang G0-manual | Bukti lapangan pemilik dari sistem lain; lensa #5 QA sudah ada tapi gagal diterapkan di sana |
| 2026-09-17 | T27 diputuskan: prinsip **#6 & #7 DIPERTAHANKAN**, tidak ditimpa walau pemilik mendelegasikan | Bukti cry-wolf + flip rate 20–35% + 25% gagal transitivitas; ketelitian dinaikkan **di dalam** batas lewat 4 penguatan K.3. Delegasi umum **tidak dipakai** untuk membongkar pengaman yang sudah teruji |
| 2026-09-17 | **6 koreksi arsitektur (M.3) diwajibkan** setelah peta jaringan diukur | `api.cloudflare.com` dll terblokir → rekomendasi bagian H **tidak lengkap** tanpa koreksi ini. Publikasi harus lewat **git push**, aset harus **dibundel lokal**, font lewat **`@fontsource` npm**, QR **lokal**, WA/pembayaran **tanpa API** |
| 2026-09-17 | **Agent TIDAK mengklaim "tidak ada skill audit"** | Uji kontrol (`react`, `nextjs`) ikut kosong → alatnya rusak karena `skills.sh` terblokir, bukan hasilnya kosong. Menyimpulkan "tidak ada" dari alat rusak = klaim palsu |
| 2026-09-17 | Temuan #3 laporan awal **DICABUT sebagai basi** | PR #71 merged saat sesi berjalan; unit jadi `abandoned` di Tahap 4 dengan gerbang valid |

---

# Giliran 11 — jawaban pemilik atas pertanyaan review Rencana Kerangka (VERBATIM)

Disimpan verbatim atas instruksi berdiri pemilik (S-01: *"Aku ga mau ada satu hal pun yang terlupakan…
simpan chat aku ini"*). Empat pertanyaan diajukan; tiga dijawab dengan kalimat sendiri.

**Pertanyaan 1 — Bentuk dasar (BERTINGKAT 3 lapis + SIKLUS 7 tahap):** pemilik memilih **"Setuju — kunci
bentuk ini"**. → **DIKUNCI.**

**Pertanyaan 2 — Gerbang resolusi cetak G3 fail-closed:** pemilik menjawab dengan kalimat sendiri
(verbatim):

> "Aku rasa sebaiknya jangan terlalu ketat, tapi bukan berarti ngentengin. Artinya begini, kita memang
> perlu tekankan agar foto atau video yang diinput adalah yang berkualitas. Tapi kalaupun ternyata dia
> tidak punya itu, kita kan bisa mensiasati nya, misalnya dengan melakukan upscaling dan penjernihan dan
> enhanchement dengan tenaga ai. Iya kan? Klo butuh skill untuk ini, kamu bisa siapkan skill nya.
> Gimana menurut kamu?"

**Catatan agent:** pemilik **meminta penilaian**, bukan persetujuan (*"Gimana menurut kamu?"*). Ini
mengaktifkan gerbang T25 dan instruksi berdiri S-03 (*"Aku mau kamu kritisi, bukan asal meng-iya-kan
saja"*). Jawaban agent ada di bagian **N** di bawah — **sebagian membenarkan pemilik, sebagian
mengoreksi**, dengan bukti.

**Pertanyaan 3 — Website induk / domain:** pemilik menjawab (verbatim):

> "Untuk masa percobaan gpp pake subdomain dulu yang gratis. Nanti waktu bener bener mulai rilis, baru
> pake domain yang cukup satu domin untuk semua undangan, kecuali klo client nya mau domain sendiri maka
> dia yang tanggung biaya nya"

→ **DIKUNCI sebagai kebijakan 3 fase** (lihat bagian 5 Rencana Kerangka): fase percobaan = subdomain
gratis; fase rilis = **satu domain untuk semua undangan**; pengecualian = **client yang mau domain
sendiri menanggung biayanya sendiri**.

**Pertanyaan 4 — cara memasang 8 gap skill:** pemilik menjawab (verbatim):

> "Aku kurang paham. Aku rasa kamu lebih tau tentng ini. Atau akan lebih baik klo kamu melakukan riset di
> internet mengenai cara pasng skill dan plugin yang paling maksimal dan terbik"

→ **DELEGASI + MANDAT RISET.** Hasil risetnya di bagian **O** di bawah.

---

# N. RISET: batas nyata AI upscaling untuk cetak — menjawab pertanyaan pemilik di G3

**Pertanyaan pemilik:** kalau client tidak punya foto berkualitas, bisakah disiasati dengan *upscaling +
penjernihan + enhancement* bertenaga AI?

**Jawaban singkat: BISA, tetapi hanya untuk SEBAGIAN jenis isi — dan undangan justru penuh dengan jenis
isi yang TIDAK bisa disiasati begitu.** Rinciannya, dengan sumber:

## N.1 Yang membenarkan pemilik (upscaling memang jalan)

- **"A 150 DPI photo upscaled 2x with AI tools can often reach acceptable quality at 300 DPI for most
  print uses"** — untuk **konten fotografis**, kenaikan **2×** dari **≥150 DPI** sering sudah cukup
  (printshop.paperlust.co).
- Alat yang disebut berulang: **Topaz Gigapixel AI** (berbayar), **LetsEnhance** (cloud, ada free tier),
  dan **Upscayl — gratis, open-source, desktop**, berbasis **Real-ESRGAN** (sjprinter.com;
  aiphotogenerator.net). Model Real-ESRGAN default bagus untuk **foto**; model **UltraSharp** dan
  **Digital Art** untuk ilustrasi/gambar hasil AI.
- Jadi usulan pemilik **bukan ide buruk** — untuk **foto pengantin, foto keluarga, foto gedung**, ini
  mitigasi yang sah dan gratis.

## N.2 Yang MENGOREKSI pemilik (batasnya keras, dan undangan kena di batas itu)

| Batas | Bukti | Kenapa ini fatal untuk undangan |
|---|---|---|
| **"Upscaling cannot recover detail"** — menaikkan 72 DPI ke 300 DPI **tidak menambah data piksel nyata** | printshop.paperlust.co | yang berubah hanya **angkanya**, bukan isinya. File boleh berlabel "300 DPI" tetapi hasilnya tetap lembek |
| **"Fine text, logos with thin strokes, and geometric line art upscale poorly. The AI model has no reliable pattern to fall back on for these, and can introduce artefacts or rounded edges on letterforms"** | printshop.paperlust.co | **undangan justru didominasi teks dan ornament garis halus** — nama pengantin, tanggal, kaligrafi, bingkai. Ini kategori **paling buruk** untuk upscaling |
| **"Text-heavy images: AI upscalers can mangle text, turning legible words into AI-hallucinated gibberish. For documents, use OCR and re-typeset instead"** | aiphotogenerator.net | **nama orang** bisa berubah jadi huruf karangan. Untuk undangan, salah nama = cacat yang tidak bisa dimaafkan client |
| **"There's a floor below which even the best AI can't produce usable results"** | aiphotogenerator.net | ada batas bawah; di bawahnya tidak ada penyelamatan |
| **"No upscaling tool creates the 155 megapixels needed from a 1-megapixel source"** untuk format besar | sjprinter.com | untuk **baliho/banner** (kalau kelak dibutuhkan) upscaling bukan jawaban |
| **"Upscaling fixes resolution only — color mode, bleed, and dimensions are separate issues"** | sjprinter.com | **menaikkan resolusi TIDAK menyelesaikan CMYK, bleed, atau ukuran.** Jadi upscaling **bukan** pengganti gerbang prepress yang lain |

## N.3 Satu hal yang LEBIH BAIK dari upscaling, dan belum disebut pemilik

- **"For flat graphics and logos, vectorization is a complete fix — the output is infinitely scalable"**
  (sjprinter.com). Tes praktisnya: **zoom 400%** — kalau tepi warnanya bersih, kemungkinan bisa
  divektorkan; kalau semuanya gradien halus, tidak.
- **Konsekuensi arsitektural yang penting untuk sistem ini:** kalau **teks di-render dari font** (bukan
  ditempel sebagai gambar) dan **ornament dibuat sebagai vektor (SVG)**, maka **masalah resolusi untuk
  keduanya HILANG SECARA STRUKTUR** — bukan diselesaikan, tapi **tidak pernah muncul**. Yang tersisa
  sebagai aset raster hanyalah **foto**.
- Ini mengubah bentuk gerbangnya: alih-alih "semua aset harus 300 DPI", aturannya jadi **"teks wajib
  vektor/font, ornament wajib vektor, hanya foto yang boleh raster — dan hanya foto yang butuh gerbang
  resolusi"**.

## N.4 Kesimpulan agent (verdict atas ide pemilik, sesuai gerbang T25)

**Ide pemilik DITERIMA SEBAGIAN dan DIPERTAJAM, bukan ditolak dan bukan diiyakan mentah-mentah:**

1. **Benar** bahwa menolak mutlak terlalu kaku, dan **benar** bahwa upscaling AI adalah mitigasi sah —
   **untuk foto**, **maksimal ~2×**, dari sumber **≥150 DPI pada ukuran cetak akhirnya**.
2. **Salah kalau diterapkan merata**: untuk **teks dan ornament garis halus** upscaling justru
   **mengarang** detail dan bisa **mengubah nama orang**. Kategori ini **tidak boleh** lewat jalur
   upscaling.
3. **Jalur yang lebih baik untuk kategori itu sudah ada**: teks = **render dari font**, ornament/logo =
   **vektor (SVG) atau vectorization**. Ini **menghapus** masalahnya secara struktur.
4. **Upscaling tidak menyelesaikan CMYK, bleed, atau ukuran** — jadi gerbang prepress lainnya **tetap
   berdiri**, tidak ikut dilonggarkan.
5. Maka G3 diubah dari **2 hasil** (lolos / tolak) menjadi **3 hasil + pengalihan menurut jenis isi** —
   rumusannya ada di Rencana Kerangka bagian 4.3. **Ini bukan melonggarkan gerbang; ini membuat gerbangnya
   membedakan jenis isi, karena ancamannya memang berbeda per jenis isi.**

**Skill yang dibutuhkan untuk ini (permintaan pemilik: *"Klo butuh skill untuk ini, kamu bisa siapkan
skill nya"*):** upscaling raster (**Upscayl/Real-ESRGAN** — gratis, open-source) + vectorization.
**Tetapi kelayakannya di lingkungan ini belum diuji** dan dicatat sebagai utang, bukan diklaim siap:
`pip install` tidak bertahan antar sesi, tidak ada ffmpeg/ImageMagick-PDF/chromium, dan **semua API
layanan eksternal terblokir** (hanya npm, PyPI, github.com) — jadi jalur cloud seperti LetsEnhance
**gugur sejak awal**. Yang tersisa: alat lokal yang bisa dipasang dari PyPI/npm/GitHub, **dan bobot
modelnya harus bisa diunduh dari sumber yang terjangkau**.

---

# O. RISET: cara memasang skill & plugin yang paling andal — menjawab delegasi pemilik

Pemilik: *"Aku kurang paham… akan lebih baik klo kamu melakukan riset di internet mengenai cara pasng
skill dan plugin yang paling maksimal dan terbik."*

## O.1 Empat jalur pemasangan yang ada di ekosistem

| Jalur | Perintah | Berlaku di lingkungan ini? |
|---|---|---|
| **Plugin marketplace** (interaktif) | `/plugin marketplace add owner/repo` lalu `/plugin install plugin@marketplace` | **TIDAK** — ini slash command Claude Code CLI, bukan sesuatu yang bisa dijalankan agent dari shell di sini |
| **CLI npm** | `npx skills add owner/repo --skill nama` atau `npx skillstore add author/nama` | **SEBAGIAN** — npm terjangkau, **tetapi ada preseden buruk di repo ini**: `npx skills find` **GAGAL-DIAM** (skills.sh terblokir). Jalur ini tidak boleh dipercaya tanpa diuji dulu |
| **git clone + salin foldernya** | `git clone https://github.com/owner/repo` lalu **salin folder skill-nya saja** ke direktori skill | **YA** — github.com terjangkau, dan ini **satu-satunya jalur yang sudah terbukti** di sesi ini |
| **Manual / ZIP** | unduh ZIP, ekstrak ke direktori skill | **YA** tapi lebih lemah provenance-nya (tidak ada sha sumber) |

## O.2 Dua direktori, dan bedanya penting

| | Personal | **Project-scoped** |
|---|---|---|
| Lokasi | `~/.claude/skills/` | **`.claude/skills/` di dalam repo** |
| Cakupan | semua proyek | **satu repo ini saja** |
| **Ikut ter-commit & terbagi lewat git** | **tidak** | **YA** |
| Cocok untuk | kebiasaan pribadi | **standar tim/repo** |

Sumber: agensi.io/learn/how-to-install-skills-claude-code; lucaberton.com/blog/claude-code-skills-plugins-2026.

**Keputusan agent: pakai PROJECT-SCOPED dan di-vendor ke dalam repo**, mengikuti konvensi yang **sudah
berjalan** di repo ini (`sistem/sistem-building-aplikasi/skills/` berisi 56 skill). Alasannya bukan
selera:

1. **Bertahan antar sesi.** Pemasangan di luar repo (dan `pip install`) **tidak persisten** di lingkungan
   ini — sudah terbukti. Skill yang hilang tiap sesi = mekanisme yang tidak bisa diandalkan.
2. **Self-contained**, sesuai filosofi repo ini (W-07 dan validator `check_selfcontained.py`): sistem
   harus bisa dipakai tanpa bergantung pada hal di luar folder/repo.
3. **Bisa diaudit dan di-rollback** karena versi-nya tercatat di git, bukan "terpasang suatu hari".
4. **Standar Agent Skills lintas alat** (`agentskills.io`): format `SKILL.md` dipakai bersama oleh Claude
   Code, Codex CLI, OpenCode, Cursor — jadi tidak mengunci ke satu alat.

## O.3 Aturan keamanan yang WAJIB (ini bagian yang paling sering dilewati)

> **"Skills can execute arbitrary code in Claude's environment. Only install skills from trusted
> sources. Review SKILL.md and all scripts before enabling a skill. Be cautious of skills that request
> sensitive data access."** — travisvn/awesome-claude-skills

Maka aturan pemasangan di sistem ini:

1. **Baca `SKILL.md` + semua skripnya SEBELUM di-commit.** Bukan sesudah.
2. **Catat provenance per skill**: repo sumber, **sha commit** yang disalin, tanggal, dan **lisensinya**.
   Tanpa sha, "skill X terpasang" tidak bisa direproduksi.
3. **Tolak skill yang meminta akses data sensitif** atau yang memanggil layanan eksternal (semua API
   eksternal **terblokir** di lingkungan ini, jadi skill semacam itu **memang tidak akan jalan**).
4. **Skill yang gagal diuji tidak boleh dinyatakan terpasang** — statusnya "ada di repo, belum terbukti
   jalan", ditulis apa adanya.

## O.4 Konsekuensi untuk 8 gap skill

Delapan gap itu **tidak lagi menunggu link pemilik** sebagai satu-satunya jalur. Jalurnya sekarang:
**agent mengusulkan per butir** (repo sumber + lisensi + kenapa) → **pemilik setujui atau ganti** →
**agent clone + review + vendor + catat provenance + uji** → baru dinyatakan terpasang. **Satu butir
ditambah** dari hasil bagian N: **upscaling raster + vectorization** (kebutuhan yang muncul dari
keputusan G3, bukan dari daftar awal).

## Log Keputusan (lanjutan)

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-17 | **Jawaban pemilik atas 4 pertanyaan review disimpan VERBATIM** di berkas ini, bukan diringkas di memori agent | Instruksi berdiri S-01, dan pelajaran giliran yang sama: keputusan yang hanya hidup di chat/memori **hilang tanpa jejak** kalau sesi mati |
| 2026-09-17 | **Bentuk dasar DIKUNCI** (BERTINGKAT 3 lapis + SIKLUS 7 tahap) | Persetujuan eksplisit pemilik |
| 2026-09-17 | **Kebijakan domain DIKUNCI 3 fase** | Kalimat pemilik sendiri: subdomain gratis untuk percobaan → satu domain saat rilis → client yang mau domain sendiri menanggung biayanya |
| 2026-09-17 | **G3 TIDAK dijawab "ya" mentah-mentah; diriset dulu dan hasilnya MENGOREKSI sebagian ide pemilik** | Pemilik bertanya *"Gimana menurut kamu?"* — itu permintaan penilaian. Instruksi berdiri S-03: *"Aku mau kamu kritisi, bukan asal meng-iya-kan saja."* Riset menunjukkan upscaling **jalan untuk foto** tetapi **mengarang detail untuk teks dan garis halus**, dan undangan didominasi keduanya |
| 2026-09-17 | **Jalur pemasangan skill = git clone + vendor project-scoped ke dalam repo**, bukan `/plugin` dan bukan mengandalkan `npx skills` | `/plugin` tidak bisa dijalankan dari sini; `npx skills find` punya **preseden GAGAL-DIAM** di repo ini; git clone **satu-satunya yang terbukti**. Vendor ke repo juga satu-satunya yang **persisten antar sesi** |

---

# P. UJI T-28: kelayakan & mutu upscale AI untuk gerbang G3 — DIUKUR, bukan diasumsikan

**Kenapa bagian ini ada.** Rencana Kerangka menjanjikan jalur **"LOLOS BERSYARAT"** (foto kurang resolusi
→ ditingkatkan AI) atas permintaan pemilik. Janji itu **ditulis sebelum kemampuannya diuji**. Aturan yang
dibuat hari yang sama berkata yang begitu tidak boleh dibiarkan. Jadi diuji.

**Skrip ujinya disimpan supaya bisa direproduksi:** `_meta/_internal/uji/uji_upscaling.py` (metrik PSNR +
SSIM Gaussian 11×11 σ=1.5 per kanal — **mengikuti preseden repo bagian J.1**, bukan metrik karangan baru).

## P.1 Ketersediaan komponen (jawaban: BISA, dengan satu pengecualian penting)

| Komponen | Hasil | Waktu pasang |
|---|---|---|
| `numpy` 2.4.6, `pillow` 12.3.0 | ✅ terpasang dari PyPI | 6,5 dtk |
| `opencv-contrib-python-headless` → **cv2 5.0.0, `dnn_superres` TERSEDIA** | ✅ | 5,3 dtk |
| `vtracer` (raster → SVG) | ✅ | 2,2 dtk |
| `svgwrite` 1.4.3 | ✅ | <1 dtk |
| **Bobot model super-resolution** | ✅ **tetapi lewat jalur tidak terduga** | lihat bawah |

**Temuan jaringan yang menentukan:** `raw.githubusercontent.com` dan `objects.githubusercontent.com`
**DIBLOKIR** (HTTP `000`, gagal dalam 0,03–0,05 dtk = koneksi ditolak, bukan timeout). Yang **terbuka**:
`github.com`, `api.github.com`, **`codeload.github.com`**, `registry.npmjs.org`, `pypi.org`.
**Akibatnya:** model tidak bisa diunduh dari URL langsung seperti yang lazim didokumentasikan, tetapi
**bisa diambil lewat tarball repo di codeload**:

```
curl -sL https://codeload.github.com/Saafke/FSRCNN_Tensorflow/tar.gz/refs/heads/master | tar xz
curl -sL https://codeload.github.com/fannymonori/TF-ESPCN/tar.gz/refs/heads/master | tar xz
```

**Provenance model (dicatat supaya bisa direproduksi tanpa jaringan):**

| Model | Ukuran | sha256 (16 awal) | Layak di-vendor ke repo? |
|---|---|---|---|
| `FSRCNN_x2.pb` | **39 KB** | `366b33f0084c7b3f…` | **YA** — kecil |
| `ESPCN_x2.pb` | **85 KB** | `59f77351e1d7c005…` | **YA** — kecil |
| `EDSR_x2.pb` | **37 MB** | `585623221baa0702…` | **TIDAK** — berat, dan ternyata **tidak bisa jalan** (P.3) |

**⚠️ `pip install` TIDAK bertahan antar sesi** di lingkungan ini (sudah terbukti sebelumnya, dan
dikonfirmasi lagi: semua paket di atas **tidak ada** saat giliran ini dimulai). Jadi total **~14 detik
pemasangan ulang harus dianggarkan tiap sesi**, dan langkahnya **wajib tertulis** di dokumen sistem.

## P.2 Mutu pada 2× upscale — FOTO vs GARIS HALUS (inti temuannya)

Bahan foto: **foto nyata dari repo** (`S5-aspal-kosong.jpg`), ground truth 900×900, sumber rendah
450×450 (= simulasi **150 DPI untuk target 300 DPI**). Bahan garis: gambar uji guratan 6/4/3/2/1 piksel
+ bentuk mirip huruf ber-serif + grid halus, ground truth 512×512 dari sumber 256×256.

**FOTO** (lebih tinggi lebih baik):

| Metode | PSNR dB | SSIM | Waktu |
|---|---|---|---|
| bicubic (bukan AI) | 36,64 | 0,9262 | 0,00 dtk |
| lanczos4 (bukan AI) | 36,91 | 0,9281 | 0,01 dtk |
| **fsrcnn (AI)** | 37,09 | 0,9263 | 0,23 dtk |
| **espcn (AI)** | 37,19 | 0,9266 | 0,16 dtk |
| edsr (AI) | **37,76** | **0,9307** | **105,9 dtk** |

**GARIS HALUS / bentuk mirip teks:**

| Metode | PSNR dB | SSIM | Waktu |
|---|---|---|---|
| bicubic | **20,85** | 0,9137 | 0,00 dtk |
| lanczos4 | 20,84 | 0,9091 | 0,00 dtk |
| **fsrcnn (AI)** | **22,61** | **0,9358** | 0,08 dtk |
| espcn (AI) | 21,96 | 0,9317 | 0,05 dtk |
| edsr (AI) | 21,82 | 0,9283 | 35,0 dtk |

**Skala penilaian yang dipakai repo ini sendiri (bagian J.1):** PSNR ≥40 & SSIM ≥0,99 = nyaris tak
terbedakan · PSNR 35–40 & **SSIM 0,97–0,99** = sangat baik · **PSNR <32 = degradasi mulai terlihat**.

### Empat kesimpulan yang mengubah desain

1. **Untuk FOTO, keuntungan AI atas Lanczos ternyata KECIL.** ESPCN +0,55 dB, FSRCNN +0,28 dB atas
   lanczos4; SSIM-nya **praktis identik** (0,9263–0,9266 vs 0,9281). Satu-satunya yang unggul berarti
   adalah **EDSR (+1,12 dB)** — dan EDSR **tidak bisa dipakai** (P.3). **Konsekuensi: sistem ini TIDAK
   BOLEH menjual "peningkatan AI" sebagai perubahan mutu.** Yang jujur: *"ditingkatkan dengan
   super-resolution; keuntungannya kecil dibanding resampling berkualitas tinggi"*.
2. **Ambang "≥150 DPI + ≤2×" MENGHASILKAN SSIM 0,93 — DI BAWAH ambang "sangat baik" repo sendiri (0,97).**
   Jadi jalur LOLOS BERSYARAT **tidak boleh dilabeli "sangat baik"**. Label yang sesuai bukti: **"baik,
   dengan risiko terlihat lembut pada cetakan dekat"**. **Konsekuensi: cetak uji (proof) wajib untuk
   SEMUA kasus LOLOS BERSYARAT, bukan hanya oplah besar** — ini memperketat draft, bukan melonggarkan.
3. **Untuk GARIS HALUS, SEMUA metode GAGAL menurut skala repo: PSNR 20,8–22,6, jauh di bawah 32
   ("degradasi mulai terlihat").** AI memang paling baik di antara yang buruk (FSRCNN +1,76 dB, SSIM
   0,9137→0,9358), tetapi **tidak ada metode yang membuat guratan tipis jadi layak cetak**.
   **Klaim riset "upscaling mangle text" TERBUKTI SECARA TERUKUR di lingkungan ini.** → **Langkah 0
   (teks wajib dari font, ornament wajib vektor) kini bukan lagi anjuran desain, melainkan KESIMPULAN
   TERUKUR.** Ini penguatan terpenting dari seluruh uji ini.
4. **Vektorisasi: cocok untuk gambar datar, tidak untuk foto — terukur.** `vtracer` pada gambar
   garis/ornament 512×512 → **SVG 23,0 KB** (wajar). Pada **foto nyata** → **SVG 6,4 MB** (tidak
   berguna). Jadi aturan "ornament wajib vektor" **bisa dijalankan**, tetapi **jangan pernah**
   memvektorkan foto.

## P.3 Plafon kinerja & memori — EDSR GUGUR

Memori lingkungan: **3.939 MB total, 3.761 MB tersedia.** Uji pada ukuran cetak nyata, tiap ukuran di
**proses terpisah** supaya satu OOM tidak menghapus hasil lain:

| Model | 400×566 | **874×1240 (A5@300 dari 150 DPI)** | **1240×1754 (A4@300 dari 150 DPI)** |
|---|---|---|---|
| **FSRCNN_x2** | 0,3 dtk | **2,0 dtk** → 1748×2480 | **3,7 dtk** → 2480×3508 |
| **ESPCN_x2** | 0,3 dtk | **0,9 dtk** | **2,0 dtk** |
| **EDSR_x2** | **126,4 dtk** | **OOM-KILL** | **OOM-KILL** |

**EDSR gugur untuk dua alasan yang saling menguat:** terlalu lambat (126 dtk untuk gambar *setengah* A5)
dan **dibunuh kehabisan memori** pada ukuran cetak sungguhan. Padahal EDSR satu-satunya yang unggul
berarti pada foto. **Jadi model terbaik tidak tersedia, dan yang tersedia keuntungannya kecil** — inilah
alasan kesimpulan P.2 butir 1.

**Percobaan pertama uji ini sendiri KENA OOM-KILL** (satu proses mengerjakan semua ukuran sekaligus).
Diulang dengan **satu proses per ukuran** — pelajaran: uji yang bisa menghabiskan memori **wajib**
dijalankan terisolasi, kalau tidak hasilnya hilang semua dan yang terlihat hanya "Killed".

## P.4 Keputusan untuk G3 berdasarkan bukti di atas

| Unsur draft | Sebelum uji | Sesudah uji |
|---|---|---|
| Ketersediaan jalur LOLOS BERSYARAT | belum diketahui (T-28) | **TERSEDIA** — FSRCNN/ESPCN, 2–4 dtk untuk A4@300 |
| Alat yang dipakai | "Upscayl/Real-ESRGAN" (dari riset web) | **DIGANTI: `cv2.dnn_superres` + FSRCNN_x2 / ESPCN_x2.** Real-ESRGAN butuh PyTorch (ratusan MB–GB) dan bobotnya dari GitHub Releases; **EDSR yang terdekat pun OOM** |
| Klaim mutu ke client | "ditingkatkan AI" | **DITURUNKAN jadi jujur**: keuntungan kecil atas resampling berkualitas; **bukan** pemulihan detail asli |
| Cetak uji (proof) | wajib untuk oplah besar | **WAJIB UNTUK SEMUA LOLOS BERSYARAT** — karena SSIM terukur 0,93, di bawah ambang "sangat baik" repo (0,97) |
| Langkah 0 (teks=font, ornament=vektor) | anjuran desain berbasis riset | **NAIK STATUS jadi kesimpulan terukur**: PSNR guratan tipis 20,8–22,6 < 32 untuk **semua** metode |
| Bobot model | belum diputuskan | **FSRCNN_x2 (39 KB) + ESPCN_x2 (85 KB) diusulkan di-vendor ke repo** — total 124 KB, karena `raw.githubusercontent.com` **diblokir** sehingga mengandalkan unduhan tiap sesi itu rapuh |

## P.5 Yang masih BELUM teruji (jangan diklaim dari angka di atas)

- **Font sungguhan tidak diuji** — font sistem kosong di lingkungan ini. Yang diuji **guratan tipis dan
  bentuk mirip huruf**, jadi kesimpulan "teks" berlaku untuk **bentuk bergaris tipis**, bukan pengukuran
  pada tipografi nyata. Ini **melemahkan sebagian** kesimpulan P.2 butir 3 dan dinyatakan sadar.
- **Mutu cetak fisik tidak terukur** — tidak ada printer di sini. PSNR/SSIM adalah **proksi**, bukan
  pengganti proof fisik. Justru karena itu cetak uji diwajibkan.
- **Sumber ≥200 DPI belum diukur.** Kalau ambang LOLOS BERSYARAT kelak diperketat dari ≥150 ke ≥200 DPI,
  **angkanya harus diukur ulang**, tidak boleh diekstrapolasi dari tabel di atas.
- **CMYK/bleed/PDF-X tidak disentuh upscaling sama sekali** — riset: *"Upscaling fixes resolution only."*
  Gerbang prepress lain tetap berdiri sendiri.
- **Perilaku pada foto kiriman client yang sudah terkompresi JPEG berat belum diuji** (bahan ujinya PNG/JPEG
  berkualitas baik dari repo). Preseden J.1 sudah memperingatkan hal serupa soal angka "hemat".

## Log Keputusan (lanjutan)

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-17 | **T-28 DIUJI Sungguhan, bukan diperkirakan** — skrip disimpan di `_meta/_internal/uji/uji_upscaling.py` | Janji "LOLOS BERSYARAT" sudah tertulis di Rencana Kerangka sebelum kemampuannya diuji. Aturan yang dibuat hari yang sama melarang itu. Skrip disimpan supaya **bisa direproduksi**, sesuai tuntutan T19 (rumusan yang bisa diuji, bukan yang terdengar sempurna) |
| 2026-09-17 | **EDSR dan Real-ESRGAN DIBUANG dari rencana; FSRCNN_x2 + ESPCN_x2 yang dipakai** | EDSR **OOM-KILL** pada A5@300 dan 126 dtk pada setengah A5; Real-ESRGAN butuh PyTorch + bobot dari host yang terblokir. Memilih model terbaik yang **tidak bisa jalan** lebih buruk daripada model sederhana yang jalan dalam 2–4 detik |
| 2026-09-17 | **Cetak uji diwajibkan untuk SEMUA LOLOS BERSYARAT** (memperketat draft, bukan melonggarkan) | SSIM terukur **0,93**, sedangkan skala repo sendiri menyebut "sangat baik" baru di **≥0,97**. Melabeli hasil ini "sangat baik" akan mengutip skala repo untuk klaim yang tidak didukung angkanya |
| 2026-09-17 | **Klaim mutu ke client DITURUNKAN** — tidak boleh disebut "peningkatan AI" tanpa penjelasan | Keuntungan terukur atas lanczos4 hanya **+0,28 s.d. +0,55 dB** pada foto dan SSIM praktis identik. Menjanjikan lebih dari itu ke client = menjanjikan hal yang tidak didukung bukti |
| 2026-09-17 | **Langkah 0 naik status dari anjuran menjadi kesimpulan terukur** | PSNR guratan tipis **20,8–22,6** untuk semua metode, di bawah ambang 32 milik repo sendiri. Klaim riset "upscaling mangle text" kini **terkonfirmasi terukur di lingkungan ini**, bukan sekadar dikutip |
| 2026-09-17 | **Bobot model diusulkan di-vendor (124 KB), TIDAK di-commit pada giliran ini** | Rencana Kerangka **belum final** dan pemilik belum menyetujui desain G3 yang baru. Menaruh biner sebelum desainnya disetujui = membuat artefak yang mungkin harus dicabut. Provenance-nya (URL codeload + sha256 + ukuran) **sudah dicatat di sini**, jadi keputusan menunda tidak menghilangkan kemampuan mereproduksi |

## P.6 T-30 DIUKUR (bukan ditunda) — dan hasilnya MEMBALIK sebagian rencana

Pemilik mendelegasikan (*"Aku ikut yang terbaik menurut kamu"*). Yang terbaik bukan memilih salah satu
dari dua pilihan yang kutawarkan, melainkan **mengukurnya sekarang** — tooling masih terpasang di sesi ini.

| Kondisi | Metode | PSNR dB | SSIM |
|---|---|---|---|
| **FOTO 150 DPI (2,0×)** | lanczos4 | 36,91 | 0,9281 |
| | FSRCNN → lanczos | 37,09 | 0,9263 |
| | ESPCN → lanczos | 37,19 | 0,9266 |
| **FOTO 200 DPI (1,5×)** | **lanczos4** | **39,28** | **0,9566** |
| | FSRCNN → lanczos | 39,14 | 0,9524 |
| | ESPCN → lanczos | 39,02 | 0,9514 |
| **GARIS 150 DPI (2,0×)** | lanczos4 | 24,18 | 0,9431 |
| | FSRCNN → lanczos | **25,67** | **0,9551** |
| **GARIS 200 DPI (1,5×)** | lanczos4 | 26,11 | 0,9657 |
| | FSRCNN → lanczos | **28,10** | **0,9752** |

### ⚠️ Confound metodologis yang WAJIB dinyatakan (ditemukan saat membandingkan dua run)

Angka **GARIS di tabel ini TIDAK BISA dibandingkan** dengan angka GARIS di P.2 (20,85–22,61). Dua sebab:
(a) run ini menambah **langkah resize akhir** yang menghaluskan sehingga **menaikkan** PSNR secara artifisial;
(b) dimensinya ganjil (511/255 vs 512/256). **Angka GARIS yang sah untuk disimpulkan adalah yang di P.2**
(perbandingan langsung, tanpa resize tambahan): **20,8–22,6 dB, di bawah ambang 32**. Angka GARIS di P.6
hanya sah untuk **membandingkan antar-metode di dalam tabel yang sama**.
**Angka FOTO justru konsisten antar-run** (lanczos4 = 36,91/0,9281 di kedua run) → **sah disimpulkan**.

### Tiga kesimpulan yang mengubah rencana

1. **Memperketat 150 → 200 DPI BERHARGA BESAR untuk foto: +2,37 dB dan SSIM 0,9281 → 0,9566.** Tapi
   **masih di bawah 0,97** ("sangat baik" versi repo). **Satu-satunya cara mencapai ≥0,97 adalah tidak
   upscale sama sekali** — yaitu jalur **LOLOS** (sumber ≥300 DPI).
2. **AI TIDAK MEMBERI KEUNTUNGAN PADA FOTO — di kedua kondisi.** Pada 2,0×: PSNR naik +0,18/+0,28 dB tetapi
   **SSIM justru TURUN** (0,9281 → 0,9263/0,9266). Pada 1,5×: **AI lebih buruk di kedua metrik**
   (39,28/0,9566 → 39,14/0,9524 dan 39,02/0,9514).
3. **AI hanya unggul pada GARIS HALUS (+1,5 s.d. +2,0 dB)** — **tetapi justru konten itu DILARANG oleh
   Langkah 0** (dan di P.2 terbukti tetap di bawah ambang 32 untuk semua metode).

### Keputusan T-30 (berdasarkan bukti di atas)

> **AI upscaling KELUAR dari jalur kritis. G3 jalur "LOLOS BERSYARAT" diimplementasikan dengan `Lanczos4`,
> ambang DIPERKETAT dari ≥150 ke ≥200 DPI, dan kenaikan dibatasi ≤1,5×.**

Alasannya, dalam satu kalimat: **AI tidak membantu pada satu-satunya jenis isi yang boleh masuk gerbang
(foto), dan hanya membantu pada jenis isi yang dilarang (garis halus).**

**Konsekuensi yang menguntungkan (tidak direncanakan, muncul dari bukti):**
- **T-29 turun prioritas**: bobot model jadi **OPSIONAL**, bukan kebutuhan jalur kritis → **tidak perlu
  vendor biner ke repo**, dan **ketergantungan `pip install` hilang dari jalur kritis** (Lanczos4 tersedia
  di Pillow/OpenCV dasar). Sistem jadi **lebih tahan** terhadap lingkungan yang paketnya tidak persisten.
- Waktu proses turun dari 2–4 dtk jadi **0,01 dtk** per aset.
- **AI tetap dipertahankan sebagai penyempurnaan opsional** untuk foto di pita 200–300 DPI, **dilabeli
  jujur** bahwa keuntungannya tidak terukur berarti — tidak boleh dijual sebagai peningkatan mutu.

**Yang belum diukur dan dinyatakan sadar:** sumber **≥250 DPI**; perilaku pada foto client yang sudah
terkompresi JPEG berat; dan **font sungguhan** (font sistem kosong — yang teruji guratan tipis).

---

## Giliran 12 (17 September 2026) — jawaban pemilik, VERBATIM

Disimpan apa adanya sesuai instruksi berdiri *"Aku ga mau ada satu hal pun yang terlupakan… simpan chat aku ini"*.

**Pesan pemilik (verbatim):**
> Lanjutkan sesuai yang menurutmu terbaik

**Jawaban atas 2 pertanyaan review (verbatim, lewat komponen pilihan):**

| Pertanyaan yang diajukan | Jawaban pemilik |
|---|---|
| *"Rencana Kerangka sudah lengkap dan sudah dikoreksi oleh hasil uji. Apakah ini sudah final sehingga folder sistem boleh dibuat?"* | memilih **"Setuju — finalisasi dan buat PR-nya"** *(opsi: aku buat `sistem/sistem-undangan/` + `00_RENCANA_KERANGKA.md` + `SYSTEM_MANIFEST.md` (Tahap: kerangka) + skeleton folder + daftar di INDEKS, semuanya dalam SATU PR tanpa auto-merge; 3 pertanyaan sisanya kupakai usulanku)* |
| *"T-30: ambang foto untuk jalur 'ditingkatkan AI'. SSIM terukur 0,93, di bawah ambang 'sangat baik' repo (0,97)."* | **jawaban bebas (verbatim):** *"Aku ikut yang terbaik menurut kamu"* |

### Apa yang dilakukan atas delegasi itu

Delegasi *"yang terbaik menurut kamu"* **tidak** diartikan sebagai izin memilih yang paling mudah. Untuk T-30
yang terbaik adalah **mengukur**, karena tooling masih terpasang di sesi yang sama — menunda satu giliran
hanya akan membuat keputusan diambil tanpa angka. Hasilnya di bagian **P.6** dan **membalik sebagian rencana**:
AI upscaling **keluar dari jalur kritis**, ambang **diperketat**.

Untuk *"buat PR-nya"*: dikerjakan **persis** seperti yang dijanjikan di opsi itu — satu PR, tanpa auto-merge,
3 pertanyaan sisanya (#2 7 hal konsisten, #3 tingkat risiko gerbang, #6 aset besar tidak masuk repo) dipakai
sebagai usulan agent dan **dicatat sebagai penerimaan bersyarat**: pemilik masih boleh mengubahnya, dan
revisinya wajib masuk Log Keputusan. **Tidak ditulis seolah-olah pemilik sudah menelaah ketiganya.**

---

## Giliran 13 (17 September 2026) — owner mengerahkan 3 hakim, dan verdict pertama MASUK

**Pesan pemilik (verbatim):**
> Review PR #74 sudah dijalankan. Aku mengerahkan 3 sesi agent untuk melakukan nya. Sekarang semuanya masih proses

**Jawaban atas 3 pertanyaan (verbatim):**

| Pertanyaan | Jawaban pemilik |
|---|---|
| *"Dua reviewer masih berjalan. Kapan koreksi dikerjakan?"* | **"Terserah kamu yang terbaik gimana. Yang penting semuanya harus dibereskan dan dimatangkan"** |
| *"R1 dieskalasikan reviewer kepadamu: 2 warning karena pegangan pengguna (W-01) belum ada. Mana yang kamu pilih?"* | **"Aku kurang paham soal ini. Aku minta saran terbaik dari kamu"** |
| *"Aturan 3 hakim belum ada. Bagaimana verdict yang berbeda harus diputuskan?"* | **"Selagi ada yang merah, maka harus diperbaiki"** |

### Verdict hakim ke-1 (sudah masuk, head yang dinilai `3543612`)

**MERAH — "Jangan merge"**, dan **menyatakan dirinya parsial** (*"ini laporan temuan terukur, bukan review
lengkap"*). Tiga temuan, **semuanya terkonfirmasi oleh penulis**:

| | Temuan | Status |
|---|---|---|
| **R1** | 2 warning validator vs syarat prompt "PASS, 0 warning" | **benar**; dieskalasikan ke pemilik → item **T-33** |
| **R2** | alat mencetak 74 skenario, dokumen menulis 73 | **benar, kesalahan penulis** → diperbaiki giliran ini |
| **R3** | pembangkit prompt mencampur diff merge-base dengan diff langsung base→head (selisih 4 berkas) | **benar**; reviewer **tidak** menuduh penulis menghapus bukti → item **T-34** |

### Dua cacat tambahan yang ditemukan penulis sendiri (di luar cakupan verdict)

**D-1 — `tools/ambil_verdict.py` membaca verdict MERAH ini sebagai "BERSIH".** Reproduksinya terukur:
kata yang cocok adalah `bersih` pada **karakter 5646 dari 6315**, di dalam kalimat larangan
*"…agar diff menjadi bersih"*, sedangkan kata **MERAH ada di karakter 35**. Dua penyebab: kosakata regex
**tidak memuat MERAH/HIJAU sama sekali** (hanya kosakata audit-isi), dan `.search()` mengambil kecocokan
**pertama di mana saja**. **Fail-open pada instrumen keselamatan**: "Jangan merge" dilaporkan "BERSIH".

**D-2 — tidak ada penjaga sinkronisasi jumlah skenario FI.** `grep -n "Jumlah" tools/test_failure_injection.py`
**tidak mengembalikan apa pun**, jadi angka di dokumen adalah **salinan tangan**. **R2 bukan salah ketik —
R2 adalah gejala dari tidak adanya penjaga**, dan akan terulang setiap kali sistem baru ditambahkan.

### INSIDEN #5 — platform meng-CLONE ULANG repo di tengah sesi

| Tahap | Fakta |
|---|---|
| Gejala | HEAD lokal jatuh ke `eff7afa` (titik cabang awal), **37 berkas** tampak belum di-commit |
| Diagnosa | reflog **hanya 2 entri**: `clone` lalu `checkout: moving from main to arena/…`. `shallow=true`, `rev-list count = 1`, **objek `17ada02` tidak ada lokal**. Jadi `.git` **dibangun ulang dari awal** dan branch lokal dibuat dari **base yang salah** |
| Yang utuh | **working tree** — 31 berkas baru ada di disk sebagai *untracked*, 6 termodifikasi |
| Pemulihan | `git fetch --unshallow --prune` → `git fetch origin <branch>:refs/remotes/origin/<branch>` → **verifikasi remote = 17ada02** → `git reset --mixed origin/<branch>` (**bukan** `--hard`, **bukan** rebase) |
| Hasil | HEAD = remote = `17ada02` · shallow false · 616 commit · **0 berkas kotor** · **0 berkas berbeda isi** · 9 alat PASS |
| Yang hilang | **tidak ada** |

**Ini kejadian ke-5 pola riwayat-git-rusak dalam satu hari**, dan yang **paling parah**: sebelumnya hanya
`.git/shallow` yang muncul, kali ini **seluruh riwayat lokal diganti**. **Aturan yang sudah ada terbukti
benar** — periksa riwayat **sebelum dan sesudah** operasi, dan jangan pernah `--hard`/rebase/
`--allow-unrelated-histories`.

## Giliran 14 (18 September 2026) — pemilik melaporkan 3 hakim selesai; yang sampai ke GitHub hanya 1

**Pesan pemilik, VERBATIM:**

> Semua hakim sudah selesai. Namun sayang nya salah satu dari 3 hakim itu melakukan nya di branch yang sama
> dengan hakim lain, jading mungkin tertimpa. Coba tolong periksa

### Yang diperiksa (bukan diiyakan, diukur)

| # | Pertanyaan | Cara memeriksa | Hasil terukur |
|---|---|---|---|
| 1 | Berapa verdict yang benar-benar ada di PR #74? | daftar komentar + review resmi + komentar baris lewat API | **4 komentar** = 3 milik penulis + **1 verdict** (hakim ke-1, MERAH, 17:37Z). **Review resmi: 0. Komentar baris: 0.** |
| 2 | Apakah verdict ke-2/ke-3 nyasar ke PR lain? | 30 komentar terbaru di **seluruh repo** | Yang baru hanya verdict **PR #75 (HIJAU)** dan **PR #76 (MERAH)** — keduanya sistem-konten-kreator |
| 3 | Apakah ada branch berisi pekerjaan review PR #74? | fetch **63 ref** (tanpa `--depth`, supaya tidak shallow) lalu `git log --all` + `git grep` isi berkas per tip | Sebutan review PR #74 **hanya ada di branch penulis sendiri**. **Nol** di 62 ref lain |
| 4 | Apakah ada bukti branch tertimpa/di-force-push? | bandingkan blob tiap berkas log sesi reviewer (slot 19–23) di semua ref | Tiap slot ada di **tepat satu branch** dengan **satu versi blob**. **Tidak ada dua versi bersaing** |
| 5 | Apakah branch PR #74 disusupi commit asing? | daftar 33 commit PR + penulisnya | **33/33 milik penulis**; head tetap `ac25de0` = `refs/pull/74/head` |
| 6 | Siapa pemilik slot 21/22/23? | baca log sesi di branch masing-masing | **Reviewer PR #75**, **pencatat Run 21**, **reviewer PR #76** — semuanya sistem-konten-kreator. Slot 21 menulis eksplisit: *"#74 di luar scope sesi ini, tidak disentuh"* |

### Kesimpulan, termasuk batasnya

**Terkonfirmasi:** hanya **1 dari 3** verdict yang sampai. **Tidak terkonfirmasi:** dugaan penimpaan branch —
**tidak ada jejaknya** di sisi repo. **Batas kejujuran:** kalau ada hakim yang mendorong ke branch bersama
lalu tertimpa push berikutnya **tanpa pernah membuka PR**, objeknya jadi tak terjangkau dan **GitHub tidak
membukanya** — jadi "tidak ada jejak" **tidak membuktikan** "tidak pernah terjadi". Yang bisa dipastikan:
**tidak ada yang bisa dipulihkan dari sisi penulis.**

### Yang lahir dari pemeriksaan ini (dieksekusi, bukan dicatat)

- **D-3 — keheningan terbaca sebagai persetujuan.** Alat menghitung **setiap komentar** sebagai slot hakim,
  jadi 3 komentar penulis ikut terhitung dan keluarannya berbunyi *"1 dari 4 verdict bukan hijau"* — terdengar
  seperti tiga hakim lain tidak menemukan apa-apa, padahal yang terjadi **2 verdict hilang**. Diperbaiki:
  klasifikasi slot (judul menyebut penulis → bukan slot, diperiksa **lebih dulu** dari token laporan) +
  **kuorum `--harapkan N`**. Pada PR nyata kini tercetak **"KUORUM BELUM TERPENUHI (1/3 slot terbaca,
  2 hakim belum menyerahkan atau tidak terbaca) — MENAHAN merge"**.
- **D-4 — kanal utama alat ini crash dan uji sendiri tidak tahu.** `cetak_issue` memakai `kumpul` yang
  **tidak pernah didefinisikan** di fungsi itu → `NameError` setiap kali isu punya komentar. Kanal `--terbaru`
  (kanal **utama**) ikut lewat fungsi itu. **`--uji` tidak menangkapnya karena hanya menguji fungsi murni,
  tidak pernah fungsi kanal.** Diperbaiki + **smoke test kanal** ditambahkan.
- **Kedua perbaikan dibuktikan load-bearing dengan merusak kodenya sungguhan:** mengembalikan cacat D-4 →
  uji **GAGAL** dengan `NameError`; mematikan saringan slot → **7 GAGAL**. Lalu dipulihkan byte-identik.
  `--uji` kini **29/29**.
- **Protokol butir 8–10:** verdict **wajib mendarat sebagai komentar PR sebelum sesi hakim ditutup** (laporan
  yang hanya hidup di `/tmp` dan di chat sesi **tidak bisa diverifikasi siapa pun**, termasuk pemiliknya);
  **kuorum dihitung, bukan diasumsikan**; **verdict hilang = pekerjaan belum dilakukan dan wajib diulang**,
  tidak ada jalur "dianggap hijau karena tidak ada kabar".
- **T-35 dibuka** (TERTAHAN): ulangi 2 hakim pada head hasil koreksi, bukan `3543612`.
- **T-33 diputuskan atas delegasi pemilik:** jalan **(b)** — buat pegangan W-01 sungguhan. Status TERTAHAN →
  TERBUKA. Pemilik boleh membatalkan.

### Kegagalan buatan sendiri ke-6 dan ke-7

**D-3b:** komentar penulis yang **mengumumkan perbaikan D-3** justru **ikut terhitung sebagai slot hakim**,
karena judulnya memuat kata *"verdict"* polos — PR #74 sempat terbaca punya **2 slot**. **Tertangkap karena
alat dijalankan ULANG SESUDAH komentar ditempel**, bukan sebelumnya. Akar diperbaiki: kosakata penyaring
dibatasi pada **token putusan sungguhan**; kata "verdict"/"temuan"/"review" polos tidak cukup. **Batas
platform dicatat di kode:** semua sesi memakai **satu identitas bot**, jadi penulis dan hakim **tidak bisa
dibedakan dari author** — karena itu klasifikasi judul + kuorum adalah satu-satunya jalan. **Dibuktikan:**
dilonggarkan → 3 uji GAGAL **dan** sinyal kuorum hilang di PR nyata.

**Ke-7:** ambang mutasi ditulis `>=2` padahal hanya 1 kasus yang bergantung padanya → **`--uji` menolak
ambang salah itu**. Ambang terlalu tinggi berteriak salah; terlalu rendah diam saat seharusnya berteriak.

### INSIDEN #6 — re-clone platform, kedua kalinya

Ditemukan **karena pemeriksaan ini membandingkan remote dengan lokal**, bukan karena gejala: `HEAD` lokal
= `eff7afa` (titik cabang awal) sementara remote = `ac25de0`, `shallow=true`, `rev-list count = 1`,
reflog 2 entri, objek `ac25de0` **tidak ada lokal**, 40 berkas tampak berubah. Pemulihan:
`fetch --unshallow --prune` → verifikasi remote = head yang didorong → `reset --mixed` (**bukan** `--hard`)
→ **0 berkas kotor, 0 berkas berbeda isi, 617 commit**. **Tidak ada yang hilang.**
**Yang berubah dari insiden #5: kali ini terdeteksi oleh pemeriksaan rutin, bukan oleh kegagalan.**

## Giliran 15 (18 September 2026) — pemilik tidak paham arahannya, dan itu temuan tentang cara agent melapor

**Pesan pemilik, VERBATIM:**

> Maaf, aku kurang paham. Sekarang aku harus apa? Klo aku harus buka 3 sesi hakim yang sebelumnya, aku
> merasa sulit, karena itu tidak semuanya aku yang buka. Ada yang dibuka sama temen aku. Jadi klo emang
> perlu, aku mending ngulang buka sesi hakim dari awal. Tapi aku ga paham sebenernya yang kamu arahkan
> itu sekarang aku harus apa

### Ini kesalahan komunikasi agent, bukan kekurangan pemilik

Laporan giliran sebelumnya berisi tabel 6 baris pemeriksaan git, istilah *ref*, *blob*, *force-push*,
*shallow*, dan sha. Pemilik sudah menyatakan sejak awal **"jujur, aku ga punya basic di coding"** dan
menuntut **bahasa awam**. Jadi pertanyaan *"sekarang aku harus apa?"* adalah **bukti bahwa laporan itu
gagal pada satu-satunya pembaca yang harus bisa memakainya**. Yang diperbaiki bukan penjelasannya —
**strukturnya**:

| Sebelum | Sesudah |
|---|---|
| kesimpulan di akhir, sesudah bukti | **satu baris keputusan lebih dulu**: "sekarang kamu tidak perlu melakukan apa-apa" |
| semua langkah campur (milik agent dan milik pemilik) | **tabel 3 langkah dengan kolom "Siapa"**, jadi langkah milik pemilik kelihatan satu |
| istilah git di badan jawaban | istilah dipindah ke bagian penjelasan, bukan ke instruksi |

### Tiga hal yang diputuskan dari pesan ini

1. **"Mending ngulang buka sesi hakim dari awal" → dikonfirmasi sebagai jalan yang LEBIH BAIK, bukan
   sekadar diizinkan.** Alasannya disebut, bukan hanya disetujui: sesi baru masing-masing dapat branch
   sendiri jadi tidak mungkin saling menimpa · yang dinilai versi yang sudah dikoreksi, bukan head basi
   `3543612` · tidak perlu mencari atau memahami sesi lama. **Agent tidak boleh mengiyakan pilihan
   pemilik tanpa menilai** (tuntutan lama: *"Aku mau kamu kritisi, bukan asal meng-iya-kan saja"*) —
   dalam hal ini pilihannya memang benar, dan alasannya diberikan.
2. **"Ada yang dibuka sama temen aku" → tidak mengubah tindakan apa pun.** Siapa pun yang membuka sesi
   hanya menempel teks yang sama. Justru ini memperkuat alasan aturan baru butir 8 (verdict wajib
   mendarat sebagai komentar PR): kalau orang lain yang membuka sesinya, satu-satunya tempat hasilnya
   bisa dipastikan sampai adalah kanal repo, bukan chat pribadi.
3. **Putaran koreksi dimulai tanpa menunggu**, karena pemilik sudah mendelegasikan urutan (giliran 13)
   dengan syarat "semuanya harus dibereskan dan dimatangkan". Menunggu konfirmasi tambahan hanya
   menambah giliran tanpa menambah informasi.

### Yang dikerjakan giliran ini: temuan R1 DITUTUP

**Jalan yang dipilih: (b) membuat pegangan penggunanya, bukan (a) melonggarkan syarat "0 peringatan".**
Dua berkas baru di folder sistem-undangan: PANDUAN_PENGGUNA.md (331 baris, 12 bagian) dan
PROMPT_ENTRI_UNIVERSAL.md (54 baris). **Blok prompt keduanya identik karena dibangkitkan dari satu
variabel yang sama dan di-`assert`**, bukan karena dilihat mata — aturan template adalah dua-file-satu-
sumber, dan selisih diam-diam antar keduanya pernah jadi temuan audit di repo ini.

**Hasil pada alat penilai: `tools/validate_repo.py` berubah dari 2 warning menjadi `WARNINGS: none`.**
Warning-nya hilang **karena pegangannya ada**, bukan karena syaratnya dilonggarkan — persis yang
diminta reviewer waktu memperingatkan *"jangan sekadar menyembunyikan warning atau membuat manual kosong
demi lolos"*.

**Tiga hal yang ditemukan di sela pekerjaan ini, dan semuanya dieksekusi:**

- **Alat penjaring manual melaporkan 0 kandidat pada kedua berkas baru — dan angka itu tidak dipercaya
  begitu saja.** Dijalankan **kontrol positif** bersamaan: pegangan sistem-building-aplikasi tetap
  menjaring **2** kandidat, sistem-klinik **4**, sistem-presentasi (yang sudah lulus audit manusia) **0**.
  Tanpa kontrol, "0" tidak bisa dibedakan dari "alatnya tidak memeriksa apa-apa".
- **Benih lebih ketat dari sistem nyata.** Validator **benih** yang dibangkitkan `tools/build_template.py`
  **sudah mewajibkan** kedua berkas manual, sedangkan validator sistem nyata hanya mewajibkan 2 berkas.
  Daftar wajib validator mandiri diperketat 2 → 4 berkas, supaya **W-01 ditegakkan dari dalam folder
  sendiri** — penting justru saat sistem diunduh jadi repo tersendiri dan validator level repo tidak ikut.
  **Diuji mutasi:** satu manual dipindah keluar → `exit 1` menyebut berkasnya; dikembalikan → `exit 0`.
- **Janji pengukuran di docstring alat penjaring ditutup dengan hasilnya.** Alat itu menulis bahwa
  pengukuran yang sah adalah dijalankan pada korpus yang **belum dipakai menyetel**, "misalnya pegangan
  sistem-undangan saat sistem itu dibangun nanti", dan sampai itu terjadi presisinya dianggap tidak
  diketahui. **Saat itu tiba.** Hasilnya dicatat **beserta batasnya**: 0 kandidat pada korpus baru
  **tidak mengukur presisi maupun recall** — bisa berarti bersih, bisa berarti cacatnya jenis yang tidak
  terjaring, dan alat tidak bisa membedakan keduanya tanpa manusia.

**Yang SENGAJA TIDAK DIKLAIM:** kelulusan pegangan. Syarat 4 Standar Kelulusan Manual **melarang penulis
menyatakan standarnya sendiri terpenuhi**, jadi tidak ada dokumen yang menulis "pegangan ini sudah lulus".
Yang dicatat adalah keadaannya (sudah dibuat, 0 kandidat dengan kontrol positif) dan yang masih kurang
(audit lensa kemudahan pakai oleh sesi independen + **uji pemakaian nyata oleh pemilik** — kalau pemilik
harus bertanya saat memakainya, standarnya belum lulus dan pertanyaannya adalah temuan).

### Tiga kegagalan buatan sendiri yang tertangkap alat repo giliran ini

| # | Kesalahan | Yang menangkap |
|---|---|---|
| 8 | Menulis rujukan **ber-backtick** ke path di dalam folder sistem dari dokumen `_meta/` — path itu tidak ada di ekstrak template, jadi **pin R7 bergeser dari 5 ke 6**. Ini pola yang **sudah pernah terjadi 7 kali** dan aturannya sudah tertulis | `test_failure_injection.py` (R7) |
| 9 | Mengutip **angka korpus** ("497 rujukan", "122 dokumen aktif") di sel Bukti Log Evolusi — angka itu bergerak setiap kali log sesi ditulis, jadi tidak bisa jadi bukti permanen | `validate_repo.py` |
| 10 | Menandai **T-33 SELESAI padahal commit-nya belum ada** — menutup utang tanpa sha | `validate_repo.py`, dengan pesan yang menyebut jalan keluarnya: *"kalau fix-nya belum di-commit, biarkan TERBUKA dan tulis sha-nya nanti"* |

Ketiganya **diperbaiki mengikuti petunjuk alatnya**, bukan dengan melonggarkan alatnya: backtick dihapus
(provenance tanpa backtick), angka korpus dihapus dari sel Bukti, dan **T-33 dikembalikan ke TERBUKA**
untuk ditutup di commit berikutnya beserta sha-nya.

### Yang masih terbuka

**Temuan R3 (T-34) BELUM dikerjakan dan dinyatakan belum** — rombak pembangkit prompt review supaya
memisahkan diff PR-terhadap-merge-base dari diff langsung base-tip→head, dan menyebut head yang hendak
diputuskan secara eksplisit. **Hakim tidak boleh diulang sebelum ini selesai**, karena mengulang sekarang
berarti membuang satu dari maksimal dua putaran untuk temuan yang sudah diketahui.
