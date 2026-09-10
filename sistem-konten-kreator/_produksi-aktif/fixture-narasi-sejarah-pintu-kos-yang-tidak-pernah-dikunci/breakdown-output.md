# Breakdown Output — Pintu Kos yang Tidak Pernah Dikunci

- **Channel:** `channel-fixture-narasi-sejarah/` (FIXTURE) — Channel Brief v2
- **Model konten:** Narasi 60 Detik (v1) — **unit: segmen narasi** (Model Brief bagian 4)
- **Sumber:** `naskah-draft.md` r1 — **NASKAH FINAL (dikunci G2, 2026-09-10)**, 134 kata, estimasi total 64,85 dtk
- **Revisi breakdown:** b1 — draft Tahap 4, menunggu G1 + G2 Tahap 4
- **Karakter Tipe B terbawa dari Tahap 3:** **Tidak ada** (naskah final tidak memunculkan karakter; penghuni kos hanya disebut dalam VO)
- **Sumber eksternal:** tidak ada — deskripsi visual di bawah adalah turunan naskah fiksi fixture, bukan klaim faktual

## Aturan turunan yang diterapkan file ini

- **Override Model Brief (Tahap 4):** kolom "Prompt generate" dan "File referensi visual" diisi **deskripsi b-roll**, bukan prompt generate karakter.
- **File referensi visual:** **tidak ada file acuan terkunci** — channel faceless; Channel Brief bagian 4 menandai semua elemen Bank Konsistensi Visual "tidak berlaku" (folder `konsistensi-visual/` tidak ada). Keterangan ini eksplisit per unit, bukan kolom dikosongkan diam-diam.
- **Metode hitung durasi (konsisten dengan naskah final):** kata = token whitespace; ucapan = kata ÷ 130 × 60 dtk; jeda antarsegmen 0,5 dtk (6 jeda, sesuai Persona & Voice "jeda 0,5 detik tiap ganti gagasan"); tanpa jeda sesudah segmen terakhir.
- **Hal yang dihindari visual (global, Channel Brief bagian 5):** wajah orang yang bisa dikenali, logo merek, teks besar di layar. Gaya: footage arsip/foto benda sehari-hari, warna hangat sedikit pudar, tekstur film; palet cokelat kayu, krem, hijau tua pudar.
- **Batasan akuisisi (untuk Tahap 5):** asset = b-roll/stok berlisensi atau hasil generate bernuansa footage arsip yang memenuhi deskripsi visual + hal yang dihindari. Hasil yang meleset jauh dari deskripsi segmen tidak dipakai — cari ulang/generate ulang; penyimpangan yang mengubah makna segmen dilaporkan, bukan diganti diam-diam (checklist Tahap 5 `#05`).

## Tabel ringkasan segmen

| Seg | Peran struktur (Model Brief §2) | Kata | Ucapan | Jeda | Estimasi segmen | Kumulatif |
|---|---|---:|---:|---:|---:|---|
| S1 | Pintu masuk — hook | 7 | 3,23 | +0,50 | 3,73 | 0,00–3,73 |
| S2 | Pintu masuk — detail benda | 17 | 7,85 | +0,50 | 8,35 | 3,73–12,08 |
| S3 | Konteks kebiasaan | 26 | 12,00 | +0,50 | 12,50 | 12,08–24,58 |
| S4 | Konteks kebiasaan — insiden pembuktian | 24 | 11,08 | +0,50 | 11,58 | 24,58–36,15 |
| S5 | Yang berubah | 20 | 9,23 | +0,50 | 9,73 | 36,15–45,88 |
| S6 | Penutup — kembali ke masa kini | 24 | 11,08 | +0,50 | 11,58 | 45,88–57,46 |
| S7 | Penutup — kalimat kunci | 16 | 7,38 | — | 7,38 | 57,46–64,85 |
| **Total** | | **134** | **61,85** | **3,00** | **64,85** | — |

*(S6 memuat 23 kata huruf + 1 em-dash berdiri sendiri — dihitung 24 token, konsisten dengan metode naskah final.)*

---

## S1 — Hook: pintu yang tidak pernah dikunci

- **Bagian naskah (VO):** "Ada satu pintu yang tidak pernah dikunci."
- **Peran struktur:** pintu masuk — hook (acuan 0–8 dtk; segmen ini 3,73 dtk ✓)
- **Estimasi durasi:** 7 kata → 3,23 dtk ucapan + 0,50 dtk jeda = **3,73 dtk** (kumulatif 0,00–3,73)
- **Arahan penyampaian:** tempo lambat (±130 kata/menit), nada hangat memancing rasa ingin tahu; penekanan ringan di "tidak pernah"; jeda penuh 0,5 dtk sesudahnya — biarkan meresap, ini hook.
- **Deskripsi visual:** close-up pintu kayu tua sedikit terbuka; cahaya hangat menyusup dari celah pintu; tekstur film, fokus dangkal; warna cokelat kayu dan krem pudar. Tanpa orang.
- **Prompt generate (deskripsi b-roll, siap akuisisi):** *Close-up shot of an old wooden door slightly ajar, warm light seeping through the gap, weathered wood texture, faded warm tones (wood brown, cream), subtle film grain, shallow depth of field, archival footage mood, no people, no text, no logos.* Kata kunci stok: "pintu kayu tua sedikit terbuka cahaya hangat", "old wooden door ajar warm light film grain".
- **File referensi visual:** tidak ada — channel faceless, tidak ada elemen terkunci (lihat "Aturan turunan").
- **Cek hal yang dihindari:** tanpa wajah ✓ tanpa logo ✓ tanpa teks ✓

## S2 — Detail benda: pintu kos di ujung gang

- **Bagian naskah (VO):** "Pintu kos kecil di ujung gang, catnya mengelupas. Konon, kunci selalu tergantung di tali tembaga di dalam."
- **Peran struktur:** pintu masuk — detail benda (melintasi batas indikatif 8 dtk; berfungsi menjembatani hook ke konteks)
- **Estimasi durasi:** 17 kata → 7,85 + 0,50 = **8,35 dtk** (kumulatif 3,73–12,08)
- **Arahan penyampaian:** nada bercerita; turun pelan di "catnya mengelupas"; "Konon," dibaca seperti membuka cerita turun-temurun — sedikit berbisik, tidak menakutkan; jeda mikro natural sebelum "Konon".
- **Deskripsi visual:** (a) gang sempit sore hari menuju satu pintu kecil di ujung, cahaya hangat miring; (b) insert detail cat pintu kayu yang mengelupas; (c) insert satu kunci kuningan tua tergantung di tali tembaga pada paku di dinding bagian dalam.
- **Prompt generate (deskripsi b-roll, siap akuisisi):** *(a) Narrow alley at golden hour leading to a small old boarding-house door at the end, warm side light, faded film look; (b) close-up of peeling paint on an old wooden door, weathered texture, warm faded tones; (c) close-up of an old brass key hanging on a copper cord from a nail on an interior wall, warm light, shallow focus, film grain.* Kata kunci stok: "gang sempit pintu ujung senja", "cat pintu mengelupas close up", "kunci tua tergantung tali tembaga", "old key hanging copper string nail".
- **File referensi visual:** tidak ada — channel faceless, tidak ada elemen terkunci.
- **Cek hal yang dihindari:** tanpa wajah ✓ tanpa logo ✓ tanpa teks ✓

## S3 — Konteks kebiasaan: tanda rumah aman

- **Bagian naskah (VO):** "Dulu, itu bukan karena lalai. Itu tanda. Pintu terbuka artinya rumah aman. Kalau penghuni pulang lewat jam sebelas dan pintunya terbuka, tidak ada yang perlu dikhawatirkan."
- **Peran struktur:** konteks kebiasaan yang menempel pada benda (acuan indikatif 8–35 dtk)
- **Estimasi durasi:** 26 kata → 12,00 + 0,50 = **12,50 dtk** (kumulatif 12,08–24,58)
- **Arahan penyampaian:** tempo stabil; "Itu bukan karena lalai." dibaca lurus, lalu "Itu tanda." **tegas-pelan** — kalimat inti segmen, beri bobot tanpa menggurui; "pulang lewat jam sebelas" tidak terburu-buru; akhiri dengan rasa lega yang tenang di "tidak ada yang perlu dikhawatirkan".
- **Deskripsi visual:** malam hari di gang yang sepi dan terasa aman; pintu kos terbuka dengan cahaya lampu warm tungsten memancar dari dalam ke lantai gang; siluet pagar dan tanaman tanpa orang terlihat jelas; suasana tenang, bukan menyeramkan.
- **Prompt generate (deskripsi b-roll, siap akuisisi):** *Quiet alley at night, a boarding-house door open with warm tungsten light spilling out onto the ground, safe and calm mood, soft shadows, faded warm film tones (wood brown, cream, muted dark green), subtle film grain, no visible faces, no people in focus, no text, no logos.* Kata kunci stok: "pintu terbuka malam cahaya lampu hangat", "open door night warm light safe home", "gang malam tenang lampu".
- **File referensi visual:** tidak ada — channel faceless, tidak ada elemen terkunci.
- **Cek hal yang dihindari:** kehadiran manusia hanya tersirat lewat cahaya — tanpa wajah ✓ tanpa logo ✓ tanpa teks ✓

## S4 — Insiden pembuktian: semalam pintu terkunci

- **Bagian naskah (VO):** "Pernah ada semalam pintu terkunci. Semua penghuni bangun. Tidak ada maling. Yang tidak bisa dijelaskan hanya satu: kenapa semua orang merasa ada yang salah."
- **Peran struktur:** konteks kebiasaan — insiden yang membuktikan aturan (masih dalam rentang indikatif kebiasaan; berakhir 36,15 dtk, offset +1,15 dtk dari batas indikatif 35 — dicatat apa adanya)
- **Estimasi durasi:** 24 kata → 11,08 + 0,50 = **11,58 dtk** (kumulatif 24,58–36,15)
- **Arahan penyampaian:** perlambat sedikit; jeda mikro sebelum "Tidak ada maling."; "Tidak ada maling." dibaca datar (bukan lega — justru janggal); kalimat penutup naik tipis dan menggantung di "ada yang salah" — pertanyaan tanpa jawaban, jangan didramatisir berlebih.
- **Deskripsi visual:** malam yang sama, tapi pintu tertutup rapat; jendela-jendela kamar kos menyala satu per satu; bayangan samar bergerak di balik gorden (bukan wajah); nuansa janggal-tegang yang tertahan; hijau tua pudar lebih dominan dari biasanya.
- **Prompt generate (deskripsi b-roll, siap akuisisi):** *The same old boarding-house door firmly shut at night, bedroom windows lighting up one by one along the facade, faint indistinct silhouettes behind curtains (no recognizable faces), subtle unease, muted dark green and brown faded film palette, film grain, no text, no logos.* Kata kunci stok: "rumah malam jendela menyala satu satu", "house night windows lights turning on", "pintu tertutup malam hari".
- **File referensi visual:** tidak ada — channel faceless, tidak ada elemen terkunci; kesamaan subjek pintu lintas S1–S5 dijaga lewat deskripsi (pintu kayu kecil, cat mengelupas, cahaya warm tungsten), bukan file acuan.
- **Cek hal yang dihindari:** bayangan tak jelas, bukan wajah ✓ tanpa logo ✓ tanpa teks ✓

## S5 — Yang berubah: kos sudah tidak ada

- **Bagian naskah (VO):** "Sekarang kos itu sudah tidak ada. Yang tersisa satu kunci tua di laci, yang tidak lagi pas untuk apa pun."
- **Peran struktur:** yang berubah (acuan indikatif 35–52 dtk; segmen ini 36,15–45,88 — di dalam rentang ✓)
- **Estimasi durasi:** 20 kata → 9,23 + 0,50 = **9,73 dtk** (kumulatif 36,15–45,88)
- **Arahan penyampaian:** nada turun, melankolis tertahan; jeda kecil sesudah "sudah tidak ada."; "tidak lagi pas untuk apa pun" dibaca pelan, hampir berbisik — beban emosi segmen ada di sini, tetap tanpa menggurui.
- **Deskripsi visual:** (a) lokasi/gang tempat kos dulu berdiri — sudut yang berubah: pagar/pintu sudah tiada, suasana siang pudar; (b) insert laci kayu tua terbuka, di dalamnya satu kunci kuningan berkarat tergeletak sendiri; cahaya jendela jatuh di permukaan laci.
- **Prompt generate (deskripsi b-roll, siap akuisisi):** *(a) A quiet corner of an old alley where a small building once stood, now changed/emptied, faded daylight, nostalgic archival film look; (b) close-up inside an open wooden drawer: one single rusty old brass key lying alone, soft window light, warm faded tones, film grain.* Kata kunci stok: "laci kayu terbuka kunci tua berkarat", "old rusty key in open drawer", "gang tua berubah nostalgia".
- **File referensi visual:** tidak ada — channel faceless, tidak ada elemen terkunci; kunci di S5 = "satu kunci tua di laci" (berkarat, tersimpan), beda keadaan dari kunci tergantung di S2 — perbedaan ini disengaja mengikuti naskah, bukan inkonsistensi.
- **Cek hal yang dihindari:** tanpa wajah ✓ tanpa logo ✓ tanpa teks ✓

## S6 — Penutup: kembali ke masa kini

- **Bagian naskah (VO):** "Tidak ada yang mencatat aturannya. Tapi tiap kali pulang dan menemukan pintu rumah terbuka, tanpa sadar kita bernapas lega — sama seperti mereka dulu."
- **Peran struktur:** penutup — mengembalikan penonton ke masa kini (wajib ada menurut Channel Brief bagian 3)
- **Estimasi durasi:** 24 kata (23 kata huruf + 1 em-dash) → 11,08 + 0,50 = **11,58 dtk** (kumulatif 45,88–57,46)
- **Arahan penyampaian:** segmen paling hangat dan ringan; "Tidak ada yang mencatat aturannya." dibaca apa adanya; em-dash pada "bernapas lega — sama seperti mereka dulu" = jeda napas natural (bukan jeda penuh); "bernapas lega" dibaca dengan embusan lembut yang terdengar seperti lega sungguhan.
- **Deskripsi visual:** masa kini — pintu rumah sederhana terbuka di sore golden hour, cahaya hangat menyambut dari dalam; satu tangan dewasa mendorong pintu (tanpa wajah, tanpa identitas); suasana pulang yang melegakan; palet kembali paling hangat dari seluruh konten.
- **Prompt generate (deskripsi b-roll, siap akuisisi):** *Present-day golden hour: a simple home door being pushed open by an adult hand (no face, no identity visible), warm welcoming light from inside, feeling of coming home and relief, warmest palette of the sequence, faded film tones, film grain, no text, no logos, no brand marks.* Kata kunci stok: "pulang membuka pintu rumah sore cahaya hangat", "opening home door golden hour warm light hand no face".
- **File referensi visual:** tidak ada — channel faceless, tidak ada elemen terkunci.
- **Cek hal yang dihindari:** hanya tangan, bukan wajah ✓ tanpa logo ✓ tanpa teks ✓

## S7 — Kalimat kunci: yang berubah

- **Bagian naskah (VO):** "Yang berubah bukan pintunya. Yang berubah: kita tidak lagi tahu siapa yang dulu menjaga tanda itu."
- **Peran struktur:** penutup — kalimat kunci (beat terakhir)
- **Estimasi durasi:** 16 kata → **7,38 dtk** tanpa jeda sesudahnya (kumulatif 57,46–64,85)
- **Arahan penyampaian:** paling pelan dari seluruh naskah; "Yang berubah bukan pintunya." datar-sadar; jeda napas singkat sesudah titik dua; "menjaga" mendapat penekanan paling halus; kalimat terakhir dibiarkan menggantung — tanpa nada vonis, tanpa menggurui.
- **Deskripsi visual:** detail tali tembaga kosong tergantung di paku (tanpa kunci), bergoyang sangat pelan; atau gang sepi di senja dengan warna makin pudar; gerakan kamera minimal/statik; fade lambat menuju gelap-hangat.
- **Prompt generate (deskripsi b-roll, siap akuisisi):** *Extreme close-up of an empty copper cord hanging from a nail on an interior wall, swaying almost imperceptibly, fading warm dusk light, increasingly desaturated faded film palette, minimal or static camera, slow gentle fade out, archival nostalgic mood, no people, no text, no logos.* Kata kunci stok: "tali tembaga kosong tergantung paku", "empty string hanging nail wall dusk", "gang sepi senja warna pudar".
- **File referensi visual:** tidak ada — channel faceless, tidak ada elemen terkunci.
- **Cek hal yang dihindari:** tanpa wajah ✓ tanpa logo ✓ tanpa teks ✓

---

## Pemeriksaan terhadap batasan yang dikunci

| Pemeriksaan | Acuan (sumber resmi) | Hasil breakdown | Status |
|---|---|---|---|
| Jumlah kata naskah | 130–145 kata (Model Brief §2) | 134 kata — tidak diubah dari naskah final | ✓ |
| Total durasi estimasi | 55–65 dtk (Model Brief §2) | 64,85 dtk (61,85 ucapan + 6×0,5 jeda) — **estimasi, belum pengukuran audio** | ✓ (caveat tetap: bila rekaman nyata > batas, laporkan & minta keputusan revisi — tertulis di naskah final) |
| Hook 0–8 dtk | Model Brief §2 + pemeriksaan naskah final | S1 = 3,73 dtk | ✓ |
| Struktur beat | benda → kebiasaan → yang berubah → penutup masa kini (Model Brief §2) | S1–S2 (benda) → S3–S4 (kebiasaan) → S5 (yang berubah) → S6–S7 (masa kini) | ✓ — batas window indikatif (8/35/52/60) bergeser ±1–6 dtk karena pembagian beat naskah final (S4 berakhir 36,15; S5 36,15–45,88 di dalam 35–52; penutup mulai 45,88); offset dicatat apa adanya, window brief bersifat panduan, batas keras (kata, total durasi, hook) terpenuhi |
| Persona & Voice | Channel Brief bagian 3 | arahan penyampaian per segmen: ±130 kata/menit, jeda 0,5 dtk, hangat-agak melankolis, tanpa menggurui | ✓ |
| Gaya visual + palet | Channel Brief bagian 5 | semua segmen: footage arsip/foto benda, hangat pudar, tekstur film; cokelat kayu/krem/hijau tua pudar | ✓ |
| Hal yang dihindari | Channel Brief bagian 5 | tanpa wajah dikenali, logo, teks besar — dicek per segmen; kontak manusia dibatasi tangan (S6) dan bayangan gorden (S4) | ✓ |
| Elemen Bank Konsistensi Visual | Channel Brief bagian 4 | tidak ada yang wajib — kolom referensi diisi keterangan eksplisit per segmen | ✓ |
| Karakter Tipe B | `06_PROMPT_LIBRARY.md` A2 | tidak ada — tidak ada yang terbawa dari Tahap 3; tidak ada karakter baru dibuat di breakdown | ✓ |
| Sumber eksternal / klaim faktual | `05_CONTENT_PRODUCTION_PIPELINE.md` | tidak ada klaim faktual baru; deskripsi visual = turunan naskah fiksi | ✓ — `SUMBER.md` tetap tidak diperlukan |

## Gerbang

- **G1 Tahap 4 (breakdown sudah benar, lanjut ke Tahap 5?):** belum — diminta ke pengguna.
- **G2 Tahap 4 (breakdown dikunci sebagai dasar generate/akuisisi asset?):** belum — diminta ke pengguna, karena akuisisi/generate memakai biaya-waktu nyata dan sulit dibatalkan setelah jalan.
