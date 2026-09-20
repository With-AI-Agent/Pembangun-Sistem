# Template Brief Undangan

> **STATUS: ISI — DRAFT.** Diisi 2026-09-20 (UTC) lewat **ROADMAP JALAN PRODUKSI
> PERTAMA, butir b1 (2/2)** (handoff log sesi slot 43; sesi slot 44) sebagai
> **template biasa** per `00_RENCANA_KERANGKA.md` bagian 7 (*"cukup template"* —
> bukan dokumen generator). **Semua isi di dokumen ini = penurunan dari isi yang
> sudah di-approve pemilik**: siklus 7 tahap & gerbang (`00_RENCANA_KERANGKA.md`
> bagian 2.3 + 4), kebijakan L1 (`01_IDENTITAS_PEMILIK.md` — harga & masa aktif,
> amplop, serah terima, batasan mutlak), dan profil L2 pernikahan (**G1 LULUS**,
> `02_PROFIL_JENIS_ACARA.md` — etika, field, konvensi, siklus, fitur).
> **Tidak ada keputusan baru pemilik di dokumen ini**; keputusan agent (cara
> menangani tenggat di bawah siklus) dinyatakan sadar di Log Keputusan dan
> **boleh ditolak/dikoreksi** saat review PR (PR normal, tanpa auto-merge).
> Banner kerangka dicabut di commit yang sama dengan perluasan validator
> (mekanika T-69/prompt 02).

| | |
|---|---|
| **Berkas** | `04_TEMPLATE_BRIEF_UNDANGAN.md` |
| **Lapis** | L3 — Undangan Konkret (brief **Tahap 1–2** siklus — diinstansiasi **per unit**/per undangan) |
| **Cara diisi** | cukup template biasa — **sudah dijalankan 2026-09-20 (UTC)** |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (Siklus 7 tahap bagian 2.3; gerbang G0–G5 bagian 4) + `01_IDENTITAS_PEMILIK.md` (bagian 5–8, 10) + `02_PROFIL_JENIS_ACARA.md` (bagian 2–9) + `03_TEMPLATE_DATA_ACARA.md` (skema data Tahap 2) |

## Fungsi dokumen ini

Brief Tahap 1–2 SIKLUS: apa yang diminta client, format yang diinginkan, anggaran, tenggat, dan batasan.

## Catatan untuk yang mengisinya nanti

Gerbang **G2** = approval **Besar**.

## Isi

### 1. Posisi Brief dalam Siklus

Brief adalah alat **Tahap 1 (Intake)** dan **Tahap 2 (Data Acara)** — dua tahap
pertama siklus 7 tahap (`00_RENCANA_KERANGKA.md` bagian 2.3):

1. **Tahap 1 — Intake** (ujung gerbangnya **G0**): brief awal diisi dari
   percakapan; **agen menuntun, bukan menyodorkan formulir kosong**; jenis acara
   terpilih menunjuk ke profil L2 yang relevan (`02_PROFIL_JENIS_ACARA.md` —
   untuk jenis selain pernikahan, bagian jenisnya harus sudah ada di dokumen L2
   dulu — kalau belum, itu **putaran Discovery 02 untuk jenis baru**, bukan
   improvisasi di brief).
2. **Tahap 2 — Data Acara** (ujung gerbangnya **G1**): isian brief bagian E
   dituangkan ke skema `03_TEMPLATE_DATA_ACARA.md`; data **divalidasi** sebelum
   masuk Tahap 3.
3. Brief adalah **input Tahap 3 (Desain & Format)** — tetapi keputusan desain &
   format **bukan dikunci di brief**: ia dikunci di gerbang **G2 (Besar)** saat
   review Tahap 3 (bagian 7). Brief boleh mencatat preferensi client; yang
   mengunci = G2.

### 2. Bagian A — Identitas dan Paket (Tahap 1)

| Item | Isi | Sumber default |
|---|---|---|
| Nama & kontak client | nama orang yang memberi order + kontak (WA) | — |
| Jenis acara | menunjuk bagian profil di `02_PROFIL_JENIS_ACARA.md` | L2 |
| Paket studio | selama **fase portofolio** (5 client / 2 bulan) = harga fleksibel per client; sesudahnya = struktur 3 paket **Basic / Premium / Luxury** (L1 bagian 6 — angka paket ditetapkan kemudian, tercatat di Log Keputusan L1) | L1 §6 |
| Kontak studio | untuk credit: cukup "Lee-Studio" sampai kontak terisi (L1 bagian 1 — *Belum Ditentukan*) | L1 §1 |

### 3. Bagian B — Permintaan Client (Tahap 1)

1. **Gambaran acara** — kota/lokasi (menentukan **zona waktu** WIB/WITA/WIT) ·
   jumlah acara (akad + resepsi? satu/dua lokasi?) → matriks variasi 02 bagian 4
   · skala tamu (intimate ≤50 / menengah / besar 500+) → menentukan relevansi
   QR check-in + layar sapa.
2. **Format yang diinginkan** — dicentang dari daftar format L1 (Cakupan Usaha):
   **web multi-halaman** · **video animasi** · **flyer/poster statis**
   (portrait untuk cetak/IG + landscape untuk broadcast) · **story WA** ·
   **square**. Pilihan ini menjadi **daftar format target** yang dijanjikan dan
   dikunci di **G2** — format yang dijanjikan di brief tetapi hilang tanpa
   tercatat = cacat serah terima.
3. **Preferensi desain** — client punya preferensi (warna, gaya, referensi) →
   **diutamakan** (Prinsip Kerja Dasar L1); **client tidak memberi keterangan**
   → katalog 8 model L2 dipakai sebagai **pilihan otomatis (fallback) — bukan
   aturan kaku** (koreksi pemilik 20 Sep 2026, 02 bagian 6). Pilihan model final
   ditetapkan di Tahap 3 bersama client (dokumen 05).
4. **Harus ada / tidak boleh** — permintaan eksplisit client (fitur dari daftar
   per-undangan 02 bagian 9: musik, galeri, amplop, countdown, streaming, dress
   code, QR check-in, analitik; format tambahan: video/cetak/story) + larangan
   client.
5. **Tamu** — daftar nama tamu untuk personalisasi per tautan (fitur bawaan, 02
   bagian 9) · **titik sensitif** (urutan keluarga, gelar, alm./wali, cerai,
   beda agama) — **ditanyakan dan dikonfirmasi eksplisit di sini** (02 bagian 3:
   tidak pernah diasumsikan); hasilnya masuk field
   `titik_sensitif_terkonfirmasi` (WAJIB, skema 03).
6. **Amplop digital** — client memberi **rekening/QRIS miliknya** (default L1 §7)
   atau tidak → fitur tidak aktif; **nominal default TANPA** (ditampilkan hanya
   bila client mau); acara keagamaan → peruntukan **infaq**.

### 4. Bagian C — Anggaran dan Tenggat (Tahap 1)

1. **Anggaran** — client menyebut angka → dicatat; tidak menyebut → **jangan
   mengarang angka** — sebutkan kebijakan fase (L1 §6: fase portofolio = fleksibel;
   rentang acuan pasar **Rp 50.000–500.000** sekali bayar, sebagai rujukan, bukan
   harga). Keputusan paket final dicatat di **Log Keputusan unit**.
2. **Tenggat** — tanggal hari-H → silangkan dengan siklus (02 bagian 8): order
   lazim **±3 bulan sebelum** · sebar digital **H-30…H-14** (luar kota/destinasi
   **H-60…H-45**) · **reminder H-7…H-1**.
   - Tenggat **sesuai siklus** → lanjut.
   - Tenggat **di bawah siklus** → **dinyatakan + diputuskan**, tidak diterima
     diam-diam (keputusan agent — Log Keputusan baris 3): (a) **jalur cepat**
     (produksi digital lincah — L1 §6; mis. hanya web, tanpa format tambahan)
     dan/atau (b) **potong format** (cetak/video yang membutuhkan waktu) — kedua
     opsi disampaikan ke client dengan konsekuensinya; client memilih; hasilnya
     dicatat di Log Keputusan unit.
3. **Masa aktif** — default **1 tahun** + perpanjangan **gratis**, tidak ada
   penonaktifan sepihak (L1 §6) — disampaikan saat brief supaya tidak jadi
   kejutan di serah terima.

### 5. Bagian D — Batasan (Tahap 1)

1. **Batasan mutlak L1 selalu berlaku** (01 bagian 10): tidak ada info palsu/salah
   (tanggal, waktu, tempat, nama, **nomor rekening** — cross-check G2/G5) ·
   tanpa watermark/merek orang lain · tanpa konten melanggar · **lisensi =
   peringatan, bukan block** (aset boleh dipakai; provenance + status dicatat;
   keputusan pemilik menutup).
2. **Batasan per jenis acara** — pantangan L2 (02 bagian 6, 9 butir) berlaku
   untuk jenis acaranya; perubahan = permintaan client eksplisit + tercatat.
3. **Harapan perubahan sesudah terbit** — sampaikan ke client di brief: field
   yang **bisa diubah setelah terbit** (jam, tempat, peta, foto, susunan acara,
   dress code — skema 03 bagian 6) + **tautan tetap sama** (path stabil, kebijakan
   domain 3 fase); revisi tak terbatas **sebelum** terbit (L1 §8). Menyampaikan
   ini di awal mencegah ekspektasi keliru di Tahap 7.

### 6. Bagian E — Data Acara (Tahap 2)

Brief tidak menyimpan data acara sendiri — ia **menyerahkannya ke skema
`03_TEMPLATE_DATA_ACARA.md`**:

1. Salin skema 03 ke unit (rekaman bagian 2 dokumen 03) dan isi dari jawaban
   client; **field per acara ditulis lengkap per larik** (tanpa rujukan
   "sama dengan …").
2. **Aturan adaptif** berlaku (03 bagian 4): boleh kurang/lebih; yang kurang
   **dinyatakan sadar**; tidak ada nilai karangan.
3. **Validasi** (03 bagian 7) dijalankan sebelum Tahap 3 — data yang belum lulus
   validasi **tidak boleh** masuk desain (urutan tidak boleh dibalik).
4. Hasil validasi + daftar field "dinyatakan sadar" → **Log Keputusan unit**.

### 7. Gerbang yang Dilewati Brief (per `00_RENCANA_KERANGKA.md` bagian 4)

| Gerbang | Saat | Dikunci | Tingkat (bagian 4.2) |
|---|---|---|---|
| **G0** | ujung Tahap 1 | brief + **jenis acara** (L2 terpilih) + field default disetujui | **Besar** — review isi lengkap oleh pemilik, tidak boleh diwakilkan |
| **G1** | ujung Tahap 2 | data acara **lengkap & valid** terhadap skema 03; yang kurang dinyatakan sadar | **Sedang** — konfirmasi ringkas + catatan (pencatatan sesuai levelnya; dokumen ini tidak mengubah klasifikasi) |
| **G2** | ujung Tahap 3 | **desain & format dikunci** (template, font, palet, daftar format yang dijanjikan) | **Besar** — review isi lengkap oleh pemilik |

**Catatan pelabelan (DISelaraskan — putusan pemilik, review isi PR #90, 20 Sep 2026,
sesi slot 44):** baris "Titik approval Besar" di `SYSTEM_MANIFEST.md` menulis
"G2 (brief & struktur data)" sedangkan `00_RENCANA_KERANGKA.md` bagian 4
menulis G2 = **desain & format dikunci**; siklus 00 bagian 2.3 sendiri menaruh
brief di G0 (Tahap 1) dan data di G1 (Tahap 2), sehingga label manifest tidak
konsisten dengan siklus. **Putusan pemilik: selaraskan manifest ke 00 bagian 4** —
baris manifest sudah dikoreksi di PR yang sama; dokumen ini mengikuti 00 bagian 4
(Log Keputusan baris 2 — laporan; baris 4 — putusan).

### 8. Cara Pakai Template Ini per Undangan

1. **Satu undangan = satu unit kerja** — folder unit + `STATUS.md` (W-03); brief
   (berkas ini terisi) disimpan **di folder unit**, bukan di folder sistem.
2. Pengisian mengikuti **Tahap 1–2** — agen menuntun (bagian 1); tawaran
   kapabilitas (jika muncul) disampaikan di Tahap 1 (aturan 00 bagian 2.3).
3. Setiap penyimpangan dari L1/L2 dan keputusan tenggat/paket → **Log
   Keputusan unit** — tidak boleh diam-diam (aturan warisan L3, 00 bagian 2.2).
4. Sesudah G1 lulus → **Tahap 3** (Desain & Format, dokumen 05) — brief menjadi
   bahan review G2; setelah G2, perubahan format = perubahan besar (tercatat +
   approval ulang).

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-20 | **Dokumen diisi — ROADMAP b1 (2/2)**: brief Tahap 1–2 + gerbang yang dilewatinya; banner kerangka dicabut; `_sistem/validate_system.py` diperluas (8 kerangka → **7 kerangka + 4 terisi**; diuji mutasi); manifest v0.5.0→**v0.6.0**; `STATUS.md` diperbarui — **satu commit** | Handoff log sesi slot 43 (disetujui pemilik; sesi slot 44): *"…04_TEMPLATE_BRIEF_UNDANGAN.md sebagai template biasa yang diturunkan dari field L2 pernikahan"*. Isinya penurunan dari siklus & gerbang (00 bagian 2.3/4) + L1 (§6 harga & masa aktif, §7 amplop, §8 serah terima, §10 batasan mutlak) + L2 (§3 etika, §5 field, §6 konvensi & fallback, §8 siklus, §9 fitur) + skema 03. **Tidak ada keputusan baru pemilik**; review isi = PR normal tanpa auto-merge |
| 2026-09-20 | **Benturan label G2 dilaporkan, tidak diputus sepihak**: manifest = "G2 (brief & struktur data)" vs `00_RENCANA_KERANGKA.md` bagian 4 = "G2 — desain & format dikunci" | Norma repo: konflik dilaporkan, bukan ditebak (preseden benturan klasifikasi G1 di dokumen 02). **Kedua dokumen sepakat G2 = Besar**; cara perlakukan dokumen ini (keputusan format dari brief dikunci di G2) = interpretasi agent, **pemilik boleh koreksi** saat review; penyelarasan label = keputusan pemilik di Log Keputusan dokumen manapun |
| 2026-09-20 | **Tenggat di bawah siklus = dinyatakan + diputuskan (jalur cepat dan/atau potong format), bukan diterima diam-diam** | **Keputusan agent, dinyatakan sadar** — dasar: siklus terukur 02 bagian 8 (H-30…H-14 digital dst.) + L1 bagian 6 (jalur cepat: produksi digital lincah; revisi tak terbatas sebelum terbit). Dokumen induk (00 bagian 2.3 Tahap 1) mewajibkan agen menuntun, bukan menerima mentah; mekanisme "nyatakan + putuskan + catat" adalah penurunan dari aturan adaptif L3 (yang kurang dinyatakan sadar). Dapat ditolak/diperketat saat review PR |
| 2026-09-20 | **Review isi PR #90 dijalankan PEMILIK (sesi slot 44): "setuju semua rekomendasi"** — (1) benturan label G2 (baris 2) **DISelaraskan oleh putusan pemilik**: baris "Titik approval Besar" manifest dikoreksi menjadi "desain & format dikunci" mengikuti 00 bagian 4 (koreksi manifest = keputusan pemilik, bukan agent); (2) **tenggat di bawah siklus = dinyatakan + diputuskan** (baris 3) **dikonfirmasi pemilik** | Putusan pemilik di chat review isi (log sesi slot 44); koreksi manifest + catatan ini satu commit di PR #90 (draft menunggu merge — tanpa auto-merge) |
