# Arsip Reproducibility Metadata — Pintu Kos yang Tidak Pernah Dikunci

- **Tanggal produksi:** 2026-09-10 (PR #36, branch `arena/01a088e2-pembangun-sistem`)
- **Model konten:** Narasi 60 Detik — Model Konten Brief **v1** (`Operational`)
- **Versi brief:** Channel Brief **v2** (`Operational`; Brand Core `_sistem/01_BRAND_CORE.md` masih template kosong — gap tercatat sadar di brief unit)
- **Judul tayang resmi:** menunggu pilihan pemilik di G2 Tahap 6 — opsi di `publish-prep.md` (slug arsip memakai judul kerja)
- **Gerbang produksi:** G1 Tahap 1/2/3 (2026-09-09) · G2 naskah final (2026-09-10) · G1+G2 Tahap 4 (2026-09-10) · G1 Tahap 5 (2026-09-10) · G2 konten final & G3: menyusul/tercatat di STATUS + log sesi

## Prompt final per unit visual (+ file referensi yang disertakan)

Gaya seragam di semua prompt: *warm faded archival film still; muted palette of wood brown, cream, faded dark green; subtle 16mm film grain; no people faces / no readable text / no logos / no brand marks*.

| File | Referensi disertakan | Prompt final (verbatim seperti dipakai) |
|---|---|---|
| `s1-hook-pintu-sedikit-terbuka.jpg` | — | "Close-up of a small old wooden boarding-house door slightly ajar at the end of a narrow corridor, warm tungsten light seeping through the thin gap, weathered wood with gently peeling faded cream paint, shallow depth of field, warm faded archival film still, muted palette of wood brown, cream and faded dark green, subtle 16mm film grain, soft nostalgic documentary mood, no people, no faces, no readable text, no logos, no brand marks" |
| `s2-kunci-di-tali-tembaga.jpg` | `s1-hook-pintu-sedikit-terbuka.jpg` | "Same weathered old boarding-house interior as the reference image: extreme close-up of an old brass key hanging on a copper cord from a small nail on the interior wall right beside the door, the door's peeling faded cream paint softly out of focus in the background, warm side light, shallow depth of field, warm faded archival film still, wood brown and cream palette with faded dark green, subtle 16mm film grain, nostalgic documentary mood, no people, no faces, no readable text, no logos" |
| `s2a-gang-menuju-pintu-senja.jpg` | — | "Narrow old alley at golden hour leading to one small weathered wooden door at the far end, warm slanting evening light brushing the old walls, quiet and calm, a few potted plants and a simple wooden fence in soft silhouette, warm faded archival film still, muted palette of wood brown, cream and faded dark green, subtle 16mm film grain, nostalgic documentary mood, no people, no faces, no readable text, no logos" |
| `s3-pintu-terbuka-malam.jpg` | `s1-hook-pintu-sedikit-terbuka.jpg` | "The same small old wooden boarding-house door with peeling paint as the reference image, now standing fully open at night, warm tungsten light spilling generously from inside onto the quiet floor in front of it, safe and calm mood, night blues around the edges, no people visible, muted palette of wood brown, cream and faded dark green, subtle 16mm film grain, faded warm archival film still, no faces, no readable text, no logos" |
| `s4-pintu-terkunci-jendela-menyala.jpg` | `s1-hook-pintu-sedikit-terbuka.jpg` | "Night scene of the same old boarding house as the reference image: its weathered wooden door firmly shut with a simple latch, small bedroom windows along the old facade lighting up one by one with dim warm light, curtains mostly still, at most one very faint distant shadow behind a curtain, restrained quiet unease without drama, muted dark green and wood brown faded palette, subtle 16mm film grain, archival film still, no visible faces, no prominent human figures, no readable text, no logos" — **versi perbaikan setelah hasil pertama menampilkan siluet menonjol** |
| `s5-kunci-tua-di-laci.jpg` | `s2-kunci-di-tali-tembaga.jpg` | "Close-up still life: the same old brass key as the reference image, now old and rusty, lying alone inside an open old wooden drawer, soft window light falling across the worn wood surface of the drawer, quiet melancholic mood, warm faded tones, wood brown and cream palette, subtle 16mm film grain, nostalgic documentary still, no people, no readable text, no logos" |
| `s5a-sudut-gang-yang-berubah.jpg` | — | "A quiet corner of an old alley in faded daylight where a small boarding house once stood: the spot is now changed and emptied, bare wall and cleared ground where a door used to be, faint traces of the old foundation, nostalgic and slightly melancholic mood, warm faded archival film still, muted palette of wood brown, cream and faded dark green, subtle 16mm film grain, documentary still, no people, no readable text, no logos" |
| `s6-pintu-rumah-kini-golden-hour.jpg` | — | "Present-day golden hour: a simple home front door being gently pushed open by an adult hand, only the hand and forearm visible, warm welcoming light glowing from inside the home, feeling of quiet relief of coming home, the warmest honey-gold faded film tones, subtle 16mm film grain, soft nostalgic documentary mood, no face visible, no identity, no readable text, no logos, no brand marks" |
| `s7-tali-tembaga-kosong-senja.jpg` | `s2-kunci-di-tali-tembaga.jpg` | "The same copper cord as the reference image, now empty without the key, hanging from the same small nail on the same weathered interior wall, swaying almost imperceptibly, fading warm dusk light dimming across the wall, increasingly desaturated faded palette, minimal static composition, quiet melancholic ending mood, subtle 16mm film grain, archival film still, no people, no readable text, no logos" |

## Daftar asset

9 file `.jpg` (±1,7 MB total): `s1-hook-pintu-sedikit-terbuka`, `s2-kunci-di-tali-tembaga`, `s2a-gang-menuju-pintu-senja`, `s3-pintu-terbuka-malam`, `s4-pintu-terkunci-jendela-menyala`, `s5-kunci-tua-di-laci`, `s5a-sudut-gang-yang-berubah`, `s6-pintu-rumah-kini-golden-hour`, `s7-tali-tembaga-kosong-senja`.

- **Lokasi penyimpanan:** di dalam repo, `_produksi-aktif/fixture-narasi-sejarah-pintu-kos-yang-tidak-pernah-dikunci/assets/` — **sementara**: folder produksi akan dihapus setelah pemilik mendownload hasil (aturan repo). Salinan permanen di luar repo = unduhan pemilik (belum dilakukan per tanggal arsip ini).

## Elemen konsistensi

- Bank Konsistensi Visual: **tidak ada elemen terkunci** (channel faceless — Channel Brief bagian 4).
- Kontrol konsistensi subjek berulang via chaining internal produksi (prinsip `06_PROMPT_LIBRARY.md` bagian A): acuan pintu = `s1` (dipakai di S2/S3/S4); acuan kunci+tali tembaga = `s2` (dipakai di S5/S7).

## Karakter Tipe B

Tidak ada — naskah tidak memunculkan karakter; `indeks-karakter.md` tidak berubah.

## Sumber eksternal

Tidak ada — fiksi fixture tanpa bahan eksternal; tidak ada file `-sumber.md` (tidak diwajibkan).

## Catatan produksi

- Jalur akuisisi: **generate di dalam sesi** (alasan: gerbang rights-check Tahap 5 — lisensi stok web tidak bisa diverifikasi dari sesi; tidak ada referensi visual dari web).
- **S4 digenerate ulang 1×** (hasil pertama siluet menonjol — berlebihan vs deskripsi terkunci "bayangan samar … tertahan"); **S2a/S5a** ditambah untuk cakupan penuh deskripsi visual S2/S5. Rincian + hasil cek checklist: `assets/CATATAN-ASSET.md` (selagi folder produksi belum dihapus).
- **VO belum direkam** — direkam/di-TTS-kan di luar sesi agent saat assembly (Persona & Voice: suara dewasa, ±130 kata/menit, jeda 0,5 dtk/gagasan). Durasi 64,85 dtk = ESTIMASI — ukur rekaman nyata; bila > batas 55–65 dtk, laporkan & minta keputusan revisi (instruksi naskah final).
- Panduan assembly (urutan asset × segmen × gerakan kamera): `publish-prep.md` bagian 5 (selagi folder produksi belum dihapus).
