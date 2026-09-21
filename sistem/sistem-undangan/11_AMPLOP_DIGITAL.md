# Amplop Digital

> **STATUS: ISI — DRAFT.** Diisi 2026-09-21 (UTC) lewat **ROADMAP JALAN PRODUKSI PERTAMA,
> butir b2** (handoff log sesi slot 44; dikerjakan sesi slot 45) sebagai **template biasa**
> per `00_RENCANA_KERANGKA.md` bagian 7 (*"cukup template"* — bukan dokumen generator).
> **Semua isi di dokumen ini = penurunan dari isi yang sudah di-approve pemilik**: kunci
> Discovery Level-0 (amplop = rekening + QRIS statis, **TANPA payment gateway**) ·
> `01_IDENTITAS_PEMILIK.md` §7 (rekening client default · versi percobaan = rekening pemilik ·
> QRIS pemilik "nanti" · nominal default tanpa nominal · pola infaq) · §8 (serah terima item 4 & 5) ·
> §10 (batasan mutlak #1 — nomor rekening = titik verifikasi G2/G5) · `02_PROFIL_JENIS_ACARA.md`
> §3 (etika), §5/§9 (fitur per-undangan), §6 (pantangan) · skema data `03_TEMPLATE_DATA_ACARA.md`
> (field `amplop_digital`) · `05_DISCOVERY_DESAIN_PROMPT.md` §1 (batas janji Tahap 3) ·
> `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` §1 (Langkah 0), §5 (asal aset ditolak), §6 (cetak uji).
> **Tidak ada keputusan baru pemilik di dokumen ini**; keputusan agent dinyatakan sadar di
> Log Keputusan di bawah dan **boleh ditolak/dikoreksi** saat review PR (PR normal, tanpa
> auto-merge). Banner kerangka dicabut di commit yang sama dengan perluasan validator
> (mekanika T-69/prompt 02).

| | |
|---|---|
| **Berkas** | `11_AMPLOP_DIGITAL.md` |
| **Lapis** | lintas semua lapis — L1 (pemilik: siapa punya rekening, kapan boleh tampil) · L2 (per jenis acara: etika & peruntukan) · L3 (per unit: nomor, a.n., bank, berkas QRIS) |
| **Cara diisi** | cukup template biasa — **sudah dijalankan 2026-09-21 (UTC)** |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (bagian 3 hal konsisten #1 & #3 · bagian 4 gerbang G2/G5 · bagian 6 butir skill #7 · bagian 7 baris `11_AMPLOP_DIGITAL.md`) + `01_IDENTITAS_PEMILIK.md` §7/§8/§10 + `02_PROFIL_JENIS_ACARA.md` §3/§5/§6/§9 + `03_TEMPLATE_DATA_ACARA.md` + `05_DISCOVERY_DESAIN_PROMPT.md` §1 + `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` §1/§5/§6 |

## Fungsi dokumen ini

Amplop digital: **rekening + QRIS statis**, **tanpa payment gateway** (karena kendala nol biaya
bulanan). Dokumen ini merinci **cara menampilkannya dengan sopan** — bagian yang sengaja ditunda
ke sini oleh Discovery Level-0, karena etikanya berbeda per jenis acara (`02_PROFIL_JENIS_ACARA.md` §3).

## Catatan untuk yang mengisinya nanti

Sudah diputuskan di Discovery Level-0. Yang perlu dirinci: cara menampilkannya sopan (etika berbeda
per jenis acara → terkait `02_PROFIL_JENIS_ACARA.md`).

## Isi

### 1. Ruang Lingkup & yang Tidak Ditawar Ulang

Amplop digital di sistem ini **bukan** fitur pembayaran. Ia adalah **cara menampilkan tujuan
transfer** supaya tamu yang ingin memberi bisa melakukannya sendiri:

| Yang berlaku | Konsekuensinya |
|---|---|
| **Rekening + QRIS statis** (kunci pemilik Level-0, `00` bagian 6 baris 7) | tidak ada biaya per transaksi dan tidak ada biaya bulanan — untuk studio maupun untuk client |
| **TANPA payment gateway** | tidak ada halaman pembayaran pihak ketiga, tidak ada saldo menumpuk di sistem ini, tidak ada potongan |
| **Uang tidak pernah lewat studio** | dana masuk **langsung** ke rekening pemilik acara (client) — tidak ada perantara, tidak ada urusan pencairan |
| **Yang mengirim = tamu client** | penerima ditentukan client, bukan studio |

**Yang ditolak dengan penjelasan awam (bukan didiamkan):** integrasi payment gateway, dompet digital
ber-saldo, "bayar di undangan", tagihan/virtual account, dan apa pun yang menahan dana. Alasannya
satu kalimat yang bisa disampaikan ke client: *"sistem ini menampilkan tujuan transfernya saja; uangnya
langsung masuk ke rekening Anda, tidak mampir ke kami"*.

### 2. Kapan Amplop Muncul — dan Kapan Tidak

Aturan aktivasi **sudah dikunci di L1/L2** dan di dokumen ini hanya ditegakkan:

1. **Aktif hanya bila client memberi rekening/QRIS** (`02` §5 & §9; `03` bagian 3). Client **tidak
   wajib** memberikannya — amplop digital adalah **opsi brief, bukan syarat terbit**.
2. **Belum/tidak ada data → bagian ini TIDAK dirender sama sekali.** Dilarang menampilkan kolom
   kosong, "menyusul", titik-titik pengganti, atau nomor karangan: batasan mutlak #1 L1 melarang
   info palsu (nilai karangan = kesalahan yang tidak bisa dimaafkan, dan untuk rekening = **kesalahan
   termahal di sistem ini**). Undangan tanpa amplop tetap **sah**.
3. **Versi percobaan/demo (undangan milik studio sendiri, termasuk uji coba b3): rekening PEMILIK**
   (transfer biasa), sesuai L1 §7 (`01` — *"klo untuk versi percobaan, gpp pake punya aku dulu"*).
   Rekening pemilik juga **versi percobaan**, bukan hal yang dijanjikan ke client.
4. **QRIS pemilik: belum ada — bukan blocker** (L1 §7). Selama belum ada, versi percobaan tampil
   **rekening saja**; itu keadaan yang sah, bukan cacat yang perlu disembunyikan.
5. **Nominal: default TANPA nominal** (L1 §7). Bila client ingin nominal ditampilkan, itu
   **permintaan per undangan** — dicatat di Log Keputusan unit, bukan diubah jadi default baru.

### 3. Data yang Ditampilkan & Aturan Satu-Sumber

Semua nilai di bagian amplop **dirender dari rekaman data acara** (`03_TEMPLATE_DATA_ACARA.md`,
field `amplop_digital`) — tidak pernah diketik ulang di halaman web, flyer, atau video:

| Isi tampil | Sumber nilai | Bentuk tampil |
|---|---|---|
| Nomor rekening | `amplop_digital.rekening.nomor` | **teks** (bukan gambar — Langkah 0, `06` §1) + tombol **salin** |
| Nama pemilik rekening (a.n.) | `amplop_digital.rekening.nama` | teks |
| Bank / penerbit | `amplop_digital.rekening.bank` | teks |
| Kode QRIS statis | `amplop_digital.qris` (referensi berkas gambar client) | gambar fungsional — lihat §5 |
| Nominal (bila diminta client) | `amplop_digital.nominal` | teks, **default kosong** |

**Aturan satu-sumber (hal konsisten #1) berlaku penuh di sini.** Kalau nomor rekening diketik manual
di dua tempat (mis. di halaman web **dan** di flyer), itu **bug skema**, bukan "kurang teliti" — satu
suntingan yang tercecer = sebagian tamu transfer ke nomor yang salah.

**Tombol salin termasuk bagian dari data, bukan hiasan:** yang disalin aplikasi harus **nilai dari
rekaman**, tanpa spasi/huruf tambahan. Menampilkan nomor dalam kelompok digit yang enak dibaca
**sah**, asalkan yang disalin tetap digit murni.

### 4. Cara Menampilkan Sopan — Etika per Jenis Acara

Prinsip (turunan `02` §3 & §6): **amplop adalah kemudahan bagi yang ingin memberi, bukan permintaan.**
Di undangan ia muncul sebagai bagian tersendiri, setelah rangkaian utama selesai — bukan di pembuka,
bukan di antara data sakral (nama, tanggal, tempat), dan tidak "menempel" pada kalimat yang meminta.

| Hal | Cara tampil | Dasarnya |
|---|---|---|
| **Penempatan** | setelah ucapan/doa restu, sebelum kalimat penutup | rangkaian fitur per-undangan `02` §9 |
| **Judul bagian** | default **"Amplop Digital"**; acara keagamaan boleh **"Infaq"**; permintaan halus client boleh **"Tanda Kasih"** | L1 §7 pola nyata 2 flyer maulid pemilik (peruntukan = **infaq**, bukan "selamatan pernikahan") |
| **Kalimat pengantar** | satu kalimat sopan, tanpa tekanan, mis. *"Bagi Bapak/Ibu/Saudara/i yang ingin memberikan tanda kasih, dapat melalui:"* | nada default L1 (`02` §7 — tidak ditanya ulang per klien) |
| **Peruntukan** | mengikuti jenis acara: pernikahan = tanda kasih; acara keagamaan = **infaq** | L1 §7 (pola flyer pemilik) |
| **Nominal** | **tidak ditampilkan** kecuali client minta (§2 butir 5) — memampang angka di depan tamu adalah pilihan client, bukan default studio | L1 §7 |
| **Nominal sebagai pengganti** | bila client tidak mau menampilkan rekening, amplop **dimatikan** — bukan diganti teks "hubungi kami" | turunan larangan info palsu L1 §10 |
| **Tema visual** | mengikuti palet/model undangan (L1 §2); **tidak** memakai warna khusus "uang"/kemewahan yang keluar dari palet | disiplin maks 2 font & 3 warna (`02` §6) |

**Etika per jenis acara:** saat dokumen ini ditulis, L2 yang sudah ada **baru pernikahan** (`02`, G1
LULUS). Untuk jenis acara lain (khitanan, ulang tahun, webinar, dsb.) aturan umum di atas tetap
berlaku, tetapi **nada & peruntukannya belum punya profil L2** — keadaan ini **dinyatakan terbuka**,
bukan diisi dengan dugaan. (Jenis acara baru ditunda pemilik sampai ada demand — bukan pekerjaan
sesi ini.)

### 5. Aturan Teknis Minimum (Tanpa Payment Gateway)

**a. Rekening = teks, QRIS = berkas fungsional.**

- Nomor rekening **wajib teks** (Langkah 0, `06` §1): teks tajam di ukuran berapa pun dan bisa
  disalin tamu; nomor rekening yang ditempel sebagai gambar **ditolak** — dan ini juga melindungi
  client dari salah ketik, sebab tamu bisa menyalin, bukan membaca lalu mengetik ulang.
- QRIS berbeda golongan: ia **bukan ornamen, bukan foto, dan bukan hiasan** — ia **kode fungsional**
  milik penerbit (bank/e-wallet client). Karena itu ia **tidak** dirancang ulang, **tidak** diberi
  efek, **tidak** diwarnai, **tidak** ditempel di atas foto, dan **tidak** diletakkan pada latar
  berpola yang mengganggu kontras. Berkas aslinya dari client dipakai apa adanya.
- **Keputusan agent yang dinyatakan sadar:** golongan "kode fungsional" ini **tidak disebut** di
  Langkah 0 `06` §1 (yang menyebut teks, ornamen/logo, foto) dan **bukan foto**, jadi ia juga tidak
  masuk gerbang resolusi G3. Dokumen ini **tidak menyunting dokumen 06**; yang dicatat di sini adalah
  perluasan cakupan yang **boleh dikoreksi pemilik** (dokumen 06 bisa diselaraskan menyebut golongan
  ini kapan pun lewat Log Keputusan-nya).

**b. Ukuran & tampil.**

- QRIS ditampilkan pada **ukuran aslinya (maksimum lebar area konten), tidak diperbesar** dari berkas
  yang diberikan. Memperbesar gambar QR = dua risiko sekaligus: kode tidak terbaca **dan** klaim mutu
  yang tidak didukung bukti.
- **Uji pindai wajib sebelum terbit** (bagian dari tahap pra-terbit): QR dipindai **dari layar HP**
  dengan aplikasi bank/e-wallet yang lazim, **minimal dua aplikasi berbeda**, pada halaman yang sudah
  terbit (bukan pratinjau desktop). Hasilnya dicatat di Log Keputusan unit bersama bukti pra-terbit
  lain — konsisten dengan aturan G3: *gerbang tanpa bukti = diklaim hijau tanpa dijalankan* (`06` §8).
- QR yang **tidak terbaca** → minta berkas ulang ke client sebagai bahan asli (bukan menyalahkan,
  jalur sopan `06` §5), atau tampilkan **rekening saja** sementara. Jangan pernah "memperbaiki" kode
  QRIS dengan merancang ulang gambarnya.
- **Untuk flyer/cetak:** blok QRIS ikut aturan cetak uji di `06` §6 (cetak uji wajib; sistem
  menyerahkan berkas siap cetak, **bukan** menjanjikan hasil cetak). **Angka ukuran minimal QR cetak
  belum diukur** — jangan dikarang; ia masuk daftar `06` §10 yang belum diukur dan wajib diukur pada
  cetak uji nyata pertama.

**c. Yang wajib ada di undangan setelah amplop aktif:** satu tempat yang jelas (bukan tersebar), nama
pemilik rekening tertulis (agar tamu tahu ke siapa uangnya pergi), dan **tanpa batas waktu buatan**
(fitur mengikuti masa aktif undangan, L1 §6 — 1 tahun, perpanjangan gratis).

### 6. Titik Verifikasi Rekening — Kesalahan Termahal di Sistem Ini

L1 §10 batasan mutlak #1: **nomor rekening wajib cross-check di G2/G5**. Cara menegakkannya di sini:

1. **Sumber tunggal.** Nomor/a.n./bank diambil dari rekaman data (`03`) yang sudah dicocokkan dengan
   client — bukan dari chat, bukan dari ingatan agent, bukan dari gambar yang dipotret dari layar.
2. **Baca balik digit per digit ke client** sebelum terbit: agent menyebutkan nomor yang **akan
   tayang** dan meminta client menyetujuinya. Persetujuan ini dicatat sebagai bukti pra-terbit
   (tanggal + cara + siapa yang menyetujui) di Log Keputusan unit.
3. **Konfirmasi visual pada pratinjau.** Client melihat sendiri bagian amplop sebagaimana tamu akan
   melihatnya (nomor, a.n., bank, QRIS) — bukan berupa daftar teks di chat.
4. **Cross-check kedua di G5** (serah terima): nomor yang ada di undangan aktif dibandingkan **sekali
   lagi** dengan nomor yang disetujui client. Dua bacaan terpisah, bukan satu bacaan yang diulang.
5. **Bila nomor sudah salah tersebar:** lapor pemilik **segera** (prioritas tertinggi, di atas
   pekerjaan lain), perbaiki rekaman + terbitkan ulang, lalu minta client mengabari tamu yang sudah
   menyebar. Perbaikan menempel pada aturan perubahan sesudah tayang (`06` §9): tautan tetap, tampilan
   yang sudah di-cache browser tamu bisa menampilkan versi lama beberapa jam — dinyatakan apa adanya,
   bukan dijanjikan seketika.

### 7. Batas Janji: Apa yang Tidak Dijanjikan ke Client

Sesuai `05_DISCOVERY_DESAIN_PROMPT.md` §1 (batas janji Tahap 3), yang **boleh** dikatakan ke client:

- *"Rekening/QRIS Anda bisa ditampilkan di undangan, dana masuk langsung ke rekening Anda, tanpa
  potongan."*
- *"Kalau Anda belum punya QRIS, undangan tetap jalan dengan tampilan rekening — nanti bisa
  ditambahkan tanpa mengubah tautan."*

Yang **tidak boleh** dijanjikan (belum ada di sistem, harus berhenti di "PERLU KEPUTUSAN PEMILIK"):

| Jangan dijanjikan | Sebabnya |
|---|---|
| **Pencatatan/verifikasi otomatis siapa yang sudah mengirim** | tanpa payment gateway tidak ada data transaksi; sistem ini tidak menerima pembayaran (`00` bagian 6 baris 7) |
| **Kalimat "dana sudah diterima"** | sistem tidak memverifikasi dana masuk; itu di luar jangkauannya |
| **Halaman konfirmasi transfer, nominal otomatis, pengingat ke tamu** | fitur baru = keputusan pemilik, bukan improvisasi Tahap 3 |
| **QRIS dinamis / nominal per tamu** | di luar kunci "QRIS statis" Level-0 |
| **Domain/waktu/harga** | sudah punya batas janjinya sendiri di `05` §1 — jangan diulang di sini |

### 8. Serah Terima

Amplop ikut paket serah terima L1 §8 — **setelah terbit**, tanpa langkah teknis, bisa diunduh dari HP:

- **item (4) L1:** gambar QR + **teks WA siap salin** untuk disebar ke tamu;
- **item (5) L1:** **info rekening/QRIS** (bila client menghimpun dana).

Konsekuensi praktis: **teks WA siap salin** yang diberikan ke client juga memuat tujuan transfer bila
amplop aktif — dan karena ia hasil turunan rekaman (`03` bagian 3), memperbaiki nomor rekening
**tidak** perlu menyunting teks yang sudah disebar secara manual: teks dirender ulang dari sumber.

### 9. Yang Belum Ada / Ditunda (dinyatakan sadar, jangan diisi dengan dugaan)

1. **QRIS milik pemilik/studio** — belum ada, bukan blocker (L1 §7).
2. **Ukuran minimal QR pada format cetak** — belum diukur (lihat §5b; masuk daftar `06` §10).
3. **Etika & peruntukan untuk jenis acara selain pernikahan** — menunggu profil L2-nya ada (dokumen 02
   per jenis acara; ditunda pemilik sampai ada demand).
4. **Halaman/struktur amplop di undangan web** — bentuk teknisnya milik dokumen 10 (arsitektur website
   induk) / L3 per unit; dokumen ini menetapkan **isi & aturannya**, bukan tata letak teknisnya.
5. **Sumber ornament/qris asing** — kalau client mengirim QRIS berupa tangkapan layar aplikasi
   (bukan berkas QRIS resmi), itu bahan asli dari client; **jangan digambar ulang** oleh agent (§5a).

### 10. Uji Coba Nyata Pertama (b3) — yang Wajib Diukur

Pada uji coba undangan pertama (rencana **b3**, rekening percobaan = rekening pemilik):

1. Nomor rekening **tampil persis** seperti yang disetujui — dibaca ulang digit per digit dari
   undangan yang sudah terbit, bukan dari rekaman.
2. Tombol salin: hasil salinan **digit murni** (tanpa spasi/tanda baca tambahan).
3. QRIS (bila ada berkasnya): dipindai **dari layar HP** dengan sekurangnya dua aplikasi berbeda.
4. Bagian amplop **tidak muncul** ketika data kosong (diuji dengan sengaja mengosongkan field).
5. Pengalaman tamu: bagian amplop dirasakan sopan — dicatat apa adanya sebagai umpan balik pemilik.

Hasil kelima butir ini **belum ada** saat dokumen ini ditulis; jangan diklaim sebelum b3 dijalankan.

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-21 | **Dokumen diisi — ROADMAP b2**: ruang lingkup & kunci Level-0 · kapan amplop muncul/tidak · data & aturan satu-sumber · etika per acara · aturan teknis (kode fungsional, uji pindai, cetak uji) · titik verifikasi rekening G2/G5 · batas janji · serah terima · yang ditunda · yang wajib diukur di b3; banner kerangka dicabut; `_sistem/validate_system.py` diperluas (5 kerangka → 4 kerangka + 7 terisi; diuji mutasi 3/3); manifest v0.8.0→**v0.9.0**; `STATUS.md` diperbarui — **satu commit** | Handoff log sesi slot 44 (disetujui pemilik): *"isi `11_AMPLOP_DIGITAL.md` (template biasa)"* + mekanika T-69/prompt 02. **Tidak ada keputusan baru pemilik** — semua isi penurunan dari kunci Level-0 + L1 §7/§8/§10 + L2 §3/§5/§6/§9 + skema 03; review isi = PR normal tanpa auto-merge |
| 2026-09-21 | **QRIS diperlakukan sebagai "kode fungsional"** — bukan ornamen, bukan foto: tidak dirancang ulang/diwarnai/diberi efek, ditampilkan pada ukuran aslinya, wajib uji pindai sebelum terbit | **Keputusan agent, dinyatakan sadar.** `06` §1 (Langkah 0) menyebut teks · ornamen/logo · foto — sedangkan QRIS adalah **kode milik penerbit** yang harus tetap terbaca, jadi ia tidak bisa diperlakukan sebagai ornamen yang boleh digambar ulang, dan bukan foto sehingga tidak masuk gerbang resolusi G3. **Gap cakupan ini dilaporkan terbuka** (bukan ditutup dengan menyunting 06 sepihak): pemilik boleh meminta dokumen 06 menyebut golongan ini, atau memperlakukan QRIS dengan cara lain saat review PR |
| 2026-09-21 | **Bagian amplop = bagian tersendiri setelah ucapan/doa, sebelum penutup; judul default "Amplop Digital" dengan opsi "Infaq"/"Tanda Kasih"; nominal tidak ditampilkan kecuali diminta client** | Turunan: penempatan & rangkaian fitur dari `02` §9; peruntukan infaq dari **pola nyata** 2 flyer maulid pemilik (L1 §7); nominal default tanpa nominal dari L1 §7. Pilihan judul = keputusan agent yang mengikuti bentuk acara (`02` §2 kata baku), boleh dikoreksi saat review |
| 2026-09-21 | **Penegakan titik verifikasi rekening: baca balik digit per digit + konfirmasi visual pratinjau + cross-check kedua di G5; buktinya dicatat di Log Keputusan unit** | L1 §10 batasan mutlak #1 mewajibkan cross-check G2/G5 tetapi tidak merinci caranya; rinciannya ditetapkan di sini agar gerbangnya punya **bukti**, mengikuti aturan bukti per aset `06` §8 (*gerbang tanpa bukti = diklaim hijau tanpa dijalankan*). Boleh dikoreksi saat review |
| 2026-09-21 | **Ketika data amplop kosong, bagiannya TIDAK dirender** (tanpa placeholder, tanpa nomor karangan) | Turunan langsung batasan mutlak #1 L1 §10 (info palsu terlarang) + aturan "tidak pernah diisi nilai karangan" `03` bagian 5. Bukan keputusan baru |
