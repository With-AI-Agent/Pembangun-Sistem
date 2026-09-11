# Bank Konsistensi Visual — Palet & Gaya Catok

### Dibangun via `04_CHARACTER_BUILDER_KIT.md` — 2026-09-11_3. Elemen milik channel `channel-kantor-pos-miso`. Ini "kunci keluarga visual" yang membuat 100 episode terasa satu rumah.

**Status:** `Reference-Ready` — G2 `setuju_g2` 2026-09-11; seluruh acuan wajib ADA di `referensi/` dan lolos audit visual (lihat `../CATATAN-ASSET.md`) `referensi/palet.png` + `referensi/style-sheet.png` + `referensi/contoh-negatif-3d-render.png` ada.

## Jenis Elemen

Palet Warna & Gaya Render — WAJIB dirujuk di SETIAP generate unit, termasuk unit yang hanya menampilkan objek tanpa Miso.

## Deskripsi (Prompt-Ready)

Gaya ilustrasi buku cerita (picture-book) era keemasan, dieksekusi dengan wash cat air transparan + gouache buram tipis di area fokus, garis pensil grafit yang halus dan tidak selalu tertutup, grain kertas matte terlihat, dan warna yang sedikit luntur/bleeding di tepi objek. Tidak ada outline hitam tebal, tidak ada gradasi digital halus, tidak ada kilau/cat 3D. Semua objek terasa digambar tangan di atas kertas — termasuk tekstur bulu Miso (gosokan pensil pendek, bukan helai rapi).

## Palet Warna — kode hex

| Peran | Nama | Hex |
|---|---|---|
| dasar kertas / langit siang | krem kertas | `#EFE3CE` |
| dinding & lantai terakota | terakota bata | `#C9764F` |
| pintu, etalase, seragam tua | hijau botol | `#3B5C4F` |
| lampu, jam, gesper, cap kuningan | kuning kuningan | `#C79A3B` |
| tas pos Miso | merah bata (aksen, maks ±10% frame) | `#B04A3A` |
| bulu dasar Miso / lantai kayu | krem kayu | `#DDBE93` |
| loreng Miso / roti & jahe | oranye pudar | `#CB8B58` |
| langit senja | kelabu hangat | `#A99E93` |
| malam setelah hujan / bayangan | biru tinta | `#4C5D70` |
| garis pensil | grafit hangat | `#574B42` |

Aturan palet: salah satu warna "dominan" (kertas/terakota/hijau botol) harus mengisi ≥50% frame; merah bata hanya aksen; saturasi maksimum "pudar-hangat"; tidak ada neon, tidak ada hitam murni (gunakan `#574B42`), tidak ada putih murni (gunakan `#EFE3CE`).

## Gaya Render — kata kunci prompt yang terbukti

`picture-book watercolor and gouache illustration, soft graphite pencil outlines, matte paper grain, colors slightly bleeding at edges, muted warm palette, diffused golden light, hand-drawn storybook texture, no thick black outlines, no 3D render, no neon`

## Referensi pembanding (acuan gaya, bukan untuk ditiru)

Estetika buku cerita bergambar klasik era 1950-70an & ilustrasi dongeng Eropa-timur: hangat, tenang, sedikit melankolis-tapi-lembut. Bukan gaya anime, bukan ilustrasi vektor datar, bukan concept-art digital halus.

## Contoh Negatif — gaya yang HARUS DIHINDARI

`referensi/contoh-negatif-3d-render.png` = contoh yang salah: render 3D fotorealistik dengan cahaya studio halus. Kalau hasil generate terlihat seperti itu → regenerate, jangan dipakai.

## Prompt Master (Reusable)

> Tempel di AKHIR setiap prompt unit (setelah Prompt Master karakter/latar), supaya gaya konsisten di semua jenis unit.

```
picture-book watercolor and gouache illustration, soft graphite pencil
outlines, matte paper grain, colors slightly bleeding at edges, muted warm
storybook palette (paper cream #EFE3CE, terracotta #C9764F, bottle green
#3B5C4F, brass gold #C79A3B, brick red #B04A3A as accent, faded orange
#CB8B58, warm gray #A99E93, ink blue shadow #4C5D70), diffused golden
light, quiet tender storybook mood, no thick black outlines, no 3D render,
no neon, no glossy highlight, no pure black, no pure white
```

## Log Keputusan Elemen

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-11 | Reference pack tipe palet/gaya = palet.png + style-sheet.png + 1 contoh negatif | Sesuai tabel tipe elemen di `04_CHARACTER_BUILDER_KIT.md` |
| 2026-09-11 | Merah bata dibatasi ±10% frame; hitam & putih murni dilarang | Ciri khas harus tetap jadi aksen; "kertas" adalah identitas — putih murni merusaknya |
