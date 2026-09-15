# Acceptance Test Log — Sistem Building Aplikasi

> Bukti eksekusi skenario ACCEPTANCE_TESTS.md — dicatat per run. Angka stabil dikutip, rujukan volatil tidak dikutip.

## Run 2026-09-15 — Run Klinik Pertama (kit v0.2.0, panggung rawat inap)

- **Tanggal:** 2026-09-15
- **Pelaksana:** agent sesi arena/01a0a48f-pembangun-sistem (run klinik pertama, rawat inap)
- **Kit:** v0.2.0 (master in-place, rawat inap — tanpa salin kit)
- **Target:** sistem/sistem-building-aplikasi (rename SISTEM-BUILDING-APLIKASI → sistem-building-aplikasi)

### Hasil Skenario

| Skenario | Hasil | Bukti |
|---|---|---|
| AT-01 Entry Point | PASS | PROMPT_ENTRI_UNIVERSAL.md + PANDUAN_PENGGUNA.md blok identik (validator pegangan PASS) |
| AT-02 Checkpoint | PASS | STATUS.md field Pekerjaan belum tersimpan: Tidak ada tepat 1x, Waktu pembaruan: 2026-09-15 — Verifikasi D lulus + REKAM-KLINIK cap v0.2.0 + Panen nihil; validate_system.py PASS |
| AT-03 Log Sesi | PASS | _log-sesi/LOG_SESI_2026-09-15.md CLOSED; 10_LOG_SESI.md ada |
| AT-04 Pegangan Identik | PASS | diff blok PANDUAN vs PROMPT = identik (validator pegangan PASS) |
| AT-05 Self-Containment | PASS | tools/check_selfcontained.py --sistem sistem-building-aplikasi --report PASS (1 salinan berlabel, 0 temuan) |
| AT-06 Fondasi Gerbang | PASS | AGENT_SYSTEM.md §Tahap 1-6 menunggu "cukup, tulis draftnya" — agen tidak menulis tanpa approval |
| AT-07 DECISIONS_LOG | PASS | AGENT_SYSTEM.md §DECISIONS_LOG mewajibkan baca + STOP bila ubah Area Berisiko Tinggi |

### Verifikasi Alat (Tahap D)

- _sistem/validate_system.py: PASS
- tools/validate_repo.py: PASS 0 warning (99 docs/308 refs/4 sistem)
- tools/check_selfcontained.py --semua: PASS (4 sistem)
- tools/test_failure_injection.py: PASS 71 skenario (15 sintetis + 12 unit nyata + 14 PR-11 + 10 check_selfcontained + 20 review_prompt)
- tools/backup_verify.py: PASS (backup 36 files, restore OK)
- tools/build_template.py: PASS (smoke extract + template clean)

### Catatan

Run ini adalah run pertama Klinik (pola F-8) — AT dijalankan penulis perubahan; verifikasi pihak kedua = review independen PR ini + run berikutnya. Panen F = nihil (tidak ada cacat baru di luar C-01…C-06).
