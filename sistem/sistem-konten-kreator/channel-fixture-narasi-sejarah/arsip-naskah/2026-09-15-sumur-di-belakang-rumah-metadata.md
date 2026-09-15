# Metadata Reproducibility — Sumur di Belakang Rumah

- **Channel:** `channel-fixture-narasi-sejarah` (Narasi Sejarah — FIXTURE)
- **Model konten:** Narasi 60 Detik **v2** — unit segmen narasi, 108–125 kata, 55–65 detik, tempo 125 kata/menit, jeda 0,7 dtk
- **Tanggal produksi:** 2026-09-15
- **Branch produksi:** `arena/01a0a2fe-pembangun-sistem`
- **Judul kerja:** Sumur di Belakang Rumah
- **Judul tayang resmi:** "Sumur yang Tidak Pernah Sepi" (Opsi 1 dari 4 opsi di publish-prep.md — **G2 disetujui 2026-09-15**)
- **Naskah final:** 118 kata, 60,84 dtk estimasi (56,64 + 4,20 dtk jeda), whitespace-split per paragraf 12/11/14/23/8/27/23 = 118
- **Topik singkat:** sumur/keran umum sebagai ruang bertemu tetangga; air ledeng mengakhiri kebiasaan antrean, bukan kebutuhan akan air

## Versi brief yang dipakai

- **Channel Brief:** v4 — 2026-09-15 — `channel-fixture-narasi-sejarah/channel-brief.md` — dikunci **G2 2026-09-15** (G3 menunggu) — tempo ±125 kata/menit + jeda 0,7 dtk + pembuka khas "Dulu, ada satu benda yang…"
- **Model Konten Brief:** v2 — 2026-09-15 — `model-konten/narasi-60-detik/brief.md` — dikunci **G2 2026-09-15** (G3 menunggu) — rentang 108–125 kata
- **Brand Core:** masih template kosong — gap dilaporkan (Channel Brief mencatat gap ini) — tidak ada nilai lintas-channel yang diwarisi
- **Pipeline:** `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md` — 6 tahap kerangka standar + override ringan Model Brief
- **Prompt Library:** `_sistem/06_PROMPT_LIBRARY.md` — bagian A2 (cek karakter Tipe B) + D (generate b-roll)

## Gerbang approval (rekonstruksi dari STATUS.md unit produksi)

- G1 Tahap 1 (Ideation) — 2026-09-15 — ide "Sumur di belakang rumah"
- G1 Tahap 2 (Konsep & Angle) — 2026-09-15
- G1 Tahap 3 (Naskah draft) — 2026-09-15
- G2 naskah final — 2026-09-15
- G1 Tahap 4 (Breakdown) — 2026-09-15
- G2 breakdown — 2026-09-15
- G1 Tahap 5 (Asset) — 2026-09-15
- G2 Tahap 6 (Assembly + judul tayang) — 2026-09-15
- G3 merge — menunggu keputusan pemilik (PR tanpa auto-merge)

## Aset b-roll (7, vertikal 9:16 = 768×1376) + sha256

| Segmen | File | sha256 | Inspeksi |
|---|---|---|---|
| S1 | `S1-mulut-sumur.png` | `297ff89bb6f796cb356125c818de0f043bb1cc17a64f1b10ffde9f1839b0f7b3` | bersih |
| S2 | `S2-ember-tali.png` | `fac83ac591b918168ff4120d8d5adc3e2901293ff57042aa59e81ce8057f16f9` | bersih |
| S3 | `S3-ember-berjejer.png` | `f1531acb0b7ac63fad508547ce3a4e23111bef7641b56badd459de4be3e7bef1` | bersih (retry 1x setelah error sisi model) |
| S4 | `S4-sandal-bayangan.png` | `808a3ef563aa21dae6e5c30ae2c3ad387e14fc35b4ba5351ba24ed671d858c31` | bersih — bayangan siluet, wajah tidak terlihat |
| S5 | `S5-ember-penuh.png` | `bf2ac328d9105da577ef6ab4dfac08f07f795c7d6cc04e98acf1c49781b8650c` | bersih — air hanya riak |
| S6 | `S6-keran-dapur.png` | `a1c028cbec31d1a76fd3acbe5e6963121d99ad950eb76ac0f54dc3eaa8684f85` | bersih — kotak kecil buram tidak terbaca |
| S7 | `S7-sumur-ditutup.png` | `7426759be9a384ba192b417d2ddc2ef93425a4921fa03b30f18e8d95c483f23e` | bersih — batik berpola tanpa teks |

**Accepted limitation:** tidak ada yang wajib dicatat — seluruh objek kecil yang muncul tidak membentuk huruf/angka/kata yang terbaca.

## Prompt final per unit visual

Semua prompt mengikuti gaya channel: foto benda sehari-hari, warna hangat sedikit pudar, tekstur film, palet cokelat kayu + krem + hijau tua pudar, vertical 9:16, shallow depth of field; **hindari** wajah dikenali, logo merek, dan teks/huruf/angka yang terbaca. Rincian per segmen ada di `breakdown-output.md` unit produksi (`_produksi-aktif/narasi-sejarah-sumur-di-belakang-rumah/breakdown-output.md`) dan hasil inspeksi di `assets/CATATAN-ASSET.md`.
