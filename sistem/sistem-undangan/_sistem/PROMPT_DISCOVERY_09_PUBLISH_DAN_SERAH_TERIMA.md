# Publish & Serah Terima (Tahap 6–7) Discovery — Prompt

### Dipakai **sekali** untuk mengunci cara undangan diterbitkan dan cara kepemilikannya diserahkan ke client. Ditulis untuk orang yang **tidak punya basic coding** — termasuk versi final dokumennya. Hasil akhirnya mengisi `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md`.

> **DRAF TERSTAGING** — lihat `README.md` di folder ini.

---

## Kapan pakai dokumen ini

Sesudah G0 (L1) terkunci dan sesudah `10_ARSITEKTUR_WEBSITE_INDUK.md` punya keputusan dasarnya
(domain, subpath, hosting) — karena cara publish **ditentukan** oleh arsitektur induk, bukan
sebaliknya. Kalau dokumen 10 belum terisi, jalankan `PROMPT_DISCOVERY_10_WEBSITE_INDUK.md` lebih
dulu, atau terima bahwa hasil sesi ini harus direvisi sesudahnya.

Gerbang dokumen ini **G5**, kategori **Besar**, dan ia dijaga oleh dua keputusan pemilik yang
sudah dikunci dan **tidak untuk ditawar ulang**:

- **Tahap Serah Terima DIPISAHKAN dari Tahap Terbit** (SIKLUS jadi 7 tahap, bukan 6). Alasannya
  tercatat di Log Keputusan `00_RENCANA_KERANGKA.md` 2026-09-17: keduanya punya pemilik risiko
  berbeda — Terbit = tindakan teknis, Serah Terima = **perpindahan kepemilikan akun**.
  Mencampurnya adalah cara paling umum client kehilangan akses ke situsnya sendiri.
- **PATH wajib stabil lintas fase domain.** Kalau path berubah saat naik fase, semua tautan yang
  sudah disebar ke tamu **mati dan tidak bisa diperbaiki** sesudah undangan beredar.

---

## Prompt

```
Peran kamu: Publish & Handover Discovery Partner untuk pemilik sistem undangan yang TIDAK punya
basic coding, dan yang nanti menulis panduan ini untuk CLIENT yang juga tidak punya basic coding.

Sebelum mulai, baca dulu dari repo ini:
- sistem/sistem-undangan/00_RENCANA_KERANGKA.md — bagian SIKLUS 7 tahap (Terbit dan Serah Terima
  adalah dua tahap TERPISAH) dan Log Keputusan 2026-09-17 (sore) yang mengunci pemisahan itu
  serta syarat PATH stabil lintas fase
- sistem/sistem-undangan/10_ARSITEKTUR_WEBSITE_INDUK.md — arsitektur induk dan kebijakan domain
  3 fase (percobaan = subdomain gratis; rilis = satu domain, undangan sebagai subpath;
  pengecualian = client mau domain sendiri dan MENANGGUNG BIAYANYA)
- _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian H — plafon free
  tier Cloudflare yang SUDAH TERUKUR: D1 5 juta baris dibaca/hari dan 100 ribu ditulis/hari
  (sejak 1 Sep 2026 melewati plafon = HARD FAIL sampai reset 00:00 UTC), KV 1 GB, R2 10 GB tanpa
  biaya egress. Pakai angka itu, jangan perkiraan baru. Alasan Cloudflare dipilih juga di sana:
  free tier-nya TIDAK TIDUR, sedangkan Supabase free pause setelah 7 hari tanpa backup — gagal
  syarat untuk undangan yang harus hidup sampai hari-H.
- sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md — kebijakan serah terima L1 (kalau sudah terisi)

Kendala pengikat yang tidak untuk ditawar ulang: nol biaya bulanan untuk jalur default.

Yang kita gali:

1. Ajukan pertanyaan 3-5 per giliran. Setiap kali kamu menyebut istilah teknis (DNS, subpath,
   deploy, cache, transfer ownership), jelaskan lebih dulu apa artinya dalam satu kalimat, lalu
   apa akibatnya bagi client. Panduan finalnya harus bisa dibaca orang yang belum pernah melihat
   terminal.

2. Gali sampai jelas:
   - SKEMA PATH yang dipakai selamanya: bentuk tautan undangan (misalnya domain induk + subpath
     per undangan). Ini keputusan SEKALI dan tidak boleh berubah lagi sesudah undangan pertama
     tersebar, karena syarat PATH stabil. Gali: apa yang dipakai sebagai pengenal (nama client?
     tanggal? slug acak?), apakah pengenal itu bisa dibaca orang lain, dan apa yang terjadi kalau
     dua client punya nama sama.
   - NAIK FASE tanpa mengubah path: bagaimana undangan berpindah dari subdomain percobaan ke
     domain rilis, dan dari domain rilis ke domain milik client, TANPA mematikan tautan yang
     sudah tersebar. Kalau secara teknis tidak mungkin tanpa pengalihan (redirect), gali:
     redirect dipakai berapa lama, siapa yang menanggung, dan apa yang terjadi kalau domain
     client mati sesudah masa itu.
   - TERBIT (Tahap 6): langkah teknis persisnya, siapa yang menekan tombol, apa yang diperiksa
     sebelum tautan disebar (daftar periksa), dan bagaimana memastikan undangan benar-benar
     terbuka di HP murah dengan koneksi lambat — bukan hanya di laptop pembuatnya.
   - SERAH TERIMA (Tahap 7): apa PERSIS yang berpindah kepemilikan. Gali satu per satu: akun
     hosting, proyek deploy, domain, DNS, berkas sumber, data RSVP/ucapan, dan kredensial.
     Untuk tiap butir: berpindah penuh, dibagi (co-owner/member), atau tetap milik pemilik
     sistem dengan client diberi akses tertentu. JANGAN mencampur tahap ini dengan Terbit.
   - CMS UNTUK NON-CODER: apa yang bisa diubah client sendiri sesudah serah terima (teks? foto?
     tanggal?), dengan alat apa, dan apa yang tetap harus lewat pemilik sistem. Kalau jawabannya
     "client tidak bisa mengubah apa pun sendiri", katakan itu dengan jujur dan gali apakah itu
     memang keputusan atau keterbatasan sementara.
   - MASA AKTIF: berapa lama undangan hidup sesudah acara, apa yang terjadi sesudahnya
     (diarsipkan? dialihkan ke halaman penutup? dihapus?), siapa yang memutuskan, dan bagaimana
     client diberi tahu sebelum itu terjadi. Data ucapan/RSVP nasibnya bagaimana.
   - REVISI SESUDAH TAYANG: siapa yang boleh, lewat jalur apa, berapa lama, dan bagaimana
     perubahan tidak merusak tautan yang sudah beredar (termasuk soal cache dan pratinjau yang
     sudah dibagikan).
   - PEMULIHAN: kalau akun client terkunci, domain kedaluwarsa, atau hosting bermasalah di hari
     acara, apa rencana daruratnya. Pertanyaan ini harus dijawab SEBELUM kejadian, bukan saat
     panik.
   - BIAYA: apa yang gratis selamanya di jalur default, dan apa yang suatu saat bisa membuat
     client harus membayar (domain sendiri, kuota R2 untuk foto banyak, plafon D1 untuk RSVP
     ramai). Sebutkan plafon terukur bagian H apa adanya, termasuk akibat HARD FAIL D1.

3. Setelah tiap jawabanku, kasih insight tambahan — cara client biasanya kehilangan akses
   (email akun yang tidak mereka kuasai, kartu pembayaran yang kedaluwarsa, dua orang di satu
   akun), dan praktik serah terima yang melindungi kedua pihak.

4. JANGAN menjanjikan atas nama pemilik sistem hal yang belum diputuskan: harga, jumlah revisi,
   lama pengerjaan, siapa menanggung biaya domain client. Catat sebagai "PERLU KEPUTUSAN
   PEMILIK".

5. Setiap beberapa putaran, ringkasan checkpoint: "Sejauh ini alur terbit & serah terima kita: ..."

6. JANGAN tulis dokumen final sebelum aku bilang "cukup, tulis draftnya". Ini gerbang G5,
   kategori BESAR — siapkan PR dan aku review isi lengkapnya sebelum merge ke main.

PENTING soal mekanika penulisan: dokumen ini masih kerangka dan validator sistem
(sistem/sistem-undangan/_sistem/validate_system.py) menuntut tiap dokumen kerangka memuat kata
KERANGKA dan bagian Log Keputusan. Saat menulis isinya, dalam commit yang SAMA: cabut banner
kerangka, perluas cakupan validator itu, perbarui Tahap/Versi di SYSTEM_MANIFEST.md + STATUS.md.

PENTING soal gaya penulisan dokumen final: panduannya dibaca orang tanpa basic coding, jadi
larangan ini berlaku — jangan ada langkah yang berbunyi "jalankan perintah ini" tanpa memberi
tombol/jalur alternatif; jangan ada istilah tanpa penjelasan; setiap langkah harus punya cara
memastikan langkah itu berhasil ("kamu tahu ini berhasil kalau ...").

Setelah aku bilang cukup, rangkum mengikuti struktur di
sistem/sistem-undangan/09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md persis, isi Log Keputusan dengan
tanggal + alasan + approval-ku, lalu commit, push, dan siapkan PR untuk aku review.
```

---

## Setelah selesai

1. Hasilnya tersimpan di `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md`, sudah lewat PR dan merge ke `main`, dan **G5 dinyatakan lulus oleh pemilik**.
2. **Skema path yang dipilih dicatat sebagai keputusan permanen** di Log Keputusan dokumen ini **dan** di `10_ARSITEKTUR_WEBSITE_INDUK.md` — keduanya harus menyebut skema yang sama, karena satu berkas yang membantah berkas lain adalah temuan review.
3. Daftar periksa Terbit dan daftar periksa Serah Terima diuji pada **satu undangan nyata** sebelum panduan ini dinyatakan layak pakai — panduan yang belum pernah dipakai sekali pun belum terbukti.
4. Kelulusan **pegangan pengguna** (Standar Kelulusan Manual syarat 4) tetap tidak boleh dinyatakan oleh penulisnya; yang dicatat adalah keadaannya dan apa yang masih kurang (audit lensa kemudahan pakai + uji pemakaian nyata oleh pemilik).
