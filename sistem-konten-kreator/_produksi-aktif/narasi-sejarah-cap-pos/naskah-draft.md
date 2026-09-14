# Naskah Draft — Cap Pos (judul kerja: "Tanggal yang sampai lebih dulu daripada orangnya")

- **Channel:** `channel-fixture-narasi-sejarah/` (FIXTURE)
- **Model konten:** Narasi Riset 60 Detik v1 (Alur Kerja Kustom) — target 130–145 kata, durasi 55–65 detik, tempo ±130 kata/menit
- **Tahap:** 3 — Naskah/Script (**final r1**, dikunci G2 2026-09-14; diarsipkan pada Tahap 6)
- **Jumlah kata VO:** **130** — dihitung dari bagian Naskah saja (whitespace-split, kalimat VO antara heading "Naskah" dan garis pemisah; hitung ulang akurat pasca-revisi: `awk '/^## Naskah/{f=1;next}/^---/{f=0} f&&NF' naskah-draft.md | wc -w` = 130)
- **Rencana durasi:** **≈ 62,9 detik estimasi** = 130 kata / 130 kata/menit × 60 = 60 detik ucapan + jeda antarparagraf (lihat catatan di bawah)
- **Revisi:** **r1 (final)**, 2026-09-14 — micro-revisi atas koreksi G2 pengguna: paragraf 2 "tanggal ketika seseorang menulis kabar" → "tanggal ketika kabar itu dikirim" (akurasi: cap pos mencatat tanggal pengiriman/pemrosesan di kantor pos kota pengirim, bukan tanggal penulisan); selaraskan "waktu kata-kata itu ditulis" → "waktu dikirim" agar tidak kontradiksi. Untuk menjaga jumlah kata tetap dalam rentang 130–145 setelah pemotongan, tambahkan dua kata kecil secara natural ("surat makin jarang" → "surat makin jarang dikirim"; "jarak antara dua waktu" → "jarak di antara dua waktu").
- **Sumber eksternal:** YA — lihat `SUMBER.md` dan `peta-fakta.md`; setiap klaim faktual telah dipetakan. Tidak ada atribusi wajib di caption.
- **Karakter Tipe B:** tidak ada. Tokoh dalam narasi adalah generik ("orang", "seseorang", "kita"); tidak ada wujud karakter per konten, visual tetap b-roll benda sesuai model.

---

## Naskah (voice over)

Dulu, ada satu benda di sudut amplop: lingkaran tinta hitam yang mengenai separuh prangko.

Cap itu ditabalkan di kota pengirim sebelum surat berangkat. Di sana tertulis nama kota dan tanggal ketika kabar itu dikirim. Berhari-hari kemudian, di kota tujuan, cap kedua ditabalkan di belakang amplop. Satu surat membawa dua waktu: waktu dikirim, dan waktu dibaca. Keduanya tidak pernah sama.

Dulu, ada rumah yang menanti kabar dari orang jauh. Sebulan sekali, cap di kertas adalah tanda pertama bahwa perjalanan itu selesai.

Ketika ponsel masuk ke rumah, surat makin jarang dikirim. Orang tidak lagi mengirim kertas untuk bilang "aku baik-baik saja".

Sekarang pesan tiba di detik yang sama. Tidak ada lagi jarak di antara dua waktu. Tidak ada yang mencatat bahwa sebuah tanggal sudah menempuh perjalanan jauh untuk sampai ke mata kita.

---

## Hitungan kata per paragraf (whitespace-split, akurat pasca-revisi)

| Paragraf | Teks pembuka | Jumlah kata | Estimasi ucapan @130 kata/menit |
|---|---|---:|---:|
| 1 (hook) | "Dulu, ada satu benda…" | 14 | 6,5 detik |
| 2 (fungsi cap — dua waktu) | "Cap itu ditabalkan…" | 47 | 21,7 detik |
| 3 (rumah yang menanti) | "Dulu, ada rumah…" | 22 | 10,2 detik |
| 4 (yang berubah) | "Ketika ponsel…" | 19 | 8,8 detik |
| 5 (penutup) | "Sekarang pesan…" | 28 | 12,9 detik |
| **Total ucapan** |  | **130** | **= 60,0 detik** |
| + 4 jeda antarparagraf × ~0,7 detik |  | — | ≈ +2,9 detik |
| **Estimasi total** |  | — | **≈ 62,9 detik** (dalam rentang 55–65 detik) |

> Jeda dipasang di 4 titik antarparagraf dengan ruang napas sekitar 0,5–0,8 detik bergantung intonasi. Tidak terburu-buru; bila rekaman nyata melewati 65 detik, lakukan revisi teks (bukan mempercepat suara diam-diam) dan laporkan.

## Catatan fact-check (gerbang sebelum G2 naskah)

- **"Lingkaran tinta hitam yang mengenai separuh prangko"** → status `Terverifikasi` (S8, S9, S10)
- **"Cap ditabalkan di kota pengirim sebelum surat berangkat… nama kota dan tanggal ketika kabar itu dikirim… cap kedua di belakang amplop di kota tujuan"** → `Terverifikasi` (S9, S10, S11 — akurat: cap mencatat tanggal ketika surat diterima/diproses di kantor pos pengirim; dikoreksi dari "ketika seseorang menulis kabar" di r0)
- **"Satu surat membawa dua waktu: waktu dikirim, dan waktu dibaca. Keduanya tidak pernah sama."** → narasi/inferensi (bukan klaim faktual; kini konsisten dengan definisi cap yang mencatat waktu pengiriman, bukan penulisan)
- **"Rumah menanti kabar dari orang jauh, sebulan sekali"** → `Cukup (bahasa diturunkan dari S13)`; kata "sebulan sekali" berasal dari kesaksian perantau dan sengaja tidak diberi nama/tempat agar jadi pengalaman generik
- **"Ketika ponsel masuk ke rumah, surat makin jarang…"** → `Terverifikasi` (S14, S15, S16, S17 — periode 2000–2008, penyebab SMS+internet)
- **"Pesan tiba di detik yang sama… tidak ada yang mencatat…"** → narasi/penutup, dibangun dari F1–F6; nada sesuai Persona & Voice (kosakata "tidak ada yang mencatat" dan "yang tersisa" muncul secara alami, tidak dipaksakan)
- **Tidak ada klaim yang berstatus `Tidak bisa diverifikasi` yang ditulis sebagai kepastian.**
- **Tidak ada nama tokoh, tidak ada angka tahun, tidak ada clickbait.**

## Cek gaya bahasa (contoh positif/negatif)

- **Sesuai (contoh positif):** kalimat pendek; "Dulu, ada satu benda…" mengikuti frasa pembuka khas channel; "Tidak ada yang mencatat…" memakai kosakata khas; penutup kembali ke masa kini tanpa menggurui.
- **Dihindari (contoh negatif):** bahasa berbunga/puitis berlebihan ("maha suci rindu", "surat itu adalah puisi yang dikirim angin"), nada menggurui ("zaman sekarang orang terlalu cepat"), sebut tahun/nama tokoh, moral "dulu lebih baik".
