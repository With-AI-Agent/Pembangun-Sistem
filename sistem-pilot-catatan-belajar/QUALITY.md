# Quality Assurance — Pilot Catatan Belajar

## Batasan Platform

Dipakai via lmarena? Ya — rujuk `_meta/PLATFORM_LMARENA.md`. Fakta: branch arena otomatis, tidak bisa push setelah merge, sesi bisa crash. Karena itu checkpoint tiap tahap + checkpoint diskusi ringan wajib untuk mencegah FI-03.

## Lapisan sistem

Audit sistem dipicu oleh kegagalan berulang, perubahan workflow, atau hasil pilot yang tidak dapat diverifikasi. Proposal perubahan wajib menjelaskan masalah, bukti, trade-off, regression check, versi, dan rollback.

## Level pemeriksaan

- **Ringan:** struktur template, sumber, status, dan quality checklist untuk catatan biasa.
- **Sedang:** cross-check semua klaim inti dan review pengguna jika catatan dipakai berulang.
- **Mendalam:** audit sumber, asumsi, failure mode, regression, dan rollback jika output berisiko atau workflow berubah.

Jangan menjalankan audit mendalam pada setiap catatan tanpa trigger. Catat level yang dipakai di STATUS.

## Lapisan output

Sebelum catatan berstatus `released`, agent memeriksa:

- level pemeriksaan sudah dipilih dan dicatat;
- sumber dan tanggal akses tersedia;
- klaim penting dapat ditelusuri;
- fakta, inferensi, dan ketidakpastian dipisahkan;
- ringkasan tidak melampaui sumber;
- pertanyaan uji dan tindakan memiliki kriteria keberhasilan;
- pengguna menyetujui output jika akan dipakai sebagai rujukan tetap.

## Lapisan observasi

Setelah digunakan, catat:

- kesalahan factual atau interpretasi;
- bagian yang tidak membantu;
- langkah yang terlalu berat;
- apakah perubahan hanya insight lokal atau perubahan workflow.

## Log evolusi

| Tanggal | Lapisan | Observasi | Perubahan | Alasan | Bukti | Versi | Approval | Rollback |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
