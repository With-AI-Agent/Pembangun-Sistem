# Metadata Reproducibility — Melati Terakhir di Pasar Kosong

- **Channel:** `channel-fixture-narasi-sejarah` (Narasi Sejarah — FIXTURE)
- **Model konten:** Narasi 60 Detik (v1 Operational) — unit segmen narasi, 130-145 kata, 55-65 detik
- **Tanggal produksi:** 2026-09-10
- **Branch produksi:** `arena/01a089b8-pembangun-sistem`
- **Judul kerja:** Melati Terakhir di Pasar Kosong
- **Judul tayang resmi yang diusulkan:** "Melati Terakhir di Pasar yang Mulai Kosong" (Opsi 1 dari 5 opsi di publish-prep.md — menunggu G2 konten final)
- **Naskah final:** 131 kata, 63,46 dtk estimasi (60,46 + 3 dtk jeda), wc -w = 131, tempo 130 kata/menit
- **Topik singkat:** melati terakhir sebagai penanda waktu pasar tutup; payung biru dilipat sebelum tengah hari di sudut pasar yang mulai kosong karena pindah

## Versi brief yang dipakai

- **Channel Brief:** v2 — 2026-09-09 — `channel-fixture-narasi-sejarah/channel-brief.md` — Operational
- **Model Konten Brief:** v1 — 2026-09-04 — `channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md` — Operational
- **Brand Core:** masih template kosong — gap dilaporkan (Channel Brief v2 mencatat gap ini) — tidak ada nilai lintas-channel yang diwarisi
- **Pipeline:** `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md` — 6 tahap kerangka standar + override ringan Model Brief
- **Prompt Library:** `_sistem/06_PROMPT_LIBRARY.md` — teknik A2 karakter Tipe B, D generate gambar b-roll

## Prompt final per unit visual (dari breakdown-output.md + CATATAN-ASSET.md)

### S1 — Hook — Keranjang Melati
```
Subjek/fokus utama: keranjang anyam bambu berisi genggam melati putih segar, satu genggam terakhir
Environment/setting: sudut pasar tradisional pagi, cahaya matahari pagi lembut, background blur lapak kayu
Gaya visual: foto benda sehari-hari, warna hangat sedikit pudar, tekstur film, palet cokelat kayu + krem + putih melati, vertical 9:16, high detail
Mood/lighting: hangat, tenang, sedikit melankolis, soft morning light
Framing/angle: close-up eye-level, shallow depth of field
Hal yang harus dihindari: wajah orang yang bisa dikenali, logo merek, teks besar di layar
```
- File referensi: tidak ada — channel faceless
- File asset: `S1-hook-keranjang-melati.jpg` — 240K — SHA256 `563f7ac096f66af172713d43cc0e54f59a619cbe7cc66f29704c1365c9f1a3db`

### S2 — Detail Karakter Tipe B
```
Subjek/fokus utama: payung biru pudar terbuka di sudut pasar, selendang batik cokelat digulung di bahu sosok perempuan tua dari belakang (rambut putih dikonde rendah, wajah tidak detail/buram, tidak dikenali), keranjang anyam di lengan
Environment/setting: sudut pasar tradisional paling gelap tapi sejuk, pagi subuh, lapak kayu kosong di background
Gaya visual: b-roll netral, warna hangat pudar, tekstur film, palet cokelat kayu + biru pudar + krem, vertical 9:16
Mood/lighting: tenang, nostalgia, soft light, tidak dramatisir
Framing/angle: medium shot dari belakang/samping, tidak ada wajah dikenali
Hal yang harus dihindari: wajah detail yang bisa dikenali, logo merek, teks besar
```
- File referensi: tidak ada
- File asset: `S2-payung-biru-sudut-gelap.jpg` — 230K — `a878f5d02d9161bdc0321051ef3b9d9a6c554cf38185d65108243450b0c89c96`
- Catatan karakter Tipe B reuse: deskripsi fisik sama persis dengan arsip `2026-09-09-penjual-bunga-di-pasar-subuh.md` — "perempuan tua usia lanjut, rambut putih dikonde rendah, selendang batik cokelat digulung di bahu, payung biru pudar, keranjang anyam berisi melati putih di lengan, biasanya dilihat dari belakang/samping — wajah tidak detail"

### S3 — Kebiasaan Menyusun
```
Subjek/fokus utama: tangan tua perempuan (kulit keriput, tanpa wajah) menyusun bunga melati putih satu per satu ke dalam keranjang anyam bambu, gerakan pelan ritual
Environment/setting: sudut pasar tradisional gelap tapi sejuk, cahaya pagi sela-sela, keranjang anyam di atas kain putih
Gaya visual: close-up detail tangan + melati, warna hangat pudar, tekstur film, vertical 9:16, palet krem + cokelat kayu + putih melati
Mood/lighting: hangat, intim, tenang, soft light
Framing/angle: close-up tangan, shallow depth, tidak ada wajah
Hal yang harus dihindari: wajah dikenali, logo, teks besar
```
- File asset: `S3-tangan-menyusun-melati.jpg` — 233K — `8bb9b497169733aff191c467f2c097dc2beb653235dbbef7d297bf54df6d39de`

### S4 — Penanda Waktu
```
Subjek/fokus utama: sudut pasar tradisional dengan payung biru pudar dan keranjang melati putih masih ada, beberapa siluet pembeli lewat blur di background
Environment/setting: pasar pagi yang mulai menipis, cahaya pagi, lapak kayu
Gaya visual: b-roll wide, warna hangat pudar, tekstur film, vertical 9:16, palet cokelat kayu + hijau tua pudar + biru pudar
Mood/lighting: hangat-melankolis, tenang, tidak ramai
Framing/angle: wide shot eye-level, depth, tidak ada wajah dikenali
Hal yang harus dihindari: wajah detail, logo merek, teks besar
```
- File asset: `S4-sudut-pasar-melati-masih-ada.jpg` — 245K — `b654aa2db28e8409fa96348d7b7508d5b645940325cc2d2fe39819e597a947f7`

### S5 — Pasar Mulai Kosong
```
Subjek/fokus utama: deretan lapak pasar tradisional kosong, kayu, pagi, hanya satu sudut dengan payung biru pudar yang masih terbuka, keranjang anyam hampir kosong dengan satu genggam melati putih terakhir
Environment/setting: pasar pagi yang mulai kosong karena pindah, cahaya pagi, suasana sepi tapi tidak dramatis
Gaya visual: b-roll, warna hangat pudar sedikit desaturasi, tekstur film, vertical 9:16, palet cokelat kayu + krem + biru pudar + putih melati
Mood/lighting: melankolis ringan, tenang, tidak sedih berlebihan, soft morning light
Framing/angle: medium-wide, eye-level, menunjukkan kekosongan bertahap
Hal yang harus dihindari: wajah dikenali, logo, teks besar, dramatisir berlebihan
```
- File asset: `S5-lapak-kosong-satu-genggam-terakhir.jpg` — 251K — `6c3990e1e3882709552c2b29b71260e5cbc10807f6160521911f812a88723f55`

### S6 — Aksi Jual & Lipat Payung
```
Subjek/fokus utama: tangan tua menyerahkan satu genggam melati putih terakhir ke tangan pembeli (blur, tidak ada wajah), lalu payung biru pudar dilipat setengah, keranjang anyam kosong di samping
Environment/setting: sudut pasar kosong pagi, cahaya pagi, lapak kosong background
Gaya visual: close-up + medium, warna hangat pudar, tekstur film, vertical 9:16, palet biru pudar + putih melati + cokelat kayu
Mood/lighting: hangat, penutup ritual, tenang, sedikit melankolis tanpa dramatisir
Framing/angle: close-up serah terima (tangan saja), lalu medium shot payung dilipat
Hal yang harus dihindari: wajah dikenali, logo, teks besar
```
- File asset: `S6-jual-terakhir-lipat-payung.jpg` — 214K — `546124471d3e4e504a4a8c4f885786f5deed75083c8eb0f51ef47d4b21278867`

### S7 — Penutup Masa Kini
```
Subjek/fokus utama: sudut pasar tradisional yang sama sekarang kosong, tidak ada payung, tidak ada keranjang, hanya lantai kayu dan cahaya pagi, bayangan payung tidak ada
Environment/setting: pasar yang sudah kosong/pindah, pagi, sepi, bersih
Gaya visual: b-roll, warna hangat pudar, tekstur film, vertical 9:16, palet cokelat kayu + krem + hijau tua pudar, sedikit kosong
Mood/lighting: tenang, nostalgia ringan, hangat-melankolis, soft light
Framing/angle: wide shot sudut kosong, eye-level, negative space
Hal yang harus dihindari: wajah, logo merek, teks besar
```
- File asset: `S7-sudut-kosong-sekarang.jpg` — 246K — `da5ae7cb295e6b9236bf59dd17bfbb7e108f5d86f78d6a39dbff3371178d5d1a`

## Daftar asset

- **Lokasi di repo (sementara):** `sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-melati-terakhir-di-pasar-kosong/assets/` — 7 JPG + CATATAN-ASSET.md — total 1,7 MB
- **Lokasi permanen di luar repo (setelah download):** sesuai konfirmasi pemilik — syarat pipeline langkah 5 terpenuhi setelah pemilik konfirmasi punya salinan permanen di luar repo + verifikasi file arsip ada di main
- **Prompt final:** lihat di atas + breakdown-output.md + CATATAN-ASSET.md
- **File referensi yang disertakan saat generate:** tidak ada — channel faceless, tidak ada Bank Konsistensi Visual yang dikunci (Channel Brief bag 4 "Tidak berlaku")
- **Hash asset:** tercatat di CATATAN-ASSET.md (SHA256 per file)

## Elemen konsistensi visual yang dirujuk

- **Tidak ada elemen Bank Konsistensi Visual yang dikunci** — channel faceless (Channel Brief bag 4)
- **Karakter Tipe B reuse:** Nenek Penjual Bunga — rambut putih dikonde rendah, selendang batik cokelat, payung biru pudar, keranjang anyam berisi melati putih di lengan — deskripsi sama persis di S2,S3,S5,S6 — reuse dari `indeks-karakter.md`, bukan karakter baru — status tetap Tipe B, konten pertama `2026-09-09-penjual-bunga-di-pasar-subuh.md`, konten kedua `2026-09-10-melati-terakhir-di-pasar-kosong.md` (kolom Konten lain)
- **Gaya visual channel:** footage arsip dan foto benda sehari-hari, warna cenderung hangat dan sedikit pudar, tekstur film; palet dominan cokelat kayu, krem, hijau tua pudar + putih melati + biru pudar payung; hindari wajah dikenali, logo merek, teks besar di layar — dipatuhi di semua asset

## Karakter Tipe B

- **Nama/sebutan:** Nenek Penjual Bunga
- **Ciri ringkas:** rambut putih dikonde rendah, selendang batik cokelat, payung biru pudar, keranjang anyam di lengan, pojok pasar subuh
- **Konten pertama:** `2026-09-09-penjual-bunga-di-pasar-subuh.md`
- **Konten kedua (ini):** `2026-09-10-melati-terakhir-di-pasar-kosong.md` — ditambahkan ke kolom Konten lain pada Tahap 6 langkah 2b
- **Status:** `Tipe B` — tetap Tipe B (tidak naik ke Tipe A) — keputusan pemilik 2026-09-10 via ask_user

## Sumber eksternal

- **Tidak ada** — cerita personal fiksi fixture, bukan klaim sejarah hasil riset
- **SUMBER.md:** tidak ada — tidak wajib (tidak ada klaim faktual yang butuh verifikasi)
- **Lisensi/hak asset:** asset generated via image generation tool, bukan stok berhak cipta, bukan footage pihak ketiga — tidak ada atribusi wajib
- **Gerbang fact-check:** Tahap 3 G2 — tidak ada klaim faktual yang butuh SUMBER.md — dilaporkan eksplisit saat minta G2

## Catatan produksi

- **Ideation:** 4 opsi, ide terpilih Opsi 1 Melati Terakhir Sebagai Jam Pasar — cek pengulangan vs arsip 2026-09-09 Penjual Bunga di Pasar Subuh — angle beda (akhir/transisi vs rutinitas) — G1 disetujui 2026-09-10
- **Konsep & Angle:** hook "Dulu, ada satu genggam melati yang selalu habis paling akhir." + 2 varian, struktur 4 beat (0-8 benda pintu masuk, 8-35 konteks kebiasaan, 35-52 yang berubah, 52-60 penutup masa kini), estimasi 132 kata / 63,92 dtk, visual b-roll 7 segmen — G1 disetujui 2026-09-10
- **Naskah:** 131 kata, 63,46 dtk estimasi, Persona & Voice check lengkap (santai tertata kalimat pendek, hangat-melankolis, kosakata khas dulu/konon/tidak ada yang mencatat, HARUS ADA benda/ruang melati+sudut pasar, TIDAK BOLEH ADA dipatuhi, pembuka/penutup khas varian dipakai) — G1+G2 disetujui 2026-09-10
- **Breakdown:** 7 segmen narasi, b-roll netral, prompt generate per segmen, file referensi tidak ada (channel faceless — keterangan eksplisit), karakter Tipe B reuse sama persis — G1+G2 disetujui 2026-09-10
- **Assets:** 7 JPG b-roll netral vertical 9:16, total 1,7 MB, hash tercatat, checklist Tahap 5 lengkap, S2 sebagai acuan visual awal — G1 disetujui 2026-09-10
- **Publish prep:** 5 opsi judul (rekomendasi Opsi 1 "Melati Terakhir di Pasar yang Mulai Kosong"), caption panjang & pendek Persona & Voice, hashtag, thumbnail konsep tanpa clickbait (close-up keranjang anyam satu genggam melati putih terakhir dengan payung biru pudar blur background)
- **Final content:** assembly notes + ringkasan 7 segmen + metadata publish ringkas
- **Langkah penutup WAJIB:** 1) naskah final dipindahkan ke arsip (file ini + `2026-09-10-melati-terakhir-di-pasar-kosong.md`), 2) indeks.md diperbarui (entri ke-4), 2b) indeks-karakter.md diperbarui (konten kedua di kolom Konten lain), 4) metadata reproducibility ini dibuat — semua sudah dilakukan sebelum G2+G3 Tahap 6
- **Syarat penghapusan folder produksi (pipeline langkah 5):** langkah 1,2,2b,4 sudah dilakukan — Agent WAJIB verifikasi file arsip benar-benar ada di main sebelum menghapus, dan pemilik harus konfirmasi punya salinan permanen di luar repo — belum dilakukan, folder produksi dipertahankan sampai G2+G3 disetujui dan PR merged
