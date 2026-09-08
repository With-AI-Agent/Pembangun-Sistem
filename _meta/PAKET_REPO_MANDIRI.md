# Paket Repo Mandiri

### Protokol untuk mengeluarkan SATU sistem domain dari repo master ini menjadi SATU folder repo yang berdiri sendiri dan siap di-upload ke GitHub — dengan satu perintah, tanpa pemilik memisah-misahkan file secara manual, dan tanpa satu bait pun isi dokumen ditulis ulang.

> Alat pelaksana: `tools/pack_repo.py`. Dokumen ini adalah **aturannya**; alat itu adalah **penegaknya**. Kalau keduanya berbeda, dokumen ini yang benar dan alatnya yang salah.

---

## Kenapa protokol ini ada

`00_CARA_KERJA_META.md` sudah lama menyatakan prinsip pemilik: *"Setiap sistem dibangun SELF-CONTAINED karena akan dipisahkan"* — alur pakai nyatanya adalah mengunduh folder sistem dan menjadikannya repo tersendiri. Yang belum ada sampai 7 Sep 2026 adalah **cara melakukannya yang bisa diulang dan dibuktikan**. Tanpa itu, "pisahkan sistemnya" berarti pemilik menyalin file satu-satu, menebak dokumen `_meta/` mana yang benar-benar dipakai, dan menemukan rujukan yang putus setelah repo baru sudah terlanjur di-upload.

Protokol ini menutup celah itu dengan satu jaminan yang bisa diverifikasi mesin: **kalau paket berhasil dibangkitkan, paket itu tervalidasi; kalau tidak tervalidasi, paketnya tidak ada.**

---

## 1. Definisi normatif "siap di-upload"

Sebuah folder hasil pack disebut **siap di-upload** hanya bila keempat syarat berikut terpenuhi **di dalam folder hasil pack itu sendiri** (bukan di master):

| # | Syarat | Cara membuktikan |
|---|---|---|
| i | `tools/validate_repo.py` **PASS dengan 0 warning** | jalankan dari root hasil pack; baris `WARNINGS: 0` dan exit code 0 |
| ii | Validator sistem PASS | jalankan `validate_system.py` milik sistem itu (ada di `_sistem/` sistem) dari root folder sistem; exit code 0 |
| iii | **Tidak ada rujukan menggantung** (pada dokumen aktif) | setiap rujukan ber-backtick berbentuk path **di dokumen aktif** (definisi tunggal: bagian 3b) resolve, KECUALI yang terdaftar eksplisit di `absent_refs_allowed` (bagian 5). Rujukan dari dokumen **non-aktif** tidak menggugurkan syarat ini — ia dicatat terpisah di `PAKET_REPO.md` (bagian 5) |
| iv | `PAKET_REPO.md` menyebut **sha commit sumber** dan **sha256 tiap file** | baca berkas itu; hitung ulang sha256 kalau ragu |

Keempatnya dijalankan otomatis oleh alat. Syarat i–ii dijalankan **setelah** paket ditulis; kalau salah satu merah, paket **dihapus** dan perintah keluar dengan exit code non-nol (bagian 7).

Perhatikan apa yang TIDAK termasuk definisi ini: "kelihatannya lengkap", "sudah saya cek manual", "harusnya jalan". Materialitas temuan bukan wewenang alat maupun penulisnya — itu hak reviewer independen (`_meta/PROTOKOL_REVIEW_INDEPENDEN.md`).

---

## 2. Isi paket

Layout root hasil pack **sama persis dengan master**. Folder sistem tetap berupa subfolder `sistem-<nama>/`, TIDAK dinaikkan menjadi root.

```
<hasil-pack>/
├── sistem-<nama>/          ← folder sistem UTUH, byte-per-byte
├── _meta/                  ← HANYA subset yang benar-benar dirujuk (bagian 3)
│   └── PAKET_REPO.json     ← profil repo (bagian 6)
├── tools/
│   ├── checkpoint_core.py
│   └── validate_repo.py
├── PANDUAN_PENGGUNA.md     ← salinan byte-per-byte dari master
├── PROMPT_ENTRI_UNIVERSAL.md  ← salinan byte-per-byte dari master
├── LOG_SESI.md             ← sengaja KOSONG (repo baru memulai lognya sendiri)
├── README.md               ← BARU, dibangkitkan
├── PAKET_REPO.md           ← BARU, dibangkitkan (bagian 8)
├── .gitignore              ← salinan byte-per-byte
└── .gitattributes          ← salinan byte-per-byte
```

**Kenapa layout dipertahankan identik** (putusan pemilik, FINAL): karena setiap rujukan di dalam dokumen ditulis relatif terhadap layout master. Menaikkan `sistem-<nama>/` menjadi root berarti menulis ulang path di puluhan dokumen — persis yang dilarang. Konsekuensi yang dikejar: **nol rewriting path, semua rujukan tetap valid, dan `tools/validate_repo.py` bisa dipakai apa adanya di repo baru.**

Folder sistem ikut **utuh**, termasuk fixture, folder produksi aktif, folder sistem internal, dan folder panduan. Fixture ikut karena ia state hidup yang menjadi bukti perilaku sistem; membuangnya membuat validator sistem kehilangan objek uji.

---

## 3. Aturan penentuan subset `_meta/`

Yang ikut BUKAN inventaris inti penuh, melainkan **transitive closure dari rujukan nyata**:

1. **Tingkat 0 (benih).** Pindai **dokumen aktif** sistem + pegangan pengguna root — persis himpunan yang dikembalikan fungsi `dokumen_aktif()` di `tools/checkpoint_core.py` (definisi tunggal, bagian 3b), **dikurangi** berkas `_meta/` itu sendiri (subset `_meta/` justru yang sedang dihitung). Ambil setiap rujukan ber-backtick berbentuk path yang menunjuk `_meta/...`.

   **Kenapa benih memakai definisi dokumen aktif, bukan "semua `.md` sistem":** dokumen bukti run (`ACCEPTANCE_TEST_LOG.md`) dan diskusi mentah (`DISKUSI_MENTAH*`) bukan dokumen aktif. Sebelum 8 Sep 2026 benih memindai semua `.md` sehingga **menulis bukti run ikut mengubah isi paket** — angka yang baru dicatat langsung basi. Dengan benih = dokumen aktif, menulis bukti tidak lagi menggeser subset `_meta/`. Jangan kembalikan benih ke "semua dokumen"; kalau cakupan dokumen aktif berubah, ubah definisinya (bagian 3b) — bukan menambah daftar di alat.
2. **Perluasan.** Untuk tiap berkas `_meta/*.md` yang sudah masuk, pindai rujukannya dan tambahkan berkas `_meta/*.md` baru yang ditemukan. **Ulangi sampai fixpoint** (tidak ada tambahan baru).
3. **Wajib.** `_meta/INDEKS_SISTEM.md` selalu ikut — `tools/validate_repo.py` membacanya sebagai sumber daftar sistem; tanpa itu validator di repo baru tidak punya objek.
4. **Rekursi tidak berlaku untuk `_meta/_internal/`** (bagian 4).

**Kenapa fixpoint, bukan berhenti di satu tingkat.** Syarat 1(i) menuntut 0 warning. Kalau berkas `_meta/` yang ikut membawa rujukan ke berkas `_meta/` yang tidak ikut, rujukan itu menggantung dan syarat i gagal. Dalam praktik pada 7 Sep 2026 closure kedua sistem konvergen pada **kedalaman 2**, jadi fixpoint dan "rekursif satu tingkat di atas benih" menghasilkan set yang sama; alat mencetak kedalaman masuk tiap berkas di keluaran `--check` supaya perbedaannya bisa dilihat, bukan diasumsikan.

**Yang tidak ikut hanya karena "biasanya penting".** Dokumen `_meta/` yang tidak pernah dirujuk sistem tidak ikut, sekalipun ia dokumen besar di master. Itu bukan kelalaian — itu definisi subsetnya. Kalau sebuah dokumen ternyata memang dibutuhkan sistem saat dipakai, obat yang benar adalah **merujuknya dari dokumen sistem** (dan dengan itu ia masuk closure secara otomatis), bukan menambahkannya diam-diam ke daftar di dalam kode.

---

## 3b. Apa yang dihitung sebagai dokumen aktif

Satu definisi, satu sumber kebenaran, dipakai oleh **validator** (`tools/validate_repo.py`, untuk memindai rujukan path) **dan** **packager** (`tools/pack_repo.py`, untuk benih subset `_meta/`): fungsi `dokumen_aktif(root, sistem)` di `tools/checkpoint_core.py`, bersama tiga konstanta di berkas yang sama — `ACTIVE_DOC_GLOBS`, `ACTIVE_DOC_EXCLUDE_DIRS`, `ACTIVE_DOC_EXCLUDE_NAMES`. Alat lain TIDAK boleh membawa salinan daftar glob sendiri; kalau cakupan berubah, ubah di `tools/checkpoint_core.py` saja.

**Termasuk** (globs): `_meta/*.md` dan pegangan pengguna root (`PANDUAN_PENGGUNA.md`, `PROMPT_ENTRI_UNIVERSAL.md`) untuk semua repo; plus untuk sistem `{name}`: `{name}/*.md`, `{name}/_sistem/*.md`, `{name}/panduan/*.md`, `{name}/_generator/*.md`, `{name}/_template/*.md`.

**Dikecualikan** (selalu, apa pun sistemnya):

| Pengecualian | Alasan |
|---|---|
| Direktori `_internal/` | audit & handoff historis = referensi, bukan instruksi aktif |
| Direktori `deck-aktif/`, `unit-aktif/`, `_produksi-aktif/` | state kerja per unit — diperiksa aturan C-01 dan alat sistemnya sendiri, bukan validator path |
| `00_RENCANA_KERANGKA.md` | rencana kerangka = sejarah (penomoran final terdokumentasi di dalam berkas) |
| `ACCEPTANCE_TEST_LOG.md` | catatan run uji (bukti). Menulis bukti TIDAK boleh mengubah isi paket — inilah perbaikan akar masalah yang membuat angka bukti basi |
| `DISKUSI_MENTAH*` | diskusi mentah discovery, bukan aturan aktif |

Konsekuensi yang disengaja: dokumen yang dikecualikan di atas **tetap ikut** sebagai bagian utuh folder sistem (bagian 2 — folder sistem disalin byte-per-byte), tapi ia tidak dipindai validator dan tidak menjadi benih subset `_meta/`. Rujukan path-nya ke berkas master yang tidak ikut dicatat di `PAKET_REPO.md` (bagian 5) supaya tidak menggantung tanpa jejak.

---

## 4. Apa yang boleh masuk `_meta/_internal/`

Default: **tidak ikut sama sekali**. `_meta/_internal/` berisi audit dan handoff historis — referensi, bukan instruksi aktif.

Pengecualian tunggal: **berkas `_meta/_internal/` yang dirujuk LANGSUNG oleh dokumen AKTIF sistem (tingkat 0)** ikut apa adanya. Contoh nyata: laporan audit sistem yang dipakai manifest sistem sebagai *provenance* temuan yang masih terbuka. Tanpa berkas itu, tabel temuan di manifest kehilangan sumbernya dan manifest jadi mengklaim sesuatu yang tidak bisa ditelusuri. Dokumen non-aktif (bagian 3b) TIDAK menarik lampiran `_meta/_internal/` — rujukannya dicatat terpisah (bagian 5).

Aturan turunannya, semuanya mengikat:

- Rujukan `_meta/_internal/` dari berkas `_meta/` (bukan dari dokumen sistem) **tidak** menarik berkas apa pun — tidak ada rekursi ke dalam area historis.
- Berkas `_meta/_internal/` yang ikut **tidak** dipindai untuk memperluas closure. Ia dibawa sebagai lampiran, bukan sebagai simpul graf.
- Arsip, cadangan, dan artefak build di dalam `_meta/_internal/` (folder backup, folder/berkas template bersih) **tidak pernah** ikut.

---

## 5. Rujukan master-only dan `absent_refs_allowed`

Sebagian dokumen `_meta/` bicara tentang mesin master itu sendiri: alat regresi meta, sistem domain lain, fixture pilot. Rujukan semacam itu **tidak bisa** dan **tidak seharusnya** resolve di repo mandiri. Menghapusnya dari dokumen = menulis ulang isi = dilarang. Membiarkannya diam-diam = rujukan menggantung yang tidak terdeteksi.

Jalan ketiga yang dipakai protokol ini: **daftar putih eksplisit bernama `absent_refs_allowed`**, disimpan sebagai DATA di dalam paket (di profil, bagian 6), bukan sebagai kelonggaran di dalam kode.

**Sifatnya:**

- **Eksplisit.** Setiap entri menyebut path rujukan + alasan satu kalimat. Tidak ada rujukan yang "tahu-tahu ditoleransi".
- **Dibangkitkan, bukan dikarang.** Alat menghitungnya dari hasil pemindaian paket yang sudah jadi; ia mendaftar rujukan yang BENAR-BENAR muncul dan BENAR-BENAR tidak resolve.
- **Tidak boleh membusuk.** Entri yang tidak lagi cocok dengan rujukan nyata — karena dokumennya berubah, atau karena berkasnya sekarang ada — adalah **error**, bukan sisa yang dimaafkan. Validator di repo mandiri menolaknya. Tanpa aturan ini, daftar putih perlahan menjadi tempat sampah yang menyembunyikan kerusakan baru.
- **Tertutup terhadap yang baru.** Rujukan menggantung yang TIDAK terdaftar tetap error. Daftar putih tidak pernah bekerja sebagai pola atau awalan; ia mencocokkan path secara persis.

**Kategori yang sah** (kategori lain harus dibahas dulu, bukan ditambahkan sepihak):

| Kode | Kategori | Contoh alasan |
|---|---|---|
| K1 | Sistem domain lain | dokumen master menunjuk sistem yang memang tidak ikut paket ini |
| K2 | Alat meta yang sengaja tidak ikut | alat regresi meta di master; repo mandiri hanya membawa dua alat (bagian 2) |
| K3 | Fixture/pilot master | fixture uji meta-sistem, bukan sistem domain |
| K4 | Artefak build/arsip master | berkas yang di master pun tidak di-commit |

Rujukan ber-backtick yang **diawali `sistem-`** dan menunjuk folder tingkat-atas yang tidak ada di paket adalah kasus K1 yang paling sering; ia ditoleransi **hanya** kalau tercantum di `absent_refs_allowed`.

**Rujukan dari dokumen NON-aktif.** Dokumen non-aktif (bagian 3b) ikut sebagai bagian utuh folder sistem tetapi tidak dipindai validator. Kalau dokumen semacam itu menunjuk berkas master yang tidak ikut paket, rujukannya **tidak** masuk `absent_refs_allowed` (dokumennya memang tidak dipindai) dan **tidak** menggugurkan syarat iii — ia dicatat di `PAKET_REPO.md` bagian **"Rujukan yang tidak dijamin resolve (dokumen non-aktif)"**. Ini catatan keterbukaan, bukan kelas toleransi kedua: rujukan yang muncul di dokumen AKTIF tetap lewat `absent_refs_allowed` seperti biasa, dengan semua aturannya (eksplisit, dibangkitkan, tidak boleh membusuk). Jangan melemahkan pemindaian dengan menambahkan dokumen non-aktif ke cakupan validator hanya supaya rujukannya "dilihat" — jalur yang benar adalah catatan terpisah ini.

---

## 6. Profil repo (berkas `PAKET_REPO.json` di dalam `_meta/`)

Profil adalah kontrak yang membuat repo mandiri bisa memakai `tools/validate_repo.py` yang sama dengan master tanpa mengubah kodenya.

Isi wajib:

- `sistem`, `versi`, `sumber_commit`, `tanggal`, `schema`;
- `meta_subset` — daftar berkas `_meta/` yang ikut;
- `tools_subset` — daftar berkas `tools/` yang ikut;
- `root_files` — daftar berkas root yang ikut;
- `absent_refs_allowed` — daftar objek `{ref, kategori, alasan}` (bagian 5).

**Aturan penegakan (tidak boleh dilunakkan):**

1. **Tanpa profil, perilaku alat tidak berubah sama sekali.** Di master profil tidak ada, jadi master memakai inventaris inti statis persis seperti sebelum 7 Sep 2026 — bit-for-bit sama.
2. **Dengan profil, kewajiban file diambil dari profil.** Setiap entri yang dideklarasikan profil **HARUS ADA**. Berkas wajib yang hilang tetap FAIL dengan berisik. Profil mempersempit *daftar* kewajiban; ia tidak pernah melunakkan *penegakannya*.
3. **Kelonggaran hidup sebagai data, bukan sebagai kode.** Tidak ada cabang di dalam alat yang berbunyi "kalau ini repo mandiri, maafkan X". Yang dimaafkan hanya apa yang tertulis di profil — dan profil ikut di dalam paket, bisa dibaca, bisa diaudit, bisa dibandingkan antar versi.

---

## 7. Kegagalan berarti tidak ada paket

Alat **tidak pernah** meninggalkan paket setengah jadi:

- Mode pemeriksaan (`--check`) tidak menulis apa pun. Kalau ada pemblokir, ia mencetak daftarnya dan keluar dengan exit code non-nol.
- Mode tulis membangkitkan paket, lalu menjalankan validator repo dan validator sistem **di dalam hasil pack**. Kalau salah satu merah: hasil pack **dihapus**, penyebabnya dicetak, exit code non-nol.

Fail-loud, bukan "dibuat dulu lalu dibuang diam-diam". Pemilik tidak boleh menemukan folder yang tampak jadi padahal gagal validasi.

**Determinisme.** Urutan berkas stabil (terurut path), manifest sha256 tidak memuat timestamp, dan dua kali run ke folder berbeda menghasilkan pohon yang identik (`diff -r` kosong). Tanggal muncul hanya di badan `PAKET_REPO.md` dan di profil sebagai data pack, bukan di dalam manifest sha256.

Angka bukti paket harus diambil dari run pada SHA yang dicatat; bila SHA itu bukan HEAD, tulis apa adanya sebagai commit sumber bukti, seperti entri PR #21.

---

## 8. Tiga suntingan yang diizinkan — selain ini, salin byte-per-byte

Ini pagar terpenting protokol: **tidak satu bait pun isi dokumen ditulis ulang.** Hanya tiga penulisan yang boleh dilakukan alat:

| # | Suntingan | Apa persisnya |
|---|---|---|
| 1 | tabel "Daftar Sistem" di salinan `_meta/INDEKS_SISTEM.md` | tabel dipangkas jadi **satu baris** (sistem yang di-pack saja), dan butir daftar tentang fixture pilot di bagian "Yang sengaja TIDAK didaftarkan" dihapus. Alasannya mekanis: validator menuntut setiap folder `sistem-*/` di disk terdaftar dan setiap baris terdaftar punya foldernya; baris sistem lain akan menunjuk folder yang tidak ada |
| 2 | `README.md` root **baru** | master tidak punya berkas ini; repo baru butuh halaman muka yang menjelaskan isi repo dan cara mulai |
| 3 | `PAKET_REPO.md` + profil `PAKET_REPO.json` **baru** | berita acara paket + profil repo |

`LOG_SESI.md` kosong dibangkitkan sebagai berkas kosong (0 byte) — bukan suntingan atas isi apa pun, melainkan wadah kosong supaya repo baru memulai lognya sendiri. Formatnya ada di `_meta/TEMPLATE_LOG_SESI.md` bila berkas itu ikut dalam subset.

Berkas root `PANDUAN_PENGGUNA.md` dan `PROMPT_ENTRI_UNIVERSAL.md` disalin **byte-per-byte**. Penyesuaian konteks repo mandiri dilakukan lewat suntingan #2 dan #3, bukan dengan mengedit keduanya — supaya klaim "tidak ada file lain yang isinya berubah" tetap bisa dibuktikan dengan `diff -r`.

**Isi wajib `PAKET_REPO.md`:** sha commit sumber; tanggal; versi sistem; daftar yang dikecualikan **beserta alasannya per butir**; daftar tiga suntingan yang benar-benar dilakukan; sha256 tiap file; dan empat perintah verifikasi yang bisa dijalankan pemilik di repo baru (validator repo, validator sistem, inisialisasi git + remote, push).

---

## 9. Aturan main untuk sistem BARU

Mengikat, tanpa pengecualian diam-diam:

> **Sebuah sistem baru tidak boleh mengklaim "Siap dipakai produksi" sebelum ia bisa di-pack.**

Konkretnya, pada saat klaim itu diajukan harus benar tiga hal:

1. `tools/pack_repo.py <nama-sistem> --check` **hijau** (nol pemblokir);
2. sistem itu punya validator sendiri bernama `validate_system.py` di folder sistem internalnya, **self-contained** (menghitung root-nya sendiri, tidak tahu-menahu soal `_meta/` maupun `tools/`, tidak mengimpor kode luar);
3. validator itu **PASS di dalam hasil pack**, bukan hanya di master.

Butir ini terdaftar sebagai kewajiban di `_meta/DEFINITION_OF_DONE.md` (bagian "Siap dipakai produksi") dan sebagai skenario uji yang bisa diulang di `_meta/ACCEPTANCE_TESTS.md`. Konsekuensinya sengaja keras: sistem yang tidak bisa dikeluarkan dari repo master **belum** self-contained, dan karena itu belum memenuhi kontrak warisan — betapapun rapi isinya.

Kenapa validator sistem harus self-contained: kalau ia mengimpor kode dari `tools/` atau membaca `_meta/`, maka repo mandiri yang tidak membawa berkas itu akan menjalankan validator yang mati. Validator sistem adalah satu-satunya alat yang menilai isi domain; ia harus hidup di mana pun foldernya dibawa.

---

## 10. Cara pakai

```
python3 tools/pack_repo.py <sistem-x> [--out DIR] [--zip] [--check] [--versi V]
```

| Flag | Arti |
|---|---|
| *(tanpa flag)* | tulis paket ke folder keluaran default, lalu jalankan validator di dalamnya |
| `--check` | **jangan tulis apa pun**; cetak rencana + daftar pemblokir; exit non-nol bila ada pemblokir |
| `--out DIR` | folder tujuan (isinya ditimpa bersih) |
| `--zip` | tambahan: buat arsip zip dari hasil paket |
| `--versi V` | paksa nomor versi. Tanpa flag ini versi **diambil dari manifest sistem** (baris Versi); angka tidak pernah dikarang |

**Membaca keluaran `--check`.** Empat blok, selalu dalam urutan yang sama:

1. **DAFTAR FILE** — semua berkas yang akan ikut, terurut, dengan penanda sumbernya (salinan / dibangkitkan).
2. **SUBSET `_meta`** — berkas `_meta/` yang ikut, masing-masing dengan kedalaman closure tempat ia masuk (`d0` = dirujuk langsung dokumen sistem).
3. **`absent_refs_allowed`** — rujukan yang memang tidak ada di paket, dengan kategori + alasan.
4. **PEMBLOKIR** — kosong berarti siap; tidak kosong berarti perbaiki dulu di master, bukan di hasil pack.

**Membaca keluaran run sungguhan.** Setelah menulis, alat mencetak keluaran mentah validator repo dan validator sistem apa adanya. Kalau perintah selesai dengan exit code 0 dan folder ada, paket itu sudah memenuhi keempat syarat bagian 1. Kalau exit code non-nol, folder sudah dihapus — jangan mencarinya.

**Setelah paket jadi**, pemilik menjalankan empat perintah verifikasi yang tercetak di `PAKET_REPO.md`. Hasil pack **tidak** di-commit ke master: master adalah satu-satunya sumber kebenaran, dan paket selalu bisa dibangkitkan ulang dari sha yang tercatat. Yang di-commit ke master hanyalah alat, protokol, dan bukti keberhasilannya.

---

## 11. Yang sengaja TIDAK ikut

Daftar ini normatif. Setiap butir punya alasan; kalau alasannya tidak lagi berlaku, ubah protokolnya dulu — jangan sunting pengecualiannya diam-diam di dalam kode.

| Tidak ikut | Alasan |
|---|---|
| Sistem domain lain | satu paket = satu sistem; itu seluruh gunanya |
| Fixture pilot meta-sistem | fixture uji meta-sistem, bukan sistem domain; ia tidak pernah terdaftar sebagai sistem |
| `_meta/_internal/` selain yang dirujuk langsung sistem | audit & handoff historis = referensi master, bukan instruksi aktif repo baru |
| Folder backup dan artefak template bersih | artefak build; di master pun tidak di-commit |
| Alat meta selain dua yang dibawa | alat itu memelihara master (template bersih, backup, injeksi kegagalan meta). Di repo mandiri mereka akan menunjuk struktur yang tidak ada. Mereka **tetap tinggal di master** — tidak ikut ≠ dihapus |
| Berkas `LOG_SESI_*.md` master | log sesi repo master; repo baru memulai lognya sendiri |
| Dokumen sejarah sesi-rekaman & dokumen uji clean-run milik master | catatan peristiwa master, bukan aturan sistem |
| Folder distribusi hasil pack sebelumnya | keluaran, bukan sumber |
| Arsip cadangan ringkasan di master | milik master; repo baru tidak memerlukannya untuk berfungsi |
| Zip historis `SISTEM KERJA KONTEN FEAT LMARENA & GITHUB (revisi agent 1).zip` di root master | artefak masukan awal yang **tetap di master** dan tidak ikut paket mana pun — jangan dihapus (provenance), dan tidak pernah disalin ke hasil pack |

---

## 12. Hubungan dengan protokol lain

- **Review independen.** Perubahan pada protokol ini atau pada alat pelaksananya berdampak permanen dan menyentuh struktur `_meta/` → trigger **L1** menurut `_meta/PROTOKOL_REVIEW_INDEPENDEN.md`. Yang mengerjakan tidak memutus.
- **Definition of Done.** Butir "siap di-pack" hidup di `_meta/DEFINITION_OF_DONE.md`; dokumen ini yang menjelaskan artinya.
- **Acceptance test.** Prosedur uji yang bisa diulang di sesi baru tanpa pengetahuan tersirat ada di `_meta/ACCEPTANCE_TESTS.md`.
- **Index.** Status paket per sistem dicatat di `_meta/INDEKS_SISTEM.md` — tanggal + versi saat paket terakhir LULUS.

---

## Log keputusan

| Tanggal | Perubahan | Alasan | Approval |
|---|---|---|---|
| 2026-09-07 | Dokumen dibuat (v1) | Putusan pemilik: satu perintah → satu folder repo mandiri siap upload, tanpa memisah file manual dan tanpa menulis ulang isi dokumen | Putusan pemilik 7 Sep 2026 (dinyatakan FINAL, tidak dibahas ulang). Menunggu review independen L1 |
| 2026-09-08 | v1.1: satu definisi "dokumen aktif" (bagian 3b) dipakai validator DAN packager; benih subset `_meta/` = dokumen aktif saja (bukan semua `.md`); rujukan dokumen non-aktif dicatat terpisah (bagian 5); syarat iii dipertegas "pada dokumen aktif" | Akar masalah bukti basi: benih memindai `ACCEPTANCE_TEST_LOG.md`/`DISKUSI_MENTAH*` sehingga menulis bukti mengubah isi paket. Satu definisi menghapus drift dua daftar glob | Putusan pemilik 8 Sep 2026 (perbaikan B1/B2). Menunggu review independen L1 — tidak ada gate lain yang diklaim tertutup |


## Memindahkan paket ke luar sandbox

Paket yang tervalidasi di sandbox belum berarti sudah tersedia bagi pemilik di luar sandbox; pemindahan adalah langkah tersendiri, bukan penutupan gate sistem.

1. **Pin sumber.** Ambil SHA main terbaru yang telah memuat perubahan prasyarat, jalankan validator repo + failure injection, lalu bandingkan angka kedua paket dengan entri bukti terakhir. Catat perbedaan apa adanya; jangan menambal paket atau mengganti angka historis agar terlihat cocok. Bila sesi terkunci pada branch kerja, gunakan snapshot bersih SHA main untuk sumber paket tanpa berpindah branch. Jangan menyebutnya run pada HEAD PR yang kemudian berubah.
2. **Bangkitkan dan buktikan.** Jalankan `python3 tools/pack_repo.py <sistem> --zip` pada sumber tersebut, catat berkas/subset/daftar putih, keluaran kedua validator DI DALAM paket, nama ZIP, serta SHA sumber; validasi merah berarti berhenti, bukan mengedit hasil pack. Ekstrak ZIP apa adanya ke direktori sementara di luar master, jalankan validator repo dari root paket dan validator sistem dari subfolder sistem.
3. **Periksa kebersihan sebelum pemindahan.** ZIP harus keluaran `--zip` packager, **jangan pernah meng-zip ulang folder yang sudah di-git-init**: direktori `.git`, terutama `.git/config`, dapat ikut membawa konfigurasi remote atau kredensial. Periksa setiap nama anggota arsip dan tolak komponen path yang persis `.git`, baik berkas maupun direktori; jangan menghapus `.gitignore` atau `.gitattributes` yang memang wajib ikut. Fakta run 8 Sep 2026: perintah `unzip -l <file.zip> | grep -c '\.git'` menghasilkan **2**, bukan 0, karena kedua berkas wajib itu; ZIP dibuang lalu dibangkitkan ulang sekali dan hasilnya tetap 2, sedangkan pemeriksaan komponen path `.git` menghasilkan **0** untuk kedua ZIP. Hasil literal itu harus dilaporkan, tidak boleh ditulis sebagai 0; materialitas perbedaan metode bukti adalah hak reviewer.
4. **Cara keluar pertama — push langsung bila izin ada.** Coba `gh repo create With-Ai-Agent/<sistem> --private` (jangan gunakan nama alternatif, jangan membuat repo publik). Target yang sudah ada **dan kosong (0 commit, isi kosong)** sah untuk dilanjutkan; verifikasi keduanya lewat API sebelum push. Target yang sudah berisi berarti **berhenti untuk sistem itu**, jangan menimpa atau force-push; 404 bukan bukti bahwa repo kosong (bisa berarti tidak terlihat oleh token). Di folder hasil pack yang belum memiliki Git, pelaksana yang diizinkan menginisialisasi `main`, menambahkan seluruh isi, membuat satu commit berpesan "Paket repo mandiri <sistem> v<versi> dari master <sha>", menambahkan origin repo target, lalu push main. Jangan menyalin riwayat master, jangan menambahkan remote ke master, dan jangan melanggar batas branch sesi untuk menjalankan langkah ini.
5. **Batas izin nyata — bukan bug mekanisme.** Pada sesi agent 8 Sep 2026, token GitHub App dapat membaca/menulis repo master privat, tetapi **TIDAK bisa createRepository di organisasi**: kedua perintah create privat ditolak persis `GraphQL: Resource not accessible by integration (createRepository)`. Ini batas izin token, bukan alasan mengubah packager atau meminta pemilik menyerahkan kredensial. Tidak ada repo mandiri yang berhasil dibuat oleh sesi tersebut.
6. **Cara keluar kedua — aset release + pemilik membuat repo privat sendiri.** Hanya bila createRepository ditolak dengan penolakan integration tersebut atau 403 setara, gunakan release di master **yang telah diverifikasi privat**, satu per sistem: nama tag `paket-<sistem>-<versi>-<sha-pendek>`, target SHA sumber lengkap, judul "Paket repo mandiri <sistem> v<versi>"; catatan memuat SHA lengkap, perintah bangkit ulang pada SHA itu, jumlah berkas/subset/absent, dan hasil kedua validator. Unggah ZIP packager apa adanya dengan `gh release create`, bukan lewat commit master; tag paket tidak boleh bertabrakan dengan tag rilis versi sistem. Setelah berhasil, verifikasi aset berstatus uploaded, unduh ulang dan cocokkan SHA256, catat URL release/aset. Pemilik mengunduh, mengekstrak, membuat repo privat (atau memakai target privat yang benar-benar kosong), lalu mengikuti petunjuk Git dalam berita acara paket. Master tetap sumber kebenaran; tidak ada isi master yang dihapus karena salinannya sudah keluar.
7. **Jangan menyamakan draft dengan pengiriman.** Fakta sesi 8 Sep 2026: pembuatan metadata draft release berhasil, tetapi unggah kedua ZIP ke uploads.github.com gagal `EOF`, termasuk percobaan ulang; tersisa dua draft dengan **0 aset**. Ini hambatan unggah yang terpisah dari penolakan createRepository; penyebab EOF belum terbukti. Jangan menyebut "tersedia sebagai aset release" sebelum aset benar-benar ada dan terverifikasi; catat status tertunda beserta URL draft dan perintah unggah ulang, lalu serahkan bukti kepada reviewer. Publikasi bukan klaim produksi: brand core kosong, pilot yang belum dijalankan, dan acceptance lain yang terbuka tetap apa adanya.
