# Bank Konsistensi Visual — Props Kantor Pos Miso

### Dibangun via `04_CHARACTER_BUILDER_KIT.md` — 2026-09-11_3. Elemen milik channel `channel-kantor-pos-miso`.

**Status:** `Reference-Ready` — G2 `setuju_g2` 2026-09-11; seluruh acuan wajib ADA di `referensi/` dan lolos audit visual (lihat `../CATATAN-ASSET.md`) `referensi/acuan-utama.png` ada (tipe acuan Props = acuan utama tunggal + sudut tambahan bila perlu).

## Jenis Elemen

Props/Objek Berulang — empat objek ciri khas yang muncul lintas episode dan harus tetap sama bentuk & warnanya.

## Deskripsi (Prompt-Ready)

1. **Tas pos merah Miso** — tas selempang kulit merah bata (hex palet: `#B04A3A`) berbentuk flap bulat melembung, tali tunggal melintang dada, gesper kuningan kecil dengan **lonceng kuningan seukuran kelereng** di dekat gesper; tepi bawah sedikit gompal/terkelupas lembut; terlihat agak kebesaran untuk tubuh Miso — flap menutup tidak sempurna saat penuh surat.
2. **Sepeda tua Kanala** — sepeda onthel frame hijau botol (`#3B5C4F`), keranjang rotan PENUH surat di setang, sadel kulit cokelat, bel kuningan, spatboard krem; selalu diparkir condong bersandar (tidak pernah ada standar tengah — dia selalu buru-buru).
3. **Cap kantor pos** — stempel postmark kuningan dengan gagang kayu gelap; di episode tertentu cap "berbicara" lewat bunyi: TUK. TUK. dua ketukan, lalu jeda — pola bunyi khas pagi.
4. **Kotak pos hijau pudar** — milik latar (`../kota-kanala/`), dirujuk di sini agar konsisten: kotak pos tua berdiri, cat hijau pudar mengelupas di sudut, condong ke satu sisi, slot surat kuningan.

Konteks pemakaian: tas SELALU di punggung Miso saat keluar kantor/di jalan (di interior kantor boleh di gantungan konter); sepeda = alat antar utama di semua episode luar; cap hanya di kantor; kotak pos selalu ada di frame exterior kantor.

## Gaya Visual

Mengikuti `../palet-gaya-catok/bank-konsistensi.md`.

## Prompt Master (Reusable)

```
red brick-colored leather postman satchel with rounded puffed flap, single
crossed shoulder strap, small brass buckle with a tiny marble-sized brass
bell, softly worn bottom edges, slightly too big for its young owner; old
bottle-green bicycle with a wicker basket full of letters on the handlebar,
brown leather saddle and brass bell, leaning without a kickstand; vintage
brass postmark stamp with dark wooden handle; faded green vintage street
mailbox with chipped paint leaning slightly, large brass mail slot; all
items together as a character's belonging set; picture-book watercolor and
gouache illustration, soft graphite pencil outlines, matte paper grain,
muted warm palette, diffused golden light
```

## Referensi

- `referensi/acuan-utama.png` — keempat props dalam satu lembar (prop sheet netral, latar krem kertas)

## Log Keputusan Elemen

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-11 | 4 props dikunci (tas, sepeda, cap, kotak pos); kotak pos tetap milik elemen Latar, dirujuk silang | Pemilik memilih scope `karakter_semua` — props jadi ciri khas; menghindari duplikasi definisi 2 tempat |
| 2026-09-11 | Tas kebesaran + lonceng seukuran kelereng = ciri "kanak-kanak yang belum proporsional dengan pekerjaannya" | Menguatkan tema channel: muda, baru lulus, berusaha dipercaya |
