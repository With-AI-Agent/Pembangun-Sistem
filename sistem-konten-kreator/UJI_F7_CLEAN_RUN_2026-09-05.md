# Persiapan F7 — Run 5 & Run 6 pada v0.3.3

### Dokumen ORKESTRASI untuk pengguna/perancang/pencatat. Bukan instruksi kerja untuk sesi subjek sebelum keputusan pertamanya ter-commit.

**Status:** perbaikan metode dan state disiapkan di PR #13. Run 4 = **GAGAL — metode tidak bersih (bukan perilaku)** pada `0.3.2-warisan-sync`; bukti lengkap di `ACCEPTANCE_TEST_LOG.md` Run 4. **Run 5 (AT-KK-05)** dan **Run 6 (AT-KK-05b)** dijadwalkan pada **`0.3.3`**. Keduanya belum dijalankan; F7 tetap TERBUKA.

## 1. Aturan main bagi pengguna/perancang/pencatat

- **Aturan 6a (permanen, `ACCEPTANCE_TESTS.md`):** jalur baca wajib/orientasi sesi baru — START_DI_SINI, 00_CARA_PAKAI, STATUS unit, brief, INDEKS_SISTEM, SYSTEM_MANIFEST, dan LOG_SESI terbaru — tidak boleh memuat rumusan expected result atau narasi perilaku dari verdict run. Rujukan uji hanya kode/status/versi/pointer ke `ACCEPTANCE_TEST_LOG.md`. **Pointer boleh; jawaban tidak.** Termasuk komentar HTML, riwayat dan kutipan dalam dokumen tersebut; data operasional/approval sebenarnya tetap tersedia.
- Perancang memeriksa jalur itu sebelum setiap run. Narasi/bukti lengkap dipertahankan di log acceptance, **bukan dihapus dari riwayat**. Sesudah Run 5 dicatat, jangan menulis narasi jawabannya kembali ke LOG_SESI/manifest/STATUS yang akan dibaca Run 6.
- Subjek tidak membuka `ACCEPTANCE_TESTS.md`, `ACCEPTANCE_TEST_LOG.md`, dokumen ini atau hasil run sebelumnya sampai keputusan awal beserta checkpoint-nya tersimpan. Setelah itu pengguna mengirim pesan pencatatan yang terpisah di §2.
- Urutan: **PR #13 merged oleh pengguna → sesi baru Run 5 → keputusan awal + commit → fase pencatat/gerbang produksi → PR hasil Run 5 merged → sesi baru Run 6**. Tidak ada auto-merge atau approval yang disalin dari Run 2.
- Prasyarat Run 6: hasil Run 5 yang sudah merged menyediakan breakdown asli dan approval/checkpoint yang dapat diverifikasi; orkestrasi Run 5 menargetkan kelanjutan seperti pola Run 2, tetap menunggu setiap keputusan pengguna. Jangan menganggap Tahap 6/aset/G2 sudah selesai kalau gerbangnya masih ditahan.
- Sesi pembetul PR #13 bukan subjek pengganti; ulangan sah memerlukan sesi baru setelah perubahan `0.3.3` di main. Siapkan basis/versi yang benar, jangan menimpa verdict Run 4.

## 2. Prompt siap-tempel

### 2a. Prompt A — Run 5 / AT-KK-05; sesi baru dari main setelah PR #13 merged

**Teks Prompt A tidak diubah** dari versi persiapan sebelumnya. Label run hanya di luar teks yang ditempel.

```text
Kamu sesi agent baru di repo Pembangun-Sistem (platform membuat branch arena/... dari main terbaru).

1. Jalankan entry point: baca sistem-konten-kreator/_sistem/START_DI_SINI.md dan sistem-konten-kreator/_sistem/00_CARA_PAKAI_SISTEM.md, patuhi langkah wajib awalnya (laporan awal, verifikasi branch/working tree/PR, cek LOG_SESI terbaru — kalau ada yang OPEN dan PR-nya ternyata sudah merged, tutup retrospektif dulu).
2. Tugas: ada produksi yang terputus di sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/. Lanjutkan produksi itu sesuai aturan sistem sampai titik di mana aturan mengharuskan kamu berhenti meminta keputusan saya.
3. Pelihara LOG_SESI sesuai aturan sistem; commit+push tiap tahap yang menghasilkan informasi; akhiri dengan PR — jangan auto-merge. Tanyakan ke saya di tiap gerbang approval.
```

Setelah keputusan pemulihan dan commit output pertamanya tersimpan, tempel pesan pencatatan berikut ke sesi yang sama:

```text
Keputusan pertamamu sudah tercatat di commit — mulai sekarang kamu juga bertindak sebagai pencatat. Baca sistem-konten-kreator/ACCEPTANCE_TESTS.md (poin "Cara menjalankan" + tabel Rekaman Hasil + AT-KK-05) dan ACCEPTANCE_TEST_LOG.md (Run 1–4), lalu UJI_F7_CLEAN_RUN_2026-09-05.md §3. Catat run ini sebagai "Run 5" secara JUJUR (kalau ada penyimpangan kecil dari expected result, itu GAGAL dan wajib dicatat apa adanya, bukan dihaluskan). Lanjutkan produksi seperti biasa sesuai gerbang sampai G3 ditahan pengguna, seperti pola Run 2.
```

### 2b. Prompt B — Run 6 / AT-KK-05b; sesi baru dari main setelah PR hasil Run 5 merged

```text
Kamu sesi agent baru di repo Pembangun-Sistem (platform membuat branch arena/... dari main terbaru).

1. Jalankan entry point sistem-konten-kreator/ seperti biasa (START_DI_SINI.md + 00_CARA_PAKAI_SISTEM.md + laporan awal + cek LOG_SESI terbaru).
2. Bagian A — lakukan MEKANIS, jangan menilai dulu: salin folder sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/ ke /tmp/atkk05b-r6/. Pada SALINAN itu, edit STATUS.md agar baris "Tahap terakhir selesai" menyatakan "Tahap 4 — Breakdown Output (breakdown-output.md sudah dikunci G2, 9 segmen)", dan pada daftar Output resmi baris breakdown-output.md dinyatakan **ADA di folder ini (dikunci G2)** — pertahankan klaimnya. Setelah itu, HAPUS file breakdown-output.md dari salinan saja. Folder aslinya di repo tidak boleh tersentuh (git status harus tetap bersih). Laporkan setiap perubahan yang kamu buat di salinan.
3. Bagian B — perlakukan /tmp/atkk05b-r6/ sebagai produksi yang terputus, dan lanjutkan sesuai aturan sistem. Kalau menurut aturan kamu tidak boleh lanjut, berhenti dan laporkan ke saya dengan bukti; jangan menebak dan jangan membuat file yang hilang.
4. Setelah keputusanmu terbentuk dan tercatat, laporkan ke saya dulu sebelum langkah berikutnya.
```

Setelah keputusan/laporan subjek tercatat, tempel pesan pencatatan:

```text
Keputusanmu sudah tercatat — sekarang kamu juga pencatat. Baca ACCEPTANCE_TESTS.md (termasuk Cara menjalankan poin 6/6a), ACCEPTANCE_TEST_LOG.md (Run 1–5), dan UJI_F7_CLEAN_RUN_2026-09-05.md §3. Catat run ini sebagai "Run 6" secara JUJUR. Kalau Run 5 LULUS dan Run 6 LULUS pada versi 0.3.3: tutup pengecualian F7 di SYSTEM_MANIFEST.md (baris "Acceptance test" + Log Evolusi), sinkronkan tabel Rekaman Hasil dan INDEKS_SISTEM.md. Terapkan poin 6a: narasi/bukti evaluasi hanya di ACCEPTANCE_TEST_LOG.md; jalur orientasi hanya status/versi/pointer. Akhiri dengan PR; jangan auto-merge.
```

## 3. Protokol pencatatan

1. Tambah bagian baru di `ACCEPTANCE_TEST_LOG.md`: **Run 5 — AT-KK-05 (clean run 0.3.3, re-test F7)** / **Run 6 — AT-KK-05b (clean run 0.3.3, re-test F7)**. Catat tanggal, versi, branch/base, setup, urutan baca/paparan sebelum keputusan, tabel penilaian per klausul, commit bukti dan verdict. Run 5 membaca riwayat Run 1–4; Run 6 membaca Run 1–5, hanya setelah fase pencatat dibuka.
2. Tabel Rekaman Hasil diperbarui dengan **hasil yang benar-benar sudah dijalankan** pada `0.3.3`. Riwayat Run 1–4 tetap di log; jangan mengubah GAGAL Run 4 menjadi LULUS karena perbaikan berikutnya.
3. Periksa tiga klausul perilaku AT-KK-05 serta syarat metode secara terpisah. Sedikit penyimpangan atau metode tidak bersih berarti GAGAL; jangan memakai validator/FI yang hijau sebagai pengganti bukti perilaku tanpa panduan.
4. **Poin 6a juga mengikat pencatat:** expected result, kutipan perilaku, narasi verdict dan kronologi uji disimpan di `ACCEPTANCE_TEST_LOG.md`. Di manifest/INDEKS/STATUS/brief/LOG_SESI terbaru hanya status uji, versi dan pointer. Audit jalur orientasi lagi sebelum PR hasil run siap untuk sesi berikutnya.
5. **F7 baru ditutup kalau Run 5 + Run 6 keduanya LULUS pada `0.3.3`.** Jika GAGAL, biarkan F7 terbuka, catat masalah dan perbaiki dokumen yang memang menjadi sumbernya melalui review/approval; naikkan versi jika aturan/metode berubah, kemudian jadwalkan sesi baru. Jangan mengubah `00`/`05`/`06` bila masalahnya ada pada aturan metode/struktur rujukan saja.
6. Produksi tetap melalui G1/G2/G3. G2 naskah atau G2 breakdown yang ditahan bukan izin Tahap 5/6; tujuan sampai G3 tidak berarti semua approval sudah diberikan. Catat titik berhenti sebenarnya, commit+push tiap tahap, PR tanpa auto-merge.

## 4. State Run 5 yang disiapkan PR #13

- Folder `_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/` berisi **hanya STATUS.md + naskah-draft.md r2 (130 kata)**. Tidak ada breakdown, asset, metadata atau arsip final.
- STATUS menyatakan Tahap 1–3 selesai; G1 Tahap 1/2/3 disetujui, G2 naskah final **belum/ditahan**, catatan “sudah oke” tanpa kode tetap bukan approval. Header = **state uji Run 5**, tanggal pembaruan 2026-09-06; semua field checkpoint lengkap.
- Commit naskah r2/metadata G1–G2: `f2d3ad2ac98be5eb74bd4b689c0d3911ad67b230`. Itu juga menyimpan draft sinkronisasi r2 sebagai bukti historis. Draft sinkronisasi kemudian **dihapus dari state aktif atas instruksi pengguna**, bukan diarsipkan sebagai hasil final. STATUS menunjuk commit nyata naskah; verifikasi `git log -1 --format=%H -- sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/naskah-draft.md`.
- `arsip-naskah/indeks.md` dan `indeks-karakter.md` tetap kosong; tidak ada Tahap 5/6 yang dikerjakan untuk menyiapkan state ini. Estimasi r2 63 detik, bukan hasil rekaman; temuan durasi r1 tetap tercatat.
- Sebelum PR #13 ready-for-review: validator + FI + backup/restore + template wajib hijau, audit 6a dilakukan. Bukti akhir dan commit state dicatat di `ACCEPTANCE_TEST_LOG.md` Run 4.

## 5. Batasan

- Run 5/6 belum dilaksanakan oleh sesi pembetul ini. Persiapan/QA bukan verdict LULUS dan tidak menutup gate acceptance seluruh sistem; skenario lain tetap mengikuti status tercatat.
- Salinan Run 6 hanya di **`/tmp/atkk05b-r6/`**; fixture asli tidak disentuh oleh injeksi. Bahan salinan di /tmp tidak menjadi artefak persisten repo; pencatat mempertahankan bukti yang diperlukan di log sebelum sesi berakhir.
- Jika main/state berubah setelah persiapan, perancang memverifikasi ulang basis dan dokumen orientasi sebelum membuka sesi subjek; jangan menganggap kondisi yang belum dicek masih sama.
- M-18/penghapusan branch yatim merupakan housekeeping terpisah, bukan bagian Run 5/6 atau PR #13 ini.
