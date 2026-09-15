# Rencana Kerangka — Sistem Presentasi

> **Status:** DISETUJUI pengguna 4 September 2026, **sengaja BELUM di-merge** atas permintaan pengguna — kerja dilanjutkan di sesi yang sama di branch `arena/01a06d7b-pembangun-sistem`. Alasan: setelah PR di-merge, platform mencabut akses push sesi ini (`_meta/PLATFORM_LMARENA.md` fakta #2), jadi merge sekarang akan mengunci sesi dan memaksa mulai dari nol. Merge dilakukan nanti lewat sesi tersendiri.
> **Revisi:** 4 Sep 2026 — tambah **Mode Gambar** (M0–M4 + gerbang lisensi) dan **Perancangan Berbasis Rekomendasi**, keduanya atas permintaan pengguna.
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

### 6. Asal-usul dan lisensi setiap gambar (ditambahkan 4 Sep 2026 atas permintaan pengguna)

Setiap gambar yang masuk slide **wajib** punya baris di `DAFTAR_GAMBAR.md`: dari mana asalnya (mode mana), siapa pemegang haknya, lisensinya apa, dan atribusi yang harus dicantumkan. Gambar tanpa baris lengkap **tidak boleh** masuk berkas final. Alasan: ini satu-satunya cara klaim "tidak melanggar hak cipta" bisa diperiksa, bukan cuma diyakini.

---

## Mode Gambar

Ditambahkan 4 Sep 2026 atas permintaan pengguna. **Mode dipilih per deck di `BRIEF.md`, tapi tiap slide boleh override dengan alasan tercatat** — karena dalam satu deck, slide hasil penelitian butuh grafik data nyata sementara slide konsep boleh pakai ilustrasi.

| Mode | Isi | Risiko hak cipta | Kapan paling tepat |
|---|---|---|---|
| **M0 — Tanpa gambar** | Teks + struktur saja | Tidak ada | Deck padat argumen, atau waktu mepet. **Bukan mode gagal** — Mayer justru mendukung slide tanpa hiasan |
| **M1 — Bahan visual milik pengguna** | Gambar yang tertanam di dokumen pengguna (misal figur di skripsi) **plus** file gambar yang dia berikan sendiri | **Paling aman** — karya pengguna sendiri | Default untuk sidang skripsi: figur aslinya justru yang paling relevan |
| **M2 — Diagram/grafik dari data nyata** | Grafik, bagan, diagram alir yang **digenerate kode** dari angka yang ada di sumber | Tidak ada (buatan sendiri) | Setiap slide yang memuat angka. **Angkanya wajib dari sumber, tidak boleh dikarang** |
| **M3 — Gambar AI** | Ilustrasi konseptual hasil generate | Tidak ada isu lisensi, **tapi ada isu kejujuran** | Hanya untuk ilustrasi konsep. **Dilarang** untuk menggambarkan data, hasil penelitian, foto dokumentasi, atau apa pun yang bisa disangka bukti. **Wajib diberi label "ilustrasi AI"** di slide |
| **M4 — Gambar asli dari internet** | Foto/ilustrasi nyata yang diambil dari internet | **Paling berisiko — wajib gerbang** | Hanya kalau M1–M3 tidak bisa memenuhi, dan lewat gerbang lisensi di bawah |

### Aturan keras penempatan gambar (ditambahkan 4 Sep 2026 atas permintaan pengguna)

Dua batasan ini **mengikat semua mode gambar**, bukan cuma M3. Alasannya sama: slide harus tetap bisa diedit, dan gambar tidak boleh mengambil alih ruang yang seharusnya berisi teks.

#### Aturan G-1: Teks slide TIDAK BOLEH jadi bagian gambar

Semua teks yang mungkin perlu diubah — judul assertion, isi, angka, label, nama, keterangan — **wajib** berada di *text frame* PowerPoint yang nyata, bukan tergoreng di dalam gambar.

- **Kenapa:** kalau teks tergoreng jadi gambar, slide jadi kaku. Ganti satu kata berarti generate ulang seluruh gambar, dan hasilnya tidak dijamin sama. Ini persis yang dikeluhkan pengguna.
- **Cara menjalankan:** setiap prompt generate gambar **wajib** memuat larangan eksplisit: *no text, no letters, no words, no numbers, no watermark*. Gambar hanya boleh berisi bentuk, ilustrasi, atau foto.
- **Cara memverifikasi "bebas teks" (dikoreksi 4 Sep 2026):** dulu kubilang tidak bisa karena tidak ada `tesseract` — **itu salah**. Yang benar: model multimodal **bisa membaca teks di dalam gambar dengan visinya** (terbukti: kubaca gambar uji berisi kode `XK-4471-QZ`, semua baris terbaca). Jadi pengecekannya tiga lapis: (a) prompt yang melarang teks, (b) **agent melihat sendiri gambar hasilnya** dan melapor kalau ada teks yang muncul, (c) **pengguna melihat preview di G2** sebagai putusan akhir.
- **Batas yang tetap harus dicatat:** pembacaan via visi dilakukan oleh **model yang sedang berjalan**. Karena lmarena Agent memakai model yang berbeda-beda per sesi (sesuai pengamatan pengguna), aturan yang aman adalah: setiap sesi yang memverifikasi gambar **wajib benar-benar melihatnya kembali**, tidak boleh mewarisi klaim "sudah dicek bebas teks" dari sesi sebelumnya tanpa melihat ulang. Ini bentuk konkret dari prinsip "jangan mewarisi klaim yang tidak kamu verifikasi sendiri".
- **Pengecualian yang sah:** gambar yang memang berasal dari bahan pengguna (M1) boleh mengandung teks, karena itu dokumen aslinya — misalnya tangkapan tabel atau figur asli skripsi. Itu bukan hasil generate, jadi tidak kaku dengan cara yang sama.

#### Aturan G-2: Gambar ditempatkan di AREA tertentu, bukan otomatis memenuhi slide

Default-nya **bukan** gambar satu slide penuh. Setiap gambar wajib punya geometri eksplisit: area mana, ukuran berapa, dan teks tetap punya ruang sendiri.

| Hal | Aturan |
|---|---|
| Penempatan | Ditentukan per slide di `RENCANA_VISUAL.md`: area (kiri/kanan/atas/bawah/pojok), lebar, tinggi |
| Slide penuh | **Boleh, tapi harus diminta eksplisit** — untuk slide pembuka, penutup, atau kutipan. Bukan default |
| Rasio gambar | **Wajib menyesuaikan rasio area tujuannya**, supaya tidak gepeng atau terpotong. Kalau rasio tidak cocok, yang disesuaikan adalah ukuran areanya, bukan gambarnya dipaksa |
| Ruang teks | Setiap slide yang ada gambarnya **tetap harus punya ruang teks yang cukup** untuk judul assertion. Gambar tidak boleh mendesak judul sampai terpotong |
| Verifikasi | Pemeriksaan struktural (jalur a di bagian verifikasi) **wajib** mengecek: gambar berada di dalam bidang slide, tidak menimpa *text frame*, dan teks tidak terdorong keluar |

**Kenapa ini penting secara desain:** python-pptx menempatkan gambar lewat koordinat eksplisit (`add_picture(path, left, top, width, height)`), jadi penempatan presisi itu memang bisa dilakukan — tapi hanya kalau rencananya sudah menentukan geometrinya lebih dulu. Tanpa `RENCANA_VISUAL.md` yang memuat geometri per slide, agent akan cenderung menaruh gambar besar di tengah dan hasilnya monoton.

### Gerbang lisensi untuk M4 (ini temuan penting, bukan basa-basi)

Yang sudah diverifikasi di lingkungan ini pada 4 Sep 2026:

- Alat pencari gambar **berfungsi** dan menyimpan berkasnya ke workspace, tapi **tidak mengembalikan metadata lisensi sama sekali** — hanya `title`, `source_url`, `thumbnail_url`.
- **Tiga hasil teratas dari pencarian uji justru dari Getty Images dan Veranda (Hearst)** — keduanya agensi stok berhak cipta, bukan bebas pakai.
- **Unduhan langsung lewat `curl` ke URL gambar diblokir** (`SSL_ERROR_SYSCALL` ke `upload.wikimedia.org:443`), jadi tidak ada jalan memverifikasi berkas lewat jalur itu.
- **Tapi halaman deskripsi berkas bisa dibaca** dan blok lisensinya terbaca. Uji nyata: `File:Cat03.jpg` di Wikimedia Commons → **CC BY-NC 3.0 + GFDL 1.2**, penulis "Fir0002/Flagstaffotos", dan **bukan domain publik**. Catatan penting: `NC` = NonCommercial, jadi gambar itu **tidak boleh** dipakai untuk keperluan komersial — persis jenis jebakan yang harus ditangkap sistem.

Karena itu aturan M4:

1. **Daftar putih sumber** yang lisensinya bisa dibaca mesin: Wikimedia Commons, Openverse, dan sumber sejenis. Di luar itu → **tidak boleh otomatis**.
2. **Wajib baca blok lisensinya**, bukan menebak dari nama situs. Hasilnya dicatat: lisensi, pemegang hak, atribusi wajib, dan **flag khusus** untuk `NC` (non-komersial) serta `SA`/copyleft (turunan harus berlisensi sama).
3. **Kalau lisensi tidak terbaca → statusnya `TIDAK DIKETAHUI`, dan gambar TIDAK BOLEH dipakai.** Agent berhenti dan menawarkan mode lain. Tidak boleh "kemungkinan besar aman".
4. **Pengguna wajib menyetujui tiap gambar M4 satu per satu** di G2, lengkap dengan lisensi dan atribusinya. Bukan persetujuan borongan.
5. Atribusi dicantumkan di slide (catatan kaki kecil) **dan** di `DAFTAR_GAMBAR.md`.

### Mode tambahan yang diusulkan agent (boleh ditolak)

- **M2 diperluas jadi "diagram penjelasan"**, bukan cuma grafik angka: diagram alir metode penelitian, kerangka konsep, timeline. Dibuat kode, jadi tetap tanpa risiko lisensi dan tetap setia pada sumber.
- **Aturan anti-gambar-dekoratif:** Mayer (coherence) menyatakan gambar yang tidak mendukung pesan justru menambah beban kognitif. Jadi "slide ini butuh gambar" harus dijawab "gambar apa yang mendukung judul assertion slide ini", bukan "biar tidak kosong".

---

## Perancangan Berbasis Rekomendasi (berlaku di SEMUA titik perancangan)

Ditambahkan 4 Sep 2026 atas permintaan pengguna. Ini **prinsip, bukan fitur** — mengikat seluruh tahap perancangan: isi slide, alur dan urutan, jumlah slide, pilihan judul assertion, arah visual, mode gambar, format output, tingkat anti-ngarang, sampai struktur deck.

### Aturan inti: Agent Mengusulkan, Pengguna Memutuskan

**Dilarang** mengajukan pertanyaan perancangan kosong seperti *"mau seperti apa?"*. Itu memindahkan beban desain ke pengguna, padahal agent-lah yang memegang konteks bahan dan aturan. Setiap pertanyaan perancangan **wajib** datang sebagai paket lima bagian:

| # | Bagian | Isi |
|---|---|---|
| 1 | **Rekomendasi** | 1 pilihan yang agent sarankan, **plus dasarnya apa** |
| 2 | **Alternatif** | 2–3 pilihan lain, masing-masing dengan trade-off — bukan daftar kosong |
| 3 | **Konsekuensi** | Apa yang terjadi kalau pilihan itu diambil (misal: "M0 untuk deck 12 slide ini membuat slide 7–9 padat teks") |
| 4 | **Default kalau dijawab "terserah"** | Agent **wajib** sudah punya default yang dinyatakan di muka — dilarang bertanya ulang |
| 5 | **Tercatat** | Pilihan + alasan + siapa yang memutuskan masuk `BRIEF.md` dan Log Keputusan |

### Dasar rekomendasi harus jujur

Setiap rekomendasi **wajib menyebut dasarnya**, dan hanya boleh salah satu dari tiga:

- **Berbasis bukti** — merujuk aturan "lantai" di `_sistem/03_PRINSIP_DESIGN_BERBASIS_BUKTI.md` (misal: "judul assertion, karena Garner & Alley 2013").
- **Berbasis bahan pengguna** — merujuk halaman/URL tertentu dari bahannya.
- **Penilaian agent** — dan **wajib dilabeli** `[PENILAIAN AGENT]`.

**Larangan:** menyajikan selera sebagai fakta. Kalau tidak ada dasar buktinya, agent harus bilang *"ini soal selera, tidak ada bukti yang mendukung satu pilihan"* — bukan mengarang pembenaran. Ini sejalan dengan aturan anti-ngarang yang sudah jadi inti sistem.

### Kenapa ini penting secara struktural, bukan sekadar sopan santun

Sistem ini dibangun karena pengguna menyatakan **"semuanya tergantung keadaan"**. Kalau agent hanya bertanya, maka "tergantung" akan berakhir jadi kekosongan, dan kekosongan diisi agent dengan tebakan yang tidak tercatat. Dengan mewajibkan paket rekomendasi, setiap "tergantung" **dipaksa jadi keputusan yang tercatat beserta alasannya** — sehingga bisa diaudit, bisa dibalik, dan bisa dilanjutkan sesi lain.


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

> **Catatan renumbering (5 Sep 2026, audit independen):** tabel di bawah adalah **rencana per 4 Sep 2026**. Implementasi final **menomori ulang** dokumen `_sistem/` (8 → 10 dokumen): final `01`=Aturan Desain/Isi/Gambar, `02`=Knowledge Desain, `03`=Kebutuhan & Tujuan, `04`=QA Produksi, `05`=Sumber & Anti-Ngarang, `06`=Lantai Berbasis Bukti, `07`=Mode Gambar & Lisensi, `08`=Perancangan Berbasis Rekomendasi, `09`=Pemahaman Bahan, `10`=Render & Verifikasi. Rujukan bernomor di dokumen aktif memakai penomoran **final**; nama lama di tabel ini adalah sejarah, bukan path yang harus ada.

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
| `_sistem/07_MODE_GAMBAR_DAN_LISENSI.md` | Kelima mode gambar, cara ekstraksi dari PDF, cara bikin grafik dari data, gerbang lisensi M4, daftar putih sumber, aturan label "ilustrasi AI" | **[ATURAN]** — **baru, dari permintaan pengguna 4 Sep 2026** |
| `_sistem/08_PERANCANGAN_BERBASIS_REKOMENDASI.md` | Aturan paket 5 bagian untuk SEMUA pertanyaan perancangan + 3 dasar rekomendasi yang sah + larangan menyajikan selera sebagai fakta | **[ATURAN]** — **baru, dari permintaan pengguna 4 Sep 2026** |

**Catatan mengikat untuk semua dokumen `[GENERATOR]`:** setiap prompt Discovery **wajib** mematuhi `_sistem/08_PERANCANGAN_BERBASIS_REKOMENDASI.md`. Prompt yang isinya hanya daftar pertanyaan tanpa rekomendasi **tidak boleh dipakai** — itu persis pola yang dilarang pengguna.

### `_generator/` — prompt Discovery detail (belum ada, harus ditulis dari nol)

| Dokumen | Fungsi | Status |
|---|---|---|
| `_generator/G1_DISCOVERY_BRIEF.md` | Menggali `BRIEF.md` bersama pengguna: tujuan, audiens, durasi, sumber, tingkat anti-ngarang, gaya, format output, ada ketentuan institusi atau tidak | **[GENERATOR]** — wajib ditulis sebelum deck pertama |
| `_generator/G2_DISCOVERY_VISUAL.md` | Menggali arah visual: kalau pengguna belum punya gambaran, agent riset (boleh internet) lalu **menawarkan 2–3 pilihan lengkap dengan rekomendasi + alasan**, pengguna memilih. **Termasuk memilih mode gambar per deck dan per slide** | **[GENERATOR]** — wajib ditulis sebelum deck pertama |
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
| `_template/T9_DAFTAR_GAMBAR.md` | `deck-aktif/<nama>/DAFTAR_GAMBAR.md` — per gambar: dipakai di slide mana, mode (M0–M4), sumber, pemegang hak, lisensi, atribusi wajib, flag NC/copyleft, status persetujuan |

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
    ├── DAFTAR_GAMBAR.md        ← provenance + lisensi tiap gambar (dikunci di G2)
    ├── STATUS.md               ← diperbarui tiap tahap, untuk recovery
    ├── bahan/                  ← TEMPAT INPUT (file sumber)
    ├── gambar/                 ← aset gambar: ekstraksi PDF, grafik buatan, AI, internet
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
| **Baca `.docx` (Word)** | **BISA, dua jalur** | (1) `python-docx` terinstall exit 0 → dokumen uji terbaca: 4 paragraf **beserta nama stylenya** (`Heading 1`, `Heading 2`, `Normal`) + 1 tabel lengkap isinya. (2) Tanpa library apa pun: `.docx` itu zip, `zipfile` bawaan Python membaca `word/document.xml` (2.817 karakter, memuat "Latar Belakang"). Nama style penting karena memberi struktur dokumen tanpa perlu menebak |
| **Baca PDF berbahasa Arab (RTL)** | **BISA, tapi jalur visi wajib untuk kutipan** | Diuji pada tesis asli 161 halaman. Ekstraksi teks (`PyMuPDF`/`pypdf`) berjalan **tapi urutan kata dalam baris teracak + glyph presentasional** → hanya untuk peta halaman/struktur, **bukan** kutipan. Jalur visi (render→baca) terbukti benar dan proper → itu jalur baca utama untuk Arab. Implikasi: untuk bahan Arab, `PEMAHAMAN_BAHAN.md` diisi lewat visi; angka halaman pemilik tesis (ص٢٠, ص٢٣, dst) terbukti cocok dengan posisi halaman PDF |
| Baca PDF hasil **scan** | **BISA, lewat jalur render + visi** | Lihat baris "Render PDF → gambar" dan "OCR via visi" di bawah. PDF scan dulu kubilang "tidak bisa" — **itu koreksi 4 Sep 2026**: ternyata `PyMuPDF` bisa merender halaman PDF jadi gambar **tanpa poppler**, lalu model membacanya dengan visi |
| **Ekstraksi gambar dari PDF pengguna** | **BISA** | PDF uji berisi 1 figur → `page.images` mendeteksi 1 gambar, `I1.png`, 12.654 bytes |
| **Render PDF → gambar** | **BISA (PyMuPDF, tanpa poppler)** | `pymupdf` terinstall exit 0; halaman PDF uji dirender ke PNG 1240×1755, 19.754 bytes, teks via `get_text()` benar |
| **OCR — membaca teks di dalam gambar** | **BISA, lewat visi model (bukan tesseract)** | Gambar uji berisi 4 baris teks kumasukkan, lalu kubaca lewat `read_file` — semua baris terbaca sempurna termasuk kode `XK-4471-QZ`. **Koreksi atas klaim "OCR tidak bisa"**: yang tidak ada hanyalah `tesseract` (biner OCR terpisah); model multimodal **itulah** OCR-nya |
| **Generate gambar AI** | **BISA** | gambar uji 29.777 bytes, header `ffd8ff` (JPEG valid) |
| **Bikin grafik/diagram dari data** | **BISA** | matplotlib terinstall exit 0; grafik uji 26.405 bytes PNG |
| **Cari gambar di internet** | **BISA, tapi tanpa metadata lisensi** | 3 hasil tersimpan ke workspace (JPEG valid, 63.411 bytes); field yang dikembalikan hanya `title`, `source_url`, `thumbnail_url` — **tidak ada lisensi**. 3 hasil teratas uji = Getty Images & Veranda (stok berhak cipta) |
| **Baca blok lisensi sebuah berkas** | **BISA** | `fetch_page` ke halaman Wikimedia Commons berhasil; `File:Cat03.jpg` → CC BY-NC 3.0 + GFDL 1.2, "not in the Public Domain", penulis tercatat |
| **Unduh gambar langsung via `curl`** | **TIDAK BISA** | `SSL_ERROR_SYSCALL` ke `upload.wikimedia.org:443`, HTTP 000, 0 bytes |
| Output HTML | **BISA** | tanpa dependensi tambahan |
| Render `.pptx` → gambar/PDF | **TIDAK BISA** | `libreoffice`/`soffice`/`pandoc` tidak ada |
| Install LibreOffice | **TIDAK BISA** | `sudo apt-get update` → `Connection failed` ke `deb.debian.org`; `apt-cache search libreoffice` kosong. PyPI **bisa** |
| `/tmp` persisten antar langkah | **TIDAK** | `/tmp/pdftest` dan artefak uji hilang antar panggilan sementara `/tmp/plottest` sempat ada. **Konsekuensi:** semua hasil kerja wajib masuk folder deck di repo, bukan `/tmp` |

**Konsekuensi desain yang mengikat:**

1. **Berkas PDF scan tidak bisa jadi bahan** kecuali pengguna menyediakan versi teksnya. Aturan ini harus fail-closed: kalau ekstraksi menghasilkan teks kosong/berantakan, agent **berhenti dan melapor**, bukan mengarang isi dari judul halaman.
2. **Agent tidak akan pernah bisa "melihat" hasil render PowerPoint.** Karena itu verifikasi tampilan memakai 3 jalur, dan laporan verifikasi **wajib menyebut jalur mana yang dipakai**:
   - **(a) Struktural lewat kode** — baca ulang `.pptx`, ukur panjang teks vs ukuran placeholder, deteksi kemungkinan meluber, pastikan gambar di dalam bidang.
   - **(b) Preview hampiran HTML** — dibuat paralel dari data slide yang sama, bisa dibuka pengguna di browser. **Jujur: ini hampiran, bukan render PowerPoint** — font dan jarak bisa beda.
   - **(c) Pengguna membuka sendiri berkas `.pptx`-nya** — ini putusan final.
3. **Larangan klaim kosong:** agent tidak boleh menulis "sudah kucek tampilannya" tanpa menyebut (a), (b), atau (c).
4. **Mode M4 tidak bisa dijamin aman secara otomatis.** Karena alat pencari gambar tidak mengembalikan lisensi dan hasil teratasnya justru agensi stok berhak cipta, klaim "tidak melanggar hak cipta" **hanya** boleh dibuat setelah blok lisensinya dibaca dan dicatat. Gerbang lisensi di bagian Mode Gambar bukan pelengkap — itu satu-satunya dasar klaim tersebut.
5. **Semua artefak wajib masuk repo, bukan `/tmp`.** `/tmp` terbukti tidak persisten antar langkah, jadi gambar, grafik, dan berkas antara yang ditaruh di sana bisa hilang sebelum sempat dipakai.
6. **Alat pencari gambar menulis ke root repo secara default** (terbukti: berkas uji mendarat di `image-search/` di root). Aturan wajib: hasil pencarian **langsung dipindahkan** ke `deck-aktif/<nama>/gambar/` dan folder sementaranya dibersihkan, supaya tidak ikut ter-commit diam-diam.

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
| 4 | **Perancangan berbasis rekomendasi** (paket 5 bagian, dasar rekomendasi jujur) | Mengikat semua tahap sesudahnya; kalau ini bocor, semua keputusan jadi tebakan tak tercatat |
| 5 | Render `.pptx` + deteksi teks meluber | Risiko teknis yang sudah terbukti ada |
| 6 | **Mode M1 + M2** (ekstraksi gambar dari bahan + grafik dari data nyata) | Paling aman dan paling relevan; M2 juga menguji apakah angka di grafik benar-benar dari sumber |
| 7 | Riset internet untuk **isi** | Baru aman diuji setelah #1 kuat |
| 8 | **Mode M3** (gambar AI) — termasuk apakah label "ilustrasi AI" benar-benar terpasang dan tidak dipakai menggambarkan data | Bergantung #1: risiko utamanya adalah gambar AI disangka bukti |
| 9 | **Mode M4** (gambar internet) + gerbang lisensi | Paling berisiko hukum; diuji terakhir, setelah aturan provenance terbukti jalan di #6–#8 |
| 10 | Riset visual + penawaran pilihan | Bergantung #7 untuk aturan sumber URL dan #9 untuk lisensi |
| 11 | Paket Ketentuan + cek kepatuhan | Bergantung #5 |
| 12 | Output HTML | Paling rendah risikonya |

---

## Keputusan atas Butir Terbuka

Pengguna menyerahkan keputusan ini ke agent pada 4 Sep 2026, dengan syarat: *"asalkan itu betul-betul hasil pemikiran mendalam dan bahkan hasil riset jika diperlukan."* Karena itu tiap keputusan di bawah disertai alasannya, bukan cuma hasilnya. Semua tercatat sebagai keputusan dan **boleh diubah nanti lewat Log Keputusan** — tapi agent tidak boleh mengubahnya diam-diam.

| # | Butir | Keputusan | Alasan |
|---|---|---|---|
| 1 | Ambang "bahan pendek vs panjang" untuk G1 | G1 **wajib** kalau bahan **> 15 halaman ATAU > 5.000 kata ATAU punya ≥ 8 bagian berstruktur** (bab/subbab). Pengguna boleh **menaikkan** ambang ini; agent **tidak boleh menurunkannya** sendiri | Ketiga pemicu itu terukur, jadi tidak bisa ditawar lewat perasaan. Pemicu ketiga (≥ 8 bagian) kutambahkan karena panjang bukan satu-satunya sumber risiko: bahan 10 halaman dengan 12 subbab tetap gampang ada yang terlewat, dan justru struktur bertingkat itu yang bikin "lengkap" bisa dihitung. Selaras prinsip *segmenting* Mayer |
| 2 | Format output | `.pptx` = default. `.html` = **selalu dibuat**, rangkap sebagai jalur preview verifikasi. **PDF tidak dijanjikan** | `.html` bukan fitur tambahan yang mahal — dia sudah dibutuhkan untuk verifikasi (jalur b), jadi membuatnya selalu ada hampir gratis. PDF tidak dijanjikan karena **terbukti tidak ada renderer** di lingkungan ini; menjanjikan yang tidak bisa dipenuhi lebih buruk daripada tidak menjanjikan |
| 3 | Berkas bahan besar masuk repo? | **Ya**, di `deck-aktif/<nama>/bahan/`, dengan batas **≤ 25 MB per berkas**. Lebih besar → tidak di-commit; yang dicatat hash + nama berkasnya, dan **hasil ekstraksinya** (`PEMAHAMAN_BAHAN.md`) tetap di-commit | Bahan harus ikut repo supaya sesi baru bisa memulihkan kerja (fakta platform #3). Batas 25 MB karena platform membatasi artefak patchset (~128 MB / 10.000 berkas), dan PDF skripsi umumnya 1–10 MB. Yang penting bukan berkas aslinya, tapi **pemahaman yang sudah diekstrak** — itu yang wajib selamat |
| 4 | Riset internet untuk isi ikut versi pertama? | **Ya**, tapi diverifikasi di urutan #7 — setelah aturan anti-ngarang terbukti kuat | Sesuai permintaan pengguna ("langsung lengkap"). Penundaan **verifikasi**, bukan penundaan **desain** — dua hal itu sengaja dibedakan |
| 5 | Nama deck siapa yang menentukan | Agent mengusulkan di **awal Tahap 1** dengan paket rekomendasi, pengguna memilih **saat itu juga** (kategori Kecil) | **Koreksi atas usulan awalku.** Tadinya kutulis "dikonfirmasi di G2" — itu salah, karena folder `deck-aktif/<nama>/` harus dibuat di awal Tahap 1, sebelum G2 ada. Menunggu G2 berarti agent menebak nama folder dulu lalu mengganti namanya, dan itu merusak rujukan |
| 7 | Mode gambar default untuk kasus sidang skripsi | **M1 + M2** (figur asli skripsi + grafik dari datanya). M3 hanya untuk slide konsep, M4 hanya kalau M1–M3 tidak sanggup | Keduanya **terbukti bisa** di lingkungan ini, **nol risiko hak cipta** (karya pengguna sendiri / buatan kode), dan paling relevan: figur asli skripsi justru yang dikenali penguji. Gambar AI kalah untuk kasus ini karena tidak boleh menggambarkan data |
| 8 | Daftar putih sumber untuk M4 | **Bukan daftar situs, tapi kriteria:** sumber yang **blok lisensinya bisa dibaca dan diverifikasi**. Wikimedia Commons sudah **terbukti** bisa. Sumber lain boleh asal lolos kriteria yang sama | **Koreksi atas usulan awalku.** Tadinya kutulis "Wikimedia Commons + Openverse" — tapi Openverse **belum kuuji** di lingkungan ini, jadi mencantumkannya berarti mengklaim yang belum terbukti. Kriteria lebih kuat daripada daftar: dia tidak perlu diperbarui tiap ada situs baru, dan tidak memberi kesan aman pada sumber yang belum diverifikasi |
| 9 | Gambar internet ikut ter-commit? | **Ya**, di `deck-aktif/<nama>/gambar/`, wajib ada barisnya di `DAFTAR_GAMBAR.md`, batas **≤ 5 MB per gambar** | Gambar harus ikut repo supaya berkas `.pptx` bisa dibangun ulang oleh sesi lain. Batas 5 MB karena gambar slide tidak butuh resolusi cetak — dan kalau perlu lebih besar, itu tanda gambarnya salah mode |
| 10 | Label "ilustrasi AI" terlihat di slide? | **Ya, terlihat di slide** (kecil, di pojok), bukan cuma di catatan | Yang berisiko tertipu gambar AI adalah **audiens**, bukan pengguna. Menyembunyikan labelnya di `DAFTAR_GAMBAR.md` melindungi nobody. Biaya label kecil; biaya audiens salah menyangka ilustrasi sebagai bukti penelitian jauh lebih besar — apalagi di sidang skripsi |
| 11 | M4 untuk keperluan komersial? | **Tidak secara default.** Dikunci kecuali lisensinya eksplisit mengizinkan, dan itu harus tercatat | Uji nyata menemukan lisensi **`NC` (NonCommercial)** pada berkas yang tampak bebas pakai (`File:Cat03.jpg` → CC BY-NC 3.0). Default aman + catatan eksplisit lebih baik daripada mengandalkan agent mengenali singkatan lisensi setiap kali |

### Satu butir yang TIDAK boleh kuputuskan sendiri

**Butir 6 — celah protokol meta Q-O2 dan Q-O3.** Ini menyentuh aturan inti `_meta/`, dan aturan repo ini sendiri melarang mengubah aturan inti tanpa proposal + approval + regression check + rollback plan (pola AT-05). Jadi kuperlakukan sebagai **proposal**, bukan keputusan.

**Usulan Q-O2** (kriteria "alasan" yang sah untuk mengulang tahap `approved`/`merged`) — alasan dianggap sah **hanya** kalau salah satu dari ini, dan wajib dicatat di Log Keputusan:
1. Output fisiknya **terbukti tidak ada atau rusak** (bukan "kayaknya kurang bagus").
2. Ada **keputusan pengguna baru** yang membatalkan dasar keputusan sebelumnya.
3. Ditemukan **konflik dengan sumber terkunci** yang tidak terlihat saat approval diberikan.
4. Aturan yang jadi dasar approval **sudah berubah** setelah approval itu.

**Usulan Q-O3** (field "Waktu pembaruan") — diisi **setiap kali satu tahap selesai**, format `YYYY-MM-DD — <nama tahap>`, memakai tanggal UTC sesi.

**Kenapa ini perlu diputuskan sebelum dokumen sistem ditulis:** `_sistem/01_ALUR_PRESENTASI.md` dan `_template/T6_STATUS.md` akan merujuk protokol recovery meta. Kalau Q-O2/Q-O3 masih kosong, sistem ini terpaksa mengarang aturannya sendiri — dan itu persis drift yang meta-sistem ini ada untuk mencegahnya.


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
