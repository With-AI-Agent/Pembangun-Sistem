# Status Unit — pilot-002

- **Status:** `in-progress`
- **Level pemeriksaan:** `Ringan`
- **Tahap terakhir selesai:** Capture (tahap 1 dari 6)
- **Tahap berikutnya:** Extract (tahap 2) — ambil ide, fakta, definisi, dan contoh dari `fixtures/SUMBER_CHECKPOINT_RECOVERY.md`, setiap butir wajib membawa rujukan ke bagian sumbernya
- **Output resmi:** `OUTPUT.md` (berstatus `draft`; hanya bagian identitas sumber + tujuan belajar + pertanyaan awal yang terisi)
- **Sumber konteks yang dibaca:**
  - `../../fixtures/SUMBER_CHECKPOINT_RECOVERY.md` (bahan belajar; snapshot dari `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`)
  - `../../SYSTEM_MANIFEST.md`
  - `../../START_DI_SINI.md`
  - `../../WORKFLOW.md`
  - `../../OUTPUT_TEMPLATE.md`
  - `../../QUALITY.md`
  - `../../STATUS_TEMPLATE.md`
  - `_meta/ACCEPTANCE_TESTS.md` (AT-04 checkpoint dan recovery)
- **Keputusan baru:**
  - Bahan belajar unit ini = `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`, bukan fixture simulasi lama; alasan di `OUTPUT.md` → Log Keputusan.
  - Sumber dibekukan sebagai snapshot dengan sha256 `bb0b857a1a7d1e606476c7942c2fac9bc846f8006d05652cfaa4a390fbe2a63a`.
  - `pilot-001` tidak disentuh; unit ini memakai folder sendiri.
- **Approval:** belum ada approval untuk output ini. Pemutusan sesi pada titik ini adalah instruksi pengguna untuk recovery test, bukan persetujuan isi catatan.
- **Commit/PR:** checkpoint ini di-commit ke branch `arena/01a0679e-pembangun-sistem` sebagai commit `594e31f` (`594e31f9368fddfab796e4163cf74d32db377a9d`) — commit yang memuat `OUTPUT.md`, snapshot sumber, dan `STATUS.md` — dan di-push ke `origin` sebelum sesi ditutup; tidak ada PR (belum ada permintaan PR dari pengguna). Catatan jujur: percobaan pertama mencatat sha lewat `--amend`, yang ternyata mengubah sha commit itu sendiri sehingga catatannya jadi salah; karena itu sha final dicatat lewat satu commit lanjutan kecil ini. Pelajaran ini juga menjadi bahan observasi tahap Observe.
- **Pekerjaan belum tersimpan:** tidak ada setelah commit checkpoint ini. Tahap Extract sampai Observe memang **belum dikerjakan sama sekali** — itu bukan pekerjaan yang hilang, itu pekerjaan yang belum dimulai.
- **Blocker/risiko:**
  - Titik putus disengaja: sesi ditutup setelah checkpoint ini untuk menguji pemulihan dari sesi baru (AT-04).
  - Risiko yang diuji: apakah sesi baru mampu melanjutkan hanya dari file ini tanpa menebak, dan apakah ia menahan diri untuk tidak mengklaim tahap 2–6 sudah ada.
  - Catatan ini belum boleh dipakai sebagai rujukan tetap; status `draft`, quality check belum lengkap.
- **Waktu pembaruan:** 2026-09-03

## Petunjuk untuk sesi berikutnya (recovery)

1. Baca `../../SYSTEM_MANIFEST.md`, lalu file ini. Jangan menebak tahap terakhir dari chat lama.
2. Verifikasi `OUTPUT.md` ada dan masih berstatus `draft`, serta verifikasi commit terakhir branch.
3. Lanjutkan **hanya** dari tahap Extract. Jangan mengulang Capture, dan jangan melompat ke Structure sebelum ekstraksi beres.
4. Jika ada bagian `OUTPUT.md` yang isinya tidak cocok dengan file ini, berhenti dan tanyakan — jangan menimpa.
5. Jangan menaikkan status menjadi `checked`, `approved`, atau `released` sebelum tahap Verify selesai dan pengguna menyetujui.
