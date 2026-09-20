# Spesifikasi Aset & Gerbang G3 Discovery — Prompt

### Dipakai **sekali** untuk mengunci dua tingkat aset (layar vs cetak) dan aturan gerbang **G3** yang fail-closed. Berbeda dari prompt Discovery lain: **angkanya sudah terukur dan tidak untuk digali ulang** — yang digali di sini adalah **keputusan berisiko yang belum diambil** (siapa menanggung apa, apa yang terjadi saat ditolak, bagaimana gerbang ditegakkan). Hasil akhirnya mengisi `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md`.

> **DRAF TERSTAGING** — lihat `README.md` di folder ini.

---

## Kapan pakai dokumen ini

Sesudah G0 (L1) terkunci dan **sebelum** satu pun aset undangan nyata dijanjikan ke client. G3
adalah gerbang yang bisa **menolak** aset, jadi ia harus ada lebih dulu dari produksi — kalau tidak,
penolakan akan terjadi di tengah jalan dan client sudah terlanjur dijanjikan.

---

## Prompt

```
Peran kamu: Asset-Spec Discovery Partner. Tugas kita mengunci dua tingkat aset (layar dan cetak)
dan aturan gerbang G3 untuk sistem undangan.

ATURAN PALING PENTING DI SESI INI: angka-angka G3 SUDAH TERUKUR dan sudah dikunci pemilik. JANGAN
menulis ulang dari ingatan, JANGAN menghitung ulang, dan JANGAN mengusulkan angka baru. Baca
sumbernya dan kutip:
- sistem/sistem-undangan/00_RENCANA_KERANGKA.md bagian 4.3, 4.4, 4.5
- _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian P (hasil uji)
- Log Keputusan 00_RENCANA_KERANGKA.md baris-baris bertanggal 2026-09-17 (malam) dan (final)
Kalau ada angka di dokumen yang bertentangan dengan sumber di atas, LAPORKAN bentrokannya —
jangan memilih sendiri mana yang benar.

Ringkasan yang harus kamu verifikasi ulang ke sumbernya sebelum dipakai (bukan pengganti sumber):
- Langkah 0: teks WAJIB di-render dari font, ornament/logo WAJIB vektor; hanya FOTO yang boleh
  raster. Status Langkah 0 = kesimpulan terukur, bukan pendapat: PSNR guratan tipis terukur
  20,8-22,6 dB untuk SEMUA metode yang diuji, di bawah ambang 32 dB milik repo sendiri.
- G3 punya TIGA hasil: LOLOS (>= 300 DPI) / LOLOS BERSYARAT (khusus fotografis, >= 200 DPI,
  upscale <= 1,5x, Lanczos4, cetak uji WAJIB) / DITOLAK.
- Ambang LOLOS BERSYARAT sudah DIPERKETAT dari >=150 menjadi >=200 DPI dan dari <=2x menjadi
  <=1,5x, berdasarkan pengukuran. AI upscaling sudah KELUAR dari jalur kritis dan diganti
  Lanczos4: keuntungan AI atas lanczos4 terukur hanya +0,28 sampai +0,55 dB dengan SSIM praktis
  identik, dan pada 1,5x AI lebih buruk di kedua metrik. EDSR OOM-kill, Real-ESRGAN butuh
  PyTorch, FSRCNN/ESPCN jalan 2-4 detik. Bonus yang tidak direncanakan: ketergantungan
  pip install hilang dari jalur kritis (pip install tidak bertahan antar sesi di lingkungan ini).

Yang kita gali adalah KEPUTUSAN BERISIKO yang belum diambil:

1. Ajukan pertanyaan 3-5 per giliran. Aku bukan orang teknis: jelaskan akibat tiap pilihan dalam
   bentuk "kalau ini dipilih, apa yang terjadi pada client dan pada tamu".

2. Gali sampai jelas:
   - DUA TINGKAT ASET: untuk tiap jenis aset (foto, ornament, logo, latar, teks), apa spesifikasinya
     di tingkat LAYAR dan di tingkat CETAK. Termasuk jawaban eksplisit: apakah satu berkas sumber
     bisa melayani keduanya, atau harus ada dua berkas sejak awal. Kalau harus dua, siapa yang
     membuatnya dan kapan.
   - DEFINISI "FOTOGRAFIS": apa yang masuk kategori ini sehingga boleh lewat jalur LOLOS
     BERSYARAT, dan apa yang tidak. Batas ini penting karena hanya kategori ini yang boleh
     di-upscale. Beri contoh nyata yang diputuskan (foto orang = ?, ilustrasi raster = ?,
     hasil render 3D = ?, screenshot = ?, foto yang sudah dikompres WhatsApp = ?).
   - NASIB ASET YANG DITOLAK: apa yang terjadi? dicari ulang dari client? diturunkan jadi
     layar-saja (tidak ikut cetak)? diganti ornament vektor? Siapa yang menanggung biayanya,
     dan bagaimana cara memberitahu client tanpa menyalahkannya. Keputusan ini harus diambil
     SEKARANG, bukan saat penolakan pertama terjadi.
   - CETAK UJI WAJIB: siapa yang mencetak, siapa yang membayar, apa yang dinilai pada hasil
     cetak, dan apa akibatnya kalau cetak uji gagal. Termasuk jawaban jujur: apakah sistem ini
     sanggup menjanjikan hasil cetak ke client, atau hanya menyerahkan berkas siap cetak.
   - CMYK: HTML-ke-PDF tidak bisa langsung CMYK (butuh Ghostscript) — fakta ini sudah tercatat
     di DISKUSI_MENTAH bagian H. Gali: apakah jalur cetak sistem ini memakai PDF/X lewat
     Ghostscript, atau menyerahkan berkas ke percetakan dan membiarkan mereka mengonversi, atau
     menunda kemampuan cetak. Jangan menjanjikan CMYK kalau jalurnya belum ada.
     Riset prepress yang sudah lengkap ada di bagian C 00_RENCANA_KERANGKA.md dan akan mengisi
     07_SPESIFIKASI_CETAK_PREPRESS.md (dokumen itu "cukup template", bukan Discovery).
   - SUMBER VEKTOR untuk ornament/logo: karena Langkah 0 mewajibkan vektor, sistem ini butuh
     persediaan ornament vektor. Gali: beli (lisensinya apa), gambar sendiri, konversi dari
     raster (PERHATIAN: gap skill vectorization masih terbuka — T-06 butir 9; hub skill yang
     tersedia mengisi upscaling tetapi TIDAK mengisi vectorization), atau minta client
     menyediakan. Jangan berasumsi kemampuan yang belum ada alatnya.
   - CARA G3 DITEGAKKAN: siapa yang menjalankan, dengan alat apa, kapan dalam SIKLUS, dan apa
     buktinya (berkas hasil? baris di log? foto cetak uji?). Gerbang yang tidak punya bukti
     pelaksanaan akan diklaim hijau tanpa pernah dijalankan — itu temuan yang sudah berulang
     di repo ini, jangan diulang di sini.
   - PERUBAHAN SESUDAH TAYANG: kalau client mengganti foto sesudah undangan tersebar, apakah G3
     dijalankan ulang, dan bagaimana tamu yang sudah membuka undangan lama dipengaruhi.

3. Setelah tiap jawabanku, kasih insight tambahan — risiko yang biasa muncul di percetakan nyata,
   dan hal yang biasanya baru ketahuan saat cetak pertama.

4. JANGAN memasukkan spesifikasi satu undangan nyata ke dokumen ini. Kalau aku mulai membahas
   foto client tertentu, catat di "Catatan untuk L3" dan kembalikan ke level sistem.

5. Setiap beberapa putaran, ringkasan checkpoint: "Sejauh ini aturan aset & G3 kita: ..."

6. JANGAN tulis dokumen final sebelum aku bilang "cukup, tulis draftnya". Ini kategori BESAR
   (isinya keputusan berisiko) — siapkan PR dan aku review isi lengkapnya sebelum merge.

PENTING soal mekanika penulisan: dokumen ini masih kerangka dan validator sistem
(sistem/sistem-undangan/_sistem/validate_system.py) menuntut tiap dokumen kerangka memuat kata
KERANGKA dan bagian Log Keputusan. Saat menulis isinya, dalam commit yang SAMA: cabut banner
kerangka, perluas cakupan validator itu, perbarui Tahap/Versi di SYSTEM_MANIFEST.md + STATUS.md.
Selain itu, karena dokumen ini memuat angka hasil pengukuran, tuliskan SUMBER tiap angka di
dalam dokumennya sendiri (bagian berapa, berkas apa) supaya angka itu bisa diaudit tanpa harus
membaca riwayat diskusi.

Setelah aku bilang cukup, rangkum mengikuti struktur di
sistem/sistem-undangan/06_SPESIFIKASI_ASET_DAN_RESOLUSI.md persis, isi Log Keputusan dokumen
dengan tanggal + alasan + approval-ku, lalu commit, push, dan siapkan PR untuk aku review.
```

---

## Setelah selesai

1. Hasilnya tersimpan di `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md`, sudah lewat PR dan merge ke `main`, dan **G3 dinyatakan lulus oleh pemilik**.
2. Setiap angka di dalamnya **punya sumber yang tertulis di dokumen itu sendiri** — ini yang membuat angka bisa diaudit tanpa membaca riwayat diskusi, dan yang mencegah penulisan ulang dari ingatan di sesi berikutnya.
3. `07_SPESIFIKASI_CETAK_PREPRESS.md` bisa langsung diisi sebagai template biasa (risetnya sudah lengkap di bagian C `00_RENCANA_KERANGKA.md`) — **tidak** perlu prompt Discovery.
4. Gap skill yang disentuh dokumen ini (**upscaling raster** terisi sebagian oleh `fal-upscale`, **vectorization** belum terisi sama sekali) tetap terbuka di daftar pekerjaan terbuka area master sebagai **T-06 butir 9**; pemasangan skill apa pun butuh persetujuan pemilik per butir.
5. Kalau pengukuran baru dilakukan sesudah dokumen ini terbit, hasilnya **menimpa** ringkasan di dokumen ini dan perubahannya dicatat di Log Keputusan — bukan diselipkan diam-diam.
