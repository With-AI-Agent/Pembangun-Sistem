# Status Pembangunan — Sistem Undangan (unit pembangunan sistem ini)

- **Status:** `isi-draft` — **v0.4.0**, `Status Draft`. Rencana kerangka **FINAL** (dikonfirmasi pemilik 17 Sep 2026; kategori **BESAR** → direview isi lengkapnya, bukan konfirmasi ringan). **Isi sistem: 2 dari 11 dokumen domain terisi** — `01_IDENTITAS_PEMILIK.md` (Discovery 01, 20 Sep 2026, **G0 LULUS — review isi lengkap oleh pemilik + PR #86 MERGED** (merge commit `36c63d4`, 20 Sep 2026 14:10 UTC; tanpa auto-merge)) dan `02_PROFIL_JENIS_ACARA.md` (Discovery 02, 20 Sep 2026 — jenis acara pertama **pernikahan**, cakupan umum; **G1 LULUS — putusan pemilik via merge PR #88, merge commit `f60e950`, 20 Sep 2026 16:48 UTC**; sifat putusan direkam jujur di log sesi slot 43 — approval isi butir-per-butir di chat, tanpa review dalam tersendiri, audit pasca-merge tersedia atas permintaan; benturan klasifikasi G1 antar-dokumen **dibiarkan pada keadaan tercatat** — tidak memblokir, bisa diselaraskan kapan pun lewat Log Keputusan dokumen 02) dan `03_TEMPLATE_DATA_ACARA.md` (roadmap b1, 20 Sep 2026 (UTC) — **template biasa**, penurunan dari field L2 pernikahan yang sudah G1 LULUS; **draft menunggu review isi PR** — tanpa auto-merge); 8 lainnya masih kerangka.
  17 Sep 2026; kategori **BESAR** → direview isi lengkapnya, bukan konfirmasi ringan). **Belum ada isi
  sistem**: 11 dokumen domain masih berupa kerangka.
- **Sistem:** Sistem Undangan — lihat SYSTEM_MANIFEST.md dan 00_RENCANA_KERANGKA.md di folder ini.
- **Tahap terakhir selesai:** **Discovery Level-0 tuntas 2026-09-17** — rencana kerangka ditulis, 7
  pertanyaan review dijawab/dikunci, bentuk dasar DIKUNCI (Bertingkat 3 lapis + Siklus 7 tahap), 6 gerbang
  G0–G5 dalam 3 tingkat risiko, **gerbang aset G3 diuji dengan angka** (bukan diperkirakan) yang
  menghasilkan **2 pembatalan keputusan oleh bukti**: Real-ESRGAN/EDSR gugur (EDSR **OOM-KILL** pada ukuran
  cetak A5@300) dan **AI upscaling dikeluarkan dari jalur kritis** karena terukur tidak memberi keuntungan
  pada foto, sedangkan satu-satunya jenis isi yang diunggulkannya (garis halus) justru dilarang Langkah 0.
  Ambang diperketat ≥150→≥200 DPI dan ≤2×→≤1,5×; implementasi `Lanczos4`. Folder sistem + manifest +
  skeleton + validator mandiri dibuat dalam **PR yang sama** (aturan M-14).
- **Tahap terakhir selesai (tambahan 18 Sep 2026):** **pegangan pengguna W-01 dibuat** — `PANDUAN_PENGGUNA.md` +
- **Tahap terakhir selesai (tambahan 20 Sep 2026):** **Discovery 01 (L1 Identitas Pemilik) tuntas** — 5 giliran
  diskusi dengan pemilik (prompt `_sistem/PROMPT_DISCOVERY_01_IDENTITAS_PEMILIK.md`; log sesi
  `_log-sesi/LOG_SESI_2026-09-20_42.md`): **13 butir terkunci** dengan approval per butir (nama **Lee-Studio** +
  credit kecil by default/premium hapus; prinsip kerja client-dulu; palet ivory+hitam+emas; font
  Playfair+Montserrat+Amiri — OFL; nada elegan-khidmat; harga fase portofolio + masa aktif 1 tahun; amplop =
  rekening/QRIS **client**; serah terima 5 item + revisi tak terbatas sebelum terbit; 0 skill terpasang; batasan
  mutlak + **lisensi = peringatan bukan block**; konsekuensi perubahan L1 + konfirmasi pemilik; **scope
  multi-acara + flyer**; biaya produksi per undangan **Rp 0** — terukur). Pengisian `01_IDENTITAS_PEMILIK.md` +
  **eksekusi T-69 dalam SATU commit**: banner kerangka dicabut, `_sistem/validate_system.py` diperluas
  (11 kerangka → 10 kerangka + 1 terisi; pemeriksaan banner/Log Keputusan/bagian isi wajib/konsistensi Tahap
  manifest — **diuji mutasi**), manifest v0.2.0→**v0.3.0** · Tahap kerangka→**draft** · Status Proposed→**Draft**,
  STATUS.md (berkas ini) diperbarui. Berikutnya: PR kategori **BESAR** (review isi lengkap pemilik, tanpa
  auto-merge) → **G0 dinyatakan lulus hanya oleh pemilik** (Syarat 4).
- **Tahap terakhir selesai (tambahan 20 Sep 2026, kedua):** **Discovery 02 (L2 Profil Jenis Acara — PERNIKAHAN) tuntas sampai draft** —
  diskusi 3 giliran dengan pemilik (prompt `_sistem/PROMPT_DISCOVERY_02_PROFIL_JENIS_ACARA.md`; log sesi
  `_log-sesi/LOG_SESI_2026-09-20_43.md`): cakupan **umum** (semua bentuk pengesahan), **semua variasi dicakup sejak awal**,
  approval per butir atas (a) kata baku & etika + titik sensitif selalu konfirmasi, (b) waktu & siklus (sebar digital
  H-30..H-14, reminder H-7..H-1, field wajib-ubah-setelah-tayang), (c) sortir fitur bawaan-L2 (11) vs per-undangan (9),
  (d) konvensi desain + 9 pantangan, (e) hal konsisten 9 butir, (f) field WAJIB 7/OPSIONAL 14/TIDAK BERLAKU per bentuk,
  terminologi default "Resepsi Pernikahan" + opsi "Walimatul Ursy", pendekatan antar-mazhab = kandidat kecil + pilihan per
  undangan; **KOREKSI pemilik terkunci:** katalog 8 model = *"sekedar pilihan otomatis ketika ga ada keterangan detail"* —
  bukan aturan kaku (diberlakukan umum ke seluruh isi L2 sebagai catatan agent, dinyatakan sadar). Butir "kurang paham"
  (kata baku, siklus) digali agent lewat riset web sesuai Prinsip Kerja Dasar L1 — sumber tercatum per bagian di dokumen 02.
  Pengisian `02_PROFIL_JENIS_ACARA.md` + **mekanika prompt 02 dalam SATU commit**: banner kerangka dicabut,
  `_sistem/validate_system.py` diperluas (10 kerangka → 9 kerangka + 2 terisi; bagian isi wajib 02 — **diuji mutasi**),
  manifest v0.3.0→**v0.4.0**, STATUS.md (berkas ini), baris Log Keputusan W-05 di `00_RENCANA_KERANGKA.md`. Berikutnya:
  PR kategori **BESAR** per prompt 02 (review isi lengkap pemilik, tanpa auto-merge) → **G1 dinyatakan lulus hanya oleh
  pemilik**. Sesudah G1 lulus: dokumen 03/04 bisa dibuat sebagai template biasa (prompt 02 "Setelah selesai" butir 3),
  dan/atau putaran jenis acara berikutnya.
- **Tahap terakhir selesai (tambahan 20 Sep 2026 (UTC), ketiga):** **ROADMAP b1 (1/2) — `03_TEMPLATE_DATA_ACARA.md` terisi** —
  **template biasa** (bukan dokumen generator — 00 bagian 7), diturunkan dari field L2 pernikahan yang sudah G1 LULUS:
  aturan satu-sumber (hal konsisten #1) + struktur rekaman + tabel field (WAJIB 7 · BAWAAN · OPSIONAL 14 · TIDAK
  BERLAKU — status mengikuti 02 §5/§9 apa adanya) + aturan adaptif (kurang = dinyatakan sadar, tidak ada nilai
  karangan) + field sensitif selalu konfirmasi + field wajib-ubah-setelah-terbit (02 §8 → G5) + validasi gerbang data.
  **Tidak ada keputusan baru pemilik**; dua keputusan agent dinyatakan sadar di Log Keputusan dokumen 03: (1) nama field
  teknis `snake_case` stabil; (2) **benturan status `susunan_acara` di dalam 02 dilaporkan** (§5 memasukkan rundown ke
  OPSIONAL 14, §9 ke BAWAAN 11) — diperlakukan "blok bawaan, detail opsional", pemilik boleh mengoreksi saat review.
  Mekanika satu commit: banner dicabut, `_sistem/validate_system.py` diperluas (9 kerangka → **8 kerangka + 3 terisi**,
  diuji mutasi **3/3** — banner dikembalikan MERAH, judul wajib diganti MERAH, baris Log Keputusan dihapus MERAH,
  pemulihan diff=0), manifest v0.4.0→**v0.5.0**, baris Log Keputusan W-05 di `00_RENCANA_KERANGKA.md`.
  **DRAFT menunggu review isi PR (tanpa auto-merge).**

  `PROMPT_ENTRI_UNIVERSAL.md`, sekaligus menutup temuan **R1** review independen PR #74 (validator
  mengeluarkan 2 peringatan karena pegangan belum ada). **Warning validator repo kini 0**, dicapai dengan
  **membuat pegangannya**, bukan dengan melonggarkan syarat "0 peringatan". Kedua berkas juga dimasukkan
  ke daftar wajib `_sistem/validate_system.py` (2 → 4 berkas) supaya **W-01 ditegakkan dari dalam folder
  sendiri** waktu sistem diunduh jadi repo tersendiri — sebelumnya hanya validator level repo yang
  menegur, dan validator benih yang dibangkitkan build_template.py ternyata **sudah lebih ketat** dari
  validator sistem nyata. **Diuji mutasi:** satu berkas manual dihapus → validator `exit 1` dengan pesan
  berkas mana yang hilang; dipulihkan → `exit 0`.
- **Koreksi keadaan peringatan (19 Sep 2026, append — temuan #2 hakim putaran 5 PR #74):** butir di atas
  menulis "**Warning validator repo kini 0**" sebagai klaim keadaan *sekarang*. Itu benar pada 18 Sep 2026
  ketika pegangan W-01 dibuat, tetapi **basi terhadap head PR #74 sekarang**: `python3 tools/validate_repo.py`
  mencetak `WARNINGS: 2`, keduanya di tier **berkas bukti historis yang append-only**
  (`sistem/sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md` baris 1870 dan 1956) — tier yang sah menurut
  keputusan pemilik 18 Sep 2026 (riwayat tidak disunting demi kosmetika tabel). Teks lama tidak dihapus;
  yang dikoreksi adalah kata "kini"-nya. **Peringatan di dokumen hidup tetap berarti butir ini belum lulus.**
  Butir ini dieksekusi sesudah pesan commit `4f819d9` keliru menyatakannya tidak berlaku — koreksinya
  dilaporkan terbuka di register T-53.
- **Tahap berikutnya:** (a) **SELESAI 20 Sep 2026 — PR #86 di-merge, G0 lulus (dinyatakan pemilik)**; (b) **SELESAI 20 Sep 2026 — G1 LULUS, PR #88 MERGED (`f60e950`)**. Berikutnya = **ROADMAP JALAN PRODUKSI PERTAMA** (tercatat di log sesi slot 43 `_log-sesi/LOG_SESI_2026-09-20_43.md` + disetujui pemilik): (b1) `03_TEMPLATE_DATA_ACARA.md` **terisi (draft — menunggu review isi PR)** + `04_TEMPLATE_BRIEF_UNDANGAN.md` menyusul di PR yang sama (sisa b1); (b2) Discovery 05/06/09 + isi dokumen 11; (b3) uji coba 1 undangan pernikahan (fiktif/sendiri) sampai terbit; (b4) terima client (fase portofolio L1). **Tunda sampai demand:** dokumen 07/08/10, T-63 (website pengelola/editor visual), putaran jenis acara berikutnya; (c) kelulusan pegangan W-01 belum dinilai (audit lensa kemudahan pakai + uji pemakaian nyata pemilik — Syarat 4); (d) buat `12_LOG_SESI.md` (W-02) + `QUALITY_ASSURANCE_AND_EVOLUTION.md` turunan (W-06); (e) **1 keputusan pemilik terbuka: lisensi Remotion** vs alternatif berlisensi longgar — data terukur 20 Sep 2026: **free license ≤3 orang membolehkan komersial** (studio 1 orang termasuk); keputusan final tetap milik pemilik sebelum `08_PIPELINE_VIDEO.md` diisi; (f) turunan mekanisme audit isi self-contained (W-10, item T-07); (g) item **"Belum Ditentukan" di `01_IDENTITAS_PEMILIK.md`** (rekening/QRIS/kontak pemilik; angka harga pasca-fase-portofolio) diisi saat momennya tiba — lalu tercatat di Log Keputusan dokumen 01; (h) **benturan klasifikasi G1** (prompt 02 BESAR vs manifest Kecil vs rencana kerangka bagian 4 gerbang produksi-Sedang) — **diputus pemilik (merge 20 Sep 2026): dibiarkan pada keadaan tercatat**, tidak diselaraskan sekarang; bisa dibuka kapan pun lewat Log Keputusan dokumen 02 (tidak memblokir).
  (b) sesudah merge: tulis **6 prompt Discovery detail** (dokumen 01, 02, 05, 06, 09, 10) — **bukan**
  langsung menulis isi sistemnya; (c) **SELESAI 18 Sep 2026** — pegangan pengguna W-01 sudah dibuat
  (lihat butir "tahap terakhir selesai" di atas); **yang masih kurang untuk naik ke `siap-pakai`: kelulusan
  pegangan belum dinilai** (Syarat 4 melarang penulis menilai sendiri → wajib audit lensa kemudahan pakai
  oleh sesi independen + uji pemakaian nyata oleh pemilik);
  (d) buat 12_LOG_SESI.md (W-02) dan QUALITY_ASSURANCE_AND_EVOLUTION.md turunan (W-06);
  (e) **1 keputusan pemilik masih terbuka: lisensi Remotion** vs alternatif berlisensi longgar
  (Motion Canvas MIT / HyperFrames Apache 2.0) untuk dokumen 08;
  (f) turunan mekanisme audit isi self-contained (W-10) — **belum ada di sistem anak mana pun**, item T-07.
- **Pekerjaan belum tersimpan:** Tidak ada
- **Waktu pembaruan:** 2026-09-20 (UTC, keempat) — **ROADMAP b1 (1/2): `03_TEMPLATE_DATA_ACARA.md` terisi** (template biasa, tanpa keputusan baru pemilik; draft menunggu review isi PR) + mekanika satu commit (validator 8 kerangka + 3 terisi, diuji mutasi 3/3; manifest **v0.5.0**). Sebelumnya (20 Sep 2026, ketiga) — **PR #88 MERGED (`f60e950`, 16:48 UTC): G1 pernikahan LULUS dinyatakan pemilik**; sync pasca-merge (register T-18, STATUS, manifest, INDEKS, log sesi slot 43 CLOSED) dijalankan di sesi yang sama — push pasca-merge terverifikasi HIDUP (preseden slot 41/42 terkonfirmasi lagi, terukur); PR admin kecil menyusul (preseden #87). Sesi berikutnya: lanjut roadmap butir (b1) — prompt siap-tempel tersimpan di log sesi slot 43. Sebelumnya (kedua): Discovery 02 tuntas sampai draft; `02_PROFIL_JENIS_ACARA.md` terisi (jenis acara: pernikahan, cakupan umum) — **v0.4.0**, Tahap tetap `draft`; mekanika prompt 02 dieksekusi (validator diperluas 9 kerangka + 2 terisi + manifest + STATUS, satu commit; diuji mutasi); **G1 menunggu review isi lengkap pemilik di PR**. Sebelumnya 2026-09-20: Discovery 01 tuntas, G0 LULUS (PR #86 merged `36c63d4`), T-69 dieksekusi. 2026-09-18: pegangan pengguna W-01 dibuat (menutup temuan R1 review PR #74); validator mandiri diperketat 2 → 4 berkas wajib.
  `arena/01a0ae7a-pembangun-sistem` (Discovery Level-0 + finalisasi rencana kerangka).
- **Risiko aktif:** (1) **pegangan pengguna sudah ADA (18 Sep 2026) tetapi kelulusannya belum
  dinilai dan log sesi (W-02) belum dibuat** — sistem ini **belum bisa dipakai** siapa pun sampai
  keduanya selesai, dan itu **syarat** naik Tahap, bukan pelengkap. Baris ini pernah membantah butir
  (c) di berkas yang sama ("belum ada" padahal (c) tercatat SELESAI) — temuan review independen
  putaran 2 PR #74. Yang kurang bukan berkasnya, melainkan PENILAIANNYA oleh sesi independen, karena
  Syarat 4 melarang penulis menilai sendiri; (2) **6 dokumen generator belum
  ditulis** — tanpa prompt Discovery detail, isinya akan lahir tanpa penggalian dan mengulangi kegagalan
  yang justru ditemukan di Discovery ini: **risetnya tercatat tetapi keputusan desainnya tidak**;
  (3) **ambang G3 diukur pada satu foto repo saja** — foto client nyata yang sudah terkompresi JPEG berat
  **belum diuji**, dan sumber ≥250 DPI serta font sungguhan belum diukur (font sistem kosong di platform
  ini); (4) **dependency penerbitan (Cloudflare) belum diuji dari lingkungan ini** — semua API eksternal
  terblokir, jadi deploy harus git-based; (5) **sinkronisasi master→turunan masih manual** untuk W-06/W-10.
