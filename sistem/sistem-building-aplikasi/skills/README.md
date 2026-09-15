# Skills — Sistem Building Aplikasi (maksimal — 52 dirs, 8.1M)

Folder ini berisi **skill/plugin vendor-local** untuk Building Aplikasi. Semantik *install* di lmarena = vendor script disimpan di repo (bukan `npm -g`), persist antar sesi, terikat repo. **WAJIB dipakai tiap aksi secara ADAPTIF** — lihat `AGENT_SYSTEM.md` § Kewajiban Penggunaan Skill (pilih skill sesuai kebutuhan task, tidak kaku).

## Ringkasan terpasang (2026-09-15 — semua yang diminta pemilik + 2026-09-15 Cloudflare/Supabase/Google)

**Total: 8.1M** (hemat 84% vs unzip semua Input-Pengguna 52M + Vercel 2.3M penuh). Sisa katalog besar tetap tersedia sebagai zip/index, tidak dibengkakkan penuh. **Agent ADAPTIF**: baca `AGENT_SYSTEM.md` tabel panduan, pilih skill yang paling tepat per task (Cloudflare vs Vercel, Supabase vs generic DB, Gmail vs Drive etc.).

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

### F. Deploy & Integrasi — Cloudflare (preferensi pemilik), Supabase, Google Workspace (baru 2026-09-15)

> Pemilik: "aku suka deploy pake cloudflare" + tanya supabase/google workspace/lain. Semua di-install vendor-local via `npx skills add --copy -y --agent "*"` (cloudflare/supabase) + `sanjay3290/ai-skills` (google).

| # | Skill | Sumber | Ukuran | Folder | Fungsi & kapan dipakai (ADAPTIF) |
|---|---|---|---|---|---|
| 33 | **cloudflare** (comprehensive) | `cloudflare/skills` | 1.5M | `cloudflare/` | Workers, Pages, D1, R2, KV, Vectorize, AI, Tunnel, WAF, Terraform — 60+ refs. **Pakai bila deploy target Cloudflare** (bukan Vercel) |
| 34 | **wrangler** | `cloudflare/skills` | 8K | `wrangler/` | CLI Cloudflare Workers — `wrangler whoami/login/deploy`, bindings, secrets |
| 35 | **agents-sdk** | `cloudflare/skills` | 92K | `agents-sdk/` | Stateful Agents SDK (SQLite state, WebSocket, Workflows, MCP, React hooks) — untuk AI agent di Workers |
| 36 | **supabase** | `supabase/agent-skills` | 32K | `supabase/` | DB/Auth/Edge/Storage/Realtime/Vectors/Cron/Queues, `supabase-js`, `@supabase/ssr`, CLI+MCP — **wajib sebelum SQL/RLS/migration** |
| 37 | **supabase-postgres-best-practices** | `supabase/agent-skills` | 156K | `supabase-postgres-best-practices/` | 8 kategori Postgres (query, conn, RLS, schema, lock…) — load BEFORE ubah DB |
| 38 | **gmail** | `sanjay3290/ai-skills` | 49K | `gmail/` | Gmail search/read/send/draft/labels via `python scripts/gmail.py` (OAuth `auth.py login`) |
| 39 | **google-drive** | same | 45K | `google-drive/` | Drive file search/upload/share |
| 40 | **google-sheets** | same | 45K | `google-sheets/` | Sheets read/write `scripts/sheets.py` |
| 41 | **google-calendar** | same | 53K | `google-calendar/` | Calendar events, availability |
| 42 | **google-docs** | same | 37K | `google-docs/` | Docs create/read export |
| 43 | **google-chat** | same | 61K | `google-chat/` | Google Chat spaces messages |
| 44 | **google-slides** | same | 41K | `google-slides/` | Slides create/edit |

Cara pilih adaptif: Deploy? → `cloudflare+wrangler` jika user bilang Cloudflare, `vercel-deploy` jika Vercel. DB? → `supabase` jika Supabase, `database-design` generic jika lain. Email/laporan? → `gmail/google-sheets` dll. Jangan pakai Vercel bila diminta Cloudflare.

**Sisa 10 Vercel niche tidak terpasang (tidak ditemukan sebagai skill valid):** `json-render-*` (5), `remotion-best-practices`, `turborepo` (repo bukan skill), `cra-to-next-migration`, `vercel-cli`, `autoship`, `before-and-after` — docs menyebut tapi repo tidak punya `SKILL.md` valid / user-invocable false. Tetap discoverable via `npx skills find` — bisa susulan bila Vercel publish ulang.

## Cara pakai (WAJIB ADAPTIF — lihat AGENT_SYSTEM.md § Kewajiban + Prinsip Adaptif)

1. **Awal sesi:** `ls skills/` + baca `skills/README.md` + baca `SKILL.md` mapping adaptif per tahap (tabel di AGENT_SYSTEM) — pilih yang paling relevan, kombinasikan bila lintas domain.
2. **Discovery:** `product-discovery/discovery-interview-prep` → `customer-journey-map` → `ai-agent-skills/ask-questions-if-underspecified`.
3. **PRD:** `product-management/prd-development` + `prd-taskmaster` → PRD 15-section + validasi 13 checks.
4. **TECH_SPEC:** `vercel-react-best-practices` + `next-best-practices` + `excalidraw-diagram` + `supabase-postgres-best-practices` (jika Postgres) + `cloudflare` (jika Cloudflare).
5. **QA:** `security-review` + `tdd-workflow` + `verification-loop` + `agent-browser`.
6. **Deploy adaptif:** Cloudflare? → `cloudflare` + `wrangler` (+ `agents-sdk` jika stateful). Vercel? → `vercel-deploy`. Supabase DB? → `supabase` + `supabase-postgres-best-practices` sebelum SQL.
7. **Integrasi Google:** Gmail? → `gmail` (`python scripts/auth.py login` → `scripts/gmail.py search/send`). Sheets/Drive? → `google-sheets/google-drive` dll.

Semua via **CLI `npx skills add --copy -y --agent "*"` + copy vendor-local** (persis lmarena) kecuali `openreview` 3 skill manual + sanjay google (manual copy via CLI sukses).

## Keamanan

- 10 zip Input-Pengguna scan `curl|bash`/`rm -rf`/`base64` — aman, tidak auto-run.
- Vercel 16 + planning + QA + Cloudflare/Supabase/Google: badges Socket/Snyk/Trust Pass — aman (Socket/Snyk Pass untuk cloudflare/supabase, kecuali trust prompt).
- Google skills butuh OAuth browser (`python scripts/auth.py login`) — tidak auto-kirim tanpa `GOG_ACCOUNT` / confirm.

## Registrasi

Terdaftar di `SYSTEM_MANIFEST.md` Dependency + Log Keputusan — total **8.1M, 52 dirs** (cloudflare 1.5M + supabase 188K + google 330K baru).
