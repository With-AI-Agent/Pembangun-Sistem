# Prompt Library

### Kumpulan teknik & prompt siap pakai yang bersifat GENERIK — dipakai lintas channel, dirujuk dari tahap manapun di `05_CONTENT_PRODUCTION_PIPELINE.md`. Ini "kotak perkakas" yang terus bisa ditambah seiring ditemukan teknik baru yang works.

---

## Cara pakai dokumen ini

Ini bukan dokumen yang dibaca urut dari atas ke bawah. Buka bagian yang relevan sesuai kebutuhan tahap produksi yang sedang dikerjakan. Tambahkan entri baru kapan pun ditemukan prompt/teknik yang terbukti works — supaya nggak perlu diketemukan ulang dari nol tiap kali.

---

## 0. Cara Agent Melanjutkan Antar Tahap (menggantikan Chain Instruction manual)

Setiap konten alur kerjanya bisa beda-beda (konten A butuh riset dulu sebelum naskah, konten B bisa langsung, konten C butuh karakter baru muncul di tengah jalan) — jadi pipeline nggak boleh kaku 1-2-3-4-5-6 yang harus disusun manual tiap kali.

**Karena agent bisa langsung baca-tulis repo, mekanismenya sekarang lebih langsung dibanding sistem versi copy-paste sebelumnya:** setelah menyelesaikan output suatu tahap, agent WAJIB:

```
1. TENTUKAN TAHAP SELANJUTNYA
   Berdasarkan output yang baru dibuat, tentukan tahap apa yang paling
   make sense untuk dikerjakan selanjutnya untuk konten spesifik ini.
   Boleh mengikuti urutan default di 05_CONTENT_PRODUCTION_PIPELINE.md,
   boleh juga menyimpang kalau konten ini butuh sesuatu yang berbeda
   (misal butuh riset tambahan dulu, ada tahap yang bisa dilewati, atau
   ada karakter baru yang muncul dan perlu dikunci dulu sebelum lanjut).
   Jelaskan singkat kenapa tahap itu yang paling pas berikutnya.

2. CEK TITIK APPROVAL
   Sesuai kategori Besar/Kecil (lihat 00_CARA_PAKAI_SISTEM.md) — kalau
   tahap yang baru selesai ini menghasilkan sesuatu yang termasuk kategori
   Besar (naskah final, breakdown yang akan dipakai generate asset, dst
   yang mengarah ke konten final), WAJIB berhenti dan minta konfirmasi
   pengguna dulu sebelum lanjut ke tahap berikutnya — jangan langsung jalan
   terus tanpa jeda.

3. LANJUTKAN, BUKAN SIAPKAN PROMPT UNTUK DI-COPY
   Begitu pengguna konfirmasi lanjut, EKSEKUSI LANGSUNG tahap berikutnya —
   baca sendiri konteks yang relevan (Channel Brief, Bank Konsistensi
   Visual, Model Konten Brief, hasil tahap sebelumnya), TIDAK perlu
   menyusun "prompt siap pakai untuk di-copy" karena tidak ada perpindahan
   platform. Kalau di output sebelumnya muncul karakter (baik yang bicara
   maupun yang diceritakan), bawa konteks itu otomatis ke tahap berikutnya.
```

**Checkpoint tambahan (lihat juga 00_CARA_PAKAI_SISTEM.md):** setiap kali pindah ke tahap besar berikutnya, ringkas ulang dulu apa yang sudah disepakati dengan membaca ulang sumber resmi — bukan mengandalkan ingatan sesi ini saja.

**Untuk Tahap Generate Asset (gambar):** mekanisme ini tetap berlaku untuk menentukan urutan generate yang disarankan, tapi outputnya berupa file gambar, bukan teks yang "melahirkan" instruksi lanjutan secara alami — cukup lanjut ke Tahap 6 setelah semua unit visual selesai digenerate.

**Kalau hasil suatu tahap ternyata jelek/tidak sesuai, dan mau ULANG tahap sebelumnya (bukan lanjut maju):**
Jangan lanjut maju — sebagai gantinya, gunakan pola ini di sesi yang sama:
```
Hasil tahap [SEBUTKAN TAHAP INI, misal "Breakdown Visual"] ini kurang
pas karena: "[JELASKAN APA YANG KURANG PAS]"

Tolong ulang tahap [SEBUTKAN TAHAP SEBELUMNYA YANG PERLU DIREVISI, misal
"Naskah"] dengan arahan tambahan: "[ARAHAN BARU]"
```
Agent membaca ulang hasil tahap sebelumnya langsung dari file yang sudah tersimpan di `_produksi-aktif/`, tidak perlu ditempel manual. Setelah tahap yang diulang itu selesai direvisi, mekanisme lanjut-maju di atas berlaku lagi.

---

## A. Konsistensi Karakter Antar Unit Visual (Shot/Section/Panel)

Masalah paling umum: karakter yang sama harus muncul di banyak unit visual berbeda (pose/ekspresi/environment beda-beda), tapi wajah & ciri khasnya harus tetap sama persis.

**Teknik dasar:**
```
[PROMPT MASTER KARAKTER dari Bank Konsistensi Visual — JANGAN diringkas/
ditulis ulang dari ingatan, copy persis]
+ [detail spesifik unit ini: pose, ekspresi, environment, lighting, angle]
```
Selalu taruh Prompt Master di depan, baru detail spesifik unit — supaya identitas karakter jadi "anchor" utama sebelum variasi.

**Sertakan file referensi visual:**
- Selalu sertakan file `acuan-utama.png` karakter (dari `konsistensi-visual/[nama-karakter]/referensi/`) sebagai referensi generate — agent bisa gabung sampai 10 file referensi sekaligus dalam 1 generate.
- Kalau unit ini butuh pose/ekspresi yang jauh beda dari acuan utama, sertakan juga `reference-sheet.png` kalau sudah ada.
- Kombinasikan dengan prompt teks untuk variasi pose/ekspresi/environment yang spesifik ke unit ini.
- Kalau hasil mulai "drift" (makin lama makin beda dari referensi setelah beberapa kali generate berturut-turut) — kembali generate dari file referensi ASLI, jangan pakai hasil generate sebelumnya sebagai acuan baru (supaya nggak makin menjauh).

---

## A2. Karakter Per-Konten (Tipe B) — "yang diceritakan", bukan permanen di channel

Beda dari Karakter Utama Channel (Tipe A, permanen, ada di Bank Konsistensi Visual), ini karakter yang muncul HANYA untuk 1 konten spesifik — misal tokoh dalam sebuah cerita yang dinarasikan, bukan host/karakter tetap channel itu sendiri. Dia tidak perlu didaftarkan permanen dari awal, tapi WAJIB konsisten dari awal sampai akhir konten yang sama, dan tetap disimpan sebagai jejak historis.

**Cara kerja:**

1. **Sebelum membuat deskripsi karakter Tipe B baru, cek dulu ke `channel-[nama-channel]/arsip-naskah/indeks-karakter.md`** — bukan `indeks.md`. `indeks.md` hanya memuat judul/tanggal/topik, jadi tidak memiliki data ciri karakter; `indeks-karakter.md` adalah satu-satunya sumber data yang memuat nama/sebutan, ciri ringkas, dan link ke arsip naskah sumber (formatnya ditetapkan di bagian 9 `03_TEMPLATE_CHANNEL_BRIEF.md`). Baca kolom **Ciri ringkas** untuk mencari karakter serupa; kalau ciri di indeks terasa kurang untuk memutuskan, buka arsip naskah sumber yang ditunjuk barisnya, jangan menebak.

   Kalau ada kandidat kecocokan, **tawarkan** untuk menaikkannya jadi Tipe A permanen (jalankan `04_CHARACTER_BUILDER_KIT.md`) sebelum lanjut, alih-alih membuat deskripsi Tipe B baru yang terpisah. Ini **bantuan agent, bukan deteksi otomatis yang pasti** — "mirip" tetap penilaian agent dan WAJIB dikonfirmasi pengguna sebelum diperlakukan sebagai karakter yang sama.

   Kalau `indeks-karakter.md` belum ada di channel ini (channel baru, atau arsip dibuat sebelum aturan ini berlaku), **buat file itu dulu** dengan format minimum dari bagian 9 `03_TEMPLATE_CHANNEL_BRIEF.md`, lalu lanjutkan. Jangan melewati langkah pengecekan diam-diam dengan alasan filenya tidak ada, dan jangan menyatakan "tidak ada karakter serupa" kalau yang terjadi sebenarnya indeksnya belum pernah dibuat — laporkan kondisi itu apa adanya ke pengguna.

2. Kalau memang karakter baru, begitu dia pertama kali muncul (biasanya saat Tahap Naskah atau Breakdown Visual), buat dulu deskripsinya secara ringkas tapi cukup detail untuk generate visual berulang — pakai format mini di bawah, JANGAN cuma disebut sekilas di narasi lalu dianggap "agent akan ingat sendiri":

```
KARAKTER PER-KONTEN: [nama/sebutan]
Fisik: [deskripsi ringkas tapi spesifik — cukup untuk prompt generate]
Peran dalam konten ini: [siapa dia, hubungannya dengan cerita/narator]
```

3. Deskripsi ini **WAJIB dibawa ke setiap tahap lanjutan** dalam konten yang sama (lihat bagian 0 di atas) — agent membaca ini dari hasil tahap sebelumnya yang tersimpan, tidak perlu ditempel manual ulang, tapi jangan biarkan "hilang" di tengah sesi produksi.

4. Generate 1 gambar acuan karakter ini di awal (unit visual pertama yang memunculkan dia), simpan sebagai file di `_produksi-aktif/[channel]-[judul-konten]/assets/`, lalu pakai gambar itu sebagai referensi untuk semua unit visual berikutnya yang melibatkan karakter ini dalam konten yang sama — sama seperti prinsip Karakter Utama Channel, cuma berlaku untuk 1 konten ini saja.

5. **Setelah konten ini selesai (Tahap 6):** deskripsi lengkap karakter Tipe B disimpan menempel ke arsip naskah konten yang memakainya (`arsip-naskah/[tanggal]-[judul].md`) — bukan file karakter mandiri terpisah. **Di tahap yang sama, WAJIB tambahkan/perbarui satu baris untuk karakter ini di `arsip-naskah/indeks-karakter.md`** (nama/sebutan, ciri ringkas, konten pertama, konten lain, status). Tanpa langkah ini, pengecekan di langkah 1 akan membaca indeks kosong dan karakter berulang tidak akan pernah terdeteksi — jadi baris indeks ini bagian dari "konten selesai", bukan pekerjaan opsional.

   Kalau karakter ini ternyata sudah punya baris di indeks (dipakai ulang), jangan buat baris baru — tambahkan konten ini ke kolom **Konten lain** pada baris yang sudah ada, lalu lanjut ke langkah 6.

6. **Kapan karakter Tipe B "naik kelas" jadi Tipe A (permanen):** kalau ternyata karakter ini dipakai lagi di konten lain (muncul lewat pengecekan langkah 1 dan sudah dikonfirmasi pengguna, bukan cuma disadari manual), itu tandanya dia harus dipindah jadi Karakter Utama Channel — jalankan `04_CHARACTER_BUILDER_KIT.md` untuk dia, hasilnya disimpan permanen di `konsistensi-visual/`, supaya konsistensinya terjamin lintas-konten, bukan cuma dalam 1 konten. Setelah naik kelas, ubah kolom **Status** barisnya di `indeks-karakter.md` menjadi `Naik ke Tipe A` beserta path elemen visualnya, supaya tidak ditawarkan naik kelas berulang kali di konten berikutnya.

---

## B. Konsistensi Voice/Gaya Bahasa dalam Naskah

**Teknik: sertakan "contoh negatif" bukan cuma "contoh positif"**
```
Gaya bicara karakter ini: [DESKRIPSI DARI VOICE PROFILE]

Contoh kalimat yang SESUAI gaya karakter ini: "[CONTOH]"
Contoh kalimat yang TIDAK SESUAI (terlalu formal/kaku/generic): "[CONTOH]"

Tulis [BAGIAN NASKAH YANG DIMINTA] dengan gaya seperti contoh yang sesuai,
hindari pola seperti contoh yang tidak sesuai.
```
Memberi contoh yang SALAH sama pentingnya dengan contoh yang benar — AI sering "default" ke gaya bahasa umum/formal kalau tidak ditegaskan hindarannya secara eksplisit. Contoh nyata dari naskah lama di `arsip-naskah/` channel ini bisa dipakai sebagai sumber contoh positif yang konkret.

---

## C. Riset & Validasi Ide

**Prompt cek "apakah ide ini sudah terlalu umum/generic":**
```
Ide konten ini: "[IDE]"
Niche channel: "[NICHE]"

Apakah ide ini termasuk jenis konten yang sudah SANGAT umum dibahas di
niche ini? Kalau iya, kasih 2-3 cara membuat angle-nya lebih unik/spesifik
supaya tidak terasa generic, TANPA keluar dari positioning channel ini.
```

**Cek pengulangan topik** (lihat juga Tahap 1 di `05_CONTENT_PRODUCTION_PIPELINE.md`): selalu cek ke `arsip-naskah/indeks.md` channel ini sebelum memfinalkan ide baru.

---

## D. Generate Gambar — Prompt Struktur Dasar (di luar konteks karakter)

Untuk unit visual yang tidak melibatkan karakter (establishing shot, b-roll, ilustrasi konsep untuk channel faceless) — atau untuk elemen Latar/Palet/Props dari Bank Konsistensi Visual:

```
Subjek/fokus utama: [APA]
Environment/setting: [DI MANA — sertakan file referensi dari
  konsistensi-visual/ kalau latar ini sudah dikunci]
Gaya visual: [SESUAI CHANNEL BRIEF BAGIAN GAYA VISUAL]
Mood/lighting: [BAGAIMANA]
Framing/angle: [BAGAIMANA]
Hal yang harus dihindari: [SESUAI CHANNEL BRIEF]
```

---

## E. Adaptasi Konten Antar Platform

Kalau 1 konten mau diadaptasi ke platform lain (misal versi panjang jadi versi pendek):

```
Konten asli (untuk platform [PLATFORM ASAL]):
"[NASKAH/KONSEP ASLI — bisa dibaca langsung dari arsip-naskah/ kalau
konten ini sudah pernah diproduksi sebelumnya]"

Adaptasikan untuk platform [PLATFORM TUJUAN], dengan mempertimbangkan:
- Durasi/panjang yang lazim di platform ini
- Gaya hook yang biasanya works di platform ini
- TETAP pertahankan Persona & Voice channel ini, jangan berubah jadi
  gaya platform yang generic
```

---

## F. Entri Baru (diisi terus seiring waktu)

*(Tambahkan di sini setiap kali menemukan prompt/teknik yang terbukti works dan layak dipakai ulang lintas channel. Format bebas, yang penting cukup jelas untuk dipakai ulang tanpa harus mengingat konteks penemuannya. Ini termasuk kategori Kecil — cukup konfirmasi ringan sebelum merge.)*

-
