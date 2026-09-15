# Metadata produksi — Warung Kopi yang Pindah Tiga Kali

- **Model konten:** Kartu Teks 8–10 v1 (`Approved` — belum `Merged` saat produksi; lihat catatan di bawah)
- **Versi brief:** Channel Brief **v3**, Model Konten Brief **v1**
- **Prompt final:** **tidak ada** — konten teks-only, tidak ada satu pun prompt generate yang dipakai. Arahan penyampaian per kartu ada di `breakdown-output.md` (masih di folder produksi sampai G3)
- **Daftar asset:** **TIDAK ADA — 0 berkas.** Model ini melarang foto, ilustrasi, ikon, logo, gradien, tekstur, dan gambar hasil generate. Karena itu tidak ada SHA256 yang dicatat: memang tidak ada berkasnya
- **Spesifikasi visual (bukan asset):** latar solid `abu aspal` kartu 1–8 → `biru pudar` kartu 9; satu warna aksen per kartu (`kuning pagi`; kartu 6 `oranye lampu sodium`); nomor kartu `n/9`
- **Elemen konsistensi:** tidak ada (channel faceless; Bank Konsistensi Visual channel ini tidak mengunci elemen apa pun)
- **Karakter Tipe B:** **tidak ada** — pemilik warung tidak diberi nama maupun deskripsi fisik, jadi tidak memenuhi syarat dicatat di `indeks-karakter.md`. Pengecekan ke indeks (1 entri: Nenek Penjual Jagung Rebus) sudah dilakukan, tidak ada kecocokan
- **Sumber eksternal:** Tidak ada
- **Verifikasi batas model:** `cek-kartu.py` → 9 kartu (batas 8–10); kartu 1 = 12 kata (≤ 15); kartu 2–9 = 21/22/20/21/19/22/21/21 kata (18–28); total 179 kata (160–250); waktu baca ~72 detik. `HASIL: PASS`, `EXIT=0`. Skrip sudah diuji-mutasi (kartu 1 → 20 kata dan kartu 4 → 31 kata membuat skrip FAIL)
- **Verifikasi breakdown:** `cek_breakdown()` → 9 unit; 18 keterangan eksplisit `tidak berlaku — konten teks-only` (2 per kartu); 9 arahan aksen (tepat 1 per kartu); 0 kolom prompt/referensi yang terisi. `HASIL: PASS`. Sudah diuji-mutasi
- **Judul publish:** Warung kopi itu pindah tiga kali. Namanya tidak pernah ganti.
- **Caption:**

  > Ada warung kopi di satu sudut jalan yang sudah tiga kali pindah tempat. Namanya tidak pernah ganti. Papannya sama, catnya sama, cuma alamatnya yang bergeser pelan-pelan.
  >
  > Yang tidak ikut pindah hanya tiga hal: jam bukanya, gelasnya yang tebal, dan kebiasaan pemiliknya menyapa tanpa menunggu jawaban.
  >
  > Sudut seperti ini ada di dekat rumahmu juga. Biasanya tanpa nama, biasanya tidak diperhatikan.
  >
  > Lain kali kamu lewat situ, lihat pelan-pelan.

- **Hashtag:** `#sudutkota #ceritakota #kotayangsama #karteks #threadcerita #ceritapendek #tanpanama`
- **Thumbnail:** tidak ada (model teks-only; kartu 1 = sampul carousel / cuitan pertama thread)
- **Catatan produksi:**
  - Produksi pertama model `Kartu Teks 8–10` — model ini dibuat di sesi yang sama dan masih berstatus `Approved` (belum `Merged`) saat produksi dijalankan. Status itu dipertahankan apa adanya, tidak dinaikkan jadi `Operational` sebelum merge. Sesuai instruksi pemilik ("setelah model terkunci, produksi 1 konten") dan preseden PR #54 / PR #58.
  - Brand Core (`_sistem/01_BRAND_CORE.md`) masih berupa dokumen generator kosong, jadi rantai pewarisan Brand Core → Channel → Model bersifat formal, bukan substantif. Dicatat sadar.
  - Unit produksi ditempatkan di `_produksi-aktif/` root (pola pasca-housekeeping PR #57), sehingga di luar cakupan `validate_system.py` yang hanya memindai `_produksi-aktif` in-system. Gap tooling pra-ada, bukan disebabkan produksi ini.
  - Angka "tiga kali" dan "tiga hal" diperlakukan sebagai premis naratif warung fiktif tanpa nama, bukan klaim faktual yang dilarang Channel Brief bagian 3. Ide berasal dari Bank Ide Awal channel (bagian 7) yang sudah dikunci G2 2026-09-09.
