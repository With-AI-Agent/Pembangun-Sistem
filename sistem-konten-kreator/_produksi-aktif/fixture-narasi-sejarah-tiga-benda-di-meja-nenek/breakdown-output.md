# Breakdown Output — Tiga Benda di Meja Nenek

> **STATUS: DRAFT TAHAP 4 — G1 BELUM, G2 BELUM.** Dibangun di atas `naskah-draft.md` **r2** (130 kata; G1 Tahap 3 disetujui 2026-09-06, **G2 naskah ditahan**). Jika naskah berubah (r3+), breakdown ini wajib disinkron ulang — jangan dipakai sebagai dasar asset tanpa sinkronisasi.

- **Tanggal:** 2026-09-06 (sesi/branch `arena/01a0744b-pembangun-sistem`)
- **Channel / Model:** Narasi Sejarah (fixture) v1 / Narasi 60 Detik v1 — keduanya `Operational`
- **Unit:** 7 **segmen narasi** (1 segmen = 1 paragraf VO), bukan shot/panel — sesuai Model Konten Brief §4
- **Sumber naskah:** `naskah-draft.md` r2 — seluruh 130 kata VO dipakai verbatim dan berurutan (jejak blob `1be4acf`)
- **Konteks dibaca ulang (checkpoint Tahap 3→4):** Channel Brief v1 (Persona & Voice, Gaya Visual §5, larangan §3), Model Konten Brief v1 (struktur 4 beat, override Tahap 4), `05` Tahap 4, `06` bagian D (struktur deskripsi b-roll), `indeks.md` + `indeks-karakter.md` (keduanya kosong)
- **Sumber eksternal:** tidak ada — cerita personal dummy/fiksi fixture; semua b-roll masih deskripsi rencana, belum ada file atau lisensi yang diperoleh
- **Karakter Tipe B:** tidak ada — nenek/anak-anak hanya disebut dalam VO, visual tetap b-roll benda (cek A2: `indeks-karakter.md` kosong)
- **Gap fondasi:** Brand Core masih template kosong (dilaporkan, bukan disembunyikan); fixture bukan channel produksi nyata
- **Garis keturunan:** breakdown sementara 112 baris di `f2d3ad2` dulu sengaja dikeluarkan dari folder aktif (keputusan administratif sesi lalu, state HEAD = Tahap 3). File ini adalah eksekusi Tahap 4 yang baru dari r2 — bukan restore.

## Checkpoint konsistensi (pra-Tahap 4, dari sumber resmi)

- Angle tetap: **radio tua sebagai pengatur pagi** — bukan tiga benda terpisah.
- Voice over: dewasa, santai tetapi tertata, hangat dan sedikit melankolis; tempo acuan ±130 kata/menit, jeda antargagasan 0,5 detik. Penekanan lembut — bukan dramatis, bukan menggurui.
- Visual: cokelat kayu, krem, hijau tua pudar; cahaya pagi hangat, tekstur film halus. **Tanpa wajah yang bisa dikenali, logo merek, teks besar di layar, atau wujud karakter baru.**
- Tidak ada elemen Bank Konsistensi Visual yang dikunci — tidak ada file acuan wajib, tidak ada prompt karakter, tidak ada reference image yang diasumsikan tersedia. Konsistensi warna/framing di bawah hanya usulan untuk konten ini, bukan penguncian lintas-konten.
- Narasi = fiksi fixture, bukan sejarah faktual. Jangan menambah kutipan siaran, lagu, tahun, atau klaim sejarah baru lewat visual/audio. "Pukul lima" adalah detail cerita.

## Timing estimasi r2 — BUKAN pengukuran rekaman

Rumus: kata ÷ 130 × 60, ditambah jeda 0,5 detik sesudah segmen 1–6. Batas kumulatif dihitung dari nilai tak-terbulatkan lalu dibulatkan dua desimal. Tambahan jeda internal/intonasi belum diukur; jangan mempercepat voice diam-diam untuk mengejar durasi.

| Segmen | Fungsi | Kata | Rentang estimasi (dtk) | Ucapan dasar (dtk) | Jeda sesudah (dtk) |
|---|---|---:|---|---:|---:|
| 1 | Benda sebagai pintu masuk | 16 | 0,00–7,88 | 7,38 | 0,50 |
| 2 | Kebiasaan pagi | 20 | 7,88–17,62 | 9,23 | 0,50 |
| 3 | Urutan yang dibaca nenek | 23 | 17,62–28,73 | 10,62 | 0,50 |
| 4 | Inti makna radio | 7 | 28,73–32,46 | 3,23 | 0,50 |
| 5 | Perubahan ke masa kini | 23 | 32,46–43,58 | 10,62 | 0,50 |
| 6 | Kebiasaan yang bertahan | 27 | 43,58–56,54 | 12,46 | 0,50 |
| 7 | Penutup reflektif | 14 | 56,54–63,00 | 6,46 | 0,00 |
| **Total** | | **130** | **0,00–63,00** | **60,00** | **3,00** |

Total estimasi **63,00 detik** — dalam batas model 55–65 detik. Bukan hasil rekaman/TTS.

## Segmen 1 — Benda sebagai pintu masuk (16 kata · 0,00–7,88 · beat 1)

**Naskah VO (verbatim):**
> Ada satu benda di sudut meja nenek: radio tua cokelat, dengan tombol aus di satu sisi.

**Deskripsi visual (b-roll):**
- Subjek: radio tua cokelat, close-up 3/4, tombol aus di satu sisi terlihat jelas.
- Environment: sudut meja kayu; latar dinding krem blur hangat.
- Gaya: footage/foto arsip, hangat-pudar, tekstur film halus.
- Mood/lighting: cahaya pagi lembut dari samping, bayangan lembut.
- Framing: medium close-up, eye-level, radio di sepertiga kanan.

**Deskripsi akuisisi** (kolom prompt generate diisi deskripsi b-roll per override Model Brief — bukan prompt karakter): "close-up radio kayu vintage di atas meja, cahaya pagi, tekstur film" (keywords: vintage wooden radio close-up, morning light, film texture).

**File referensi visual:** tidak ada — channel tidak mengunci elemen visual apa pun (Brief §4). Jangan asumsikan reference image tersedia.

**Arahan penyampaian:** tempo lambat pembuka; tekan "satu benda" dan "tombol aus"; jeda 0,5 dtk sesudahnya.

## Segmen 2 — Kebiasaan pagi (20 kata · 7,88–17,62 · beat 2)

**Naskah VO (verbatim):**
> Dulu, radio itu membangunkan satu rumah. Bukan alarm. Suara penyiar pagi pukul lima, lalu berita, lalu lagu yang itu-itu lagi.

**Deskripsi visual (b-roll):**
- Subjek: interior rumah pagi — pintu kamar terbuka ke lorong terang, atau jendela dengan tirai tersibak dan cahaya masuk. Tanpa orang.
- Environment: rumah sederhana bernuansa kayu.
- Gaya: footage arsip, hangat-pudar, tekstur film halus.
- Mood/lighting: pagi terang lembut, kontras rendah.
- Framing: wide interior.

**Deskripsi akuisisi:** "interior rumah pagi hari, cahaya masuk dari jendela, tirai tersibak" (keywords: morning home interior, window light, curtains).

**File referensi visual:** tidak ada (lihat Segmen 1).

**Arahan penyampaian:** deretan "lalu berita, lalu lagu" dibaca rata seperti rutinitas; "Bukan alarm" diberi jeda mikro sebelumnya dan dibaca datar-tegas; "pukul lima" datar — detail fiksi, bukan klaim.

## Segmen 3 — Urutan yang dibaca nenek (23 kata · 17,62–28,73 · beat 2)

**Naskah VO (verbatim):**
> Nenek tidak benar-benar mendengarkannya. Yang dia dengar adalah urutannya. Kalau lagunya berganti, air sudah matang. Kalau penyiar menyebut cuaca, anak-anak harus sudah mandi.

**Deskripsi visual (b-roll):**
- Subjek: dapur pagi — ketel/panci di kompor dengan uap tipis; boleh 2 potongan (ketel beruap → ruang dapur dengan bangku kosong dan handuk tergantung). Tanpa wajah.
- Environment: dapur sederhana bernuansa kayu.
- Gaya: footage arsip, hangat-pudar, tekstur film halus.
- Mood/lighting: cahaya pagi dari jendela dapur, uap terlihat lembut.
- Framing: medium shot; detail lalu melebar.

**Deskripsi akuisisi:** "dapur pagi hari, ketel beruap di atas kompor" (keywords: morning kitchen, steaming kettle on stove).

**File referensi visual:** tidak ada (lihat Segmen 1).

**Arahan penyampaian:** tekan "urutannya"; dua klausa "Kalau…" diberi jeda mikro di antaranya agar terasa seperti aturan rumah yang dihafal.

## Segmen 4 — Inti makna radio (7 kata · 28,73–32,46 · beat 2)

**Naskah VO (verbatim):**
> Radio itu bukan hiburan. Radio itu jam.

**Deskripsi visual (b-roll):**
- Subjek: makro skala/jarum tuner radio tua; jam dinding blur di latar sebagai pasangan makna.
- Environment: meja yang sama, latar gelap-lembut.
- Gaya: foto makro bernuansa arsip, hangat-pudar, tekstur film halus.
- Mood/lighting: sorot lembut pada skala radio, latar tenggelam.
- Framing: extreme close-up; rack focus opsional ke jam dinding.

**Deskripsi akuisisi:** "makro skala tuner radio vintage, jam dinding blur di latar" (keywords: vintage radio dial macro, wall clock bokeh).

**File referensi visual:** tidak ada (lihat Segmen 1).

**Arahan penyampaian:** dua kalimat pendek, datar-tegas, jeda di antaranya; tekan "jam". Ini jeda napas emosional — jangan dramatis.

## Segmen 5 — Perubahan ke masa kini (23 kata · 32,46–43,58 · beat 3)

**Naskah VO (verbatim):**
> Sekarang radionya tidak ada. Diganti ponsel yang bisa bangun sendiri, yang bisa kita suruh diam, yang layarnya kita lihat sebelum melihat siapa pun.

**Deskripsi visual (b-roll):**
- Subjek: ponsel modern tergeletak di meja (layar menyala blur, tanpa teks terbaca, tanpa logo terlihat); tangan mematikan alarm — tangan saja, tanpa wajah.
- Environment: meja/kamar masa kini; cahaya sedikit lebih netral namun tetap hangat.
- Gaya: footage bersih bernuansa hangat, tekstur film tipis agar sekeluarga dengan segmen lain.
- Mood/lighting: pagi, sedikit lebih terang dan dingin daripada segmen 1–4.
- Framing: close-up meja.

**Deskripsi akuisisi:** "ponsel di meja pagi hari, tangan mematikan alarm, tanpa merek terlihat" (keywords: smartphone on table morning, hand turning off alarm, no brand).

**File referensi visual:** tidak ada (lihat Segmen 1).

**Arahan penyampaian:** nada sedikit lebih datar/observatif; tekan "bisa bangun sendiri" dan "sebelum melihat siapa pun" — kepahitan lembut, bukan ceramah.

## Segmen 6 — Kebiasaan yang bertahan (27 kata · 43,58–56,54 · beat 3)

**Naskah VO (verbatim):**
> Tapi urutan paginya masih sama. Air dimasak dulu, baru anak-anak dibangunkan. Hanya saja sekarang tidak ada yang memberi tanda, jadi kami menebak-nebak sendiri kapan pagi seharusnya mulai.

**Deskripsi visual (b-roll):**
- Subjek: dapur masa kini — kompor menyala/ketel beruap; meja sarapan dengan cangkir; jam dinding menunjukkan pagi. Tanpa wajah.
- Environment: dapur terang masa kini dengan sentuhan kayu agar sekeluarga.
- Gaya: footage bersih bernuansa hangat, tekstur film tipis.
- Mood/lighting: pagi terang, nyaman, sedikit hampa.
- Framing: medium-wide dapur.

**Deskripsi akuisisi:** "dapur modern pagi hari, meja sarapan, ketel beruap" (keywords: modern kitchen morning, breakfast table, steaming kettle).

**File referensi visual:** tidak ada (lihat Segmen 1).

**Arahan penyampaian:** alur kontemplatif; tekan "masih sama" lalu turun di "menebak-nebak sendiri"; jeda 0,5 dtk sesudahnya.

## Segmen 7 — Penutup reflektif (14 kata · 56,54–63,00 · beat 4)

**Naskah VO (verbatim):**
> Yang berubah bukan kebiasaannya. Yang berubah: kita tidak lagi tahu siapa yang dulu mengaturnya.

**Deskripsi visual (b-roll):**
- Subjek: sudut meja yang SAMA seperti Segmen 1, kini tanpa radio — ruang kosong, sisa bingkai cahaya; cermin visual pembuka-penutup.
- Environment: sudut meja kayu, dinding krem, cahaya pagi.
- Gaya: footage/foto arsip, hangat-pudar, tekstur film halus — paling melankolis di antara semua segmen.
- Mood/lighting: cahaya pagi lembut, sedikit redup.
- Framing: sama seperti Segmen 1 (eye-level medium close-up) untuk efek cermin.

**Deskripsi akuisisi:** "sudut meja kayu kosong, cahaya pagi, nuansa melankolis" (keywords: empty wooden table corner, morning light, melancholic).

**File referensi visual:** tidak ada (lihat Segmen 1).

**Arahan penyampaian:** paling lambat; tekan "bukan kebiasaannya" dan "siapa yang dulu mengaturnya"; akhir menggantung lembut, tanpa penekanan moral.

## Kepatuhan brief (cek sendiri pra-G1)

- Hook 0–8 dtk: Segmen 1 selesai 7,88 ✓. Penutup kembali ke masa kini: Segmen 7 ✓. Satu benda konkret sebagai pintu masuk ✓.
- Larangan §3 Brief: tanpa klaim sejarah tak-sumber ("pukul lima" = detail fiksi) ✓; tanpa nama tokoh nyata ✓; tanpa nada menggurui ✓; tanpa clickbait ✓.
- Larangan visual §5 Brief: tanpa wajah yang bisa dikenali, tanpa logo/merek, tanpa teks besar di layar ✓ (ditegaskan per segmen, terutama Segmen 5).
- Struktur 4 beat model (0–8 / 8–35 / 35–52 / 52–60) sebagai acuan: S1→beat 1 (0–7,88 ✓); S2–S4→beat 2 (7,88–32,46 ✓); S5–S6→beat 3 (32,46–56,54 — mulai ±2,5 dtk lebih awal dari acuan 35); S7→beat 4 (56,54–63,00 — selesai di 63, tetap dalam batas 65). Batas beat diperlakukan sebagai acuan aliran, bukan pagu kaku — brief tidak menetapkan toleransi eksplisit, dan total 63 dtk memenuhi spesifikasi 55–65 dtk.
- Konsistensi lintas-segmen: S1↔S7 framing cermin; palet dan tekstur film dijaga segmen 1–7; transisi era (S4→S5) ditandai perubahan suhu cahaya, bukan ganti gaya.
