# System Manifest — Sistem Presentasi

> Manifest ini adalah kartu identitas dan kontrak navigasi sebuah sistem domain. Ini bukan pengganti dokumen instruksi atau living document.

## Identitas

- **Nama sistem:** Sistem Presentasi
- **Tujuan utama:** Mengubah bahan (dokumen pengguna, atau topik yang perlu diriset) menjadi berkas presentasi yang setia pada sumbernya, strukturnya berbasis bukti, tampilannya konsisten, dan prosesnya bisa dilanjutkan sesi lain
- **Pengguna/consumer:** Pemakai = pengguna repo ini. Consumer hasil akhir = audiens presentasi (misal dosen penguji sidang skripsi)
- **Pemilik keputusan:** Pengguna repo ini
- **Versi:** `0.4.2`
- **Tahap:** siap-pakai
- **Status:** `Built & terverifikasi; teraudit 1x` — kerangka disetujui 4 Sep 2026; dokumen instruksi aktif lengkap; **merge ke main diminta pengguna 5 Sep 2026** (PR #9); **audit independen Sedang selesai 5 Sep 2026** (sesi agent baru) — 11 temuan (2×P1 skrip, 3×P2 state deck, 6×P3) **semua diperbaiki di v0.3.0**; pegangan pengguna ditambahkan (v0.3.0); **mekanisme log sesi (`LOG_SESI`) diturunkan self-contained ke `_sistem/11_LOG_SESI.md` + prompt pembuka/penutup diperbarui (v0.4.0, 5 Sep 2026)**
- **Tanggal dibuat:** 4 September 2026 (UTC)
- **Audit terakhir:** 5 Sep 2026 — (a) audit otomatis: `validate_system.py` exit 0, `qa_deck.py` 14 slide exit 0, `install_deps.sh` exit 0; (b) **audit independen Sedang** oleh sesi agent baru (`arena/01a0706d`): laporan `_meta/_internal/AUDIT_SISTEM_PRESENTASI_2026-09-05.md` — verifikasi: rebuild reproducible (konten identik), G-1 gambar bebas teks via visi, spot-check visi hal 6/66–67/151, commit jejak valid; temuan AP-01…AP-11 diperbaiki di v0.3.0.
- **Quality protocol (versi sistem ini — self-contained):** trigger audit + level default + prosedur rollback dirinci di bagian "Quality & Evolution" manifest ini; verifikasi output oleh `_sistem/04_QA_PRODUKSI.md` + `qa_deck.py`. Induk: `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` = **provenance saja** (sistem harus tetap berfungsi penuh bila folder diunduh standalone)

## Bentuk Sistem

- **Bentuk:** [ ] Bertingkat  [ ] Flat  [ ] Siklus  [x] Gabungan
  - **Bertingkat** di lapisan struktural: Paket Ketentuan (opsional) → Aset Gaya (opsional) → Deck (wajib). Kedua lapisan atas **sengaja opsional**; yang tidak boleh kosong hanya lapisan Deck
  - **Siklus** di lapisan produksi: Perancangan → Pemahaman Bahan → Outline + Rencana Visual → Produksi Berkas → Verifikasi
- **Unit kerja utama:** 1 deck = 1 presentasi = 1 folder `deck-aktif/<nama-deck>/`
- **Kriteria satu unit selesai:** ketiga gerbang (G1 bila wajib, G2, G3) sudah disetujui; `DAFTAR_GAMBAR.md` lengkap untuk tiap gambar; verifikasi Tahap 5 tercatat beserta **jalur verifikasi mana yang dipakai**; berkas ada di `keluaran/` dan sudah di-commit + push
- **Titik approval Besar:** **G1** Peta Pemahaman Bahan (wajib bila bahan > 15 halaman ATAU > 5.000 kata ATAU ≥ 8 bagian berstruktur) · **G2** Outline + Rencana Visual (selalu) · **G3** Berkas Final (selalu) · tiap gambar mode M4 satu per satu
- **Titik approval Kecil:** perbaikan salah ketik, penataan folder, penyesuaian warna minor dalam gaya yang sudah dipilih, pemilihan nama deck di awal Tahap 1

## Dokumen Navigasi

- **Entry point:** `START_DI_SINI.md` — **sudah dibuat** (5 Sep 2026), self-contained agar sistem bisa diekstrak jadi repo tersendiri
- **Pegangan pengguna:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` — **sudah dibuat** (5 Sep 2026, v0.3.0) sesuai `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`: prompt pembuka universal (satu prompt → agent terorientasi penuh) + prompt penutup sesi
- **Dokumen instruksi aktif:** `_sistem/01`–`11` **sudah ada**: 01 aturan desain/isi/gambar, 02 knowledge desain+riset+bahasa+layout, 03 paham kebutuhan/tujuan, 04 QA per-produksi, 05 anti-ngarang, 06 desain berbasis bukti, 07 mode gambar+lisensi, 08 perancangan rekomendasi, 09 pemahaman bahan, 10 render+verifikasi, **11 log sesi berkelanjutan (`LOG_SESI`) — self-contained** (5 Sep 2026). `_generator/G1–G3`, `_template/T1–T9`, `ACCEPTANCE_TESTS.md`, `validate_system.py` sudah ada.
- **Living documents:** per deck: `BRIEF.md`, `OUTLINE.md`, `RENCANA_VISUAL.md`, `DAFTAR_GAMBAR.md`, `PERKATAAN_PEMILIK_VERBATIM.md`, `STATUS.md`. Lintas deck: tiap `PAKET_KETENTUAN` dan `ASET_GAYA`
- **Log keputusan:** wajib ada di tiap living document di atas
- **Ringkasan cadangan:** `_cadangan-claude/RINGKASAN_sistem-presentasi.md` — dibuat 5 Sep 2026 (dipindah ke lokasi root 5 Sep 2026, AP-10)
- **Laporan audit:** `_meta/_internal/AUDIT_SISTEM_PRESENTASI_2026-09-05.md` (independen, Sedang, 5 Sep 2026). Diskusi awal tercatat di `DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md`

## Prinsip

| Prinsip meta-sistem | Berlaku? | Cara diterapkan | Alasan jika di-override |
|---|---|---|---|
| Hierarki | Ya, dengan penyesuaian | 3 lapis: Ketentuan → Gaya → Deck. Level bawah merujuk, tidak mengulang | Penyesuaian: lapisan Ketentuan dan Gaya **opsional**. Alasan: pengguna menyatakan semua aspek "tergantung keadaan", jadi mewajibkan aset gaya di muka hanya jadi penghalang untuk bikin satu deck |
| Chaining | Ya, apa adanya | 5 tahap; agent baca hasil tahap sebelumnya langsung dari repo. Tetap wajib berhenti di G1/G2/G3 | — |
| Approval bertingkat | Ya, kriteria spesifik domain | Besar = G1/G2/G3 + tiap gambar M4. Kecil = salah ketik, penataan folder, warna minor, nama deck | — |
| Checkpoint & verifikasi | Ya, **wajib** | `STATUS.md` per deck diperbarui tiap tahap + commit & push. **Log sesi berkelanjutan** (`LOG_SESI` — aturan self-contained di `_sistem/11_LOG_SESI.md`): dicatat setelah tiap pertukaran yang menghasilkan informasi baru, bukan checkpoint periodik berbasis ambang | Tidak boleh di-override: sistem ini dipakai via lmarena (lihat Batasan Platform) |
| Log keputusan | Ya | Di semua living document yang disebut di atas | — |
| Self-contained / portabel | **Ya (wajib)** | Semua aturan yang benar-benar dipakai (desain, kedalaman isi, gambar, skrip build, template) diturunkan ke dalam `sistem-presentasi/` — lihat `_sistem/01_ATURAN_DESIGN_ISI_GAMBAR.md`; rujukan `_meta/` hanya provenance | Dinyatakan pengguna 5 Sep 2026: tiap sistem akan diunduh & dijadikan **repo standalone** terpisah dari meta-sistem, jadi harus berfungsi penuh tanpa `_meta/` |

**Prinsip yang TIDAK diwarisi dari sistem konten kreator:** pemisahan "Konsistensi Visual vs Non-Visual" — `_meta/02_PRINSIP_UNIVERSAL.md` sendiri menyatakan prinsip itu spesifik-domain. Analognya digali sendiri untuk domain ini dan hasilnya: **jejak sumber** (tiap pernyataan → nomor halaman/URL) + **kepatuhan Paket Ketentuan** + **provenance & lisensi tiap gambar**.

## Quality & Evolution

- **Lapisan self-audit sistem:** baca ulang seluruh dokumen sistem, cross-check rujukan, jalankan `_sistem/validate_system.py` — **ini alat self-audit yang benar-benar lokal** (ikut folder, jalan di repo standalone). Bila folder ini berada DI DALAM repo master, tambahkan `tools/validate_repo.py` (cakupan dokumen aktif `sistem-presentasi/` diperluas 5 Sep 2026, AP-11; validator master = provenance/konteks, BUKAN dependensi operasional — koreksi klaim self-contained, review PR #11 F6). Deck living documents tetap diperiksa oleh `validate_system.py` sistem ini (out of scope validator meta, sengaja).
- **Lapisan verifikasi output:** 3 jalur, dan laporan **wajib menyebut jalur mana yang dipakai** — (a) struktural lewat kode: baca ulang `.pptx`, ukur teks vs placeholder, deteksi kemungkinan meluber, cek gambar tidak menimpa *text frame*; (b) preview HTML hampiran yang dibuka pengguna; (c) pengguna membuka sendiri berkas `.pptx`-nya. Jalur (b) dan (c) **bukan** render PowerPoint
- **Trigger audit:** perubahan aturan di `_sistem/`; kegagalan acceptance test; keluhan pengguna atas hasil deck; sebelum status naik ke `Operational`
- **Level audit default:** Sedang
- **Prosedur rollback:** aturan inti berubah hanya lewat proposal + approval + regression check + rollback plan (pola AT-05). Deck yang gagal tidak diperbaiki dengan mengedit `STATUS.md`-nya
- **Pengeluaran jadi repo mandiri:** sistem ini harus tetap lolos validasi ketika foldernya dikeluarkan jadi repo sendiri — protokol + cara mengujinya di `_meta/PAKET_REPO_MANDIRI.md` (repo master). *(Catatan: sistem ini tidak punya berkas QA terpisah — protokol QA-nya memang hidup di bagian ini, jadi baris rujukannya ditaruh di sini.)*
- **Override quality protocol:** Tidak ada

## Dependency dan Risiko

- **Dependency eksternal:** `python-pptx` (+ Pillow, lxml) untuk `.pptx` · `pypdf` untuk PDF · `python-docx` untuk `.docx` · `matplotlib` untuk grafik. Semua **tidak terpasang default** tapi **terbukti bisa diinstall** dari PyPI
- **Data yang wajib ada:** bahan sumber per deck di `deck-aktif/<nama>/bahan/`; `BRIEF.md` terisi penuh sebelum Tahap 4
- **Risiko utama:**
  1. **Agent mengarang** — risiko terbesar, karena fitur "riset internet untuk isi" berkonflik langsung dengan syarat "tidak boleh ngarang". Diredam oleh jejak sumber wajib + acceptance test urutan #1
  2. **Klaim kelengkapan yang tidak bisa diverifikasi** — diredam oleh tabel cakupan + hitungan + spot-check acak
  3. **Pelanggaran hak cipta gambar** — alat pencari gambar **tidak mengembalikan metadata lisensi** dan hasil teratas uji justru Getty Images/Veranda. Diredam oleh gerbang lisensi M4 + `DAFTAR_GAMBAR.md`
  4. **Gambar AI disangka bukti** — diredam oleh larangan menggambarkan data + label "ilustrasi AI" yang terlihat di slide
  5. **Slide kaku tidak bisa diedit** — diredam oleh Aturan G-1 (teks tidak boleh tergoreng jadi gambar)
- **Batasan yang diketahui (semua terverifikasi 4 Sep 2026, bukan asumsi):**
  - **Tidak bisa** render `.pptx` → gambar/PDF; `libreoffice`/`pandoc` tidak ada dan **tidak bisa diinstall** (`deb.debian.org` tidak terjangkau)
  - **OCR tersedia lewat visi model**, bukan lewat `tesseract` (dikoreksi 4 Sep 2026 setelah pengguna mengoreksi). Terbukti: gambar uji berisi kode `XK-4471-QZ` terbaca sempurna lewat `read_file`. `PyMuPDF` bisa merender PDF (termasuk hasil scan) jadi gambar **tanpa poppler**, sehingga PDF scan **bisa** diproses lewat jalur render + visi. Catatan: verifikasi via visi harus dilakukan ulang oleh tiap sesi, tidak diwarisi dari sesi sebelumnya
  - **Tidak bisa** unduh gambar via `curl` (`SSL_ERROR_SYSCALL`, HTTP 000) — gambar internet hanya lewat alat pencari
  - `/tmp` **tidak persisten** antar langkah → semua artefak wajib masuk repo
  - Alat pencari gambar menulis ke **root repo** secara default → wajib dipindahkan ke folder deck dan dibersihkan
  - **Bahasa dokumen sumber belum tentu Latin.** Kasus nyata pertama (tesis yang diunggah 4 Sep 2026) berbahasa **Arab** (RTL). Status per komponen:
    - **Menulis Arab ke `.pptx` (RTL): TERBUKA/TERVERIFIKASI** — python-pptx menyimpan teks Arab sebagai Unicode + atribut `rtl="1"` + font complex-script `a:ea` + rata-kanan `algn="r"` (semua dicek ada di XML slide). Pembentukan huruf (shaping) dilakukan oleh PowerPoint, bukan oleh agent
    - **Ekstraksi teks Arab dari PDF: BERJALAN tapi TIDAK untuk kutipan presisi** — diuji pada tesis asli (161 halaman). `PyMuPDF`/`pypdf` mengembalikan teks Arab, **tapi urutan kata dalam satu baris teracak** (PDF menyimpan tata letak visual kanan-ke-kiri) dan glyph berbentuk presentasional (ﻫﺬا, bukan هذا). Cocok hanya untuk **indeks/struktur kasar** (deteksi topik, nomor halaman), **bukan** untuk kutipan verbatim
    - **Jalur VISI adalah jalur baca utama untuk Arab: TERVERIFIKASI BENAR** — halaman 23 dirender via PyMuPDF lalu dibaca dengan visi; hasilnya urutan benar dan huruf terbentuk proper (paragraf "منهج البحث" terbaca utuh). Karena itu untuk bahan Arab, `PEMAHAMAN_BAHAN.md` **wajib** diisi lewat jalur visi (render→baca), dengan ekstraksi teks hanya sebagai peta halaman
    - **Font Arab:** untuk `.pptx` cukup menyebut nama font Arab (mis. Amiri); PowerPoint yang mengganti kalau tidak ada. Untuk preview (PIL/HTML) butuh font Arab + `arabic_reshaper`, **belum diverifikasi**
  - **Jalur unduh eksternal yang TERBUKA:** `api.github.com` bisa (HTTP 200) dan `git` ke GitHub bisa. Yang **diblokir:** `raw.githubusercontent.com` dan host umum via `curl` (`SSL_ERROR_SYSCALL`). Konsekuensi: berkas besar sebaiknya diambil lewat `git fetch` (commit ke branch), bukan lewat raw/API-contents (API contents hanya inline sampai ~1 MB)
- **Prosedur recovery:** `STATUS.md` per deck mengikuti kontrak checkpoint (`_template/T6_STATUS.md`: field deterministik `Pekerjaan belum tersimpan` + `Waktu pembaruan` per checkpoint/akhir sesi) + aturan sesi di `_sistem/11_LOG_SESI.md`. Induk: `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` (provenance). **Q-O2 & Q-O3 DITUTUP 5 Sep 2026 di meta v1.3.0** — alasan sah mengulang tahap approved = instruksi pengguna baru (kutip+tanggal) ATAU bukti kecacatan berpath, dicatat di STATUS; `Waktu pembaruan` diisi tiap checkpoint & akhir sesi, format `YYYY-MM-DD — <peristiwa>`

## Warisan (Kontrak)

Status butir `03_KONTRAK_WARISAN.md` meta v1.3.0 untuk sistem ini (disinkronkan 5 Sep 2026; tabel penuh sejak rencana kerangka — format warisan baru):

| Butir | Status | Letak di folder sistem |
|---|---|---|
| W-01 pegangan 2-file | diterapkan | `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` (blok identik) |
| W-02 LOG_SESI | diterapkan | `_sistem/11_LOG_SESI.md` + langkah pembuka/penutup di pegangan |
| W-03 field checkpoint | diterapkan (v0.4.1) | `_template/T6_STATUS.md` + `deck-aktif/*/STATUS.md` |
| W-04 manifest | diterapkan | `SYSTEM_MANIFEST.md` (file ini) |
| W-05 log keputusan dokumen hidup | diterapkan | tabel `## Log Keputusan` per living document + deck |
| W-06 QA 3-lapis | diterapkan (ringkas, di-izinkan desain) | bagian Quality & Evolution manifest + `qa_deck.py`/`validate_system.py` |
| W-07 fakta platform | diterapkan | bagian Batasan Platform di bawah (3 fakta inline) |
| W-08 approval bertingkat | diterapkan | definisi G1/G2/G3 di `00_RENCANA_KERANGKA.md` + `_sistem/` |
| W-09 ringkasan cadangan | diterapkan (disinkronkan 5 Sep) | `_cadangan-claude/RINGKASAN_sistem-presentasi.md` (root master; provenance — dibuat oleh meta, bukan bagian folder standalone) |

## Batasan Platform

- **Dipakai via lmarena?** **Ya**
- **Jika Ya:** rujuk ke `_meta/PLATFORM_LMARENA.md`. Terapkan checkpoint tiap tahap + commit & push + **log sesi berkelanjutan** (aturannya diturunkan self-contained ke `_sistem/11_LOG_SESI.md`). Alasan kausal: tanpa commit+push sesi baru tidak bisa melanjutkan (FI-03); tanpa log sesi, konteks sesi (keputusan, koreksi, fakta penting) hilang permanen saat crash karena agent sesi baru tidak punya akses ke chat sesi lama.
  - **Bukti nyata dari sesi pembangunan sistem ini (4 Sep 2026):** workspace **di-clone ulang antar giliran sebanyak dua kali**, dan commit lokal hilang sementara isi file selamat. Pemulihannya: `git ls-remote` untuk tahu tip server, lalu `git reset --mixed <tip>` sebelum commit berikutnya, supaya riwayat tidak bercabang. Ini alasan tambahan kenapa "commit tiap tahap + push" bukan birokrasi di sistem ini.

## Acceptance

- [x] Semua dokumen wajib tersedia — **YA**: `_sistem/01–10`, `_generator/G1–G3`, `_template/T1–T9`, `START_DI_SINI.md`, `ACCEPTANCE_TESTS.md`, `validate_system.py`, `qa_deck.py` (diverifikasi `validate_system.py` exit 0, 5 Sep 2026)
- [x] Semua dependency valid — `_sistem/install_deps.sh` memasang & memverifikasi python-pptx, Pillow, pypdf, python-docx, matplotlib (exit 0, 5 Sep 2026)
- [x] Status dan versi sudah diperbarui — `0.4.0` / `Built & terverifikasi` (5 Sep 2026)
- [x] Approval yang diperlukan sudah ada — kerangka disetujui 4 Sep 2026; **approval sistem = pengguna meminta merge ke main 5 Sep 2026**. Q-O2/Q-O3 **DITUTUP 5 Sep 2026 di meta v1.3.0** — selaras baris "Prosedur recovery" di atas (penyelarasan pasca review PR #11; sebelumnya baris ini masih menyebut "tetap terbuka")
- [x] Audit terakhir tercatat — 5 Sep 2026 (otomatis: validate_system + qa_deck + install_deps, semua exit 0; **independen Sedang: 11 temuan diperbaiki di v0.3.0**)
- [x] Ringkasan cadangan sinkron — `_cadangan-claude/RINGKASAN_sistem-presentasi.md` (root; dipindah dari `_meta/` 5 Sep 2026, AP-10)
- [x] Pegangan pengguna tersedia di dalam folder sistem — `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` (prompt pembuka + penutup, 5 Sep 2026)
- [x] **Paket repo mandiri LULUS** — 7 Sep 2026, versi `0.4.2`. tools/pack_repo.py mode pemeriksaan hijau (0 pemblokir); hasil pack lolos validator repo (0 warning) + `validate_system.py` di DALAM hasil pack. Protokol: `_meta/PAKET_REPO_MANDIRI.md`; bukti: `ACCEPTANCE_TEST_LOG.md` bagian "Paket repo mandiri"
- [x] Mekanisme log sesi diturunkan ke dalam folder sistem — `_sistem/11_LOG_SESI.md` (self-contained) + langkah 5 prompt pembuka (recovery log `OPEN`) + langkah 2 prompt penutup (menutup log `CLOSED`) + `validate_system.py` memeriksa 11 dokumen (5 Sep 2026, v0.4.0)

## Log Evolusi

*(Bagian ini dibuka 7 Sep 2026. Riwayat versi sebelumnya tetap tercatat apa adanya di bagian Identitas/Status di atas dan di `_meta/INDEKS_SISTEM.md` — tidak disalin ulang ke sini supaya tidak ada dua versi sejarah yang bisa berselisih.)*

| Tanggal | Versi | Perubahan | Bukti |
|---|---|---|---|
| 7 Sep 2026 | **0.4.2** | Sistem menjadi **dapat dibangkitkan jadi repo mandiri**: `_sistem/validate_system.py` diadaptasi seperlunya (daftar periksa disetarakan — baris Versi manifest + field checkpoint `Pekerjaan belum tersimpan` di tiap STATUS deck dan `_template/T6_STATUS.md` + baris `HASIL: PASS/FAIL`), jalur exit code dan baris keluaran lama dipertahankan; gate baru "Paket repo mandiri LULUS"; rujukan protokol 1 baris di bagian Quality & Evolution | `ACCEPTANCE_TEST_LOG.md` bagian "Paket repo mandiri" (perintah + keluaran validator DI DALAM hasil pack, keduanya PASS/0-warning). Protokol: `_meta/PAKET_REPO_MANDIRI.md`. **Menunggu review independen L1** |
