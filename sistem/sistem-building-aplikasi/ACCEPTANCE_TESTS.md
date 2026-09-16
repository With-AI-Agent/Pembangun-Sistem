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

### AT-08 — Copy Folder → Repo Standalone (bukti perilaku, bukan klaim)
- **Tujuan:** membuktikan folder ini benar-benar bisa dipakai sebagai repo aplikasi baru tanpa repo meta — jalur yang ditempuh pemilik.
- **Langkah:** `cp -r` seluruh isi folder ke direktori kosong → `rm _Notes.md` → `git init` + commit → jalankan `python3 _sistem/validate_system.py` (tanpa `tools/` meta) → `find skills -mindepth 1 -maxdepth 1 -type d | wc -l` → cek setiap berkas yang dirujuk prompt entri ada → scan rujukan berprefix (`_sistem/`, `skills/`, `docs/`, `_log-sesi/`, `_salinan-meta/`) yang tidak ada di repo standalone → cek `PROJECT_STATE.md` tidak ada (artinya proyek baru → Tahap 1).
- **Lolos bila:** validator exit 0 di repo standalone; jumlah direktori `skills/` = klaim dokumen; semua berkas yang dirujuk prompt entri ADA; **0 rujukan berprefix yang menggantung**; `tools/` dan `_meta/` memang tidak ada tetapi tidak ada dokumen aktif yang menjadikannya dependensi wajib.

### AT-09 — Tidak Ada Pedoman Usang yang Hidup Tanpa Penanda
- **Tujuan:** mencegah terulangnya cacat K-1 (run klinik ke-2): dokumen yang sudah digantikan tetap hidup dan memberi instruksi yang bertentangan dengan dokumen berlaku — pemilik mengikuti yang lama dan tersesat di pemakaian pertama.
- **Langkah:** `python3 _sistem/validate_system.py` (cek `check_penanda_arsip` + `check_tidak_adaklaim_satu_berkas` + `check_area_luar_tanpa_backtick` + `check_klaim_jumlah_dir_skills` + `check_template_roadmap_7_atribut`), lalu uji mutasi: (a) hapus penanda arsip di `PANDUAN_PEMAKAIAN.md`, (b) ubah klaim jumlah direktori `skills/`, (c) suntik kalimat "yang masuk ke repo hanya AGENT_SYSTEM.md" ke dokumen aktif, (d) suntik rujukan ber-backtick ke berkas di `tools/`, (e) hapus satu atribut task di `_sistem/templates/ROADMAP.md` — tiap mutasi harus membuat validator GAGAL, lalu kembalikan.
- **Lolos bila:** kondisi bersih exit 0 **dan** kelima mutasi terdeteksi (validator GAGAL) — bukti bahwa gerbangnya benar-benar menyala, bukan hijau karena tidak memeriksa apa pun.

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-16 | AT-08 (copy → repo standalone, bukti perilaku) + AT-09 (anti-pedoman-usang-hidup, dengan uji mutasi) ditambahkan; 5 cek baru ditanam di `_sistem/validate_system.py` | Run klinik ke-2: pemilik tersesat oleh `PANDUAN_PEMAKAIAN.md` (arsip tanpa penanda) dan bukti kesiapan sebelumnya struktural saja (pola F-8 — AT dijalankan penulis perubahan). AT-08 memberi bukti perilaku jalur pemakaian nyata; AT-09 + uji mutasi membuat cacat sejenis tidak bisa lolos diam-diam |
| 2026-09-15 | Skrip lahir pada run klinik pertama (kit v0.2.0) — 7 skenario, stdlib-only, tanpa angka volatil | W-06: sistem belum punya QA 3-lapis; AT harus berbasis struktur/exit code, bukan hitung baris |
