# Panggung Bengkel (Rawat Inap) — Aturan Menginap

Folder ini adalah staging untuk run mode BENGKEL: salinan sistem target "menginap" di repo meta supaya agent bisa pakai tools dan arsip meta untuk rombakan berat.

Aturan keras (ringkasan — teks final di 01_ALUR_RUN saat dibangun):

1. Copy target masuk ke `_bengkel/<nama-target>/` HANYA di branch kerja sesi itu. TIDAK PERNAH di-merge ke `main` repo meta — repo meta tidak boleh bengkak oleh titipan (keputusan pemilik 11 Sep 2026).
2. Karena itu PR bengkel biasanya DI-CLOSE setelah hasil dipulangkan (bukan merged), kecuali ada bagian yang memang jadi milik meta (mis. temuan baru untuk katalog cacat, laporan ke `_arsir-run/` — hanya berkas laporan, bukan isi tamu).
3. Pemulangan hasil: download workspace / patch yang diterapkan pemilik di repo target. Sebelum close: semua commit sudah push (sesi tidak bisa push setelah PR merged/closed — fakta platform, bukan anjuran).
4. Kebijakan Lebur tetap berlaku penuh di bengkel — apa pun yang ditanam ke tamu ikut konvensi tamu, overwrite tetap per-item.
5. Branch yatim akibat sesi mati: dilaporkan, tidak dihapus diam-diam (pola pemilik: penghapusan branch = keputusan sadar).
6. Hygiene ukuran (K-9, pemilik 13 Sep 2026): salinan berisi HANYA yang dibedah (kerangka sistem + dokumen yang disentuh); aset besar (gambar/video/data) tidak ikut menginap — kerja aset dilakukan di repo target sendiri, daftar yang di-exclude dicatat di laporan diagnosis. Saluran ini bukan anti-bloat mutlak: branch yang di-push menempati store repo asal selama branch/PR hidup; karena itu pemulangan hasil disusul hapus branch (keputusan pemilik) dan PR di-close, dan karena itu pula bengkel adalah PENGECUALIAN ber-kuota sementara suntik default.

Status folder (14 Sep — sistem siap-pakai): masih kosong dari isi tamu — hanya README ini; tamu pertama menginap saat run bengkel pertama. Berkas `.gitkeep` tidak dipakai; keberadaan folder dijamin oleh berkas ini.
