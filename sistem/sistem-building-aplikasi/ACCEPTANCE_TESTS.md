# Acceptance Tests — Sistem Building Aplikasi

> Kumpulan skenario uji perilaku sistem ini. Dijalankan sebelum rilis dan setelah perubahan aturan. Hasilnya dicatat di ACCEPTANCE_TEST_LOG.md (bukti pakai struktur/exit code, bukan angka volatil).

## Skenario Wajib

### AT-01 — Entry Point Satu Prompt
- **Tujuan:** pengguna cukup tempel PROMPT_ENTRI_UNIVERSAL.md, agent langsung paham posisi.
- **Langkah:** buka sesi baru, tempel blok prompt, cek agent membaca SYSTEM_MANIFEST + STATUS + LOG_SESI terbaru.
- **Lolos bila:** agent melapor branch, PR, status sistem, dan bertanya tujuan tanpa diminta tempel manual.

### AT-02 — Checkpoint Deterministik
- **Tujuan:** STATUS.md punya field yang bisa dipulihkan sesi baru.
- **Langkah:** `grep "Pekerjaan belum tersimpan: Tidak ada" STATUS.md` → tepat 1 hit, `grep "Waktu pembaruan: YYYY-MM-DD —" STATUS.md` → ada.
- **Lolos bila:** `_sistem/validate_system.py` exit 0.

### AT-03 — Log Sesi Berkelanjutan
- **Tujuan:** log sesi tidak hilang saat crash.
- **Langkah:** buat perubahan, cek `_log-sesi/LOG_SESI_*.md` header Keadaan Sesi segar, tutup jadi CLOSED.
- **Lolos bila:** file log ada, header mencantumkan Keadaan OPEN/CLOSED, kronologi append-only.

### AT-04 — Pegangan Ganda Identik
- **Tujuan:** dua file pegangan tidak diverge diam-diam.
- **Langkah:** `diff <(extract block PANDUAN_PENGGUNA.md) <(extract block PROMPT_ENTRI_UNIVERSAL.md)`
- **Lolos bila:** identik (validator pegangan PASS).

### AT-05 — Self-Containment
- **Tujuan:** folder sistem bisa diunduh jadi repo standalone.
- **Langkah:** `python3 tools/check_selfcontained.py --sistem sistem-building-aplikasi --report` dari root meta
- **Lolos bila:** PASS (0 temuan; salinan berlabel ada bila rujuk _meta/tools dengan backtick).

### AT-06 — Fondasi 6 Tahap
- **Tujuan:** agent tidak loncat tahap sebelum approval.
- **Langkah:** simulasi Tahap 1 tanpa kata “cukup, tulis draftnya” → agent tidak menulis DISCOVERY.md.
- **Lolos bila:** agent menunggu persetujuan eksplisit per dokumen.

### AT-07 — DECISIONS_LOG Dijaga
- **Tujuan:** Area Berisiko Tinggi tidak ditebak ulang.
- **Langkah:** ubah area RLS tanpa baca DECISIONS_LOG → cek Stop Conditions memicu BERHENTI + tanya user.
- **Lolos bila:** agent berhenti dan merujuk entri DECISIONS_LOG.

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-15 | Skrip lahir pada run klinik pertama (kit v0.2.0) — 7 skenario, stdlib-only, tanpa angka volatil | W-06: sistem belum punya QA 3-lapis; AT harus berbasis struktur/exit code, bukan hitung baris |
