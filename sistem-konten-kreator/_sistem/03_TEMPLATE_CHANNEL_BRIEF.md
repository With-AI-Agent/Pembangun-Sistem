# Channel Brief — [NAMA CHANNEL]

### Ini dokumen "hidup" milik SATU channel. Hasil dari `02_CHANNEL_DISCOVERY_PROMPT.md` ditulis mengikuti struktur ini, disimpan sebagai `channel-[nama-channel]/channel-brief.md` di repo. **Ini dokumen yang WAJIB dibaca agent di setiap sesi produksi konten channel ini** (otomatis, lewat Entry Point Universal di `00_CARA_PAKAI_SISTEM.md`) — inilah "kunci" yang mencegah brand voice dan karakter berubah-ubah antar sesi.

---

## Status: [ ] Draft — masih digali  /  [ ] Terkunci — siap produksi

*(Ganti status ini jadi "Terkunci" setelah Channel Discovery selesai dan sudah di-merge ke `main`. Selama masih Draft — termasuk selama masih dalam bentuk PR yang belum di-merge — jangan mulai produksi konten dari brief ini, hasilnya akan berubah-ubah. Channel Brief termasuk kategori Besar, jadi WAJIB direview isi lengkapnya sebelum merge.)*

---

## 1. Identitas Channel

- **Nama channel:**
- **Platform utama:**
- **Format teknis:** [ ] Short-form  /  [ ] Long-form  /  [ ] Gambar & carousel  /  [ ] Campuran

*(Untuk pertanyaan "apakah channel ini pakai karakter atau tidak" — itu dijawab lengkap di bagian 4 di bawah, bukan di sini. Jangan isi ulang di sini supaya tidak ada 2 tempat yang bisa beda jawaban.)*

## 2. Niche & Positioning

- **Topik inti (sudut pandang spesifik, bukan cuma judul besar):**
- **Masalah/kebutuhan/hiburan yang dipenuhi buat penonton:**
- **Target penonton (kondisi/minat spesifik, bukan cuma demografi):**
- **Apa yang bikin channel ini beda dari yang sudah ada:**
- **Referensi/kompetitor yang relevan (untuk dipelajari, bukan ditiru):**

## 3. Persona & Voice Channel (WAJIB DIISI — berlaku untuk SEMUA channel, termasuk faceless)

*(Ini "suara" yang seolah bicara ke penonton — baik itu suara karakter tertentu, atau suara channel itu sendiri kalau tidak ada karakter yang bicara langsung. Ini SELALU ada, karena bahkan channel faceless tetap punya gaya bahasa/narasi yang konsisten. Jangan disamakan dengan Konsistensi Visual di bagian 4 — bagian ini urusan BAHASA & SUARA, bagian 4 urusan WUJUD/VISUAL. Bagian ini termasuk kategori "konsistensi non-visual" — cukup dijaga lewat deskripsi + contoh nyata dari arsip naskah, tidak butuh file gambar.)*

- **Siapa "suara" di balik channel ini?** [ ] Karakter tertentu yang bicara langsung (lihat Tipe A di bagian 4)  /  [ ] Narator/voice over tanpa wujud visual tetap  /  [ ] Tidak ada narasi bicara sama sekali (misal caption/teks saja)
- **Gaya bahasa:** (formal/santai/blak-blakan/puitis, dsb — beri contoh kalimat kalau bisa)
- **Tone emosional dominan:** (misal: hangat & suportif / tegas & provokatif / santai & lucu)
- **Kosakata/frasa khas yang sering dipakai:**
- **Karakteristik suara/voice** (kalau pakai text-to-speech — nada, kecepatan bicara, aksen, dsb; kosongkan kalau tidak relevan):
- **Hal yang HARUS ADA di setiap konten channel ini:**
- **Hal yang TIDAK BOLEH ADA / dihindari di channel ini:**
- **Contoh kalimat pembuka/penutup khas (kalau ada polanya):**

## 4. Konsistensi Visual

*(Ini urusan WUJUD — apakah ada elemen visual yang harus konsisten muncul berulang. Berbeda dari bagian 3 di atas: sebuah channel bisa punya Persona/Voice tanpa elemen visual apa pun (faceless murni), atau punya salah satu/semua elemen di bawah. Detail lengkap tiap elemen (termasuk file gambar referensi) disimpan di `channel-[nama-channel]/konsistensi-visual/`, dibangun lewat `04_CHARACTER_BUILDER_KIT.md`. Isi checklist di bawah eksplisit satu per satu — kalau tidak relevan untuk channel ini, tandai "tidak berlaku", jangan dilewatkan tanpa dipikirkan.)*

**Karakter — Tipe A (Karakter Utama Channel)** *(permanen, reusable lintas-konten — misal host virtual/tokoh utama tetap. Kosongkan/tandai "tidak berlaku" kalau channel ini tidak punya karakter utama tetap.)*

> Daftar karakter Tipe A channel ini: [nama-elemen di `konsistensi-visual/`] — lihat detail lengkap & rujukan gaya bicaranya di bagian 3 di atas.

**Karakter — Tipe B (Karakter Per-Konten)** *(karakter yang "diceritakan", bisa beda-beda tiap konten, TIDAK dicatat permanen di sini — disimpan menempel ke arsip naskah konten yang memakainya. Cukup wajib konsisten dalam 1 konten yang sama — caranya lihat bagian A2 di `06_PROMPT_LIBRARY.md`. Agent membantu memeriksa indeks karakter sebelum membuat karakter Tipe B baru; kalau ternyata dipakai berulang, akan ditawarkan naik kelas jadi Tipe A di atas.)*

*(tidak perlu diisi di sini — ini catatan pengingat saja bahwa jenis karakter ini ada dan cara kerjanya beda dari Tipe A)*

**Latar/Lingkungan** *(kalau channel ini punya setting yang konsisten berulang — misal selalu 1 ruangan/tempat yang sama. Tandai "tidak berlaku" kalau tidak relevan.)*

> [ ] Tidak berlaku untuk channel ini  /  [ ] Ada, lihat detail di `konsistensi-visual/[nama-latar]/`

**Palet Warna & Gaya Render** *(ciri khas visual channel ini secara keseluruhan — lihat juga bagian 5 di bawah untuk detail teknisnya.)*

> [ ] Tidak berlaku untuk channel ini  /  [ ] Ada, lihat detail di `konsistensi-visual/[nama-elemen]/` dan bagian 5

**Props/Objek Berulang** *(benda yang jadi ciri khas — misal 1 karakter selalu pegang benda tertentu.)*

> [ ] Tidak berlaku untuk channel ini  /  [ ] Ada, lihat detail di `konsistensi-visual/[nama-elemen]/`

## 5. Gaya Visual

- **Referensi visual/mood (deskripsikan, atau catat nama gaya seperti "anime 90an", "claymation", dsb):**
- **Palet warna dominan (kalau relevan):**
- **Pendekatan generate visual untuk channel ini:** (misal: langsung generate biasa / selalu pakai reference image dari `konsistensi-visual/` / kombinasi — ini BOLEH beda dari channel lain, tulis alasannya)
- **Hal yang harus dihindari secara visual:**

## 6. Area Berisiko Tinggi — hal yang gampang "ditebak ulang" beda oleh AI

*(Daftar eksplisit hal-hal yang paling gampang berubah/salah kalau agent nggak dikasih konteks penuh tiap sesi. Isi sesuai channel ini, contoh di bawah hanya ilustrasi. Ini juga jadi acuan konkret untuk perintah "cek konsistensi" — lihat `00_CARA_PAKAI_SISTEM.md`.)*

- Contoh: nama karakter sering ke-generate typo/beda ejaan kalau tidak eksplisit
- Contoh: gaya bicara karakter gampang jadi terlalu formal kalau prompt tidak menegaskan santainya
- (isi sesuai temuan aktual channel ini, tambah terus seiring waktu)

## 7. Bank Ide Awal

*(Ide-ide konten yang muncul selama Channel Discovery, belum diprioritaskan. Ini bahan mentah untuk tahap ideation di pipeline produksi, bukan daftar final. Ini termasuk kategori Kecil — perubahan di bagian ini cukup dikonfirmasi ringan sebelum merge, tidak perlu direview detail seperti bagian lain di dokumen ini.)*

-
-
-

## 8. Model Konten dalam Channel Ini

*(Channel bisa punya lebih dari 1 cara produksi/format — misal "animasi 60 detik" vs "gambar statis + narasi". Tiap model konten punya folder sendiri di `channel-[nama-channel]/model-konten/[nama-model]/`, lihat `07_MODEL_KONTEN_DISCOVERY_PROMPT.md`. Daftar di sini biar gampang dilacak dari Channel Brief ini.)*

| Nama Model Konten | Folder | Status |
|---|---|---|
| | | |

*(Kalau channel ini baru punya/akan punya 1 model konten saja, tetap disarankan dibuatkan Model Konten Brief-nya walau sederhana — supaya detail teknis produksi tidak numpuk di Channel Brief ini.)*

## 9. Arsip Naskah

*(Naskah final tiap konten yang sudah selesai/publish disimpan permanen di `channel-[nama-channel]/arsip-naskah/`. Folder ini wajib memiliki `indeks.md` untuk judul/tanggal/topik dan `indeks-karakter.md` untuk karakter Tipe B yang pernah dipakai. Indeks karakter harus menunjuk ke arsip naskah sumber. Ini berfungsi untuk: (1) mencegah pengulangan topik tanpa sadar, kecuali memang sengaja diulang dengan alasan jelas; (2) menjadi referensi nyata untuk menjaga konsistensi gaya bahasa; (3) memberi agent data yang benar-benar diperlukan untuk mendeteksi kemungkinan karakter Tipe B yang muncul kembali. Kemiripan tetap merupakan bantuan agent dan wajib dikonfirmasi pengguna, bukan jaminan klasifikasi otomatis.)*

**Format minimum `arsip-naskah/indeks-karakter.md`:**

| Nama/sebutan | Ciri ringkas | Konten pertama | Konten lain | Status |
|---|---|---|---|---|
| | | | | Tipe B / ditinjau untuk Tipe A |

## 10. Log Keputusan Channel

*(Mulai kosong, diisi terus selama channel berjalan. Setiap kali ada keputusan yang mengubah/menambah sesuatu yang sudah dikunci di atas — misal karakter berkembang kepribadiannya, gaya visual sedikit bergeser — catat di sini dengan tanggal, JANGAN biarkan perubahan itu cuma "diingat" di satu sesi kerja saja. Tabel ini TETAP dipertahankan meskipun ada git history — commit message dan Log Keputusan ini beda level detail, yang satu teknis singkat, yang satu berisi alasan.)*

| Tanggal | Keputusan | Alasan |
|---|---|---|
| | | |
