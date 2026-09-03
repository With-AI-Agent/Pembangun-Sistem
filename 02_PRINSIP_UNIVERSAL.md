# Prinsip Universal

### Prinsip-prinsip yang terbukti works di Sistem Konten Kreator (setelah 2 putaran audit menyeluruh), dipilah mana yang benar-benar lintas-domain vs mana yang spesifik ke konten kreator saja. Ini DEFAULT berlaku untuk sistem baru manapun — tapi boleh di-override di level `00_RENCANA_KERANGKA.md` sistem itu, asal dicatat alasannya secara eksplisit, bukan diam-diam diabaikan.

---

## Cara pakai dokumen ini

Dibaca sekali saat Discovery Level-0 sistem baru dimulai (lihat `01_DISCOVERY_LEVEL_0.md`), untuk memutuskan prinsip mana yang dipakai apa adanya, mana yang perlu disesuaikan, mana yang tidak relevan sama sekali untuk sistem itu. Setelah keputusan itu diambil, dicatat di bagian "Prinsip yang Dipakai / Di-override" pada rencana kerangka sistem tersebut — bukan diasumsikan otomatis semua berlaku tanpa dipikirkan.

---

## 1. Prinsip Hierarki

**Inti:** kalau sistem berbentuk BERTINGKAT, level yang sudah dikunci di atas WAJIB diwarisi oleh level di bawahnya — level bawah TIDAK BOLEH mengulang isi level atas, cukup merujuk, lalu menambahkan/meng-override yang spesifik di level itu saja.

**Syarat berlaku:** HANYA relevan kalau Discovery Level-0 sistem itu menjawab Bentuk Dasar-nya BERTINGKAT (atau gabungan yang mengandung unsur bertingkat). Kalau sistemnya FLAT murni, prinsip ini tidak berlaku — tidak perlu dipaksakan.

**Kenapa universal:** konsepnya generik — "keputusan besar dikunci sekali, keputusan turunan tidak mengulang tapi merujuk" — ini berlaku untuk hierarki APAPUN, tidak spesifik ke "Brand Core → Channel" saja.

---

## 2. Prinsip Rantai/Chaining

**Inti:** kalau sistem berbentuk SIKLUS (ada alur kerja berulang dengan beberapa tahap), agent membaca sendiri hasil tahap sebelumnya langsung dari repo dan melanjutkan ke tahap berikutnya — TIDAK perlu pengguna menyalin/menempel prompt manual antar tahap, karena semua terjadi dalam sesi kerja yang sama dengan akses baca-tulis repo langsung.

**Syarat berlaku:** relevan untuk sistem manapun yang punya bentuk SIKLUS (baik sebagai keseluruhan sistem, atau sebagai salah satu bagian dari sistem yang bertingkat).

**Titik approval WAJIB tetap ada:** meski agent melanjutkan sendiri, dia tetap harus berhenti di titik-titik yang termasuk kategori Besar (lihat Prinsip 3 di bawah) sebelum lanjut — bukan jalan terus tanpa jeda sampai akhir siklus.

**Kenapa universal:** ini soal cara kerja agent dengan repo (baca-tulis langsung, bukan copy-paste manual), bukan soal domain apa yang sedang dikerjakan.

---

## 3. Prinsip Approval Bertingkat

**Inti:** tidak semua hasil kerja butuh level pengawasan yang sama. Dibagi minimal 2 kategori:
- **Besar** — perubahan yang bisa menyebar dampaknya ke banyak bagian lain, atau susah dibalik kalau salah. WAJIB direview isi lengkapnya oleh pengguna sebelum di-merge.
- **Kecil** — perubahan yang dampaknya lokal dan gampang diperbaiki lagi nanti. Cukup dikonfirmasi ringan tanpa perlu baca detail.

**Syarat berlaku:** UNIVERSAL, berlaku ke sistem apapun. Yang BERBEDA per sistem adalah KRITERIA konkret apa saja yang masuk kategori Besar vs Kecil — itu harus ditentukan spesifik saat Discovery sistem itu (bukan disalin mentah dari kriteria sistem konten kreator, karena "konten produksi final" itu spesifik ke domain konten kreator).

**Kenapa universal:** prinsip "sebagian keputusan berisiko tinggi, sebagian rendah, dan keduanya butuh perlakuan review berbeda" berlaku ke semua jenis sistem kerja.

---

## 4. Prinsip Checkpoint & Verifikasi Konsistensi

**Inti:** untuk sesi kerja yang panjang/berlapis, ada 2 lapis pertahanan terhadap risiko agent "kehilangan jejak" dari yang sudah disepakati:
- **Checkpoint otomatis** — setiap pindah ke tahap besar berikutnya, agent berhenti sejenak dan meringkas ulang dengan membaca ulang sumber resmi (bukan mengandalkan ingatan sesi).
- **Perintah manual verifikasi** — pengguna bisa memanggil kapan saja untuk membandingkan hasil kerja terbaru dengan sumber resmi yang sudah dikunci.

**Syarat berlaku:** relevan kalau sistem itu punya sesi kerja yang BISA panjang/berlapis (misal siklus produksi dengan banyak tahap). Kalau sistemnya sederhana (misal cuma 1-2 tahap pendek), prinsip ini boleh disederhanakan atau tidak dipakai — jangan dipaksakan kalau menambah kerumitan tanpa manfaat nyata.

**Kenapa universal (dengan syarat):** risiko "agent melenceng di sesi panjang" itu berlaku ke sistem manapun yang memang punya sesi panjang — bukan spesifik ke produksi konten.

---

## 5. Prinsip Log Keputusan

**Inti:** setiap dokumen "hidup" (yang isinya bisa berubah seiring waktu) WAJIB punya tabel Log Keputusan sendiri — mencatat tanggal, apa yang berubah, dan ALASANNYA. Ini TIDAK digantikan oleh git history/commit message, karena keduanya beda level detail: commit message biasanya teknis dan singkat, Log Keputusan berisi alasan di balik keputusan itu.

**Syarat berlaku:** UNIVERSAL, berlaku ke semua dokumen hidup di sistem apapun.

**Kenapa universal:** alasan di balik prinsip ini (kebutuhan untuk memahami "kenapa" bukan cuma "apa yang berubah") tidak bergantung pada domain sistemnya.

---

## Prinsip yang TIDAK Universal (contoh, supaya jelas batasnya)

**Pemisahan Konsistensi Visual vs Non-Visual** — ini prinsip dari Sistem Konten Kreator yang SPESIFIK ke domain itu, TIDAK otomatis berlaku ke sistem lain. Prinsip ini soal jangkar visual (gambar referensi) vs jangkar teks (deskripsi + contoh) — cuma relevan kalau sistem yang dibangun memang melibatkan elemen visual yang harus konsisten. Sistem berbasis teks murni (misal beberapa jenis ruang belajar atau fondasi aplikasi) mungkin tidak butuh pemisahan ini sama sekali — tapi MUNGKIN SAJA butuh jenis "konsistensi" lain yang analog (misal konsistensi skema data, konsistensi gaya penilaian) yang perlu digali sendiri saat Discovery Level-0, bukan mewarisi definisi dari sistem konten kreator.

Ini dicantumkan sebagai contoh supaya jelas: **tidak semua yang terbukti works di 1 sistem otomatis jadi "universal"** — 5 prinsip di atas sudah dipilah khusus karena memang generik, prinsip lain yang tidak disebutkan di dokumen ini dianggap spesifik-domain kecuali dibuktikan sebaliknya lewat pemakaian nyata.
