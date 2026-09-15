# Breakdown Output — Kata Data — 2 Jam Sekali Jalan (Tahap 4 — DRAF, menunggu G1+G2)

**Unit:** frame (5 frame 9:16). Referensi tiap generate: `channel-kata-data/konsistensi-visual/palet-gaya-data/referensi/style-sheet.png` + `palet.png`.

**Prompt Master elemen (copy persis, dipakai di semua frame):**

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

---

## F1 — Hook (Beat 1: "Dua jam. Sekali jalan.")

- **Bagian naskah:** Beat 1 penuh.
- **Deskripsi visual:** Angka hero "2 JAM" kuning elektrik raksasa di tengah frame; caption putih kecil "SEKALI JALAN" di bawahnya. Tanpa chart, tanpa kartu sumber.
- **Prompt generate:** [Prompt Master] + `Hero text exact "2 JAM" electric-yellow centered, small white caption "SEKALI JALAN" below, no chart, no source pill, no other text.`
- **File referensi:** `style-sheet.png` + `palet.png`.

## F2 — Konteks BPS (Beat 2 kalimat 1: "...BPS 2023 — ...1,5–2 jam...")

- **Bagian naskah:** Beat 2 kalimat 1.
- **Deskripsi visual:** Angka hero "1,5–2 JAM" kuning elektrik; caption putih "KOMUTER JABODETABEK"; pill abu "Sumber: BPS, 2023".
- **Prompt generate:** [Prompt Master] + `Hero text exact "1,5-2 JAM" electric-yellow centered, white caption "KOMUTER JABODETABEK" below, source pill exact "Sumber: BPS, 2023", no chart, no other text.`
- **File referensi:** `style-sheet.png` + `palet.png`.

## F3 — Konteks DTKJ (Beat 2 kalimat 2: "...35,6 persen...1–2 jam...")

- **Bagian naskah:** Beat 2 kalimat 2.
- **Deskripsi visual:** Donut chart proporsional 35,6% (busur kuning, sisa abu gelap) dengan angka "35,6%" putih di tengah; caption "RESPONDEN 1–2 JAM SEKALI JALAN"; pill "Sumber: DTKJ, 2021".
- **Prompt generate:** [Prompt Master] + `One donut chart with exactly 35.6 percent arc in electric-yellow on dark gray remainder, white number "35,6%" centered inside, white caption "RESPONDEN 1-2 JAM SEKALI JALAN", source pill exact "Sumber: DTKJ, 2021", no other text.`
- **File referensi:** `style-sheet.png` + `palet.png`.

## F4 — Artinya (Beat 3: "...30–40 hari penuh...")

- **Bagian naskah:** Beat 3 penuh (fokus visual: hasil hitungan).
- **Deskripsi visual:** Angka hero "30–40 HARI" kuning elektrik; baris putih kecil "3–4 JAM × 240 HARI KERJA"; caption "SETAHUN HABIS DI JALAN". Tanpa kartu sumber (hitungan sendiri — atribusi di VO + caption publish).
- **Prompt generate:** [Prompt Master] + `Hero text exact "30-40 HARI" electric-yellow centered, small white line "3-4 JAM x 240 HARI KERJA" above, white caption "SETAHUN HABIS DI JALAN" below, no chart, no source pill, no other text.`
- **File referensi:** `style-sheet.png` + `palet.png`.

## F5 — Penutup (Beat 4: "Kata data... Sumber: BPS 2023; DTKJ 2021.")

- **Bagian naskah:** Beat 4 penuh.
- **Deskripsi visual:** Wordmark putih "KATA DATA" di tengah; pill abu besar "Sumber: BPS 2023; DTKJ 2021" di bawahnya. Tanpa angka hero (VO membawa kalimat penutup).
- **Prompt generate:** [Prompt Master] + `Centered white wordmark exact "KATA DATA", large muted source pill exact "Sumber: BPS 2023; DTKJ 2021" below, no hero number, no chart, no other text.`
- **File referensi:** `style-sheet.png` + `palet.png`.
