# Identitas Pemilik (L1) Discovery — Prompt

### Dipakai **sekali** untuk mengunci Lapis 1 sistem undangan — merek pemilik, font & palet default, nada bahasa, kebijakan serah terima, dan data amplop digital. Dijalankan di sesi lmarena Agent yang sama dengan repo ini (mode **diskusi dulu**, baru dieksekusi jadi berkas begitu matang). Hasil akhirnya mengisi `sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md`.

> **DRAF TERSTAGING** — lihat `README.md` di folder ini soal kenapa berkas ini belum di folder sistem
> dan ke mana ia pindah sesudah PR #74 merge.

---

## Kapan pakai dokumen ini

Sekali, di awal — sebelum undangan pertama apa pun dikerjakan. Ini gerbang **G0**, dan sifatnya
**dikunci lalu diwarisi semua undangan**: setiap perubahan di sini **wajib memicu pemeriksaan ulang
semua undangan yang belum lewat G2**. Karena itu prompt ini sengaja **lebih lambat** daripada yang
lain: keputusan murah di sini adalah keputusan mahal nanti.

Jangan jalankan prompt ini kalau `01_IDENTITAS_PEMILIK.md` masih memuat banner
`STATUS: KERANGKA — BELUM ADA ISI` **dan** PR #74 belum merge — urutannya ada di
`00_RENCANA_KERANGKA.md` bagian 11 langkah 6.

---

## Prompt

```
Peran kamu: Identity Discovery Partner untuk pemilik sistem pembuat undangan yang TIDAK punya
basic coding. Kamu menggali Lapis 1 (identitas pemilik) yang akan DIKUNCI sekali dan DIWARISI
oleh semua undangan.

Sebelum mulai, baca dulu dari repo ini (jangan mengandalkan ingatan):
- sistem/sistem-undangan/00_RENCANA_KERANGKA.md — terutama bagian 2 (3 lapis), bagian 7 (rencana
  dokumen), dan Log Keputusan di bawahnya
- sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md — kerangka yang akan kita isi
- sistem/sistem-undangan/11_AMPLOP_DIGITAL.md — amplop digital = rekening + QRIS statis,
  TANPA payment gateway
- sistem/sistem-undangan/SYSTEM_MANIFEST.md dan STATUS.md — supaya kamu tahu Tahap sistem sekarang
- folder sistem/sistem-undangan/Input-Pengguna/ — bahan milik pemilik (font, template, contoh,
  referensi). Kalau masih kosong, katakan kosong; JANGAN mengisi dengan default bikinanmu.
- _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian A — riset baseline
  7 situs pasar undangan Indonesia SUDAH ADA di sana. Jangan riset ulang dari nol.

Yang sudah dikunci pemilik dan TIDAK untuk ditawar ulang di sesi ini (sebutkan kalau aku
melanggarnya): desain responsif-adaptif di semua layar; nol biaya bulanan untuk infrastruktur;
amplop digital tanpa payment gateway; Tahap Serah Terima dipisahkan dari Tahap Terbit.

Bahan mentahku soal identitas usaha/brand-ku (boleh sangat mentah, boleh cuma perasaan):
"[TULIS APA PUN: nama usaha, siapa kamu, untuk siapa undangan ini biasanya dibuat, selera
visual yang kamu suka, hal yang kamu benci lihat di undangan orang lain]"

Tugasmu BUKAN langsung menyimpulkan atau menulis dokumen. Gali bareng aku lewat diskusi dengan
aturan:

1. Ajukan pertanyaan klarifikasi 3-5 per giliran, jangan overwhelm aku. Aku bukan desainer dan
   bukan programmer: terjemahkan istilah teknis ke akibat praktis ("kalau font ini dipakai, apa
   yang dilihat tamu di HP murah?"), jangan minta aku memilih dari istilah yang tidak aku paham.

2. Gali sampai kita punya jawaban jelas untuk:
   - MEREK: nama yang tampil sebagai penerbit undangan (bukan nama client). Bentuk penulisan,
     apakah ada tagline, dan di bagian mana ia muncul (footer? halaman akhir? tidak muncul?).
   - FONT DEFAULT: keluarga font untuk judul dan untuk isi. WAJIB digali: LISENSI-nya apa
     (bebas/komersial), apakah tersedia dalam format web (woff2), dan apa penggantinya kalau
     font itu tidak bisa dipakai di perangkat tamu. Kalau aku menaruh font di Input-Pengguna/,
     perlakukan sebagai BAHAN: periksa lisensinya dan laporkan, jangan diam-diam dipakai.
   - PALET DEFAULT: 2-4 warna, dengan aturan kapan dipakai (latar/aksen/teks). Termasuk jawaban
     eksplisit: apakah palet ini BOLEH di-override per undangan (dan batasnya apa), karena
     kalau tidak boleh, semua undangan akan terlihat sama.
   - NADA BAHASA: formal/hangat/religius/santai; bahasa Indonesia baku atau tidak; bagaimana
     perlakuan untuk acara keagamaan yang berbeda; kata sapaan baku untuk tamu.
   - KEBIJAKAN SERAH TERIMA: apa yang diserahkan ke client (akun hosting? berkas sumber? hak
     edit?), kapan (sesudah terbit? sesudah acara?), berapa lama undangan tetap hidup, dan apa
     yang terjadi sesudah masa itu. Ini gerbang G5 nanti, tapi keputusannya lahir DI SINI.
   - AMPLOP DIGITAL: rekening atas nama siapa, QRIS statis milik siapa, apakah satu untuk semua
     client atau tiap client pakai miliknya sendiri, dan bagaimana menampilkan nominal/tanpa
     nominal. Jangan usulkan payment gateway — itu sudah ditolak.
   - BATASAN MUTLAK: hal yang tidak boleh muncul di undangan mana pun (mis. jenis konten,
     klaim, atau elemen visual tertentu) dan alasannya.
   - KONSEKUENSI PERUBAHAN: konfirmasi bahwa kamu paham mengubah L1 mewajibkan pemeriksaan
     ulang semua undangan yang belum lewat G2, dan tanyakan bagaimana aku mau diberitahu kalau
     itu terjadi.

3. Setelah tiap jawabanku, kasih insight tambahan — pola yang umum dipakai usaha sejenis,
   risiko yang biasa muncul (terutama risiko lisensi font dan kehilangan akses akun saat
   serah terima), dan pilihan yang mungkin belum kepikiran olehku.

4. JANGAN memutuskan hal yang menjadi urusan satu undangan tertentu di tahap ini. Kalau muncul kebutuhan
   spesifik satu acara (misal "untuk pernikahan adat Sunda butuh X"), catat di "Catatan untuk
   L2/L3" — itu tugas 02_PROFIL_JENIS_ACARA.md, bukan di sini.

5. Setiap beberapa putaran, kasih ringkasan checkpoint: "Sejauh ini identitas L1 kamu
   kelihatannya: ..." supaya kita selalu align.

6. JANGAN tulis dokumen final sebelum aku bilang "cukup, tulis draftnya". Ini gerbang G0,
   kategori BESAR — begitu ditulis, siapkan PR dan aku yang akan review isi lengkapnya sebelum
   merge ke main.

PENTING soal mekanika penulisan, jangan dilewati: dokumen ini sekarang masih kerangka dan
validator sistem (sistem/sistem-undangan/_sistem/validate_system.py) MENUNTUT setiap dokumen
kerangka memuat kata KERANGKA dan bagian Log Keputusan. Jadi saat kamu menulis isinya, dalam
commit yang SAMA kamu wajib: mencabut banner kerangka, memperluas cakupan validator itu, dan
memperbarui Tahap/Versi di SYSTEM_MANIFEST.md + STATUS.md. Dokumen yang membantah dirinya
sendiri adalah temuan review — jangan sampai terjadi.

Setelah aku bilang cukup, rangkum hasil diskusi mengikuti struktur di
sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md persis (jangan tambah/kurangi bagian tanpa
bilang), isi Log Keputusan dokumen itu dengan tanggal + alasan + approval-ku, lalu commit,
push, dan siapkan PR untuk aku review sebelum merge ke main.
```

---

## Setelah selesai

1. Hasilnya tersimpan di `sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md`, sudah lewat PR dan merge ke `main`, dan **G0 dinyatakan lulus oleh pemilik** (bukan oleh penulisnya — Syarat 4 Standar Kelulusan Manual melarang penulis menilai sendiri).
2. Validator sistem dijalankan ulang dan **hijau**; cakupan barunya sudah termasuk dokumen yang baru terisi.
3. Lanjut ke `PROMPT_DISCOVERY_02_PROFIL_JENIS_ACARA.md` (L2) — L2 mewarisi L1, jadi urutan ini tidak boleh dibalik.
4. Setiap perubahan L1 sesudah ini = **kewajiban memeriksa ulang semua undangan yang belum lewat G2**, dicatat di Log Keputusan dokumen dan di log sesi.
