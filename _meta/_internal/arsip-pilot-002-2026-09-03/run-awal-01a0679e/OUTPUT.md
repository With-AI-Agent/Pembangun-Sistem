# Catatan Belajar — Protokol Checkpoint & Recovery

- **Status:** `draft`
- **Sumber:** `../../fixtures/SUMBER_CHECKPOINT_RECOVERY.md` (snapshot beku dari `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`)
- **URL/lokasi:** repo `With-AI-Agent/Pembangun-Sistem`, commit `e7ce5e5`
- **Tanggal akses:** 2026-09-03
- **Tujuan belajar:** memahami syarat minimum sebuah checkpoint supaya sesi agent yang benar-benar terputus dapat melanjutkan tanpa menebak, dan menerapkannya pada unit pilot ini.

## Pertanyaan Awal

- Apa yang membuat sebuah checkpoint cukup untuk recovery nyata, dan bukan hanya ringkasan yang nyaman dibaca di chat?
- Kondisi apa yang membuat agent wajib berhenti dan bertanya, bukan melanjutkan?

## Ringkasan

_Belum dikerjakan. Bagian ini hasil tahap Structure (tahap 3)._

## Konsep Inti

_Belum dikerjakan. Bagian ini hasil tahap Structure (tahap 3)._

| Konsep | Penjelasan | Rujukan sumber | Tingkat kepastian |
|---|---|---|---|
| | | | |

## Hubungan Antar Konsep

_Belum dikerjakan. Bagian ini hasil tahap Structure (tahap 3)._

## Hal yang Belum Jelas

_Belum dikerjakan. Bagian ini hasil tahap Verify (tahap 4)._

## Pertanyaan Uji Pemahaman

_Belum dikerjakan. Bagian ini hasil tahap Apply (tahap 5)._

## Langkah Penerapan

_Belum dikerjakan. Bagian ini hasil tahap Apply (tahap 5)._

## Hasil Tahap Capture (tahap 1 — selesai)

### Identitas sumber

| Field | Nilai | Bukti |
|---|---|---|
| Judul | Protokol Checkpoint & Recovery | judul baris 1 sumber |
| Pembuat | meta-sistem ini (dokumen `_meta/`, pemilik keputusan pengguna) | `_meta/SYSTEM_MANIFEST.md` |
| Lokasi asli | `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` | path repo |
| Lokasi snapshot | `sistem-pilot-catatan-belajar/fixtures/SUMBER_CHECKPOINT_RECOVERY.md` | dibuat unit ini |
| sha256 sumber asli | `bb0b857a1a7d1e606476c7942c2fac9bc846f8006d05652cfaa4a390fbe2a63a` | `sha256sum` saat capture |
| Ukuran sumber | 53 baris, 1996 byte | `wc -l -c` saat capture |
| Verifikasi snapshot | baris 10+ snapshot identik byte-per-byte dengan sumber; `diff` kosong, exit 0 | `diff` saat capture |
| Tanggal akses | 2026-09-03 | sesi ini |
| Jenis sumber | dokumen internal repo, bukan sumber publik | sifat repo |

### Tujuan belajar (dirumuskan ulang dari pertanyaan awal)

Memeriksa apakah `STATUS.md` unit pilot sudah memenuhi aturan checkpoint di sumber, dengan menguji unit ini sendiri lewat pemutusan sesi nyata.

### Pertanyaan awal yang akan dijawab tahap berikutnya

1. Apa yang membuat checkpoint cukup untuk recovery nyata, bukan hanya ringkasan chat?
2. Kondisi apa yang mewajibkan agent berhenti dan bertanya?
3. Apa beda "output tersimpan" dengan "output aman untuk sesi berikutnya"?

## Quality Check

- **Level pemeriksaan:** `Ringan` (catatan biasa, sumber internal tidak berisiko; belum ada trigger untuk level Sedang/Mendalam)

- [ ] Klaim penting memiliki rujukan — _belum dapat dinilai; belum ada klaim inti sebelum tahap Structure_
- [ ] Fakta dan inferensi dibedakan — _belum dapat dinilai; tabel konsep belum diisi_
- [x] Ketidakpastian tidak disembunyikan — setiap bagian yang belum dikerjakan ditandai eksplisit, tidak dibiarkan kosong tanpa keterangan
- [ ] Pertanyaan uji dapat dijawab atau diuji — _belum ada; dihasilkan di tahap Apply_
- [ ] Langkah penerapan memiliki bukti keberhasilan — _belum ada; dihasilkan di tahap Apply_

Catatan: checklist ini **sengaja tidak dicentang semua**. Status output tetap `draft`, bukan `checked`, karena hanya 1 dari 6 tahap yang selesai.

## Log Keputusan

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-03 | Bahan belajar unit `pilot-002` = `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`, bukan fixture simulasi lama | Topiknya persis yang sedang diuji (recovery nyata); sumber nyata dan dapat ditelusuri, bukan bahan sintetis |
| 2026-09-03 | Sumber disalin jadi snapshot beku di `fixtures/SUMBER_CHECKPOINT_RECOVERY.md` dengan sha256 tercatat | Menjawab risiko "sumber tidak tercatat sehingga catatan tidak dapat diverifikasi"; ekstraksi tahap berikutnya menunjuk versi yang persis dibaca |
| 2026-09-03 | Unit baru `pilot-002`, `pilot-001` tidak disentuh | Menjaga contoh awal tetap utuh sebagai pembanding, sesuai instruksi pengguna |
| 2026-09-03 | Output berhenti di tahap Capture dan status tetap `draft` | Sengaja, sebagai titik putus untuk recovery test nyata (acceptance test AT-04) |
