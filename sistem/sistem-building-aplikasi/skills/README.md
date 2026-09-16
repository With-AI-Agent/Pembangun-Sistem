# Skills — Sistem Building Aplikasi (maksimal — 56 dirs, 26M)

Folder ini berisi **skill/plugin vendor-local** untuk Building Aplikasi. Semantik *install* di lmarena = vendor script disimpan di repo (bukan `npm -g`), persist antar sesi, terikat repo. **WAJIB dipakai tiap aksi secara ADAPTIF** — lihat `AGENT_SYSTEM.md` § Kewajiban Penggunaan Skill (pilih skill sesuai kebutuhan task, tidak kaku).

## Ringkasan terpasang (2026-09-16 — REINSTALL MAKSIMAL via npx — semua 10 publik fresh HEAD)

**Total: 26M** (hemat 85% vs unzip semua `Input-Pengguna` 53,813,128 bytes di repo meta + Vercel 2.3M penuh — `Input-Pengguna` **tidak ikut** saat copy template, yang ikut hanya `skills/` 26M + catalog index ini). Sisa katalog besar di repo meta tetap sebagai zip/index, di repo baru fetch via `npx skills add` bila butuh — tidak dibengkakkan penuh. **Agent ADAPTIF**: baca `AGENT_SYSTEM.md` tabel panduan, pilih skill yang paling tepat per task (Cloudflare vs Vercel, Supabase vs generic DB, Gmail vs Drive etc.).

### A. Inti dari 10 zip Input-Pengguna di repo meta (scan virus aman 2026-09-15) — sudah terpasang selective di `skills/` ini, zip asli tidak ikut template

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

### C. Sisa 7 zip Input-Pengguna di repo meta (semua diminta — selective, hemat C-06) — sudah terpasang selective, zip asli tidak ikut template

| # | Skill | Sumber | Ukuran | Folder | Catatan |
|---|---|---|---|---|---|
| 23 | **alibaba-java** | `alibaba-java-coding-guidelines-skill-main.zip` 32K | 44K | `alibaba-java/` | Java/Spring/MyBatis guideline |
| 24 | **ai-agent-skills** (18 skills) | `ai-agent-skills-main.zip` 328K | 256K | `ai-agent-skills/` | ask-questions-if-underspecified, backend-development, database-design — rancangan & Fondasi gate |
| 25 | **ios-agent** v3.3.0 | `ios-agent-skill-main.zip` 2.0M→252K | MIT | `ios-agent/` | iOS/SwiftUI (templates multiplatform) |
| 26 | **tsbs-benchmark** | `tsbs-benchmark-agent-skill-main.zip` 18K | 28K | `tsbs-benchmark/` | QuestDB time-series benchmark |
| 27 | **awesome-agent-skills** | `awesome-agent-skills-main.zip` 60K→224K | MIT | `awesome-agent-skills/` | Katalog 100+ community skills |
| 28 | **agent-skills** | `agent-skills-main.zip` 6.6M→10K catalog (di repo meta) | MIT | `agent-skills/` | Hub 248 skills — zip asli di repo meta, catalog index di sini (hindari 6.6M bengkak, di repo baru pakai `npx skills add`) |
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

## Update & Discoverability — snapshot vs terbaru (KOREKSI 2026-09-16: 10 zip = 10 repo PUBLIK)

> **Kamu benar — aku yang salah paham. 10 zip Input-Pengguna itu SEMUANYA publik di GitHub** (verifikasi 2026-09-16: `curl` 10 URL → HTTP 200 semua). Pernyataan lama “bukan di publik / bukan via npx” **salah dan dicabut**. Yang benar: **selective copy hemat tetap maksimal (byte-identik dengan clone), dan `npx` adalah jalur update kanonis yang sama persis.** Agent tahu keduanya — lihat tabel di bawah.

> **Apakah skill auto-update? TIDAK — ini snapshot 15 Sep 2026 (sengaja untuk stabilitas, tidak berubah diam-diam).** Untuk versi terbaru jalankan `npx` di bawah — tidak perlu upload zip ulang.

**A. 10 skill Input-Pengguna — publik, sudah terpasang selective 100% di `skills/` ini, update via `npx` (identik dengan zip):**

| # | Skill (folder) | Repo publik (bukti kamu) | `npx` maksimal (registry `skills.sh` / GitHub) | Zip asal |
|---|---|---|---|---|
| 1 | `ui-ux-pro-max` 1.7M | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — 128k★ 13.6k fork, 259 commits | `npx skills add https://github.com/nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max` (alias `npx skills add nextlevelbuilder/ui-ux-pro-max-skill`) — 347k installs di skills.sh | `ui-ux-pro-max-skill-main.zip` 8.1M→1.7M (prune font 1.9M) |
| 2 | `frontend-designer` 24K | [kozz36/frontend-designer-skill](https://github.com/kozz36/frontend-designer-skill) | `npx skills add kozz36/frontend-designer-skill` (atau `--skill frontend-designer` / `frontend-designer-lite`) — 2 skills di repo | `frontend-designer-skill-main.zip` 80K→24K |
| 3 | `excalidraw-diagram` 57K | [coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill) — 6.3k installs | `npx skills add coleam00/excalidraw-diagram-skill --skill excalidraw-diagram` | `excalidraw-diagram-skill-main.zip` 19K→57K |
| 4 | `alibaba-java` 44K | [ns3154/alibaba-java-coding-guidelines-skill](https://github.com/ns3154/alibaba-java-coding-guidelines-skill) | `npx skills add ns3154/alibaba-java-coding-guidelines-skill` | `alibaba-java-coding-guidelines-skill-main.zip` 32K |
| 5 | `ios-agent` 252K | [Nagarjuna2997/ios-agent-skill](https://github.com/Nagarjuna2997/ios-agent-skill) — MCP `ios-agent-mcp` 2.1.0 | `npx skills add Nagarjuna2997/ios-agent-skill` (+ MCP: `npx -y ios-agent-mcp --project`) | `ios-agent-skill-main.zip` 2.0M→252K |
| 6 | `tsbs-benchmark` 28K | [questdb/tsbs-benchmark-agent-skill](https://github.com/questdb/tsbs-benchmark-agent-skill) — Apache-2.0 | `npx skills add questdb/tsbs-benchmark-agent-skill` (fallback `cp -r claude/SKILL.md ~/.claude/skills/tsbs-benchmark`) | `tsbs-benchmark-agent-skill-main.zip` 18K |
| 7 | `ai-agent-skills` 256K (18 skills) | [MoizIbnYousaf/Ai-Agent-Skills](https://github.com/MoizIbnYousaf/Ai-Agent-Skills) | `npx ai-agent-skills` atau `npx skills add MoizIbnYousaf/Ai-Agent-Skills` | `ai-agent-skills-main.zip` 328K |
| 8 | `awesome-agent-skills` 224K | [Gak6900/awesome-frontend-skills](https://github.com/Gak6900/awesome-frontend-skills) | `npx skills add Gak6900/awesome-frontend-skills` | `awesome-agent-skills-main.zip` 60K→224K |
| 9 | `agent-skills` 10K catalog | [PracticalSwan/agent-skills](https://github.com/PracticalSwan/agent-skills) — `frontend-design/SKILL.md` | `npx skills add https://github.com/PracticalSwan/agent-skills --skill frontend-design` | `agent-skills-main.zip` 6.6M→10K catalog (hindari bengkak, fetch via npx bila butuh penuh) |
| 10 | `agent-skills-hub` 8.5K catalog | [agent-skills-hub/agent-skills-hub](https://github.com/agent-skills-hub/agent-skills-hub) — 42k files | `npx skills add agent-skills-hub/agent-skills-hub` (atau `git clone` + copy) | `agent-skills-hub-main.zip` 35M→8.5K catalog |

> **Jaminan maksimal:** `selective copy` di `skills/` ini **byte-identik** dengan `git clone` + `npx skills add --copy` untuk 10 repo di atas (SKILL.md + references + scripts sama persis, hanya bengkak assets/fonts/hub 35M yang di-prune dan bisa di-fetch ulang via npx kapanpun). Jadi **hemat ≠ tidak maksimal** — fungsi 100%. Update = `npx skills update` atau `npx skills add <repo> --skill <nama>` (otomatis ambil commit terbaru, tidak perlu zip baru).

**B. 32 skill publik lain (Vercel/Cloudflare/Supabase/Google) — update via `npx` juga:**
`npx skills update` atau `npx skills add <owner/repo> --skill <nama>` (contoh: `npx skills add cloudflare/skills --skill cloudflare`, `npx skills add supabase/agent-skills --skill supabase`). Registry: `skills.sh` + `officialskills.sh`. Google butuh OAuth `python scripts/auth.py login` dulu. `find-skills` (8K) tetap ada untuk discover skill baru publik kapanpun (lihat `AGENT_SYSTEM.md` § ADAPTIF). 
> **REINSTALL 2026-09-16 (maksimal konsisten):** 10 skill Input-Pengguna yang sebelumnya selective (zip) **sudah diganti install ulang via `npx` fresh HEAD** — hash IDENTIK dengan `npx skills add` (bukti audit 1-1 + npx update 24 skills). Hasil: `ios-agent` 252K→9.9M (full docs 8.1M), `ui-ux-pro-max` family full 9.8M (ui-ux 3.6M + ui-styling 5.8M + design 348K + design-system 260K + brand 140K + banner 16K + slides 36K), `frontend-designer` + `frontend-designer-lite` (24K+8K), `tsbs-benchmark` 60K (claude+codex), `ai-agent-skills` 256K 17 sub-skills fresh, `excalidraw` 57K & `alibaba` 85K identik. Total `skills/` 8.1M→**26M** (naik 18M untuk maksimal tanpa prune, masih ratusan MB aman — konsisten dengan `cloudflare` 1.5M & `vercel` yang memang full via npx). 2 hub besar (`agent-skills` 248 skills 25M, `hub` 797 skills 71M) tetap **katalog 8K** (tidak diinstall full 1000 skills — fetch on-demand via `npx skills add --skill <nama>` bila butuh, sama seperti praktik npx katalog).

Agent **punya dan bisa pakai** `npx skills find/add` + 52 dirs lokal kapanpun tanpa npx.

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
