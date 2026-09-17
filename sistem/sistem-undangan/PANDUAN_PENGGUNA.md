---
agent_instruction: IGNORE for execution — USER GUIDE ONLY
---

# Pegangan Pengguna — Sistem Undangan

### Dokumen ini UNTUK KAMU sendiri — sengaja ikut masuk repo (dan ikut terbawa kalau sistem ini diunduh
### jadi repo tersendiri) supaya kamu selalu punya akses. **AGENT tidak boleh menganggap ini instruksi
### eksekusi kecuali kamu memintanya secara eksplisit.**

---

## 1. Apa ini, untuk siapa, dan hasil akhirnya apa

Sistem ini membuat **undangan untuk kebutuhan apa pun dan dalam format apa saja** — pernikahan, khitanan,
ulang tahun, webinar, sampai pengumuman usaha. Kamu **tidak perlu bisa coding dan tidak perlu paham
istilah teknis**: kamu menempel **satu prompt pembuka**, lalu agent yang menuntun — menanyakan info acara,
mengusulkan desain, membuat aset, merakit semua format, menerbitkan, lalu menyerahkan ke client. Agent juga
yang **melakukan riset** (bukan kamu), dan yang **membuat asetnya** (gambar, ornament, video). Hasil
akhirnya: **situs undangan yang tayang**, **berkas PDF siap cetak**, **video undangan**, atau ketiganya —
dan **satu situs induk** yang mengelola semua undangan yang pernah kamu buat. Seluruh rancangannya
ditargetkan **nol biaya bulanan**.

**Keadaan sistem ini hari ini — dibaca dulu, jangan dilewati:**

| | |
|---|---|
| **Tahap** | `kerangka` — **v0.1.0** |
| **Sudah ada** | Rencana kerangka **FINAL** (bentuk dasar dikunci pemilik), 11 dokumen domain **berbentuk kerangka**, folder bahan milikmu, validator mandiri, STATUS pembangunan |
| **BELUM ada** | **Isi** ke-11 dokumen itu. Artinya **sistem ini belum bisa memproduksi undangan sungguhan.** |
| **Tahap berikutnya** | Menulis 6 prompt Discovery detail (dokumen 01, 02, 05, 06, 09, 10), baru kemudian isinya |
| **Konsekuensi buatmu** | Panduan ini menjelaskan **alur yang akan kamu pakai** dan **aturan main yang sudah dikunci**. Kalau kamu menempel prompt pembuka hari ini, agent akan melaporkan terus terang bahwa sistemnya masih kerangka — itu **perilaku yang benar**, bukan kegagalan |

---

## 2. Prompt Pembuka Universal (Gunakan Ini SETIAP Sesi Baru)

Salin blok di bawah ke **chat pertama** — dalam keadaan apa pun (undangan baru, undangan lanjutan, revisi,
audit, cek status). Detail dan catatan pemakaiannya ada di `PROMPT_ENTRI_UNIVERSAL.md`.

```
Kamu adalah lmarena Agent yang terhubung ke repo sistem undangan ini.
Sebelum melakukan apa pun:

1. Baca `SYSTEM_MANIFEST.md`, `STATUS.md`, dan `00_RENCANA_KERANGKA.md` di akar sistem ini.
2. Deteksi kondisi branch saat ini (baru/kosong vs lama/sudah ada progres) dan cek working tree; JANGAN berasumsi sedang berada di branch utama.
3. Cek dan laporkan SEMUA PR yang masih terbuka di repo ini — dari sistem mana pun, bukan hanya sistem undangan.
4. Laporkan keadaan sistem ini dari `STATUS.md`: tahap (kerangka/berkembang/siap-pakai), versi, tahap terakhir yang selesai, tahap berikutnya, dan apakah ada pekerjaan yang belum tersimpan.
5. Baca `Input-Pengguna/README.md` dan laporkan apakah ada bahan milik pemilik yang sudah masuk tetapi belum diproses.
6. Cari file `LOG_SESI_*.md` terbaru (akar sistem ini, folder unit kerja, atau folder log sesi repo). Kalau keadaannya `OPEN`, BACA dan laporkan keadaan sesi sebelumnya SEBELUM bertanya tujuan sesi — jangan tanya ulang konteks yang sudah tercatat di sana.
7. Jalankan `python3 _sistem/validate_system.py` dan laporkan hasilnya APA ADANYA, termasuk peringatan atau kegagalan yang belum dibereskan. Jangan menghaluskannya.
8. Kalau tahap sistem masih `kerangka`, katakan terus terang bahwa sistem ini BELUM bisa memproduksi undangan, dan sebutkan apa yang sudah ada dan apa yang belum. Jangan berpura-pura siap.
9. Tanyakan: "Apa tujuan sesi ini?" (mulai undangan baru untuk client, lanjut undangan yang sudah ada, revisi desain atau aset, isi identitas pemilik L1, tambah profil jenis acara L2, siapkan terbit/cetak/serah terima, audit atau cek konsistensi, atau lainnya)
10. Berdasarkan jawaban, baca sendiri dokumen yang relevan (`01_IDENTITAS_PEMILIK.md` sampai `11_AMPLOP_DIGITAL.md`) — TANPA perlu aku tempel manual isinya.
11. Kalau melanjutkan unit kerja yang sudah ada, ikuti petunjuk pemulihan di `STATUS.md` unit itu; jangan mengulang kerja yang sudah tercatat selesai.
12. Jangan lewati gerbang G0 sampai G5. Gerbang berisiko BESAR (G0, G2, G5, dan perubahan apa pun pada data L1) wajib keputusan pemilik langsung dan TIDAK BOLEH diwakilkan ke agent.
13. Kalau ada data acara yang kurang, NYATAKAN bahwa data itu kurang. Jangan mengisi diam-diam dengan nilai karangan.
14. Jangan mulai eksekusi atau menulis file apa pun sebelum aku konfirmasi tujuan sesi ini sudah jelas.

Setelah itu, bawa aku langsung ke langkah yang tepat sesuai tujuan.
```

---

## 3. Prompt Penutup Sesi (Gunakan di Akhir Sesi)

Sebelum menutup sesi — kerja mau di-merge, mau dijeda, atau sesinya sudah panjang — tempel ini supaya sesi
berikutnya bisa melanjutkan tanpa kehilangan apa pun:

```
Tutup sesi ini dengan benar:
1. Update `STATUS.md` unit kerja yang disentuh: tahap yang selesai, tahap berikutnya, dan waktu pembaruan.
2. Tutup log sesi ini: file `LOG_SESI_*.md` milik sesi ini — isi final bagian "Keadaan Sesi" (yang sudah selesai, yang masih terbuka, langkah berikutnya) lalu tandai `CLOSED`. Kalau kerja belum tuntas, tandai `OPEN` dan tulis "dilanjutkan di mana".
3. Cek working tree: SEMUA perubahan wajib ter-commit dan ter-push. Tanpa itu, sesi baru tidak bisa melanjutkan — ini batasan platform, bukan pilihan.
4. Kalau ada undangan baru atau undangan yang selesai, pastikan folder unitnya lengkap (data acara + brief + spesifikasi desain + aset + keluaran) dan ikut ter-commit.
5. Pastikan bahan milik pemilik yang dipakai di sesi ini tercatat asalnya di `Input-Pengguna/README.md`.
6. Ringkaskan kondisi akhir: commit terakhir, status PR, dan langkah aman berikutnya.
7. Kalau aku mau merge PR: pastikan semua sudah ter-push SEBELUM merge. Sesudah merge atau close, sesi ini TIDAK BISA push lagi (batasan platform); kerja lanjutan harus dari sesi baru yang dibuka dari branch utama.
```

---

## 4. Istilah yang perlu kamu tahu (versi awam)

| Istilah | Artinya | Analogi |
|---|---|---|
| **repo** | folder proyek beserta seluruh riwayat perubahannya | satu lemari arsip yang menyimpan setiap versi dokumen |
| **branch** | salinan jalur kerja supaya perubahan tidak langsung menimpa yang asli | kertas salinan untuk dicoret-coret sebelum naskah asli diubah |
| **branch utama (`main`)** | jalur resmi; hasil yang sudah disetujui masuk ke sini | naskah final di lemari |
| **commit** | menyimpan satu perubahan sebagai satu titik di riwayat | menekan "simpan" dan memberi catatan apa yang berubah |
| **push** | mengirim commit dari ruang kerja ke penyimpanan bersama | mengunggah hasil simpanan ke lemari arsip pusat |
| **PR (pull request)** | usulan "gabungkan perubahanku ke branch utama" — tempat kamu memeriksa sebelum setuju | draf yang disodorkan untuk ditandatangani |
| **merge** | menyetujui PR dan memasukkan perubahannya ke branch utama | menandatangani draf jadi naskah resmi |
| **gerbang (G0–G5)** | titik di mana pekerjaan **dikunci** dan butuh persetujuanmu | tanda tangan di tiap tahap, supaya tidak ada yang lolos tanpa sepengetahuanmu |

---

## 5. Cara sistem ini disusun — 3 lapis (supaya kamu tahu mana yang diisi sekali, mana yang tiap kali)

| Lapis | Isinya | Seberapa sering kamu mengisinya |
|---|---|---|
| **L1 — Identitas & Preferensi Pemilik** | nama/merek usahamu, font & warna default, gaya ornament bawaan, bahasa & nada, kebijakan harga dan masa aktif, **rekening + QRIS statis** untuk amplop digital, kebijakan serah terima ke client | **sekali**, jarang diperbarui. Mengubahnya = risiko **BESAR** karena diwarisi semua undangan |
| **L2 — Profil Jenis Acara** | per jenis acara (pernikahan, khitanan, webinar, dst): daftar field info default yang **boleh kurang boleh lebih**, konvensi desain & etika per jenis, format keluaran yang lazim, kata-kata baku | **sekali per jenis acara**, lalu dipakai ulang |
| **L3 — Undangan Konkret** | satu client, satu acara: data nyata, desain final, aset, keluaran per format, daftar tamu dan tautan personal | **setiap kali membuat undangan** |

**Aturan yang mengikat agent:** satu undangan **boleh menyimpang** dari profil jenis acara atau dari
preferensimu, tetapi penyimpangannya **wajib dicatat beserta alasannya** di log keputusan unit itu —
**tidak boleh diam-diam**.

---

## 6. Tujuh tahap yang akan kamu lalui per undangan, dan di mana kamu harus bilang "ya"

| # | Tahap | Apa yang kamu lakukan | Gerbang di ujungnya | Risikonya |
|---|---|---|---|---|
| 1 | **Intake** | menempel prompt pembuka; menjawab pertanyaan agent; memilih jenis acara | **G0** — brief + jenis acara disetujui | **BESAR** |
| 2 | **Data Acara** | mengisi info acara; yang tidak kamu punya **dinyatakan kurang**, tidak dikarang | **G1** — data lengkap & valid | SEDANG |
| 3 | **Desain & Format** | memilih gaya; menaruh bahan milikmu (font, template, contoh); menentukan format yang dijanjikan | **G2** — desain & format dikunci | **BESAR** |
| 4 | **Aset** | menyetujui atau menolak hasil olahan aset | **G3** — aset lolos gerbang resolusi | SEDANG |
| 5 | **Rakit & Pratinjau** | memeriksa pratinjau di semua format dan ukuran layar | **G4** — pratinjau disetujui | SEDANG |
| 6 | **Terbit** | memutuskan tayang ke web, serah berkas cetak, atau render video | — | — |
| 7 | **Serah Terima & Rawat** | memastikan **kepemilikan akun client jelas**, cara revisi setelah tayang, masa aktif | **G5** — terbit/serah terima | **BESAR** |

**Kenapa tahap 6 dan 7 dipisah:** *Terbit* adalah tindakan teknis, *Serah Terima* adalah **perpindahan
kepemilikan akun dan tanggung jawab** ke client. Mencampur keduanya adalah cara paling umum client
kehilangan akses ke situsnya sendiri.

**Soal aset dan cetak (G3) — perlu kamu tahu karena ini yang paling sering bikin kecewa:** layar dan mesin
cetak punya kebutuhan yang **bertentangan**, jadi aset dibuat dalam **dua tingkat**. Untuk cetak, gerbangnya
menghasilkan tiga keputusan: **LOLOS** (memang sudah cukup tajam), **LOLOS BERSYARAT** (boleh dinaikkan
ketajamannya dengan cara tertentu, dan **wajib cetak uji dulu**), atau **DITOLAK** (jangan dipaksakan —
buat ulang). Aturannya sengaja ketat: **teks dan garis halus tidak boleh bergantung pada gambar hasil
pembesaran**, karena pembesaran tidak bisa memunculkan detail yang tidak pernah ada.

---

## 7. Bahan milikmu: taruh di mana, dan apa yang terjadi sesudahnya

| Bidang | Isi |
|---|---|
| **Apa** | Tempat kamu menaruh bahan milikmu sendiri — font, template, contoh undangan yang kamu suka, foto, logo, referensi gaya. **Mekanisme ini milikmu**, bukan milik agent |
| **Kapan** | kapan saja kamu punya bahan; paling berguna sebelum tahap Desain & Format (G2) |
| **Cara** | 1. Buka folder `Input-Pengguna/` di sistem ini. 2. Baca `Input-Pengguna/README.md` — di situ tertulis cara menamai dan menaruh bahan. 3. Taruh berkasnya, atau minta agent menaruhkannya dan sebutkan dari mana berkas itu berasal. 4. Kalau bahan itu punya lisensi atau batas pakai, **katakan** — agent tidak boleh menebak |
| **Sesudahnya** | agent melaporkan bahan apa saja yang masuk, lalu memakainya di tahap desain. Setiap bahan yang dipakai tercatat **asalnya** — jadi tidak ada aset yang muncul tanpa jejak |
| **Kalau gagal** | Gejala: agent memakai gaya yang tidak kamu minta, atau bertanya ulang bahan yang sudah kamu taruh. Langkah pertama: minta agent membaca ulang `Input-Pengguna/README.md` dan melaporkan daftar bahan yang terdeteksi **beserta asal-usulnya**, lalu bandingkan dengan yang benar-benar kamu taruh |

---

## 8. Kalimat Pembuka untuk Berbagai Situasi

Semua situasi di bawah dimulai dengan **prompt pembuka di §2**. Yang di sini adalah kalimat **lanjutan**
yang kamu tempel **sesudah** agent melaporkan keadaan repo. Bagian dalam tanda `[...]` **wajib kamu isi
dulu** sebelum menempel — kalau dibiarkan bolong, agent akan menebak.

### Situasi 1 — Mulai undangan baru untuk client

| Bidang | Isi |
|---|---|
| **Apa** | membuka satu unit undangan baru (lapis L3) dari nol |
| **Kapan** | ada client atau acara baru yang mau dibuatkan undangan |
| **Cara** | 1. Tempel prompt §2, tunggu laporan keadaan. 2. Tempel blok di bawah ini dengan `[...]` sudah diisi. 3. Jawab pertanyaan agent satu per satu. 4. Setujui atau tolak di **G0** sebelum lanjut |
| **Sesudahnya** | agent membuat folder unit kerja + brief awal, lalu menuntun pengisian data acara. Kamu akan diminta keputusan di G0 |
| **Kalau gagal** | Gejala: agent langsung membuat desain tanpa bertanya data acara, atau langsung melewati G0. Langkah pertama: tempel *"Berhenti. Kembali ke tahap Intake, tanyakan data acara dulu, dan jangan lewati G0."* |

```
Buat undangan baru. Client: [nama client]. Jenis acara: [pernikahan / khitanan / ulang tahun / webinar / lainnya].
Tanggal acara: [tanggal]. Format yang aku mau: [situs undangan / PDF cetak / video / kombinasi].
Baca dulu profil jenis acara yang cocok di L2, lalu tanyakan data acara yang kurang — JANGAN mengarang
data yang tidak aku berikan. Berhenti di G0 dan tunggu persetujuanku sebelum lanjut ke desain.
```

### Situasi 2 — Lanjutkan undangan yang sudah dikerjakan

| Bidang | Isi |
|---|---|
| **Apa** | menyambung unit kerja yang berhenti di tengah jalan, tanpa mengulang yang sudah selesai |
| **Kapan** | sesi sebelumnya ditutup, atau kamu pindah perangkat/sesi |
| **Cara** | 1. Tempel prompt §2 — agent akan mencari log sesi yang belum tertutup dan `STATUS.md` unit itu. 2. Tempel blok di bawah. 3. Periksa laporan "sampai di mana" sebelum menyuruh lanjut |
| **Sesudahnya** | agent melaporkan tahap terakhir yang selesai, gerbang terakhir yang sudah kamu setujui, dan langkah berikutnya — lalu lanjut dari situ |
| **Kalau gagal** | Gejala: agent mengulang tahap yang sudah selesai, atau tidak menemukan unitnya. Langkah pertama: tempel *"Baca STATUS.md unit [nama unit] dan sebutkan tahap terakhir yang tercatat selesai. Jangan kerjakan apa pun sebelum aku konfirmasi."* |

```
Lanjutkan undangan untuk [nama client / nama unit kerja]. Baca STATUS.md unit itu dan log sesi terakhir,
laporkan: tahap apa yang sudah selesai, gerbang apa yang sudah aku setujui, dan apa langkah berikutnya.
Jangan mengulang kerja yang sudah tercatat selesai, dan jangan lanjut eksekusi sebelum aku konfirmasi.
```

### Situasi 3 — Revisi desain atau ganti aset

| Bidang | Isi |
|---|---|
| **Apa** | mengubah tampilan atau mengganti bahan sesudah desain dibuat |
| **Kapan** | hasil pratinjau kurang pas, atau client minta perubahan |
| **Cara** | 1. Tempel prompt §2. 2. Tempel blok di bawah dengan perubahan yang **spesifik**. 3. Kalau perubahannya menyentuh hal yang sudah dikunci di **G2**, agent wajib memintamu mengunci ulang — jangan biarkan lewat |
| **Sesudahnya** | agent menyebut apa yang berubah, format apa saja yang ikut terpengaruh (karena satu sumber data menghasilkan banyak format), lalu menampilkan pratinjau ulang |
| **Kalau gagal** | Gejala: hanya satu format yang diperbarui sementara format lain masih memakai desain lama. Langkah pertama: tempel *"Sebutkan semua format yang dijanjikan di G2, lalu tunjukkan mana yang sudah memakai revisi ini dan mana yang belum."* |

```
Revisi undangan [nama unit]. Yang aku mau berubah: [sebutkan spesifik — mis. warna utama jadi hijau tua,
font judul diganti, foto sampul diganti dari bahan yang sudah aku taruh]. Sebutkan dulu apa saja yang ikut
terpengaruh di semua format, baru kerjakan. Kalau revisi ini mengubah hal yang sudah dikunci di G2,
katakan dan minta aku kunci ulang.
```

### Situasi 4 — Siapkan terbit, cetak, atau serah terima

| Bidang | Isi |
|---|---|
| **Apa** | menyiapkan keluaran akhir: tayang ke web, berkas siap cetak, atau paket serah terima ke client |
| **Kapan** | pratinjau sudah kamu setujui di **G4** |
| **Cara** | 1. Tempel prompt §2. 2. Tempel blok di bawah. 3. Untuk cetak: **minta laporan gerbang asetnya**, dan kalau ada yang berstatus LOLOS BERSYARAT, **lakukan cetak uji** sebelum mencetak banyak. 4. Untuk serah terima: pastikan **kepemilikan akun** sudah atas nama client sebelum G5 ditutup |
| **Sesudahnya** | agent menyiapkan artefak terbit + catatan versi, lalu meminta keputusanmu di **G5** |
| **Kalau gagal** | Gejala: hasil cetak terlihat pecah, atau client tidak bisa masuk ke akunnya sendiri. Langkah pertama: untuk cetak, minta *"tampilkan status gerbang resolusi tiap aset dan sebutkan mana yang LOLOS BERSYARAT atau DITOLAK"*; untuk akses, minta *"daftar akun apa saja yang dipakai, atas nama siapa, dan bagaimana cara client mengambil alih"* |

```
Siapkan [terbit web / berkas cetak / paket serah terima] untuk undangan [nama unit]. Tampilkan laporan
gerbang asetnya apa adanya. Untuk serah terima: daftarkan akun apa saja yang terlibat, atas nama siapa
sekarang, dan langkah pemindahan kepemilikan ke client. Jangan tutup G5 sebelum aku konfirmasi.
```

### Situasi 5 — Isi atau ubah identitas & preferensi pemilik (L1)

| Bidang | Isi |
|---|---|
| **Apa** | mengisi atau mengubah lapis paling atas: merek, font & warna default, rekening + QRIS untuk amplop digital, kebijakan harga dan masa aktif, kebijakan serah terima |
| **Kapan** | pertama kali memakai sistem ini, atau ada kebijakan yang berubah |
| **Cara** | 1. Tempel prompt §2. 2. Tempel blok di bawah. 3. Baca ulang ringkasan yang dibuat agent sebelum setuju — **ini risiko BESAR** karena diwarisi **semua** undangan |
| **Sesudahnya** | agent menulis dokumen identitas pemilik, mencatat perubahan di log keputusan, dan menyebutkan undangan mana saja yang ikut terpengaruh |
| **Kalau gagal** | Gejala: perubahan dipakai diam-diam ke undangan lama tanpa pemberitahuan. Langkah pertama: tempel *"Sebutkan unit mana saja yang mewarisi L1, dan tunjukkan mana yang berubah tanpa dicatat di log keputusan."* |

```
Aku mau [isi pertama kali / ubah] data L1: [sebutkan yang mau diisi atau diubah — mis. font default,
warna utama, rekening dan QRIS untuk amplop digital, masa aktif undangan, kebijakan harga]. Ringkas dulu
perubahannya, sebutkan undangan mana saja yang ikut terpengaruh, dan tunggu persetujuanku sebelum menulis.
```

### Situasi 6 — Audit atau cek konsistensi

| Bidang | Isi |
|---|---|
| **Apa** | memeriksa apakah isi sistem masih saling cocok — data vs desain vs keluaran vs yang dijanjikan |
| **Kapan** | sebelum terbit, sesudah perubahan besar, atau kalau kamu curiga ada yang tidak konsisten |
| **Cara** | 1. Tempel prompt §2. 2. Tempel blok di bawah. 3. Baca temuannya **sampai habis**, termasuk yang di luar dugaanmu — temuan di luar cakupan **wajib dilaporkan**, tidak boleh disaring |
| **Sesudahnya** | agent memberi daftar temuan berlabel (mana yang pasti, mana yang dugaan), tanpa langsung memperbaiki apa pun |
| **Kalau gagal** | Gejala: agent menjawab "semuanya konsisten" tanpa menunjukkan apa yang diperiksa. Langkah pertama: tempel *"Sebutkan berkas apa saja yang benar-benar kamu buka dan bandingkan, dan tunjukkan bukti per bandingannya."* |

```
Audit konsistensi undangan [nama unit / seluruh sistem]. Bandingkan data acara, spesifikasi desain yang
dikunci di G2, aset yang benar-benar dipakai, dan keluaran tiap format. Laporkan temuan apa adanya,
termasuk yang di luar yang aku minta — jangan disaring, jangan dihaluskan. Jangan perbaiki apa pun dulu;
menemukan bukan memperbaiki.
```

---

## 9. Cara Review & Merge

1. **Periksa isinya, bukan cuma judulnya.** Buka PR dan baca ringkasan perubahannya. Yang kamu cari: apakah
   yang dikerjakan **sama dengan yang kamu minta**, dan apakah ada klaim yang tidak disertai bukti.
2. **Minta review independen sebelum merge.** Katakan ke agent: *"bangkitkan prompt review untuk PR ini"*.
   Agent akan menghasilkan prompt siap tempel dari alat repo induk; kamu membukanya di **sesi agent lain**
   supaya yang menilai bukan yang mengerjakan.
3. **Tunggu verdict-nya, dan baca keputusannya.** Kalau verdict-nya menolak, **jangan merge** — perbaiki
   dulu. Kalau kamu mengerahkan beberapa hakim, aturannya: **selagi ada satu saja yang menolak, pekerjaan
   belum boleh dianggap lulus**. Hakim yang tidak menyerahkan laporan **tidak dihitung setuju**.
4. **Merge hanya kalau kamu setuju.** Tidak ada penggabungan otomatis di repo ini.
5. **Sesudah merge, sesi itu tidak bisa menyimpan lagi.** Kerja lanjutan harus dari **sesi baru** yang
   dibuka dari branch utama. Karena itu: **pastikan semua sudah ter-push SEBELUM merge** (lihat §3 butir 7).

**Yang perlu kamu waspadai:** PR yang isinya mengubah **alat penilai** (validator, alat uji, alat review)
punya **konflik kepentingan** — yang mengerjakan tidak boleh sekaligus yang memutuskan. Putuskan sendiri,
atau minta sesi lain menilai.

---

## 10. Perintah mesin yang mungkin kamu lihat agent jalankan

Kamu **tidak perlu** menjalankan ini sendiri; tabel ini supaya kamu bisa mengenali apa yang terjadi dan
tahu apakah hasilnya normal.

| Perintah | Fungsi | Kapan dipakai | Keluaran diharapkan | Kalau gagal |
|---|---|---|---|---|
| `python3 _sistem/validate_system.py` | memeriksa folder sistem ini sendiri: berkas wajib ada, butir warisan terdeklarasi, tahap tercatat | di awal sesi, sebelum commit, dan sesudah mengubah berkas sistem | baris `VALIDATOR SISTEM-UNDANGAN: PASS` disertai tahap, jumlah berkas yang diperiksa, dan jumlah butir warisan | kalau muncul `FAIL` atau daftar berkas hilang: **jangan commit**. Minta agent menyebut berkas mana yang hilang dan mengapa, lalu perbaiki berkasnya — **bukan** melonggarkan validatornya |

---

## 11. Kebiasaan yang Perlu Dijaga

- **Simpan di tiap tahap.** Setiap selesai satu tahap, perubahan di-commit dan di-push. Kerja yang tidak
  ter-push **tidak bisa dilanjutkan** oleh sesi baru.
- **Log sesi selalu segar.** Berkas `LOG_SESI_*.md` diperbarui setelah tiap pertukaran penting; bagian
  "Keadaan Sesi" di atasnya harus selalu menggambarkan keadaan terkini; di akhir sesi ditandai `CLOSED`.
- **Jangan lanjut kerja di sesi yang PR-nya sudah di-merge.** Buka sesi baru dari branch utama.
- **Kalau sesi mati mendadak**, sesi baru akan otomatis membaca log sesi yang belum tertutup. Kalau log
  itu tidak ada, cadangannya: unduh ruang kerja lewat perintah platform `/download-workspace`, lalu lanjut
  dari `STATUS.md`.
- **Jangan biarkan agent mengarang data.** Info acara yang tidak kamu punya harus dinyatakan **kurang**.
  Nama atau tanggal yang dikarang bisa tercetak di ratusan undangan.
- **Keputusan besar tetap di tanganmu.** G0, G2, G5, dan perubahan L1 tidak boleh diwakilkan.

---

## 12. Catatan kualitas — termasuk hal yang TIDAK boleh dinyatakan oleh penulis dokumen ini

- **Standar lulusnya pegangan ini bukan "sudah lengkap"**, melainkan: **"bisa dipakai orang awam tanpa
  bertanya lagi."**
- **Penulis dokumen ini DILARANG menyatakan standar itu terpenuhi.** Kelulusannya wajib dinilai oleh
  **sesi independen** memakai lensa kemudahan pakai (kacamata pengguna awam), dan yang lebih kuat lagi:
  **kamu menjalankan satu alur dari pegangan ini tanpa bertanya**. Kalau kamu harus bertanya,
  **standarnya belum lulus** — dan pertanyaanmu itu sendiri adalah temuan yang wajib dicatat.
- **Batas kejujuran:** agent bukan orang awam. Pemeriksaan oleh agent hanya menyaring cacat bentuk;
  kelulusan sesungguhnya tetap butuh manusia.
- Alat penjaring cacat pegangan di repo induk **bersifat penjaring kandidat, bukan pemberi putusan** —
  rasio positif palsunya terukur sekitar 65%, jadi setiap temuannya wajib dibaca di sumbernya sebelum
  dipercaya.
- **Pegangan ini lahir dari temuan review, bukan dari kenyamanan penulis.** Ia dibuat karena reviewer
  independen menolak kelulusan dengan alasan "syarat 0 peringatan tidak terpenuhi" sementara pegangan
  pengguna belum ada. Jalan yang dipilih adalah **membuat pegangannya sungguhan**, bukan melonggarkan
  syarat pemeriksanya.
- **Isi blok prompt di §2 wajib identik dengan isi `PROMPT_ENTRI_UNIVERSAL.md`** (dua file, satu sumber).
  Kalau salah satunya diubah, ubah keduanya lalu bandingkan.
- **Tidak ada tabel atau blok yang diduplikasi di dalam dokumen ini.** Setiap mekanisme dijelaskan di satu
  tempat, dan tempat lain menunjuk ke sana — salinan kedua pasti akan menyimpang.

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-18 | Pegangan pengguna dibuat pertama kali: §1 keadaan sistem dinyatakan terus terang masih `kerangka`, §2 prompt pembuka universal (identik dengan `PROMPT_ENTRI_UNIVERSAL.md`), §3 prompt penutup, §4 istilah awam, §5 tiga lapis, §6 tujuh tahap + enam gerbang, §7 bahan milik pemilik, §8 enam situasi (masing-masing dengan 6 bidang), §9 cara review & merge 5 langkah, §10 tabel perintah 5 kolom, §11 kebiasaan, §12 catatan kualitas | Butir warisan W-01 dan temuan **R1** review independen PR #74: validator mengeluarkan 2 peringatan karena pegangan pengguna belum ada, sehingga syarat penerimaan "lulus tanpa peringatan" tidak terpenuhi. Dua jalan tersedia: melonggarkan syarat pemeriksa, atau **membuat pegangannya**. Yang dipilih yang kedua — melonggarkan syarat alat penilai demi pekerjaan penulis yang belum selesai adalah pola menggeser gawang, dan pegangan pengguna justru inti tuntutan pemilik sejak awal. Ditulis mengikuti Standar Kelulusan Manual 5 syarat; **kelulusannya tidak dinyatakan di dokumen ini** karena penulis dilarang menilainya sendiri |
