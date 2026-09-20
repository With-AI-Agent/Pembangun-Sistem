# Quality Assurance & Evolution Protocol

## Tujuan

Meta-sistem ini memiliki mekanisme bawaan untuk memeriksa, mengaudit, memperbaiki, dan mengembangkan kualitas pada tiga lapisan yang berbeda:

1. **Lapisan meta-sistem:** memeriksa dan mengembangkan sistem pembangun sistem itu sendiri.
2. **Lapisan sistem domain:** setiap sistem yang dibangun mewarisi mekanisme untuk memeriksa dan mengembangkan dirinya sendiri.
3. **Lapisan output:** setiap sistem memeriksa output yang dihasilkannya sebelum output dipakai, diterbitkan, atau dianggap selesai.

Ketiga lapisan ini tidak berarti semua hal harus diaudit dengan kedalaman yang sama. Kedalaman pemeriksaan harus proporsional terhadap risiko, dampak, biaya perubahan, dan pentingnya output.

---

## Prinsip keputusan

### 1. Default aktif, tetapi dapat di-override

Mekanisme ini adalah default untuk sistem baru. Sistem boleh menonaktifkan atau menyederhanakan lapisan tertentu hanya jika:

- pengguna meminta secara eksplisit; atau
- Discovery membuktikan lapisan tersebut tidak relevan untuk domain itu.

Override wajib dicatat di manifest sistem dengan alasan, dampak, dan siapa yang menyetujui. “Tidak dilakukan karena lupa” bukan override yang valid.

### 2. Pemeriksaan tidak sama dengan perubahan

Audit hanya menghasilkan temuan dan rekomendasi. Agent tidak boleh mengubah aturan, struktur, atau output yang sudah dikunci hanya karena menemukan kemungkinan perbaikan.

Perubahan harus melewati:

```text
observasi → analisis → proposal → diskusi → keputusan → implementasi → verifikasi → rilis
```

### 3. Jangan mengoptimalkan tanpa bukti

Usulan upgrade harus menjelaskan:

- masalah yang hendak diselesaikan;
- bukti masalah atau alasan risikonya;
- solusi yang diusulkan;
- trade-off dan risiko baru;
- cara mengukur keberhasilan;
- cara rollback jika kualitas turun.

“Lebih lengkap”, “lebih canggih”, atau “lebih otomatis” bukan bukti bahwa kualitas meningkat.

### 4. Perubahan harus dapat dilacak dan dibalik

Setiap perubahan evolusioner wajib mencatat:

- tanggal;
- lapisan yang terdampak;
- versi sebelum dan sesudah;
- masalah/pemicu;
- keputusan dan alasan;
- bukti verifikasi;
- hasil yang diharapkan;
- rencana rollback;
- approval.

---

## Lapisan 1 — Audit dan evolusi meta-sistem

Meta-sistem diperiksa ketika:

- ada usulan perubahan prinsip atau workflow;
- pilot menemukan kegagalan;
- sistem baru berulang kali mengalami failure mode yang sama;
- tool, platform, atau kemampuan agent berubah;
- ada perubahan besar pada struktur repository;
- dilakukan release mayor atau audit berkala berbasis risiko.

Siklusnya:

1. Kumpulkan observasi dari audit, pilot, penggunaan, dan laporan pengguna.
2. Kelompokkan masalah: bug, ambiguitas, gap proses, kebutuhan baru, atau preferensi.
3. Tulis proposal perubahan; jangan langsung mengedit prinsip aktif.
4. Diskusikan dampak lintas sistem.
5. Uji proposal pada dokumen dan skenario yang terdampak.
6. Minta approval pengguna untuk perubahan Besar.
7. Implementasikan perubahan dalam branch/PR terpisah.
8. Jalankan regression check terhadap sistem dan contoh yang sudah ada.
9. Catat hasil, versi, dan keputusan.
10. Rilis hanya jika Definition of Done terpenuhi.

Audit meta-sistem tidak harus dilakukan setiap sesi. Trigger-nya berbasis risiko dan bukti agar sistem tidak mengalami audit berlebihan tanpa manfaat.

---

## Lapisan 2 — Self-improvement sistem domain

Setiap sistem baru wajib memiliki bagian atau dokumen yang menjelaskan:

- apa yang harus konsisten;
- failure mode yang perlu dipantau;
- kapan sistem dianggap mulai menyimpang;
- bagaimana pengguna/agent mengusulkan perbaikan;
- siapa yang menyetujui perubahan;
- bagaimana versi lama dipulihkan;
- kapan audit ulang dilakukan.

Siklus minimum:

```text
jalankan sistem → catat observasi → klasifikasikan → usulkan perbaikan
→ review/approval → implementasi → audit regresi → update versi
```

Sistem domain tidak boleh mengubah fondasi dirinya sendiri secara diam-diam selama produksi. Perubahan pada aturan yang diwariskan atau keputusan inti harus masuk jalur perubahan biasa.

---

## Lapisan 3 — Verifikasi output

Setiap output memiliki pemeriksaan minimum yang sesuai dengan jenisnya. Contoh kategori:

| Jenis output | Pemeriksaan minimum |
|---|---|
| Dokumen keputusan | Kelengkapan, konsistensi, sumber, status, approval |
| Output kreatif | Kesesuaian brief, kualitas teknis, brand/voice, hak penggunaan |
| Data | Skema, validasi, kelengkapan, duplikasi, provenance |
| Kode/aplikasi | Test, lint, security check, acceptance criteria, rollback |
| Rekomendasi | Sumber, asumsi, ketidakpastian, dampak |

Output harus memiliki status yang jelas:

```text
Draft → Checked → Approved → Released → Observed
```

“Checked” bukan berarti “Approved”. Output berisiko tinggi harus ditinjau manusia sesuai aturan approval sistem.

---

## Kedalaman pemeriksaan berbasis risiko

| Level | Kapan dipakai | Pemeriksaan |
|---|---|---|
| Ringan | Perubahan lokal dan mudah dibalik | Checklist, struktur, dependency langsung |
| Sedang | Output dipakai berulang atau memengaruhi satu area | Checklist lengkap, cross-check, review ringkas |
| Mendalam | Keputusan menyebar, sulit dibalik, atau output publik/berisiko | Audit multi-lensa, uji skenario, review manusia, bukti dan rollback |

Lapisan eksternal (meta v1.4.0, 6 Sep 2026): **eksternal: review oleh sesi lain sesuai `PROTOKOL_REVIEW_INDEPENDEN.md`** — wajib untuk pekerjaan level trigger L1 di protokol itu (penutupan gate/klaim permanen, bump versi aturan, perubahan struktural `_meta/`, operasi riwayat, merge yang mengubah klaim DONE/manifest); reviewer memverifikasi dari artefak dan tidak meng-merge atas namanya sendiri tanpa izin eksplisit pemilik (tidak ada auto-merge, kapan pun).

Agent harus menjelaskan level yang dipakai. Pengguna dapat meminta audit lebih dalam kapan saja.

### Lensa audit (dikodifikasi 5 Sep 2026 — temuan M-08; sebelumnya "multi-lensa" disebut tapi tidak pernah didefinisikan)

Audit level **Mendalam** wajib melewati semua lensa di bawah dan menuliskannya di laporan; level Sedang memakai minimal lensa 1–3:

1. **Konsistensi rujukan silang** — setiap path/kontrak yang dirujuk dokumen aktif benar-benar ada dan menunjuk hal yang sama.
2. **Kontradiksi antar-dokumen aktif** — satu aturan tidak boleh menuntut dua hal berbeda di dua tempat (contoh nyata: `--state open` vs kebutuhan melihat PR merged, M-04).
3. **Klaim vs bukti eksekusi** — jangan baca PASS-nya saja; jalankan alat TERHADAP DATA NYATA, dan jalankan data nyata terhadap fungsi alatnya. (Contoh nyata: fail-closed lulus terhadap fixture-nya sendiri tapi `False` untuk semua unit nyata di repo — M-02; ini yang tidak tertangkap 3 audit sebelumnya.)
4. **Jalur gagal** — FI/DoD benar-benar menegakkan (field absen = tidak aman, bukan aman).
5. **Kemudahan pakai (kacamata pengguna awam)** — cukup satu prompt? Apakah dokumen yang ditempel pengguna adalah versi terbaru? (Contoh nyata: prompt pembuka PANDUAN vs entry point 00 berbeda langkah — M-05/M-15.)
6. **Propagasi ke sistem masa depan** — aturan baru harus sampai ke SEMUA titik turunannya: template distribusi, daftar tool, manifest template, DoD, Discovery, validator. Yang hanya ada di narasi = belum ditanam.
7. **Kesehatan repo** — branch/PR menggantung, artefak terjebak, file yang tidak seharusnya ter-track, artefak basi (ringkasan cadangan — M-09).

**Klasifikasi temuan WAJIB** di laporan audit (langkah 2 siklus): setiap temuan diberi jenis `B` (bug) / `A` (ambiguitas) / `G` (gap proses) / `N` (kebutuhan baru) / `P` (preferensi/housekeeping) + prioritas P1–P3 + dasar bukti (path/commit/output tool). Temuan tanpa bukti terverifikasi dicatat sebagai "dugaan" dan tidak boleh langsung jadi perbaikan.

---

## Regression check wajib

Setelah perubahan pada aturan, template, atau workflow, periksa:

1. Apakah contoh lama masih valid?
2. Apakah dependency dan cross-reference masih valid?
3. Apakah aturan lama yang sengaja dipertahankan masih konsisten?
4. Apakah perubahan memperbaiki masalah tanpa membuat failure mode baru?
5. Apakah sistem yang mewarisi aturan perlu migrasi?
6. Apakah template dan manifest perlu diperbarui?
7. Apakah ringkasan cadangan masih akurat?

Jika jawaban belum diketahui, status perubahan adalah `needs-validation`, bukan `improved`.

---

## Rollback dan penurunan kualitas

Jika setelah perubahan kualitas turun:

1. hentikan propagasi perubahan;
2. tandai versi yang bermasalah;
3. bandingkan hasil sebelum/sesudah;
4. lihat log keputusan dan bukti verifikasi;
5. rollback atau buat perbaikan baru melalui PR;
6. catat penyebab dan pelajaran;
7. tambahkan regression test agar masalah tidak berulang.

Versi lama tidak boleh dihapus sebelum versi baru terbukti stabil.

---

## Lapisan pengeluaran: folder sistem mandiri

Sebuah sistem yang foldernya belum lolos `tools/check_selfcontained.py` **belum** benar-benar self-contained. Protokol, definisi folder sebagai deliverable, dan cara mengujinya ada di `_meta/PAKET_REPO_MANDIRI.md`.

---

## Batasan anti-recursion

Mekanisme ini bersifat rekursif secara prinsip, tetapi tidak boleh menghasilkan audit tanpa akhir. Pada setiap lapisan, tetapkan:

- objek yang diaudit;
- trigger audit;
- level kedalaman;
- acceptance criteria;
- kondisi berhenti;
- pemilik approval.

Sistem tidak perlu mengaudit mekanisme auditnya pada setiap output. Audit mekanisme dilakukan saat ada bukti masalah, perubahan besar, atau release yang relevan.

---

## ATURAN CAKUPAN — cakupan membatasi pencarian dan klaim, TIDAK PERNAH membatasi laporan

Ditambahkan 17 Sep 2026. Aturan ini **melengkapi** Batasan anti-recursion di atas, dan keduanya menjawab
masalah yang berbeda — mencampuradukkannya adalah sumber kesalahan nyata:

- **Batasan anti-recursion** membatasi **LOOP** (berapa dalam/berapa kali audit boleh berulang).
- **Aturan cakupan** membatasi **RENCANA PENCARIAN dan KLAIM** (apa yang diperiksa sistematis, dan apa yang
  boleh dinyatakan sudah diperiksa).
- **Tidak satu pun dari keduanya membatasi LAPORAN.**

### Aturannya

> **Cakupan membatasi RENCANA PENCARIAN dan KLAIM. Cakupan TIDAK PERNAH membatasi LAPORAN.**

**Yang dibatasi cakupan:**
1. Apa yang dicari **secara sistematis** — yaitu checklist wajib audit.
2. Apa yang boleh **DIKLAIM** sudah diperiksa. Menyebut cakupan lebih luas dari yang dikerjakan adalah
   kebohongan, dan itu dilarang.

**Yang TIDAK BOLEH dibatasi cakupan:**
3. Apa yang boleh **DILAPORKAN**. Temuan di luar cakupan **WAJIB tetap dilaporkan**.

**Kewajiban saat menemukan sesuatu di luar cakupan:**
- laporkan dengan label **"di luar cakupan"**;
- beri **klasifikasi** (`B`/`A`/`G`/`N`/`P`) + **prioritas** (`P1`–`P3`) + **dasar bukti** — sama seperti
  temuan dalam cakupan, karena nilainya tidak lebih rendah hanya karena tidak diminta;
- **jangan bertindak** atasnya tanpa mandat — **menemukan ≠ memperbaiki** (Prinsip 2 di atas:
  *"Pemeriksaan tidak sama dengan perubahan"*);
- kalau menyadari telah membaca sesuatu di luar jalur yang diizinkan, **ungkapkan (disclosure)** — jangan
  disembunyikan, dan jangan dipakai diam-diam sebagai dasar kesimpulan.

**Yang dilarang:**
- **mengklaim** cakupan lebih luas dari yang benar-benar dikerjakan;
- **membuang atau menghaluskan** temuan karena tidak diminta (ini juga melanggar prinsip append-only
  `PROTOKOL_REVIEW_INDEPENDEN.md` #8: *"jangan menghaluskan"*);
- **menyaring** temuan supaya laporan "muat" dalam cakupan yang diminta.

### Kenapa aturan ini perlu ditulis eksplisit

Pemicunya adalah kalimat nyata dari seorang reviewer yang dibaca pemilik repo ini: *"Saya baca dulu aturan
pemeriksa laporan supaya laporannya memenuhi syarat **tanpa melebih-lebihkan cakupan**."* Kalimat itu
**ambigu** — bisa berarti disiplin anti-overclaim (benar), bisa berarti penyaringan temuan (berbahaya).
Pemilik menyatakan kejanggalannya, dan **kejanggulan itu sah**.

Aturan ini **bukan karangan baru** — repo ini sudah mempraktikkannya. Enam preseden yang memeriksanya
(17 Sep 2026):

| Preseden | Apa yang terjadi |
|---|---|
| berkas log sesi _log-sesi/LOG_SESI_2026-09-15_3.md (tanpa backtick — lihat catatan di bawah tabel) | Log `OPEN` basi milik sesi lain **DITEMUKAN tapi TIDAK DISENTUH** — hanya **dicatat + dilaporkan** |
| berkas log sesi _log-sesi/LOG_SESI_2026-09-16_11.md + body PR #35 (tanpa backtick, alasan sama) | **"disklor paparan"**: sesi **mengungkapkan** telah membuka berkas di luar jalur baca wajib **sebelum** keputusan pertama ter-commit |
| `_meta/_internal/HOUSEKEEPING_2026-09-16.md` | 5 branch diverged + log `OPEN` milik sesi lain ditemukan di luar mandat → **dilaporkan lengkap dengan rekomendasi**, tanpa menghapus/menindak |
| Prinsip pada dokumen ini sendiri | *"Temuan tanpa bukti terverifikasi dicatat sebagai 'dugaan' dan tidak boleh langsung jadi perbaikan"* — temuan **lemah** pun dicatat, bukan dibuang |
| Skema klasifikasi `B`/`A`/`G`/`N`/`P` | Adanya kategori **`N` (kebutuhan baru)** dan **`P` (preferensi/housekeeping)** = **slot struktural** untuk temuan yang bukan objek utama. Skema ini hanya masuk akal kalau temuan di luar cakupan memang **ditampung** |
| `PROTOKOL_REVIEW_INDEPENDEN.md` #8 | **append-only**, *"jangan menghapus riwayat, jangan menghaluskan"* |

> **Catatan penulisan rujukan (belajar dari 4 kejadian nyata pada 17 Sep 2026):** nama berkas di
> `_log-sesi/` dan di dalam folder sistem **ditulis tanpa backtick** di dokumen `_meta/`. Alasannya mekanis,
> bukan gaya: kedua area itu **tidak ikut ke ekstrak template bootstrap**, sehingga rujukan ber-backtick ke
> sana menjadi **tak-terselesaikan** di ekstrak, menggeser pin `EXPECTED_TEMPLATE_WARNINGS` (harus persis 5)
> dan membuat `tools/test_failure_injection.py` MERAH — **tanpa pesan yang menyebut berkas penyebabnya**.
> Yang **aman** diberi backtick: `tools/*.py` dan berkas `_meta/*.md` (ikut ke ekstrak), serta `_meta/_internal/`
> (terverifikasi empiris tidak memicu warning). Aturan umumnya: **kalau ragu, tulis tanpa backtick sebagai
> provenance.** Preseden lebih tua: v1.12.1 *"tidak menambah rujukan ber-backtick ke dokumen aktif"*.

**Penerapan pada audit 17 Sep 2026:** audit itu dimandatkan untuk **manual pengguna**. Enam temuan di luar
cakupan (allowlist jaringan yang belum tercatat sebagai fakta platform; tidak ada butir warisan untuk
mekanisme audit-isi; `review_prompt.py` hanya terikat PR; tidak ada pengambilan hasil otomatis; `gh issue
create` belum teruji) **tetap dilaporkan** dengan label, dan **tidak satu pun ditindak tanpa mandat**.
Lihat `_meta/_internal/AUDIT_MANUAL_DAN_MEKANISME_REVIEW_2026-09-17.md` bagian 4.

---
## Log minimum

Gunakan log keputusan pada level yang terdampak. Untuk perubahan besar, catat juga di changelog/release notes:

| Tanggal | Lapisan | Observasi | Perubahan | Alasan | Bukti | Versi | Approval | Rollback |
|---|---|---|---|---|---|---|---|---|
| 2026-09-17 | Lapisan 1 (meta) | Tabel log ini **ditemukan KOSONG** padahal dokumen ini jelas berevolusi — bagian "Lensa audit" menyebut pengkodifikasiannya sendiri terjadi 5 Sep 2026 (temuan M-08), tetapi tidak ada satu pun baris log yang mencatatnya. **Entri sebelum 17 Sep 2026 TIDAK direkonstruksi**: menulis riwayat yang tidak kusaksikan sendiri = fabrikasi, dan itu lebih buruk daripada tabel yang kosong. Yang dicatat sebagai gantinya: **fakta bahwa tabelnya kosong**, sebagai temuan pelanggaran W-05 pada dokumen hidup | **ATURAN CAKUPAN ditambahkan** sebagai bagian baru: cakupan membatasi RENCANA PENCARIAN dan KLAIM, **TIDAK PERNAH** membatasi LAPORAN. Termasuk kewajiban melabeli + mengklasifikasi temuan di luar cakupan, larangan menyaring/menghaluskan, larangan bertindak tanpa mandat, dan kewajiban disclosure. **6 preseden repo** dicantumkan sebagai bukti bahwa aturan ini bukan karangan baru | Instruksi eksplisit pemilik 17 Sep 2026 (T31) setelah membaca kalimat reviewer *"supaya laporannya memenuhi syarat tanpa melebih-lebihkan cakupan"* dan menyatakan kejanggalannya: *"seharusnya jika memang ada yang perlu dilaporkan maka seharusnya itu tetap dilaporkan biarpun tidak masuk dalam cakupan yang diminta."* **Verdict agent: pemilik BENAR** — kalimat itu ambigu, dan yang diputuskan adalah aturannya supaya ambiguitas tidak bisa muncul lagi | `_meta/_internal/AUDIT_MANUAL_DAN_MEKANISME_REVIEW_2026-09-17.md` bagian 4 (penerapan nyata: 6 temuan di luar cakupan dilaporkan, tidak ditindak); `_meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md` bagian L.3 (6 preseden diverifikasi per berkas); seluruh 7 alat PASS setelah perubahan | meta v1.15.0 | Mandat pemilik T31 + delegasi "lakukan yang terbaik"; menunggu review independen **L1** (perubahan struktural `_meta/` = L1 wajib per `PROTOKOL_REVIEW_INDEPENDEN.md` baris 17) | revert commit yang menambah bagian ATURAN CAKUPAN (aditif murni, tanpa migrasi data) |
