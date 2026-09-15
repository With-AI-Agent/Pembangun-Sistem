# Model Konten Brief — Kartu Teks 8–10 (Channel: Kisah Sudut Kota)

### Dokumen "hidup" milik SATU model konten dalam SATU channel. Hasil dari `07_MODEL_KONTEN_DISCOVERY_PROMPT.md`.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — draf pertama selesai 2026-09-15
- [x] **Reviewed** — dibaca lengkap oleh pemilik 2026-09-15
- [x] **Approved** — dikunci lewat gerbang **G2** 2026-09-15 (gerbang **G2-a** sesi `arena/01a0a448`)
- [ ] **Merged** — menunggu gerbang **G3** (PR tanpa auto-merge)
- [ ] **Operational** — belum; hanya boleh dipakai produksi setelah `Merged` dan seluruh checklist di bawah tercentang

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan: unit breakdown = **kartu teks**
- [x] Override terhadap Channel Brief sudah dinyatakan eksplisit: 2 override (larangan "teks besar di layar" di bagian 5, dan terjemahan "karakteristik suara/voice" jadi ritme baca) + 1 penambahan platform
- [x] Gerbang tambahan sudah dicatat — **tidak ada gerbang tambahan**; G2/G3 bawaan tetap berlaku dan tidak ada yang dihapus
- [x] Channel Brief induknya sudah berstatus `Operational` (v3 — pengecualian gap warisan **sudah ditutup** 2026-09-15, jadi `Operational` kini tanpa pengecualian)
- [ ] Sudah `Merged` ke `main`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-15`

## Mewarisi dari: `channel-fixture-kisah-sudut-kota/channel-brief.md`

Semua yang sudah dikunci di Channel Brief — Persona & Voice (bagian 3), batasan klaim, Area Berisiko Tinggi (bagian 6) — otomatis berlaku di sini tanpa ditulis ulang. Brief ini hanya menambahkan yang spesifik untuk format teks-only.

Dua catatan pewarisan yang dinyatakan jujur, bukan disembunyikan:

1. **Channel induknya adalah FIXTURE** (lihat header `channel-brief.md`). Model ini dibangun sebagai artefak produksi sungguhan di atas channel fixture itu.
2. **Brand Core belum pernah diisi.** `_sistem/01_BRAND_CORE.md` masih berupa dokumen generator — bagian hasilnya masih heading `## [ISI DENGAN HASIL DISKUSI DI ATAS — kosong sampai kamu jalankan prompt-nya]` tanpa isi. Jadi rantai pewarisan Brand Core → Channel → Model di sini bersifat formal, bukan substantif.

---

## 1. Identitas Model Konten

- **Nama model konten:** Kartu Teks 8–10
- **Definisi singkat (beda dari model konten lain di channel yang sama):** satu cerita sudut kota disampaikan sebagai **rangkaian 8–10 kartu berisi teks saja** — tanpa gambar, tanpa video, tanpa audio. Berbeda dari `Narasi 60 Detik` yang mengandalkan voice over + b-roll: di model ini **teks adalah medianya**, bukan keterangan pendamping visual. Tidak ada asset yang digenerate atau diakuisisi sama sekali; konsistensi dijaga lewat tipografi, layout, dan palet warna solid — bukan lewat gambar referensi.

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** **8–10 kartu**. Per kartu **18–28 kata**, kecuali kartu 1 (hook) **maksimal 15 kata**. Total **±160–250 kata**, waktu baca **±60–90 detik** pada kecepatan baca santai. Satu kartu = satu gagasan; kartu tidak boleh dipecah di tengah gagasan.
- **Struktur konten khas format ini:**
  1. **Kartu 1 — Hook:** satu sudut kota konkret sebagai pintu masuk, ≤ 15 kata. Boleh memakai pola pembuka khas channel (*"Di sudut [tempat], ada satu kebiasaan yang tidak pernah berubah."*).
  2. **Kartu 2 — Kebiasaan yang menempel:** apa yang selalu terjadi di sudut itu.
  3. **Kartu 3 sampai n−2 — Akumulasi:** tiap kartu menambah satu detail atau satu lapis pengamatan. Tidak ada kartu yang mengulang gagasan kartu sebelumnya.
  4. **Kartu n−1 — Yang berubah:** pergeseran, kehilangan, atau hal yang tidak lagi sama. Tanpa dramatisasi.
  5. **Kartu n — Penutup:** mengajak penonton melihat sudut terdekatnya sendiri. Boleh memakai pola penutup khas channel (*"Lain kali kamu lewat situ, lihat pelan-pelan."*).
- **Platform paling cocok untuk format ini:** **platform-agnostik** — satu set kartu yang sama bisa dipakai sebagai **carousel Instagram** maupun **thread X/Twitter** tanpa diubah isinya. Ini **menambah** platform, **bukan mengganti** platform yang dikunci Channel Brief bagian 1 (YouTube Shorts + TikTok) — jadi Channel Brief tidak perlu direvisi untuk model ini.

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** **tidak ada asset gambar sama sekali.** Tidak ada foto, ilustrasi, ikon, logo, maupun gambar hasil generate. Yang dikunci di model ini sebagai pengganti "gaya visual" adalah **tipografi dan layout kartu**:
  - Latar: **satu warna solid** diambil dari palet Channel Brief bagian 5 — `abu aspal` atau `biru pudar` sebagai latar utama. Warna solid adalah **spesifikasi**, bukan file asset, sehingga Tahap 5 tetap tidak berlaku.
  - Teks: satu warna kontras terhadap latar, satu jenis huruf, satu ukuran per tingkatan (judul kartu vs isi).
  - Aksen: **maksimal satu** warna aksen per kartu (`kuning pagi` atau `oranye lampu sodium`) untuk **maksimal satu frasa** yang perlu ditekankan.
  - Nomor kartu ditampilkan konsisten (mis. `1/9`) supaya pembaca tahu sisa rangkaian.
  - Dilarang: foto, ilustrasi, ikon, logo merek, gradien, tekstur, dan wajah orang yang bisa dikenali.
- **OVERRIDE EKSPLISIT terhadap Channel Brief bagian 5:** Channel Brief melarang **"teks besar di layar"** — aturan itu dibuat untuk model b-roll, di mana teks besar bersaing dengan gambar. Di model ini **teks adalah satu-satunya medium**, jadi larangan tersebut **tidak berlaku**. Yang tetap dipertahankan dari aturan aslinya: tidak ada logo merek dan tidak ada wajah orang yang bisa dikenali.
- **Elemen Konsistensi Visual dari channel:** tidak ada yang perlu ditampilkan — Channel Brief bagian 4 tidak mengunci elemen visual apa pun (semua ditandai "tidak berlaku"). Karena itu palet warna solid di atas berfungsi sebagai **satu-satunya jangkar konsistensi visual** model ini.

## 4. Alur Kerja Produksi

**Mode:** [x] Ikuti Kerangka Standar (dengan override ringan)  /  [ ] Alur Kerja Kustom

### Kalau Mode = Ikuti Kerangka Standar

- **Override Persona/Voice:** Tone, gaya bahasa, kosakata khas, dan seluruh larangan Channel Brief bagian 3 **berlaku tanpa perubahan**. Satu penyesuaian teknis dinyatakan eksplisit: **"karakteristik suara/voice"** di Channel Brief (suara dewasa muda, tempo ± 130 kata/menit, jeda 0,5 detik tiap ganti gagasan) **tidak berlaku sebagai audio** karena model ini tanpa suara. Aturan itu **diterjemahkan jadi ritme baca**: satu gagasan per kartu, dan **perpindahan kartu menggantikan fungsi jeda 0,5 detik**. "Kalimat pendek" dan "tanpa basa-basi" tetap mengikat penuh.
- **Bentuk konkret Tahap Breakdown untuk format ini:** **kartu teks**. `05_CONTENT_PRODUCTION_PIPELINE.md` Tahap 4 menyebut bentuk generik `bagian/paragraf` untuk konten teks-only; brief ini menetapkan bentuk yang lebih spesifik — **kartu** — karena satu kartu adalah satu satuan yang berdiri sendiri dan dibaca terpisah. File breakdown disimpan sebagai `breakdown-output.md` di folder produksi.
- **Override Ringan per Tahap:**
  - **Tahap 1 (Ideation):** tidak ada override.
  - **Tahap 2 (Konsep & Angle):** kerangka disusun sebagai **peta 8–10 kartu** (satu baris per kartu), bukan sebagai beat berdurasi. Jumlah kartu harus sudah pasti di tahap ini.
  - **Tahap 3 (Naskah/Script):** naskah ditulis **per kartu** dengan batas 18–28 kata (kartu 1 ≤ 15 kata), total ±160–250 kata. Batas ini diperiksa dan dicatat angkanya sebelum meminta G2.
  - **Tahap 4 (Breakdown Output):** unit = **kartu teks**. Kolom *prompt generate* dan *file referensi visual* **dikosongkan dengan keterangan eksplisit** `tidak berlaku — konten teks-only` (bukan diisi asal supaya formatnya penuh). Sebagai gantinya tiap kartu memuat **arahan penyampaian**: frasa mana yang mendapat warna aksen, dan di mana penekanan baca.
  - **Tahap 5 (Generate/Acquire Assets):** **TIDAK BERLAKU.** Tidak ada satu pun asset yang digenerate atau diakuisisi. Dicatat di `STATUS.md` sebagai `Tahap 5 — tidak berlaku (konten teks-only)` — keputusan sadar yang tercatat, bukan tahap yang terlupakan.
  - **Tahap 6 (Assembly & Publish Prep):** **tidak ada thumbnail dan tidak ada deskripsi konsep thumbnail** (tidak ada gambar). Output final = **urutan kartu sebagai teks siap tempel** (satu blok per kartu, lengkap dengan nomor kartu) + caption + hashtag. Langkah penutup tetap wajib penuh: pindah naskah ke `arsip-naskah/`, update `indeks.md`, update `indeks-karakter.md` kalau ada tokoh Tipe B, dan buat arsip ringan `-metadata.md`.
- **Gerbang:** **tidak ada gerbang tambahan.** Gerbang bawaan `05_CONTENT_PRODUCTION_PIPELINE.md` berlaku utuh dan tidak ada yang dihapus: Tahap 1 = G1; Tahap 2 = G1; Tahap 3 = G1 + G2; Tahap 4 = G1 + G2; Tahap 5 = dilewati; Tahap 6 = G2 + G3.

### Kalau Mode = Alur Kerja Kustom

Tidak berlaku — model ini mengikuti kerangka standar.

## 5. Contoh Konkret

Contoh dari Bank Ide Awal Channel Brief bagian 7 (ide *"Gerbang gang yang selalu terbuka, padahal tidak ada yang jaga"*), 9 kartu:

| Kartu | Isi (ringkas) | Fungsi |
|---|---|---|
| 1 | *"Di sudut gang itu, gerbangnya tidak pernah dikunci."* (9 kata) | Hook — sudut kota konkret |
| 2 | Tidak ada yang jaga; tidak ada pos; hanya gerbang besi yang digeser. | Kebiasaan yang menempel |
| 3 | Pagi: dibuka dari dalam oleh orang pertama yang lewat. | Akumulasi |
| 4 | Siang: anak-anak menjadikannya gawang. | Akumulasi |
| 5 | Malam: tetap terbuka, lampunya mati separuh. | Akumulasi |
| 6 | Tidak ada yang pernah bertanya siapa yang menutup. | Akumulasi |
| 7 | Suatu hari gerbangnya diganti baru, ada gagang kuncinya. | Yang berubah |
| 8 | Kuncinya tidak pernah dipakai. | Yang berubah — tanpa dramatisasi |
| 9 | *"Lain kali kamu lewat situ, lihat pelan-pelan. Kota ini tidak pernah bercerita dua kali."* | Penutup khas channel |

Validasi: contoh ini memakai 9 kartu (dalam rentang 8–10), kartu 1 ≤ 15 kata, tidak ada angka/tanggal/nama resmi (mematuhi larangan Channel Brief bagian 3), sudut yang bercerita dan orangnya hanya menempel (mematuhi bagian 6), dan tidak butuh satu pun gambar.

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-15 | Nama model = **Kartu Teks 8–10**, folder `model-konten/kartu-teks-8-10/` | Konvensi repo menaruh angka pembeda di nama (`narasi-60-detik`, `data-60-detik`, `dongeng-60-90`); menyebut unit + jumlah adalah yang paling dibutuhkan agent saat produksi. Nama channel tidak dipakai di nama model karena foldernya sudah berada di dalam channel itu. Keputusan didelegasikan pemilik ("Yang terbaik gimana?") |
| 2026-09-15 | Platform = **agnostik** (carousel Instagram / thread X), Channel Brief bagian 1 **tidak** direvisi | Pilihan pemilik. Model menambah platform, bukan mengganti yang dikunci channel, sehingga tidak memicu G2 revisi Channel Brief |
| 2026-09-15 | Latar warna solid + 1 warna aksen **diizinkan**; foto/ilustrasi/ikon dilarang | "Tanpa gambar" dibaca sebagai *tidak ada file asset gambar*, bukan *tidak ada warna*. Warna solid adalah spesifikasi, bukan asset — Tahap 5 tetap tidak berlaku. Kanvas polos murni akan membuang palet channel, padahal channel ini tidak punya Bank Konsistensi Visual sehingga palet adalah satu-satunya jangkar visual. Keputusan didelegasikan pemilik ("Yang terbagus gimana?") |
| 2026-09-15 | Larangan **"teks besar di layar"** (Channel Brief bagian 5) **di-override** untuk model ini | Aturan itu dibuat untuk model b-roll, tempat teks besar bersaing dengan gambar. Di model teks-only, teks adalah satu-satunya medium. Larangan logo merek dan wajah yang bisa dikenali tetap dipertahankan |
| 2026-09-15 | Alur kerja = **kerangka standar dengan override ringan**, unit breakdown = **kartu teks** | Pilihan pemilik. Struktur produksi tidak beda dari akar; yang beda hanya bentuk unit dan Tahap 5 yang tidak berlaku. `05_CONTENT_PRODUCTION_PIPELINE.md` Tahap 4 sudah punya baris tabel khusus konten teks-only, jadi ini kasus normal, bukan pengecualian |
| 2026-09-15 | Batas per kartu 18–28 kata (hook ≤ 15), total ±160–250 kata, 8–10 kartu | Menjaga "kalimat pendek" dan "tanpa basa-basi" dari Persona & Voice channel; rentang total memberi waktu baca ±60–90 detik supaya setara ritme model `Narasi 60 Detik` |
