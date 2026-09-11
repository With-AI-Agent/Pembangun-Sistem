# Catatan Aset Referensi — Kantor Pos Miso (Tahap 2 Kit, 2026-09-11_3)

| File | Ukuran | SHA-256 (7) |
|---|---|---|
| `miso/acuan-utama.png` | 1,998,400 B | `5563eaf` |
| `miso/reference-sheet.png` | 2,014,025 B | `199262a` |
| `kota-kanala/sudut-eksterior-kantor-pos.png` | 2,982,759 B | `b3f48b0` |
| `kota-kanala/sudut-interior-lobby.png` | 3,020,827 B | `4bb5cba` |
| `kota-kanala/sudut-jalan-senja.png` | 2,944,729 B | `6e6e1de` |
| `props-kantor-pos-miso/acuan-utama.png` | 1,974,744 B | `9fbf453` |
| `palet-gaya-catok/contoh-negatif-3d-render.png` | 2,097,082 B | `eb30971` |
| `palet-gaya-catok/palet.png` | 2,301,858 B | `0688aa2` |
| `palet-gaya-catok/style-sheet.png` | 2,342,344 B | `48b652d` |

## Hasil audit visual per file (standar: checklist Tahap 5 pipeline + tabel reference pack kit)

| File | Verdict | Catatan |
|---|---|---|
| miso/acuan-utama.png | BERSIH | Semua ciri terkunci ada: loreng oranye pudar, kaus kaki 4 + ujung ekor putih, mata amber, rompi navy 2 kuningan, tas merah cross-strap + lonceng; netral default, latar krem |
| miso/reference-sheet.png | BERSIH | 8 panel (turnaround 4 + ekspresi 4) konsisten identitas; ekspresi "kesal" tampil sebagai manyun kecil bermartabat — aman anti-OOC |
| kota-kanala/sudut-eksterior-kantor-pos.png | BERSIH | Terakota + pintu hijau botol + slot kuningan + jam + kotak pos hijau pudar cat mengelupas + batu berumput + sepeda; tanpa teks |
| kota-kanala/sudut-interior-lobby.png | BERSIH | Konter hijau-botol kuningan, rak kotak kayu, jam ±08.00, tas+rompi di gantungan (konsisten), tanpa orang/teks |
| kota-kanala/sudut-jalan-senja.png | PERLU REGENERASI | Suasana & palet pas, TAPI ada plang terbaca "BOOKSHOP"/"HARDWARE STORE" — melanggar 'tanpa teks terbaca di gambar'; regen tanpa plang (antre — batas generate giliran tercapai) |
| props-kantor-pos-miso/acuan-utama.png | BERSIH (hasil regen ke-2) | Versi pertama ditolak: plang kotak pos "LETTERS/GR/mahkota" & cap "LONDON ROYAL MAIL" = aroma merek nyata; versi sekarang tanpa teks/mahkota/lambang, keempat objek sesuai |
| palet-gaya-catok/palet.png | BERSIH | 8 swatch watercolor bleeds di kertas — urutan warna sesuai tabel hex bank |
| palet-gaya-catok/style-sheet.png | PERLU REGENERASI | Gaya benar, TAPI Miso pakai topi poso navy (bukan bagian identitas terkunci — acuan utama tanpa topi) dan kotak pos gaya AS; regen tanpa topi + pillar box hijau (antre — batas generate giliran tercapai) |
| palet-gaya-catok/contoh-negatif-3d-render.png | BERSIH | Tepat sebagai contoh negatif: glossy 3D studio, tanpa watercolor/grain; coretan merah kecil di pojok = artefak, file ini memang untuk DIHINDARI, tidak dipakai generate |

## Status Reference-Ready
- `miso/` dan `props-kantor-pos-miso/` — acuan wajib ADA & bersih → boleh `Reference-Ready` (ditetapkan setelah regen 2 file terakhir & G1 aset)
- `kota-kanala/` dan `palet-gaya-catok/` — tunggu 1 regen masing-masing
