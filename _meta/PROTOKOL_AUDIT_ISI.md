# Protokol Audit Isi — memeriksa ISI repo/sistem, bukan PR

> **Sumber tunggal mekanisme audit isi.** Untuk review **PR** (memutuskan merge), lihat
> `PROTOKOL_REVIEW_INDEPENDEN.md` + `tools/review_prompt.py` — **dua mekanisme berbeda untuk dua
> pekerjaan berbeda**, dan mencampuradukkannya adalah kesalahan nyata yang pernah terjadi di repo ini.
>
> Dibuat 17 Sep 2026 atas tuntutan eksplisit pemilik: *"yang aku maksud saat ini adalah mekanisme
> review isi repo, isi sistem, dan semua hal yang perlu diperiksa. **Bukan soal PR dan bukan soal merge.**"*

---

## Apa ini

Mekanisme untuk **memeriksa isi** repo, sebuah sistem, sebuah folder, atau sebuah dokumen — lalu
**melaporkan temuan**, tanpa memperbaiki apa pun dan tanpa memutuskan merge apa pun.

**Bedanya dengan review PR:**

| | Review PR | **Audit isi (protokol ini)** |
|---|---|---|
| Objek | satu PR (base sha ↔ head sha) | **satu jalur** di pohon kerja, di-pin ke satu sha |
| Keluaran | verdict + keputusan merge | **laporan temuan** — tidak ada merge |
| Kanal | komentar PR | **GitHub Issue** berpola tetap |
| Alat pembangkit | `tools/review_prompt.py --pr N` | **`tools/audit_prompt.py --objek <path>`** |
| Alat pengambil | `tools/ambil_verdict.py --pr N` | **`tools/ambil_verdict.py --terbaru`** |
| Siapa yang memperbaiki | penulis PR, setelah verdict | **tidak ditentukan di sini** — butuh mandat terpisah |

**Induk juga objek yang sah.** `--objek _meta` dan `--objek tools` sama sahnya dengan
`--objek sistem/<nama>`. Instruksi pemilik 17 Sep 2026: mekanisme ini **harus tertanam di
meta-sistem juga**, bukan hanya di sistem yang dibangunnya.

## Kapan dipakai

Pakai audit isi kalau pertanyaannya *"sehatkah isi ini?"*, **bukan** *"bolehkah ini di-merge?"*:

- setelah membangun sistem baru dan sebelum menyatakannya siap dipakai;
- berkala, berbasis risiko (kedalaman mengikuti `QUALITY_ASSURANCE_AND_EVOLUTION.md`);
- saat pemilik meminta *"periksa semuanya"* tanpa menunjuk PR;
- setelah perubahan struktural `_meta/` atau menaikkan versi aturan;
- saat mencurigai satu **kelas** cacat yang mungkin tersebar (mis. manual yang tidak bisa dipakai awam);
- untuk **memeriksa mekanisme audit itu sendiri** — lihat bagian "Pengecualian pengadil" di bawah,
  karena ini kasus khusus yang tidak boleh diputuskan sendiri.

**Jangan** pakai audit isi untuk: memutuskan merge (itu review PR), atau sebagai alasan memperbaiki
sesuatu tanpa mandat (menemukan ≠ memperbaiki, QA Prinsip 2).

## Cara — langkah bernomor

### Bagi pemilik (yang meminta audit)

1. Buka **sesi agent baru** — jangan sesi yang sedang mengerjakan objek itu. Auditor yang mengaudit
   pekerjaannya sendiri tidak bisa independen.
2. Minta sesi itu membangkitkan prompt auditnya:
   ```bash
   python3 tools/audit_prompt.py --objek _meta --kedalaman mendalam
   ```
   Ganti `--objek` dengan yang mau diperiksa. **Jangan menulis prompt audit sendiri** — lihat "Kalau gagal".
3. **Tempel seluruh keluaran perintah itu** ke sesi auditor sebagai pesan pertama.
4. Tunggu. Auditor akan menyerahkan hasilnya ke sebuah GitHub Issue.
5. Kembali ke sesi yang sedang berjalan dan **cukup bilang**: *"audit sudah selesai."*
   Sesi itu akan mengambil hasilnya sendiri:
   ```bash
   python3 tools/ambil_verdict.py --terbaru
   ```
   **Kamu tidak perlu menyalin, meringkas, atau melaporkan apa pun.**

### Bagi sesi yang diminta mengaudit

1. Baca prompt yang ditempel — **jangan menambah, memotong, atau menyuntingnya**.
2. Ikuti 13 bagiannya berurutan. Bagian yang paling sering dilanggar: **bagian 6 ATURAN CAKUPAN** dan
   **bagian 8 verifikasi adversarial**.
3. Serahkan hasil ke GitHub Issue sesuai bagian 10 prompt (judul + label berpola tetap).

### Bagi sesi yang diaudit (setelah pemilik bilang "audit sudah selesai")

1. Jalankan `python3 tools/ambil_verdict.py --terbaru`.
2. Baca **seluruh** bagiannya, termasuk **"di luar cakupan"** dan **"kandidat yang dicabut"**.
   Keduanya bagian dari laporan, bukan sampah.
3. **Membaca verdict ≠ menyetujuinya.** Bertindak atas temuan butuh mandat pemilik.
4. Laporkan ke pemilik: apa temuannya, mana yang kamu sarankan ditindak, mana yang tidak beserta alasannya.

## Prompt siap tempel

**Prompt audit tidak pernah ditulis tangan.** Ia dibangkitkan:

```bash
# lihat bentuknya dulu tanpa objek sungguhan
python3 tools/audit_prompt.py --generic

# audit induk (meta-sistem itu sendiri)
python3 tools/audit_prompt.py --objek _meta --kedalaman mendalam

# audit satu sistem
python3 tools/audit_prompt.py --objek sistem/sistem-klinik

# audit alat-alatnya
python3 tools/audit_prompt.py --objek tools --kedalaman mendalam

# audit satu berkas
python3 tools/audit_prompt.py --objek _meta/PANDUAN_PENGGUNA_TEMPLATE.md --kedalaman ringan

# simpan ke berkas kalau mau ditempel dari tempat lain
python3 tools/audit_prompt.py --objek _meta --out /tmp/prompt-audit.md
```

| Perintah | Fungsi | Kapan dipakai | Keluaran diharapkan | Kalau gagal |
|---|---|---|---|---|
| `python3 tools/audit_prompt.py --objek <path>` | membangkitkan prompt audit yang **ter-pin** ke sha HEAD | sebelum membuka sesi auditor | prompt 13 bagian ke stdout, inventaris berkas diambil dari pohon kerja | exit 2 + pesan: objek tidak ada / sha tidak sah / objek keluar repo. **Perbaiki argumennya, jangan menulis prompt tangan** |
| `--kedalaman ringan\|sedang\|mendalam` | mengatur kedalaman berbasis risiko | selalu dipikirkan, default `sedang` | bagian 3 prompt berubah sesuai pilihan | pilihan tidak dikenal → `argparse` menolak dengan daftar pilihan sah |
| `--generic` | melihat bentuk prompt tanpa objek nyata | untuk memeriksa alatnya, atau menunjukkan ke pemilik | prompt dengan `<OBJEK>` dan `<SHA PIN>` | — |
| `python3 tools/ambil_verdict.py --terbaru` | mengambil hasil audit terbaru **tanpa diberi tahu nomornya** | setelah pemilik bilang "audit sudah selesai" | badan Issue + semua komentar + verdict terbaca otomatis | exit 2: tidak ditemukan / ambigu. **Tidak pernah menyimpulkan "bersih" dari ketiadaan hasil** |
| `python3 tools/ambil_verdict.py --daftar` | melihat semua kandidat hasil audit | untuk memilih yang mana | daftar Issue terbaru di atas, dengan objek + sha + cara dikenali | keluaran kosong = memang belum ada audit diserahkan |
| `python3 tools/ambil_verdict.py --pr N` | kanal lama: hasil review PR | untuk review PR, bukan audit isi | review + komentar PR | exit 2 kalau PR tidak ada |

## Apa yang terjadi sesudahnya

1. **Auditor** membuat Issue berjudul `AUDIT <objek> @<sha7>` berlabel `audit-independen`, isinya 6
   bagian wajib: VERDICT satu baris → ringkasan angka → tabel temuan terklasifikasi → **temuan di luar
   cakupan** → **kandidat yang dicabut** → **batasan audit**.
2. **Putaran lanjutan ditambahkan sebagai komentar**, tidak pernah menyunting temuan putaran pertama
   (append-only, jangan menghaluskan).
3. **Sesi yang diaudit** mengambil sendiri dengan `ambil_verdict.py --terbaru`.
4. **Pemilik** memutuskan apa yang ditindak. Tidak ada yang berubah di repo sebelum itu.

## Kalau gagal

| Gejala | Sebab | Langkah pertama |
|---|---|---|
| `ERROR: tidak ada --objek dan tidak ada --generic` | alat **sengaja menolak menebak objek** | sebut objeknya. Menebak objek = mengaudit sesuatu yang tidak diminta siapa pun |
| `ERROR: objek X TIDAK ADA di root repo` | salah eja, atau objeknya memang belum ada | periksa ejaan; daftar sistem ada di `INDEKS_SISTEM.md` |
| `ERROR: sha pin tidak sah` | `--pin` diisi bukan 7–40 heksadesimal | hilangkan `--pin` (default HEAD), atau isi sha yang benar |
| `ERROR: gh tidak tersedia / tidak terautentikasi` | kanal GitHub tidak bisa dibaca | periksa autentikasi GitHub; sementara, buka Issue-nya di browser dan salin manual |
| `tidak ditemukan hasil audit di kanal Issue` | audit belum diserahkan, **atau** auditor menaruhnya di tempat lain, **atau** label belum dibuat | **jangan simpulkan "bersih"**. Tanya auditor/cek `gh issue list --state all`. Sekali saja buat labelnya: `gh label create audit-independen --description "hasil audit isi independen"` |
| `ambigu: beberapa hasil audit dengan waktu identik` | alat **sengaja menolak menebak** yang mana | `--daftar` lalu `--issue <N>` |
| Auditor mengembalikan prompt yang sudah disunting | pelanggaran bagian "Sumber prompt" | **tolak**, bangkitkan ulang, dan catat sebagai temuan. Prompt yang disunting pihak yang diaudit bukan audit |

**Kenapa prompt tidak boleh ditulis tangan:** kalau pihak yang diaudit boleh menulis instruksi untuk
pengadilnya sendiri, maka hasil audit mengukur **kepandaian menulis prompt**, bukan **kesehatan isi**.
Ini alasan yang sama kenapa `review_prompt.py` ada untuk PR.

---

## Aturan yang mengikat audit isi

Semuanya **diwarisi**, tidak dikarang ulang di sini — satu sumber:

1. **ATURAN CAKUPAN** (`QUALITY_ASSURANCE_AND_EVOLUTION.md`): *cakupan membatasi RENCANA PENCARIAN dan
   KLAIM, TIDAK PERNAH membatasi LAPORAN.* Temuan di luar cakupan **wajib dilaporkan** dengan label +
   klasifikasi + bukti; dilarang membuangnya, menghaluskannya, atau bertindak atasnya tanpa mandat.
2. **Tujuh lensa audit** (`QUALITY_ASSURANCE_AND_EVOLUTION.md` bagian "Lensa audit"). Semua wajib
   dijalankan; lensa yang bersih **wajib dinyatakan bersih**, karena pembaca tidak bisa membedakan
   "sudah diperiksa, bersih" dari "tidak diperiksa".
3. **Klasifikasi temuan wajib**: `B`/`A`/`G`/`N`/`P` + prioritas `P1`–`P3` + dasar bukti. Temuan tanpa
   bukti terverifikasi = **"dugaan"**, tidak boleh langsung jadi perbaikan.
4. **Kedalaman berbasis risiko**: Ringan / Sedang / Mendalam. Jangan menaikkan tanpa alasan (derau),
   jangan menurunkan diam-diam (kalau tidak sanggup, **katakan di laporan**).
5. **Verifikasi adversarial**: bantah setiap kandidat temuan sendiri dulu, baca di sumbernya, jelaskan
   MENGAPA bukan hanya BAHWA, bedakan build-time dan run-time, dan **laporkan rasio sinyalmu sendiri**.
   Bukti dari repo ini: audit 17 Sep 2026 **mencabut 28 dari 43 kandidat (~65%)** sebagai positif palsu.
6. **Batas anti-recursion + kondisi berhenti** (`QUALITY_ASSURANCE_AND_EVOLUTION.md`): audit isi =
   **satu putaran** melapor lalu berhenti; keseluruhan proses maksimal **2 putaran**, lalu **eskalasi ke
   pemilik**. **Batas 2 putaran membatasi LOOP, bukan cakupan laporan.**
7. **Append-only**: jangan menghapus riwayat, jangan menghaluskan (`PROTOKOL_REVIEW_INDEPENDEN.md` #8).
8. **Batas publikasi 6d**: selama jendela uji terbuka, artefak yang dipublikasikan tidak boleh memuat
   rumusan jawaban/kriteria yang belum tertutup uji — pakai pointer SHA+baris.
9. **Read-only**: auditor tidak commit, tidak push, tidak menyunting berkas repo. Salinan kerja hanya di `/tmp`.

## Pengecualian pengadil

**Mengaudit mekanisme audit memakai mekanisme audit adalah rekursi yang sah untuk dilaporkan, tetapi
tidak untuk diputuskan sendiri.**

Kalau objek audit mencakup salah satu dari ini:

- `tools/audit_prompt.py` · `tools/ambil_verdict.py` · `tools/review_prompt.py` ·
  `tools/test_failure_injection.py` · `PROTOKOL_REVIEW_INDEPENDEN.md` · `PROTOKOL_AUDIT_ISI.md`

maka auditor **wajib**: melaporkan temuan seperti biasa, **tetapi tidak menyatakan mekanisme pengadil itu
sendiri sahih atau tidak sahih**. Keputusan itu milik pemilik, dan sebaiknya diperiksa pengadil dari
**keluarga model yang berbeda** (bukti: self-preference bias terdokumentasi — model menilai keluaran
keluarganya sendiri lebih tinggi).

Daftar ini **sengaja diduplikasi** di `tools/review_prompt.py` (`ARBITER_PATH_REASONS`) dan
`tools/audit_prompt.py` (`ARBITER_PATHS`) karena keduanya menegakkannya di kanal berbeda.
**Kalau salah satunya bertambah, yang lain WAJIB ikut** — dua sumber yang saling menunjuk, dan
ketidaksinkronannya adalah temuan audit.

## Yang belum terbukti (jangan diklaim siap)

- **`gh issue create` belum diuji** di lingkungan ini — yang terbukti baru kemampuan **baca**
  (`gh api rate_limit`, `gh issue list`, `gh pr view`). Menguji pengiriman berarti **membuat artefak
  nyata di repo**, jadi butuh izin pemilik. **Sampai itu diuji, bagian "Cara menyerahkan hasil" adalah
  rancangan yang masuk akal, bukan mekanisme terverifikasi.**
- **Label `audit-independen` belum dibuat** di repo ini.
- Presisi alat pemindai pendukung (`tools/check_manuals.py`) **tidak diketahui** di luar korpus
  penyetelannya — peringatannya tertulis di docstring alat itu sendiri.

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Protokol dibuat; `tools/audit_prompt.py` + `tools/ambil_verdict.py` dibangun | Tuntutan pemilik T29+T30. Sebelum ini repo hanya punya mekanisme review **PR**: `PROTOKOL_REVIEW_INDEPENDEN.md` mensyaratkan "nomor PR + SHA basis + SHA head" di anatomi butir 2, dan `review_prompt.py` hanya punya `--pr`/`--generic` (diperiksa di sumbernya, baris 616–618). **Klaim agent sebelumnya bahwa mekanisme review isi "sudah ada" dikoreksi sebagai over-claim** — yang sudah ada adalah mesin auditnya (QA 3 lapis, 7 lensa, klasifikasi, 8 arsip audit nyata, Sistem Klinik), tetapi **tidak ada prompt audit yang dibangkitkan alat**, sehingga prompt audit harus dikarang tangan: pihak yang diaudit menulis instruksi untuk pengadilnya sendiri. Ditemukan sebagai X-04/X-05 pada audit 17 Sep. Dokumen ini ditulis mengikuti **Standar Kelulusan Manual 5 syarat** yang ditambahkan di hari yang sama (6 bidang: apa/kapan/cara/prompt/sesudahnya/kalau gagal + tabel perintah 5 kolom) supaya tidak mengkhianati standarnya sendiri |
| 2026-09-17 | **Induk dinyatakan sebagai objek audit yang sah** (`--objek _meta`, `--objek tools`) | Instruksi eksplisit pemilik 17 Sep 2026: *"mekanisme itu juga harus tertanam di meta sistem … bukan pada sistem-sistem yang dibangun nya saja, tapi juga pada induk sistem itu sendiri."* Audit atas induk menemukan pengecualian struktural nyata: induk tidak tunduk pada kontrak warisannya sendiri dan 3 butir (W-03, W-07, W-09) tidak diterapkan tanpa terdeteksi alat mana pun |
| 2026-09-17 | Bagian "Yang belum terbukti" ditambahkan, termasuk bahwa **pengiriman via Issue belum diuji** | Menolak mengklaim mekanisme siap hanya karena rancangannya masuk akal. `gh issue create` membuat artefak nyata di repo sehingga butuh izin pemilik; yang terbukti baru kemampuan baca |
