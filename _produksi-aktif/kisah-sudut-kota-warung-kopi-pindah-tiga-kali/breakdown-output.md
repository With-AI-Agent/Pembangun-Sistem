# Tahap 4 — Breakdown Output

**Channel:** Kisah Sudut Kota · **Model:** Kartu Teks 8–10 v1 · **Unit breakdown:** **kartu teks**
**Naskah sumber:** `naskah-draft.md` (**FINAL** — G1 Tahap 3 + G2 naskah final disetujui 2026-09-15)
**Gerbang:** menunggu **G1 Tahap 4** dan **G2 breakdown**

> **Kenapa kolom "prompt generate" dan "referensi visual" dikosongkan, bukan diisi:**
> `05_CONTENT_PRODUCTION_PIPELINE.md` Tahap 4 mensyaratkan untuk konten tanpa asset visual: *"lewati poin 3 dan 4, tulis 'tidak berlaku — konten [teks-only]', dan sebagai gantinya cantumkan arahan penyampaian per unit."* Model brief `kartu-teks-8-10` bagian 4 menegaskan kolom itu **dikosongkan dengan keterangan eksplisit — bukan diisi asal supaya formatnya penuh**. Karena itu setiap baris di bawah memuat keterangan eksplisit, bukan sel kosong dan bukan prompt karangan.

## Spesifikasi layout (berlaku untuk semua kartu)

| Aspek | Spesifikasi | Sumber |
|---|---|---|
| Latar | Warna solid `abu aspal` (kartu 1–8) dan `biru pudar` (kartu 9 sebagai penanda penutup) | Brief model bagian 3; palet Channel Brief bagian 5 |
| Teks | Satu warna kontras, satu jenis huruf, satu ukuran per tingkatan | Brief model bagian 3 |
| Aksen | **Maksimal satu** frasa per kartu, warna `kuning pagi` (kartu 1–5, 7–9) / `oranye lampu sodium` (kartu 6) | Brief model bagian 3 |
| Nomor kartu | Format `n/9`, posisi konsisten | Brief model bagian 3 |
| Dilarang | Foto, ilustrasi, ikon, logo merek, gradien, tekstur, wajah yang bisa dikenali | Brief model bagian 3 |
| Asset gambar | **TIDAK ADA — 0 berkas** | Brief model bagian 4 (Tahap 5 tidak berlaku) |

## Rincian per kartu

| # | Bagian naskah | Prompt generate | Referensi visual | Arahan penyampaian (frasa beraksen + penekanan) |
|---|---|---|---|---|
| 1/9 | *"Di sudut jalan itu, ada warung kopi yang sudah tiga kali pindah."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"tiga kali pindah"**. Baca datar, tanpa penekanan dramatis di awal — biarkan angkanya yang bekerja. |
| 2/9 | *"Namanya tidak pernah ganti… tanpa pernah diumumkan kepada siapa pun."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"Namanya tidak pernah ganti"**. Penekanan pada kata "sama" yang diulang — ritme sengaja, jangan dipercepat. |
| 3/9 | *"Pindahan pertama cuma menyeberang jalan… dari tempat yang sama."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"cuma menyeberang jalan"**. Kata "cuma" harus terasa ringan — ini perpindahan paling kecil. |
| 4/9 | *"Pindahan kedua masuk ke dalam gang… yang sudah hafal jalannya."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"masuk ke dalam gang"**. Jeda lebih panjang sebelum "Sewanya naik" — penyebabnya tidak perlu ditegaskan. |
| 5/9 | *"Pindahan ketiga balik lagi ke sudut semula… seolah tidak pernah terjadi apa-apa."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"balik lagi ke sudut semula"**. Kalimat terakhir dibaca nyaris datar; "seolah tidak pernah terjadi apa-apa" adalah puncak sunyi thread ini. |
| 6/9 | *"Yang tidak ikut pindah hanya tiga hal… tanpa menunggu jawaban."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"hanya tiga hal"** (aksen `oranye lampu sodium` — satu-satunya kartu yang memakainya). Tiga sebutan berikutnya dibaca berirama sama, seperti daftar yang dihafal. |
| 7/9 | *"Pelanggannya ikut berpindah-pindah… tanpa merasa asing."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"muncul lagi di tempat baru"**. Penekanan tipis pada "tanpa merasa asing" — penutup kartu ini yang menyiapkan kartu 8. |
| 8/9 | *"Yang berubah sebenarnya bukan warung itu… yang lewat di depannya."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"bukan warung itu"**. Ini kartu pivotal: baca lebih lambat dari kartu lain. Tanpa nada menghakimi — pengamatan, bukan penilaian. |
| 9/9 | *"Sudut seperti ini ada di dekat rumahmu juga… lihat pelan-pelan."* | **tidak berlaku — konten teks-only** | **tidak berlaku — konten teks-only** | Aksen: **"lihat pelan-pelan"**. Latar berganti ke `biru pudar` sebagai penanda penutup. Kalimat terakhir dibiarkan pendek, tanpa tambahan. |

## Rekapitulasi

Angka di bawah **keluaran `cek-kartu.py`** (fungsi `cek_breakdown`), bukan dihitung tangan:

```
CEK BREAKDOWN — unit kartu teks
  jumlah unit (baris n/9) : 9
  keterangan eksplisit 'tidak berlaku — konten teks-only' : 18 (harus 2 x unit = 18)
  arahan 'Aksen:'          : 9 (harus tepat 1 per unit = 9)
  kolom prompt/referensi    : semua 9 baris berketerangan eksplisit
HASIL: PASS
EXIT=0
```

| Klaim | Nilai | Batas | Status |
|---|---|---|---|
| Jumlah unit | 9 | 8–10 | ✅ |
| Asset yang harus digenerate/diakuisisi | 0 | 0 | ✅ |
| Kolom prompt generate terisi prompt karangan | 0 dari 9 | 0 | ✅ |
| Kolom referensi visual terisi | 0 dari 9 | 0 | ✅ |
| Frasa beraksen | 9 (tepat 1 per kartu) | maks 1 per kartu | ✅ |

**Mutation test (membuktikan pemeriksa bergigi):** kolom prompt generate baris `3/9` diisi prompt karangan (`b-roll sudut jalan pagi, cahaya lembut, 9:16`) **dan** kartu 5 diberi dua arahan aksen, lalu skrip dijalankan ulang —
```
EXIT (termutasi) = 1
  keterangan eksplisit 'tidak berlaku — konten teks-only' : 17 (harus 2 x unit = 18)
  arahan 'Aksen:'          : 10 (harus tepat 1 per unit = 9)
  kolom prompt/referensi    : ADA YANG TERISI / TIDAK LENGKAP
  - keterangan 'tidak berlaku' = 17, seharusnya 18 (2 per kartu)
  - jumlah 'Aksen:' = 10, seharusnya 9 (satu per kartu)
  - baris '3/9' kolom prompt generate tidak kosong-berketerangan: 'b-roll sudut jalan pagi, cahaya lembut, 9:16'
HASIL: FAIL
```
Kedua pelanggaran tertangkap **independen**. Berkas dipulihkan → `EXIT=0`, `HASIL: PASS`, `diff` terhadap salinan cadangan **IDENTIK**.

## Tahap berikutnya

**Tahap 5 (Generate/Acquire Assets) — TIDAK BERLAKU.** Model brief bagian 4 menetapkan Tahap 5 dilewati dan dicatat di `STATUS.md` sebagai `Tahap 5 — tidak berlaku (konten teks-only)`. Tidak ada satu pun berkas yang digenerate. Langsung ke Tahap 6 (Assembly & Publish Prep).
