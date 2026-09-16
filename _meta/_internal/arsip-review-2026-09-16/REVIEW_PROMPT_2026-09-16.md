> **ARSIP — SUDAH DIGANTIKAN, JANGAN DIPAKAI.** Artefak prompt review independen untuk run reinstall npx (branch arena/01a0a48f, HEAD 6acf7b3). Pin commit/branch di dalamnya **basi sejak saat itu juga** (paradoks yang dikatalogkan sebagai C-07): sumber otoritatif prompt review adalah yang **dibangkitkan saat review dibutuhkan**, bukan berkas yang disimpan — jalankan `python3 tools/review_prompt.py --pr <nomor>` di repo master. Dipindah dari root repo ke sini 2026-09-16 oleh sesi `arena/01a0a7d3-pembangun-sistem` (mandat pemilik: bereskan housekeeping yang tertunda); **isi asli di bawah baris ini tidak disunting sama sekali** (pensiunkan, jangan hapus — Kebijakan Lebur Aturan 2).

---

# Prompt Review Independen — Sistem Building Aplikasi (2026-09-16, 26M 56 dirs)

> Salin SELURUH blok ini ke sesi agent BARU yang independen (bukan sesi ini). Agent baru harus di branch `arena/...` yang terpisah dan tidak boleh push ke branch sesi ini. Hasil review: laporan temuan + saran perbaikan (Critical/Minor) + bukti validator.

```
Kamu adalah reviewer independen untuk repo With-AI-Agent/Pembangun-Sistem, branch arena/01a0a48f-pembangun-sistem, commit HEAD 6acf7b3 (setelah reinstall maksimal via npx).

TUGAS: Lakukan review HIJAU penuh seperti Tahap 6 Cross-Check + audit hidup (AGENT_SYSTEM.md § Mekanisme Hidup), TANPA mengubah file. Laporkan temuan dengan severity.

KONTEKS PENTING (yang sudah diperbaiki sejak review lama a67e5bf):
- Template self-contained: `sistem/sistem-building-aplikasi/` 56 dirs, 26M (naik dari 52 dirs 8.1M) — 10 skill publik sudah reinstall fresh HEAD via npx (bukti hash identik + npx update 24 skills): ios-agent 252K→9.9M full, ui-ux family 9.8M full (ui-ux 3.6M + ui-styling 5.8M + design 348K + design-system 260K + brand 140K + banner 16K + slides 36K), frontend-designer + lite, alibaba 85K, excalidraw 57K, tsbs 60K, ai-agent 17 sub-skills. 2 hub besar tetap katalog 8K on-demand: agent-skills 248 skills (PracticalSwan ff6d12f) & hub 797 skills (8185719) — daftar di skills/agent-skills/CATALOG.md & hub/CATALOG.md, fetch via `npx skills add <repo> --skill <nama>`. Input-Pengguna/ (10 zip 53,813,128 bytes) TIDAK ikut template, tapi semua skill katalog tetap bisa dipakai via npx (dijamin di AGENT_SYSTEM.md § Kewajiban + PANDUAN_PENGGUNA.md + skills/README.md § Update & Discoverability tabel 10 URL publik + npx).
- Dokumen sinkron: AGENT_SYSTEM.md 56 dirs 26M, PANDUAN_PENGGUNA.md 56 dirs 26M, skills/README.md 56 dirs 26M + REINSTALL note + tabel 10 npx.
- Validator harus PASS: `python3 sistem/sistem-building-aplikasi/_sistem/validate_system.py` PASS, `tools/validate_repo.py` + `tools/check_selfcontained.py` bila ada.

LANGKAH REVIEW (wajib berurutan, bukti path):

1. `git log --oneline -10` + `git status` + `git diff main...HEAD --stat` (atau `aad8da6...HEAD` jika main belum merge) — catat file berubah.
2. `ls -1 sistem/sistem-building-aplikasi/skills/ | wc -l` + `du -sh sistem/sistem-building-aplikasi/skills` — harus 56 dirs 26M.
3. `python3 sistem/sistem-building-aplikasi/_sistem/validate_system.py` — harus PASS.
4. `ls sistem/sistem-building-aplikasi/skills/agent-skills/CATALOG.md sistem/sistem-building-aplikasi/skills/agent-skills-hub/CATALOG.md && wc -l` + `head` — verifikasi katalog 248/797 on-demand.
5. `cat sistem/sistem-building-aplikasi/skills/README.md | grep -A2 "REINSTALL\|56 dirs"` + `cat sistem/sistem-building-aplikasi/AGENT_SYSTEM.md | grep -A2 "56 dirs\|katalog"` + `cat sistem/sistem-building-aplikasi/PANDUAN_PENGGUNA.md | grep -A2 "56 dirs\|katalog"` — pastikan jaminan katalog tidak bingung.
6. `cat AUDIT_ZIP_VS_NPX.md | head -30` + `cat AUDIT_NPX_UPDATE.md | head -30` — bukti hash identik + npx update.
7. `ls Input-Pengguna/*.zip 2>&1 | head` — pastikan tidak ikut template (check_selfcontained).
8. Cari inkonsistensi: istilah, referensi PRD/TECH_SPEC tanpa ROADMAP task, Area Berisiko Tanpa task, ambiguitas, gap.

OUTPUT: Laporan markdown dengan tabel temuan (Critical/Minor, file:line, saran), ringkasan validator, dan pernyataan "TEMPLATE SELF-CONTAINED: PASS/FAIL" + "KATALOG ON-DEMAND: TERJAMIN/TIDAK".
```

Simpan laporan sebagai `REVIEW_2026-09-16_INDEPENDEN.md` di root sesi review, dan sebagai komentar PR jika ada PR terbuka.

Bukti yang harus ada di laporan: path file + line + hash `md5sum skills/.../SKILL.md` untuk 3 sample (excalidraw, alibaba, frontend-designer) vs npx.
