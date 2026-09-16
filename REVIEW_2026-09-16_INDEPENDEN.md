# Review Independen — Sistem Building Aplikasi

**Tanggal review:** 2026-09-16 (UTC)  
**Scope:** `sistem/sistem-building-aplikasi` pada branch target `arena/01a0a48f-pembangun-sistem`  
**Commit target yang diaudit:** `44cfd3aaaaf9c569d0d369f037fa398a88db4482` (`44cfd3a`)  
**Base pembanding:** `aad8da66e1545039425b423d055a9d3e1b32f734` (`aad8da6`)  
**PR:** [#59](https://github.com/With-AI-Agent/Pembangun-Sistem/pull/59), masih `OPEN`  
**Mode:** read-only terhadap target dan template; tidak ada file sumber/template target yang diubah.

> **Catatan moving target.** Prompt review yang tersimpan di target masih mem-pin HEAD `6acf7b3` (`REVIEW_PROMPT_2026-09-16.md:6`), tetapi remote branch sudah bergerak melalui `1e64e45`, `e3a8cf1`, lalu `44cfd3a`. Laporan ini sengaja mem-pin dan menjalankan ulang semua gerbang pada HEAD remote terbaru `44cfd3a`, bukan menyamarkan hasilnya sebagai review `6acf7b3`. Pada snapshot `e3a8cf1`, self-contained memang gagal karena self-prefix di `_sistem/AUDIT_NPX_UPDATE_2026-09-16.md:43`; commit `44cfd3a` menghapus prefix tersebut dan hasil terbaru sudah PASS.

## 1. Status, log, dan diff

- Checkout sesi tetap `arena/01a0a797-pembangun-sistem` pada `df726196970b63ed898603f311053a9a932f20eb`, `git status --short --branch` bersih.
- Target dibaca dari remote ref dan diarsipkan ke `/tmp/pembangun-sistem-review-01a0a48f`; tidak dilakukan checkout atau push ke branch target.
- `git diff main...HEAD` tidak dapat dipakai pada checkout shallow/grafted ini karena tidak ada merge-base dengan `main`. Sesuai fallback pada prompt review, dipakai `git diff aad8da6..44cfd3a`:
  - **1.842 files changed**
  - **433.109 insertions, 24 deletions**
- Sepuluh commit target terakhir diverifikasi dengan `git log`; commit terbaru adalah `44cfd3a fix review: STATUS 26M 56 dirs + self-contained PASS ...`.

## 2. Ukuran dan bentuk `skills/`

Pengukuran pada arsip target:

| Pengukuran | Hasil | Keterangan |
|---|---:|---|
| `ls -1 sistem/.../skills/ \| wc -l` | 57 | 56 direktori + `README.md`; ini bukan hitungan direktori murni |
| `find skills -mindepth 1 -maxdepth 1 -type d \| wc -l` | **56** | hitungan direktori yang benar |
| Direktori root yang memiliki `SKILL.md` | 50 | 6 direktori lain adalah aggregate/catalog parent |
| `find skills -type f -name SKILL.md \| wc -l` | 87 | termasuk skill nested |
| file reguler di `skills/` | 22.808.963 bytes | tidak termasuk block overhead filesystem |
| `du -sb skills/` | 23.099.519 bytes | sekitar 23,1 MB desimal |
| `du -sh skills/` | **26M** | hasil yang diminta prompt |

## 3. Ringkasan gerbang validator

| Gerbang | Perintah | Hasil pada HEAD `44cfd3a` |
|---|---|---|
| Validator lokal sistem | `python3 sistem/sistem-building-aplikasi/_sistem/validate_system.py` | **PASS** — `SYSTEM-BUILDING-APLIKASI VALIDATOR: PASS` |
| Validator repo | `python3 tools/validate_repo.py` | **PASS / exit 0**, 104 active docs dan 336 path references; ada 2 warning unresolved yang dicatat di bawah |
| Failure injection | `python3 tools/test_failure_injection.py` | **PASS 72 skenario** (`15 + 13 + 14 + 10 + 20`) |
| Self-contained sistem | `python3 tools/check_selfcontained.py --sistem sistem-building-aplikasi --report` | **PASS**, 0 temuan; 2 rujukan historis tidak ditegakkan |
| Self-contained semua sistem | `python3 tools/check_selfcontained.py --semua` | **PASS**, 4 sistem |
| Backup/restore | `python3 tools/backup_verify.py` | **PASS**, 36 file diverifikasi dan restore OK |
| Template builder | `python3 tools/build_template.py` | **PASS**; smoke juga exit 0, dengan 5 warning referensi meta yang memang di luar paket benih |
| GitHub checks | `gh pr checks 59` | Tidak ada check CI yang dilaporkan; bukti di atas adalah eksekusi lokal |

### Warning `validate_repo`

`tools/validate_repo.py` tetap mengembalikan exit 0, tetapi melaporkan dua unresolved reference pada `_sistem/AUDIT_NPX_UPDATE_2026-09-16.md:37` untuk label contoh `.claude/skills/.../SKILL.md` dan `sistem/.../skills/.../SKILL.md`. Ini bukan kegagalan self-contained karena keduanya adalah kolom bukti audit, tetapi tidak konsisten dengan acceptance log yang mengklaim `0 warning`.

## 4. Katalog 248/797 dan on-demand

Bukti lokal:

- `skills/agent-skills/CATALOG.md` ada, 60 baris, menyatakan **248 skills**, HEAD `ff6d12f`; `git ls-remote` mengonfirmasi `ff6d12f61e8250dd1b988e101a482f6adc05c451`.
- `skills/agent-skills-hub/CATALOG.md` ada, 60 baris, menyatakan **797 skills**, HEAD `8185719`; `git ls-remote` mengonfirmasi `81857196f21e0b6b6b327e32dc21570d3b21b5b2`.
- Kedua katalog hanya menampilkan sample 50 nama, bukan enumerasi penuh.
- Uji fresh on-demand di direktori kosong berhasil:
  - `npx --yes skills add PracticalSwan/agent-skills --skill frontend-design --copy --agent claude-code -y` → `Found 248 skills`, 1 skill terpasang.
  - `npx --yes skills add agent-skills-hub/agent-skills-hub --skill 3d-web-experience --copy --agent claude-code -y` → 1 skill terpasang. CLI melaporkan `Found 787 skills` dan warning satu `imagen/SKILL.md` tidak memiliki frontmatter `description`, sedangkan katalog menyatakan 797.
- CLI yang diuji: `skills 1.5.26`.

**KATALOG ON-DEMAND: TERJAMIN** — mekanisme `npx skills add <repo> --skill <nama>` terbukti dapat mengambil skill yang dipilih dari kedua katalog. Namun, angka hub **797 di katalog versus 787 yang ditemukan CLI** dan sample-only catalog harus diperbaiki/dijelaskan sebelum klaim katalog dianggap enumerasi kanonis.

## 5. Audit ZIP-vs-npx, update, dan tiga sample hash

`Input-Pengguna/` pada repo meta berisi 10 ZIP dengan total **53.813.128 bytes**. Arsip hanya folder `sistem/sistem-building-aplikasi` tidak memuat `Input-Pengguna/`; `check_selfcontained` juga menyalin hanya folder sistem dan selesai dengan 0 temuan.

Perintah dan path yang benar-benar dibandingkan:

| Sample | Path vendor di arsip target | Path hasil npx | md5 vendor | md5 npx | `cmp` |
|---|---|---|---|---|---|
| excalidraw | `/tmp/pembangun-sistem-review-01a0a48f/sistem/sistem-building-aplikasi/skills/excalidraw-diagram/SKILL.md` | `/tmp/npx-review-excalidraw/.claude/skills/excalidraw-diagram/SKILL.md` | `1b69d72e17d463772c2a9baf64d0cff2` | `1b69d72e17d463772c2a9baf64d0cff2` | **IDENTIK** |
| alibaba | `/tmp/pembangun-sistem-review-01a0a48f/sistem/sistem-building-aplikasi/skills/alibaba-java/SKILL.md` | `/tmp/npx-review-alibaba/.claude/skills/alibaba-java-coding-guidelines-skill/SKILL.md` | `7311d7906502246eba010b144e1b7f55` | `7311d7906502246eba010b144e1b7f55` | **IDENTIK** |
| frontend-designer | `/tmp/pembangun-sistem-review-01a0a48f/sistem/sistem-building-aplikasi/skills/frontend-designer/SKILL.md` | `/tmp/npx-review-frontend/.claude/skills/frontend-designer/SKILL.md` | `c776e7eb40f5fc3b2c5c727446bd65f5` | `c776e7eb40f5fc3b2c5c727446bd65f5` | **IDENTIK** |

Catatan nama upstream: repo Alibaba yang valid adalah `ns3154/alibaba-java-coding-guidelines-skill`; nama folder vendor disingkat menjadi `alibaba-java`.

### `npx skills update`

- Pada fixture npx yang memiliki instalasi provider-managed, `npx --yes skills update -p -y` berhasil memperbarui `excalidraw-diagram` dan `frontend-designer` masing-masing 1 skill.
- Pada fixture Alibaba, command exit 0 tetapi memberi warning beberapa current paths cocok dan melewati skill tersebut untuk menghindari migrasi path yang salah.
- Pada salinan bersih langsung dari folder template (`/tmp/npx-template-update`), command mengembalikan **`No project skills to update`** karena template hanya membawa `skills/` vendor-local, bukan metadata/path project-managed npx.
- Audit yang disimpan di `_sistem/AUDIT_NPX_UPDATE_2026-09-16.md:45-53` mengklaim run historis `/tmp/npx-test` memperbarui 24 skill; direktori historis itu tidak lagi tersedia untuk direproduksi. Jadi bukti independen saat ini memastikan update command hidup untuk fixture managed dan on-demand add hidup, tetapi tidak membuktikan `npx skills update` bekerja terhadap hasil `cp -r` template.

## 6. Cross-check PRD / TECH_SPEC / ROADMAP dan area risiko

| Artefak | Keadaan target | Hasil cross-check |
|---|---|---|
| `docs/PRD.md` | Belum ada; `docs/` hanya berisi `README.md` | Tidak ada PRD aplikasi untuk dibandingkan |
| `docs/TECH_SPEC.md` | Belum ada | Tidak ada TECH_SPEC aplikasi untuk dibandingkan |
| `docs/ROADMAP.md` | Belum ada | Tidak ada task aplikasi untuk dibandingkan |
| `_sistem/templates/ROADMAP.md` | Ada sebagai benih | Dapat diaudit terhadap kontrak 7 atribut; ditemukan gap M-05 |
| Area Berisiko | Didefinisikan secara generik di `AGENT_SYSTEM.md:247-260` (RLS/auth, role/permission, kalkulasi, state machine) | Tidak ada area produk konkret karena dokumen fondasi belum dibuat |

Dengan demikian, tidak tepat menyatakan cross-check semantik PRD/TECH_SPEC/ROADMAP aplikasi sudah lulus; status yang benar adalah **N/A — template starter belum memiliki artefak aplikasi**. Cross-check yang bisa dilakukan sekarang adalah kontrak template, bootstrap, path skill, checkpoint, dan mekanisme hidup.

## 7. Temuan Critical / Minor

### Critical

| ID | File:line | Temuan | Saran perbaikan |
|---|---|---|---|
| C-01 | `AGENT_SYSTEM.md:41-53`; `docs/README.md:5-14`; `PANDUAN_PENGGUNA.md:119-132` | Salinan bersih dari template tidak memiliki `PROJECT_STATE.md`, tetapi selalu memiliki `docs/README.md`. Algoritme menguji apakah `/docs` berisi “file apa pun”; akibatnya repo baru dapat salah dianggap sesi terputus dan meminta recovery dari sesi yang tidak pernah ada, bukan memulai Discovery. | Ubah deteksi menjadi “ada artefak fondasi selain `docs/README.md`”, atau sertakan `PROJECT_STATE.md` awal yang eksplisit `FONDASI_TAHAP_1_DISCOVERY` dan selaraskan semua entry point. Klarifikasi pula bahwa `/docs` berarti `docs/` relatif terhadap root repo. |
| C-02 | `_log-sesi/LOG_SESI_2026-09-15.md:3-9`; `10_LOG_SESI.md:7-16`; `STATUS.md:3-6`; `PANDUAN_PENGGUNA.md:119-134` | Folder yang dipromosikan sebagai template membawa log `OPEN` dari run meta nyata: PR #59, G-Final, branch target, dan status/ukuran lama. Bootstrap mewajibkan membaca serta melaporkan setiap log `OPEN`, sehingga repo aplikasi baru akan menerima konteks klinik/meta yang bukan miliknya. `STATUS.md` juga masih menyatakan run klinik dan “Merge PR (G-Final)” sebagai tahap berikutnya. | Jangan distribusikan log sesi live. Ganti dengan log template netral atau tandai arsip `CLOSED`/`reference_only` yang dikecualikan dari recovery; reset `STATUS.md`/manifest ke keadaan starter saat paket template dibuat. |
| C-03 | `AGENT_SYSTEM.md:121-128`; layout aktual `skills/product-discovery/skills/*/SKILL.md` dan `skills/product-management/skills/*/SKILL.md` | Mapping skill wajib menunjuk path literal yang tidak ada, misalnya `skills/product-discovery/discovery-interview-prep`, `skills/product-management/prd-development`, dan `skills/ai-agent-skills/skills/...`. Dua aggregate parent pertama sebenarnya memiliki subfolder `skills/`. Ini dapat memblokir pencarian skill wajib pada Discovery, PRD, ROADMAP, dan coding logic. | Perbaiki path menjadi path aktual, misalnya `skills/product-discovery/skills/discovery-interview-prep/SKILL.md`, atau dokumentasikan resolver `find skills/... -name SKILL.md`; tambahkan pemeriksaan path mapping ke validator. |
| C-04 | `AGENT_SYSTEM.md:80-85` dibanding `AGENT_SYSTEM.md:442-449`; `START_DI_SINI.md:27-30`; `_sistem/templates/AGENT_OPERATING_GUIDE.md:27-35` | Kontrak akhir sesi mensyaratkan state/log diperbarui lalu semua di-commit dan di-push, tetapi prosedur coding memerintahkan **commit & push pada langkah 6 lalu baru update `PROJECT_STATE.md` pada langkah 7**. Crash setelah langkah 7 meninggalkan penunjuk state lokal yang tidak tersedia untuk sesi berikutnya, bertentangan dengan jaminan anti-hilang konteks. | Satukan urutan: update `ROADMAP`, `DECISIONS_LOG`, `PROJECT_STATE`, `STATUS`, dan `LOG_SESI`; cek `git status`; lalu satu commit + push terakhir; verifikasi remote/working tree sebelum menyatakan aman. Jika tetap commit per task, wajib ada push kedua setelah state diperbarui. |
| C-05 | `AGENT_SYSTEM.md:494-498`; `START_DI_SINI.md:48-50`; `PANDUAN_PENGGUNA.md:149-153` | Mekanisme hidup A menjanjikan audit lengkap dengan `tools/validate_repo.py`, `tools/check_selfcontained.py`, dan `tools/test_failure_injection.py`, tetapi direct copy yang dinyatakan sebagai template tidak membawa folder `tools/`. Pada repo standalone, perintah wajib itu gagal dengan file tidak ditemukan; hanya validator lokal yang tersedia. | Tandai command root-tools sebagai “meta repo / bila tersedia” dan sediakan fallback audit standalone yang benar-benar ada, atau bawa salinan minimal tools yang diperlukan ke `_sistem/`. Uji mekanisme hidup dari salinan bersih, bukan hanya dari master meta. |

### Minor

| ID | File:line | Temuan | Saran perbaikan |
|---|---|---|---|
| M-01 | `SYSTEM_MANIFEST.md:76-86,98-105`; `skills/README.md:120,122,144`; `_cadangan-claude/RINGKASAN_sistem-building-aplikasi.md:1-3,14-27,43,55-64`; `STATUS.md:5,8`; `_sistem/AUDIT_ZIP_VS_NPX_2026-09-16.md:18,27` | Sinkronisasi ukuran/status belum selesai: aktual `26M/56 dirs`, tetapi banyak dokumen masih menyebut `8.1M/52 dirs`, `1.7M` selective, atau savings `85%/84%`; `_cadangan` masih menyebut 8.1M dan status validator `102/327`; audit ZIP-vs-npx masih menggambarkan snapshot prune lama. | Regenerasi ringkasan, manifest, status, README, audit, dan angka acceptance dari satu command sumber; atau label semua angka lama sebagai historical snapshot dengan tanggal/commit yang jelas. Jangan membandingkan `du` direktori dengan ukuran ZIP terkompresi tanpa definisi baseline. |
| M-02 | `skills/agent-skills/CATALOG.md:1-7`; `skills/agent-skills-hub/CATALOG.md:1-7`; `skills/agent-skills*/README.md:3`; hasil npx CLI 1.5.26 | Catalog hub menyatakan 797, tetapi fresh npx discovery menemukan 787 dan melewati `imagen/SKILL.md` karena frontmatter wajib hilang. Kedua katalog juga hanya mencetak 50 nama sample, bukan daftar 248/797 lengkap; README subcatalog menyebut jumlah sample yang berbeda. | Regenerasi catalog dari HEAD yang sama dengan versi CLI yang didokumentasikan; pisahkan `total directory`, `installable SKILL.md`, dan `invalid/skipped`; nyatakan sample-only secara eksplisit atau simpan manifest penuh. |
| M-03 | `skills/README.md:119,134`; `_sistem/AUDIT_NPX_UPDATE_2026-09-16.md:3,45-53`; `PANDUAN_PENGGUNA.md:132-134` | `npx skills update` tidak menemukan project skills pada salinan langsung template karena skill disimpan sebagai vendor-local `skills/` tanpa metadata npx. Audit historical di `/tmp/npx-test` menguji fixture berbeda. Selain itu updater dapat melewati skill dengan duplicate paths. Klaim “semua skill publik bisa auto-update” terlalu luas untuk template copy. | Dokumentasikan jalur update yang benar untuk vendor-local (`npx skills add ... --skill ...` lalu sync/copy), atau sertakan metadata/path managed dan test clean-copy; laporkan skip sebagai caveat operasional, bukan sekadar “tidak error”. |
| M-04 | `SYSTEM_MANIFEST.md:79,114-117`; `skills/README.md:111,120`; `_sistem/AUDIT_NPX_UPDATE_2026-09-16.md:23-24,57`; `PANDUAN_PENGGUNA.md:132-134` | Teks menyebut 10 repo/18 skill AI seolah seluruhnya installable, tetapi bukti npx sendiri menyatakan 9/10 repo berhasil dan `Gak6900/awesome-frontend-skills` adalah curated list tanpa `SKILL.md`; aktual `ai-agent-skills` memiliki 17 nested `SKILL.md`, bukan 18. | Gunakan istilah “10 sumber publik; 9 installable + 1 katalog” dan koreksi hitungan 17/18 dengan definisi yang eksplisit. |
| M-05 | `AGENT_SYSTEM.md:306-338`; `_sistem/templates/ROADMAP.md:5-15`; `SYSTEM_MANIFEST.md:105`; `PANDUAN_PENGGUNA.md:132` | `AGENT_SYSTEM` mewajibkan 7 atribut per task (Tujuan, Ref, File, DoD, Kompleksitas, Risiko/mitigasi, Verifikasi), tetapi contoh task di template ROADMAP hanya memberi ref/kompleksitas dan tidak memuat file, DoD, verifikasi, serta risiko. Klaim template “7 file” juga mengabaikan template tambahan `LOG_SESI.md`, `PROFIL_PENGGUNA.md`, dan `STATUS.md` yang aktualnya membuat 10 file. | Jadikan contoh ROADMAP benar-benar memenuhi 7 atribut dan ubah checklist/count template menjadi 10 atau jelaskan pembagian core versus lifecycle templates. |
| M-06 | `AGENT_SYSTEM.md:340-342` | Instruksi “Setelah user setujui...” untuk commit ROADMAP dan update PROJECT_STATE diulang identik dua kali. | Hapus satu blok dan tambahkan regression check untuk duplicate instruction. |
| M-07 | `PANDUAN_PEMAKAIAN.md:3-5,25-34`; `PANDUAN_PENGGUNA.md:117-134`; `SYSTEM_MANIFEST.md:98` | Panduan legacy mengatakan file itu bukan untuk agent dan “yang masuk ke repo hanya `AGENT_SYSTEM.md`”, serta memiliki prompt lama; panduan baru menyuruh menyalin seluruh folder. Manifest masih mencantumkan panduan legacy sebagai dokumen wajib. | Arsipkan/keluarkan panduan legacy dari paket direct-copy atau ubah menjadi redirect satu paragraf ke `PANDUAN_PENGGUNA.md`; jangan menyimpan dua kontrak entry yang berbeda. |
| M-08 | `ACCEPTANCE_TEST_LOG.md:16-31`; `REVIEW_PROMPT_2026-09-16.md:6,17-18`; `REVIEW_SIMULASI_2026-09-16.md:1-4,31-42` | Acceptance log masih merekam `102 docs/327 refs`, 0 warning, dan log `CLOSED`, sedangkan rerun HEAD terbaru menghasilkan `104 docs/336 refs` dan 2 warning; review prompt/simulasi juga mem-pin HEAD lama. Ini melemahkan reproducibility dan dapat membuat reviewer mengaudit object yang salah. | Tambahkan commit SHA ke setiap run, refresh evidence setelah setiap head berubah, dan tandai laporan lama sebagai historical snapshot. |
| M-09 | `_sistem/AUDIT_NPX_UPDATE_2026-09-16.md:37`; output `tools/validate_repo.py` | Dua path di tabel hash adalah label ilustratif tetapi ditulis sebagai code path sehingga validator repo menganggapnya unresolved. Exit 0 tetap PASS, tetapi coverage menghasilkan noise dan bertentangan dengan klaim 0 warning. | Gunakan label seperti `<npx output>/...` dan `vendor skills/...` tanpa token path yang resolver anggap literal, atau tambah aturan validator untuk kolom bukti audit. |
| M-10 | `AGENT_SYSTEM.md:498`; `_salinan-meta/PLATFORM_LMARENA.md:14-27`; `AGENT_SYSTEM.md:23-29` | Mekanisme hidup menyuruh membuka branch bernama `sistem-audit-YYYY-MM-DD`, sedangkan fakta platform menyatakan branch otomatis `arena/...` dan aturan global memerintahkan bekerja pada branch sesi. Ini dapat membuat agent mencoba pindah branch yang tidak diasosiasikan dengan sesi. | Nyatakan bahwa audit memakai branch yang diberikan platform; gunakan nama deskriptif hanya jika platform mengizinkan, dan jangan `switch`/push ke branch lain tanpa prosedur resmi. |

## 8. Mekanisme hidup — hasil audit

**Ada dan dikenali:**

- Trigger natural language A/B terdokumentasi di `AGENT_SYSTEM.md:482-532`.
- Jalur sistem meta mencakup baca manifest/status/log, validator, laporan severity, approval, branch/PR tanpa auto-merge.
- Jalur aplikasi pasca-rilis mencakup Cross-Check, task ROADMAP baru, dan siklus 0.5/v2.
- Aturan keputusan berisiko, checkpoint, `PROJECT_STATE`, `STATUS`, dan `LOG_SESI` tersedia.

**Belum aman sebagai mekanisme operasional penuh:**

- C-04 membuat state terakhir dapat tertinggal di remote.
- C-05 membuat audit lengkap tidak dapat dijalankan dari direct-copy standalone.
- C-02 membuat recovery membaca konteks meta yang salah.
- M-10 membuat branch audit tidak selaras dengan fakta platform.

## 9. Kesimpulan wajib

### TEMPLATE SELF-CONTAINED: PASS

Pass ini berlaku untuk HEAD terbaru `44cfd3a`: validator lokal PASS dan `check_selfcontained.py --sistem/--semua` PASS. Ini tidak menghapus Critical workflow findings di atas. Snapshot lama `e3a8cf1` masih FAIL pada self-prefix; commit `44cfd3a` memperbaikinya.

### KATALOG ON-DEMAND: TERJAMIN

Terjamin untuk mekanisme fetch skill terpilih yang diuji langsung dengan `npx skills add` pada sumber 248 dan hub; tidak berarti angka hub 797 sudah tervalidasi sebagai jumlah installable (CLI menemukan 787), dan tidak berarti `npx skills update` otomatis bekerja pada folder vendor-local hasil copy template.

**Rekomendasi review:** gerbang teknis self-contained hijau, tetapi PR belum layak dinyatakan hijau penuh sebelum C-01 sampai C-05 ditangani atau secara eksplisit diterima pemilik dengan keputusan terdokumentasi. 
