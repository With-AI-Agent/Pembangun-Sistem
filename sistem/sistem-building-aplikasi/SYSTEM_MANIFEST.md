# System Manifest — Sistem Building Aplikasi

> Manifest ini adalah kartu identitas dan kontrak navigasi sistem ini. Bukan pengganti dokumen instruksi.

## Identitas

- **Nama sistem:** Sistem Building Aplikasi (Sistem Fondasi Aplikasi)
- **Tujuan utama:** Membangun aplikasi untuk pemilik non-teknis lewat 2 fase: Fondasi (6 dokumen: DISCOVERY → PRD → TECH_SPEC → AGENT_OPERATING_GUIDE → ROADMAP → CROSS_CHECK) + Coding (eksekusi Roadmap task demi task dengan DECISIONS_LOG & PROJECT_STATE), dijalankan oleh AI Agent yang mengurus semua pekerjaan teknis.
- **Pengguna/consumer:** Pemilik proyek yang tidak paham coding/architecture/DevOps (user) — consumer hasil akhir = pengguna aplikasi yang dibangun.
- **Pemilik keputusan:** Pengguna (pemilik repo) — semua approval Besar + merge PR adalah haknya.
- **Versi:** `0.1.0`
- **Tahap:** siap-pakai — cek W-01/W-02/W-03 kembali ketat sudah dilakukan pada run klinik 2026-09-15 (validator ketat hijau; lihat 03_KONTRAK_WARISAN bagian Tahap pembangunan — provenance meta)
- **Status:** `Siap dipakai` — Fondasi 6 tahap + Coding aktif didefinisikan di AGENT_SYSTEM.md; pegangan, STATUS, LOG_SESI, QA, dan fakta platform tertanam pada run klinik pertama (kit v0.2.0, 2026-09-15, panggung rawat inap).
- **Tanggal dibuat:** 2026-09-15 (dirawat pertama oleh Klinik; file AGENT_SYSTEM.md lahir sebelumnya di Claude — lihat _Notes.md)
- **Audit terakhir:** 2026-09-15 — run klinik pertama (Tahap B diagnosis → G-Rencana → Tindakan → Verifikasi → Catatan → Panen), validator repo & self-contained PASS.
- **Quality protocol (versi sistem ini — self-contained):** trigger audit, level default, dan prosedur rollback dirinci di bagian Quality & Evolution manifest ini; verifikasi output oleh ACCEPTANCE_TESTS.md + _sistem/validate_system.py di dalam folder sistem ini. Induk: _meta/QUALITY_ASSURANCE_AND_EVOLUTION.md di master = provenance saja (sistem harus tetap berfungsi penuh bila foldernya diunduh standalone).

## Bentuk Sistem

- **Bentuk:** [x] Bertingkat  [ ] Flat  [x] Siklus  [x] Gabungan (Bertingkat di Fondasi: Tahap 1→6 berurutan; Siklus di Coding: assess → eksekusi task → update ROADMAP/DECISIONS_LOG → commit; Gabungan karena Fondasi + Coding + Siklus Baru v1/v2)
- **Unit kerja utama:** 1 aplikasi = 1 siklus Fondasi (6 dokumen di /docs) + eksekusi Coding per ROADMAP (task atomik). Siklus Baru (v1, v2) = unit tambahan.
- **Kriteria satu unit selesai:** 6 dokumen Fondasi disetujui & PROJECT_STATE = CODING_AKTIF (Tahap 6), lalu semua task ROADMAP tuntas, DECISIONS_LOG tercatat untuk Area Berisiko Tinggi, ROADMAP tercentang, PROJECT_STATE terupdate, PR tanpa auto-merge telah di-merge pemilik.
- **Titik approval Besar:** G-Fondasi per dokumen (DISCOVERY, PRD, TECH_SPEC, AGENT_GUIDE, ROADMAP, CROSS_CHECK — pengguna bilang “cukup, tulis draftnya”), perubahan DECISIONS_LOG, perubahan Area Berisiko Tinggi, G-Final sebelum merge, siklus baru v1/v2.
- **Titik approval Kecil:** perbaikan typo, penataan folder, update STATUS/LOG_SESI, commit & push di branch, checkpoint handoff.

## Dokumen Navigasi

- **Entry point:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` (pegangan), `AGENT_SYSTEM.md` (instruksi agent), `START_DI_SINI.md` (navigasi per jenis sesi)
- **Dokumen instruksi aktif:** `AGENT_SYSTEM.md` (6 Tahap Fondasi + Prosedur Coding + Checkpoint & Handoff + Tahap 0.5) + `_sistem/validate_system.py` (turunan self-contained, bila ada)
- **Living documents:** `/docs/DISCOVERY.md`, `/docs/PRD.md`, `/docs/TECH_SPEC.md`, `/docs/AGENT_OPERATING_GUIDE.md`, `/docs/ROADMAP.md`, `/docs/DECISIONS_LOG.md`, `PROJECT_STATE.md` (root)
- **Log keputusan:** tabel Log Keputusan di SYSTEM_MANIFEST ini + di tiap living document /docs
- **Ringkasan cadangan:** `_cadangan-claude/RINGKASAN_sistem-building-aplikasi.md` di repo induk (dibuat pada run klinik pertama; disinkron saat struktur berubah)
- **Laporan audit:** `ACCEPTANCE_TESTS.md` + `ACCEPTANCE_TEST_LOG.md` di folder sistem; validasi lokal `_sistem/validate_system.py`
- **Pegangan pengguna:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` di root folder sistem — WAJIB, mengikuti template pegangan meta, blok prompt identik

## Prinsip

| Prinsip meta-sistem | Berlaku? | Cara diterapkan | Alasan jika di-override |
|---|---|---|---|
| Hierarki | Ya | Fondasi 1→6 bertingkat (DISCOVERY→CROSS_CHECK), lalu ROADMAP → task. Tahap atas menentukan tahap bawah, tidak diulang. | — |
| Chaining | Ya | Agent baca artefak tahap sebelumnya langsung dari /docs di repo; gerbang tetap menghentikan sebelum lanjut | — |
| Approval bertingkat | Ya (kriteria spesifik di Bentuk Sistem) | Besar/Kecil dikunci di manifest ini + AGENT_SYSTEM.md | — |
| Checkpoint & verifikasi | Ya — dan merupakan ISI sistem | PROJECT_STATE deterministik + LOG_SESI berkelanjutan + DECISIONS_LOG wajib; diwariskan ke app yang dibangun | — |
| Log keputusan | Ya | Semua dokumen hidup /docs + manifest wajib tabel Log Keputusan | — |
| Quality assurance & evolusi (prinsip 6) | Ya, kedalaman bertahap | L1: self-audit via validate_system.py; L2: verifikasi output per task; L3: audit silang Tahap 6; rollback = PR balikan | — |

## Warisan (Kontrak)

Status butir 03_KONTRAK_WARISAN untuk sistem ini — default SEMUA diterapkan (G-Rencana 2026-09-15):

| Butir | Status (diterapkan / override) | Letak di folder sistem | Override? |
|---|---|---|---|
| W-01 pegangan | diterapkan | PANDUAN_PENGGUNA.md + PROMPT_ENTRI_UNIVERSAL.md (root) | — |
| W-02 LOG_SESI | diterapkan | 10_LOG_SESI.md (aturan self-contained) + _log-sesi/LOG_SESI_*.md | — |
| W-03 field checkpoint STATUS | diterapkan | STATUS.md (field deterministik exact) + TEMPLATE di _sistem/ | — |
| W-04 manifest | diterapkan | SYSTEM_MANIFEST.md ini | — |
| W-05 log keputusan | diterapkan | tabel Log Keputusan di manifest ini + tiap /docs | — |
| W-06 QA 3-lapis | diterapkan | ACCEPTANCE_TESTS.md + _sistem/validate_system.py (ringkas, stdlib-only) | — |
| W-07 fakta platform | diterapkan | PANDUAN_PENGGUNA.md + bagian Batasan Platform di bawah | — |
| W-08 approval bertingkat | diterapkan | kriteria Besar/Kecil di Bentuk Sistem + AGENT_SYSTEM.md | — |
| W-09 ringkasan cadangan | diterapkan | _cadangan-claude/RINGKASAN_sistem-building-aplikasi.md (root meta) | — |

## Quality & Evolution

- **Lapisan self-audit sistem:** baca ulang AGENT_SYSTEM.md + /docs Relevan, jalankan `_sistem/validate_system.py` (exit 0), cek tools/validate_repo.py bila di repo induk.
- **Lapisan verifikasi output:** Tahap 6 Cross-Check (audit konsistensi /docs) + per-task: DECISIONS_LOG tercatat, ROADMAP tercentang, PROJECT_STATE terupdate.
- **Trigger audit:** (a) setiap 3 task besar selesai, (b) temuan cacat berulang di 2 sesi, (c) perubahan AGENT_SYSTEM.md / kontrak, (d) perintah pemilik.
- **Level audit default:** Sedang
- **Prosedur rollback:** perubahan aturan AGENT_SYSTEM.md = PR balikan + baris di DECISIONS_LOG/REKAM target menyatakan mekanisme dinonaktifkan via commit/PR apa; tidak pernah hapus diam-diam.
- **Override quality protocol:** Tidak ada

## Dependency dan Risiko

- **Dependency eksternal:** akses sesi agent (mayoritas lmarena; kadang Claude Code/Antigravity — aturan netral-platform), akses internet untuk riset Tahap 1/3, `git` + `gh` untuk branch/PR.
  - **Kapabilitas terpasang vendor-local (hemat C-06):**
    - **Batch K-10 zip (audit 10 zip 52M 2026-09-15 — scan virus aman):** `skills/frontend-designer` v3.0.1 Apache-2.0 (24K) + `skills/excalidraw-diagram` (57K, argue-visually) + `skills/ui-ux-pro-max` core 1.7M selective + `design`/`design-system`/`ui-styling` — total 2.1M (prune 1.9M font data).
    - **Batch Vercel 10 skill (audit 26 skill 2026-09-15 — buka sempurna vercel.com + skills.sh 5 link + CLI --copy + manual git sparse):** `skills/vercel-react-best-practices` 416K (70 rules) + `skills/vercel-composition-patterns` 80K + `skills/web-design-guidelines` 4K (100+ rules) + `skills/building-components` 152K + `skills/next-best-practices` 124K + `skills/next-cache-components` 12K + `skills/next-upgrade` 4K + `skills/ai-sdk` 8K + `skills/agent-browser` 4K + `skills/vercel-deploy` 48K — total Vercel 852K; gabung 2.9M. Lihat `skills/README.md` & `_sistem/03_AUDIT_VERCEL_SKILLS.md` (26 skill 9 kategori) & `_sistem/02_TAWARAN_KAPABILITAS_PLUS_AUDIT.md` (10 zip). Sisa 16 Vercel + 4 zip besar (hub 35M, agent-skills 6.6M, ios 2M, java) = katalog discoverable via `npx skills find`.
  - **Kandidat tertunda:** Context7/llms.txt, Superpowers, Playwright (web_search 5 sumber) — lihat tabel 7 kolom di `_sistem/02_TAWARAN_KAPABILITAS_PLUS_AUDIT.md` §B, kini dilengkapi `_sistem/03_AUDIT_VERCEL_SKILLS.md` §2.
- **Data yang wajib ada:** `/docs` (Fondasi), `PROJECT_STATE.md` (penunjuk sesi), `DECISIONS_LOG.md` (memori Area Berisiko), `ROADMAP.md` (task).
- **Risiko utama:** (1) Agent salah tebak Area Berisiko Tinggi karena tidak baca DECISIONS_LOG (mitigasi: W-05 wajib dibaca sebelum sentuh area); (2) Sesi crash tanpa LOG_SESI (mitigasi: W-02 berkelanjutan + PROJECT_STATE deterministik); (3) Scope creep di PRD (mitigasi: MoSCoW Tahap 2 + Non-Goals eksplisit); (4) Bengkak aset akibat skill besar (mitigasi: selective install + prune, sudah hemat 94% 52M+2.3M→2.9M, validator cek ukuran).
- **Batasan yang diketahui:** AGENT_SYSTEM.md berasumsi repo target punya `git`/`gh`; bila target lokal tanpa git, pakai rawat inap di repo meta (K-11 Klinik).
- **Prosedur recovery:** LOG_SESI + STATUS deterministik + PROJECT_STATE; baca ketiganya di awal sesi baru; pola checkpoint meta ditanam self-contained di 10_LOG_SESI.md & STATUS.md.

## Batasan Platform

- **Dipakai via lmarena?** Ya
- **Jika Ya:** rujuk ke _meta/PLATFORM_LMARENA.md (provenance, tanpa backtick di dokumen aktif — salinan berlabel ada di _salinan-meta bila diperlukan). Terapkan checkpoint tiap tahap + **log sesi berkelanjutan (LOG_SESI)** — aturannya diturunkan self-contained ke 10_LOG_SESI.md di folder sistem ini. Alasan kausal: tanpa commit+push, sesi baru tidak bisa melanjutkan (FI-03); tanpa log sesi, konteks sesi (keputusan, koreksi, fakta penting) hilang permanen saat crash karena agent sesi baru tidak punya akses ke chat lama.
- **Jika Tidak:** —

## Acceptance

- [x] Semua dokumen wajib tersedia (AGENT_SYSTEM.md + PANDUAN_PEMAKAIAN.md + manifest/status/pegangan/log/qa pada run klinik 2026-09-15)
- [x] Semua dependency valid (sesi agent + git/gh + akses internet riset — dinyatakan, bukan asumsi terbukti)
- [x] Status dan versi sudah diperbarui (0.1.0 / Siap dipakai — G-Rencana 2026-09-15)
- [x] Approval yang diperlukan sudah ada (G-Rencana borongan 1-9 disetujui pemilik 2026-09-15; G-Final menunggu)
- [x] Audit terakhir tercatat (run klinik pertama — diagnosis katalog + kontrak tanaman + verifikasi)
- [ ] Ringkasan cadangan sinkron (akan dibuat di _cadangan-claude/ pada run ini — W-09)
- [x] Pegangan pengguna tersedia di dalam folder sistem (prompt pembuka + penutup — dibuat run ini)

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-15 | Manifest dibuat pada run klinik pertama (rawat inap, kit v0.2.0) — G-Rencana 1-9 disetujui pemilik (termasuk rename folder SISTEM-BUILDING-APLIKASI → sistem-building-aplikasi) | Klinik Jenis Sesi 3: folder tamu belum punya manifest (C-02) — manifest adalah syarat W-04 dan Tahap siap-pakai; dibuat bersama diagnosis katalog + kontrak tanaman, dalam PR yang sama (prinsip M-14) |
| 2026-09-15 | Susulan K-10 sempurnakan maksimal: audit 10 zip Input-Pengguna (scan virus aman, skor relevansi), pasang selective 3 skill inti (frontend-designer 24K + excalidraw 57K + ui-ux-pro-max selective 2.1M, hemat 92% vs 52M) + tawaran borongan 7-kolom (web_search 5 sumber) | Perbaiki janji Klinik 05_TAWARAN yang sebelumnya hanya stub 2 kandidat tanpa riset + amankan virus (curl\|bash tidak auto-run) + penuhi permintaan pemilik sempurnakan maksimal |
| 2026-09-15 | Susulan Vercel maksimal: audit laman 26 skill 9 kategori (buka sempurna + 5 skills.sh) + uji CLI npx skills add --copy (6 sukses) + copy manual 3 openreview (user-invocable false) + pasang selective 10 Vercel inti (852K) → total skills 2.9M (hemat 94%) + ralat Klinik (tawaran wajib, web_search opsional) | Penuhi "buka semua link sempurna + cara install beneran" + pilihan terbaik vs pasang semua 26 (hemat C-06, sisakan 16 Vercel niche sebagai katalog discoverable) |
