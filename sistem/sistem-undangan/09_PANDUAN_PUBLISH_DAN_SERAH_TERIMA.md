# Panduan Publish Dan Serah Terima

> **STATUS: ISI — DRAFT.** Diisi 2026-09-21 (UTC) lewat **ROADMAP JALAN PRODUKSI PERTAMA,
> butir b2** (handoff log sesi slot 44; dikerjakan sesi slot 45) dengan **prompt Discovery 09**
> (`_sistem/PROMPT_DISCOVERY_09_PUBLISH_DAN_SERAH_TERIMA.md`). Gerbangnya **G5 — kategori BESAR**
> (review isi lengkap pemilik sebelum merge; tanpa auto-merge).
> **Keputusan pemilik: paket D1–D6 disetujui seluruhnya** (*"Setuju semua"*, 21 Sep 2026, log sesi
> slot 45): (D1) fase 1 **hosting tetap di akun studio**, yang berpindah = 5 item serah terima +
> arsip, kepemilikan akun ditunda ke fase 2/3 · (D2) **bentuk tautan permanen** dikunci di sini ·
> (D3) **naik fase tanpa mematikan tautan** (pengalihan otomatis selama masa aktif, biaya nol) ·
> (D4) **fase 1 belum ada CMS** untuk client — perubahan lewat studio, CMS rumahnya dokumen 10 ·
> (D5) undangan **tetap hidup** sampai client bilang berhenti/minta hapus; 1 tahun = titik tawaran
> perpanjangan gratis; data ucapan/RSVP milik client · (D6) **jalur default gratis selamanya**,
> jalur darurat = arsip studio + tautan lama hidup, plafon gratis ditulis apa adanya dengan sumbernya.
> **Bagian yang butuh dokumen 10 (`10_ARSITEKTUR_WEBSITE_INDUK.md` — ditunda pemilik) dinyatakan
> TERBUKA di §11, bukan ditebak** (putusan B6 atas konflik urutan `_sistem/README.md` vs roadmap).
> Banner kerangka dicabut di commit yang sama dengan perluasan validator (mekanika T-69/prompt 02).

| | |
|---|---|
| **Berkas** | `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` |
| **Lapis** | lintas semua lapis — L1 (kebijakan serah terima & masa aktif & akun hosting) · L2 (field wajib-bisa-diubah setelah terbit) · L3 (satu undangan = satu unit: tautan, catatan versi, daftar periksa) |
| **Cara diisi** | **YA — perlu prompt Discovery detail** — **sudah dijalankan 2026-09-21 (UTC)** |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (bagian 2.3 Tahap 6–7 · bagian 4 gerbang G5 · bagian 6 batasan platform & kebijakan domain 3 fase) + `01_IDENTITAS_PEMILIK.md` §6/§8 (masa aktif, serah terima 5 item, arsip, revisi, akun hosting) + `02_PROFIL_JENIS_ACARA.md` §8 (field wajib bisa diubah setelah terbit) + `04_TEMPLATE_BRIEF_UNDANGAN.md` + `05_DISCOVERY_DESAIN_PROMPT.md` §1 (batas janji) + `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` §6 (cetak uji) & §9 (perubahan sesudah tayang) + `11_AMPLOP_DIGITAL.md` §6 (verifikasi rekening) + keputusan pemilik **D1–D6** (21 Sep 2026) |

## Fungsi dokumen ini

Tahap 6–7 SIKLUS: deploy, **hosting di akun CLIENT**, CMS untuk non-coder, masa aktif, dan **cara
revisi setelah tayang**. Ditulis untuk orang yang **tidak punya basic coding**.

**Dua pembaca, dua bagian — ini penting dibaca dulu:**

| Bagian | Pembaca | Isi |
|---|---|---|
| §3–§6 + §10 | **pemilik studio (operator)** | cara menerbitkan, cara menyerahkan, apa yang dijaga |
| §7–§9 | **client** (boleh dikirim apa adanya) | apa yang client miliki, cara minta revisi, apa yang terjadi kalau ada masalah |

**Cara membaca:** tidak ada satu pun langkah di sini yang berbunyi "jalankan perintah ini". Semua
langkah dilakukan lewat **halaman web** (dashboard) dengan tombol. Setiap langkah punya penutup
*"kamu tahu ini berhasil kalau …"* — kalau kalimat itu tidak terbukti, langkahnya **belum berhasil**,
dan itu bukan kegagalan yang perlu dipanikkan: ada langkah pemulihannya di §9.

## Catatan untuk yang mengisinya nanti

Gerbang **G5** = approval **Besar** (sebelum terbit/serah terima). **Syarat mengikat yang sudah dikunci: PATH wajib stabil lintas fase domain** — kalau path berubah saat naik fase, semua tautan yang sudah disebar ke tamu mati dan tidak bisa diperbaiki.

## Isi

### 1. Cara Membaca: Empat Kata yang Sering Ditakuti

Istilah teknis dipakai seminimal mungkin. Empat kata ini tidak bisa dihindari karena semuanya
menyangkut **tautan** — benda yang paling tidak boleh rusak:

| Kata | Artinya dalam satu kalimat | Kenapa penting bagi client |
|---|---|---|
| **Hosting** | tempat tinggal berkas undangan supaya bisa dibuka dari mana saja | kalau hostingnya di akun orang lain, undangan bisa ikut hilang saat akun itu bermasalah |
| **Domain** | nama alamat yang diketik orang (mis. `lee-studio.pages.dev`) | inilah bagian tautan yang paling sering diingat tamu |
| **Subpath** | tambahan di belakang domain yang menandai **satu undangan** (mis. `/rina-budi-0626`) | ini pengenal yang tidak boleh berubah; tamu yang menyimpan tautan lama harus tetap bisa masuk |
| **Deploy / terbit** | menaikkan versi terbaru undangan ke hosting supaya orang lain bisa melihatnya | sebelum deploy, yang ada baru pratinjau; sesudahnya baru benar-benar "tayang" |
| **Cache (dibacakan: kes)** | salinan yang disimpan HP/browser tamu supaya undangan cepat dibuka lagi | sesudah perubahan, tamu yang pernah membuka bisa **masih melihat versi lama beberapa jam** — dinyatakan apa adanya, bukan dijanjikan seketika |
| **Pengalihan (redirect)** | pintu lama yang otomatis memindahkan tamu ke pintu baru | alat utama supaya tautan lama tidak mati saat undangan naik fase domain |

### 2. Keputusan yang Sudah Dikunci (jangan dibongkar diam-diam)

**Dari Discovery Level-0 & L1 (kunci lama):**

- **Tahap Terbit dipisahkan dari Tahap Serah Terima.** Terbit = tindakan teknis; Serah Terima =
  perpindahan kepemilikan/tanggung jawab. Mencampurnya = cara paling umum client kehilangan situsnya.
- **Kebijakan domain 3 fase:** (1) percobaan = subdomain gratis bawaan platform; (2) rilis = **satu
  domain studio**, tiap undangan **subpath**; (3) pengecualian = client mau domain sendiri →
  **client menanggung biayanya**, dan sistem wajib mendukungnya sebagai **opsi**, bukan asumsi.
- **Deploy wajib jalur Git** — platform kerja ini memblokir panggilan API layanan luar, jadi
  penerbitan dilakukan dengan menyambungkan repo ke layanan hosting, bukan "menekan tombol upload"
  dari luar. Akibat praktisnya: **berkas yang jadi sumber kebenaran tinggal di repo**, bukan di
  komputer siapa pun.
- **Situsnya statik.** Tidak ada AI yang menjawab tamu di situs, tidak ada aplikasi yang berjalan
  sendiri. Ini membatasi janji: fitur "pintar" apa pun di situs **bukan** bagian sistem ini
  (kecuali diputuskan lain lewat dokumen 10).
- **Biaya produksi & bulanan Rp 0** di jalur default (L1 §6).

**Keputusan pemilik hari ini (D1–D6) — ringkasnya:**

| # | Keputusan | Akibat yang bisa dilihat client |
|---|---|---|
| **D1** | **Fase 1: hosting tetap di akun studio.** Yang berpindah ke client = **5 item serah terima L1** + **arsip gratis** di studio. Perpindahan kepemilikan akun **ditunda** ke fase 2/3 | client tidak perlu punya akun apa pun; tautan tidak mati; studio masih bisa memperbaiki kalau ada masalah |
| **D2** | **Bentuk tautan permanen dikunci** (§3) | tautan yang sudah disebar ke tamu **tidak akan berubah** |
| **D3** | **Naik fase domain tidak mematikan tautan**: subpath lama tidak pernah dihapus selama masa aktif, dan tautan lama **dialihkan otomatis** ke yang baru | tamu yang menyimpan tautan lama tetap masuk sampai hari-H |
| **D4** | **Fase 1 belum ada CMS** untuk client — perubahan lewat studio; CMS + panel adalah keputusan arsitektur yang rumahnya **dokumen 10** (ditunda) | jangan mengiklankan CMS ke client sebelum ada; yang dijanjikan = studio mengerjakan perubahan |
| **D5** | Undangan **tetap hidup** sampai client bilang berhenti/minta dihapus; **1 tahun = titik tawaran perpanjangan gratis**; data ucapan/RSVP **milik client** | tidak ada penghapusan sepihak; data bisa diminta |
| **D6** | **Jalur default gratis selamanya**; jalur darurat = arsip studio + tautan lama hidup; plafon gratis ditulis apa adanya (§10) | tidak ada tagihan kejutan dari studio; yang gratis disebut gratis, yang berbayar disebut berbayar |

**Yang dinyatakan TERBUKA (bukan keputusan yang saya ambil sendiri):** bagian-bagian yang menuntut
keputusan arsitektur dokumen 10 (panel/CMS, penyimpanan data runtime, mekanisme perutean subpath di
`satu domain`, jadwal alarm plafon) — daftarnya di **§11**. Sampai itu diputus, yang berlaku adalah
**cara manual yang tercatat di sini**, bukan improvisasi.

### 3. Skema Path Permanen (D2) — dikunci di sini, tidak berubah sesudah undangan pertama tersebar

**Bentuk tautan (dipakai selamanya):**

```
fase 1 (percobaan) :  lee-studio.pages.dev/<slug>
fase 2 (rilis)     :  <domain-studio>/<slug>
```

**`<slug>` = pengenal undangan.** Aturannya:

| Aturan | Isinya |
|---|---|
| Bentuk | huruf kecil, angka, dan tanda hubung saja — **tanpa spasi, tanpa huruf besar, tanpa tanda baca** |
| Pola usulan | **nama kedua mempelai (atau nama panggilan) + bulan-tahun acara**, mis. `rina-budi-0626` |
| Kenapa pola ini | bisa **dibacakan lewat telepon/WA tanpa ejaan** dan masih terbaca di tautan yang ditempel di chat |
| Nama sama | kalau slug sudah dipakai, tambahkan pembeda **di belakang** (mis. `rina-budi-0626b`) — **jangan** mengubah pola, jangan memberi angka acak di depan |
| Panjang | pendek saja (usulan ≤ 40 karakter) — tautan panjang salah ketik dan tidak rapi di chat |
| Bahasa | sesuai bahasa undangan; hindari kata yang bisa salah tafsir (hindari angka yang mirip huruf, mis. `0` vs `O`) |
| Perlindungan | **tanpa password** (default L1). Password hanya bila client meminta; kalau ada, sebutkan di serah terima |
| Salah ketik tautan | boleh dibuatkan **tautan pendek/pengalihan tambahan** kapan pun — yang **tidak boleh** adalah mengubah slug itu sendiri |
| Pindah domain | slug **tetap sama**; hanya bagian depannya (domain) yang berubah, dan pengalihan menanganinya (§5) |

**Aturan yang tidak bisa ditawar:** setelah undangan pertama disebar ke tamu, **slug tidak boleh
diubah lagi** — bahkan atas permintaan. Kalau client ingin "nama tautan yang lebih bagus", yang
diberikan adalah **tautan tambahan** yang mengalihkan ke slug lama, bukan penggantian.

> **Kamu tahu skema ini dipatuhi kalau:** pada undangan ke-2 dan seterusnya, slug dibuat dengan pola
> yang sama dan langsung **dicatat di Log Keputusan unit** (satu baris: slug + pembeda kalau ada) —
> tanpa itu, orang berikutnya tidak punya cara tahu slug mana yang sudah terpakai.

### 4. Terbit (Tahap 6) — langkah untuk pemilik studio, tanpa basic coding

**Yang dibutuhkan lebih dulu:** data acara lolos validasi (dokumen 03 §7) · aset lolos **G3**
(dokumen 06) · desain & daftar format disetujui di **G2** (dokumen 05) · pratinjau disetujui client
(**G4**) · amplop digital sudah diverifikasi rekeningnya bila aktif (dokumen 11 §6).

**Langkah A — masukkan undangan ke repo (jalur Git, tidak ada upload manual).**
Letakkan berkas undangan di folder unitnya (satu undangan = satu unit kerja), lalu simpan perubahan
dari halaman GitHub dengan tombol **"Commit changes"**.

> **Kamu tahu ini berhasil kalau:** berkas undangan yang baru muncul di daftar berkas repo pada
> halaman GitHub, dan jam "committed" menunjukkan waktu kamu baru saja menekan tombol.

**Langkah B — sambungkan repo ke layanan hosting (sekali saja per repo).**
Di dashboard Cloudflare: menu **Workers & Pages** → **Create** → **Pages** → pilih **Connect to Git**
→ pilih repo studio → pada bagian build, isi perintah build dengan **kosong** (situs ini statik) dan
arahkan **output folder** ke folder unit undangan → **Save and Deploy**.

> Nama tombol bisa sedikit berbeda saat layanan diperbarui; yang dicari tetap tiga hal: *Connect to Git*,
> *output folder*, dan tombol *Deploy*.
> **Kamu tahu ini berhasil kalau:** dashboard menampilkan status **Success** dan alamat
> `…pages.dev` bisa dibuka di HP kamu. Kalau statusnya Failed, baca kalimat galat yang ditampilkan —
> biasanya arah output folder yang salah, dan itu bisa diperbaiki tanpa mengubah apa pun di undangan.

**Langkah C — set alamat permanen (slug §3).**
Di proyek undangan: **Custom domains / Preview & production alias** → pasang subpath sesuai slug yang
sudah dicatat. **Jangan** memberi slug sementara untuk "nanti diganti" — pemakaian pertama = pemakaian
selamanya.

**Langkah D — daftar periksa SEBELUM tautan disebar** (lakukan berurutan; ini gerbang kecil yang bisa
dibuktikan):

| # | Periksa | Kamu tahu lolos kalau |
|---|---|---|
| 1 | Buka tautan di **HP biasa**, bukan laptop | halaman terbuka < 5 detik pada koneksi seluler biasa |
| 2 | Buka di **jaringan lambat** (mode hemat data / 3G) | teks langsung terbaca walau foto belum muncul semua |
| 3 | Cek **semua isi dari data** (nama, tanggal, jam, tempat, peta, rekening) | sama persis dengan yang disetujui client di G4 — tidak ada satu pun yang berbeda |
| 4 | Baca **digit per digit nomor rekening** dari halaman yang sudah terbit (bila amplop aktif) | cocok dengan yang disetujui client (dokumen 11 §6) |
| 5 | Pindai **QRIS** dari layar HP dengan ≥ 2 aplikasi (bila ada) | nama penerima benar di kedua aplikasi |
| 6 | Cek **musik**: tombol mati berfungsi, tidak berbunyi sendiri | suara baru keluar setelah tamu menekan tombol |
| 7 | Cek **ucapan & RSVP**: kirim satu ucapan percobaan | ucapan percobaan muncul; dihapus sesudahnya |
| 8 | Cek **tampilan di layar kecil** (HP lama/ukuran kecil) | tidak ada tulisan terpotong, tidak perlu digeser ke samping |
| 9 | Cek **flyer/poster** (format tambahan) | terbuka rapi di aplikasi galeri/WhatsApp |
| 10 | Simpan **catatan versi** (tanggal + isi perubahan singkat) di folder unit | tercatat satu baris; tanpa ini, "versi mana yang disetujui client" jadi tebakan |

**Langkah E — serahkan tautan + teks WA siap salin ke client** (isi teks dibuat dari data yang sama,
bukan diketik ulang) → lanjut ke **§6 Serah Terima**. **Terbit ≠ serah terima**: terbit berarti tamu
bisa membuka; serah terima berarti client resmi memegang hasilnya.

### 5. Naik Fase Domain (D3) — supaya tautan lama tidak pernah mati

| Dari → ke | Apa yang berubah | Yang wajib dilakukan supaya tautan lama hidup | Biaya |
|---|---|---|---|
| **Fase 1 → 2** (subdomain gratis → satu domain studio) | hanya **bagian depan** tautan (domain); **slug tetap** | pasang **pengalihan otomatis** dari alamat lama ke alamat baru, dan **pertahankan selama masa aktif** — bukan beberapa minggu | Rp 0 |
| **Fase 2 → 3** (client mau domain sendiri) | domain undangan jadi milik client | client **menanggung biaya domain** (kunci Level-0, sudah diputus); pengalihan dari alamat lama tetap dipertahankan **selama masa aktif** | biaya domain ditanggung client |
| **Domain client kedaluwarsa / mati** | alamat client berhenti | undangan **tetap hidup** di alamat studio (jalur default tidak pernah dihapus); tautan lama tetap berfungsi | Rp 0 |

**Aturan keselamatan:** undangan **selalu punya satu pintu cadangan** di sisi studio. Kalau pintu
milik client mati, tamu masih bisa masuk lewat pintu studio — dan client diberi tahu sebelum hal itu
terjadi, bukan sesudah.

> **Kamu tahu naik fase berhasil kalau:** tautan **lama** dibuka di HP dan tamu **mendarat di halaman
> undangan yang benar** (bukan halaman galat, bukan halaman lain), dan foto/ucapan tetap utuh.
> Diuji pada tautan lama **yang benar-benar sudah disebar**, bukan tautan karangan.

### 6. Serah Terima (Tahap 7) — apa yang berpindah, apa yang tetap

**Waktunya: SESUDAH terbit** dan sesudah client menyetujui versi publikasi. Terpisah dari Tahap 6
(kunci Level-0).

**Yang berpindah ke client — 5 item L1 (semuanya bisa diunduh dari HP, tanpa langkah teknis):**

| # | Item | Bentuk yang diterima client |
|---|---|---|
| 1 | **Tautan undangan aktif** | satu tautan (ditambah password **bila** client meminta — default tanpa password) |
| 2 | **Berkas video** (kalau format video dipilih) | berkas siap diputar/disimpan |
| 3 | **Flyer/poster statis** (bila dipakai) | berkas gambar portrait + landscape |
| 4 | **Gambar QR + teks WA siap salin** | untuk disebar ke tamu; teks turunan dari data, bukan ketikan manual |
| 5 | **Info rekening/QRIS** (bila client menghimpun dana) | rincian yang **sudah diverifikasi** di §4 D-4 |

**Yang TIDAK berpindah di fase 1 (D1) — dan ini disebut apa adanya ke client:**

- **Kepemilikan akun hosting dan proyek deploy: tetap di studio.** Kalimat yang dipakai ke client:
  *"untuk sementara undangannya dirawat di akun studio supaya tidak ada yang bisa rusak — kalau nanti
  mau dipindahkan, itu punya jalur sendiri (fase berikutnya)."*
- **Berkas sumber mentah & skrip**: tetap di studio (client menerima **hasil + arsip**, bukan
  kepemilikan berkas kerja).
- **Data ucapan/RSVP**: **milik client** (D5) — client berhak meminta salinan dan berhak meminta hapus.

**Daftar periksa SERAH TERIMA (dibaca berurutan, dijawab satu per satu, jangan "nanti"):**

| # | Periksa | Kamu tahu ini berhasil kalau |
|---|---|---|
| 1 | Client menerima **5 item** dan sudah membuka/mengunduh minimal satu item dari HP-nya sendiri | client bilang "sudah saya buka" — bukan "sepertinya bisa" |
| 2 | Client **menyimpan tautannya** (disimpan di catatan chat/WA) | client mengirim ulang tautan itu ke kamu dan tautannya sama |
| 3 | **Teks WA siap salin** diuji client sekali | client menempelkannya di chat dan bentuknya rapi |
| 4 | Client tahu **cara minta perubahan** (§7) dan **siapa yang dihubungi** | client mengulang kembali satu kalimat ("kalau ada perubahan, saya WA Anda") |
| 5 | Client tahu **tidak ada penonaktifan sepihak** dan **arsip gratis** ada | client tahu undangan tidak akan hilang sendiri |
| 6 | **Catatan serah terima** dibuat di Log Keputusan unit: tanggal · 5 item · tombol/tautan yang dikirim · hal yang client tanyakan | satu baris tercatat; `Status unit` bisa ditutup |
| 7 | **Arsip studio** diperiksa bisa dibuka | kamu bisa membuka arsip itu dari akun studio tanpa bantuan alat baru |

> **Kamu tahu serah terima SELESAI kalau:** 7 butir di atas beres dan tercatat. Sampai itu, unit
> undangan **belum boleh** ditutup — gerbang tanpa bukti = diklaim hijau tanpa dijalankan
> (prinsip yang sama dengan G3).

### 7. Perubahan Sesudah Tayang (D4) — jujur, fase 1 lewat studio

**Kunci L1:** sebelum terbit revisi **tak terbatas**; sesudah terbit **perubahan kecil (typo, waktu,
tempat, foto) = gratis**, perubahan besar (model/warna/struktur baru) = **tambahan**.

**Field yang wajib bisa diubah setelah terbit** (spesifikasi L2 §8 — jangan diklaim bisa kalau belum
diuji di b3): jam mulai/selesai · tempat/alamat/tautan peta · foto galeri · susunan acara ·
dress code · teks WA sebar. **Nama/gelar** = sensitif → boleh, **lewat konfirmasi** (bukan "ikuti
saja"), karena perubahan nama merembet ke semua format.

**Cara client meminta perubahan (fase 1 — yang dijalankan, bukan yang dikonsep):**

1. Client mengirim WA ke studio: **apa** yang berubah + **kapan** sebaiknya berganti.
2. Studio menyebut **jadwal** kecil/jelas ("besok sore sudah berganti") — jangan "nanti".
3. Studio mengubah dari **satu sumber data**, bukan mengedit tampilan satu per satu.
4. Perubahan dibuka ulang di HP oleh studio, lalu **client diberi tahu saat sudah tayang**.
5. Client mengecek sendiri dari HP-nya. **Cache:** tampilan lama bisa masih muncul **beberapa jam** —
   jalan pintas: buka tautan + tanya "sudah berubah atau belum"; kalau belum, tunggu/muat ulang.
   Ini disampaikan di muka supaya tidak terasa seperti kegagalan.

**Perubahan yang menyentuh foto** → foto pengganti **wajib lewat G3 lagi** untuk foto itu (dokumen 06
§9): kalau tidak lolos, jangan dipasang diam-diam — tawarkan jalan keluarnya (dokumen 06 §5).
**Perubahan yang menyentuh nomor rekening** → wajib ulangi baca balik + cross-check §4 D-4, lalu
minta client mengabari tamu yang sudah menyebar (dokumen 11 §6).

**CMS untuk client sendiri:** **belum ada di fase 1 (D4)** — dan **tidak boleh diiklankan**. Kalau
client bertanya, jawab apa adanya: *"sekarang saya yang ubah; nanti kalau ada fitur panel, saya kabari."*
Rumah keputusan itu = **dokumen 10** (§11).

**Apa yang bukan urusan client (dan bukan janji):** menekan tombol terbit sendiri, mengubah
desain/struktur, atau memasang fitur baru. Semuanya lewat studio.

### 8. Masa Aktif & Nasib Data (D5) — bagian yang boleh dikirim ke client

- **Masa aktif default: 1 tahun sejak acara.** Perpanjangan **gratis**, **tanpa penonaktifan sepihak**
  (kunci L1). **Tahun itu titik penawaran**, bukan titik mati otomatis.
- **Sesudah 1 tahun:** undangan **tetap hidup** sampai client bilang berhenti atau minta dihapus.
  Kalau client memilih berhenti: undangan disimpan sebagai **arsip** di studio, dan client **boleh
  memintanya kembali kapan pun, gratis**.
- **Data ucapan/RSVP:** **milik client**, disimpan selama masa aktif, dan client boleh **minta
  salinan** atau **minta dihapus** (putusan B5 atas dokumen 05 §5 — tidak ada moderasi default).
- **Pemberitahuan:** kalau ada perubahan yang memengaruhi undangan (mis. masa aktif hampir habis,
  perubahan teknis di sisi studio), **client diberi tahu lebih dulu**, tidak menunggu ditanya.

### 9. Pemulihan (Rencana Darurat) — dijawab sekarang, bukan saat panik

| Kejadian | Yang terjadi | Langkah pemulihan | Janji |
|---|---|---|---|
| **Tamu bilang tautan tidak bisa dibuka** | bisa salah ketik, bisa cache, bisa gangguan sementara | cek tautan dari HP lain → cek status halaman di dashboard hosting → kirim ulang tautan yang benar | tidak menjanjikan "seketika"; yang dijanjikan: **diperiksa hari itu** dan client dikabari apa adanya |
| **Akun studio bermasalah / lupa akses** | studio kehilangan jalan masuk ke proyek | pakai **email pemulihan** yang tercatat di akun tersebut; kalau perlu, deploy ulang dari repo (sumber ada di repo, bukan di satu komputer) | tidak ada tautan yang mati hanya karena satu akun bermasalah |
| **Domain client kedaluwarsa** (fase 3) | alamat milik client berhenti | undangan **tetap hidup** di alamat studio; client diberi tahu dan diberi tautan studio | **tautan kehilangan domainnya, tapi undangannya tidak hilang** |
| **Gangguan hosting di hari-H** | halaman tidak terbuka sementara | pakai **flyer/poster statis** yang sudah diserahkan sebagai jalur cadangan informasi; pantau status layanan; beri tahu client apa adanya | tidak menjanjikan SLA; yang dijanjikan: **jalur cadangan sudah ada di tangan client** |
| **Perubahan mendadak di hari-H** (jam/venue) | data harus cepat berganti | ubah dari satu sumber → terbit ulang → kirim teks WA baru + minta client menyebar ulang | dikerjakan **secepat mungkin**; cache beberapa jam disampaikan jujur |

**Pertanyaan yang masih TERBUKA (dinyatakan, bukan dijawab sendiri):** apakah studio menjanjikan
**respons hari yang sama** pada hari-H (janji layanan). Sampai pemilik memutuskan, yang berlaku:
undangan diperiksa **hari itu** dan client dikabari apa adanya — **tanpa** menuliskan jam/angka
respons di panduan client. Menaikkan ini jadi janji tertulis = keputusan pemilik.

### 10. Biaya & Plafon (D6) — gratisnya disebut gratis, batasnya disebut apa adanya

**Yang gratis selamanya di jalur default:** hosting statis (request & bandwidth statis tanpa batas
pada free tier) · font berlisensi bebas · ornament vektor buatan sendiri · penerbitan ulang ·
perpanjangan masa aktif · arsip & pemulihan berkas.

**Yang bisa membuat ada biaya (disebut di muka, tidak disembunyikan):**

| Hal | Batas / biaya | Siapa menanggung | Sumber angka |
|---|---|---|---|
| **Domain sendiri** (fase 3) | harga domain ditentukan penyedia; belum diriset di dokumen ini | **client** (kunci Level-0) | `00_RENCANA_KERANGKA.md` bagian 6 (kebijakan domain 3 fase) |
| **Kuota penyimpanan berkas besar (R2)** | **10 GB** tanpa biaya keluaran (egress) | studio di jalur default; D6: studio menanggung, client diberi tahu lebih dulu | `_sistem/PROMPT_DISCOVERY_09_PUBLISH_DAN_SERAH_TERIMA.md` (angka riset 17 Sep 2026, area internal master — provenance) |
| **Kuota basis data harian (D1)** — dipakai RSVP/ucapan ramai | **5 juta baris dibaca/hari**, **100 ribu baris ditulis/hari**; **sejak 1 Sep 2026 melewati plafon = berhenti sampai reset 00:00 UTC** (bukan tagihan) | studio menanggung langkah tambahan; client tidak ditagih (D6) | idem |
| **Penyimpanan sementara (KV)** | **1 GB** | studio | idem |
| **Layanan berbayar lain** (mis. video, cetak, domain) | ada dokumennya sendiri (07/08) yang **ditunda** pemilik; jangan dijanjikan | — | `05_DISCOVERY_DESAIN_PROMPT.md` §1 |

**Cara menjelaskan plafon ke client (kalimat siap pakai):** *"Undangan ini jalan tanpa biaya bulanan.
Ada batas teknis bawaan layanan gratis untuk buku tamu/RSVP yang sangat ramai — kalau sampai tersentuh,
sistemnya berhenti sebentar lalu hidup lagi sendiri; kalau sampai kejadian, saya kabari."*

**Yang WAJIB terjadi kalau plafon tersentuh:** (1) **jangan** menyembunyikan; (2) catat kejadiannya
(tanggal + apa yang tampak di layar tamu); (3) beri tahu pemilik; (4) sesudah pulih, evaluasi apakah
butuh langkah tambahan. **Apa langkah tambahan itu = keputusan pemilik**, bukan improvisasi.

### 11. Yang Belum / Dinyatakan TERBUKA (butuh dokumen 10 — jangan ditebak)

`10_ARSITEKTUR_WEBSITE_INDUK.md` **ditunda pemilik** sampai ada demand. Bagian dokumen ini yang
**bergantung** padanya dan sengaja **dibiarkan terbuka** (putusan B6 — bagian terbuka lebih jujur
daripada keputusan yang dipaksakan):

1. **Mekanisme perutean subpath di "satu domain"** (bagaimana beberapa undangan berbagi satu domain
   secara teknis) — yang **sudah dikunci di sini** hanya **bentuk** tautannya (§3), bukan cara
   mesinnya mengarahkan.
2. **Panel/CMS & tempat penyimpanan data runtime** (ucapan, RSVP, check-in): skema, tempat, dan
   siapa yang boleh membaca.
3. **Alarm plafon** (peringatan otomatis sebelum kuota harian tersentuh) — mitigasinya sudah tercatat
   sebagai rencana di riset, tetapi belum ada keputusan bentuknya.
4. **Alur upload foto client tanpa teknisi** (kalau nanti diputuskan ada).
5. **Bentuk akhir halaman website induk** (daftar undangan, pengelolaan client).

**Hal lain yang belum ada dan tidak boleh diklaim:**

6. **CMS sudah jalan di fase 1** — tidak ada (D4); jangan diiklankan.
7. **Angka yang belum diukur:** lead time 3 hari kerja (dokumen 05 §4 — wajib diukur di produksi
   nyata pertama) · target layar ≤2000 px / ±≤300 KB per foto (dokumen 06 §2 — operasional, bukan
   hasil uji) · ukuran minimal QR cetak (dokumen 06 §10/11 §5b).
8. **Uji di dunia nyata:** daftar periksa Terbit (§4 D) dan Serah Terima (§6) **wajib diuji pada
   satu undangan nyata (rencana b3) sebelum panduan ini dinyatakan layak pakai** — panduan yang
   belum pernah dipakai sekali pun belum terbukti.
9. **Janji respons hari-H** (§9) — menunggu keputusan pemilik.

### 12. Angka & Sumbernya (auditable tanpa membaca riwayat diskusi)

| Angka | Nilai | Sumbernya |
|---|---|---|
| Plafon baca basis data **D1** | **5 juta baris/hari** | `_sistem/PROMPT_DISCOVERY_09_PUBLISH_DAN_SERAH_TERIMA.md` (riset 17 Sep 2026; area internal master = provenance) |
| Plafon tulis basis data **D1** | **100 ribu baris/hari**; melewatinya = **berhenti sampai reset 00:00 UTC** | idem |
| Penyimpanan sementara **KV** | **1 GB** | idem |
| Penyimpanan berkas besar **R2** | **10 GB**, tanpa biaya keluaran | idem |
| Hosting statis | request & bandwidth statis **tanpa batas**, tanpa biaya bulanan | `01_IDENTITAS_PEMILIK.md` §6/§8 (terukur 2026) |
| Biaya produksi & bulanan jalur default | **Rp 0** | `01_IDENTITAS_PEMILIK.md` §6 |
| Lead time janji studio | **3 hari kerja** (+ revisi tak terbatas sebelum terbit) — **wajib diukur** | `05_DISCOVERY_DESAIN_PROMPT.md` §4 |
| Masa aktif | **1 tahun** sejak acara + perpanjangan gratis | `01_IDENTITAS_PEMILIK.md` §6 |
| Rentang harga pasar (rujukan, bukan harga studio) | Rp 50.000–500.000 sekali bayar | `01_IDENTITAS_PEMILIK.md` §6 (riset 6–7 penyedia) |
| Riset & skrip uji asal angka plafon | disimpan di **area internal master** — **provenance, tidak ikut** bila folder ini dipisah, dan **tidak disalin** ke sini | `00_RENCANA_KERANGKA.md` bagian 6 (penunjuk sumber) |

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| 2026-09-21 | **D1 — Fase 1 hosting tetap di AKUN STUDIO; yang berpindah = 5 item serah terima L1 + arsip gratis; perpindahan kepemilikan akun ditunda ke fase 2/3** | **Putusan pemilik** (paket D1–D6, *"Setuju semua"*, log sesi slot 45) atas **benturan yang dilaporkan agent, tidak ditebak**: `00_RENCANA_KERANGKA.md` bagian 2.3 Tahap 7 berbunyi *"hosting di **akun client**"* sedangkan kebijakan domain fase 1 menempatkan undangan di **subdomain studio** — keduanya tidak bisa benar sekaligus di fase 1. Kukuh dengan kunci L1 §8 (*"client menerima link + arsip, bukan kepemilikan akun"*) |
| 2026-09-21 | **D2 — Skema path permanen DIKUNCI: `lee-studio.pages.dev/<slug>` (fase 1) → `<domain-studio>/<slug>` (fase 2); slug = nama mempelai + bulan-tahun; slug tidak boleh berubah sesudah undangan pertama tersebar; tautan tambahan/pengalihan boleh, penggantian slug tidak** | Putusan pemilik (D1–D6). Menegakkan syarat **PATH stabil lintas fase** (`00` bagian 6.3) — kalau path berubah, tautan yang sudah disebar **mati dan tidak bisa diperbaiki**. Bentuk & aturan rincinya ditulis di sini karena dokumen 10 (arsitektur) masih ditunda; **dokumen 09 memberi bentuk, dokumen 10 nanti memberi mesinnya** — keduanya wajib kompak |
| 2026-09-21 | **D3 — Naik fase domain TIDAK mematikan tautan: subpath lama tidak pernah dihapus selama masa aktif + pengalihan otomatis dipertahankan selama masa aktif (bukan beberapa minggu); kalau domain client mati, undangan tetap hidup di alamat studio** | Putusan pemilik (D1–D6). Biaya nol (jalur default); melindungi tamu yang menyimpan tautan lama sampai hari-H |
| 2026-09-21 | **D4 — Fase 1 BELUM ada CMS untuk client; perubahan lewat studio (WA → studio ubah → client diberi tahu); CMS/panel adalah keputusan arsitektur dokumen 10 dan TIDAK BOLEH diiklankan ke client** | Putusan pemilik (D1–D6). Kejujuran batas kapabilitas (aturan yang sama dengan dokumen 05 §1: yang belum ada tidak dijanjikan). Mengikat juga `_sistem/PROMPT_DISCOVERY_09...` butir 2 (*"kalau jawabannya 'client tidak bisa mengubah apa pun sendiri', katakan itu dengan jujur"*) |
| 2026-09-21 | **D5 — Undangan tetap hidup sampai client bilang berhenti/minta dihapus; 1 tahun = titik penawaran perpanjangan GRATIS; data ucapan/RSVP milik client (boleh minta salinan/hapus); tidak ada penonaktifan sepihak** | Putusan pemilik (D1–D6) di atas kunci L1 §6 + putusan B5 (log sesi slot 45) |
| 2026-09-21 | **D6 — Jalur default gratis selamanya; jalur darurat = arsip studio + tautan lama hidup; plafon gratis ditulis apa adanya dengan sumbernya; kalau plafon tersentuh, studio menanggung langkah tambahan dan client tidak ditagih** | Putusan pemilik (D1–D6). Memenuhi permintaan prompt 09 butir 2 (*"sebutkan plafon terukur apa adanya, termasuk akibat HARD FAIL D1"*) |
| 2026-09-21 | **Daftar periksa Terbit (10 butir) & Serah Terima (7 butir) ditetapkan sebagai gerbang kecil yang WAJIB diuji pada satu undangan nyata (b3) sebelum panduan ini layak dipakai** | Turunan `_sistem/PROMPT_DISCOVERY_09...` bagian "Setelah selesai" butir 3 (*"panduan yang belum pernah dipakai sekali pun belum terbukti"*). Duduk di atas prinsip bukti yang sama dengan G3 (`06` §8): gerbang tanpa bukti = diklaim hijau tanpa dijalankan |
| 2026-09-21 | **Keputusan agent yang dinyatakan sadar** (boleh dikoreksi pemilik saat review PR): (a) pola slug `nama-mempelai + bulan-tahun` + aturan pembeda di belakang; (b) istilah teknis diterjemahkan di §1 (hosting/domain/subpath/deploy/cache/pengalihan); (c) urutan 10 + 7 butir daftar periksa; (d) tabel angka & sumber §12; (e) bagian terbuka §11 dipisah dari bagian yang sudah dikunci — **tanpa menutup gap dengan menebak** | Kaidah pelaporan repo: konflik/gap **dilaporkan terbuka, tidak ditebak** (preseden benturan G1 & B6). Semua butir ini **bukan** keputusan pemilik; yang berkaitan dengan keputusan pemilik sudah berlabel D1–D6 |
| 2026-09-21 | **Janji respons hari-H: DIBIARKAN TERBUKA** — tidak ada angka/jam respons yang ditulis di panduan client; yang berlaku = diperiksa **hari itu** dan client dikabari apa adanya | Janji layanan = keputusan pemilik yang **belum** diputuskan (dua pertanyaan bertema itu dijawab sebagai **bukan janji**); menuliskannya lebih dulu berarti mengarang janji atas nama pemilik — dilarang oleh prompt 09 butir 4 |
| 2026-09-21 | **Dokumen diisi — ROADMAP b2 (butir terakhir)**: seluruh isi §1–§12 + Log Keputusan; banner kerangka dicabut; `_sistem/validate_system.py` diperluas (4 kerangka → **3 kerangka + 8 terisi**; diuji mutasi 3/3); manifest v0.9.0→**v0.10.0**; `STATUS.md` diperbarui — **satu commit** | Handoff log sesi slot 44 (disetujui pemilik) + prompt Discovery 09 (`_sistem/`) + mekanika T-69/prompt 02. **G5 menunggu review isi lengkap pemilik** (kategori BESAR) — PR normal **tanpa auto-merge** |
