# Template Pegangan Pengguna — Sistem [Nama Sistem]

> Template untuk `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` setiap sistem yang dibangun di repo ini. **WAJIB** ada di dalam folder sistem itu sendiri (self-contained — ikut terbawa kalau sistem diunduh jadi repo standalone; lihat `00_CARA_KERJA_META.md`, prinsip pegangan pengguna).
>
> **Aturan dua file:**
> 1. `PROMPT_ENTRI_UNIVERSAL.md` di root folder sistem — berisi **satu blok prompt pembuka** siap tempel + catatan pemakaian singkat. (Agent: file ini adalah sumber prompt pembuka; isinya boleh dirujuk dokumen sistem lain.)
> 2. `PANDUAN_PENGGUNA.md` (root folder sistem, atau subfolder `panduan/`) — pegangan lengkap bagi **pengguna**. Tandai jelas di awal: `agent_instruction: IGNORE for execution — USER GUIDE ONLY`. Agent **tidak boleh** memperlakukannya sebagai instruksi eksekusi kecuali diminta eksplisit.
>
> Standar yang dikejar: **sama mudahnya dipakai dengan meta-sistem ini sendiri** — pengguna cukup menempel SATU prompt pembuka, lalu agent otomatis terorientasi penuh (apa sistemnya, cara kerja, ketentuan, kondisi repo, PR menggantung) tanpa perlu ditempel manual.

---

## STANDAR KELULUSAN MANUAL — 5 syarat yang membuat pegangan boleh disebut selesai

> Ditambahkan 17 Sep 2026 atas tuntutan pemilik setelah bukti lapangan: manual sistem lain terbukti
> *"prompt tanpa panduan"*, *"tabel perintah tanpa penjelasan fungsi dan cara"*, dan ada kalimat yang
> *"ditujukan ke pengguna, bukan ke agent"*. Standar kelulusannya dirumuskan pemilik sendiri:
> **"bisa dipakai orang awam tanpa bertanya lagi."**
> **Acuan bentuk yang sudah terbukti ada di repo ini:** pegangan sistem-presentasi (sistem/sistem-presentasi/PANDUAN_PENGGUNA.md — ditulis tanpa backtick sebagai provenance: berkas di dalam folder sistem tidak ikut ke ekstrak template bootstrap, dan rujukan ber-backtick ke sana akan menggeser pin R7 di tools/test_failure_injection.py)
> (0 temuan bug/ambiguitas saat audit 17 Sep: punya frontmatter, pembuka "Apa ini", dan §review dengan
> 5 langkah bernomor termasuk peringatan pasca-merge + jalur unduh berkas). **Jangan mengarang bentuk baru
> kalau yang ini sudah cukup.**

### Syarat 1 — setiap MEKANISME wajib punya 6 bidang

Satu prompt saja **tidak cukup**. Prompt tanpa prosedur membuat pengguna menempel kalimat lalu tidak tahu
apa yang seharusnya terjadi, dan tidak tahu apa yang harus dilakukan kalau hasilnya aneh.

| # | Bidang | Pertanyaan yang dijawab |
|---|---|---|
| 1 | **Apa** | mekanisme ini apa, dalam 1–2 kalimat bahasa awam |
| 2 | **Kapan** | situasi yang membuatnya perlu dipakai |
| 3 | **Cara** | langkah bernomor — bukan paragraf |
| 4 | **Prompt siap tempel** | blok berpagar, utuh, tanpa bagian yang harus dikarang sendiri |
| 5 | **Sesudahnya** | apa yang akan terjadi setelah prompt ditempel — supaya pengguna bisa mengenali hasil normal |
| 6 | **Kalau gagal** | gejala gagalnya apa, dan langkah pertamanya apa |

**Uji cepat:** tutup bidang 3, 5, dan 6. Kalau pembaca masih bisa memakai mekanismenya tanpa bertanya,
bidang itu memang tidak perlu. Kalau tidak bisa — **bidang itu wajib diisi**, bukan dihapus.

### Syarat 2 — setiap PERINTAH MESIN wajib punya 5 kolom

Tabel perintah yang hanya berisi perintah adalah tabel yang **terlihat rapi tetapi tidak bisa dipakai**.

| Kolom | Isi |
|---|---|
| **Perintah** | persis seperti yang diketik, siap salin |
| **Fungsi** | untuk apa — bukan terjemahan nama perintahnya |
| **Kapan dipakai** | situasi pemakaiannya |
| **Keluaran diharapkan** | apa yang muncul kalau berhasil, supaya berhasil bisa dikenali |
| **Kalau gagal** | gejala + langkah pertama |

Perintah di dalam blok `bash` pun wajib diberi **komentar penjelasan di barisnya**, bukan hanya disebut.

### Syarat 3 — ATURAN ARAH BICARA (paling sering dilanggar, dan bisa diperiksa alat)

Tiga aturan, masing-masing dengan alasan kausal:

1. **Blok prompt yang akan ditempel ke agent wajib berkalimat PERINTAH KE AGENT** — "baca…", "verifikasi…",
   "jalankan…", "laporkan…", "jangan…".
   **Dilarang** berkalimat ke manusia di dalam blok itu: "kamu bisa…", "silakan…", "Anda akan…".
   *Alasan:* prompt yang salah arah membuat agent mengira sedang membaca **penjelasan**, bukan **instruksi** —
   dan agent bisa tidak mengerjakan apa pun sambil tetap terdengar meyakinkan.
2. **Prosa dokumen DILARANG bersuara orang-pertama agent** — "aku", "ku-", "menurutku", "usulanku",
   "aku jujur", "kamu benar".
   *Alasan:* itu **residu chat** yang membeku jadi isi dokumen. Ia merujuk percakapan yang tidak ada di
   dokumen ("ide kamu ini" — ide yang mana?), dan tidak bisa kedaluwarsa secara terlihat.
   **Bukti nyata:** audit 17 Sep menemukan 2 baris seperti ini di pegangan sistem-building-aplikasi
   (temuan F-05; nama berkas disebut tanpa backtick — alasan sama seperti di atas).
3. **Bagian yang harus diisi pengguna wajib ditandai sebagai placeholder** — bentuk `[...]` atau `<...>`,
   dan disebut di kalimat sebelumnya. *Alasan:* tanpa tanda, pengguna menempel prompt yang masih bolong
   dan agent akan menebak.

**Pengecualian yang sah** (jangan salah tangkap): di dalam blok prompt, kata **"aku" memang benar** kalau itu
**suara pengguna** yang menempel — contoh: *"jangan mulai eksekusi sebelum **aku** konfirmasi tujuan sesi ini"*.
Yang dilarang adalah **"aku" di prosa dokumen**, dan **"kamu" yang menunjuk manusia di dalam blok prompt**.

### Syarat 4 — kelulusan TIDAK BOLEH dinyatakan sendiri oleh penulisnya

Standar lulusnya **bukan** "sudah lengkap", melainkan: **"bisa dipakai orang awam tanpa bertanya lagi."**

- Penulis (agent yang membuat pegangan) **dilarang** menyatakan standar ini terpenuhi.
- **Wajib** diaudit oleh **sesi independen** memakai **lensa #5** `QUALITY_ASSURANCE_AND_EVOLUTION.md`
  (*kemudahan pakai — kacamata pengguna awam*).
- **Uji pemakaian nyata lebih kuat daripada audit:** pemilik menjalankan **satu alur** dari pegangan itu
  tanpa bertanya. Kalau pemilik harus bertanya, **standarnya belum lulus** — dan pertanyaannya itu sendiri
  adalah temuan yang wajib dicatat.
- **Batas kejujuran:** agent **bukan** orang awam. Audit agent hanya bisa menyaring cacat bentuk;
  kelulusan sesungguhnya tetap butuh manusia.

### Syarat 5 — SATU SUMBER, jangan duplikasi di dalam dokumen yang sama

**Dilarang menyalin tabel/blok/daftar dua kali di dalam satu dokumen** (misalnya tabel "Situasi" yang sama
muncul di §4 dan §7). **Tunjuk satu sumber**, atau pindahkan isinya ke satu tempat saja.

*Alasan kausal:* salinan kedua **akan** menyimpang — bukan "mungkin". **Bukti:** audit 17 Sep menemukan tabel
kembar berheader "Situasi / Yang terjadi" di pegangan sistem-klinik baris 53 dan 77 yang **sudah
menyimpang**: salinan kedua **kehilangan satu baris aturan** (K-10 "tanyanya diborong, bukan dicicil").
Pembaca yang kebetulan membaca bagian 7 tidak pernah tahu aturan itu ada. Dokumen itu **sudah melewati run
klinik dan review independen PR #63** — dua lapis pemeriksaan manusia — dan cacatnya tetap lolos,
karena yang diminta template hanyalah *"cek diff keduanya"*, yaitu **perintah untuk diingat, bukan alat yang
berjalan**. Lihat `tools/check_manuals.py`.

---

## Isi WAJIB `PANDUAN_PENGGUNA.md` (per bagian)

### 1. Pembuka
- 1 paragraf: apa sistem ini, untuk siapa, hasil akhirnya apa (bahasa awam).
- Penanda `agent_instruction: IGNORE for execution — USER GUIDE ONLY` (+ penjelasan: dokumen ini untuk pengguna, bukan instruksi agent).

### 2. Prompt Pembuka Universal (PALING PENTING — wajib ada di paling atas setelah pembuka)
Blok prompt siap salin. Wajib memuat instruksi ke agent:
1. Baca dokumen entry point sistem (mis. `START_DI_SINI.md`) + dokumen cara-pakai/sistem utamanya.
2. Verifikasi kondisi branch/working tree (branch aktif `arena/...` dibuat otomatis platform; jangan asumsi `main`).
3. **Cek dan laporkan semua PR yang masih terbuka** (level repo — dari sistem/apapun, kalau multi-sistem).
4. Cek status sistem (manifest/index) dan laporkan ringkas.
5. **Cari `LOG_SESI_*.md` terbaru** (folder `_log-sesi/` / folder sistem / folder unit); kalau keadaannya `OPEN` → baca dan **laporkan keadaan sesi sebelumnya** — konteks itu tidak boleh ditanya ulang ke pengguna.
6. Tanya tujuan sesi; berdasarkan jawaban, baca sendiri file yang relevan — tanpa perlu ditempel manual.
7. Jangan menulis/eksekusi apa pun sebelum tujuan sesi dikonfirmasi.

### 3. Prompt Penutup Sesi (wajib ada)
Blok prompt siap salin untuk akhir sesi. Wajib memuat instruksi ke agent:
1. Update `STATUS.md` unit kerja (tahap selesai, tahap berikutnya, waktu pembaruan).
2. **Tutup log sesi** `LOG_SESI_YYYY-MM-DD.md` sesi ini: isi final header "Keadaan Sesi" (yang selesai, yang terbuka, langkah berikutnya) dan tandai `CLOSED` (atau `OPEN` + "dilanjutkan di mana").
3. Cek working tree — semua perubahan ter-commit dan ter-push (tanpa commit+push, sesi baru tidak bisa melanjutkan — fakta platform).
4. Update indeks sistem (kolom "terakhir disentuh" + status) kalau bekerja di suatu sistem.
5. Kalau kerja berlanjut lintas sesi: tulis laporan sesi/handoff sesuai template repo.
6. Ringkaskan kondisi akhir (commit terakhir, PR, langkah aman berikutnya).
7. Kalau PR akan di-merge: pastikan semua sudah push **sebelum** merge — setelah merge/close, sesi ini **tidak bisa push lagi** (fakta platform); kerja lanjutan harus dari sesi baru yang dibuka dari `main`.

### 4. Istilah (versi awam)
Repo, branch, `main`, commit, push, PR, merge — masing-masing 1–2 kalimat + analogi sederhana.

### 5. Kalimat pembuka untuk berbagai situasi
Minimal 3 situasi spesifik sistem ini (misal: mulai unit kerja baru, lanjut unit lama, revisi hasil, cek konsistensi/audit). Tiap situasi = 1 blok kalimat siap tempel.

### 6. Cara review & merge
Bagaimana pengguna meninjau hasil (PR), kapan merge, dan apa konsekuensinya (sesi tak bisa push pasca-merge).

### 7. Kebiasaan yang perlu dijaga
Checkpoint tiap tahap + commit & push; **log sesi berkelanjutan** (`LOG_SESI_YYYY-MM-DD.md` — di-update setelah tiap pertukaran penting, header keadaan selalu segar, `CLOSED` di akhir sesi); jangan lanjut kerja di sesi yang PR-nya sudah merge; kalau sesi crash, sesi baru akan otomatis membaca log sesi yang belum tertutup — kalau tidak ada, backstop = download workspace (`/download-workspace`) + lanjut dari `STATUS.md`.

---

## Catatan kualitas

- `PROMPT_ENTRI_UNIVERSAL.md` dan blok prompt di `PANDUAN_PENGGUNA.md` §2 **wajib identik** (dua file, satu sumber); selisih diam-diam pernah terjadi dan jadi temuan audit — cek diff keduanya setiap kali mengubah salah satu. Meta-sistem sendiri mengikuti standar 2-file ini di root repo (M-15, 5 Sep 2026).
- Prompt pembuka/penutup harus **portabel**: memakai path relatif folder sistem, tidak menggandeng path repo meta — supaya tetap benar saat sistem berdiri sebagai repo standalone.
- Setiap perubahan aturan sistem yang memengaruhi alur sesi wajib diikuti pembaruan bagian 2–3 pegangan (agar satu-prompt tetep cukup).
- Pegangan ikut dicek kelengkapannya oleh validator sistem (lihat `validate_system.py` masing-masing) dan `tools/validate_repo.py` (file root sistem).
- **Syarat 1–5 di atas diperiksa oleh `tools/check_manuals.py`** — tetapi alat itu **penjaring kandidat, BUKAN pemberi putusan**. Rasio positif palsunya terukur **~65%** pada korpus audit 17 Sep (28 dari 43 kandidat dicabut setelah diverifikasi), jadi **setiap temuannya wajib dibaca di sumbernya sebelum dipercaya**. Menjalankannya lalu menelan keluarannya akan menghasilkan cacat jenis baru: laporan yang meyakinkan tetapi salah.
- **Yang TIDAK bisa diperiksa alat:** apakah kalimatnya benar-benar bisa dipahami orang awam. Itu lensa #5, dan hanya bisa dinilai manusia (Syarat 4).

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | **STANDAR KELULUSAN MANUAL ditambahkan** (Syarat 1–5): 6 bidang per mekanisme, 5 kolom per perintah, ATURAN ARAH BICARA (3 aturan + pengecualian yang sah), kelulusan tidak boleh dinyatakan penulis sendiri (wajib audit lensa #5 + uji pemakaian nyata oleh pemilik), dan SATU SUMBER jangan duplikasi. Bagian Catatan kualitas dirujuk ke `tools/check_manuals.py` dengan peringatan rasio positif palsu. **Tabel Log Keputusan ini dibuat** — template adalah dokumen hidup yang isinya berubah, jadi W-05 berlaku padanya, dan sebelumnya tabel ini tidak ada | Tuntutan pemilik T26 (giliran 5) berdasarkan **bukti lapangan** dari sistem lain: prompt tanpa panduan, tabel perintah tanpa penjelasan fungsi/cara, dan kecurigaan ada kalimat yang ditujukan ke pengguna bukan ke agent. Audit 17 Sep memverifikasi bukti itu di repo ini juga: F-05 (residu chat jadi isi manual) dan F-01 (tabel kembar yang sudah menyimpang). Syarat 5 lahir langsung dari F-01. Standar kelulusan memakai rumusan pemilik sendiri, bukan rumusan agent |
| 2026-09-17 | **Catatan provenance tanpa backtick** disisipkan di 3 tempat pada dokumen ini (acuan pegangan sistem-presentasi, bukti F-05, bukti F-01) | **Pola kegagalan yang terjadi 3× pada hari yang sama saat dokumen ini ditulis:** menyebut berkas di dalam folder sistem dengan backtick dari dokumen `_meta/` membuat rujukan itu tak-terselesaikan di **ekstrak template bootstrap**, sehingga pin R7 (`EXPECTED_TEMPLATE_WARNINGS` = persis 5) bergeser dan `tools/test_failure_injection.py` MERAH. Gagalnya **tidak menyebut berkas mana** yang jadi penyebab, jadi diagnosis butuh skrip terpisah. Aturan praktisnya: **dari dokumen `_meta/`, sebut nama berkas folder sistem TANPA backtick** (provenance), atau pastikan berkas itu memang ikut ke ekstrak template (berlaku untuk `tools/*.py`, yang memang ikut). Preseden lebih tua: v1.12.1 *"tidak menambah rujukan ber-backtick ke dokumen aktif"* |
| 2026-09-05 | Template dibuat sebagai sumber W-01 (pegangan pengguna 2-file) | Butir kontrak warisan W-01; preseden M-15 (selisih diam-diam antar 2 file) |
