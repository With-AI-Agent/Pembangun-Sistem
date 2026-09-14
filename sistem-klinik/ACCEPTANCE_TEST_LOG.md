# Log Bukti Acceptance Test — Sistem Klinik (AT-KL)

> Bukti eksekusi skenario `ACCEPTANCE_TESTS.md`. Bukti memakai struktur (berkas ada/hilang), pola (grep/regex), dan status kembalian alat (exit code) — BUKAN angka yang berubah-ubah (larangan C-04). Eksekusi: 2026-09-14, sesi arena/01a09fd5-pembangun-sistem (Langkah 7 rencana kerangka).

## Metode eksekusi (jujur)

- Uji dijalankan pada **salinan sandbox** `_fixture/sistem-kecil-sakit/` di `/tmp/atkl/` — fixture asli di repo TIDAK diubah agar tetap "sakit" untuk pengujian berikutnya; kit TIDAK pernah masuk git manapun (Kebijakan Lebur aturan 4 dihormati sampai di dalam uji sendiri).
- Target sandbox di-`git init` lokal tanpa remote — langkah "PR target terbuka" dilewati secara sadar (tidak ada remote); padanannya: commit peleburan tercatat lokal. Di run nyata langkah PR berlaku penuh.
- G-Rencana & G-Final run uji: mandat pemilik 14 Sep 2026 (pemilik memilih "Tuntaskan Langkah 7 dulu" — acceptance test pertama adalah isinya).

## AT-KL-01 — Idempotensi dan Penanaman Dasar

### Run 1 (suntik penuh) — LULUS

| Langkah | Hasil |
|---|---|
| Salin kit ke target | `kit/` v0.1.2 di sandbox target |
| Tahap A pendaftaran | kunjungan pertama; konvensi target: README ringkas + python → tanam bentuk sederhana per 04 |
| Tahap B diagnosis | C-05 temuan (checkpoint absen total); C-03/C-02 varian absen (tanpa log/manifest); C-01/C-04/C-06 n/a; kapabilitas: nihil-jujur |
| G-Rencana | mandat pemilik (uji fixture) |
| Tahap C tanam | README di-EXTEND (Prompt Pembuka + STATUS SISTEM + Fakta Platform + Titik Persetujuan + QA); CREATE LOG_SESI.md, SYSTEM_MANIFEST.md (mini + Log Keputusan), REKAM-KLINIK.md (cap v0.1.2); nol overwrite |
| Tahap D verifikasi | `kit/alat/validate_target.py` → `VALIDATION PASSED (TARGET)` exit 0; grep W-01/W-02/W-03(+field deterministik)/W-04/W-05/W-06/W-07/W-08 semua OK; `python3 app.py` exit 0 |
| Tahap E peleburan | `rm -rf kit` + commit — isi target akhir: README.md, LOG_SESI.md, REKAM-KLINIK.md, SYSTEM_MANIFEST.md, app.py (kit hilang; jejak = rekam + cap) |
| Tahap F panen | 1 temuan meta (aturan anti-kit-usang belum tertulis — lihat AT-KL-02); target ini sendiri nihil cacat baru |

### Run 2 (suntik kedua — idempoten) — LULUS

- REKAM-KLINIK dibaca dulu: cap v0.1.2 = kit yang dibawa v0.1.2 → tidak ada tawaran naik versi.
- Diagnosis ulang: detektor exit 0; seluruh mekanisme terverifikasi TERPASANG (verifikasi, bukan tanam ulang).
- Keputusan: rencana kosong; peleburan; **`git commit` menolak: "nothing to commit, working tree clean"** — bukti nol perubahan pada run kedua.

### Run 3 (detektor merah) — LULUS

- Field STATUS di README target disuntik `rusak` secara paksa.
- `validate_target.py` → `VALIDATION FAILED (TARGET): W-03: Field STATUS menunjukkan 'rusak'`, **exit 1**.
- (Konteks: kondisi "STATUS absen total" juga teruji merah exit 1 saat pre-audit di fixture asli, 14 Sep.)

## AT-KL-02 — Cek Kit Basi (Fail-Closed)

- **Temuan awal (pre-audit statis, 14 Sep):** ekspektasi skenario (agent menolak bekerja dengan kit usang) BELUM tertulis di aturan — 01 §1.3 + Tahap A.4 hanya mengatur arah cap < kit (tawaran naik versi). Ini cacat aturan sungguhan yang ditangkap acceptance test.
- **Perbaikan:** kalimat anti-kit-usang ditambahkan ke 01 §1.3 + Tahap A.4 (kit lebih tua dari cap → BERHENTI fail-closed, wajib sinkron dulu, dicatat di rekam); kit distamping ulang, versi 0.1.1 → 0.1.2; Log Keputusan 01 + manifest menerima baris perubahan ini.
- **Eksekusi ulang pasca-perbaikan — LULUS:** target dengan rekam cap v0.1.2 + kit palsu ber-stamp versi-kit 0.1.1 → stamp vs cap terdeteksi (0.1.1 < 0.1.2) → aturan 1.3 memicu: Tahap B ditolak, tuntutan sinkron kit dulu, nol byte ditulis ke target (bukti: `git status` target hanya menampilkan folder kit yang tak pernah masuk git).

## Verifikasi struktural sistem (bukan AT-KL, tapi satu baris per perubahan)

- `python3 _sistem/validate_system.py` → PASS (setelah START_DI_SINI didaftarkan ke REQUIRED).
- `python3 tools/validate_repo.py` → PASS 0 warning (88 dokumen aktif, 297 rujukan, 0 unresolved).
- `python3 tools/check_selfcontained.py --sistem sistem-klinik --report` → PASS exit 0.

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-14 | Bukti pertama AT-KL-01 (3 run) + AT-KL-02 dicatat; metode sandbox didokumentasikan | Langkah 7 rencana: acceptance test pertama di fixture (suntik-2x idempoten) — syarat sebelum run nyata sah |
| 2026-09-14 | AT-KL-02 menangkap cacat aturan → diperbaiki 01 §1.3/Tahap A.4 + kit v0.1.2 | Bukti bahwa katalog+uji bekerja: uji menemukan yang belum dipenuhi aturan, aturan diperbaiki, uji ulang lulus |
