# RINGKASAN — Sistem Building Aplikasi (sinkron 2026-09-15, 8.1M)

> Ringkasan untuk Claude chat biasa (cadangan lmarena). Dibuat pada run klinik pertama 2026-09-15 (kit v0.2.0, rawat inap) + disinkron 2026-09-15 susulan maksimal adaptif (8.1M). Sinkron dengan SYSTEM_MANIFEST.md v0.1.0 + skills 8.1M.

## Identitas
- **Nama:** Sistem Building Aplikasi (Sistem Fondasi Aplikasi)
- **Tujuan:** membangun aplikasi untuk pemilik non-teknis via Fondasi 6 dokumen (Discovery→PRD→Tech Spec→Agent Guide→Roadmap→Cross-Check) + Coding task-ROADMAP, dijalankan AI Agent
- **Pemilik:** pengguna repo
- **Versi:** 0.1.0 — Tahap siap-pakai
- **Folder:** `sistem/sistem-building-aplikasi/` (rename dari SISTEM-BUILDING-APLIKASI pada 2026-09-15)
- **Entry point:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` (identik) → `START_DI_SINI.md` (5 jenis sesi) → `AGENT_SYSTEM.md` + `SYSTEM_MANIFEST.md` + `STATUS.md` + `LOG_SESI`

## Struktur (matang, self-contained)
- `AGENT_SYSTEM.md` — 33K, aturan kerja agent: LANGKAH PERTAMA (PROJECT_STATE) + Kewajiban Skill ADAPTIF (52 dirs 8.1M, Prinsip Adaptif, tabel 15 baris Cloudflare/Supabase/Google) + 6 Tahap Fondasi detail + Tahap 0.5 Siklus Baru + Prosedur Coding (assess→validasi→eksekusi) + Checkpoint & Handoff 6 audit + Stop Conditions + "terserah" handler
- `SYSTEM_MANIFEST.md` — 17K, manifest + warisan W-01…W-09 semua diterapkan + Dependency 8.1M + Quality 3-lapis + Batasan Platform lmarena
- `STATUS.md` — checkpoint deterministik (`Pekerjaan belum tersimpan: Tidak ada` exact 1x, `Waktu pembaruan: YYYY-MM-DD —`)
- `PANDUAN_PENGGUNA.md` (132 baris) + `PROMPT_ENTRI_UNIVERSAL.md` (25 baris) — pegangan 2-file identik (W-01), prompt pembuka/penutup, istilah awam, kalimat pembuka 5 situasi
- `START_DI_SINI.md` — navigasi per jenis sesi (Fondasi 1-6, Coding, Siklus Baru, Audit, Checkpoint)
- `10_LOG_SESI.md` — aturan log berkelanjutan self-contained (W-02) — header Keadaan Sesi segar, append-only, CLOSED di akhir
- `_log-sesi/LOG_SESI_2026-09-15.md` — log run pertama + susulan K-10 + Vercel + maksimal + Cloudflare/Supabase/Google adaptif
- `ACCEPTANCE_TESTS.md` (7 skenario AT-01…AT-07) + `ACCEPTANCE_TEST_LOG.md` + `_sistem/validate_system.py` (stdlib, 8 required files, status fields, manifest W, pegangan) — QA 3-lapis (W-06)
- `_sistem/02_TAWARAN_KAPABILITAS_PLUS_AUDIT.md` — audit 10 zip + tawaran 7 kolom + riset 5 sumber
- `_sistem/03_AUDIT_VERCEL_SKILLS.md` — audit 26 Vercel 9 kategori + bukti fetch
- `_sistem/templates/` — starter templates 7 file: DISCOVERY, PRD, TECH_SPEC, AGENT_OPERATING_GUIDE, ROADMAP, DECISIONS_LOG, PROJECT_STATE
- `docs/README.md` — placeholder /docs (akan diisi 6 dokumen Fondasi saat build app pertama)
- `_salinan-meta/PLATFORM_LMARENA.md` — salinan berlabel fakta platform lmarena (W-07)
- `skills/` — 8.1M, 52 dirs, vendor-local (lihat skills/README.md): frontend-designer, excalidraw, ui-ux-pro-max, Vercel 16, supabase 2, cloudflare 3, gmail/google 7, product-management/discovery, security/QA, etc. Hemat 85% vs 53,813,128 bytes (~51.3 MiB) penuh bila unzip semua. Wajib pakai ADAPTIF.
- `_Notes.md` — link chat Claude: https://claude.ai/chat/c2d459f8-4adc-48e3-a37d-6cbee248e6d3

## Bentuk & Warisan (semua tertanam matang)
- **Bentuk:** Gabungan (Bertingkat Fondasi 1-6 + Siklus Coding + Gabungan Siklus Baru)
- **Unit:** 1 aplikasi = 1 siklus Fondasi (/docs 6) + Coding ROADMAP (task atomik)
- **Approval:** Besar (G-Fondasi per dokumen, DECISIONS_LOG, Area Berisiko, G-Final, siklus baru) vs Kecil (typo, folder, STATUS/LOG, commit, handoff) — dikunci di manifest + AGENT_SYSTEM
- **Warisan W-01…W-09 semua diterapkan:**
  - W-01 pegangan → PANDUAN_PENGGUNA + PROMPT_ENTRI_UNIVERSAL (identik, validator pegangan PASS)
  - W-02 LOG_SESI → 10_LOG_SESI + _log-sesi (header Keadaan Sesi, append-only, backstop STATUS+PROJECT_STATE)
  - W-03 STATUS → STATUS.md field deterministik exact + TEMPLATE di _sistem/templates/PROJECT_STATE.md
  - W-04 manifest → SYSTEM_MANIFEST ini
  - W-05 log keputusan → Log Keputusan di manifest + tiap /docs + DECISIONS_LOG template + Aturan Mengikat DECISIONS_LOG di AGENT_SYSTEM
  - W-06 QA 3-lapis → ACCEPTANCE_TESTS 7 skenario + validate_system.py (stdlib) + check_selfcontained + validate_repo + FI 72 (15+13+14+10+20)
  - W-07 fakta platform → PANDUAN_PENGGUNA + Batasan Platform + _salinan-meta/PLATFORM_LMARENA.md
  - W-08 approval bertingkat → Bentuk Sistem + AGENT_SYSTEM Stop Conditions
  - W-09 ringkasan cadangan → file ini (sinkron 2026-09-15, 8.1M)
- **Mekanisme inti tertanam (beyond W):**
  - PROJECT_STATE (STATUS/DETAIL/UPDATE TERAKHIR) — format + lifecycle LANGKAH PERTAMA & TERAKHIR di AGENT_SYSTEM, template di _sistem/templates/
  - DECISIONS_LOG (Area Berisiko Tinggi) — 3 aturan mengikat + format entri + wajib baca sebelum ubah + wajib stop sebelum ganti + wajib tulis setelah putusan
  - ROADMAP (task atomik, ref PRD/TECH_SPEC, ⚠️ DECISIONS_LOG) — Tahap 5 + Coding Procedure
  - Checkpoint & Handoff (6 audit jujur: ROADMAP, DECISIONS_LOG, konsistensi, repo, PROJECT_STATE, ringkasan)
  - Branch & commit (deskriptif, tiap sesi = branch baru, push bukan main, merge manual)
  - Stop Conditions (5 kondisi wajib berhenti) + "terserah" handler (rekomendasi + catat resmi)
  - Self-contained (folder diunduh standalone tetap jalan — validator salinan berlabel, provenance tanpa backtick)
  - Kewajiban Skill ADAPTIF (Wajib + Prinsip Adaptif — analisa task → pilih skill tepat Cloudflare vs Vercel vs Supabase vs Google, tabel 15 baris, find-skills discovery)
- **Fakta platform lmarena:** branch arena otomatis, push dicabut setelah merge/close, sesi bisa crash kapan saja, agent baru buta tanpa commit+push+LOG_SESI — mitigasi checkpoint tiap tahap + LOG_SESI berkelanjutan

## Kapabilitas Terpasang (maksimal 8.1M)
- **Batch K-10 zip (10 zip 53,813,128 bytes):** frontend-designer 24K, excalidraw 57K, ui-ux-pro-max selective 1.7M (2.1M)
- **Vercel 16 (26 audit):** react-best-practices 416K (70 rules), composition 80K, web-design 4K (100+ a11y), building-components 152K, next-best 124K, cache 12K, upgrade 4K, ai-sdk 8K, agent-browser 4K, vercel-deploy 48K, react-native 260K, ai-elements 1016K, streamdown 68K, ucp 84K, workflow 32K, find-skills 8K (1.5M)
- **Sisa zip 7:** alibaba-java 44K, ai-agent-skills 256K (18), ios-agent 252K, tsbs 28K, awesome 224K, agent-skills catalog 10K (248 skills), hub catalog 8.5K (42k files)
- **Rancangan:** product-management 360K (8), product-discovery 204K (7), prd-taskmaster 76K, brainstorming 92K
- **QA:** security-review, tdd-workflow, verification-loop, superpowers 5 (tdd, debugging, writing-plans, verification)
- **Cloudflare/Supabase/Google (baru):** cloudflare 1.5M (60+ refs Workers/Pages/D1/R2/KV), wrangler 8K, agents-sdk 92K, supabase 32K, supabase-postgres 156K (8 kategori), gmail 49K, drive 45K, sheets 45K, calendar 53K, docs 37K, chat 61K, slides 41K

## Status Saat Ini (matang)
- **2026-09-15:** run klinik pertama C (rename + manifest + pegangan + log + QA + salinan meta) + Verifikasi D + Catatan E + Panen F (validator hijau) + G-Rencana 1-9 disetujui + susulan K-10 (3 skill inti, 2.1M) + susulan Vercel 10 inti (852K) + susulan maksimal semua sisa (6 Vercel niche +7 zip + planning + QA →6.0M) + susulan Cloudflare/Supabase/Google adaptif (12 skill →8.1M). Semua validator PASS (validate_system, validate_repo 102 dokumen/324 refs, check_selfcontained --semua PASS 4 sistem, FI 72). PR #59 OPEN di arena/01a0a48f-pembangun-sistem menunggu G-Final merge pemilik. /docs masih kosong — Tahap 1 Discovery siap kapan saja. _cadangan ini sinkron 2026-09-15.

## Ke Mana Hasil Dibawa
- Hasil kerja Fondasi → `/docs/*.md` + `PROJECT_STATE.md` di repo aplikasi target
- Hasil Coding → kode aplikasi di repo target
- Semua via branch `tahap-*/fase-*` → PR tanpa auto-merge → merge pemilik (jangan push ke main)
