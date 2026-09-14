# Arsip Reproducibility Metadata — Cap Pos di Amplop

- **Tanggal produksi:** 2026-09-14
- **Model konten:** Narasi Riset 60 Detik v1 (Alur Kerja Kustom — pasca PR #52)
- **Versi brief:** Channel Brief v2; Model Konten Brief Narasi Riset 60 Detik v1; Model Konten Brief Narasi 60 Detik v1
- **Status:** G2 Tahap 6 disetujui 2026-09-14; judul tayang resmi dikunci opsi 1 ("Lingkaran tinta di sudut amplop"); G3 merge belum
- **Judul tayang resmi:** Lingkaran tinta di sudut amplop (metadata opsi 1, dipilih)

## Prompt final asset

Aset digenerate sebagai still frame b-roll non-karakter, sesuai gaya Channel Brief (cokelat/krem/hijau tua pudar, film grain, wajah/logo/teks tidak ada). Tidak ada Prompt Master karakter atau file Bank Konsistensi Visual (channel faceless). Segmen 7 menggunakan `segmen-01-cap-pintu-masuk.png` sebagai reference image internal untuk kontinuitas meja kayu.

Catatan accepted limitation: segmen 01 dan 03 memuat pseudo-glyph buram pada cap yang tidak dapat dibaca sebagai kata apapun (blob/smudge tinta); ini adalah batas kemampuan model gambar yang dapat dicapai setelah 3x retry dan tidak mengganggu narasi.

1. **Segmen 1 — `assets/segmen-01-cap-pintu-masuk.png`**
   sha256: `309367c5b175854fe42e8181a9cacd67b7ae2c59ff49fe4d6601a653943ef150`
   Close-up lingkaran tinta/smudge cap mengenai prangko polos di sudut amplop krem di meja kayu usang; cahaya sore lembut; palet cokelat/krem; film grain; tidak ada teks/logo/wajah yang bisa dibaca.

2. **Segmen 2 — `assets/segmen-02-cap-kota-asal.png`**
   sha256: `c81e4ee1a1dab325954b12c9e1e494b6e2a68c476e09fb2d390773fbd033e1e4`
   Close-up stempel kayu ditekan di amplop krim polos; hanya ujung lengan baju sebagai penekan (tidak ada wajah/ciri); amplop tidak memuat alamat/logo; cap di karet stempel tidak terbaca; meja kayu gelap; cahaya natural; palet arsip.

3. **Segmen 3 — `assets/segmen-03-cap-kota-tujuan.png`**
   sha256: `c96f86094d9184c4bdd97fb065ea9b1d99a7fadcb0b9e97f980147705806bfe6`
   Balik amplop terselip di celah kotak surat kayu gelap; cap bulat buram di flap belakang; cahaya pagi lembut; palet cokelat/krem; tidak ada alamat terbaca.

4. **Segmen 4 — `assets/segmen-04-dua-waktu.png`**
   sha256: `0329f3190348c18377d90fccfd47fccdcb8634f39865aa7c6b4a8136162d1391`
   Overhead amplop krim di permukaan kayu dengan dua cap bulat bertumpuk lembut; cahaya redup; tidak ada split screen; tidak ada teks terbaca.

5. **Segmen 5 — `assets/segmen-05-rumah-menanti.png`**
   sha256: `a9df8e6c274283162b44f6adf3d891f7921f5d980effc0221140aadad4ec933f`
   Kotak surat kayu di dinding rumah dengan satu amplop terselip; tanaman hijau tua di dekatnya; pagi; tidak ada nomor/alamat; palet cokelat-krem-hijau tua pudar.

6. **Segmen 6 — `assets/segmen-06-ponsel.png`**
   sha256: `5226fc15b2df576b9d683eedc1ad690ffa218a83bca3272187087a3a4e409c48`
   Ponsel slab hitam polos generik (tanpa notch/logo/ikon) dan amplop cokelat tertutup di atas meja kayu yang sama; layar kosong; cahaya lebih modern; tidak ada teks/logo.

7. **Segmen 7 — `assets/segmen-07-meja-kosong-penutup.png`**
   sha256: `64c19737048a6559ee22fa48b69fedd7a546a2d985517bf97a68b50d6951e65e`
   Sudut meja kayu kosong (kontinuitas dengan segmen 1) dengan noda/cincin samar bekas benda; tidak ada amplop, tidak ada ponsel, tidak ada objek; cahaya pagi netral hangat.

## Daftar asset

- `assets/segmen-01-cap-pintu-masuk.png`
- `assets/segmen-02-cap-kota-asal.png`
- `assets/segmen-03-cap-kota-tujuan.png`
- `assets/segmen-04-dua-waktu.png`
- `assets/segmen-05-rumah-menanti.png`
- `assets/segmen-06-ponsel.png`
- `assets/segmen-07-meja-kosong-penutup.png`

Asset tetap berada di folder produksi aktif sampai G3 merge dan pengguna mengunduh hasilnya. Setelah itu folder `_produksi-aktif/narasi-sejarah-cap-pos/` dihapus sesuai aturan Tahap 6.

- **Elemen konsistensi:** tidak ada elemen Bank Konsistensi Visual; reference image segmen 01 dipakai hanya untuk kontinuitas internal konten (meja kayu di segmen 7).
- **Karakter Tipe B:** tidak ada.
- **Sumber eksternal:** rujuk `2026-09-14-cap-pos-di-amplop-sumber.md`.
- **Catatan produksi:**
  - Micro-revisi naskah r0→r1 atas koreksi akurasi cap tanggal pengiriman; penambahan 2 kata kecil ("dikirim" dan "di antara") untuk menjaga jumlah kata tetap 130.
  - Aset segmen 01 dan 03 memiliki accepted limitation (pseudo-glyph pada cap yang tidak terbaca sebagai kata) setelah 3x retry untuk segmen 01.
  - Estimasi durasi 62,9 detik — belum diukur dari TTS/rakaman; bila pembacaan nyata melewati 65 detik, revisi teks (bukan mempercepat suara).
  - Tidak ada atribusi wajib di caption (fakta sejarah umum dan bahasa pengalaman diturunkan, bukan kutipan langsung).
