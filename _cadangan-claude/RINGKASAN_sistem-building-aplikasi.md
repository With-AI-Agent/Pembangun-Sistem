# RINGKASAN — Sistem Building Aplikasi (sinkron 2026-09-16, pasca run klinik ke-2)

> Ringkasan untuk Claude chat biasa (cadangan lmarena). Dibuat pada run klinik pertama 2026-09-15 (kit v0.2.0, rawat inap); **disinkron total 2026-09-16** oleh run klinik ke-2 karena versi lama memuat angka basi (8.1M/52 dirs, ukuran berkas lama, "PR #59 OPEN menunggu G-Final" padahal sudah MERGED). Sinkron dengan `SYSTEM_MANIFEST.md` **v0.2.0**.
>
> **Angka ukuran sengaja tidak dipakai sebagai bukti** (pelajaran C-04 Katalog Cacat Klinik: bukti volatil). Yang dikutip di sini = fakta terukur bertanggal + perintah mengukurnya.

## Identitas
- **Nama:** Sistem Building Aplikasi (Sistem Fondasi Aplikasi)
- **Tujuan:** membangun aplikasi untuk pemilik non-teknis via Fondasi 6 dokumen (Discovery→PRD→Tech Spec→Agent Operating Guide→Roadmap→Cross-Check) + Coding task-ROADMAP, dijalankan AI agent
- **Pemilik keputusan:** pengguna repo (semua approval Besar + merge PR haknya)
- **Versi:** `0.2.0` — Tahap `siap-pakai`
- **Folder:** `sistem/sistem-building-aplikasi/` (rename dari `SISTEM-BUILDING-APLIKASI` pada 2026-09-15)
- **Entry point:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` (blok prompt identik — dijaga validator) → `START_DI_SINI.md` (7 jenis sesi) → `AGENT_SYSTEM.md` + `SYSTEM_MANIFEST.md` + `STATUS.md` + `PROFIL_PENGGUNA.md` (LANGKAH 0) + `LOG_SESI` terbaru
- **Dokumen ARSIP (jangan diikuti):** `PANDUAN_PEMAKAIAN.md` (v3 pra-template; dulu menyebut hanya `AGENT_SYSTEM.md` yang masuk repo baru — **salah**, sudah dipensiunkan 2026-09-16), `REKAM-KLINIK.md` (jejak perawatan sistem), `_Notes.md` (catatan pribadi pemilik + tautan chat; jangan ikut copy)

## Cara pakai sebagai template (yang paling sering salah dipahami)
- **Yang di-copy ke repo aplikasi baru = SELURUH isi folder**, bukan hanya `AGENT_SYSTEM.md`:
  `cp -r sistem/sistem-building-aplikasi/* my-app-baru/` lalu `git init` → commit → push → hubungkan agent → tempel **Prompt Pembuka Universal**.
- **Jangan ikut di-copy:** `Input-Pengguna/` (10 zip provenance audit, 53.813.128 bytes, hanya di repo meta), `.git`, dan `_Notes.md`.
- **Kenapa tidak bisa satu berkas saja:** `AGENT_SYSTEM.md` merujuk `PROFIL_PENGGUNA.md` (LANGKAH 0 wajib), `skills/` (kewajiban pakai skill), `_sistem/templates/` (10 template), `_sistem/validate_system.py` (audit hidup), `10_LOG_SESI.md`, `START_DI_SINI.md`. Satu berkas saja = semua rujukan putus.
- **Validasi di repo baru (tanpa `tools/` meta):** `python3 _sistem/validate_system.py` harus PASS; cek manual `ls skills/` + `cat skills/README.md`.

## Struktur (self-contained)
- `AGENT_SYSTEM.md` — aturan kerja agent: LANGKAH 0 `PROFIL_PENGGUNA` (dengan pengecualian sesi perawatan sistem, anti-deadlock) → LANGKAH 1 `PROJECT_STATE` → 1b `LOG_SESI`/`STATUS`/branch/PR → 2 lapor posisi → 3 update state sebagai langkah TERAKHIR; § Kewajiban Penggunaan Skill + Prinsip ADAPTIF (tabel pemetaan per Tahap, aturan resolve 6 direktori agregat); 6 Tahap Fondasi; Tahap 0.5 Siklus Baru; Prosedur Coding; Checkpoint & Handoff 6 audit; Stop Conditions; handler "terserah"; § Mekanisme Hidup A (sistem) & B (aplikasi)
- `SYSTEM_MANIFEST.md` — identitas, bentuk, dokumen navigasi, prinsip, Warisan W-01…W-09 (semua diterapkan), Quality & Evolution (trigger audit, rollback = PR balikan), Dependency & Risiko, Batasan Platform, Acceptance, Log Keputusan
- `STATUS.md` — checkpoint deterministik (`**Pekerjaan belum tersimpan:** Tidak ada` tepat 1x + `**Waktu pembaruan:** YYYY-MM-DD — peristiwa`)
- `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` — pegangan 2-file (W-01): prompt pembuka + prompt penutup, istilah awam, kalimat pembuka 5 situasi, § Cara Pakai Sebagai Template, § Profil Pengguna, § Mekanisme Hidup, kebiasaan yang dijaga
- `START_DI_SINI.md` — navigasi 7 jenis sesi (Fondasi, Coding, Siklus Baru, Audit/Cross-Check, Checkpoint & Handoff, Audit/Sempurnakan Sistem, Audit/Sempurnakan Aplikasi)
- `PROFIL_PENGGUNA.md` — 4 pertanyaan wajib sesi pertama (bahasa, gaya, latar belakang, preferensi opsi) → prinsip komunikasi permanen; template reset di `_sistem/templates/`
- `10_LOG_SESI.md` + `_log-sesi/` — log sesi berkelanjutan (W-02), 7 aturan, header "Keadaan Sesi" selalu segar, append-only; `_log-sesi/LOG_SESI_2026-09-15.md` = arsip run pertama (CLOSED, berpenanda "abaikan di repo baru")
- `ACCEPTANCE_TESTS.md` (**AT-01…AT-09**) + `ACCEPTANCE_TEST_LOG.md` + `_sistem/validate_system.py` (stdlib-only, exit 0) — QA 3 lapis (W-06)
- `_sistem/templates/` — **10 template**: 6 Fondasi (DISCOVERY, PRD, TECH_SPEC, AGENT_OPERATING_GUIDE, ROADMAP, DECISIONS_LOG) + PROJECT_STATE + STATUS + LOG_SESI + PROFIL_PENGGUNA. `ROADMAP.md` memuat contoh task **7 atribut lengkap** + checklist kelengkapan (bentuk singkat dilarang `AGENT_SYSTEM.md` Tahap 5)
- `_sistem/` juga berisi arsip audit bertanggal: `02_TAWARAN_KAPABILITAS_PLUS_AUDIT.md`, `03_AUDIT_VERCEL_SKILLS.md`, `AUDIT_NPX_UPDATE_2026-09-16.md`, `AUDIT_ZIP_VS_NPX_2026-09-16.md` (arsip — angka di dalamnya adalah keadaan saat ditulis)
- `docs/README.md` — placeholder `docs/`; 6 dokumen Fondasi dibuat di repo aplikasi saat Tahap 1-6
- `_salinan-meta/PLATFORM_LMARENA.md` — salinan berlabel fakta platform (W-07); **jangan diedit** (harus tetap = master + 3 baris label)
- `REKAM-KLINIK.md` — jejak perawatan Klinik: run 1 (2026-09-15, cap kit v0.2.0) + run 2 (2026-09-16, cap kit v0.2.0)
- `skills/` — vendor-local, **terukur 2026-09-16: `du -sh` 26M, 56 direktori, 1.802 berkas** (23.099.842 bytes apparent). Lihat `skills/README.md` (tabel A–F + § Update & Discoverability + § Keamanan + § Registrasi + **§ Integritas vendor**)

## Kapabilitas terpasang (ringkas — detail & ukuran per folder di `skills/README.md`)
- **Keluarga ui-ux (reinstall penuh via `npx`):** `ui-ux-pro-max`, `ui-styling`, `design`, `design-system`, `brand`, `banner-design`, `slides`
- **Desain/diagram:** `frontend-designer` (+`-lite`), `excalidraw-diagram`, `web-design-guidelines`, `building-components`, `design-system`
- **Vercel/Next (16):** `vercel-react-best-practices`, `vercel-composition-patterns`, `next-best-practices`, `next-cache-components`, `next-upgrade`, `ai-sdk`, `agent-browser`, `vercel-deploy`, `vercel-react-native-skills`, `ai-elements`, `streamdown`, `ucp`, `workflow`, `find-skills`
- **Rancangan/produk:** `product-management` (8 sub-skill), `product-discovery` (7), `prd-taskmaster`, `brainstorming`, `ai-agent-skills` (17 sub-skill valid, nested)
- **QA/keamanan:** `security-review`, `tdd-workflow`, `verification-loop` (tanpa frontmatter — dokumen referensi), `test-driven-development`, `systematic-debugging`, `writing-plans`, `verification-before-completion`
- **Deploy/DB/integrasi:** `cloudflare`, `wrangler`, `agents-sdk`, `supabase`, `supabase-postgres-best-practices`, `gmail`, `google-drive`, `google-sheets`, `google-calendar`, `google-docs`, `google-chat`, `google-slides`
- **Stack spesifik:** `ios-agent` (dokumen penuh), `alibaba-java`, `tsbs-benchmark`
- **Katalog on-demand (tidak dipasang penuh):** `agent-skills` 248 skills (penuh ±25M), `agent-skills-hub` 787 skill valid dari 797 direktori (penuh ±71M), `awesome-agent-skills` (curated list) → fetch `npx skills add <owner/repo> --skill <nama>`

## Bentuk & Warisan
- **Bentuk:** Gabungan — Bertingkat (Fondasi 1→6), Siklus (Coding: assess→eksekusi→update ROADMAP/DECISIONS_LOG→commit), Siklus Baru (v1/v2 via Tahap 0.5)
- **Approval Besar:** per dokumen Fondasi ("cukup, tulis draftnya"), perubahan `DECISIONS_LOG`, Area Berisiko Tinggi, G-Final sebelum merge, siklus baru. **Kecil:** typo, penataan folder, update STATUS/LOG_SESI, commit & push di branch, checkpoint handoff
- **W-01…W-09 semua diterapkan:** pegangan 2-file (W-01), LOG_SESI berkelanjutan (W-02), STATUS deterministik (W-03), manifest (W-04), log keputusan (W-05), QA 3 lapis (W-06), fakta platform + salinan berlabel (W-07), approval bertingkat (W-08), ringkasan cadangan = berkas ini (W-09)
- **Fakta platform lmarena:** branch `arena/...` dibuat otomatis (tidak bisa diganti → deskripsi pindah ke judul commit/PR/LOG_SESI), push dicabut setelah PR merge/close, sesi bisa crash kapan saja → commit+push+LOG_SESI adalah syarat fisik, bukan birokrasi

## Keamanan `skills/` (scan read-only 2026-09-16, 1.802 berkas)
- Tidak ada kredensial nyata (pola `ghp_`, `sk-`, `AKIA`, `xox*`, `-----BEGIN … PRIVATE KEY` = 0); tidak ada `.env`/`.pem`/`.key`/nested `.git`
- `curl … | sh` hanya 1 kemunculan sebagai **teks dokumentasi** (`skills/README.md`), bukan perintah
- `rm -rf` 11 kemunculan — semua di skrip/CI/docs vendor dengan target variabel lokal; `sudo` 4 — semua `sudo xcode-select -s` (docs/CI iOS)
- 37 berkas ber-bit executable + 127 skrip `sh/py/js/ts` → agent wajib baca `SKILL.md` sebelum menjalankan (sudah diwajibkan § Kewajiban Skill)
- Skill Google memakai OAuth browser (`python scripts/auth.py login`) → token tersimpan lokal saat dipakai

## Status saat ini
- **2026-09-15:** run klinik pertama (rawat inap, kit v0.2.0) — rename folder, tanam manifest/STATUS/pegangan/START_DI_SINI/log/QA/salinan meta/RINGKASAN + daftar INDEKS; G-Rencana 1-9 disetujui; 6 gelombang susulan skill (2.1M → 2.9M → 6.0M → 8.1M/52 dirs → reinstall penuh **26M/56 dirs**); review independen + delta review HIJAU; **PR #59 MERGED** 2026-09-16 00:59 UTC (merge commit `1963712`)
- **2026-09-16:** **run klinik ke-2** (rawat inap, kit v0.2.0) — pemicu: pemilik ragu "beneran siap pakai & aman" setelah menemukan `PANDUAN_PEMAKAIAN.md` yang menyebut hanya `AGENT_SYSTEM.md` masuk repo baru. Audit menyeluruh **semua berkas folder** (termasuk pedoman pengguna) + scan keamanan `skills/` + dry-run copy → **11 Critical + 9 Minor** diperbaiki; versi 0.1.0→**0.2.0**; panen: usulan butir katalog Klinik **C-07 "Dokumen Pengganti yang Tidak Dipensiunkan"**
- **Yang belum:** run Fondasi Tahap 1 **nyata** di repo aplikasi pertama (bukti perilaku sesungguhnya); `docs/` masih hanya `README.md`

## Ke mana hasil dibawa
- Hasil Fondasi → `docs/*.md` + `PROJECT_STATE.md` di repo aplikasi target; hasil Coding → kode aplikasi di repo target
- Semua lewat branch kerja sesi → PR **tanpa auto-merge** → merge oleh pemilik; jangan pernah push ke `main`
