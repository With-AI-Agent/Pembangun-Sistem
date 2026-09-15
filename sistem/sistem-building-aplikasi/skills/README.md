# Skills — Sistem Building Aplikasi

Folder ini berisi **skill/plugin vendor-local** untuk Building Aplikasi.
Semantik *install* di lmarena = vendor script disimpan di repo (bukan `npm -g`), persist antar sesi, terikat repo.

## Skill terpasang (run klinik susulan 2026-09-15 — borongan K-10)

| # | Skill | Sumber zip | Versi/Lisensi | Folder | Fungsi untuk Building Aplikasi |
|---|-------|------------|---------------|--------|-------------------------------|
| 1 | **frontend-designer** | `frontend-designer-skill-main.zip` (80K→24K terpasang) | v3.0.1 Apache-2.0 | `skills/frontend-designer/` | Design-system, tokens, CSS architecture, a11y — dipakai saat TECH_SPEC & Coding membuat UI production-ready |
| 2 | **excalidraw-diagram** | `excalidraw-diagram-skill-main.zip` (19K→57K) | MIT-like | `skills/excalidraw-diagram/` | Generate diagram arsitektur/workflow `.excalidraw` yang *argue visually* + pipeline Playwright render — dipakai di DISCOVERY/TECH_SPEC/ROADMAP |
| 3 | **ui-ux-pro-max** (core) | `ui-ux-pro-max-skill-main.zip` (8.1M→1.7M selective) | — | `skills/ui-ux-pro-max/` | Reasoning UI/UX lintas stack (tokens, styles, typography) — induk untuk design decision |
| 4 | **design** | (subset ui-ux-pro-max) | — | `skills/design/` | Logo/brand/banner/slides/icon — asset aplikasi non-teknis |
| 5 | **design-system** | (subset ui-ux-pro-max) | — | `skills/design-system/` | Primitive/semantic tokens, Tailwind integration — jembatan ke frontend-designer |
| 6 | **ui-styling** | (subset ui-ux-pro-max) | — | `skills/ui-styling/` | Shadcn/Tailwind responsive/theming/a11y |

**Total terpasang: 2.1M (hemat 92% vs 52M jika semua zip di-unzip penuh).** Heavy data tidak esensial (google-fonts.csv 730K, phosphor-icons 805K) di-prune dan bisa di-restore kapan saja dari `Input-Pengguna/` — sesuai C-06 anti bengkak aset.

## Cara pakai (agent)

- Baca `SKILL.md` di skill yang relevan sebelum eksekusi — tiap skill punya Activation Contract & Hard Rules.
- Contoh:
  - Mau buat TECH_SPEC layout/UI → baca `skills/frontend-designer/SKILL.md` + `skills/design-system/*.md`
  - Mau visualkan arsitektur → minta agent "buat diagram Excalidraw untuk …" (agent akan pakai `skills/excalidraw-diagram/references/`)
  - Mau audit UI → `skills/ui-ux-pro-max/scripts/search.py` / `scripts/design_system.py` (stdlib-only, tidak perlu install global)

## Keamanan

- Semua 10 zip telah di-scan `unzip -l + strings | grep -Ei curl|base64|rm -rf|eval|subprocess` (2026-09-15):
  - Tidak ada virus/malware jelas. Pola `curl | bash` hanya di `agent-skills-hub` (`bun.sh/install`) dan instalasi docs, `rm -rf` hanya di Dockerfile `rm -rf /var/lib/apt/lists`, `base64 -d` hanya di kubeconfig CI, `subprocess` di ui-ux hanya local `subprocess` Python standar — tidak dieksekusi otomatis.
  - Install dilakukan **tanpa menjalankan** `bin/install.js`/`install.sh`/`setup.sh` otomatis; hanya copy `SKILL.md`+`references` — aman sandbox.
- Jika script installer perlu dijalankan kelak, review manual dulu, jalan di branch terpisah, dan catat di Log Keputusan.

## Kandidat ditunda (butuh approval susulan)

Lihat `_sistem/02_TAWARAN_KAPABILITAS_PLUS_AUDIT.md` — 10 zip diaudit lengkap (struktur SKILL.md, lisensi, skor relevansi Building Aplikasi, risiko). Kandidat besar seperti `agent-skills-hub` (35M, 42k file), `agent-skills` (6.6M), `ios-agent-skill` (2M, Swift/iOS), `alibaba-java` (32K, Java) tersedia di `Input-Pengguna/` dan bisa ditanam selective bila stack aplikasi membutuhkannya. Borongan berikutnya maksimal 5 item —user sudah janji "nanti ada skill tambahan lagi" → folder ini siap extensible.

## Registrasi manifest

Terdaftar di `SYSTEM_MANIFEST.md` → Dependency eksternal (bagian bawah) + Log Keputusan.
