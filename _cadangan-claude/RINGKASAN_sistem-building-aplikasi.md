# RINGKASAN — Sistem Building Aplikasi

> Ringkasan untuk Claude chat biasa (cadangan lmarena). Dibuat pada run klinik pertama 2026-09-15 (kit v0.2.0, rawat inap). Sinkron dengan SYSTEM_MANIFEST.md v0.1.0.

## Identitas
- **Nama:** Sistem Building Aplikasi (Sistem Fondasi Aplikasi)
- **Tujuan:** membangun aplikasi untuk pemilik non-teknis via Fondasi 6 dokumen + Coding task-ROADMAP, dijalankan AI Agent
- **Pemilik:** pengguna repo
- **Versi:** 0.1.0 — Tahap siap-pakai
- **Folder:** `sistem/sistem-building-aplikasi/` (rename dari SISTEM-BUILDING-APLIKASI pada 2026-09-15)
- **Entry point:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` → `START_DI_SINI.md` → `AGENT_SYSTEM.md` + `SYSTEM_MANIFEST.md` + `STATUS.md`

## Struktur
- `AGENT_SYSTEM.md` — aturan kerja agent (6 Tahap Fondasi + Coding + Handoff, 401 baris inti)
- `PANDUAN_PEMAKAIAN.md` — pegangan privat pemilik (JANGAN masuk repo target; sudah ada sejak Claude)
- `SYSTEM_MANIFEST.md` — manifest + warisan W-01…W-09
- `STATUS.md` — checkpoint deterministik
- `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` — pegangan 2-file identik (W-01)
- `START_DI_SINI.md` — navigasi per jenis sesi
- `10_LOG_SESI.md` — aturan log berkelanjutan (W-02)
- `_log-sesi/LOG_SESI_2026-09-15.md` — log run pertama
- `ACCEPTANCE_TESTS.md` + `ACCEPTANCE_TEST_LOG.md` + `_sistem/validate_system.py` — QA 3-lapis (W-06)
- `_salinan-meta/PLATFORM_LMARENA.md` — salinan berlabel fakta platform (W-07)
- `_Notes.md` — link chat Claude: https://claude.ai/chat/c2d459f8-4adc-48e3-a37d-6cbee248e6d3

## Bentuk & Warisan
- **Bentuk:** Gabungan (Bertingkat Fondasi 1-6 + Siklus Coding + Gabungan Siklus Baru)
- **Unit:** 1 aplikasi = 1 siklus Fondasi (/docs 6) + Coding ROADMAP
- **Warisan:** W-01…W-09 semua diterapkan (cek SYSTEM_MANIFEST.md)
- **Fakta platform:** lmarena branch arena otomatis, push dicabut setelah merge, sesi bisa crash → mitigasi commit+push + LOG_SESI

## Ke Mana Hasil Dibawa
- Hasil kerja Fondasi → `/docs/*.md` + `PROJECT_STATE.md` di repo aplikasi target
- Hasil Coding → kode aplikasi di repo target
- Semua via branch `tahap-*/fase-*` → PR tanpa auto-merge → merge pemilik

## Status Saat Ini
- **2026-09-15:** run klinik pertama selesai Tahap C (rename + manifest + pegangan + log + QA + salinan meta). Menunggu Verifikasi D + Catatan E + Panen F + G-Final + PR. Belum ada /docs Fondasi yang terisi — siap mulai Tahap 1 Discovery kapan saja.
