# Skills — Sistem Building Aplikasi

Folder ini berisi **skill/plugin vendor-local** untuk Building Aplikasi.
Semantik *install* di lmarena = vendor script disimpan di repo (bukan `npm -g`), persist antar sesi, terikat repo.

## Skill terpasang (run klinik susulan 2026-09-15 — borongan K-10 + Vercel)

| # | Skill | Sumber | Versi/Lisensi | Folder | Fungsi untuk Building Aplikasi |
|---|-------|--------|---------------|--------|-------------------------------|
| 1 | **frontend-designer** | `frontend-designer-skill-main.zip` (80K→24K) | v3.0.1 Apache-2.0 | `skills/frontend-designer/` | Design-system, tokens, CSS architecture, a11y — TECH_SPEC & Coding UI |
| 2 | **excalidraw-diagram** | `excalidraw-diagram-skill-main.zip` (19K→57K) | MIT | `skills/excalidraw-diagram/` | Diagram argue-visually + Playwright render — DISCOVERY/TECH_SPEC/ROADMAP |
| 3 | **ui-ux-pro-max** (core) | `ui-ux-pro-max-skill-main.zip` (8.1M→1.7M selective, prune 1.9M) | — | `skills/ui-ux-pro-max/` | Reasoning tokens/styles/typography lintas stack |
| 4 | **design** | subset ui-ux-pro-max | — | `skills/design/` | Logo/brand/banner/slides/icon |
| 5 | **design-system** | subset ui-ux-pro-max | — | `skills/design-system/` | Primitive/semantic tokens, Tailwind |
| 6 | **ui-styling** | subset ui-ux-pro-max | — | `skills/ui-styling/` | Shadcn/Tailwind responsive/theming/a11y |
| 7 | **vercel-react-best-practices** | `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices` (CLI --copy) | v1.0.0 MIT, 714K installs | `skills/vercel-react-best-practices/` | 70 rules 8 kategori (waterfalls,bundle,RSC,rerender) — setiap komponen Next.js |
| 8 | **vercel-composition-patterns** | `vercel-labs/agent-skills --skill vercel-composition-patterns` | MIT, 337K installs | `skills/vercel-composition-patterns/` | Compound components, context — hindari boolean prop |
| 9 | **web-design-guidelines** | `vercel-labs/agent-skills --skill web-design-guidelines` | MIT, 635K installs | `skills/web-design-guidelines/` | Web Interface Guidelines 100+ a11y/perf/UX — pelengkap frontend-designer |
| 10 | **building-components** | `vercel/components.build --skill building-components` | MIT | `skills/building-components/` | Primitives ARIA/slots/theming, as-child |
| 11 | **next-best-practices** | `vercel-labs/openreview` `.agents/skills/next-best-practices` (manual, user-invocable false) | MIT | `skills/next-best-practices/` | Next.js file conventions, RSC boundaries, async APIs — 20 md |
| 12 | **next-cache-components** | `vercel-labs/openreview` `.agents/skills/next-cache-components` | MIT | `skills/next-cache-components/` | Next 16 PPR/cacheComponents |
| 13 | **next-upgrade** | `vercel-labs/openreview` `.agents/skills/next-upgrade` | MIT | `skills/next-upgrade/` | Upgrade Next.js codemod |
| 14 | **ai-sdk** | `vercel/ai --skill ai-sdk` (path `skills/use-ai-sdk/SKILL.md`) | MIT | `skills/ai-sdk/` | AI SDK (generateText, streamText, ToolLoopAgent) — baca node_modules/ai/docs versi-terpasang |
| 15 | **agent-browser** | `vercel-labs/agent-browser --skill agent-browser` | 855K installs | `skills/agent-browser/` | Browser automation 15+ command — verify E2E |
| 16 | **vercel-deploy** | `vercel-labs/agent-skills --skill deploy-to-vercel` | v3.0.0 MIT | `skills/vercel-deploy/` | Deploy preview tarball 40+ frameworks |

**Total terpasang: 2.9M (6 dari zip 2.1M + 10 Vercel 852K).** Hemat 94% vs unzip semua zip 52M penuh + hemat C-06 vs pasang 26 Vercel penuh. Heavy data pruned (google-fonts 730K + phosphor 805K) restorable dari `Input-Pengguna/`.

## Cara pakai (agent)

- Baca `SKILL.md` di skill yang relevan sebelum eksekusi — tiap skill punya Activation Contract & Hard Rules.
- Contoh:
  - Mau buat TECH_SPEC layout/UI → baca `skills/frontend-designer/SKILL.md` + `skills/design-system/*.md` + `skills/web-design-guidelines/SKILL.md`
  - Mau visualkan arsitektur → minta agent "buat diagram Excalidraw untuk …" (agent akan pakai `skills/excalidraw-diagram/references/`)
  - Mau audit UI → `skills/ui-ux-pro-max/scripts/search.py` + `skills/web-design-guidelines` fetch https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
  - Mau coding Next.js → baca `skills/vercel-react-best-practices/rules/` + `skills/next-best-practices/*.md` (RSC, async params) + `skills/building-components/SKILL.md`
  - Mau deploy/verify → `skills/vercel-deploy/scripts/deploy.sh` + `agent-browser skills get core`
- Semua skill terpasang via **CLI baku `npx skills add --copy`** (symlink ke 74 agen + `skills-lock.json`) lalu **copy vendor-local** ke `skills/` agar persist lmarena; `openreview` 3 skill di-copy manual karena `user-invocable: false` ditolak CLI.

## Keamanan

- 10 zip Input-Pengguna di-scan `unzip -l + strings | grep -Ei curl|base64|rm -rf|eval|subprocess` (2026-09-15): tidak ada virus, hanya legit `bun.sh|bash`, `rm -rf /var/lib/apt/lists`, `base64 kubeconfig` — tidak auto-run.
- 10 Vercel skill: cek `skills.sh` security badges (Socket/Snyk/Gen Agent Trust Pass kecuali vercel-deploy SnykFail tapi Trust Pass — script hanya upload tarball) — aman.
- Install tanpa menjalankan `bin/install.js`/`setup.sh` otomatis; hanya copy `SKILL.md`+`references` — aman sandbox.

## Kandidat ditunda (butuh approval susulan)

Lihat `_sistem/02_TAWARAN_KAPABILITAS_PLUS_AUDIT.md` (10 zip) & `_sistem/03_AUDIT_VERCEL_SKILLS.md` (26 Vercel, 9 kategori). Sisa 16 Vercel (turborepo, ai-elements, streamdown, ucp, workflow, json-render 5, react-native, cra-to-next, vercel-cli, autoship, find-skills, before-and-after) + 4 zip besar (hub 35M, agent-skills 6.6M, ios 2M, java 32K) tersedia discoverable via `npx skills find <query>` / `Input-Pengguna/` — siap susulan max 5 per borongan.

## Registrasi manifest

Terdaftar di `SYSTEM_MANIFEST.md` → Dependency eksternal + Log Keputusan.
