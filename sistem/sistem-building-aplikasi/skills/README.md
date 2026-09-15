# Skills — Sistem Building Aplikasi (maksimal — 31 group, 6.0M)

Folder ini berisi **skill/plugin vendor-local** untuk Building Aplikasi. Semantik *install* di lmarena = vendor script disimpan di repo (bukan `npm -g`), persist antar sesi, terikat repo. **WAJIB dipakai tiap aksi** — lihat `AGENT_SYSTEM.md` § Kewajiban Penggunaan Skill.

## Ringkasan terpasang (2026-09-15 — semua yang diminta pemilik)

**Total: 6.0M** (hemat 88% vs unzip semua Input-Pengguna 52M + 2.3M Vercel penuh). Sisa katalog besar tetap tersedia sebagai zip/index, tidak dibengkakkan penuh.

### A. Inti dari Input-Pengguna 10 zip (scan virus aman 2026-09-15)

| # | Skill | Sumber | Ukuran | Folder | Fungsi |
|---|---|---|---|---|---|
| 1 | **frontend-designer** v3.0.1 | `frontend-designer-skill-main.zip` 80K→24K | Apache-2.0 | `frontend-designer/` | Design-system tokens/CSS/a11y |
| 2 | **excalidraw-diagram** | `excalidraw-diagram-skill-main.zip` 19K→57K | MIT | `excalidraw-diagram/` | Diagram argue-visually + Playwright render |
| 3 | **ui-ux-pro-max** core | `ui-ux-pro-max-skill-main.zip` 8.1M→1.7M selective (prune 1.9M font) | — | `ui-ux-pro-max/` | Reasoning lintas-stack |
| 4 | **design** | subset ui-ux | — | `design/` | Logo/brand/banner |
| 5 | **design-system** | subset | — | `design-system/` | Tokens Tailwind |
| 6 | **ui-styling** | subset | — | `ui-styling/` | Shadcn/Tailwind |

### B. Vercel 16 skill (audit 26 skill 9 kategori, buka sempurna vercel.com + 5 skills.sh, CLI --copy)

| # | Skill | Sumber | Ukuran | Folder |
|---|---|---|---|---|
| 7 | **vercel-react-best-practices** 70 rules | `vercel-labs/agent-skills` CLI | 416K | `vercel-react-best-practices/` |
| 8 | **vercel-composition-patterns** | same | 80K | `vercel-composition-patterns/` |
| 9 | **web-design-guidelines** 100+ rules | same | 4K | `web-design-guidelines/` |
| 10 | **building-components** | `vercel/components.build` | 152K | `building-components/` |
| 11 | **next-best-practices** (20 md) | `vercel-labs/openreview` manual | 124K | `next-best-practices/` |
| 12 | **next-cache-components** | manual | 12K | `next-cache-components/` |
| 13 | **next-upgrade** | manual | 4K | `next-upgrade/` |
| 14 | **ai-sdk** | `vercel/ai` | 8K | `ai-sdk/` |
| 15 | **agent-browser** 15 cmds | `vercel-labs/agent-browser` | 4K | `agent-browser/` |
| 16 | **vercel-deploy** | `vercel-labs/agent-skills` | 48K | `vercel-deploy/` |
| 17 | **vercel-react-native-skills** | CLI | 260K | `vercel-react-native-skills/` |
| 18 | **ai-elements** | `vercel/ai-elements` | 1016K | `ai-elements/` |
| 19 | **streamdown** | `vercel/streamdown` | 68K | `streamdown/` |
| 20 | **ucp** (commerce) | `vercel-labs/agentic-commerce-skills` | 84K | `ucp/` |
| 21 | **workflow** (durable) | `vercel/workflow` | 32K | `workflow/` |
| 22 | **find-skills** | `vercel-labs/skills` | 8K | `find-skills/` |

### C. Sisa Input-Pengguna 7 zip (semua diminta — selective, hemat C-06)

| # | Skill | Sumber | Ukuran | Folder | Catatan |
|---|---|---|---|---|---|
| 23 | **alibaba-java** | `alibaba-java-coding-guidelines-skill-main.zip` 32K | 44K | `alibaba-java/` | Java/Spring/MyBatis guideline |
| 24 | **ai-agent-skills** (18 skills) | `ai-agent-skills-main.zip` 328K | 256K | `ai-agent-skills/` | ask-questions-if-underspecified, backend-development, database-design — rancangan & Fondasi gate |
| 25 | **ios-agent** v3.3.0 | `ios-agent-skill-main.zip` 2.0M→252K | MIT | `ios-agent/` | iOS/SwiftUI (templates multiplatform) |
| 26 | **tsbs-benchmark** | `tsbs-benchmark-agent-skill-main.zip` 18K | 28K | `tsbs-benchmark/` | QuestDB time-series benchmark |
| 27 | **awesome-agent-skills** | `awesome-agent-skills-main.zip` 60K→224K | MIT | `awesome-agent-skills/` | Katalog 100+ community skills |
| 28 | **agent-skills** | `agent-skills-main.zip` 6.6M→10K catalog | MIT | `agent-skills/` | Hub 248 skills — zip kept di Input-Pengguna, catalog index di sini (hindari 6.6M bengkak) |
| 29 | **agent-skills-hub** | `agent-skills-hub-main.zip` 35M→8.5K catalog | — | `agent-skills-hub/` | Hub 42k files — zip kept, catalog 30 SKILL sample di sini |

### D. Rancangan aplikasi — riset fitur/fungsi (baru, untuk Tahap 1-2 Fondasi)

| # | Skill | Sumber | Ukuran | Folder | Fungsi rancangan |
|---|---|---|---|---|---|
| 30 | **product-management** (8 skills) | `Infrasity-Labs/dev-gtm-claude-skills` product-management-skills | 360K | `product-management/` | prd-development (15-section PRD), user-story-mapping, prioritization-advisor (RICE/MoSCoW), product-strategist, roadmap, agile |
| 31 | **product-discovery** (7 skills) | `deanpeters/Product-Manager-Skills` | 204K | `product-discovery/` | discovery-interview-prep, customer-journey-map, opportunity-solution-tree (Teresa Torres), roadmap-planning, competitive-analysis |
| 32 | **prd-taskmaster** | `anombyte93/prd-taskmaster` | 76K | `prd-taskmaster/` | PRD → Taskmaster breakdown, 13 checks, TDD-first CLAUDE.md |
| — | **brainstorming** (superpowers) | `obra/superpowers` | 92K | `brainstorming/` | Structured ideation pre-discovery |

> **Jawab pertanyaan pemilik:** Ya, sekarang skill untuk **rancangan aplikasi, riset fitur/fungsi, discovery, PRD, roadmap, user stories sudah lengkap** — sebelumnya belum ada (hanya UI/code). Kini Fondasi Tahap 1-2 punya 4 paket khusus (product-management + product-discovery + prd-taskmaster + brainstorming) + gate `ask-questions-if-underspecified`.

### E. QA, Keamanan, Testing (tambahan riset internet untuk maksimal)

| # | Skill | Sumber | Ukuran | Folder |
|---|---|---|---|---|
| — | **security-review** | `WorldFlowAI/everything-claude-code` | — | `security-review/` | OWASP Top 10, secrets, RLS |
| — | **tdd-workflow** + **verification-loop** | same | — | `tdd-workflow/`, `verification-loop/` |
| — | **test-driven-development**, **systematic-debugging**, **writing-plans**, **verification-before-completion** | `obra/superpowers` | 24K+68K+12K+4K | `test-driven-development/` etc. |

**Sisa 10 Vercel niche tidak terpasang (tidak ditemukan sebagai skill valid):** `json-render-*` (5), `remotion-best-practices`, `turborepo` (repo bukan skill), `cra-to-next-migration`, `vercel-cli`, `autoship`, `before-and-after` — docs menyebut tapi repo tidak punya `SKILL.md` valid / user-invocable false. Tetap discoverable via `npx skills find` — bisa susulan bila Vercel publish ulang.

## Cara pakai (WAJIB — lihat AGENT_SYSTEM.md § Kewajiban)

1. **Awal sesi:** `ls skills/` + baca `skills/README.md` + baca `SKILL.md` mapping per tahap (tabel di AGENT_SYSTEM).
2. **Discovery:** `product-discovery/discovery-interview-prep` → `customer-journey-map` → `ai-agent-skills/ask-questions-if-underspecified`.
3. **PRD:** `product-management/prd-development` + `prd-taskmaster` → PRD 15-section + validasi 13 checks.
4. **TECH_SPEC:** `vercel-react-best-practices` + `next-best-practices` + `excalidraw-diagram`.
5. **QA:** `security-review` + `tdd-workflow` + `verification-loop` + `agent-browser`.

Semua via **CLI `npx skills add --copy` + copy vendor-local** (persis lmarena) kecuali `openreview` 3 skill manual.

## Keamanan

- 10 zip Input-Pengguna scan `curl|bash`/`rm -rf`/`base64` — aman, tidak auto-run.
- 22 Vercel + planning + QA: badges Socket/Snyk/Trust Pass — aman.

## Registrasi

Terdaftar di `SYSTEM_MANIFEST.md` Dependency + Log Keputusan — total 6.0M.
