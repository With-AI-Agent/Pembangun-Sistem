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

## Log minimum

Gunakan log keputusan pada level yang terdampak. Untuk perubahan besar, catat juga di changelog/release notes:

| Tanggal | Lapisan | Observasi | Perubahan | Alasan | Bukti | Versi | Approval | Rollback |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
