# Template Data Acara

> **STATUS: ISI — DRAFT.** Diisi 2026-09-20 (UTC) lewat **ROADMAP JALAN PRODUKSI PERTAMA,
> butir b1** (handoff log sesi slot 43; sesi slot 44) sebagai **template biasa** per
> `00_RENCANA_KERANGKA.md` bagian 7 (*"cukup template"* — bukan dokumen generator).
> **Semua isi di dokumen ini = penurunan dari isi yang sudah di-approve pemilik**:
> field L2 pernikahan (**G1 LULUS**, `02_PROFIL_JENIS_ACARA.md`), aturan satu-sumber
> (`00_RENCANA_KERANGKA.md` hal konsisten #1 + bagian 2.3 Tahap 2), siklus waktu
> (02 bagian 8), dan kebijakan L1 (`01_IDENTITAS_PEMILIK.md` — format keluaran,
> batasan mutlak, amplop digital). **Tidak ada keputusan baru pemilik di dokumen ini**;
> keputusan agent (nama field teknis, status rundown) dinyatakan sadar di Log Keputusan
> di bawah dan **boleh ditolak/dikoreksi** saat review PR (PR normal, tanpa auto-merge).
> Banner kerangka dicabut di commit yang sama dengan perluasan validator
> (mekanika T-69/prompt 02).

| | |
|---|---|
| **Berkas** | `03_TEMPLATE_DATA_ACARA.md` |
| **Lapis** | L3 — Undangan Konkret (skema template — diinstansiasi **per unit**/per undangan) |
| **Cara diisi** | cukup template biasa — **sudah dijalankan 2026-09-20 (UTC)** |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (hal konsisten #1, Tahap 2 siklus, aturan warisan L3) + `02_PROFIL_JENIS_ACARA.md` bagian 2–9 (field default, satu-sumber, etika, siklus, fitur) + `01_IDENTITAS_PEMILIK.md` (format keluaran, batasan mutlak, amplop, serah terima) |

## Fungsi dokumen ini

**Skema data acara = hal konsisten #1 dan paling berbahaya.** Satu sumber data dipakai banyak format (web, video, flyer, cetak) — kalau skemanya longgar, satu perubahan nama bisa tercecer di satu format saja.

## Catatan untuk yang mengisinya nanti

Wajib memuat: field wajib vs opsional, tipe & format tiap field (tanggal, jam, zona waktu, koordinat), dan **aturan satu-sumber** (tidak boleh ada salinan nilai yang bisa berbeda).

## Isi

### 1. Aturan Satu-Sumber (inti skema — yang paling dulu dibaca)

1. **Satu rekaman data per undangan** adalah satu-satunya sumber nilai untuk semua format
   keluaran (laman web multi-halaman, video animasi, flyer/poster portrait+landscape, story WA,
   square — format L1). Tiap format **merender dari rekaman itu**, tidak pernah menyalin manual.
2. **Tidak boleh ada salinan nilai yang bisa berbeda.** Kalau sebuah nilai (nama, tanggal, jam,
   alamat, nomor rekening) muncul di dua tempat yang bisa disunting terpisah, itu **bug skema** —
   perbaiki strukturnya, bukan isinya. Contoh nyata yang dilarang: jam acara diketik di halaman web
   dan diketik ulang di video.
3. **Perubahan = ubah di sumber, lalu render ulang semua format.** Tidak ada "benerin satu halaman
   doang" — cara itu adalah persis kegagalan yang hal konsisten #1 cegah (kerusakan yang tidak
   terlihat sampai formatnya dibuka).
4. **Larik per acara, bukan nilai tunggal.** Undangan boleh memuat lebih dari satu acara (akad +
   resepsi; satu hari dua lokasi; dua hari) — `acara` adalah **daftar**, dan tanggal+jam+tempat
   ditulis **lengkap per acara** (tamu tidak boleh menebak; 02 bagian 4 sumbu 2). Larik yang menulis
   *"sama dengan akad"* **dilarang** — nilai salinan itu akan bisa berbeda.
5. Zona waktu **selalu ada dan selalu ditulis** (WIB/WITA/WIT) di setiap acara (02 bagian 7 butir 4).

### 2. Struktur Rekaman Data Acara

Satu unit undangan (1 client / 1 acara = 1 unit kerja, `STATUS.md` per unit — W-03) menyimpan SATU
rekaman dengan blok berikut. Urutan = urutan pengisian di Tahap 2:

1. **Meta** — jenis acara + profil L2 yang dipakai (`02_PROFIL_JENIS_ACARA.md`, bagian jenis yang
   relevan) · status paket studio (L1 bagian 6) · kontak client.
2. **Mempelai** — data kedua mempelai (field `nama_mempelai`, bawah).
3. **Tuan rumah** — pola + nama/gelar + daftar turut mengundang + hasil konfirmasi titik sensitif.
4. **Acara** — daftar event; tiap event punya nama, hari/tanggal/jam/zona waktu, venue/alamat/peta.
5. **Tamu & sapaan** — sapaan baku (default L1) + daftar nama tamu untuk personalisasi per tautan.
6. **Fitur** — field fitur bawaan L2 (02 bagian 9) + field per-undangan yang dipilih saat brief
   (dokumen 04).
7. **Amplop digital** — rekening/QRIS client bila diaktifkan (L1 bagian 7; detail teknis dokumen 11).
8. **Publikasi** — URL undangan (path stabil lintas fase — kebijakan domain 3 fase, 00 bagian 5) +
   catatan versi terbit.

### 3. Tabel Field

Nama field teknis = `snake_case` stabil (keputusan agent — Log Keputusan baris 2); label = teks yang
ditampilkan. Status mengikuti 02 bagian 5 (WAJIB 7 · OPSIONAL 14 · TIDAK BERLAKU) dan 02 bagian 9
(BAWAAN 11 · PER-UNDANGAN 9). Field **WAJIB** diverifikasi di gerbang data (bagian 7 dokumen ini);
yang kurang **dinyatakan sadar** (bagian 4), tidak diisi nilai karangan.

| Field | Label | Tipe & format | Status | Cakupan | Catatan |
|---|---|---|---|---|---|
| `nama_mempelai` | Nama Mempelai | daftar 2, per orang: `nama_lengkap` (string) + `nama_panggilan` (string) | **WAJIB** | kedua mempelai | nama lengkap + gelar utuh bila gelar ada (02 §3) |
| `pola_tuan_rumah` | Pola Tuan Rumah | enum: `orang_tua` · `mempelai_sendiri` | **WAJIB** | unit | 02 §3 dua pola baku |
| `orang_tua` | Orang Tua | daftar, per orang: `nama_lengkap` + `gelar_utuh` (H./Hj./Dr./S.Pd — tidak disingkat) | **WAJIB** bila `pola_tuan_rumah=orang_tua` (tidak berlaku bila mempelai sendiri — nyatakan sadar) | tuan rumah | orang tua **bercerai**: baris terpisah tanpa "&"; **meninggal**: wali "(selaku Wali Nikah)" atau alm./almh. — **selalu konfirmasi keluarga** (02 §3) |
| `turut_mengundang` | Turut Mengundang | daftar string (saudara kandung, kakek/nenek, keluarga besar, instansi) | opsional | tuan rumah | urutan = titik sensitif (02 §3: sumber berbeda — selalu konfirmasi) |
| `titik_sensitif_terkonfirmasi` | Konfirmasi Titik Sensitif | boolean + catatan: apa yang dikonfirmasi, siapa, kapan | **WAJIB** (bagian dari WAJIB #2, 02 §5) | unit | urutan, gelar, alm./wali, cerai, beda agama — **tidak pernah diasumsikan** |
| `bentuk_acara` | Bentuk Acara | enum: `akad_nikah` · `pemberkatan` · `holy_matrimony` · `pencatatan_sipil` · `adat` (+ `nama_prosesi_adat` string bebas bila adat — dari client, tidak dipatok studio) | **WAJIB** | unit | kata baku default per 02 §2; preferensi keluarga menang (dikonfirmasi) |
| `dengan_resepsi` | Dengan Resepsi | boolean | **WAJIB** | unit | 02 §5 butir 3 |
| `istilah_resepsi` | Istilah Resepsi | enum: `Resepsi Pernikahan` (default) · `Walimatul Ursy` (opsi ditawarkan) | **WAJIB** bila `dengan_resepsi=true` **dan** bentuk Islami (tidak berlaku otomatis untuk non-Islami — nyatakan sadar) | unit | keputusan 02 §2 |
| `acara` | Acara (event) | **daftar ≥1** — tiap larik: `nama_acara` (string, mis. "Akad Nikah", "Resepsi") · `hari` (string, mis. "Sabtu") · `tanggal` (**ISO 8601 `YYYY-MM-DD`**) · `jam_mulai` (**24 jam `HH:MM`**) · `jam_selesai` (opsional, `HH:MM`) · `zona_waktu` (**enum `WIB`/`WITA`/`WIT` — WAJIB, selalu ditulis**) · `venue` (string) · `alamat` (string lengkap) · `tautan_peta` (URL Google Maps **atau** koordinat `lat,lng`) | **WAJIB** (hari+tanggal, jam, tempat+peta, zona waktu = WAJIB 02 §5 butir 4–7) | **per acara** | larik harus lengkap per acara — larik rujukan "sama dengan …" dilarang (bagian 1 butir 4) |
| `tanggal_hijriah` | Tanggal Hijriah | string (per kalender yang dipakai keluarga) | opsional | per acara (bentuk Islami) | 02 §5 |
| `pembuka` | Pembuka | string (teks final) + `sumber` (default kandidat 02 §2 / permintaan client) | **BAWAAN** — selalu ada di setiap undangan pernikahan (02 §9 butir 5); bila client tidak menentukan → kandidat default L2, pilihan final per undangan | unit | pembuka Islami **hanya** untuk acara Islami (kunci L1) — non-Islami = kalimat netral elegan |
| `susunan_acara` | Susunan Acara | daftar: `waktu` + `kegiatan` | **BAWAAN** (blok selalu ada — 02 §9 butir 4); isi detail opsional | per acara | **benturan tercatat di 02**: §5 memasukkan rundown ke OPSIONAL 14, §9 ke BAWAAN 11 — cara dokumen ini memperlakukannya: blok bawaan, detail dari client; client tidak memberi detail → susunan minimal + dinyatakan sadar (Log Keputusan baris 3 — boleh dikoreksi) |
| `sapaan_tamu` | Sapaan Tamu | string (default L1: *"Kepada Yth. Bapak/Ibu/Saudara/i"*) + `personalisasi` (daftar nama tamu per tautan) | **BAWAAN** (02 §9 butir 6) | unit | variasi hangat = permintaan client |
| `ucapan_doa` | Ucapan & Doa Restu | string (default sesuai bentuk) + buku tamu publik | **BAWAAN** (02 §9 butir 7) | unit | — |
| `rsvp` | RSVP | `batas_waktu` (ISO `YYYY-MM-DD`) + `kontak` (string) | opsional (02 §5) | unit | fitur bawaan L2 #8 = form RSVP + rekap client selalu ada; data batas/kontak opsional |
| `teks_wa_sebar` | Teks WA Siap Salin | string + QR (dihasilkan dari rekaman, bukan diketik manual — aturan satu-sumber) | **BAWAAN** (02 §9 butir 9; serah terima L1 item 4) | unit | **wajib bisa diperbarui setelah terbit** (bagian 6) |
| `penutup` | Kalimat Penutup | string (default elegan sesuai bentuk) | **BAWAAN** (02 §9 butir 10) | unit | credit Lee-Studio = **BAWAAN** (02 §9 butir 11, L1 bagian 1 — hilang di paket premium) |
| `dress_code` | Dress Code | string | opsional (02 §5) | unit | **wajib bisa diubah setelah terbit** (bagian 6) |
| `amplop_digital` | Amplop Digital | `rekening` (nomor + a.n. + bank) · `qris` (referensi gambar) · `nominal` (default: **tanpa nominal** — L1 §7) | opsional — aktif **hanya** bila client memberi rekening/QRIS | unit | rekening = **titik verifikasi G2/G5** (L1 batasan mutlak #1: salah = uang tamu ke tempat salah); acara keagamaan → peruntukan **infaq** |
| `galeri` | Galeri / Love Story | daftar: `foto` (referensi aset) + `caption`; `love_story` string | opsional (02 §5) | unit | **foto wajib bisa diganti setelah terbit** (bagian 6); resolusi foto = gerbang G3 (dokumen 06) |
| `musik` | Musik Latar | referensi file + `autoplay=false` + tombol off **wajib** | opsional (02 §5) | unit | pantangan 02 §6 butir 7: autoplay tanpa tombol off dilarang |
| `countdown` | Countdown | boolean; target default = **mulai acara inti** | opsional (02 §5) | unit | — |
| `streaming` | Live Streaming | URL | opsional (02 §5) | unit | — |
| `hashtag` | Hashtag Acara | string | opsional (02 §5) | unit | — |
| `qr_checkin` | QR Check-in + Layar Sapa | boolean | opsional (02 §5) — relevan acara besar (skala tamu, 02 §4 sumbu 3) | unit | — |
| `info_tamu` | Info Parkir / Akomodasi | string | opsional (02 §5) | unit | tamu luar kota/destinasi |
| `format_tambahan` | Format Tambahan | daftar: `video` · `cetak` (spesifikasi → dokumen 07) · `story_wa` | opsional (02 §5; format L1 bagian Cakupan Usaha) | unit | pilihan format final = gerbang **G2** (BESAR) |
| `catatan_keluarga` | Catatan Khusus Keluarga | string | opsional (02 §5) | unit | — |

**TIDAK BERLAKU (otomatis per bentuk — bukan pilihan, 02 §5):** `pembuka` religius Islami untuk acara
non-Islami dan sebaliknya (kunci L1) · display mahar (tidak baku; permintaan = custom, dicatat di
Log Keputusan unit).

### 4. Aturan Adaptif (boleh kurang boleh lebih)

L3 **boleh menyimpang** dari daftar L2 — tetapi:

1. **Yang kurang = dinyatakan sadar.** Field WAJIB yang memang tidak ada untuk unit ini (mis. pola
   `mempelai_sendiri` sehingga `orang_tua` tidak terpakai; `istilah_resepsi` untuk non-Islami)
   ditulis eksplisit **"tidak berlaku — alasan …"**, bukan dibiarkan kosong diam-diam.
2. **Tidak pernah diisi nilai karangan.** Tidak ada nama, tanggal, nomor rekening, atau alamat
   "contoh" yang tertinggal — nilai kosong = belum terisi = belum boleh lewat gerbang data.
3. **Field tambahan = boleh** (mis. info shuttle, info foto booth) — dicatat di Log Keputusan unit
   beserta alasannya (aturan warisan L3, 00 bagian 2.2).
4. **Struktur (nama field, tipe) tidak boleh berubah per unit** — yang boleh berubah hanya **isi**
   dan **status** field. Mengubah nama field = perubahan skema = perubahan dokumen ini + Log
   Keputusan + re-render semua format terdampak (hal konsisten #1).

### 5. Field Sensitif dan Verifikasi

Selalu dikonfirmasi ke client/keluarga **per undangan — tidak pernah diasumsikan** (02 §3):

- urutan nama orang tua / pihak mana dulu (sumber berbeda — 02 §3);
- gelar (utuh, tidak disingkat tanpa persetujuan);
- kasus sensitif: orang tua bercerai (baris terpisah tanpa "&"), meninggal (wali "selaku Wali Nikah" / alm.-almh. sesuai keluarga), beda agama/suku (dua kolom setara);
- pemilihan `pembuka` final per undangan (kandidat 02 §2) untuk yang sensitif;
- **nomor rekening + QRIS** — cross-check **G2 dan G5** (L1 batasan mutlak #1: info salah = kesalahan
  termahal di sistem ini).

### 6. Field yang Wajib Bisa Diubah Setelah Terbit (spesifikasi untuk G5 / dokumen 09)

Dari 02 bagian 8 — mekanisme sebar ulang: **tautan tetap sama** (path stabil, kebijakan domain 3
fase), teks WA diperbarui dari sumber:

| Field | Boleh diubah setelah terbit | Catatan |
|---|---|---|
| `jam_mulai` / `jam_selesai` per acara | **YA** | perubahan mendadak lazim (02 §8) |
| `venue` / `alamat` / `tautan_peta` per acara | **YA** | — |
| `galeri` (foto) | **YA** | gerbang G3 tetap berlaku untuk foto pengganti |
| `susunan_acara` | **YA** | — |
| `dress_code` | **YA** | — |
| `teks_wa_sebar` | **YA** (perbaikan turunan otomatis dari sumber) | — |
| `nama_mempelai` / gelar / `orang_tua` | **sensitif** — bisa, **lewat konfirmasi** (02 §8) | perubahan nama = re-render semua format |

### 7. Validasi Data Acara (gerbang data — ujung Tahap 2, `00_RENCANA_KERANGKA.md` bagian 4)

Data acara **tidak boleh masuk Tahap 3 (Desain & Format)** sebelum lulus:

1. Semua field **WAJIB** terisi **atau** tertulis "tidak berlaku — alasan …" (bagian 4).
2. `titik_sensitif_terkonfirmasi` = YA beserta catatannya (bagian 5) — tanpa ini **gagal, bukan
   peringatan**.
3. Format tiap field benar: tanggal terbaca ISO, jam 24 jam, zona waktu ada **di setiap larik acara**,
   `tautan_peta` ada (URL atau koordinat), larik `acara` lengkap per larik (tidak ada rujukan
   "sama dengan …").
4. Nilai amplop digital (bila aktif) sudah dicocokkan dengan client (L1 batasan mutlak #1).
5. Hasil validasi + field yang "dinyatakan sadar" tercatat di **Log Keputusan unit**.

Tingkat risikonya mengikuti `00_RENCANA_KERANGKA.md` bagian 4.2 (gerbang produksi per-undangan);
pencatatan sesuai levelnya — dokumen ini tidak mengubah klasifikasi gerbang manapun.

### 8. Cara Pakai Template Ini per Undangan

1. **Satu undangan = satu unit kerja** — folder unit + `STATUS.md` (W-03) + **salinan skema ini
   terisi** (rekaman bagian 2). Unit baru tidak boleh "meminjam nilai" dari unit lain — setiap
   rekaman ditulis sendiri dari sumber client.
2. Pengisian mengikuti **Tahap 2 siklus** — agen menuntun dari brief (dokumen 04), bukan
   menyodorkan formulir kosong (00 bagian 2.3).
3. Setiap penyimpangan dari L2/L1 (bagian 4) dan hasil validasi (bagian 7) → **Log Keputusan unit**.
4. Setelah data valid (bagian 7) → baru Tahap 3 (Desain & Format, dokumen 05) — urutan tidak boleh
   dibalik: desain yang dibangun di atas data tidak valid harus dibongkar.

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-20 | **Dokumen diisi — ROADMAP b1 butir (1)**: skema data acara + aturan satu-sumber + validasi; banner kerangka dicabut; `_sistem/validate_system.py` diperluas (9 kerangka → 8 kerangka + 3 terisi; diuji mutasi); manifest v0.4.0→**v0.5.0**; `STATUS.md` diperbarui — **satu commit** | Handoff log sesi slot 43 (disetujui pemilik): *"isi 03_TEMPLATE_DATA_ACARA.md … sebagai template biasa yang diturunkan dari field L2 pernikahan"* + mekanika T-69/prompt 02 (banner+validator+manifest+STATUS satu commit). **Tidak ada keputusan baru pemilik** — semua isi penurunan dari L1/L2 yang sudah G0/G1 LULUS; review isi = PR normal tanpa auto-merge |
| 2026-09-20 | **Nama field teknis = `snake_case` stabil berbahasa Indonesia** (`nama_mempelai`, `acara`, `amplop_digital`, dst.) | **Keputusan agent, dinyatakan sadar** — 02/01 memberi isi field tetapi tidak memberi nama teknis; nama stabil dibutuhkan aturan satu-sumber (hal konsisten #1: "nama field" ikut dikunci). Dapat ditolak/diganti saat review PR; ganti nama = perubahan skema yang dicatat di Log Keputusan |
| 2026-09-20 | **`susunan_acara` diperlakukan: blok BAWAAN, detail opsional** (bukan murni opsional 02 §5, bukan murni bawaan 02 §9) | **Benturan antar-bagian di 02 dilaporkan, tidak diputus diam-diam**: bagian 5 memasukkan rundown ke OPSIONAL 14, bagian 9 ke BAWAAN 11 ("susunan acara sederhana"). Cara memperlakukan = interpretasi agent (Log Keputusan baris ini) — **pemilik boleh mengoreksi saat review**; koreksi hanya mengubah status di tabel bagian 3 |
| 2026-09-20 | **Status field mengikuti 02 bagian 5 + 9 apa adanya** (WAJIB 7 · BAWAAN · OPSIONAL · TIDAK BERLAKU) — tidak ada field yang dinaik/turunkan statusnya sepihak | Prinsip penurunan: L3 tidak memutuskan ulang isi L2; yang ditambahkan hanya **struktur teknis** (tipe, format, cakupan per unit/mempelai/acara) yang memang tugas dokumen ini per 00 bagian 7 |
