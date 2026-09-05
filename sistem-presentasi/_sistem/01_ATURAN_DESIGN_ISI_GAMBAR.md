# 01 — Aturan Desain, Kedalaman Isi, dan Gambar (Sistem Presentasi)

> **Dokumen instruksi AKTIF & SELF-CONTAINED.** Ini aturan yang benar-benar dipakai saat memproduksi deck. Ia sengaja berada **di dalam folder sistem** (bukan di `_meta/`) karena setiap sistem akan diunduh dan dipakai sebagai repo standalone. Rujukan `_meta/` di sini hanya *provenance*.
> Pelajaran nyata dari deck #1 (tesis fikih hiasan wanita, 5 Sep 2026) sudah dimasukkan ke sini.

## A. Kedalaman Isi (menjawab "isi terlalu ringkas")
1. **Mulai dari temuan/kesimpulan, bukan metode.** Audiens sidang ingin hasil dulu; metode cukup 1–2 slide.
2. **Jangan over-summarize.** Tiap bullet = kalimat utuh yang bermakna, boleh dua klausa. Hindari bullet 2–3 kata yang kehilangan substansi.
3. **Isi substantif sebanyak bahan memungkinkan.** Bila bahan memuat rincian (daftar, perbandingan, dalil), muat rincian itu (boleh sub-bullet), bukan hanya judulnya.
4. **Jejak sumber wajib** di tiap slide (nomor halaman/URL), kecil di footer.
5. **Jumlah slide mengikuti kebutuhan isi**, bukan dipaksa ringkas. Rentang umum 12–18 untuk 10–15 menit; lebih banyak slide dengan isi penuh lebih baik daripada sedikit slide padat-terpotong.
6. **Naskah pembicara masuk Notes**, bukan slide (anti-redundancy).

## B. Desain (menjawab "desain terlalu ringkas/belum jadi")
1. **Tipografi minimum:** judul 34–40pt, isi 24–26pt, footer 14–16pt. Jangan di bawah itu.
2. **Isi terpusat vertikal** (`vertical_anchor=MIDDLE`) agar tidak ada ruang kosong menganga.
3. **Identitas konsisten tiap slide:** footer bar penuh-lebar (nomor slide angka-Arab + jejak sumber) + spine sisi-kanan dua-warna (dominan + aksen). Slide judul diberi bingkai aksen.
4. **Palet:** dominasi gelap-tenang + aksen hangat + latar terang; kontras ≥ WCAG AA. Default deck#1: hijau `#0F3D2E` + emas `#C9A227` + krem `#F7F3E9`.
5. **Koherensi (Mayer):** jangan ada ornamen yang tidak membawa makna; gambar dekoratif hanya sebagai aksen brand yang sangat muted, bukan hiasan ramai.
6. **RTL untuk Arab:** `rtl=1`, `algn=right`, font complex-script (`a:ea`/`a:cs`), shaping diserahkan ke PowerPoint.

## C. Gambar — mekanisme MULTI-MODE (wajib tawarkan & catat)
Mode (pilih per deck, boleh campur per slide):
- **M0** tanpa gambar (teks+struktur). Default aman.
- **M1** gambar dari bahan pengguna (jika ada).
- **M2** struktur/diagram/tabel dibangun agent (bukan foto; bebas lisensi). Dianjurkan untuk perbandingan/alur.
- **M3** gambar AI (generate_image). **Wajib**: tanpa teks di dalam gambar; hanya aksen/ilustrasi; diberi label "ilustrasi AI" bila tampil; tidak boleh menggambarkan data/klaim.
- **M4** gambar internet. **Wajib** cek lisensi per gambar + `DAFTAR_GAMBAR.md`; bila lisensi tak terverifikasi, tolak.

**Dua batasan keras (dari pengguna):**
1. **Teks tidak boleh dibakar ke gambar.** Bagian yang mungkin diubah harus tetap teks PowerPoint yang bisa diedit (Aturan G-1).
2. **Gambar tidak harus penuh.** Gambar boleh ditempatkan **parsial** pada area/ukuran tertentu (geometri eksplisit: x,y,w,h), mis. aksen pojok atau pita sisi.

Setiap gambar (M1/M3/M4) wajib tercatat di `DAFTAR_GAMBAR.md`: mode, sumber/lisensi, geometri, alasan.

## D. Portabilitas (menjawab alur "dijadikan repo sendiri")
1. Semua aset & aturan dipakai berada di dalam folder sistem; skrip build tidak mengimpor dari `_meta/`.
2. `build_deck*.py` + `export_html.py` harus reproducible: install lib ke target lokal, jalankan, hasil ke `keluaran/`.
3. Setelah deck jadi, folder deck (bahan+doc+keluaran+skrip) harus bermakna penuh bila dipindahkan sendirian.

## E. Verifikasi sebelum diajukan
1. Baca-balik `.pptx` (struktur, rtl, font, tabel, notes).
2. Render preview HTML hampiran.
3. **Buka hasil secara visual** (preview/PowerPoint) dan nilai desain+isi — bukan hanya cek struktur. (Deck#1 gagal di sini: struktur lulus tapi tampilan dinilai kurang.)

## Log Keputusan
| Tanggal | Keputusan | Dasar | Oleh |
|---|---|---|---|
| 2026-09-05 | Dokumen ini dibuat; aturan A–E ditetapkan dari umpan balik deck#1 | Keluhan pengguna + pelajaran | agent |
