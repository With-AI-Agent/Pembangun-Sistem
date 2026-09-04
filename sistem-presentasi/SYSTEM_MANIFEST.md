# System Manifest — Sistem Presentasi

> Manifest ini adalah kartu identitas dan kontrak navigasi sebuah sistem domain. Ini bukan pengganti dokumen instruksi atau living document.

## Identitas

- **Nama sistem:** Sistem Presentasi
- **Tujuan utama:** Mengubah bahan (dokumen pengguna, atau topik yang perlu diriset) menjadi berkas presentasi yang setia pada sumbernya, strukturnya berbasis bukti, tampilannya konsisten, dan prosesnya bisa dilanjutkan sesi lain
- **Pengguna/consumer:** Pemakai = pengguna repo ini. Consumer hasil akhir = audiens presentasi (misal dosen penguji sidang skripsi)
- **Pemilik keputusan:** Pengguna repo ini
- **Versi:** `0.1.0-kerangka`
- **Status:** `Proposed` — `00_RENCANA_KERANGKA.md` disetujui pengguna 4 Sep 2026 tapi **sengaja belum di-merge**; dokumen instruksi aktif belum ada
- **Tanggal dibuat:** 4 September 2026 (UTC)
- **Audit terakhir:** belum ada
- **Quality protocol:** `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` (default aktif)

## Bentuk Sistem

- **Bentuk:** [ ] Bertingkat  [ ] Flat  [ ] Siklus  [x] Gabungan
  - **Bertingkat** di lapisan struktural: Paket Ketentuan (opsional) → Aset Gaya (opsional) → Deck (wajib). Kedua lapisan atas **sengaja opsional**; yang tidak boleh kosong hanya lapisan Deck
  - **Siklus** di lapisan produksi: Perancangan → Pemahaman Bahan → Outline + Rencana Visual → Produksi Berkas → Verifikasi
- **Unit kerja utama:** 1 deck = 1 presentasi = 1 folder `deck-aktif/<nama-deck>/`
- **Kriteria satu unit selesai:** ketiga gerbang (G1 bila wajib, G2, G3) sudah disetujui; `DAFTAR_GAMBAR.md` lengkap untuk tiap gambar; verifikasi Tahap 5 tercatat beserta **jalur verifikasi mana yang dipakai**; berkas ada di `keluaran/` dan sudah di-commit + push
- **Titik approval Besar:** **G1** Peta Pemahaman Bahan (wajib bila bahan > 15 halaman ATAU > 5.000 kata ATAU ≥ 8 bagian berstruktur) · **G2** Outline + Rencana Visual (selalu) · **G3** Berkas Final (selalu) · tiap gambar mode M4 satu per satu
- **Titik approval Kecil:** perbaikan salah ketik, penataan folder, penyesuaian warna minor dalam gaya yang sudah dipilih, pemilihan nama deck di awal Tahap 1

## Dokumen Navigasi

- **Entry point:** `START_DI_SINI.md` — **belum dibuat**
- **Dokumen instruksi aktif:** direncanakan di `_sistem/01`…`_sistem/08` — **belum ada satu pun**. Rencana lengkapnya di `00_RENCANA_KERANGKA.md` bagian Rencana Dokumen
- **Living documents:** per deck: `BRIEF.md`, `OUTLINE.md`, `RENCANA_VISUAL.md`, `DAFTAR_GAMBAR.md`, `STATUS.md`. Lintas deck: tiap `PAKET_KETENTUAN` dan `ASET_GAYA`
- **Log keputusan:** wajib ada di tiap living document di atas
- **Ringkasan cadangan:** `_cadangan-claude/RINGKASAN_sistem-presentasi.md` — **belum dibuat** (dibuat setelah struktur stabil)
- **Laporan audit:** belum ada. Diskusi awal tercatat di `DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md`

## Prinsip

| Prinsip meta-sistem | Berlaku? | Cara diterapkan | Alasan jika di-override |
|---|---|---|---|
| Hierarki | Ya, dengan penyesuaian | 3 lapis: Ketentuan → Gaya → Deck. Level bawah merujuk, tidak mengulang | Penyesuaian: lapisan Ketentuan dan Gaya **opsional**. Alasan: pengguna menyatakan semua aspek "tergantung keadaan", jadi mewajibkan aset gaya di muka hanya jadi penghalang untuk bikin satu deck |
| Chaining | Ya, apa adanya | 5 tahap; agent baca hasil tahap sebelumnya langsung dari repo. Tetap wajib berhenti di G1/G2/G3 | — |
| Approval bertingkat | Ya, kriteria spesifik domain | Besar = G1/G2/G3 + tiap gambar M4. Kecil = salah ketik, penataan folder, warna minor, nama deck | — |
| Checkpoint & verifikasi | Ya, **wajib** | `STATUS.md` per deck diperbarui tiap tahap + commit & push. Checkpoint diskusi ringan bila >5 giliran | Tidak boleh di-override: sistem ini dipakai via lmarena (lihat Batasan Platform) |
| Log keputusan | Ya | Di semua living document yang disebut di atas | — |

**Prinsip yang TIDAK diwarisi dari sistem konten kreator:** pemisahan "Konsistensi Visual vs Non-Visual" — `_meta/02_PRINSIP_UNIVERSAL.md` sendiri menyatakan prinsip itu spesifik-domain. Analognya digali sendiri untuk domain ini dan hasilnya: **jejak sumber** (tiap pernyataan → nomor halaman/URL) + **kepatuhan Paket Ketentuan** + **provenance & lisensi tiap gambar**.

## Quality & Evolution

- **Lapisan self-audit sistem:** baca ulang seluruh dokumen sistem, cross-check rujukan, jalankan `tools/validate_repo.py` **setelah cakupan validator diperluas** ke `sistem-presentasi/` (saat ini validator hanya memindai `_meta/*.md` + `PANDUAN_PENGGUNA.md` — jadi "VALIDATION PASSED" **belum** berarti dokumen sistem ini terperiksa)
- **Lapisan verifikasi output:** 3 jalur, dan laporan **wajib menyebut jalur mana yang dipakai** — (a) struktural lewat kode: baca ulang `.pptx`, ukur teks vs placeholder, deteksi kemungkinan meluber, cek gambar tidak menimpa *text frame*; (b) preview HTML hampiran yang dibuka pengguna; (c) pengguna membuka sendiri berkas `.pptx`-nya. Jalur (b) dan (c) **bukan** render PowerPoint
- **Trigger audit:** perubahan aturan di `_sistem/`; kegagalan acceptance test; keluhan pengguna atas hasil deck; sebelum status naik ke `Operational`
- **Level audit default:** Sedang
- **Prosedur rollback:** aturan inti berubah hanya lewat proposal + approval + regression check + rollback plan (pola AT-05). Deck yang gagal tidak diperbaiki dengan mengedit `STATUS.md`-nya
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
    - **Ekstraksi teks Arab dari PDF: BELUM terverifikasi** — uji sintetis tidak konklusif karena font untuk *menulis* PDF ujiku tidak punya glyph Arab (hasilnya titik). Butuh berkas Arab asli (tesisnya) untuk membuktikan. Jalur cadangan yang selalu jalan: render PDF→gambar via PyMuPDF lalu baca dengan visi
    - **Font Arab:** untuk `.pptx` cukup menyebut nama font Arab (mis. Amiri); PowerPoint yang mengganti kalau tidak ada. Untuk preview (PIL/HTML) butuh font Arab + `arabic_reshaper`, **belum diverifikasi**
  - **Jalur unduh eksternal yang TERBUKA:** `api.github.com` bisa (HTTP 200) dan `git` ke GitHub bisa. Yang **diblokir:** `raw.githubusercontent.com` dan host umum via `curl` (`SSL_ERROR_SYSCALL`). Konsekuensi: berkas besar sebaiknya diambil lewat `git fetch` (commit ke branch), bukan lewat raw/API-contents (API contents hanya inline sampai ~1 MB)
- **Prosedur recovery:** `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` + `STATUS.md` per deck. **Catatan:** protokol itu masih punya 2 celah terbuka (Q-O2 kriteria "alasan" mengulang tahap approved, Q-O3 interval "Waktu pembaruan") — lihat `_meta/_internal/arsip-pilot-002-2026-09-03/README.md`. Usulan penutupannya ada di `00_RENCANA_KERANGKA.md` bagian "Satu butir yang TIDAK boleh kuputuskan sendiri", **menunggu approval pengguna**

## Batasan Platform

- **Dipakai via lmarena?** **Ya**
- **Jika Ya:** rujuk ke `_meta/PLATFORM_LMARENA.md`. Terapkan checkpoint tiap tahap + commit & push + checkpoint diskusi ringan bila diskusi >5 giliran. Alasan kausal: tanpa commit+push sesi baru tidak bisa melanjutkan (FI-03); tanpa checkpoint diskusi, diskusi panjang bisa hilang saat crash.
  - **Bukti nyata dari sesi pembangunan sistem ini (4 Sep 2026):** workspace **di-clone ulang antar giliran sebanyak dua kali**, dan commit lokal hilang sementara isi file selamat. Pemulihannya: `git ls-remote` untuk tahu tip server, lalu `git reset --mixed <tip>` sebelum commit berikutnya, supaya riwayat tidak bercabang. Ini alasan tambahan kenapa "commit tiap tahap + push" bukan birokrasi di sistem ini.

## Acceptance

- [ ] Semua dokumen wajib tersedia — **belum**: `_sistem/01`…`08`, `_generator/G1`–`G3`, `_template/T1`–`T9`, `START_DI_SINI.md` semuanya belum ada
- [ ] Semua dependency valid — **sebagian**: keempat library terbukti bisa diinstall, tapi belum ada skrip yang memasang dan memverifikasinya sebagai bagian sistem
- [ ] Status dan versi sudah diperbarui — ya, `0.1.0-kerangka` / `Proposed`
- [ ] Approval yang diperlukan sudah ada — **sebagian**: `00_RENCANA_KERANGKA.md` disetujui; proposal Q-O2/Q-O3 **belum**
- [ ] Audit terakhir tercatat — **belum ada audit**
- [ ] Ringkasan cadangan sinkron — **belum dibuat**
