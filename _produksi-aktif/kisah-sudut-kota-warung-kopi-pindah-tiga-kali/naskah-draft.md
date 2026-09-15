# Tahap 3 — Naskah (r1)

**Channel:** Kisah Sudut Kota · **Model:** Kartu Teks 8–10 v1 · **Judul kerja:** *Warung Kopi yang Pindah Tiga Kali*
**Kerangka:** `konsep-angle.md` (G1 Tahap 2 disetujui 2026-09-15)
**Batas model:** 8–10 kartu · 18–28 kata/kartu · kartu 1 ≤ 15 kata · total ±160–250 kata
**Gerbang:** menunggu **G1 Tahap 3** (lanjut ke breakdown) dan **G2 naskah final** (mengunci untuk diarsipkan)

---

## Kartu 1 — Hook

> Di sudut jalan itu, ada warung kopi yang sudah tiga kali pindah.

## Kartu 2 — Kebiasaan yang menempel

> Namanya tidak pernah ganti. Papan yang sama, cat yang sama. Hanya alamatnya yang bergeser pelan-pelan, tanpa pernah diumumkan kepada siapa pun.

## Kartu 3 — Pindah pertama

> Pindahan pertama cuma menyeberang jalan. Gedung lamanya direnovasi, dan warung itu digeser ke sisi yang satunya, tetap terlihat dari tempat yang sama.

## Kartu 4 — Pindah kedua

> Pindahan kedua masuk ke dalam gang. Sewanya naik, dan tidak ada yang perlu dijelaskan kepada pelanggan yang sudah hafal jalannya.

## Kartu 5 — Pindah ketiga

> Pindahan ketiga balik lagi ke sudut semula. Berdiri di sebelah toko yang dulu tidak mau menerimanya, seolah tidak pernah terjadi apa-apa.

## Kartu 6 — Yang tidak ikut pindah

> Yang tidak ikut pindah hanya tiga hal: jam bukanya, gelasnya yang tebal, dan kebiasaan pemiliknya menyapa tanpa menunggu jawaban.

## Kartu 7 — Yang mengikuti

> Pelanggannya ikut berpindah-pindah. Ada yang hilang satu musim, lalu muncul lagi di tempat baru, duduk di kursi yang berbeda tanpa merasa asing.

## Kartu 8 — Yang berubah

> Yang berubah sebenarnya bukan warung itu. Kota di sekitarnya berganti jauh lebih cepat: tokonya, namanya, dan orang-orang yang lewat di depannya.

## Kartu 9 — Penutup

> Sudut seperti ini ada di dekat rumahmu juga. Biasanya tanpa nama, biasanya tidak diperhatikan. Lain kali kamu lewat situ, lihat pelan-pelan.

---

## Verifikasi batas model

Angka di bawah **keluaran skrip** `cek-kartu.py` di folder ini — bukan dihitung tangan. Jalankan ulang kapan saja: `python3 _produksi-aktif/kisah-sudut-kota-warung-kopi-pindah-tiga-kali/cek-kartu.py`

```
CEK NASKAH — model Kartu Teks 8-10
  berkas           : _produksi-aktif/kisah-sudut-kota-warung-kopi-pindah-tiga-kali/naskah-draft.md
  jumlah kartu     : 9 (batas 8-10)
  kartu 1 (Hook) : 12 kata  [<= 15 (hook)]  OK
  kartu 2 (Kebiasaan yang menempel) : 21 kata  [18-28]  OK
  kartu 3 (Pindah pertama) : 22 kata  [18-28]  OK
  kartu 4 (Pindah kedua) : 20 kata  [18-28]  OK
  kartu 5 (Pindah ketiga) : 21 kata  [18-28]  OK
  kartu 6 (Yang tidak ikut pindah) : 19 kata  [18-28]  OK
  kartu 7 (Yang mengikuti) : 22 kata  [18-28]  OK
  kartu 8 (Yang berubah) : 21 kata  [18-28]  OK
  kartu 9 (Penutup) : 21 kata  [18-28]  OK
  total kata       : 179 (batas 160-250)  OK
  waktu baca       : ~72 detik pada 150 kata/menit
HASIL: PASS
EXIT=0
```

**Mutation test (membuktikan skrip bergigi, bukan sekadar mencetak OK):** kartu 1 digembungkan jadi 20 kata dan kartu 4 jadi 31 kata, lalu skrip dijalankan ulang —
```
EXIT (termutasi) = 1
  kartu 1 (Hook) : 20 kata  [<= 15 (hook)]  MELESET
  kartu 4 (Pindah kedua) : 31 kata  [18-28]  MELESET
  total kata       : 198 (batas 160-250)  OK
HASIL: FAIL
  - kartu 1 = 20 kata, melebihi 15
  - kartu 4 = 31 kata, di luar 18-28
```
Kedua pelanggaran tertangkap **secara independen** (total masih 198 dan tetap OK, jadi kegagalan bukan efek samping dari total). Berkas dipulihkan → `EXIT=0`, `HASIL: PASS`, `diff` terhadap salinan cadangan **IDENTIK**.

## Catatan kepatuhan

| Batasan Channel Brief | Status |
|---|---|
| Satu sudut kota konkret sebagai pintu masuk | ✅ Kartu 1 — sudut jalan + warung kopi |
| Penutup mengajak melihat sudut terdekatnya sendiri | ✅ Kartu 9 — "ada di dekat rumahmu juga… lihat pelan-pelan" |
| Kalimat pendek, tanpa basa-basi | ✅ Semua kalimat ≤ 12 kata; tidak ada pembuka basa-basi |
| Kosakata khas channel terpakai | ✅ "sudut" (k1, k5, k9), "menempel"/"ikut pindah" (k2, k6, k7), "yang lewat" (k8), "tanpa nama" (k9), "kota yang sama"→"tempat yang sama" (k3) |
| Tanpa klaim faktual yang tidak bisa dirujuk | ✅ Tidak ada angka statistik, tanggal, maupun nama resmi. "Tiga kali" dan "tiga hal" = premis naratif warung fiktif tanpa nama (lihat `ideation.md`) |
| Tanpa nama tokoh nyata | ✅ Pemilik tidak pernah diberi nama |
| Tanpa nada menggurui | ✅ Tidak ada kalimat simpulan atau pesan moral; kartu 8 menyatakan pengamatan, bukan pelajaran |
| Tanpa clickbait | ✅ Kartu 1 tidak menjanjikan apa pun yang tidak muncul di kartu 2–9 |
| Sudut yang bercerita, orangnya menempel | ✅ Pemilik hanya muncul di kartu 6 sebagai kebiasaan |
| Tanpa gambar / video / audio | ✅ Tidak ada satu pun arahan visual; lihat Tahap 4 (kolom prompt generate dikosongkan berketerangan) |

## Sumber eksternal

**Tidak ada.** `SUMBER.md` tidak dibuat karena tidak ada satu pun klaim yang bersumber dari luar. Gerbang fact-check Tahap 3 karena itu **tidak terpicu** — tidak ada klaim berstatus `Belum` atau `Tidak bisa diverifikasi`.

## Karakter Tipe B

**Tidak ada.** Pemilik warung tidak digambarkan secara fisik dan tidak diberi nama, jadi tidak memenuhi syarat sebagai karakter Tipe B yang perlu dicatat di `indeks-karakter.md`. Pemeriksaan ke `arsip-naskah/indeks-karakter.md` (1 entri: Nenek Penjual Jagung Rebus) sudah dilakukan — tidak ada kecocokan dan tidak ada karakter baru.
