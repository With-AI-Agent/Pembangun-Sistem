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

1. **Auditor** menyerahkan laporan berjudul `AUDIT <objek> @<sha7>` lewat **salah satu dari dua kanal**
   (lihat bagian "Dua kanal penyerahan" di bawah), isinya 6 bagian wajib: VERDICT satu baris → ringkasan
   angka → tabel temuan terklasifikasi → **temuan di luar cakupan** → **kandidat yang dicabut** →
   **batasan audit**.
2. **Putaran lanjutan DITAMBAHKAN, tidak pernah menyunting temuan putaran pertama** (append-only, jangan
   menghaluskan). Di kanal Issue = komentar baru. Di kanal berkas = **berkas baru** dengan sha baru, atau
   bagian `## Putaran 2` yang ditambahkan di bawah — **jangan** menimpa isi putaran 1.
3. **Sesi yang diaudit** mengambil sendiri dengan `ambil_verdict.py --terbaru`, yang mencari di **kedua
   kanal sekaligus** dan mengambil yang terbaru tanpa menebak.
4. **Pemilik** memutuskan apa yang ditindak. Tidak ada yang berubah di repo sebelum itu.

## Dua kanal penyerahan (yang satu TERBUKTI DIBLOKIR di lingkungan ini)

**Diubah 17 Sep 2026 sesudah uji nyata atas izin pemilik** (*"Ya, uji penuh sekarang"*). Sebelumnya
protokol ini hanya punya satu kanal — GitHub Issue — dan kanal itu dinyatakan "belum diuji". **Sudah
diuji, dan hasilnya membatalkan rancangan awalnya:**

| Operasi | Hasil uji 17 Sep 2026 | Artinya |
|---|---|---|
| `gh issue create` | **HTTP 403** `Resource not accessible by integration (createIssue)` | **kanal Issue TIDAK BISA dipakai** di lingkungan produksi ini |
| `gh api repos/.../permissions` | `{"admin":false,"maintain":false,"pull":false,"push":false,"triage":false}` | token bot **tidak punya izin repo tingkat API** sama sekali |
| `gh label create audit-independen` | **BERHASIL** (label `#5319e7` kini ada di repo) | izin `labels:write` ADA walaupun `issues:write` tidak |
| `gh issue list` / `gh pr list` / `gh api repos/...` | **BERHASIL** (baca) | kanal baca jalan; repo ini punya 73 PR dan **0 Issue** |
| `git push` / `git ls-remote` | **BERHASIL** | **kanal git berfungsi dua arah** |

**Kesimpulan yang diambil:** mekanisme ini **tidak boleh bergantung pada kanal yang diblokir**. Maka
kanal penyerahan **utama** sekarang adalah **berkas yang di-commit**, dan Issue jadi **alternatif** yang
langsung hidup kalau izin `issues:write` kelak diberikan.

### Kanal A — berkas ter-commit (UTAMA, terbukti berfungsi)

Auditor menulis laporannya ke:

```
_meta/_internal/audit/AUDIT_<objek-dengan-garis-bawah>_<sha7>.md
```

Baris **pertama** berkas wajib berpola persis `# AUDIT <objek> @<sha7>` — **baris itulah yang dibaca
alat**, bukan nama berkasnya (satu sumber kebenaran, dan polanya identik dengan judul kanal Issue).
Auditor lalu **commit + push**. Sesi yang diaudit mengambilnya dengan perintah yang sama seperti biasa:

```bash
python3 tools/ambil_verdict.py --terbaru
```

**Kenapa di `_meta/_internal/`:** folder itu **tidak ikut ke ekstrak template** (diperiksa lewat
`build_template.py`), jadi artefak audit per-run **tidak bocor** ke sistem anak dan tidak menggeser pin
peringatan template.

### Kanal B — GitHub Issue (alternatif, terblokir saat ini)

```bash
gh issue create --title "AUDIT <objek> @<sha7>" --label "audit-independen" --body-file /tmp/hasil-audit.md
```

Kalau perintah ini mengembalikan **403**, itu **bukan kesalahan auditor** dan **bukan alasan untuk
menyimpulkan audit gagal** — pindah ke Kanal A dan **catat 403-nya di dalam laporan**, supaya sesi
berikutnya tidak menghabiskan waktu menemukan hal yang sama.

`ambil_verdict.py` **mencari di kedua kanal** dan menggabungkan kandidatnya. Kanal Issue yang tidak
tersedia dilaporkan sebagai **catatan**, bukan sebagai kegagalan fatal — karena ketidaktersediaan kanal
**tidak pernah** boleh dibaca sebagai "tidak ada temuan".

## Kalau gagal

| Gejala | Sebab | Langkah pertama |
|---|---|---|
| `ERROR: tidak ada --objek dan tidak ada --generic` | alat **sengaja menolak menebak objek** | sebut objeknya. Menebak objek = mengaudit sesuatu yang tidak diminta siapa pun |
| `ERROR: objek X TIDAK ADA di root repo` | salah eja, atau objeknya memang belum ada | periksa ejaan; daftar sistem ada di `INDEKS_SISTEM.md` |
| `ERROR: sha pin tidak sah` | `--pin` diisi bukan 7–40 heksadesimal | hilangkan `--pin` (default HEAD), atau isi sha yang benar |
| `ERROR: gh tidak tersedia / tidak terautentikasi` | kanal GitHub tidak bisa dibaca | periksa autentikasi GitHub; sementara, buka Issue-nya di browser dan salin manual |
| `tidak ditemukan hasil audit di KEDUA kanal` | audit belum diserahkan, **atau** auditor menaruhnya di tempat lain | **jangan simpulkan "bersih"**. Cek keduanya: `gh issue list --state all --limit 30` **dan** `ls _meta/_internal/audit/` |
| `gh issue create` → **HTTP 403** `Resource not accessible by integration` | token tidak punya `issues:write` — **terverifikasi di lingkungan ini 17 Sep 2026** | **bukan kesalahan auditor.** Pindah ke **Kanal A** (berkas ter-commit) dan catat 403-nya di dalam laporan. Labelnya tetap boleh dibuat: `gh label create audit-independen --description "..."` — itu **berhasil** walaupun Issue tidak |
| `ambil_verdict.py` mencetak `[catatan kanal] kanal Issue tidak tersedia` | gh tidak terpasang / tidak ada izin / jaringan diblokir | **bukan kegagalan.** Kanal berkas tetap menjawab. Yang dilarang: menyimpulkan "bersih" karena satu kanal mati |
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

## Yang sudah diuji, dan yang masih belum terbukti

**SUDAH DIUJI 17 Sep 2026** atas izin pemilik (*"Ya, uji penuh sekarang"*) — hasilnya di tabel bagian
"Dua kanal penyerahan". Yang **terbukti berfungsi ujung-ke-ujung**: `audit_prompt.py` membangkitkan
prompt ter-pin → laporan ditulis → diserahkan lewat **kanal berkas** → `ambil_verdict.py --terbaru`
menemukannya sendiri, mencetak isinya, dan membaca verdictnya otomatis. **Rantai T30 pemilik terpenuhi
lewat kanal git, bukan kanal Issue.**

**MASIH BELUM TERBUKTI — jangan diklaim siap:**

- **Kanal Issue belum pernah berhasil dipakai** untuk menyerahkan hasil. Labelnya ada, tapi isinya
  **nol** karena `gh issue create` ditolak 403. Kalau izin kelak diberikan, **kanal ini harus diuji
  ulang** — keberhasilannya membuat label **tidak** membuktikan keberhasilan membuat Issue.
- **Independensi auditor belum pernah terpenuhi dalam uji ini.** Uji kanal 17 Sep 2026 dijalankan oleh
  **sesi yang sama** yang membangun mekanisme dan yang objeknya diaudit, jadi verdict-nya
  **PROVISIONAL** dan dinyatakan begitu di dalam laporannya sendiri. Yang terbukti adalah **rantai
  penyerahan**, bukan kualitas penilaian.
- **Kanal berkas belum diuji lintas-sesi.** Baru terbukti terbaca oleh sesi yang menulisnya. Yang belum
  diuji: sesi **lain** di checkout **lain** mengambilnya sesudah `git pull`.
- Presisi alat pemindai pendukung (`tools/check_manuals.py`) **tidak diketahui** di luar korpus
  penyetelannya — peringatannya tertulis di docstring alat itu sendiri.
- **Append-only di kanal berkas belum ditegakkan alat.** Tidak ada pemeriksaan yang mencegah auditor
  menimpa laporan putaran pertama. Di kanal Issue aturannya alami (komentar); di kanal berkas aturannya
  **hanya imbauan** — ini **gap cek nyata**, tercatat di `_meta/DAFTAR_PEKERJAAN_TERBUKA.md`.

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | Protokol dibuat; `tools/audit_prompt.py` + `tools/ambil_verdict.py` dibangun | Tuntutan pemilik T29+T30. Sebelum ini repo hanya punya mekanisme review **PR**: `PROTOKOL_REVIEW_INDEPENDEN.md` mensyaratkan "nomor PR + SHA basis + SHA head" di anatomi butir 2, dan `review_prompt.py` hanya punya `--pr`/`--generic` (diperiksa di sumbernya, baris 616–618). **Klaim agent sebelumnya bahwa mekanisme review isi "sudah ada" dikoreksi sebagai over-claim** — yang sudah ada adalah mesin auditnya (QA 3 lapis, 7 lensa, klasifikasi, 8 arsip audit nyata, Sistem Klinik), tetapi **tidak ada prompt audit yang dibangkitkan alat**, sehingga prompt audit harus dikarang tangan: pihak yang diaudit menulis instruksi untuk pengadilnya sendiri. Ditemukan sebagai X-04/X-05 pada audit 17 Sep. Dokumen ini ditulis mengikuti **Standar Kelulusan Manual 5 syarat** yang ditambahkan di hari yang sama (6 bidang: apa/kapan/cara/prompt/sesudahnya/kalau gagal + tabel perintah 5 kolom) supaya tidak mengkhianati standarnya sendiri |
| 2026-09-17 | **Induk dinyatakan sebagai objek audit yang sah** (`--objek _meta`, `--objek tools`) | Instruksi eksplisit pemilik 17 Sep 2026: *"mekanisme itu juga harus tertanam di meta sistem … bukan pada sistem-sistem yang dibangun nya saja, tapi juga pada induk sistem itu sendiri."* Audit atas induk menemukan pengecualian struktural nyata: induk tidak tunduk pada kontrak warisannya sendiri dan 3 butir (W-03, W-07, W-09) tidak diterapkan tanpa terdeteksi alat mana pun |
| 2026-09-17 | Bagian "Yang belum terbukti" ditambahkan, termasuk bahwa **pengiriman via Issue belum diuji** | Menolak mengklaim mekanisme siap hanya karena rancangannya masuk akal. `gh issue create` membuat artefak nyata di repo sehingga butuh izin pemilik; yang terbukti baru kemampuan baca |
| 2026-09-17 (siang) | **KANAL PENYERAHAN DIROMBAK: berkas ter-commit jadi UTAMA, Issue jadi alternatif.** Bagian "Dua kanal penyerahan" ditambahkan; `ambil_verdict.py` membaca **kedua kanal** dan ketidaktersediaan satu kanal jadi **catatan**, bukan kegagalan fatal | **Uji nyata atas izin pemilik membuktikan rancangan awal SALAH:** `gh issue create` → **HTTP 403** `Resource not accessible by integration`, dan `permissions` API menunjukkan **semua izin repo false**. Sebaliknya `gh label create` **berhasil** dan `git push` **berhasil**. Mekanisme yang bergantung pada kanal diblokir = mekanisme yang tidak jalan. Kanal berkas ditaruh di `_meta/_internal/audit/` karena folder itu **tidak ikut ekstrak template** (diperiksa), jadi artefak per-run tidak bocor ke sistem anak |
| 2026-09-17 (siang) | **A-01/A-02 DITUTUP:** `_meta/PROTOKOL_AUDIT_ISI.md`, `_meta/PROTOKOL_REVIEW_INDEPENDEN.md`, `tools/audit_prompt.py`, `tools/ambil_verdict.py`, `tools/check_manuals.py` didaftarkan ke `CORE_REQUIRED` | Ditemukan oleh **audit yang dijalankan untuk menguji kanal itu sendiri**: menghapus ketiga artefak mekanisme audit-isi **tidak membuat alat mana pun gagal** (terverifikasi di salinan repo penuh `/tmp/full`, baseline hijau sebelum penghapusan). Prinsip *"kewajiban tidak diturunkan dari keberadaan"* ternyata tidak diterapkan pada mekanisme yang dibangun untuk menegakkannya. Sesudah didaftarkan, uji penghapusan yang sama **MERAH**: `- missing required file: tools/audit_prompt.py` |
