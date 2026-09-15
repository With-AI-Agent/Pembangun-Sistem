# Catatan Asset — Sumur di Belakang Rumah (Tahap 5)

**Model konten:** Narasi 60 Detik **v2** — unit = segmen narasi (S1–S7), semua aset **vertikal 9:16 (768×1376)**.
**Tanggal generate & inspeksi:** 2026-09-15. Semua aset digenerate sebagai still frame netral (bukan stok berhak cipta).

**Kriteria inspeksi (dari `breakdown-output.md` bagian "Catatan untuk Tahap 5"):** (1) dimensi vertikal 9:16; (2) tidak ada huruf/angka/kata yang terbaca; (3) tidak ada wajah yang bisa dikenali; (4) tidak ada logo merek. Hasil di bawah diverifikasi dengan membuka tiap gambar satu per satu.

| File | Dimensi | sha256 | Inspeksi |
|---|---|---|---|
| S1-mulut-sumur.png | 768×1376 | `297ff89bb6f796cb356125c818de0f043bb1cc17a64f1b10ffde9f1839b0f7b3` | BERSIH — mulut sumur batu + katrol kayu + ember kayu; tanpa teks, tanpa wajah, tanpa logo |
| S2-ember-tali.png | 768×1376 | `fac83ac591b918168ff4120d8d5adc3e2901293ff57042aa59e81ce8057f16f9` | BERSIH — ember seng tergantung tali mengilap; tanpa teks, tanpa wajah, tanpa logo |
| S3-ember-berjejer.png | 768×1376 | `f1531acb0b7ac63fad508547ce3a4e23111bef7641b56badd459de4be3e7bef1` | BERSIH — ember berjejer menunggu giliran; ember polos tanpa marka; tanpa wajah, tanpa logo |
| S4-sandal-bayangan.png | 768×1376 | `808a3ef563aa21dae6e5c30ae2c3ad387e14fc35b4ba5351ba24ed671d858c31` | BERSIH — dua pasang sandal + bayangan samar orang di dinding bata; bayangan hanya siluet, **wajah tidak terlihat**; tanpa teks, tanpa logo |
| S5-ember-penuh.png | 768×1376 | `bf2ac328d9105da577ef6ab4dfac08f07f795c7d6cc04e98acf1c49781b8650c` | BERSIH — ember penuh, permukaan air beriak; air hanya menampilkan riak + pantulan langit, **tidak ada pantulan wajah**; tanpa teks, tanpa logo |
| S6-keran-dapur.png | 768×1376 | `a1c028cbec31d1a76fd3acbe5e6963121d99ad950eb76ac0f54dc3eaa8684f85` | BERSIH — keran logam mengisi ember; ada objek kecil buram di sudut atas-kanan (rak + kotak) tetapi **terlalu kecil/buram untuk dibaca** — bukan teks terbaca; tanpa wajah, tanpa logo |
| S7-sumur-ditutup.png | 768×1376 | `7426759be9a384ba192b417d2ddc2ef93425a4921fa03b30f18e8d95c483f23e` | BERSIH — sumur ditutup pelat beton + jemuran + pot; kain batik berpola tapi **tanpa teks**; ada pelat kecil buram di atas pintu yang tidak terbaca; tanpa wajah, tanpa logo |

**Accepted limitation:** tidak ada yang wajib dicatat — semua glyph/objek kecil yang muncul tidak membentuk huruf/angka/kata yang terbaca. (S6 & S7: objek kecil buram dicatat di atas sebagai "tidak terbaca", bukan sebagai limitation.)

**Tidak ada elemen Bank Konsistensi Visual** yang harus dijaga kemiripannya antar segmen (channel faceless), jadi tidak ada yang perlu diregenerasi demi konsistensi karakter.
