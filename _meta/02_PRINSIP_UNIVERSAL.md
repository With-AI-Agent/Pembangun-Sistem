# Prinsip Universal

### Prinsip-prinsip yang terbukti works di Sistem Konten Kreator (setelah 2 putaran audit menyeluruh), dipilah mana yang benar-benar lintas-domain vs mana yang spesifik ke konten kreator saja. Ini DEFAULT berlaku untuk sistem baru manapun — tapi boleh di-override di level `00_RENCANA_KERANGKA.md` sistem itu, asal dicatat alasannya secara eksplisit, bukan diam-diam diabaikan.

---

## Cara pakai dokumen ini

Dibaca sekali saat Discovery Level-0 sistem baru dimulai (lihat `01_DISCOVERY_LEVEL_0.md`), untuk memutuskan prinsip mana yang dipakai apa adanya, mana yang perlu disesuaikan, mana yang tidak relevan sama sekali untuk sistem itu. Setelah keputusan itu diambil, dicatat di bagian "Prinsip yang Dipakai / Di-override" pada rencana kerangka sistem tersebut — bukan diasumsikan otomatis semua berlaku tanpa dipikirkan.

**Batas dokumen:** prinsip di bawah mengatur *cara berperilaku* (bisa disesuaikan per sistem dengan alasan tercatat). Kewajiban *deliverable* yang tidak boleh hilang saat sistem baru dibangun — pegangan, LOG_SESI, field checkpoint deterministik, manifest, log keputusan, QA 3-lapis, fakta platform, approval, ringkasan cadangan — diatur terpisah di `03_KONTRAK_WARISAN.md` sebagai **default aktif** (override hanya via konfirmasi pengguna + tercatat). Kalau keduanya bertentangan, **kontrak warisan menang untuk SELURUH W-01…W-09 — termasuk butir yang hanya diverifikasi lewat proses/review manusia (mis. W-08 approval bertingkat)**, bukan hanya yang bisa dicek validator; prinsip tetap menjadi panduan perilaku untuk hal di luar daftar W. Bedakan dua hal: **penyesuaian cara penerapan** (bentuk artefak mengikuti domain, alasan tercatat di rencana kerangka) tidak perlu approval; **penonaktifan** butir tetap hanya via prosedur override kontrak (konfirmasi pengguna eksplisit + tercatat di manifest) — review PR #11 (F10).

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
- **Log sesi berkelanjutan (`LOG_SESI`)** — setiap sesi memelihara `LOG_SESI_YYYY-MM-DD.md` (format `TEMPLATE_LOG_SESI.md`), di-update + commit + push segera setelah tiap pertukaran yang menghasilkan informasi baru; header "Keadaan Sesi" selalu segar; ditandai `CLOSED` saat sesi berakhir. Filter anti-bising WAJIB (lihat protokol) — catat yang penting, bukan dump chat. **Alasan kausal:** Sesi lmarena bisa crash kapan saja (fakta platform #3 di `PLATFORM_LMARENA.md`) dan agent sesi baru tidak punya akses ke chat lama; hanya file yang bertahan. Menggantikan "checkpoint diskusi ringan >5 giliran" yang berbasis ambang (sebelum ambang, konteks sudah hilang).

**Syarat berlaku:** relevan kalau sistem itu punya sesi kerja yang BISA panjang/berlapis (misal siklus produksi dengan banyak tahap) ATAU dipakai via lmarena Agent Mode. Kalau sistemnya sederhana (misal cuma 1-2 tahap pendek) dan tidak dipakai via lmarena, prinsip ini boleh disederhanakan atau tidak dipakai — jangan dipaksakan kalau menambah kerumitan tanpa manfaat nyata. Untuk sistem yang dipakai via lmarena, prinsip ini **wajib** karena fakta platform: sesi bisa crash, dan setelah PR merge, sesi tidak bisa push lagi (tidak bisa, bukan jangan — lihat `PLATFORM_LMARENA.md`).

**Kenapa universal (dengan syarat):** risiko "agent melenceng di sesi panjang" itu berlaku ke sistem manapun yang memang punya sesi panjang — bukan spesifik ke produksi konten. Ditambah fakta platform lmarena (branch arena otomatis, loss push setelah merge, crash), maka checkpoint bukan cuma soal konsistensi, tapi syarat fisik supaya sesi baru **bisa** melanjutkan (mencegah FI-03).

---

## 5. Prinsip Log Keputusan

**Inti:** setiap dokumen "hidup" (yang isinya bisa berubah seiring waktu) WAJIB punya tabel Log Keputusan sendiri — mencatat tanggal, apa yang berubah, dan ALASANNYA. Ini TIDAK digantikan oleh git history/commit message, karena keduanya beda level detail: commit message biasanya teknis dan singkat, Log Keputusan berisi alasan di balik keputusan itu.

**Syarat berlaku:** UNIVERSAL, berlaku ke semua dokumen hidup di sistem apapun.

**Kenapa universal:** alasan di balik prinsip ini (kebutuhan untuk memahami "kenapa" bukan cuma "apa yang berubah") tidak bergantung pada domain sistemnya.

---

## Prinsip yang TIDAK Universal (contoh, supaya jelas batasnya)

**Pemisahan Konsistensi Visual vs Non-Visual** — ini prinsip dari Sistem Konten Kreator yang SPESIFIK ke domain itu, TIDAK otomatis berlaku ke sistem lain. Prinsip ini soal jangkar visual (gambar referensi) vs jangkar teks (deskripsi + contoh) — cuma relevan kalau sistem yang dibangun memang melibatkan elemen visual yang harus konsisten. Sistem berbasis teks murni (misal beberapa jenis ruang belajar atau fondasi aplikasi) mungkin tidak butuh pemisahan ini sama sekali — tapi MUNGKIN SAJA butuh jenis "konsistensi" lain yang analog (misal konsistensi skema data, konsistensi gaya penilaian) yang perlu digali sendiri saat Discovery Level-0, bukan mewarisi definisi dari sistem konten kreator.

Ini dicantumkan sebagai contoh supaya jelas: **tidak semua yang terbukti works di 1 sistem otomatis jadi "universal"** — 5 prinsip di atas sudah dipilah khusus karena memang generik, prinsip lain yang tidak disebutkan di dokumen ini dianggap spesifik-domain kecuali dibuktikan sebaliknya lewat pemakaian nyata.


## 6. Prinsip Quality Assurance & Evolusi

**Inti:** setiap sistem yang dibangun harus memiliki cara untuk memeriksa kualitas dirinya, memperbaiki diri berdasarkan bukti, dan memverifikasi outputnya. Prinsip ini terdiri dari tiga lapisan: meta-sistem terhadap dirinya sendiri, sistem domain terhadap dirinya sendiri, dan sistem terhadap output yang dihasilkan.

**Syarat berlaku:** default berlaku untuk semua sistem. Kedalaman audit disesuaikan dengan risiko. Lapisan atau bagian tertentu boleh di-override jika tidak relevan atau pengguna meminta secara eksplisit, tetapi override wajib dicatat beserta alasan, dampak, dan approval.

**Batas penting:** audit menghasilkan temuan atau proposal; audit tidak otomatis mengubah keputusan yang sudah dikunci. Perubahan mengikuti alur observasi → analisis → proposal → diskusi → keputusan → implementasi → verifikasi → rilis. Setiap perubahan harus memiliki bukti, regression check, versi, dan rencana rollback yang sesuai risikonya. Detail prosedur ada di `QUALITY_ASSURANCE_AND_EVOLUTION.md`.

**Kenapa universal:** semua sistem dapat mengalami drift, bug, perubahan kebutuhan, dan penurunan kualitas. Yang berbeda per domain adalah objek output, indikator kualitas, kedalaman pemeriksaan, dan cara rollback — bukan kebutuhan dasarnya untuk memiliki loop perbaikan yang terkendali.
