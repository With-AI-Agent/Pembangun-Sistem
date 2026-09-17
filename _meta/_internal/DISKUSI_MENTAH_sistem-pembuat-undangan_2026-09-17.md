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
