# Model Konten Discovery — Prompt

### Dipakai tiap kali mau menetapkan 1 "model konten" baru dalam sebuah channel — yaitu format/pendekatan produksi spesifik (misal: "cerita horor animasi 60 detik" vs "cerita horor gambar statis + narasi" dalam channel horor yang sama). Dijalankan di sesi lmarena Agent yang sama dengan repo (mode diskusi dulu, baru dieksekusi jadi file begitu matang). Hasil akhirnya mengikuti struktur di `08_TEMPLATE_MODEL_KONTEN_BRIEF.md`, disimpan di `channel-[nama-channel]/model-konten/[nama-model]/brief.md`.

---

## Kenapa level ini perlu ada, dan bedanya dengan Channel Brief

Channel Brief (`03`) menjawab pertanyaan besar: channel ini ngomongin apa, dengan suara/karakter seperti apa. Tapi channel yang sama bisa dieksekusi dengan **beberapa cara produksi yang sangat berbeda** — dan tiap cara itu punya kebutuhan teknis sendiri: gaya visual spesifik, struktur naskah khas, bentuk breakdown yang beda, bahkan durasi/ritme yang beda.

Kalau ini dicampur jadi satu di Channel Brief, hasilnya jadi kabur — "gaya visual channel ini apa" jadi sulit dijawab kalau channel itu punya 2 model konten dengan visual yang beda total. Model Konten Brief menjawab level yang lebih spesifik ini, sambil **mewarisi** apa yang sudah dikunci di level Channel (Persona/Voice, Konsistensi Visual) — jadi nggak perlu ditulis ulang.

**Ini juga tempat menentukan detail konkret Pipeline Produksi untuk format ini** (lihat prinsip "kerangka tetap, detail fleksibel" di `00_CARA_PAKAI_SISTEM.md`): kerangka 6 tahap tetap dipertahankan sebagai struktur umum, tapi bentuk konkret Tahap Breakdown (shot untuk video, section untuk infografis, panel untuk komik, dll) dan detail lain yang spesifik ke format ini ditentukan di sini.

**Penting — bukan cuma soal visual/teknis:** perbedaan antar model konten kadang bukan cuma di gaya visual, tapi di **struktur alur kerjanya sendiri**. Misal, "konten yang diekstrak dari buku motivasi jadi beberapa bahan konten" punya alur kerja yang beda TOTAL dari "konten murni dari pemikiran sendiri" — yang pertama ada tahap ekstraksi di depan yang menghasilkan banyak bahan sekaligus, yang kedua langsung 1 ide ke 1 konten. Dokumen ini menampung dua kemungkinan: model konten yang cuma beda DETAIL teknis dari pipeline standar, atau model konten yang butuh ALUR KERJA SENDIRI DARI NOL karena strukturnya memang beda dari akar.

**Aturan pewarisan:**
> Semua yang sudah dikunci di Channel Brief (Persona & Voice, Konsistensi Visual) OTOMATIS berlaku untuk semua Model Konten di channel itu, KECUALI kalau Model Konten Brief secara eksplisit menyatakan override (misal: variasi tone yang sedikit berbeda untuk format tertentu). Model Konten Brief TIDAK BOLEH mengulang isi Channel Brief — cukup merujuk, lalu fokus ke hal yang spesifik/beda di level ini.

---

## Kapan pakai dokumen ini

- Channel baru yang formatnya beragam sejak awal (sudah tau mau ada beberapa cara produksi)
- Channel yang sudah jalan dengan 1 model konten, lalu mau coba format eksekusi baru untuk channel yang sama
- Kalau channel ini sebenarnya cuma akan punya 1 cara produksi selamanya — Model Konten Brief tetap disarankan dibuat (walau singkat), supaya detail teknis produksi tidak numpuk jadi bagian Channel Brief yang harusnya level lebih tinggi

---

## Prompt

```
Peran kamu: Content Format Development Partner untuk konten kreator yang
membangun channel dengan bantuan agent intensif.

Sebelum mulai: baca channel-[nama-channel]/channel-brief.md dari repo ini
(terutama bagian Persona & Voice, dan Konsistensi Visual kalau ada).

Model konten yang mau dikembangkan untuk channel ini (boleh sangat mentah,
boleh sudah lumayan jelas):
"[TULIS APAPUN YANG ADA DI KEPALA SOAL MODEL KONTEN INI]"

Tugasmu BUKAN langsung menyimpulkan atau menulis dokumen. Gali lewat
diskusi (3-5 pertanyaan per giliran) sampai punya jawaban jelas untuk:

1. NAMA & DEFINISI model konten ini (singkat, jelas beda dari model
   konten lain di channel yang sama kalau ada)

2. FORMAT TEKNIS SPESIFIK:
   - Durasi/panjang pasti (bukan cuma "short-form", tapi misal "45-75 detik")
   - Struktur konten khas format ini (misal: hook-3 beat-twist-CTA, atau
     pola lain yang spesifik ke format ini)
   - Platform yang paling cocok untuk format spesifik ini

3. GAYA VISUAL SPESIFIK format ini (BUKAN mengulang Gaya Visual Channel
   kalau sudah ada di Channel Brief — ini yang KHUSUS beda di format ini):
   - Pendekatan visual (animasi/gambar statis/video real/motion graphic/dst)
   - Apakah elemen Konsistensi Visual channel ini (karakter Tipe A, latar,
     dst — kalau ada) tampil di format ini dengan cara yang sama seperti
     biasanya, atau perlu penyesuaian (misal karakter yang sama tapi
     digambar ulang gaya berbeda untuk format animasi vs format ilustrasi
     statis — kalau perlu, ini akan disimpan sebagai file tambahan di
     folder assets/ model konten ini, bukan mengubah Bank Konsistensi
     Visual aslinya)

4. GERBANG ALUR KERJA (PENTING — tanyakan ini secara eksplisit, jangan
   diasumsikan): apakah proses produksi untuk model konten ini mengikuti
   struktur kerangka 6 tahap standar (Ideation → Konsep → Naskah →
   Breakdown Output → Generate/Acquire Assets → Publish Prep, cuma beda di DETAIL
   teknis tiap tahap), ATAU strukturnya beda DARI AKAR — misal:
   - Ada tahap sebelum Ideation yang belum ada di alur standar (misal:
     mengekstrak/mengolah materi dari sumber eksternal seperti buku,
     artikel, video)
   - Prosesnya menghasilkan BANYAK bahan/calon konten sekaligus dari
     1 sesi kerja (bukan 1 ide → 1 konten seperti alur standar), yang
     masing-masing baru akan dieksekusi terpisah setelahnya
   - Ada tahap lain yang sifatnya sangat spesifik dan tidak ada
     padanannya di 6 tahap standar

   KALAU JAWABANNYA "beda dari akar" → JANGAN paksa masuk ke poin 5 di
   bawah (Variasi/Override tahap standar). Sebagai gantinya, alihkan ke
   MODE ALUR KERJA KUSTOM: gali dari nol, tahap demi tahap, urutan kerja
   yang sebenarnya untuk model konten ini, dengan pertanyaan seperti:
   - Dimulai dari apa (sumber/input awal)?
   - Tahap demi tahap apa saja yang dilalui sampai ada bahan/konten
     yang siap dieksekusi lebih lanjut?
   - Di titik mana proses ini "bertemu kembali" dengan kerangka standar
     (biasanya begitu 1 ide/bahan konkret sudah didapat, dari situ bisa
     lanjut Naskah → Breakdown Output → dst seperti biasa)?
   Gali ini selengkap Channel Discovery — jangan buru-buru, karena ini
   akan jadi pedoman kerja yang dipakai berulang-ulang.

   KALAU JAWABANNYA "sama seperti standar, cuma beda detail teknis" →
   lanjut ke poin 5 seperti biasa (override ringan per tahap).

5. VARIASI/OVERRIDE dari default (HANYA kalau di poin 4 dijawab "sama
   seperti standar"):
   - Apakah tone/voice di format ini SAMA PERSIS dengan Persona & Voice
     Channel, atau ada penyesuaian kecil khusus format ini (jelaskan
     kalau ada, ini yang disebut "override")
   - BENTUK KONKRET Tahap Breakdown untuk format ini (shot untuk video,
     section untuk infografis, panel untuk komik, atau bentuk lain yang
     sesuai format ini) — WAJIB dijawab eksplisit, karena ini yang dipakai
     agent tiap kali produksi konten dengan model konten ini
   - Tahap lain dari kerangka standar yang beda detail teknisnya untuk
     format ini (paling sering Tahap 5 Generate/Acquire Assets) — jelaskan tahap
     mana dan apa bedanya

6. CONTOH KONKRET: minta dibayangkan/diceritakan 1 contoh konten dari
   format ini secara singkat (dari awal proses sampai jadi), supaya bisa
   divalidasi apakah definisi/alur di atas sudah cukup jelas untuk
   dieksekusi ulang tanpa bingung.

Setiap beberapa putaran, kasih ringkasan checkpoint. Setelah dikonfirmasi
"cukup, tulis draftnya", rangkum jadi dokumen mengikuti struktur di
08_TEMPLATE_MODEL_KONTEN_BRIEF.md persis. PASTIKAN dokumen ini TIDAK
mengulang isi Channel Brief — cukup catat "mewarisi dari Channel Brief"
untuk hal yang sama, dan detailkan HANYA bagian yang spesifik/beda di
level model konten ini. Kalau hasil diskusi masuk MODE ALUR KERJA
KUSTOM, tulis alur itu selengkap dan sekonkret mungkin di bagian
"Alur Kerja Kustom" — ini akan menggantikan rujukan ke kerangka standar
untuk model konten ini.

Setelah draft ini dikonfirmasi final, buat folder
channel-[nama-channel]/model-konten/[nama-model]/ (kalau belum ada),
tulis hasilnya ke brief.md di folder itu, commit, push, siapkan PR untuk
direview sebelum merge ke main.
```

---

## Setelah selesai

1. Hasilnya tersimpan di `channel-[nama-channel]/model-konten/[nama-model]/brief.md`, sudah lewat PR dan merge ke `main`. Update juga tabel "Model Konten dalam Channel Ini" di `channel-brief.md` (bagian 8) supaya gampang dilacak.
2. **Kalau model konten ini pakai kerangka standar dengan override ringan** — pastikan override itu tercatat jelas di bagian "Override Ringan" di Model Konten Brief ini, supaya saat produksi harian, agent cek dulu file ini sebelum mengikuti default `05_CONTENT_PRODUCTION_PIPELINE.md` mentah-mentah.
3. **Kalau model konten ini punya Alur Kerja Kustom** — bagian "Alur Kerja Kustom" di Model Konten Brief ini yang jadi acuan utama saat produksi, BUKAN `05_CONTENT_PRODUCTION_PIPELINE.md`. Begitu alur kustom itu sampai di titik "sudah ada 1 ide/bahan konkret yang siap dieksekusi", baru dari situ boleh lanjut mengikuti tahap-tahap standar (Naskah → Breakdown Output → dst) seperti biasa — ini akan tercatat jelas di bagian "titik pertemuan" pada Alur Kerja Kustom.
4. Setiap produksi konten untuk model konten ini: Entry Point Universal (`00_CARA_PAKAI_SISTEM.md`) mewajibkan agent membaca Channel Brief channel-nya DAN Model Konten Brief ini — dua-duanya masuk daftar konteks wajib di tabel "Konteks Wajib per Jenis Sesi", tidak perlu ditempel manual.
