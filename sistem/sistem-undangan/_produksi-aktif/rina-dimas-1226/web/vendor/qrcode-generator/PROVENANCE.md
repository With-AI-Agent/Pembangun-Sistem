# Provenance Pustaka Pihak Ketiga — `qrcode-generator`

Aturan yang dipatuhi: `01_IDENTITAS_PEMILIK.md` bagian 10 butir 4 (**lisensi = PERINGATAN, BUKAN BLOCK;
setiap aset dicatat provenance + status lisensi**) dan `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` bagian 7
(jalur sumber bahan: bahan berlisensi dengan provenance).

| Butir | Isi |
|---|---|
| Nama | `qrcode-generator` |
| Versi | `2.0.4` |
| Penulis/asal | kazuhikoarase — `https://github.com/kazuhikoarase/qrcode-generator.git` |
| Cara diperoleh | `npm pack qrcode-generator` di sesi 2026-09-21 (UTC) — paket diambil utuh dari registry npm, **tidak** disunting |
| Berkas yang di-vendor | `qrcode.js` (dist resmi paket, 56694 byte) |
| sha256 berkas yang di-vendor | `79ec86f82856005b1c887905cfccfcfbec3821ca61c7fd5a952faa5f778f791c` |
| Lisensi | **MIT** — dinyatakan di dua tempat: field `"license"` pada `package.json` **dan** header berkas yang di-vendor sendiri (*"Copyright (c) 2009 Kazuhiko Arase … Licensed under the MIT license"*) |
| Catatan kejujuran | **Berkas `LICENSE` terpisah tidak ikut** di dalam paket npm ini, tetapi **teks lisensi MIT ada di header berkas yang di-vendor** + field `package.json`. Jadi statusnya **jelas**, dan tetap dicatat di sini supaya sesi berikutnya tidak perlu menebak |
| Kenapa dipakai | Serah terima L1 bagian 8 item (4) mensyaratkan **gambar QR** untuk sebar; QR tidak boleh digambar ulang manual (dokumen 11 bagian 5a: kode harus tetap terbaca) |
| Dipakai di | `web/index.html` (QR tautan yang tampil di halaman) + `web/buat-qr.js` (menghasilkan `qr-sebar.svg`, QR **vektor** — tidak menambah aset raster) |
