# Workflow — Pilot Catatan Belajar

## Batasan Platform lmarena (fakta, bukan aturan kita)

Sistem ini dipakai via lmarena Agent Mode. Rujuk `_meta/PLATFORM_LMARENA.md` untuk detail:
- Branch `arena/...` dibuat otomatis oleh platform — verifikasi via `git branch --show-current`
- Setelah PR merge/close, sesi **tidak bisa** push lagi (platform cabut akses) — file baru akan terjebak
- Sesi bisa crash kapan saja — diskusi panjang yang belum jadi file bisa hilang

Implikasi: commit tiap tahap + checkpoint diskusi ringan jika diskusi >5 giliran mendekati keputusan.

## Aturan umum

- Satu unit kerja memproses satu bahan atau satu pertanyaan utama.
- Sumber wajib dicatat sebelum ekstraksi.
- Bedakan fakta sumber, interpretasi, dan pertanyaan terbuka.
- Setiap tahap menghasilkan bagian atau file yang dapat dirujuk tahap berikutnya.
- Jangan menyatakan output selesai sebelum status dan quality check diperbarui.
- Jika diskusi >5-7 giliran mendekati keputusan, buat `DISKUSI_MENTAH_*.md` dan commit (alasan kausal: sesi bisa crash — fakta platform).

## Tahap

### 1. Capture

Catat judul, penulis/pembuat, URL atau lokasi sumber, tanggal akses, dan tujuan belajar.

Output: identitas sumber dan pertanyaan awal.

### 2. Extract

Ambil ide, fakta, definisi, dan contoh penting. Jangan menambahkan klaim yang tidak ada di sumber tanpa label.

Output: daftar ekstraksi dengan rujukan sumber.

### 3. Structure

Susun ekstraksi menjadi ringkasan, konsep inti, hubungan antar konsep, dan istilah yang belum dipahami.

Output: draft catatan berdasarkan `OUTPUT_TEMPLATE.md`.

### 4. Verify

Periksa apakah setiap klaim penting memiliki sumber, apakah inferensi diberi label, dan apakah ada konflik atau ketidakpastian.

Output: catatan berstatus `checked` atau daftar blocker.

### 5. Apply

Turunkan 1–3 pertanyaan uji pemahaman dan langkah penerapan yang realistis. Jangan menyamakan aktivitas dengan bukti paham.

Output: pertanyaan dan tindakan.

### 6. Observe

Setelah digunakan, catat apa yang terbukti berguna, apa yang salah, dan apakah workflow perlu diubah. Perubahan workflow masuk ke jalur proposal dan approval, bukan edit diam-diam.

Output: observasi dan usulan evolusi.
