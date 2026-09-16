> **ARSIP — SUDAH DIGANTIKAN, JANGAN DIPAKAI.** Artefak prompt delta review untuk HEAD 593ba79 (verifikasi 5 Critical fix) di branch yang sama. Pin commit/branch di dalamnya **basi sejak saat itu juga** (paradoks yang dikatalogkan sebagai C-07): sumber otoritatif prompt review adalah yang **dibangkitkan saat review dibutuhkan**, bukan berkas yang disimpan — jalankan `python3 tools/review_prompt.py --pr <nomor>` di repo master. Dipindah dari root repo ke sini 2026-09-16 oleh sesi `arena/01a0a7d3-pembangun-sistem` (mandat pemilik: bereskan housekeeping yang tertunda); **isi asli di bawah baris ini tidak disunting sama sekali** (pensiunkan, jangan hapus — Kebijakan Lebur Aturan 2).

---

# Prompt Delta Review — 593ba79 (5 Critical fix verification)

> Paste SELURUH blok ini ke sesi reviewer independen yang sama (branch arena/01a0a797). Cukup verifikasi delta, tidak perlu full 8 langkah.

```
Kamu adalah reviewer independen delta untuk branch arena/01a0a48f-pembangun-sistem, HEAD baru 593ba79 (perbaikan 5 Critical dari review 44cfd3a).

TUGAS DELTA (5-10 menit): Verifikasi bahwa 5 Critical di REVIEW_2026-09-16_INDEPENDEN.md sudah RESOLVED di 593ba79. Tidak perlu ubah file.

LANGKAH DELTA:
1. git fetch origin arena/01a0a48f-pembangun-sistem && git show origin/arena/01a0a48f-pembangun-sistem:REVIEW_2026-09-16_INDEPENDEN.md | head -5 (pastikan target)
   git diff aad8da6..593ba79 --stat | head -20
2. C-01: grep -n "artefak fondasi selain.*README.md" sistem/sistem-building-aplikasi/AGENT_SYSTEM.md — harus ada, bukan "/docs sudah berisi file apa pun"
3. C-02: head -10 sistem/sistem-building-aplikasi/_log-sesi/LOG_SESI_2026-09-15.md | grep -E "CLOSED.*ARSIP TEMPLATE" — harus CLOSED bukan OPEN, ada catatan "abaikan di repo baru"
4. C-03: grep -n "Catatan path.*find skills" sistem/sistem-building-aplikasi/AGENT_SYSTEM.md — harus ada resolver note
5. C-04: grep -A2 "Update.*PROJECT_STATE.*STATUS.md.*LOG_SESI" sistem/sistem-building-aplikasi/AGENT_SYSTEM.md | grep -E "semua state dulu|commit.*push sekali" — urutan harus state dulu baru push
6. C-05: grep -n "bila di repo meta.*tools/validate" sistem/sistem-building-aplikasi/AGENT_SYSTEM.md — harus ada fallback standalone
7. M-02/M-04/M-09: grep -E "787 installable|9 skill installable.*1 katalog|17 skills valid" sistem/sistem-building-aplikasi/skills/README.md; grep "787 installable" sistem/sistem-building-aplikasi/skills/agent-skills-hub/CATALOG.md; python3 tools/validate_repo.py 2>&1 | tail -5 (harus 0 unresolved), python3 tools/check_selfcontained.py --sistem sistem/sistem-building-aplikasi --report 2>&1 | grep -E "PASS|FAIL"

OUTPUT DELTA: Tabel 5 baris C-01..C-05 RESOLVED/BELUM + 3 validator (validate_repo 0 warning, check_selfcontained PASS, FI 72) + pernyataan "DELTA REVIEW: HIJAU — siap merge" atau "BELUM".
Simpan sebagai REVIEW_DELTA_593ba79.md dan komentar PR #59.
```

Target HEAD: 593ba7944c3f857fda9ebb82c3c725aa70e2a6f1
Base: aad8da6
