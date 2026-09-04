# Catatan Belajar — Protokol Checkpoint & Recovery Meta-Sistem

- **Status:** `observed` (checked → ready-for-review → observed, menunggu approval pengguna untuk released)
- **Sumber:** `../../fixtures/SUMBER_NYATA_PILOT_002.md` (yang merujuk ke `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` dan `_meta/02_PRINSIP_UNIVERSAL.md`)
- **URL/lokasi:** `sistem-pilot-catatan-belajar/fixtures/SUMBER_NYATA_PILOT_002.md` + `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`
- **Tanggal akses:** 2026-09-04
- **Tujuan belajar:** Menguji apakah protokol checkpoint & recovery cukup jelas untuk dijalankan sebagai behavioral pilot dan recovery test nyata, serta memahami gap yang menyebabkan gate rilis belum centang

## Pertanyaan Awal

- Bagaimana memastikan sesi agent yang terputus di tengah jalan bisa dilanjutkan tanpa menebak tahap terakhir?
- Apa perbedaan antara "output ada di workspace" vs "output aman untuk sesi baru"?
- Kapan checkpoint harus di-commit dan kapan cukup di workspace?
- Bagaimana protokol ini menangani konflik antar branch?

## Ringkasan

Checkpoint adalah catatan persisten (STATUS.md) yang memungkinkan sesi baru melanjutkan tanpa mengandalkan ingatan chat. Protokol mewajibkan: baca sumber resmi dulu, simpan output ke path resmi, baru update STATUS, lalu commit+push jika output jadi dependency tahap berikutnya. Recovery mewajibkan baca manifest, STATUS, verifikasi file output dan commit, verifikasi branch/PR, jangan ulang tahap yang sudah approved/merged, dan berhenti jika ambigu.

## Konsep Inti

| Konsep | Penjelasan | Rujukan sumber | Tingkat kepastian |
|---|---|---|---|
| Checkpoint persisten | Catatan STATUS.md yang menyimpan tahap terakhir, output resmi, konteks dibaca, approval, commit/PR, pekerjaan belum tersimpan | PROTOKOL_CHECKPOINT_RECOVERY.md, Format checkpoint | fakta |
| Aturan commit sebelum lanjut | Output yang jadi dependency tahap berikutnya wajib di-commit dan push sebelum dinyatakan tersedia untuk sesi baru | PROTOKOL_CHECKPOINT_RECOVERY.md, Aturan 4 | fakta |
| Fail-closed | Jika STATUS hilang atau OUTPUT hilang, state dianggap tidak aman, agent tidak boleh lanjut otomatis | FAILURE_INJECTION_TESTS.md FI-01, FI-02 + BEHAVIORAL_AUDIT | fakta |
| Workspace vs aman | Output yang hanya di workspace belum aman untuk sesi baru | PROTOKOL_CHECKPOINT_RECOVERY.md Aturan 5 + HANDOFF | fakta |
| Recovery 6 langkah | Baca manifest, baca STATUS, verifikasi output & commit, verifikasi branch/PR, jangan ulang approved, berhenti jika ambigu | PROTOKOL_CHECKPOINT_RECOVERY.md Recovery | fakta |
| Checkpoint otomatis vs manual | Otomatis tiap pindah tahap besar (baca ulang sumber resmi), manual bisa dipanggil kapan saja oleh pengguna | 02_PRINSIP_UNIVERSAL.md Prinsip 4 | fakta |
| Kondisional | Checkpoint relevan untuk sesi panjang/berlapis; sistem sederhana boleh disederhanakan | 02_PRINSIP_UNIVERSAL.md Syarat berlaku | fakta |
| Konflik | Jangan timpa tanpa tunjukkan konflik, identifikasi file/branch/keputusan bertabrakan, pisahkan tujuan, minta approval ulang jika Besar | PROTOKOL_CHECKPOINT_RECOVERY.md Recovery konflik | fakta |
| Observasi pilot sebelumnya | Pilot-001 lulus struktural tapi belum diuji pengguna nyata dan belum diuji recovery nyata | HANDOFF_NEXT_SESSION.md + PILOT_REPORT + BEHAVIORAL_AUDIT | fakta |
| Gate rilis yang belum | Behavioral audit nyata, recovery test nyata, pilot disetujui user, backup, template bersih belum | SYSTEM_MANIFEST.md Gate Rilis Master | fakta |
| Interpretasi risiko birokrasi | Quality protocol 3 lapisan lengkap tapi berisiko menambah beban jika dipakai tanpa level | BEHAVIORAL_AUDIT B-04 | inferensi |
| Interpretasi kebutuhan pilot-002 | Pilot nyata harus pakai sumber nyata, level Sedang, dan sengaja diinterupsi untuk bukti recovery | HANDOFF langkah 4-6 + analisis | inferensi |

## Hubungan Antar Konsep

- Checkpoint persisten → memungkinkan fail-closed check → memungkinkan recovery 6 langkah
- Aturan commit sebelum lanjut → membedakan workspace vs aman → mencegah FI-03
- Checkpoint otomatis + manual → mitigasi risiko agent kehilangan jejak di sesi panjang (Prinsip 4)
- Kondisional → mencegah birokrasi berlebihan (terkait B-04)
- Konflik handling → terkait FI-04 dan FI-05

## Hal yang Belum Jelas

- Apakah format STATUS_TEMPLATE saat ini cukup untuk mencatat "sumber konteks yang dibaca" secara deterministik? (B-02 bilang perlu dicatat eksplisit)
- Apakah level pemeriksaan Ringan/Sedang/Mendalam sudah cukup operasional untuk pilot catatan belajar? (B-04)
- Bagaimana mengukur "aman untuk sesi baru" secara otomatis selain manual check file ada?

## Pertanyaan Uji Pemahaman

1. Jika STATUS.md menyatakan `released` tapi OUTPUT.md tidak ada, apa yang harus dilakukan agent menurut protokol? (Jawaban: state tidak valid, tidak boleh lanjut, laporkan blocker — FI-02)
2. Tunjukkan perbedaan antara checkpoint otomatis dan perintah manual verifikasi, dan kapan masing-masing dipakai.
3. Rancang satu skenario di mana agent harus berhenti dan bertanya karena status ambigu, bukan menebak.

## Langkah Penerapan

- **Tindakan:** Jalankan pilot-002 ini sampai Observe, dengan simulasi interupsi di tiap tahap, dan catat apakah STATUS.md berhasil memulihkan konteks tanpa menebak.
- **Kapan:** Sesi ini (2026-09-04), branch `arena/01a06bce-pembangun-sistem`
- **Bukti berhasil:** 
  - Setiap tahap memiliki commit terpisah
  - Simulasi FI-01 s/d FI-04 menghasilkan fail-closed (state_is_safe = False)
  - STATUS.md setelah recovery berisi sumber konteks yang dibaca + alasan
  - Laporan behavioral audit baru bisa dibuat

## Quality Check

- **Level pemeriksaan:** Sedang

- [x] Klaim penting memiliki rujukan (semua baris di tabel konsep punya rujukan sumber)
- [x] Fakta dan inferensi dibedakan (kolom tingkat kepastian)
- [x] Ketidakpastian tidak disembunyikan (bagian Hal yang Belum Jelas)
- [x] Pertanyaan uji dapat dijawab atau diuji (3 pertanyaan di atas)
- [x] Langkah penerapan memiliki bukti keberhasilan (commit + fail-closed test)

## Log Keputusan

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-04 | Pilih sumber nyata dari dokumen meta sendiri | Agar pilot menguji protokol yang akan dipakai untuk rilis meta, bukan topik random |
| 2026-09-04 | Level Sedang, bukan Ringan | Pilot-001 sudah Ringan; pilot-002 perlu cross-check dan review pengguna |
| 2026-09-04 | Rencana recovery test FI-01 s/d FI-04 di STATUS | Menutup B-03 yang belum diuji failure injection nyata |
