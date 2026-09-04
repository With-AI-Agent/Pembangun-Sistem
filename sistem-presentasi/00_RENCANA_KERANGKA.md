# Rencana Kerangka — Sistem Presentasi

> **Status:** DRAFT untuk review pengguna. **Kategori Besar** menurut `_meta/02_PRINSIP_UNIVERSAL.md` — rencana kerangka menentukan seluruh struktur sistem baru, jadi **wajib direview isi lengkapnya** oleh pengguna sebelum merge, bukan cukup konfirmasi ringan.
>
> **Dibuat:** 4 September 2026 (UTC) — sesi `arena/01a06d7b-pembangun-sistem`, mengikuti alur `_meta/01_DISCOVERY_LEVEL_0.md`.
> **Sumber diskusi:** `DISKUSI_MENTAH_DISCOVERY_LEVEL_0.md` (berisi kutipan ide mentah pengguna, hasil riset, dan bukti teknis).
>
> **INI BARU RENCANA.** Setelah di-merge, langkah berikutnya adalah menulis prompt Discovery detail untuk tiap dokumen bertanda **[GENERATOR]** — BUKAN langsung menulis isi sistemnya (`_meta/00_CARA_KERJA_META.md` Langkah 3).

---

## Untuk Siapa/Apa

**Pemakai:** pengguna sendiri, yang butuh presentasi jadi dari bahan yang dia punya (dokumen, catatan, atau topik yang perlu diriset).

**Yang mengonsumsi hasil akhirnya:** audiens presentasi — misalnya dosen penguji di sidang skripsi, atasan di rapat kerja, atau peserta kelas.

**Tujuan akhir kalau sistem ini dipakai dengan benar:** pengguna mendapat berkas presentasi yang (a) **setia pada sumbernya** — tidak ada satu pun pernyataan yang dikarang, (b) **strukturnya terbukti efektif** menurut riset, bukan sekadar selera, (c) **tampilannya konsisten** dan patuh ketentuan institusi kalau ada, dan (d) proses pembuatannya **bisa dilanjutkan sesi lain** kalau sesi terputus.

**Yang secara eksplisit BUKAN tujuan sistem ini:** mengganti pemahaman pengguna atas bahannya sendiri. Sistem ini membuat peta pemahaman yang bisa dicek, tapi tanggung jawab isi tetap di pengguna — karena dialah yang presentasi.

---

## Bentuk Dasar

**Gabungan BERTINGKAT + SIKLUS** — sama pola dasarnya dengan Sistem Konten Kreator, tapi lapisannya ditentukan dari domain presentasi, bukan disalin.

### Unsur BERTINGKAT (lapisan atas, OPSIONAL dan pakai ulang)

```
Lapisan A  PAKET KETENTUAN   ketentuan institusi (kampus/perusahaan) yang
         (opsional)          wajib dipatuhi: logo, warna, font, jumlah slide,
                             struktur wajib. Kalau ada, dia mengikat semua deck.
    ↓ diwarisi
Lapisan B  ASET GAYA         palet, font, master .pptx, gaya ilustrasi.
         (opsional)          Kalau tidak ada, agent mengusulkan (boleh riset
                             internet) lalu MENAWARKAN pilihan ke pengguna.
    ↓ diwarisi
Lapisan C  DECK              1 presentasi = 1 unit kerja. Mewarisi A dan B,
         (wajib)             tidak mengulang isinya — cukup merujuk.
```

Kedua lapisan atas **sengaja opsional**. Alasan: jawaban pengguna atas pertanyaan bentuk adalah "beda-beda, tergantung keadaan" — jadi memaksa pengguna punya aset gaya dulu sebelum bisa bikin satu deck akan jadi penghalang. Yang **tidak** opsional adalah lapisan C.

### Unsur SIKLUS (wajib, dijalankan sekali per deck)

```
Tahap 1  PERANCANGAN      → BRIEF.md terisi & disetujui
Tahap 2  PEMAHAMAN BAHAN  → PEMAHAMAN_BAHAN.md + CHECKLIST_CAKUPAN.md
Tahap 3  OUTLINE + VISUAL → OUTLINE.md + RENCANA_VISUAL.md
Tahap 4  PRODUKSI BERKAS  → keluaran/*.pptx (+ preview.html)
Tahap 5  VERIFIKASI       → HASIL_VERIFIKASI.md + STATUS.md final
```

Agent membaca sendiri hasil tahap sebelumnya langsung dari repo (Prinsip Rantai), **tapi wajib berhenti di gerbang** — lihat bagian Titik Penguncian.

### Konsekuensi penting dari jawaban "semuanya tergantung"

Karena pengguna menyatakan aturan sumber, kedalaman, gaya, dan gerbang semuanya bisa beda per kasus, maka **yang dikunci bukan isinya tapi prosesnya**: setiap deck **wajib** punya `BRIEF.md` yang terisi sebelum produksi boleh dimulai. Brief itulah tempat semua "tergantung" itu diputuskan dan dicatat — sehingga "tergantung" tidak berubah jadi "agent menebak".

---

## Yang Harus Konsisten

Lima hal ini adalah jangkar sistem. Kalau salah satunya bocor, hasil jadi tidak bisa dipercaya.

### 1. Jejak sumber (paling penting — ini pengganti "konsistensi visual/non-visual" milik sistem konten kreator)

**Setiap pernyataan di slide wajib punya jejak ke sumber**: nomor halaman (bahan pengguna) atau URL (riset internet). Tidak ada jejak → pernyataan itu **tidak boleh** masuk slide.

Tiga tingkat yang harus dinyatakan eksplisit di `BRIEF.md`:

| Tingkat | Aturan | Kapan dipakai |
|---|---|---|
| `ketat` | Hanya kata asli dari sumber, agent boleh memotong & menyusun ulang | Pengguna minta verbatim |
| `ringkas` *(default)* | Boleh tulis ulang kalimat demi kejelasan slide, makna wajib tetap, jejak halaman wajib ada | Umum |
| `ringkas+label` | Seperti `ringkas`, plus boleh menambah penjelasan umum **asal diberi label jelas** `[BUKAN DARI SUMBER]` | Presentasi pengajaran/umum |

**Konsisten artinya:** tingkat yang dipilih di `BRIEF.md` berlaku untuk **seluruh** slide deck itu, tidak boleh berubah di tengah jalan tanpa dicatat di Log Keputusan.

### 2. Kontrak Brief wajib terisi sebelum produksi

Produksi (Tahap 4) **terlarang** dimulai kalau `BRIEF.md` masih ada field wajib kosong. Ini aturan fail-closed, bukan anjuran.

### 3. Lantai desain berbasis bukti

Berlaku untuk semua deck kecuali di-override eksplisit **dengan alasan tercatat** di `BRIEF.md`:

| Aturan lantai | Dasar |
|---|---|
| Judul slide = kalimat pernyataan (assertion), bukan frasa topik | Garner & Alley 2013, *IJEE* 29(6):1564-1579, p < .01 |
| Isi slide = bukti visual, bukan dinding bullet | struktur assertion-evidence (Alley, Penn State) |
| Buang materi yang tidak mendukung pesan (coherence) | Mayer |
| Teks slide ≠ transkrip naskah bicara; naskah masuk *speaker notes* (redundancy) | Mayer |
| Satu pesan per slide; materi kompleks dipecah (segmenting) | Mayer |
| Penanda untuk bagian penting (signaling) | Mayer / Kosslyn |
| Jumlah slide mengikuti durasi (~1 slide per 1–2 menit) | konvensi sidang 10–15 menit → 10–15 slide |
| Font minimum terbaca | aturan 10/20/30 |

### 4. Penamaan file dan istilah antar deck

Supaya sesi baru bisa memulihkan deck mana pun tanpa menebak: nama file di dalam `deck-aktif/<nama>/` **baku** (`BRIEF.md`, `PEMAHAMAN_BAHAN.md`, `CHECKLIST_CAKUPAN.md`, `OUTLINE.md`, `RENCANA_VISUAL.md`, `STATUS.md`, `keluaran/`).

### 5. Kepatuhan Paket Ketentuan

Kalau sebuah `PAKET_KETENTUAN` dipasang ke deck, maka cek kepatuhan jadi **bagian wajib** Tahap 5, bukan opsional.

---

## Titik Penguncian/Approval

**Tiga gerbang, adaptif.** "Adaptif" di sini **bukan** berarti agent boleh memutuskan sendiri mau berhenti atau tidak — pemicunya angka terukur.

| Gerbang | Apa yang dikunci | Wajib? | Kategori |
|---|---|---|---|
| **G1 — Peta Pemahaman** | `PEMAHAMAN_BAHAN.md` + `CHECKLIST_CAKUPAN.md`: agent paham bahannya, tidak ada bagian terlewat | **Wajib** kalau bahan > 15 halaman **atau** > 5.000 kata. Di bawah itu boleh digabung ke G2 — dan yang menentukan adalah **hitungan halaman/kata**, bukan perasaan agent | Besar |
| **G2 — Outline + Rencana Visual** | `OUTLINE.md` (judul assertion per slide + jejak sumber) + `RENCANA_VISUAL.md` (gaya terpilih) | **Selalu wajib** | Besar |
| **G3 — Berkas Final** | `keluaran/*.pptx` + hasil verifikasi | **Selalu wajib** sebelum dinyatakan selesai/diserahkan | Besar |

**Kenapa G1 ada di depan:** memperbaiki kesalahan pemahaman itu murah di tahap peta, mahal setelah 30 slide jadi. Ini jawaban langsung atas keluhan pengguna ("selama ini bingung gimana caranya memastikan AI sudah paham keseluruhan").

**Kategori Kecil** (cukup konfirmasi ringan, tidak perlu baca detail): perbaikan salah ketik, penataan ulang folder, penyesuaian warna minor dalam gaya yang sudah dipilih.

**Yang tidak boleh dilewati dalam kondisi apa pun:** G2 dan G3.

---

## Rencana Dokumen

Tanda **[GENERATOR]** = perlu prompt Discovery detail tersendiri (digali lewat diskusi dengan pengguna). Tanda **[TEMPLATE]** = cukup template yang diisi langsung, tidak perlu diskusi panjang. Tanda **[ATURAN]** = dokumen aturan tetap, ditulis sekali, tidak digali per deck.

### Akar folder

| Dokumen | Fungsi | Perlu prompt Discovery? |
|---|---|---|
| `00_RENCANA_KERANGKA.md` | File ini | — (sudah ada) |
| `START_DI_SINI.md` | Entry point sistem: apa yang dibaca dulu, konteks wajib per jenis sesi | **[ATURAN]** |
| `SYSTEM_MANIFEST.md` | Identitas, versi, gate, temuan audit — dari `_meta/SYSTEM_MANIFEST_TEMPLATE.md` | **[TEMPLATE]** |
| `ACCEPTANCE_TESTS.md` | Skenario uji perilaku (dibuat setelah aturan jadi) | **[ATURAN]** |
| `ACCEPTANCE_TEST_LOG.md` | Bukti per run | **[TEMPLATE]** |

### `_sistem/` — aturan tetap lintas deck

| Dokumen | Fungsi | Perlu prompt Discovery? |
|---|---|---|
| `_sistem/01_ALUR_PRESENTASI.md` | 5 tahap + 3 gerbang + aturan fail-closed + apa yang dibaca di tiap tahap | **[ATURAN]** |
| `_sistem/02_ATURAN_SUMBER_DAN_ANTI_NGARANG.md` | Kontrak jejak sumber, 3 tingkat (`ketat`/`ringkas`/`ringkas+label`), larangan mengarang, cara menandai yang tidak bersumber | **[ATURAN]** — tapi **isinya perlu didiskusikan dulu** dengan pengguna sebelum ditulis final |
| `_sistem/03_PRINSIP_DESIGN_BERBASIS_BUKTI.md` | "Lantai" di atas + cara override yang sah | **[ATURAN]** |
| `_sistem/04_PEMAHAMAN_BAHAN_MENDALAM.md` | Mekanisme 5 langkah: kerangka dulu → kartu per bagian → tabel cakupan → spot-check → approval. Termasuk cara baca PDF & batasannya | **[ATURAN]** |
| `_sistem/05_RENDER_DAN_VERIFIKASI.md` | Cara bikin `.pptx` dengan python-pptx, pakai template pengguna, dan 3 jalur verifikasi tampilan | **[ATURAN]** |
| `_sistem/06_PROMPT_LIBRARY.md` | Prompt siap pakai per tahap | **[ATURAN]** |

### `_generator/` — prompt Discovery detail (belum ada, harus ditulis dari nol)

| Dokumen | Fungsi | Status |
|---|---|---|
| `_generator/G1_DISCOVERY_BRIEF.md` | Menggali `BRIEF.md` bersama pengguna: tujuan, audiens, durasi, sumber, tingkat anti-ngarang, gaya, format output, ada ketentuan institusi atau tidak | **[GENERATOR]** — wajib ditulis sebelum deck pertama |
| `_generator/G2_DISCOVERY_VISUAL.md` | Menggali arah visual: kalau pengguna belum punya gambaran, agent riset (boleh internet) lalu **menawarkan 2–3 pilihan**, pengguna memilih | **[GENERATOR]** — wajib ditulis sebelum deck pertama |
| `_generator/G3_DISCOVERY_KETENTUAN.md` | Menggali ketentuan institusi dari dokumen pedoman kampus/perusahaan jadi `PAKET_KETENTUAN` yang bisa dicek | **[GENERATOR]** — boleh menyusul, hanya perlu kalau pengguna punya ketentuan institusi |

### `_template/` — diisi langsung, tanpa diskusi panjang

| Dokumen | Diisi jadi apa |
|---|---|
| `_template/T1_BRIEF.md` | `deck-aktif/<nama>/BRIEF.md` |
| `_template/T2_PEMAHAMAN_BAHAN.md` | kartu per bagian: klaim utama, angka, kutipan kunci + halaman |
| `_template/T3_CHECKLIST_CAKUPAN.md` | tabel cakupan: tiap bab/subbab → `sudah dipetakan` / `dilewati + alasan` / `belum`; plus hitungan tabel & gambar |
| `_template/T4_OUTLINE.md` | per slide: judul assertion, bukti visual yang dipakai, jejak sumber, catatan pembicara |
| `_template/T5_RENCANA_VISUAL.md` | gaya terpilih, palet, font, rencana visual per slide |
| `_template/T6_STATUS.md` | status persisten per deck (pola `PROTOKOL_CHECKPOINT_RECOVERY.md`) |
| `_template/T7_ASET_GAYA.md` | `_aset-gaya/<nama>/` — pakai ulang antar deck |
| `_template/T8_PAKET_KETENTUAN.md` | `_paket-ketentuan/<institusi>/` — pakai ulang antar deck |

### Folder kerja

```
sistem-presentasi/
├── _aset-gaya/<nama>/          ← lapisan B, opsional, pakai ulang
├── _paket-ketentuan/<institusi>/  ← lapisan A, opsional, pakai ulang
└── deck-aktif/<nama-deck>/     ← lapisan C, 1 folder per presentasi
    ├── BRIEF.md                ← hasil Tahap 1 (dikunci di G2)
    ├── PEMAHAMAN_BAHAN.md      ← hasil Tahap 2 (dikunci di G1)
    ├── CHECKLIST_CAKUPAN.md    ← hasil Tahap 2 (dikunci di G1)
    ├── OUTLINE.md              ← hasil Tahap 3 (dikunci di G2)
    ├── RENCANA_VISUAL.md       ← hasil Tahap 3 (dikunci di G2)
    ├── STATUS.md               ← diperbarui tiap tahap, untuk recovery
    ├── bahan/                  ← TEMPAT INPUT (file sumber)
    └── keluaran/               ← TEMPAT OUTPUT (.pptx, preview.html)
```

Ini menjawab permintaan pengguna "ada tempat input, ada tempat output" — keduanya **per deck**, supaya bahan dan hasil satu presentasi tidak tercampur dengan presentasi lain.

---

## Prinsip yang Dipakai / Di-override

Dari `_meta/02_PRINSIP_UNIVERSAL.md`:

| Prinsip | Keputusan | Catatan |
|---|---|---|
| 1. Hierarki | **Dipakai, dengan penyesuaian** | Berlaku 3 lapis (Ketentuan → Gaya → Deck). Penyesuaian: lapisan A dan B **opsional** — deck boleh berdiri tanpa keduanya. Alasan: pengguna menyatakan semua aspek "tergantung keadaan", jadi mewajibkan aset gaya di muka hanya jadi penghalang |
| 2. Rantai/Chaining | **Dipakai apa adanya** | 5 tahap, agent baca hasil tahap sebelumnya dari repo. Titik approval tetap wajib (G1/G2/G3) |
| 3. Approval Bertingkat | **Dipakai, kriteria spesifik domain** | Kategori Besar = G1, G2, G3. Kategori Kecil = salah ketik, penataan folder, warna minor dalam gaya terpilih |
| 4. Checkpoint & Verifikasi Konsistensi | **Dipakai, WAJIB** | Sistem ini dipakai via lmarena Agent Mode → wajib, bukan opsional (fakta platform #2 dan #3). Termasuk checkpoint diskusi ringan >5 giliran |
| 5. Log Keputusan | **Dipakai** | Dokumen hidup yang wajib punya Log Keputusan: `BRIEF.md`, `OUTLINE.md`, `RENCANA_VISUAL.md`, `STATUS.md`, dan tiap `PAKET_KETENTUAN` |
| 6. Quality Assurance & Evolusi | **Dipakai** | Tiga lapisan. Lapisan output = berkas presentasi; indikator kualitasnya = jejak sumber lengkap, tidak ada teks meluber, kepatuhan Paket Ketentuan |

**Yang TIDAK diwarisi dari sistem konten kreator:** pemisahan "Konsistensi Visual vs Non-Visual". `_meta/02_PRINSIP_UNIVERSAL.md` sendiri menyatakan prinsip itu spesifik-domain. Analognya di sistem ini digali sendiri dan hasilnya ada di bagian *Yang Harus Konsisten*: **jejak sumber** (non-visual, paling penting) + **kepatuhan Paket Ketentuan** (visual).

---

## Batasan Teknis yang Sudah Diverifikasi di Lingkungan Ini

Bukan asumsi — semua ini dijalankan dan dicek hasilnya pada 4 Sep 2026 di sesi `arena/01a06d7b-pembangun-sistem`.

| Kemampuan | Status | Bukti |
|---|---|---|
| Bikin `.pptx` asli (judul, bullet berlevel, tabel, gambar) | **BISA** | deck uji 3 slide, 32.684 bytes, dibaca ulang: `slide: 3`, `punya tabel: True`, `punya gambar: True` |
| `python-pptx` | tidak terpasang default, **bisa diinstall** | `pip install --target … python-pptx` exit 0 (Pillow 12.3.0 + lxml 6.1.3 ikut) |
| Baca PDF berbasis teks | **BISA** | `pypdf` terinstall exit 0; PDF uji 2 halaman diekstrak benar per halaman ("BAB I PENDAHULUAN…", "BAB IV HASIL…") |
| Baca PDF hasil **scan** | **TIDAK BISA** | `tesseract` tidak ada, tidak ada alat OCR |
| Output HTML | **BISA** | tanpa dependensi tambahan |
| Render `.pptx` → gambar/PDF | **TIDAK BISA** | `libreoffice`/`soffice`/`pandoc` tidak ada |
| Install LibreOffice | **TIDAK BISA** | `sudo apt-get update` → `Connection failed` ke `deb.debian.org`; `apt-cache search libreoffice` kosong. PyPI **bisa** |

**Konsekuensi desain yang mengikat:**

1. **Berkas PDF scan tidak bisa jadi bahan** kecuali pengguna menyediakan versi teksnya. Aturan ini harus fail-closed: kalau ekstraksi menghasilkan teks kosong/berantakan, agent **berhenti dan melapor**, bukan mengarang isi dari judul halaman.
2. **Agent tidak akan pernah bisa "melihat" hasil render PowerPoint.** Karena itu verifikasi tampilan memakai 3 jalur, dan laporan verifikasi **wajib menyebut jalur mana yang dipakai**:
   - **(a) Struktural lewat kode** — baca ulang `.pptx`, ukur panjang teks vs ukuran placeholder, deteksi kemungkinan meluber, pastikan gambar di dalam bidang.
   - **(b) Preview hampiran HTML** — dibuat paralel dari data slide yang sama, bisa dibuka pengguna di browser. **Jujur: ini hampiran, bukan render PowerPoint** — font dan jarak bisa beda.
   - **(c) Pengguna membuka sendiri berkas `.pptx`-nya** — ini putusan final.
3. **Larangan klaim kosong:** agent tidak boleh menulis "sudah kucek tampilannya" tanpa menyebut (a), (b), atau (c).

---

## Strategi Verifikasi Bertahap — keberatan agent, perlu diputuskan pengguna

Pengguna minta sistem dibangun **lengkap sejak awal**, dengan alasan: *"ini bukan seperti aplikasi yang susah buatnya, semua dieksekusi oleh agent AI."*

**Agent setuju untuk LINGKUP DESAIN.** Semua kemampuan dirancang sekarang juga di dokumen ini — bahan pengguna, riset internet untuk isi maupun visual, output `.pptx` dan HTML, Paket Ketentuan. Tidak ada alasan menunda perancangannya.

**Agent keberatan kalau "lengkap" berarti "divalidasi sekaligus di akhir."** Empat alasan:

1. **Aturan repo ini sendiri.** `_meta/00_CARA_KERJA_META.md`: *"1 dokumen direvisi/dibangun penuh dulu, baru lanjut ke dokumen berikutnya — bukan banyak sekaligus, supaya kesalahan kecil tidak menyebar sebelum ketahuan."*
2. **Preseden di repo ini.** Sistem Konten Kreator butuh 2 putaran audit menyeluruh + 8 acceptance test, dan setelah semua itu statusnya masih `belum divalidasi pemakaian nyata`.
3. **Alasan teknis paling penting:** fitur **"riset internet untuk ISI" berkonflik langsung dengan syarat "tidak boleh ngarang"**. Kalau keduanya dibangun dan diuji sekaligus, kegagalan tidak bisa dilokalisasi — kita tidak tahu aturan mana yang bocor. Fitur itu butuh acceptance test-nya sendiri.
4. **"Semua dieksekusi agent AI" justru menaikkan risiko, bukan menurunkan.** Yang dibangun di sini bukan kode yang bisa dites otomatis, tapi **aturan yang harus diikuti agent**. Kalau aturannya ambigu, agent akan mengarang dengan percaya diri. Preseden: AT-KK-05b di sistem konten kreator menguji persis itu (`STATUS.md` mengklaim berkas ADA padahal tidak ada), dan agent dinyatakan LULUS **hanya karena berhenti dan melapor**, bukan karena pintar menebak.

**Jalan tengah yang diusulkan:** desain lengkap sekarang; **pembangunan dan verifikasi dokumen per dokumen**, dengan urutan dari yang paling berisiko:

| Urutan | Yang diverifikasi | Kenapa di urutan ini |
|---|---|---|
| 1 | Anti-ngarang / jejak sumber | Paling fundamental; semua fitur lain bergantung padanya |
| 2 | Mekanisme kelengkapan bahan panjang | Menjawab keluhan utama pengguna |
| 3 | Gerbang G1/G2/G3 + recovery lewat `STATUS.md` | Syarat fisik karena sesi bisa crash |
| 4 | Render `.pptx` + deteksi teks meluber | Risiko teknis yang sudah terbukti ada |
| 5 | Riset internet untuk **isi** | Baru aman diuji setelah #1 kuat |
| 6 | Riset visual + penawaran pilihan | Bergantung #5 untuk aturan sumber URL |
| 7 | Paket Ketentuan + cek kepatuhan | Bergantung #4 |
| 8 | Output HTML | Paling rendah risikonya |

---

## Hal yang Masih Terbuka (perlu keputusan pengguna)

| # | Hal | Usulan agent |
|---|---|---|
| 1 | Ambang "bahan pendek vs panjang" untuk G1 | **> 15 halaman ATAU > 5.000 kata** → G1 wajib. Angka boleh diubah |
| 2 | Format output selain `.pptx` | `.pptx` (default) + `.html` (sekalian jadi jalur preview). **PDF tidak dijanjikan** — tidak ada renderer di lingkungan ini |
| 3 | Berkas bahan besar (misal PDF skripsi 100 halaman) masuk repo atau tidak | Masuk ke `deck-aktif/<nama>/bahan/`, tapi perlu aturan batas ukuran + catatan di `.gitignore` kalau terlalu besar |
| 4 | Riset internet untuk **isi** ikut versi pertama? | **Ya** (sesuai permintaan pengguna "langsung lengkap"), tapi diverifikasi di urutan 5 — setelah aturan anti-ngarang terbukti kuat |
| 5 | Nama deck: ditentukan pengguna atau diusulkan agent | Diusulkan agent di Tahap 1, dikonfirmasi pengguna di G2 |
| 6 | Celah protokol meta Q-O2 & Q-O3 (lihat `_meta/_internal/arsip-pilot-002-2026-09-03/README.md`) | Ditangani sebagai **pekerjaan meta-sistem terpisah**, bukan di sistem ini. Tapi harus dicatat karena `STATUS.md` sistem ini akan memakainya |

---

## Langkah Berikutnya Setelah Rencana Ini Disetujui

Sesuai `_meta/01_DISCOVERY_LEVEL_0.md` bagian "Setelah selesai":

1. Salin `_meta/SYSTEM_MANIFEST_TEMPLATE.md` → `sistem-presentasi/SYSTEM_MANIFEST.md`, isi identitas awal.
2. Tulis `START_DI_SINI.md` dan keenam dokumen `_sistem/` — **satu selesai penuh dulu baru lanjut ke berikutnya**.
3. Tulis ketiga prompt **[GENERATOR]** di `_generator/` (G1 dan G2 wajib sebelum deck pertama).
4. Buat kedelapan **[TEMPLATE]** di `_template/`.
5. Baru jalankan Discovery detail per dokumen untuk mengisi konten nyata.
6. Tulis `ACCEPTANCE_TESTS.md` mengikuti 8 urutan verifikasi di atas.
7. Update `_meta/INDEKS_SISTEM.md` (tambah baris Sistem Presentasi, status `Kerangka dibuat, isi belum`).
8. Buat `_cadangan-claude/RINGKASAN_sistem-presentasi.md` setelah struktur stabil.
