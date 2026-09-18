# Status Pembangunan — Sistem Undangan (unit pembangunan sistem ini)

- **Status:** `kerangka` — **v0.2.0**, `Status Proposed`. Rencana kerangka **FINAL** (dikonfirmasi pemilik
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
  `PROMPT_ENTRI_UNIVERSAL.md`, sekaligus menutup temuan **R1** review independen PR #74 (validator
  mengeluarkan 2 peringatan karena pegangan belum ada). **Warning validator repo kini 0**, dicapai dengan
  **membuat pegangannya**, bukan dengan melonggarkan syarat "0 peringatan". Kedua berkas juga dimasukkan
  ke daftar wajib `_sistem/validate_system.py` (2 → 4 berkas) supaya **W-01 ditegakkan dari dalam folder
  sendiri** waktu sistem diunduh jadi repo tersendiri — sebelumnya hanya validator level repo yang
  menegur, dan validator benih yang dibangkitkan build_template.py ternyata **sudah lebih ketat** dari
  validator sistem nyata. **Diuji mutasi:** satu berkas manual dihapus → validator `exit 1` dengan pesan
  berkas mana yang hilang; dipulihkan → `exit 0`.
- **Tahap berikutnya:** (a) PR ini direview **L1** dan di-merge pemilik — **tanpa auto-merge**;
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
- **Waktu pembaruan:** 2026-09-18 — pegangan pengguna W-01 dibuat (menutup temuan R1 review PR #74); validator mandiri diperketat 2 → 4 berkas wajib
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
