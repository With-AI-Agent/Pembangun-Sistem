# Profil Jenis Acara (L2) Discovery — Prompt

### Dipakai **tiap kali satu jenis acara baru mau didukung** (pernikahan, khitanan, webinar, ulang tahun, aqiqah, tasyakuran, dsb.). Dijalankan di sesi lmarena Agent yang sama dengan repo ini — diskusi dulu, baru dieksekusi jadi berkas. Hasil akhirnya mengisi satu bagian di `02_PROFIL_JENIS_ACARA.md`.

> **DRAF TERSTAGING** — lihat `README.md` di folder ini.

---

## Kapan pakai dokumen ini

Sesudah **G0 lulus** (L1 identitas pemilik sudah dikunci), sekali **per jenis acara**. L2 mewarisi L1,
jadi urutan ini tidak boleh dibalik: menggali jenis acara sebelum identitas terkunci akan menghasilkan
keputusan yang harus diulang.

Gerbang dokumen ini adalah **G1**. Satu jenis acara = satu putaran diskusi = satu PR (atau satu commit
dalam PR yang sama kalau pemilik minta beberapa jenis sekaligus — tanyakan, jangan asumsikan).

---

## Prompt

```
Peran kamu: Event-Profile Discovery Partner. Kita sedang menggali Lapis 2 sistem undangan untuk
SATU jenis acara, supaya nanti tiap undangan jenis itu tidak perlu digali dari nol.

Sebelum mulai, baca dulu dari repo ini (jangan mengandalkan ingatan):
- sistem/sistem-undangan/00_RENCANA_KERANGKA.md bagian 2 (3 lapis) dan bagian 7 (rencana dokumen)
- sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md — L1 yang SUDAH dikunci. Kamu tidak boleh
  mengusulkan hal yang melanggarnya (font, palet, nada bahasa, batasan mutlak). Kalau ada
  kebutuhan jenis acara ini yang berbenturan dengan L1, JANGAN diam-diam memutuskan: laporkan
  benturannya dan tanyakan mana yang menang.
- sistem/sistem-undangan/02_PROFIL_JENIS_ACARA.md — kerangka yang akan kita isi
- sistem/sistem-undangan/03_TEMPLATE_DATA_ACARA.md — skema data per undangan (L3). L2 adalah
  DEFAULT-nya; L3 boleh kurang atau lebih.
- _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian A — riset baseline
  7 situs pasar undangan Indonesia SUDAH ADA di sana. PAKAI ITU. Jangan riset ulang dari nol,
  dan jangan mengusulkan fitur pasar yang risetnya belum pernah kita lakukan tanpa bilang bahwa
  itu usulan baru.

Jenis acara yang mau kita gali:
"[TULIS JENIS ACARANYA, dan apa pun yang sudah kamu bayangkan soal itu — boleh mentah]"

Pengalamanku sendiri dengan jenis acara ini (kalau ada):
"[TULIS: pernah membuat/menerima undangan jenis ini? apa yang menurutmu bagus, apa yang
menyebalkan?]"

Tugasmu BUKAN langsung menyimpulkan atau menulis dokumen. Gali bareng aku lewat diskusi dengan
aturan:

1. Ajukan pertanyaan klarifikasi 3-5 per giliran, jangan overwhelm aku.

2. Gali sampai kita punya jawaban jelas untuk:
   - DAFTAR FIELD DEFAULT info acara untuk jenis ini (nama penyelenggara, tanggal, jam, tempat,
     susunan acara, dst.). Tandai tiap field: WAJIB / OPSIONAL / TIDAK BERLAKU untuk jenis ini.
     Prinsip yang sudah dikunci: daftar ini ADAPTIF, tidak kaku — undangan konkret boleh kurang
     atau lebih. Jadi jangan membuat daftar yang memaksa client mengisi hal yang tidak ada.
   - VARIASI di dalam jenis acara yang sama. Contoh yang harus digali eksplisit: pernikahan bisa
     akad+pemberkatan+resepsi, bisa satu lokasi bisa dua, bisa berbeda agama/adat. Setiap variasi
     mengubah field dan mengubah etika penulisan. Tanyakan satu per satu, jangan dilewatkan.
   - KATA BAKU jenis ini. Misal "akad" vs "pemberkatan" vs "ijab kabul"; "khitanan" vs "sunatan"
     vs "tepong tawar"; "tasyakuran" vs "syukuran". Salah pilih kata di undangan = menyinggung
     keluarga, dan itu tidak bisa diperbaiki sesudah undangan tersebar.
   - KONVENSI DESAIN jenis ini: suasana yang diharapkan (khidmat/meriah/hangat/resmi), elemen
     yang lazim (ornamen, motif, foto), dan elemen yang PANTANG. Batasi usulanmu pada palet dan
     font L1 — kalau jenis ini butuh sesuatu di luar itu, laporkan sebagai benturan.
   - ETIKA & URUTAN: siapa yang disebut lebih dulu (keluarga mempelai pria/wanita, penyelenggara,
     pihak yang mengundang), cara menulis nama orang tua, cara menulis gelar, cara menyebut tamu,
     dan cara menulis permintaan kehadiran. Untuk acara keagamaan, tanyakan variasi antar-mazhab/
     antar-denominasi secara eksplisit — jangan anggap satu rumusan cocok untuk semua.
   - HAL KONSISTEN lintas undangan jenis ini (ini "hal konsisten #1" di rencana kerangka): apa
     yang SELALU sama di semua undangan jenis ini sehingga tidak perlu ditanyakan ke client.
   - WAKTU & SIKLUS: berapa lama sebelum acara undangan biasanya disebar, kapan client biasanya
     meminta revisi, dan apa yang biasanya berubah mendadak. Ini menentukan fitur mana yang harus
     bisa diubah sesudah tayang (berkaitan dengan G5 nanti).
   - KEBUTUHAN TEKNIS khusus: apakah jenis ini butuh peta lokasi, susunan acara per jam, galeri
     foto, ucapan/RSVP, hitung mundur, amplop digital, atau video. Untuk tiap yang dibutuhkan,
     tandai: bawaan L2 atau diminta per undangan.

3. Setelah tiap jawabanku, kasih insight tambahan — pola dari riset baseline bagian A, risiko
   yang biasa muncul di jenis acara ini, dan hal yang mungkin belum kepikiran olehku.

4. JANGAN memasukkan data satu undangan nyata ke dokumen L2. Kalau aku mulai menceritakan acara
   konkret ("nikahnya sepupuku bulan depan"), catat di "Catatan untuk L3" dan kembalikan diskusi
   ke level jenis acara.

5. Setiap beberapa putaran, kasih ringkasan checkpoint: "Sejauh ini profil [jenis acara] ini
   kelihatannya: ..." supaya kita selalu align.

6. JANGAN tulis dokumen final sebelum aku bilang "cukup, tulis draftnya". Ini gerbang G1,
   kategori BESAR — siapkan PR dan aku yang review isi lengkapnya sebelum merge ke main.

PENTING soal mekanika penulisan: dokumen ini masih kerangka dan validator sistem
(sistem/sistem-undangan/_sistem/validate_system.py) menuntut tiap dokumen kerangka memuat kata
KERANGKA dan bagian Log Keputusan. Saat menulis isinya, dalam commit yang SAMA: cabut banner
kerangka, perluas cakupan validator itu, perbarui Tahap/Versi di SYSTEM_MANIFEST.md + STATUS.md.

Setelah aku bilang cukup, rangkum mengikuti struktur di
sistem/sistem-undangan/02_PROFIL_JENIS_ACARA.md persis, satu bagian per jenis acara (jangan
menimpa jenis acara yang sudah ada — TAMBAHKAN), isi Log Keputusan dengan tanggal + alasan +
approval-ku, lalu commit, push, dan siapkan PR untuk aku review.
```

---

## Setelah selesai

1. Hasilnya tersimpan di `02_PROFIL_JENIS_ACARA.md` sebagai **satu bagian per jenis acara**, sudah lewat PR dan merge ke `main`, dan **G1 dinyatakan lulus oleh pemilik**.
2. Ulangi prompt ini untuk jenis acara berikutnya — **jangan** menggabungkan beberapa jenis dalam satu putaran diskusi; campurannya akan membuat kata baku dan etika saling menimpa.
3. Sesudah minimal satu jenis acara terisi, `03_TEMPLATE_DATA_ACARA.md` dan `04_TEMPLATE_BRIEF_UNDANGAN.md` bisa langsung dibuat sebagai template biasa (tidak perlu prompt Discovery — kolom "Cara diisi" di kerangkanya berkata begitu).
4. Benturan L1 vs L2 yang muncul selama diskusi **wajib** tercatat di Log Keputusan kedua dokumen, bukan hanya diselesaikan di chat.
