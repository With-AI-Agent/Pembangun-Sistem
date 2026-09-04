# Platform lmarena — Fakta vs Policy

Dokumen ini menjelaskan batasan fisik platform lmarena Agent Mode yang mempengaruhi cara membangun dan memakai sistem apapun di repo ini. Tujuannya agar agent tidak salah asumsi — tahu mana yang **tidak bisa** karena platform, mana yang **sebaiknya jangan** karena policy kita.

Sumber resmi: help.arena.ai/articles/5432423882-how-to-use-agent-mode (diakses 2026-09-04)

---

## Fakta Platform (tidak bisa / otomatis — bukan aturan kita)

### 1. Branch kerja otomatis

**Fakta:** Saat sesi lmarena dimulai, kamu boleh pilih base branch (misal `main`) di UI, tapi setelah itu lmarena **otomatis** membuat branch baru `arena/[id]-...` dan semua kerja agent terjadi di branch tersebut. Ini perilaku platform, bukan pilihan kita.

**Akibat:**
- Branch aktif yang perlu diverifikasi adalah `arena/...`, bukan `main`.
- `main` hanya berubah setelah PR di-merge.
- Jika agent mengasumsikan kerja di `main` langsung, maka commit-nya tidak akan ada di `main` dan akan hilang saat sesi berganti.

**Kenapa penting:** Agent harus cek `git branch --show-current` di awal sesi, bukan asumsi.

### 2. Kehilangan akses push setelah merge/close

**Fakta:** Setelah PR di-merge atau di-close, platform mencabut token push untuk sesi tersebut. Dokumen resmi: *"Once the pull request is merged or closed, the session can no longer push to GitHub. Any files created after that point stay in the session but can't be pushed, downloaded, or carried into a new session."*

**Akibat:**
- Sesi tersebut **tidak bisa** push lagi, bukan "sebaiknya jangan". Push akan gagal secara teknis.
- File yang dibuat setelah merge akan terjebak di sesi dan tidak bisa dibawa ke sesi baru.
- Workaround resmi jika sudah terlanjur: tambah `/download-workspace` di akhir URL sesi untuk download zip workspace (tidak bisa push, tapi masih bisa download).

**Kenapa penting:** Jika user merge PR dari sesi A, lalu lanjut chat di sesi A yang sama, kerjaan barunya hilang. Harus buka sesi baru dari `main`.

### 3. Sesi bisa menjadi unusable di tengah jalan

**Fakta:** Arena sendiri mengakui sesi kadang menjadi unusable (chat tidak bisa lanjut, error halaman keluar sendiri). Mereka sediakan workaround download workspace sebagai mitigasi.

**Akibat:**
- Diskusi panjang yang belum jadi file + commit bisa hilang jika sesi crash.
- File di workspace yang belum commit/push belum aman untuk sesi baru (sesuai FI-03).

**Kenapa penting:** Protokol checkpoint harus memperhitungkan crash platform, bukan hanya kesalahan agent.

---

## Policy Sistem (harus / sebaiknya — aturan kita dengan alasan kausal)

Policy ini dibuat **karena** fakta platform di atas, bukan aturan sembarang.

### P1 — Commit tiap tahap besar selesai

**Policy:** Setelah satu tahap besar selesai (misal Capture, Extract, Structure, atau satu dokumen brief selesai), agent harus commit + push sebelum menyatakan tahap tersedia untuk sesi baru.

**Alasan kausal:** Karena fakta #3 (sesi bisa crash) dan fakta #2 (file workspace belum aman), maka tanpa commit, sesi baru **tidak bisa** melanjutkan. Ini mencegah FI-03.

### P2 — Checkpoint diskusi ringan

**Policy:** Jika diskusi sudah >5-7 giliran dan mendekati keputusan, agent harus buat file draft `DISKUSI_MENTAH_YYYY-MM-DD_HHMM.md` di `unit-aktif/[id]/` atau `_meta/_internal/discussions/` berisi ringkasan diskusi, opsi yang dipertimbangkan, keputusan yang hampir diambil, pertanyaan terbuka. Status `in-progress`, commit dengan pesan `checkpoint diskusi: ...`

**Alasan kausal:** Karena fakta #3, diskusi panjang yang belum jadi file final bisa hilang. Checkpoint ringan ini menyelamatkan konteks tanpa harus log semua chat (efisien vs aman). Ini menutup rasa "sedih diskusi panjang hilang".

**Kapan tidak perlu:** Diskusi pendek <3 giliran atau masih eksplorasi awal — tidak perlu checkpoint, cukup lanjut chat.

### P3 — Verifikasi branch dan PR di awal sesi

**Policy:** Di awal sesi baru, agent harus cek `git branch --show-current`, `git log --oneline -3`, dan `gh pr list --state open`.

**Alasan kausal:** Karena fakta #1 (branch otomatis), agent tidak boleh asumsi branch. Karena fakta #2, jika PR sudah merge tapi sesi lama masih dipakai, push akan gagal. Verifikasi mencegah mismatch (FI-04).

### P4 — Jangan lanjut kerja di sesi yang PR-nya sudah merge

**Policy:** Jika `gh pr list` menunjukkan PR dari branch aktif sudah MERGED/CLOSED, maka sesi ini tidak boleh dipakai untuk kerja baru. Harus buka sesi baru dari `main`.

**Alasan kausal:** Karena fakta #2 (tidak bisa push setelah merge). Ini bukan larangan moral, tapi konsekuensi fisik.

---

## Bagaimana menanam di sistem yang dihasilkan

Setiap sistem domain yang akan dipakai via lmarena harus memiliki bagian "Batasan Platform" di manifest atau entry point-nya:

```markdown
## Batasan Platform

- **Dipakai via lmarena?** Ya
- **Jika Ya:** rujuk ke `_meta/PLATFORM_LMARENA.md` untuk fakta platform. Terapkan P1-P4 sesuai bentuk sistem ini (bertinjkat/flat/siklus).
- **Jika Tidak:** tulis alasan override eksplisit (misal: sistem ini manual 100% Obsidian, tidak via agent)
```

Untuk sistem baru, pertanyaan ini ditanyakan di Discovery Level-0 (lihat `01_DISCOVERY_LEVEL_0.md`).

Untuk sistem existing (konten kreator, catatan belajar), bagian ini ditambahkan di `00_CARA_PAKAI_SISTEM.md` atau `WORKFLOW.md`.

---

## Override

Jika sebuah sistem memang tidak dipakai via lmarena sama sekali, maka fakta platform di atas tidak berlaku untuk sistem tersebut. Override harus dicatat di manifest sistem dengan alasan, dampak, dan approval — sesuai `QUALITY_ASSURANCE_AND_EVOLUTION.md`. "Tidak dilakukan karena lupa" bukan override valid.

---

## Log Keputusan

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-04 | Buat dokumen ini | Menutup gap asumsi agent tentang lifecycle sesi lmarena, setelah observasi pengguna dan verifikasi docs resmi Arena. Fakta platform sebelumnya tidak eksplisit di meta, menyebabkan risiko file terjebak setelah merge dan diskusi hilang saat crash. |
| 2026-09-04 | Bedakan fakta (tidak bisa/otomatis) vs policy (harus/jangan + alasan kausal) | Agar agent tidak salah kalibrasi — tahu mana yang tidak bisa secara fisik vs mana yang sebaiknya jangan karena risiko. Sesuai prinsip Log Keputusan di 02_PRINSIP_UNIVERSAL.md. |
