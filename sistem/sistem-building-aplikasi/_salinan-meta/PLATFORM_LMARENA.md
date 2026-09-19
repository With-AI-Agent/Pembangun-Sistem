> Salinan turunan. Sumber: _meta/PLATFORM_LMARENA.md sha 1b7b88ba45b94eb4191db002baba3cf8e31cb624 tanggal 2026-09-19 versi-meta 1.35.0
> Perbedaan: tidak ada
> Pemakaian: fakta platform yang dirujuk bagian Batasan Platform manifest sistem ini (butir W-07) — dibawa agar folder ini berdiri sendiri tanpa _meta/.
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

### 4. Jaringan sesi dibatasi ke allowlist — hanya registry paket + GitHub

**Fakta:** Proses yang berjalan **di dalam sesi agent** hanya bisa menjangkau sebagian kecil host. Diukur
2026-09-17 (18 host, `curl`), bukan diasumsikan:

- **✅ Terjangkau:** `registry.npmjs.org` · `pypi.org` · `api.github.com` (via `gh`, terautentikasi) ·
  `github.com` (web + `git clone`/`push`/`fetch`)
- **❌ Terblokir** — gejala seragam `curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL`, HTTP `000`:
  `skills.sh` · `raw.githubusercontent.com` · `fonts.google.com` · `fonts.gstatic.com` · `api.cloudflare.com` ·
  `dash.cloudflare.com` · `developers.cloudflare.com` · `api.supabase.com` · `api.vercel.com` ·
  `api.whatsapp.com` · `graph.facebook.com` · `midtrans.com` · `api.qrserver.com` · `unpkg.com` ·
  `cdn.jsdelivr.net` · `objects.githubusercontent.com` · `google.com` · `remotion.dev`

**Akibat:**
- **CLI cloud tidak bisa dipakai untuk memublikasikan.** `wrangler deploy`, `vercel deploy`, dan sejenisnya
  **tidak bisa** dijalankan agent dari sesi karena API-nya terblokir. Jalur publikasi yang tetap hidup =
  **`git push` ke GitHub → hosting membangun otomatis**. Penyambungan awal hosting↔GitHub adalah
  **tindakan pengguna di browser**, bukan kerja agent.
- **`npx skills find` GAGAL-DIAM.** Mengembalikan "No skills found" untuk kueri apa pun — termasuk kueri yang
  pasti ada hasilnya (`react`, `nextjs`) — karena registry `skills.sh` tak terjangkau. **Berbahaya justru karena
  keluarannya terlihat seperti jawaban yang sah** ("tidak ada skill untuk X"), padahal alatnya yang mati.
  **Wajib uji kontrol** sebelum menyimpulkan apa pun dari alat ini.
- **Aset dari CDN tidak bisa diunduh/diuji di sesi.** Font dan library **wajib dibundel lokal**. Jalur terbukti:
  paket npm **`@fontsource/*`** (diverifikasi `@fontsource/playfair-display` v5.3.0 tersedia). Ini sekaligus
  self-hosting yang memang lebih cepat dan lebih aman untuk privasi.
- **WAKTU-PAKAI ≠ WAKTU-BANGUN.** Yang terblokir adalah **proses di sesi agent**. **Browser pengguna akhir
  tidak terblokir**, jadi aplikasi yang sudah tayang **tetap bisa** memanggil API eksternal (database, auth,
  WhatsApp). Konsekuensinya: provisioning (membuat database, memasang secret) = **tindakan pengguna di browser**;
  agent menyiapkan kode + migrasi + instruksinya.

**Kenapa penting:** Alat platform **`web_search`/`fetch_page` tetap berfungsi** karena jalurnya berbeda dari
`curl` proses sandbox — jadi riset internet tetap bisa dijalankan. Tetapi **mekanisme apa pun yang dirancang
bergantung pada `curl`/`wget` ke situs umum akan gagal**, dan gagal dengan cara yang mudah disalahartikan
sebagai "situsnya yang error". Aturan yang mewajibkan agent "riset internet" **wajib menyebut alat platform**,
bukan perintah shell.

### 5. Riwayat git lokal bisa terpotong atau ter-reset DI TENGAH sesi

**Fakta:** Dalam **satu** sesi (2026-09-17, branch `arena/01a0ae7a-pembangun-sistem`) terjadi **tiga kali**:
1. HEAD branch lokal **ter-reset ke basis sesi** sementara working tree dipertahankan → commit yang sudah
   ter-push dan terverifikasi ada di server **tidak lagi terlihat di riwayat lokal**, dan push berikutnya
   ditolak `! [rejected] … (fetch first)`.
2. **Pola yang sama terulang** di giliran lain (4 commit "hilang" dari riwayat lokal, utuh di server).
3. **`.git/shallow` muncul kembali** di antara giliran padahal sudah di-unshallow di awal sesi →
   `origin/main` hanya terlihat **1 commit**, `git merge-base HEAD origin/main` **kosong**, dan `git merge`
   ditolak **"refusing to merge unrelated histories"**.

**Akibat:**
- **Tidak ada konten yang hilang** pada ketiga kejadian — yang rusak adalah **posisi HEAD** dan **kedalaman
  riwayat**. Keduanya bisa dipulihkan tanpa force-push.
- Gejala ini **menyerupai** konflik kerja nyata, jadi mudah salah diobati. **`git merge --allow-unrelated-histories`
  adalah obat yang SALAH** untuk kejadian #3: itu menyembunyikan penyebabnya dan berisiko menimpa sejarah.
- `git pull --rebase` juga **bukan** obat yang aman di sini: berkas log yang sama akan bentrok add/add.

**Kenapa penting:** Karena kejadian ini **berulang dalam satu sesi**, pemeriksaan riwayat **tidak cukup dilakukan
sekali di awal sesi** — harus dilakukan **sebelum tiap operasi yang bergantung riwayat**. Lihat policy **P6**.

---

## Policy Sistem (harus / sebaiknya — aturan kita dengan alasan kausal)

Policy ini dibuat **karena** fakta platform di atas, bukan aturan sembarang.

### P1 — Commit tiap tahap besar selesai

**Policy:** Setelah satu tahap besar selesai (misal Capture, Extract, Structure, atau satu dokumen brief selesai), agent harus commit + push sebelum menyatakan tahap tersedia untuk sesi baru.

**Alasan kausal:** Karena fakta #3 (sesi bisa crash) dan fakta #2 (file workspace belum aman), maka tanpa commit, sesi baru **tidak bisa** melanjutkan. Ini mencegah FI-03.

### P2 — Log sesi berkelanjutan (`LOG_SESI`)

**Policy:** Setiap sesi memelihara file `LOG_SESI_YYYY-MM-DD.md` di folder scope kerja (unit, sistem, atau folder `_log-sesi/` untuk level repo/meta; format `TEMPLATE_LOG_SESI.md`). Agent append + update header "Keadaan Sesi" + commit + push **segera setelah tiap pertukaran yang menghasilkan informasi baru**. Yang dicatat: keputusan/koreksi/kendala/preferensi pengguna (near-verbatim), proposal penting + dasarnya, kesepakatan & penolakan + alasan, fakta terverifikasi, state kerja, pertanyaan terbuka. Yang TIDAK dicatat: konfirmasi, basa-basi, ulang isi `STATUS.md`/Log (tunjuk path), dump chat. Akhir sesi: header ditandai `CLOSED` (atau `OPEN` + "dilanjutkan di mana"). Entry point sesi baru: cari log terbaru; yang `OPEN` wajib dibaca dan keadaannya dilaporkan + dikonfirmasi ke pengguna.

**Alasan kausal:** Karena fakta #3 (sesi bisa crash, kadang tidak bisa dibuka lagi) dan karena agent sesi baru tidak punya akses ke chat sesi lama, maka konteks yang tidak segera jadi file **hilang permanen**. Mekanisme ini adalah pencatatan sebagai mode normal, bukan checkpoint darurat: aturan lama (checkpoint >5 giliran mendekati keputusan) diganti karena berbasis ambang+judgment — sebelum ambang tercapai, tidak ada yang tercatat, dan diskusi eksploratif tidak selalu "mendekati" keputusan.

**Anti-overkill (bagian dari policy, bukan anjuran):** filter "yang dicatat / yang tidak dicatat" di atas WAJIB dipatuhi. Biaya over-recording = detik per pertukaran; biaya under-recording = jam konteks yang hilang. Floor-nya tetap aman: bahkan pencatatan minimum (keputusan + keadaan) sudah menyelamatkan 90% nilai.

**Kapan file tidak perlu dibuat:** sesi tanpa informasi baru (mis. cek status lalu selesai).

### P3 — Verifikasi branch dan PR di awal sesi

**Policy:** Di awal sesi baru, agent harus cek `git branch --show-current`, `git log --oneline -3`, dan `gh pr list --state all --limit 20`.

**Alasan kausal:** Karena fakta #1 (branch otomatis), agent tidak boleh asumsi branch. Karena fakta #2, jika PR sudah merge tapi sesi lama masih dipakai, push akan gagal. Verifikasi mencegah mismatch (FI-04). **Perintahnya wajib `--state all`, bukan `--state open`** — P4 harus bisa MENGLIHAT PR branch aktif yang sudah MERGED/CLOSED, dan itu tidak pernah muncul di daftar `open` (dibetulkan di audit meta 5 Sep 2026, temuan M-04; dua sesi nyata 4–5 Sep terpaksa memakai `--state all` untuk bekerja benar).

### P4 — Jangan lanjut kerja di sesi yang PR-nya sudah merge

**Policy:** Jika `gh pr list` menunjukkan PR dari branch aktif sudah MERGED/CLOSED, maka sesi ini tidak boleh dipakai untuk kerja baru. Harus buka sesi baru dari `main`.

**Alasan kausal:** Karena fakta #2 (tidak bisa push setelah merge). Ini bukan larangan moral, tapi konsekuensi fisik.

### P5 — Desain untuk allowlist jaringan, bukan untuk internet bebas

**Policy:** Setiap sistem yang dibangun di repo ini **wajib mengasumsikan fakta #4**. Konkret: (a) publikasi lewat
**git push + build otomatis di sisi hosting**, bukan lewat CLI cloud; (b) **semua aset dibundel lokal** (font via
`@fontsource/*` atau berkas di repo), **dilarang** bergantung CDN saat bangun; (c) API pihak ketiga hanya boleh
dipanggil dari **waktu-pakai** (browser pengguna akhir), **tidak pernah** dari alat/perintah yang dijalankan agent
di sesi; (d) aturan yang mewajibkan "riset internet" **wajib menyebut alat platform** (`web_search`/`fetch_page`),
bukan `curl`/`wget`; (e) sebelum menyimpulkan apa pun dari alat yang mengakses jaringan, **jalankan uji kontrol**
dengan masukan yang pasti berhasil.

**Alasan kausal:** Karena fakta #4, desain yang mengasumsikan internet bebas **akan gagal di produksi** — dan
gagalnya sering **diam** (contoh nyata: `npx skills find` mengembalikan "No skills found", yang terbaca seperti
jawaban sah). Desain untuk jalur terbatas **tetap benar** di lingkungan yang lebih bebas, tetapi tidak sebaliknya.
Jadi memilih jalur ketat **tidak punya biaya** dan **menghilangkan** satu kelas kegagalan.

### P6 — Tiga pemeriksaan sebelum operasi yang bergantung riwayat

**Policy:** Sebelum **operasi apa pun yang bergantung riwayat git** (merge, rebase, `merge-base`, cek leluhur,
`git log` lintas-branch, dan **sebelum setiap commit**), agent **wajib** memeriksa tiga hal:
1. `git rev-parse --is-shallow-repository` → **harus `false`**
2. HEAD lokal **mengandung** sha remote branch sesi → `git ls-remote --heads origin <branch>` lalu
   `git merge-base --is-ancestor <sha-remote> HEAD`
3. `git rev-list --count origin/main` → **masuk akal** (ratusan, bukan 1)

Kalau salah satu gagal: **pulihkan dulu** — `git fetch --unshallow --prune` untuk shallow, atau
`git fetch` + **`git reset --mixed <sha remote>`** untuk HEAD yang ter-reset (`--mixed`, **bukan** `--hard`:
working tree tidak boleh disentuh). **Verifikasi byte-identik** sebelum commit ulang. **Dilarang** memakai
`--allow-unrelated-histories` atau `pull --rebase` untuk mengatasi gejala ini.

**Alasan kausal:** Karena fakta #5, riwayat lokal **tidak bisa dipercaya** hanya karena tadi sudah diperiksa.
`reset --mixed` memindahkan HEAD **tanpa** menyentuh working tree, jadi pemulihan **tidak bisa** menghilangkan
pekerjaan yang belum ter-commit — inilah sebabnya itu satu-satunya jalur yang diizinkan. Tiga kejadian nyata di
satu sesi (2026-09-17) semuanya pulih **tanpa kehilangan satu byte pun** dan **tanpa force-push**, karena
prosedur ini diikuti.

---

## Bagaimana menanam di sistem yang dihasilkan

Setiap sistem domain yang akan dipakai via lmarena harus memiliki bagian "Batasan Platform" di manifest atau entry point-nya:

```markdown
## Batasan Platform

- **Dipakai via lmarena?** Ya
- **Jika Ya:** rujuk ke `_meta/PLATFORM_LMARENA.md` untuk **5** fakta platform. Terapkan **P1–P6** sesuai bentuk sistem ini (bertinjkat/flat/siklus).
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
| 2026-09-17 | **Fakta platform #4 (allowlist jaringan) + #5 (riwayat git bisa terpotong/ter-reset di tengah sesi) DITAMBAH**; policy **P5** (desain untuk allowlist) + **P6** (3 pemeriksaan sebelum operasi bergantung riwayat) ditambahkan; bagian "Bagaimana menanam" diperbarui dari 3 fakta/P1-P4 jadi **5 fakta/P1–P6** | Keduanya **diukur/dialami langsung** di sesi `arena/01a0ae7a-pembangun-sistem` 2026-09-17, bukan dugaan: #4 dari uji `curl` ke 18 host (bukti: berkas _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian M — ditulis tanpa backtick sebagai provenance, karena dokumen kerja internal sesi ini memang TIDAK disalin ke folder sistem); #5 dari **3 kejadian nyata dalam satu sesi** (2× HEAD ter-reset, 1× `.git/shallow` muncul lagi → merge ditolak). Ditemukan saat audit (temuan X-01/X-02 di berkas _meta/_internal/AUDIT_MANUAL_DAN_MEKANISME_REVIEW_2026-09-17.md (provenance tanpa backtick, alasan sama)): dokumen ini sebelumnya hanya memuat 3 fakta dan **tidak menyebut allowlist sama sekali**, padahal pemilik mengonfirmasi produksi = lmarena — jadi ini batasan produksi nyata. `npx skills find` dicatat khusus karena **gagal-diam**: keluarannya terlihat seperti jawaban sah |
| 2026-09-04 | Bedakan fakta (tidak bisa/otomatis) vs policy (harus/jangan + alasan kausal) | Agar agent tidak salah kalibrasi — tahu mana yang tidak bisa secara fisik vs mana yang sebaiknya jangan karena risiko. Sesuai prinsip Log Keputusan di 02_PRINSIP_UNIVERSAL.md. |
