# Arsip Reproducibility Metadata — Cap Pos di Amplop

- **Tanggal produksi:** 2026-09-14 (konten); koreksi aset/metadata/statistik 2026-09-15 pasca review putaran 1
- **Model konten:** Narasi Riset 60 Detik v1 (Alur Kerja Kustom — pasca PR #52)
- **Versi brief:** Channel Brief v3; Model Konten Brief Narasi Riset 60 Detik v1; Model Konten Brief Narasi 60 Detik v1
- **Status:** G2 final disetujui 2026-09-14; koreksi putaran-1 review selesai 2026-09-15; G3 merge menunggu
- **Judul tayang resmi:** Lingkaran tinta di sudut amplop (metadata opsi 1, dipilih)

## Prompt final asset

Aset digenerate sebagai still frame b-roll non-karakter, vertikal 9:16 portrait (semua 7 file 768×1376 px, diverifikasi `identify`), sesuai gaya Channel Brief (cokelat/krem/hijau tua pudar, film grain, wajah/logo/teks tidak ada). Tidak ada Prompt Master karakter atau file Bank Konsistensi Visual (channel faceless).

**Catatan accepted limitation (revisi 2026-09-15 pasca review putaran 1):**
- Segmen 01 (regenerasi): bingkai lingkaran tinta hitam mengenai separuh prangko di sudut amplop krem; blob tinta di dalam lingkaran berupa gumpalan tinta TIDAK BERATURAN tanpa satupun fragmen yang membentuk huruf/angka/kata. Dipastikan dengan inspeksi visual pada hasil retry-2; tidak ada accepted limitation yang tersisa untuk segmen 01.
- Segmen 02 (regenerasi, 2x retry): permukaan karet stempel adalah piringan karet hitam POLOS TANPA UKIRAN (tidak ada huruf, angka, kota, tanggal, atau glyph apapun); bekas tinta di kertas adalah blob tinta basah tidak beraturan tanpa bentuk huruf. Diverifikasi inspeksi visual retry-2: **tidak ada word/huruf/angka terbaca** → accepted limitation dihapus.
- Segmen 03 (tidak diregenerasi): lingkaran cap buram di balik amplop masih memuat blob yang samar; setelah inspeksi ulang, blob tersebut tidak membentuk huruf/angka/kata yang terbaca (samar seperti lipatan kertas + noda tinta) — **bukan accepted limitation**, hanya efek kedalaman pudar.
- Segmen 06 (regenerasi, 2x retry): ponsel slab hitam polos generik, layar kosong hitam total, tanpa notch/camera cutout/home button/logo. Tepi ponsel terlihat tipis sebagai bezel hitam (tidak dapat dihindari pada benda rectangular); tidak ada tombol/ikon/teks di permukaan depan. Amplop cokelat tertutup rapi di samping.

Semua dimensi sudah diverifikasi `identify`: 7 file × 768×1376 px (h/w ≈ 1,79 ≈ 9:16).

1. **Segmen 1 — `assets/segmen-01-cap-pintu-masuk.png`** (regenerasi 2026-09-15)
   sha256: `ddefca8d5af11ac461ddf3767978fa56d8ad8c610b80114c5fa9229107316703`
   Prompt final: "A vertical 9:16 portrait still-frame b-roll photograph, documentary-style, vertical composition tall and narrow for phone screen. Close-up detail of the corner of an old cream-yellowed paper envelope resting on a worn dark wooden table. A black ink circular postmark smudge touches half of a blank generic stamp (no design, no face value numbers, no country name). Soft late afternoon side light, warm sepia palette (browns/creams/muted tones), subtle film grain. Absolutely NO readable text, NO letters, NO numbers, NO words, NO logos, NO faces, NO addresses anywhere in frame — the ink mark is an abstract blobby ink circle without any letter shapes, just uneven smudged ink texture. Quiet nostalgic mood."

2. **Segmen 2 — `assets/segmen-02-cap-kota-asal.png`** (regenerasi 2026-09-15, 2x retry; hasil akhir = retry-2)
   sha256: `9f2e3e33f70c41008c09f7d053c72bd6ef338b061f1c67456ef506d99dfd3ee8`
   Prompt final (retry-2): "A vertical 9:16 portrait still-frame b-roll photograph, documentary-style, tall narrow phone aspect ratio. Top-down close-up on a dark wood desk. A circular rubber postmark stamp with a wooden handle is being pressed onto a cream paper envelope. The flat circular RUBBER STAMPING SURFACE of the stamp is ENTIRELY SMOOTH AND BLANK — completely free of any carving, no letters, no numbers, no words, no symbols, no glyphs, no date dial, no city name. It is a smooth clean matte black rubber disc. As it presses down, it leaves a round irregular ink smudge (wet black ink bleeding unevenly) — the ink mark is a messy blob with soft edges, NOT containing any readable letter shapes. Only the thumb and cuff of a plain dark shirt of the hand pressing the stamp is visible at the top edge — NO faces, NO identifying features. Soft window light from the side, warm sepia/brown archival palette, subtle film grain. STRICTLY NO TEXT, NO LETTERS, NO NUMBERS, NO WORDS, NO ADDRESSES, NO LOGOS ANYWHERE IN THE ENTIRE IMAGE."
   Hasil inspeksi visual: piringan karet hitam polos sempurna; bekas tinta di amplop adalah blob tinta hitam tidak beraturan tanpa fragmen huruf/angka/kata.

3. **Segmen 3 — `assets/segmen-03-cap-kota-tujuan.png`** (tidak diregenerasi; 768×1376 portrait)
   sha256: `c96f86094d9184c4bdd97fb065ea9b1d99a7fadcb0b9e97f980147705806bfe6`
   Close-up balik amplop terselip di celah kotak surat kayu gelap; cap bulat buram di flap belakang; cahaya pagi lembut; palet cokelat/krem; tidak ada alamat terbaca.

4. **Segmen 4 — `assets/segmen-04-dua-waktu.png`** (tidak diregenerasi; 768×1376 portrait)
   sha256: `0329f3190348c18377d90fccfd47fccdcb8634f39865aa7c6b4a8136162d1391`
   Overhead amplop krim di permukaan kayu dengan dua cap bulat bertumpuk lembut; cahaya redup; tidak ada split screen; tidak ada teks terbaca.

5. **Segmen 5 — `assets/segmen-05-rumah-menanti.png`** (tidak diregenerasi; 768×1376 portrait)
   sha256: `a9df8e6c274283162b44f6adf3d891f7921f5d980effc0221140aadad4ec933f`
   Kotak surat kayu di dinding rumah dengan satu amplop terselip; tanaman hijau tua di dekatnya; pagi; tidak ada nomor/alamat; palet cokelat-krem-hijau tua pudar.

6. **Segmen 6 — `assets/segmen-06-ponsel.png`** (regenerasi 2026-09-15, 2x retry; hasil akhir = retry-2)
   sha256: `b1e2704923e5a862f7f8342388444409e540544d9827ded0d1a18ce444627f31`
   Prompt final (retry-2): "A vertical 9:16 portrait still-frame b-roll photograph, documentary-style, tall narrow phone aspect ratio. Top-down flat-lay on a worn dark wooden table. On the table lies a single smooth matte-black rectangular slab representing a generic smartphone — but the FRONT FACE is one perfectly smooth continuous sheet of flat black glass with ABSOLUTELY NO FEATURES: no speaker slit, no earpiece grille, no camera cutout, no notch, no punch hole, no home button, no buttons visible from above, no logo, no brand markings. It is a seamless plain black rectangle, like a polished black stone slab. Beside it, a plain closed brown kraft envelope lies flat, completely blank with no address, no stamp, no windows. Soft warm modern neutral daylight, subtle film grain, brown-cream palette that matches the vintage envelope series. STRICTLY NO TEXT, NO LETTERS, NO NUMBERS, NO WORDS, NO ADDRESSES, NO LOGOS ANYWHERE IN THE ENTIRE IMAGE."
   Hasil inspeksi visual: bingkai depan hitam polos tanpa notch/camera cutout; hanya bezel tepi tipis yang terlihat (tidak dapat dihindari untuk bentuk rectangular); tidak ada ikon/logo/teks. Amplop cokelat tertutup rapi di samping.

7. **Segmen 7 — `assets/segmen-07-meja-kosong-penutup.png`** (tidak diregenerasi; 768×1376 portrait)
   sha256: `64c19737048a6559ee22fa48b69fedd7a546a2d985517bf97a68b50d6951e65e`
   Sudut meja kayu kosong (kontinuitas dengan segmen 1) dengan noda/cincin samar bekas benda; tidak ada amplop, tidak ada ponsel, tidak ada objek; cahaya pagi netral hangat.

## Daftar asset

- `assets/segmen-01-cap-pintu-masuk.png` — ddefca8d… (regenerated 2026-09-15)
- `assets/segmen-02-cap-kota-asal.png` — 9f2e3e33… (regenerated 2026-09-15, retry-2)
- `assets/segmen-03-cap-kota-tujuan.png` — c96f8609…
- `assets/segmen-04-dua-waktu.png` — 0329f319…
- `assets/segmen-05-rumah-menanti.png` — a9df8e6c…
- `assets/segmen-06-ponsel.png` — b1e27049… (regenerated 2026-09-15, retry-2)
- `assets/segmen-07-meja-kosong-penutup.png` — 64c19737…

Semua aset tetap berada di folder produksi aktif sampai G3 merge dan pengguna mengunduh hasilnya. Setelah itu folder `_produksi-aktif/narasi-sejarah-cap-pos/` dihapus sesuai aturan Tahap 6.

- **Elemen konsistensi:** tidak ada elemen Bank Konsistensi Visual.
- **Karakter Tipe B:** tidak ada.
- **Sumber eksternal:** rujuk `2026-09-14-cap-pos-di-amplop-sumber.md`.
- **Catatan produksi:**
  - Micro-revisi naskah r0→r1 atas koreksi akurasi cap tanggal pengiriman; penambahan 2 kata kecil ("dikirim" dan "di antara") untuk menjaga jumlah kata tetap 130.
  - Koreksi review putaran 1 (2026-09-15): regenerasi segmen 01, 02, 06 menjadi vertikal 9:16 (768×1376); segmen 02 diretry 2x dengan prompt anti-teks agresif sampai karet stempel benar-benar polos dan tinta tidak membentuk huruf; tabel hitungan kata per paragraf di naskah-draft dan arsip diperbaiki (14/45/21/19/31 = 130); klaim F6 di peta-fakta dikoreksi menjadi 3 penerbit independen (bukan 4+eprints).
  - Estimasi durasi 62,9 detik — belum diukur dari TTS/rakaman; bila pembacaan nyata melewati 65 detik, revisi teks (bukan mempercepat suara).
  - Tidak ada atribusi wajib di caption (fakta sejarah umum dan bahasa pengalaman diturunkan, bukan kutipan langsung).
