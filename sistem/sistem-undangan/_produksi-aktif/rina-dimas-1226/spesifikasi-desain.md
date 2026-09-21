# Spesifikasi Desain — Unit Uji Coba `rina-dimas-1226`

> Keluaran **Tahap 3 (Desain & Format)** siklus — bahan review **G2** (kategori **BESAR**).
> Di unit uji coba ini, keputusan G2 = putusan pemilik 21 Sep 2026 (paket **E1–E4**): model
> **Modern minimalis**, format **web + flyer statis**. Semua nilai di bawah **diturunkan dari L1/L2**,
> bukan selera baru; penyimpangan dicatat di bagian 6 dan di `log-keputusan-unit.md`.

## 1. Model & Suasana

| Butir | Nilai | Asalnya |
|---|---|---|
| Model | **Modern minimalis** (`02` bagian 6, baris katalog: *netral + 1 aksen · Montserrat dominan · whitespace · nyaris tanpa ornamen*) | Putusan pemilik (G2) |
| Suasana | Tenang, lapang, formal-khidmat | `02` bagian 6 (akad = khidmat & tenang) |
| Prinsip visual | **Satu aksen saja**, garis tipis, tanpa motif ramai | L1 bagian 4 + `02` bagian 6 |
| Disiplin | maks **2 font** · maks **3 warna** · whitespace lega · footer konsisten | L1 (`02` bagian 6) |

## 2. Palet (3 warna, tepat di batas disiplin L1)

| Peran | Nilai | Catatan |
|---|---|---|
| Latar (bidang utama) | `#FAF7F2` (ivory) | default L1 |
| Teks (isi) | `#2B2B2B` (abu sangat gelap) | default L1 · **bukan** latar hitam dominan (pantangan `02` bagian 6 butir 2) |
| Aksen | `#B08D57` (emas tua) | default L1 · dipakai **hanya** untuk garis/judul kecil, bukan blok warna |

Tidak ada warna keempat. Warna status/kontras lain tidak diperkenalkan.

## 3. Tipografi (2 font — batas L1)

| Peran | Font | Ukuran | Catatan |
|---|---|---|---|
| Nama mempelai & judul bagian | **Playfair Display** | `clamp(1.75rem, 8vw, 3rem)` | font judul L1 |
| Isi & label | **Montserrat** | 1rem dasar, `clamp` untuk judul kecil | font isi L1; paling terbaca di HP |
| Angka/tanggal | Montserrat, `letter-spacing` kecil | — | tanggal & jam dibaca cepat |

**Penyimpulan teknis yang dinyatakan sadar:** font dimuat lewat **Google Fonts (woff2)** dengan
`display=swap` + fallback stack sistem (`ui-serif`, `Georgia`, `system-ui`, `Segoe UI`, `sans-serif`).
**Berkas font woff2 lokal + subset belum dibuat** — pembuatan subset ada di daftar gap skill
(vektorisasi/subsetting) yang **belum terpasang** (0 skill terpasang, T-06). Konsekuensinya jujur:
pada koneksi sangat lambat ada sesaat tampilan memakai font sistem, dan **undangan belum 100%
mandiri** soal font. Ini **bukan** kelalaian yang disembunyikan: tercatat di sini + Log Keputusan unit.

## 4. Struktur Halaman Web (urutan mengikuti `02` bagian 7 butir 1 — tidak diacak)

1. **Pembuka** — pembuka Islami (bentuk akad nikah) + salam
2. **Sapaan tamu** — default L1 *"Kepada Yth. Bapak/Ibu/Saudara/i"*; **personalisasi** dari parameter
   tautan `?tamu=Nama` (nama dibaca dari tautan, tidak diketik ulang per format)
3. **Mempelai** — nama lengkap kedua mempelai + tuan rumah (pola `orang_tua`) + **turut mengundang**
4. **Info acara per acara** — akad & resepsi: hari, tanggal, jam, **zona waktu ditulis**, venue,
   alamat, tautan peta (dua larik penuh — tidak ada larik yang menulis *"sama dengan …"*)
5. **Countdown** — target = mulai acara inti (`02` bagian 5)
6. **Susunan acara** — blok bawaan; detail terisi (keputusan unit, lihat Log Keputusan)
7. **Ucapan & doa restu + RSVP** — buku tamu publik (mode uji: penyimpanan sementara di perangkat,
   **ditandai di layar**)
8. **Dress code**
9. **Penutup + credit `Lee-Studio`** — kecil, tipis, memakai warna undangan sendiri, ≤10–15% bidang (L1 bagian 1)

**Amplop digital** tidak muncul karena datanya kosong (aturan `11` bagian 2 butir 2) — diuji, bukan
diabaikan. **Musik, galeri, streaming, QR check-in** tidak ada (Bagian B brief).

## 5. Format yang Dijanjikan (G2)

| Format | Berkas | Status |
|---|---|---|
| **Web** (responsif-adaptif semua layar) | `web/index.html` + `web/style.css` + `web/app.js` | **Ada** — pratinjau nyata |
| **Flyer statis portrait** | `web/flyer-portrait.svg` | **Ada** — dirender dari rekaman data yang sama |
| **Flyer statis landscape** | `web/flyer-landscape.svg` | **Ada** |
| **Teks WA siap salin** | dihasilkan halaman web (tombol salin) | **Ada** — dari rekaman, bukan ketikan manual |
| Video / cetak / story WA | — | **TIDAK dijanjikan** (dokumen 07/08 ditunda; `05` bagian 3) |

**Kenapa flyer dibuat SVG (bukan PNG/JPG):** teks di dalamnya tetap **teks dari font** dan
ornamentnya **vektor** — persis Langkah 0 (`06` bagian 1). Flyer SVG juga bisa dicetak/diperbesar
tanpa pecah, dan **tidak menambah aset raster** ke unit ini.

## 6. Penyimpangan yang Dinyatakan Sadar (aturan warisan L3 — tidak boleh diam-diam)

| # | Penyimpangan dari L1/L2 | Alasan | Boleh dikoreksi |
|---|---|---|---|
| 1 | Font dimuat dari CDN Google Fonts, **bukan** woff2 lokal tersubset | subsetting font = gap skill T-06 yang **belum terpasang**; menunggu keputusan pemasangan skill | Ya — sesudah skill font tersedia |
| 2 | Credit `Lee-Studio` ditulis **tanpa kontak** (WA/IG) | kontak studio masih *Belum Ditentukan* di L1 | Ya — begitu kontak ada |
| 3 | Ucapan/RSVP disimpan **sementara di perangkat tamu** | penyimpanan data runtime = keputusan dokumen 10 (TERBUKA, `09` bagian 11 butir 2) | Ya — sesuai hasil dokumen 10 |
| 4 | Susunan acara **terisi detail** | `02` bagian 5 (OPSIONAL) vs bagian 9 (BAWAAN) pernah bentrok; dokumen 03 sudah memutuskan **blok bawaan, detail dari client** → pada uji coba detail diisi pemilik sebagai operator | Ya — client nyata menentukan sendiri |
| 5 | Tanpa foto & tanpa musik | batasan uji coba (brief Bagian D) — bukan aturan baru | Ya — pada unit produksi |
