# Draft Breakdown Output — Tiga Benda di Meja Nenek

> **DRAFT LAMA r1 — TIDAK SINKRON DENGAN NASKAH r2 (6 Sep 2026 WIB).** Pengguna telah mengizinkan revisi naskah menjadi 130 kata tanpa mengubah brief. Isi 7 segmen dan timing 144 kata di bawah **sengaja dipertahankan sebagai draft r1**, bukan breakdown revisi yang disetujui. Jangan dipakai untuk acquire/assembly; penyesuaian menunggu review naskah r2. Penandaan ini bukan penguncian atau pengulangan Tahap 4.

> **FIXTURE UJI — DRAFT, BELUM DIKUNCI.** Output Tahap 4 awal dibuat dari naskah r1 yang sudah tersimpan, hanya dengan izin lanjut **G1 Tahap 3 r1**. **G2 naskah final belum diberikan; G1 dan G2 breakdown belum diberikan.** Dokumen ini bukan izin memulai Tahap 5 atau mengarsipkan konten final.

- **Tanggal penyusunan r1:** 2026-09-05 (UTC); status tidak sinkron ditandai 2026-09-06 WIB
- **Unit output:** **segmen narasi**, bukan shot/panel; satu segmen dipasangkan dengan satu potongan b-roll netral sesuai Model Konten.
- **Sumber naskah breakdown ini:** naskah **r1 pada commit `706060d391753e97954a49ccd6275ec8d061ff22`**, bukan [naskah-draft.md revisi r2 saat ini](naskah-draft.md). Seluruh 144 kata r1 masih dipertahankan verbatim dan berurutan di bawah. Saat recovery awal naskah r1 tidak diubah; r2 baru dibuat sesudah izin revisi eksplisit pengguna.
- **Konteks:** [Channel Brief v1](../../channel-fixture-narasi-sejarah/channel-brief.md), bagian 3–6; [Model Konten Brief v1](../../channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md), bagian 2–4. Keduanya dibaca ulang sebelum checkpoint tahap ini.
- **Aturan kerja:** [pipeline](../../_sistem/05_CONTENT_PRODUCTION_PIPELINE.md), gerbang Tahap 3–5, dan [prompt library](../../_sistem/06_PROMPT_LIBRARY.md), bagian 0/B/D. Format acquire menggantikan prompt generate sesuai override model.
- **Gap fondasi:** Brand Core masih template kosong. Tidak mengarang nilai lintas-channel atau menganggap fixture sebagai produksi nyata yang sudah lengkap.
- **Sumber eksternal:** belum ada. Deskripsi b-roll di bawah adalah arahan pencarian nanti, bukan footage yang sudah diperoleh atau lisensi yang sudah diverifikasi.

## Checkpoint konsistensi

- Pintu masuk tetap **radio tua di sudut meja nenek**, bukan mengganti angle menjadi tiga benda terpisah.
- Voice over: dewasa, santai tetapi tertata, hangat dan sedikit melankolis; tempo acuan ±130 kata/menit, jeda antargagasan 0,5 detik. Penekanan lembut, bukan dramatis atau menggurui.
- Visual: cokelat kayu, krem, hijau tua pudar; cahaya pagi hangat dan tekstur film halus. **Tanpa wajah yang bisa dikenali, logo merek, teks besar di layar, atau wujud karakter baru.** Nenek/anak-anak tetap disebut dalam VO, tidak diperankan secara visual.
- Tidak ada elemen Bank Konsistensi Visual yang dikunci. Tidak ada file acuan wajib, prompt karakter, atau reference image yang diasumsikan tersedia. Konsistensi warna/framing di bawah hanya usulan untuk konten ini, bukan penguncian bank lintas-konten.
- Narasi diperlakukan sebagai cerita personal dummy fixture, bukan sejarah faktual yang telah diteliti. Jangan menambahkan kutipan siaran, lagu, tahun, atau klaim sejarah baru lewat visual/audio.

## Timing estimasi — belum memenuhi batas durasi model

**Rumus:** jumlah kata ÷ 130 × 60 detik, ditambah jeda 0,5 detik sesudah segmen 1–6. Rentang pada tabel sudah mencakup jeda sesudah segmen. Angka dibulatkan dua desimal; bukan hasil rekaman/TTS, belum menghitung tambahan jeda internal atau perubahan intonasi.

| Segmen | Fungsi | Kata | Rentang estimasi (detik) | Ucapan dasar (detik) | Jeda sesudah (detik) |
|---|---|---:|---|---:|---:|
| 1 | Benda sebagai pintu masuk | 20 | 0,00–9,73 | 9,23 | 0,50 |
| 2 | Kebiasaan pagi | 24 | 9,73–21,31 | 11,08 | 0,50 |
| 3 | Urutan yang dibaca nenek | 28 | 21,31–34,73 | 12,92 | 0,50 |
| 4 | Inti makna radio | 7 | 34,73–38,46 | 3,23 | 0,50 |
| 5 | Perubahan ke masa kini | 24 | 38,46–50,04 | 11,08 | 0,50 |
| 6 | Kebiasaan yang bertahan | 27 | 50,04–63,00 | 12,46 | 0,50 |
| 7 | Penutup reflektif | 14 | 63,00–69,46 | 6,46 | 0,00 |
| **Total** | | **144** | **0,00–69,46** | **66,46** | **3,00** |

**Temuan untuk review, bukan override:** 144 kata memang masuk rentang 130–145 kata model, tetapi 66,46 detik tanpa jeda / 69,46 detik dengan enam jeda melebihi durasi **55–65 detik**. Hook juga diperkirakan lebih panjang daripada acuan 0–8 detik; closing bergeser melewati acuan 52–60 detik. Jangan memaksa tabel menjadi 60 detik dengan mempercepat voice atau memangkas teks tanpa keputusan pengguna.

## Segmen 1 — Benda sebagai pintu masuk

**Naskah VO (verbatim):**
> Ada satu benda yang tidak pernah pindah dari sudut meja nenek: radio tua berwarna cokelat, tombolnya aus di satu sisi.

- **Visual:** radio tua cokelat di sudut meja kayu, cahaya pagi dari samping; detail tombol aus terlihat, tidak ada orang dalam frame.
- **Arahan acquire / pengganti prompt generate:** cari satu potongan b-roll tenang radio vintage tanpa merek dengan ruang kayu bernuansa hangat. Utamakan detail casing dan tombol; jangan memakai materi yang membawa logo atau tulisan dominan.
- **Referensi visual / file acuan:** deskripsi b-roll radio cokelat dan sudut meja di atas; **belum ada file**, tidak membutuhkan acuan Bank Konsistensi Visual.
- **Penyampaian:** masuk seperti bercerita, bukan membacakan fakta sejarah. Tekankan ringan “radio tua”; jeda 0,5 detik di akhir gagasan.

## Segmen 2 — Kebiasaan pagi

**Naskah VO (verbatim):**
> Dulu, radio itu yang membangunkan satu rumah. Bukan alarm. Suara penyiar pagi yang mulai bicara pukul lima, lalu berita, lalu lagu yang itu-itu lagi.

- **Visual:** b-roll radio di ruang rumah yang masih sepi; cahaya tipis dari jendela memberi kesan pagi, tanpa menyatakan jam atau tahun tertentu lewat teks.
- **Arahan acquire / pengganti prompt generate:** cari b-roll radio netral di interior kosong bernuansa cokelat/krem. Bila tersedia nanti, potongan berbeda dari sumber berlisensi yang sama dengan segmen 1 dapat menjaga kesinambungan; belum ada file yang dipilih.
- **Referensi visual / file acuan:** deskripsi radio dan interior pagi; **belum ada file**, tidak ada reference image wajib.
- **Penyampaian:** “Bukan alarm” pendek dan ringan; urutan penyiar–berita–lagu dibaca alami, tanpa menirukan suara penyiar atau menyisipkan siaran/lagu pihak ketiga. Jeda 0,5 detik sesudah segmen.

## Segmen 3 — Urutan yang dibaca nenek

**Naskah VO (verbatim):**
> Nenek tidak pernah benar-benar mendengarkannya. Yang dia dengar adalah urutannya. Kalau lagunya sudah berganti, artinya air sudah matang. Kalau penyiar sudah menyebut cuaca, artinya anak-anak harus sudah mandi.

- **Visual:** ketel mengeluarkan uap di dapur sederhana, dengan warna kayu dan krem; rutinitas diwakili benda, bukan sosok nenek atau anak-anak.
- **Arahan acquire / pengganti prompt generate:** cari satu b-roll ketel mendidih dalam cahaya pagi, tanpa orang, merek, atau label mencolok. Uap dan suasana dapur menjadi penghubung narasi tentang kebiasaan, bukan rekonstruksi peristiwa sejarah.
- **Referensi visual / file acuan:** deskripsi ketel dan dapur pagi hangat; **belum ada file**, tidak memerlukan acuan karakter/latar terkunci.
- **Penyampaian:** penekanan ringan pada “urutannya”; dua kalimat “Kalau…” mengalir dengan pola serupa, tanpa berubah menjadi nasihat. Jeda 0,5 detik sesudah segmen.

## Segmen 4 — Radio itu jam

**Naskah VO (verbatim):**
> Radio itu bukan hiburan. Radio itu jam.

- **Visual:** detail tombol radio aus dalam frame tenang; bertahan pada objek radio, tidak menambahkan benda baru sebagai pokok cerita.
- **Arahan acquire / pengganti prompt generate:** cari potongan detail radio tanpa logo, warna cokelat dan tekstur usang. Potongan dari sumber radio segmen 1 dapat dipertimbangkan setelah tersedia dan hak penggunaannya diperiksa.
- **Referensi visual / file acuan:** deskripsi tombol radio usang; **belum ada file**, tidak ada file acuan wajib.
- **Penyampaian:** kalimat kedua ditegaskan lembut, bukan punchline dramatis. Jeda 0,5 detik sesudah segmen; jeda internal tambahan perlu diuji saat pembacaan nanti.

## Segmen 5 — Pengganti di masa kini

**Naskah VO (verbatim):**
> Sekarang radionya sudah tidak ada. Diganti ponsel yang bisa bangun sendiri, yang bisa kita suruh diam, yang layarnya kita lihat sebelum melihat siapa pun.

- **Visual:** ponsel netral berada sendiri di meja kayu, layar menyala tanpa antarmuka yang terbaca; tidak menampilkan wajah atau tangan karakter.
- **Arahan acquire / pengganti prompt generate:** cari satu b-roll ponsel tanpa logo di meja, framing sederhana dan warna hangat senada radio. Hindari notifikasi pribadi, nama aplikasi, teks besar, atau antarmuka bermerek yang dominan.
- **Referensi visual / file acuan:** deskripsi ponsel netral pada meja kayu; **belum ada file**, tidak ada reference image wajib.
- **Penyampaian:** “Sekarang” menandai perpindahan waktu; tetap hangat, tidak mengecam kebiasaan memakai ponsel. Jeda 0,5 detik sesudah segmen.

## Segmen 6 — Yang tetap berlangsung

**Naskah VO (verbatim):**
> Tapi urutan paginya masih sama. Air dimasak dulu, baru anak-anak dibangunkan. Hanya saja sekarang tidak ada yang memberi tanda, jadi kami menebak-nebak sendiri kapan pagi seharusnya mulai.

- **Visual:** b-roll ketel dan uap di dapur kosong; menggemakan visual segmen 3 untuk menunjukkan kebiasaan yang masih ada tanpa menambahkan adegan manusia.
- **Arahan acquire / pengganti prompt generate:** cari potongan dapur pagi dengan ketel sebagai fokus, tanpa logo/orang. Potongan alternatif dari sumber dapur segmen 3 boleh dipertimbangkan nanti; bukan klaim footage sudah tersedia.
- **Referensi visual / file acuan:** deskripsi dapur pagi dan uap ketel; **belum ada file**, tidak ada latar terkunci lintas-konten.
- **Penyampaian:** “masih sama” lembut, lalu rasa kehilangan kecil pada “tidak ada yang memberi tanda”; jangan meratap. Jeda 0,5 detik sesudah segmen.

## Segmen 7 — Kembali ke masa kini

**Naskah VO (verbatim):**
> Yang berubah bukan kebiasaannya. Yang berubah: kita tidak lagi tahu siapa yang dulu mengaturnya.

- **Visual:** sudut meja kayu kosong dalam cahaya pagi, menggemakan posisi radio pada pembuka. Ruang kosong menutup cerita, bukan menambahkan tokoh atau klaim baru.
- **Arahan acquire / pengganti prompt generate:** cari satu b-roll sudut meja kosong bernuansa cokelat/krem, framing tenang, tanpa wajah, logo, teks, atau benda lain yang menyita fokus. Kesamaan komposisi dengan pembuka adalah arahan pemilihan, bukan jaminan sumber yang sudah diperoleh.
- **Referensi visual / file acuan:** deskripsi sudut meja kosong dan cahaya pagi; **belum ada file**, tidak memerlukan acuan visual terkunci.
- **Penyampaian:** turunkan intonasi secara alami, tidak menggurui. Tidak ada CTA atau tambahan kata; waktu tahan gambar akhir belum dimasukkan ke estimasi dan harus ditentukan setelah durasi VO benar-benar diukur.

## Catatan review r1 — historis, bukan status keputusan terkini

**Pembaruan 6 Sep WIB:** opsi revisi pada butir 1 di bawah sudah dipilih pengguna dan menghasilkan naskah r2. Catatan/timing r1 tetap disimpan; keputusan terkini dan gerbang r2 ada di `STATUS.md` serta `naskah-draft.md`. Belum ada G2 naskah atau approval breakdown.

1. **G2 naskah final (Tahap 3): belum.** Pengguna perlu membaca naskah utuh di atas/sumbernya dan memutuskan penanganan temuan durasi sebelum penguncian. Saran berdampak paling kecil: izinkan revisi draft menuju 130–134 kata tanpa mengubah angle/voice, kemudian review ulang dan ukur pembacaannya; rentang ini belum menjamin durasi final. Jika ingin mempertahankan teks dan melonggarkan durasi, perubahan Model Konten perlu **G2 tersendiri**, bukan dianggap disetujui bersama naskah.
2. **G1 breakdown (Tahap 4): belum.** Setelah dasar naskah diselesaikan, review pemenggalan, pasangan b-roll, dan arahan VO. Revisi naskah membatalkan kecocokan verbatim/timing draft breakdown ini sehingga harus diselaraskan dulu.
3. **G2 breakdown (Tahap 4): belum.** Baru setelah dependency naskah final dan review breakdown terpenuhi, tanyakan penguncian breakdown sebagai dasar acquire. Menyetujui G1 tidak mengizinkan pemakaian biaya/waktu asset tanpa G2.
4. **Tahap 5: belum dimulai, bukan dilewati.** Konten ini memiliki visual b-roll dan VO, bukan teks-only. Saat nanti memperoleh bahan eksternal, buat `SUMBER.md` sejak bahan pertama: URL/penerbit, tanggal akses, jenis, status verifikasi, lisensi/hak dan atribusi. Belum ada stok, rekaman, musik, atau suara yang dipilih/diunduh/digenerate dalam tahap ini.
5. **Judul kerja:** “Tiga Benda di Meja Nenek” belum menjadi judul publish yang disetujui. Naskah berfokus pada radio sebagai pengatur pagi; jangan menjanjikan pembahasan tiga benda tanpa isinya. Penyesuaian judul/metadata diputuskan pada gerbang yang relevan, bukan dengan menambah isi naskah sendiri.
6. **G3 merge: belum.** Draft PR hanya checkpoint untuk review; bukan persetujuan konten final, bukan izin merge atau publish. Naskah belum diarsipkan dan folder produksi tidak dihapus.
