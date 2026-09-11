# Catatan Aset Referensi — Kantor Pos Miso (Tahap 2 Kit, 2026-09-11_3)

| File | Ukuran | SHA-256 (7) |
|---|---|---|
| `miso/acuan-utama.png` | 1,998,400 B | `5563eaf` |
| `miso/reference-sheet.png` | 2,014,025 B | `199262a` |
| `kota-kanala/sudut-eksterior-kantor-pos.png` | 2,982,759 B | `b3f48b0` |
| `kota-kanala/sudut-interior-lobby.png` | 3,020,827 B | `4bb5cba` |
| `kota-kanala/sudut-jalan-senja.png` | 2,950,902 B | `4854305` |
| `props-kantor-pos-miso/acuan-utama.png` | 1,974,744 B | `9fbf453` |
| `palet-gaya-catok/contoh-negatif-3d-render.png` | 2,097,082 B | `eb30971` |
| `palet-gaya-catok/palet.png` | 2,301,858 B | `0688aa2` |
| `palet-gaya-catok/style-sheet.png` | 2,890,560 B | `afbefa4` |

## Hasil audit visual per file (standar: checklist Tahap 5 pipeline + tabel reference pack kit)

| File | Verdict | Catatan |
|---|---|---|
| `miso/referensi/acuan-utama.png` | BERSIH | Semua ciri terkunci ada: loreng oranye pudar, kaus kaki 4 + ujung ekor putih, mata amber, rompi navy 2 kuningan, tas merah cross-strap + lonceng; netral default, latar krem |
| `miso/referensi/reference-sheet.png` | BERSIH | 8 panel (turnaround + ekspresi) konsisten identitas; ekspresi "kesal" tampil sebagai manyun kecil bermartabat — aman anti-OOC |
| `kota-kanala/referensi/sudut-eksterior-kantor-pos.png` | BERSIH | Terakota + pintu hijau botol + slot kuningan + jam + kotak pos hijau pudar + batu berumput + sepeda; tanpa teks |
| `kota-kanala/referensi/sudut-interior-lobby.png` | BERSIH | Konter hijau-botol kuningan, rak kotak kayu, jam ±08.00, tas+rompi di gantungan (konsisten), tanpa orang/teks |
| `kota-kanala/referensi/sudut-jalan-senja.png` | BERSIH (hasil regen ke-2) | V1 ditolak: plang terbaca "BOOKSHOP/HARDWARE STORE". V2: kanopi & plang blank total, hanya piktogram etalase tanpa huruf; gang batu + kanal + lampu senja + sepeda + surat di slot pintu — sesuai bank |
| `props-kantor-pos-miso/referensi/acuan-utama.png` | BERSIH (hasil regen ke-2) | V1 ditolak: "LETTERS/GR/mahkota" & cap "LONDON ROYAL MAIL" (aroma merek nyata). V2: tanpa teks/mahkota/lambang; tas+bells, sepeda keranjang surat, cap gagang kayu dasar kosong, pillar box hijau cat mengelupas — sesuai bank |
| `palet-gaya-catok/referensi/palet.png` | BERSIH | 8 swatch watercolor bleeds di kertas — urutan warna sesuai tabel hex bank |
| `palet-gaya-catok/referensi/style-sheet.png` | BERSIH (hasil regen ke-2) | V1 ditolak: Miso pakai topi navy (bukan identitas) + kotak pos gaya AS. V2: tanpa topi di semua panel, pillar box hijau blank, 4 adegan (kotak pos, mencap, sepeda, jendela senja) konsisten acuan utama |
| `palet-gaya-catok/referensi/contoh-negatif-3d-render.png` | BERSIH | Tepat sebagai contoh negatif: glossy 3D studio; coretan merah pojok = artefak, file ini untuk DIHINDARI |

## Status
Semua acuan wajib per tipe reference pack (Karakter: acuan+sheet; Latar: 3 sudut; Props: acuan; Palet/Gaya: palet+style+negatif) ADA dan BERSIH audit → keempat elemen `Reference-Ready`. Total regenerasi karena temuan audit: 3 file (props v1, jalan-senja v1, style-sheet v1).
