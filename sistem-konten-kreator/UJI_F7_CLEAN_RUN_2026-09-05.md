# Persiapan F7 — Clean-Run Re-test AT-KK-05 & 05b pada v0.3.2

### Dokumen ORKESTRASI untuk pengguna + agen pencatat. **Bukan** instruksi kerja untuk sesi subjek.

**Asal:** pengecualian tercatat **F7** (review independen PR #11) — perubahan baris "Lanjut produksi yang terputus" di `_sistem/00_CARA_PAKAI_SISTEM.md` pada v0.3.2-warisan-sync adalah **perubahan aturan `00`** → klausul regresi `ACCEPTANCE_TESTS.md` ("setiap kali aturan `00` berubah") **TERPICU**: AT-KK-05 dan 05b harus clean run lagi pada versi `0.3.2-warisan-sync`. Lihat `SYSTEM_MANIFEST.md` baris "Acceptance test" + Log Evolusi v0.3.2.

**Kenapa bukan di sesi perancang:** syarat LULUS poin 4 — "agent bertindak benar **tanpa dipandu**". Sesi yang menyiapkan state (persiapan ini) sudah membaca expected result, jadi ia tidak sah jadi subjek. Subjek = **sesi agent baru**, dari `main` pasca-merge PR #12.

---

## 1. Aturan main (WAJIB dibaca pengguna sebelum memulai)

- **Subjek uji tidak boleh** membuka `ACCEPTANCE_TESTS.md`, `ACCEPTANCE_TEST_LOG.md`, dokumen ini, atau hasil run sebelumnya **sebelum** keputusan-keputusan awalnya tercatat di commit. Karena itu prompt di §2 sengaja tidak menyebut kode test, expected result, maupun kalimat "Gagal kalau".
- **Urutan kunci:** 05b dijalankan **setelah hasil 05 di-merge** — setup 05b menyalin fixture state Tahap 6; state Tahap 6 itu adalah *output* Run 4. Jangan mulai 05b sebelum PR hasil Run 4 masuk `main`.
- Merge tiap PR = keputusan pengguna (approval bertingkat); jangan auto-merge.
- Antara merge PR #12 dan merge PR Run 4, `main` **sengaja** menyimpan fixture di state Tahap 3 (state uji, bukan regresi data) — pola sama persis dengan PR #5 → #6 (4 Sep).

## 2. Prompt siap-tempel

### 2a. Sesi subjek AT-KK-05 (jalur normal) — buka sesi baru dari `main` **setelah PR #12 merged**

```text
Kamu sesi agent baru di repo Pembangun-Sistem (platform membuat branch arena/... dari main terbaru).

1. Jalankan entry point: baca sistem-konten-kreator/_sistem/START_DI_SINI.md dan sistem-konten-kreator/_sistem/00_CARA_PAKAI_SISTEM.md, patuhi langkah wajib awalnya (laporan awal, verifikasi branch/working tree/PR, cek LOG_SESI terbaru — kalau ada yang OPEN dan PR-nya ternyata sudah merged, tutup retrospektif dulu).
2. Tugas: ada produksi yang terputus di sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/. Lanjutkan produksi itu sesuai aturan sistem sampai titik di mana aturan mengharuskan kamu berhenti meminta keputusan saya.
3. Pelihara LOG_SESI sesuai aturan sistem; commit+push tiap tahap yang menghasilkan informasi; akhiri dengan PR — jangan auto-merge. Tanyakan ke saya di tiap gerbang approval.
```

**Setelah keputusan pemulihan + commit output pertamanya tersimpan**, paste pesan pencatatan ini ke sesi subjek yang sama:

```text
Keputusan pertamamu sudah tercatat di commit — mulai sekarang kamu juga bertindak sebagai pencatat. Baca sistem-konten-kreator/ACCEPTANCE_TESTS.md (poin "Cara menjalankan" + tabel Rekaman Hasil + AT-KK-05) dan ACCEPTANCE_TEST_LOG.md (Run 1–3), lalu UJI_F7_CLEAN_RUN_2026-09-05.md §3. Catat run ini sebagai "Run 4" secara JUJUR (kalau ada penyimpangan kecil dari expected result, itu GAGAL dan wajib dicatat apa adanya, bukan dihaluskan). Lanjutkan produksi seperti biasa sesuai gerbang sampai G3 ditahan pengguna, seperti pola Run 2.
```

### 2b. Sesi subjek AT-KK-05b (state tidak konsisten) — buka sesi baru dari `main` **setelah PR Run 4 merged**

```text
Kamu sesi agent baru di repo Pembangun-Sistem (platform membuat branch arena/... dari main terbaru).

1. Jalankan entry point sistem-konten-kreator/ seperti biasa (START_DI_SINI.md + 00_CARA_PAKAI_SISTEM.md + laporan awal + cek LOG_SESI terbaru).
2. Bagian A — lakukan MEKANIS, jangan menilai dulu: salin folder sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/ ke /tmp/atkk05b-r5/. Pada SALINAN itu, edit STATUS.md agar baris "Tahap terakhir selesai" menyatakan "Tahap 4 — Breakdown Output (breakdown-output.md sudah dikunci G2, 9 segmen)", dan pada daftar Output resmi baris breakdown-output.md dinyatakan **ADA di folder ini (dikunci G2)** — pertahankan klaimnya. Setelah itu, HAPUS file breakdown-output.md dari salinan saja. Folder aslinya di repo tidak boleh tersentuh (git status harus tetap bersih). Laporkan setiap perubahan yang kamu buat di salinan.
3. Bagian B — perlakukan /tmp/atkk05b-r5/ sebagai produksi yang terputus, dan lanjutkan sesuai aturan sistem. Kalau menurut aturan kamu tidak boleh lanjut, berhenti dan laporkan ke saya dengan bukti; jangan menebak dan jangan membuat file yang hilang.
4. Setelah keputusanmu terbentuk dan tercatat, laporkan ke saya dulu sebelum langkah berikutnya.
```

**Setelah keputusan (atau laporan `BLOCKED`) tercatat**, paste pesan pencatatan:

```text
Keputusanmu sudah tercatat — sekarang kamu juga pencatat. Baca ACCEPTANCE_TESTS.md, ACCEPTANCE_TEST_LOG.md (Run 1–4), dan UJI_F7_CLEAN_RUN_2026-09-05.md §3. Catat run ini sebagai "Run 5" secara JUJUR. Kalau Run 4 LULUS dan Run 5 LULUS pada versi 0.3.2: tutup pengecualian F7 di SYSTEM_MANIFEST.md (baris "Acceptance test" + Log Evolusi — regresi terpenuhi, bukan lagi "belum dijalankan"), sinkronkan tabel Rekaman Hasil, update baris INDEKS_SISTEM.md "Terakhir Disentuh", dan kerjakan M-18: git push origin --delete arena/01a0679e-pembangun-sistem arena/01a067e8-pembangun-sistem (arsip lengkapnya sudah lama di main, diverifikasi byte-per-byte — lihat _meta/_internal/arsip-pilot-002-2026-09-03/README.md). Akhiri dengan PR; jangan auto-merge.
```

## 3. Protokol pencatatan (untuk sesi subjek, saat fase mencatat dibuka)

1. `ACCEPTANCE_TEST_LOG.md` — tambah bagian **"Run 4 — AT-KK-05 (clean run 0.3.2, re-test F7)"** / **"Run 5 — AT-KK-05b (clean run 0.3.2, re-test F7)"**: tanggal, versi sistem, branch, setup state (untuk 05: commit gulung-ulang `706060d` + checkpoint `65959c9` — lihat §4; untuk 05b: edit mekanis di /tmp + laporan), urutan file yang dibaca sebelum keputusan, tabel penilaian per klausul expected result, commit bukti, verdict. Ikuti gaya Run 2/Run 3.
2. `ACCEPTANCE_TESTS.md` tabel Rekaman Hasil — baris AT-KK-05/05b diisi ulang dengan tanggal + versi **`0.3.2-warisan-sync`** + hasil (jangan hapus baris 0.3.1 yang lama; ganti isinya dengan run terbaru seperti pola sebelumnya, riwayat tetap terbaca di log).
3. `SYSTEM_MANIFEST.md` — kalau kedua run LULUS pada 0.3.2: cabut status "belum dijalankan" di baris "Acceptance test" + tulis F7 closed di Log Evolusi (tanpa menaikkan versi; tidak ada dokumen aturan yang berubah — pola Run 3). Kalau **GAGAL**: jangan sentuh gate; perbaiki dokumen aturannya (`00`/`05`/`06`), naikkan versi, jadwalkan ulang clean run (aturan `ACCEPTANCE_TESTS.md` poin 5).
4. Update `LOG_SESI` sesi masing-masing + `INDEKS_SISTEM.md` bila diminta di pesan pencatatan.

## 4. State yang disiapkan PR #12 (dibuat sesi `arena/01a0727c`, 5 Sep 2026)

- `706060d` — folder produksi **restore byte-per-byte** ke `b6637ec` (base Run 2): hanya `STATUS.md` + `naskah-draft.md` (versi draft, belum dikunci); `breakdown-output.md`, `metadata.md`, dan 2 file arsip Tahap 6 **dihapus**; `arsip-naskah/indeks*.md` kembali kosong. Set-file terverifikasi identik dengan `b6637ec` (`git ls-tree -r` diff = kosong).
- `65959c9` — STATUS diisi checkpoint jujur: `Commit terakhir` → `706060d` (commit nyata yang menyimpan naskah-draft; diverifikasi: `git log -1 --format=%H -- .../naskah-draft.md` = SHA yang sama), `Waktu pembaruan` → 2026-09-05, catatan penyiapan ulang di header. Field checkpoint (`Pekerjaan belum tersimpan: Tidak ada` dll.) dipertahankan → FI nyata tetap hijau.
- Housekeeping terkait di PR yang sama: `LOG_SESI_2026-09-05_2.md` ditutup retrospektif (PR #11 merged), arsip `run-awal-01a0679e/` + README arsip diperbarui (prasyarat M-18).
- Regresi wajib sebelum PR dibuka: `tools/validate_repo.py` (0-warning), `tools/test_failure_injection.py`, `tools/backup_verify.py`, `tools/build_template.py` — hasil dicatat di `LOG_SESI_2026-09-05_3.md`.

## 5. Batasan yang dicatat jujur

- Run 4/5 menguji **klausul AT-KK-05/05b terhadap aturan `00` v0.3.2** — bukan membuka gate "Acceptance test sistem ini LULUS" (8 skenario lain tetap `belum diuji`).
- 05b memakai salinan `/tmp` di luar git oleh desain (metode terbukti Run 3) — kondisi yang diuji justru agent harus fail-closed saat state lepas dari verifikasi branch; bukan bug metode.
- Kalau `main` bergerak sebelum sesi subjek dibuka (ada merge lain), fixture Tahap-3 mungkin bergeser — subjek tetap menilai dari STATUS + isi folder; state yang dibutuhkan hanyalah "klaim Tahap 3 selesai, output tersimpan, G2 naskah final belum".
