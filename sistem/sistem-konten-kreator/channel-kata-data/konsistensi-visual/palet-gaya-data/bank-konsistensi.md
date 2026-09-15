# Bank Konsistensi Visual — Palet & Gaya Data

### Dibangun via `04_CHARACTER_BUILDER_KIT.md` — 2026-09-15. Elemen milik channel `channel-kata-data`. Ini "kunci keluarga visual" yang membuat semua episode langsung dikenali di feed.

**Status:** `Calon Reference-Ready` — acuan wajib ADA di `referensi/` dan lolos audit visual (`../CATATAN-ASSET.md`): `referensi/palet.png` + `referensi/style-sheet.png` + `referensi/contoh-negatif-gaya-salah.png`. Status final `Reference-Ready` ditetapkan setelah G2 elemen.

## Jenis Elemen

Palet Warna & Gaya Render — WAJIB dirujuk di SETIAP generate visual channel ini. Mencakup juga treatment angka raksasa, gaya chart, dan kartu sumber (per keputusan brief: bukan props terpisah).

## Deskripsi (Prompt-Ready)

Motion-infografis flat modern untuk video vertikal: background navy-hitam pekat yang mengisi seluruh frame, satu aksen kuning elektrik yang hanya dipakai untuk angka hero dan maksimal separuh elemen chart, tipografi sans-serif extra-bold putih yang besar dan terbaca di layar HP, chart sederhana (bar vertikal berujung bulat atau donut) dengan proporsi yang selalu sesuai angka, dan satu pill abu redup di bagian bawah sebagai kartu sumber. Semua bentuk geometris bersih, warna flat tanpa gradien, tanpa bayangan realistis, tanpa elemen foto, tanpa karakter/clip-art.

## Palet Warna — kode hex

| Peran | Nama | Hex |
|---|---|---|
| background seluruh frame | navy pekat | `#0B1020` |
| angka hero + aksen chart | kuning elektrik (aksen, maks ±20% frame) | `#FFD60A` |
| teks utama + chart sekunder | putih | `#FFFFFF` |
| label kecil, grid, kartu sumber | abu kebiruan redup | `#8A93A6` |

Aturan palet: background navy wajib mengisi ≥70% frame; kuning hanya aksen (angka hero + maksimal separuh bar chart); warna data maksimal 3 (kuning + putih + abu); tidak ada gradien, tidak ada neon selain kuning aksen, tidak ada warna keempat apa pun.

## Gaya Render — kata kunci prompt yang terbukti

`flat vector motion-infographic, vertical 9:16, deep navy-black background, one electric-yellow accent, white extra-bold sans-serif typography, giant numbers as hero, simple rounded bar or donut chart with honest proportional axes, small muted source pill at bottom, clean geometric shapes, flat colors, no gradients, no realistic shadows, no photo elements, no people, no clip-art characters`

## Treatment Terkunci

- **Angka hero:** 40–60% tinggi layar di frame hook; kuning elektrik, extra-bold.
- **Chart:** hanya bar vertikal (ujung bulat, ascending, proporsional) atau donut; label angka selalu cocok dengan proporsi visual; sumbu jujur (Y terpotong dilarang kecuali berpenanda).
- **Kartu sumber:** satu pill kecil bawah, abu redup, format "Sumber: [lembaga], [tahun]".
- **Tipografi:** sans-serif extra-bold; ukuran minimum terbaca di layar HP 6 inci (tidak ada teks kecil).

## Referensi pembanding (acuan gaya, bukan untuk ditiru)

Satu gambar web — template bar chart vertikal + angka persen raksasa (sumber: https://mediamodifier.com/blog/infographic-templates — detail + atribusi di `SUMBER.md`; berkas TIDAK direproduksi ke repo). Yang diambil: format vertikal, angka raksasa sebagai hero, bar sederhana. Deviasi eksplisit yang dikunci: background digelapkan ke navy/hitam, satu aksen kuning, tanpa gradien.

## Contoh Negatif — gaya yang HARUS DIHINDARI

`referensi/contoh-negatif-gaya-salah.png` = contoh yang salah: render 3D glossy, background gradien pelangi, stiker clip-art campur gaya, foto tempelan, teks kecil tak terbaca. Kalau hasil generate terlihat seperti itu → regenerate, jangan dipakai.

## Prompt Master (Reusable)

> Tempel di SETIAP prompt generate visual channel ini.

```
flat vector motion-infographic frame, vertical 9:16, deep navy-black
background #0B1020 filling the frame, one electric-yellow accent #FFD60A
for hero numbers only, white extra-bold sans-serif typography #FFFFFF,
giant numbers as hero (40-60% frame height), simple rounded vertical bar
or donut chart with strictly proportional honest axes, one small muted
blue-gray source pill #8A93A6 at bottom reading "Sumber: [lembaga],
[tahun]", clean geometric shapes, flat colors only, no gradients, no
realistic shadows, no photo elements, no people, no clip-art, maximum
3 data colors
```

## Log Keputusan Elemen

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-15 | Elemen 1-channel (bukan lintas-channel); reference pack = palet (swatch + hex) + gaya (style-sheet + contoh negatif) | Hanya channel Kata Data yang memakai gaya ini; mengikuti tabel tipe reference pack kit 04 |
| 2026-09-15 | Aksen = kuning elektrik `#FFD60A` (bukan hijau mint) | Pilihan pemilik (`kuning`) — kontras tertinggi di layar HP |
| 2026-09-15 | Referensi gaya = 1 gambar web (bar vertikal mediamodifier), arahan saja, tidak direproduksi | Tugas pemilik + aturan kit 04 (rujukan eksternal dicatat di SUMBER.md) |
| 2026-09-15 | Kartu sumber & bingkai angka = bagian elemen ini, bukan props terpisah | Keputusan brief G2 — faceless, tidak ada props |
