---
agent_instruction: IGNORE for execution — USER GUIDE ONLY
user_guide_only: true
purpose: Pegangan pengguna meta-sistem Pembangun Sistem — dokumen ini untuk manusia/pengguna, bukan instruksi eksekusi agent; agent membacanya hanya jika diminta eksplisit oleh pengguna. Prompt eksekusi lintas-sesi tetap sah ditempel dari bagian 1 dan bagian Prompt Penutup (sumber: PROMPT_ENTRI_UNIVERSAL.md).
---

# Panduan Pengguna — Meta-Sistem Pembangun Sistem

### Dokumen ini UNTUK KAMU sendiri — bukan bagian dari `_meta/`, boleh ikut repo (ditandai jelas ini bukan instruksi kerja untuk agent — dan sejak 17 Sep 2026 juga ditandai secara machine-readable di frontmatter, menyamakan dengan 4 sistem anak; sebelumnya niat ini hanya ada dalam prosa sehingga tidak bisa digrep andal: temuan audit F-06). Kalau bingung mulai dari mana, baca dokumen ini duluan.

---

## 1 Prompt Universal — Pakai Ini SETIAP KALI Mulai Sesi Baru

> Blok yang sama tersedia sebagai file siap-salin di `PROMPT_ENTRI_UNIVERSAL.md` (root repo). Kalau mengubah salah satu, ubah keduanya — keduanya wajib identik.

Tidak peduli ini pertama kali kamu pakai sistem ini, atau sudah bertahun-tahun dipakai — cukup buka sesi lmarena Agent (pilih repo yang sesuai), lalu ketik persis ini:

```
Baca dulu _meta/00_CARA_KERJA_META.md dari repo ini untuk paham cara
kerja repo ini secara keseluruhan.

Setelah itu:
1. Minta agent membuat laporan awal sesuai `_meta/SESSION_REPORT_TEMPLATE.md`, termasuk branch, working tree, commit, PR, status sistem, konteks yang dibaca, dan blocker.
2. Cek apakah ada PR yang masih terbuka/menggantung di repo ini (dari
   sistem manapun, tidak cuma yang mau aku kerjakan sekarang) — laporkan
   ke aku kalau ada, karena itu tandanya ada kerjaan lama yang belum
   selesai di-merge.
3. Cek _meta/INDEKS_SISTEM.md untuk tahu sistem apa saja yang sudah ada
   dan statusnya masing-masing.
4. Minta agent cari file `LOG_SESI_*.md` terbaru (folder `_log-sesi/` / folder
   sistem / folder unit kerja); kalau keadaannya `OPEN`, BACA dulu dan laporkan apa yang
   terjadi di sesi terakhir — jangan minta aku menjelaskan ulang konteks yang
   sudah tercatat di sana.
5. Kalau ada folder sistem yang baru saja kuletakkan di repo ini untuk
   dirawat (RAWAT INAP — sistemnya tinggal di repo ini, bukan repo
   eksternal): ikuti aturan rawat inap Sistem Klinik — entry point-nya jenis
   sesi 3 di berkas START_DI_SINI.md folder sistem klinik (foldernya tercatat
   di INDEKS_SISTEM, butir 3) — orientasi dulu (manifest/STATUS/log folder
   itu), lalu TANYA aku apa yang mau kulakukan (audit / perbaiki / upgrade)
   SEBELUM menyentuh apa pun; gerbang G-Rencana & G-Final aturan klinik
   berlaku, dan PR-nya = PR normal repo ini (tanpa auto-merge).

Berdasarkan itu, tanya aku: aku mau ngapain di sesi ini — bangun sistem
baru, lanjut/audit sistem yang sudah ada, rawat inap salah satu sistem
(lihat butir 5), atau hal lain. Kalau aku mau
lanjut sistem yang sudah lama tidak disentuh, ingatkan dulu apakah perlu
diaudit sebelum lanjut. Kalau aku sebut sistem tertentu, BARU baca lebih
dalam folder sistem/sistem-[nama]/ itu — jangan baca seluruh isi repo di awal,
cukup baca yang relevan dengan apa yang aku mau kerjakan.
```

**Kenapa checklist di atas (bukan cuma 1 langkah):** ini gabungan 2 hal yang PENTING dicek di level REPO ini (bukan cuma di dalam 1 sistem) — PR menggantung (bisa dari sistem manapun, karena 1 repo menampung banyak sistem sekaligus) dan status sistem-sistem yang ada. Tanpa cek PR ini, ada risiko kerjaan lama dari sistem lain terlupakan menggantung — persis kasus yang pernah terjadi sebelum prinsip ini dikunci di sistem konten kreator.

**Berlaku untuk SEMUA situasi** — baik kamu baru pertama kali sentuh repo ini, mau bikin sistem baru yang benar-benar baru, atau mau lanjut sistem yang sudah kamu tinggal setahun. Agent akan menyesuaikan sendiri berdasarkan apa yang dia temukan di `INDEKS_SISTEM.md`.

---

## Prompt Penutup Sesi — Pakai di Akhir Tiap Sesi

Sebelum menutup sesi (baik kerja sudah selesai mau di-merge, mau jeda dulu, atau sesi mau di-crash-kan karena panjang), tempel ini supaya sesi berikutnya bisa melanjutkan tanpa kehilangan apa pun:

```
Tutup sesi ini dengan benar:
1. Update STATUS.md unit kerja yang disentuh (tahap selesai, tahap
   berikutnya, waktu pembaruan).
2. Tutup log sesi ini (LOG_SESI_YYYY-MM-DD.md): isi final "Keadaan Sesi"
   (yang selesai, yang terbuka, langkah berikutnya) dan tandai CLOSED.
3. Cek working tree: semua perubahan WAJIB ter-commit dan ter-push —
   tanpa commit+push, sesi baru tidak bisa melanjutkan (fakta platform).
4. Update "Terakhir Disentuh" + status tiap sistem yang disentuh di
   _meta/INDEKS_SISTEM.md.
5. Kalau kerja berlanjut lintas sesi, buat laporan sesi/handoff sesuai
   template repo.
6. Ringkaskan kondisi akhir: commit terakhir, status PR, dan langkah
   aman berikutnya.
7. Kalau aku mau merge PR: pastikan semua sudah push SEBELUM merge —
   setelah merge/close, sesi ini TIDAK BISA push lagi (fakta platform);
   kerja lanjutan harus dari sesi baru yang dibuka dari main.
8. Kalau sesi ini membuka PR: jalankan
   `python3 tools/review_prompt.py --pr <NOMOR PR>` dan tempel SELURUH
   keluarannya sebagai pesan terakhirmu — jangan disunting, jangan
   dikarang sendiri. Itu prompt review independennya
   (`_meta/PROTOKOL_REVIEW_INDEPENDEN.md` §"Sumber prompt").
```

---

## Minta Review, Tanpa Perantara

Kalau sebuah PR perlu diperiksa sesi lain, kamu **tidak perlu menunggu sesi yang mengerjakannya**
menuliskan prompt review, dan **tidak perlu menulisnya sendiri**. Dua perintah, dijalankan dari root repo:

```bash
# 1. buka PR-nya (kalau belum dibuka sesi yang mengerjakan)
gh pr create --base main --title "JUDUL" --body "ISI"

# 2. bangkitkan prompt reviewnya — nomor PR, base sha, head sha, daftar berkas
#    diisi otomatis dari data PR di GitHub
python3 tools/review_prompt.py --pr NOMOR_PR
```

Salin seluruh keluaran perintah ke-2 itu ke **sesi baru** — itulah prompt reviewernya, lengkap.

Tiga hal yang perlu kamu tahu:

- **Prompt itu tidak boleh dikarang.** Sesi yang mengerjakan PR dilarang menulis atau menyunting prompt
  review untuk dirinya sendiri; kalau ia merasa reviewer perlu konteks tambahan, konteks itu masuk ke
  body PR. Aturannya di `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` bagian "Sumber prompt".
- **Sesi yang membuka PR wajib menempelkan keluaran perintah ke-2 sebagai pesan terakhirnya.** Kalau
  sesinya keburu mati, kamu jalankan sendiri perintah yang sama — hasilnya identik.
- **Kalau alatnya gagal, tidak ada prompt yang keluar.** Ia sengaja menolak mencetak prompt dengan sha
  kosong; pesan gagalnya menyebut apa yang harus diperbaiki (biasanya nomor PR-nya salah).

Mau lihat bentuk promptnya dulu tanpa PR sungguhan (versi berisi `<NOMOR PR>` / `<BASE SHA>` /
`<HEAD SHA>`):

```bash
python3 tools/review_prompt.py --generic
```

Isi panduan ini sengaja tidak menyalin teks promptnya: satu-satunya salinan yang tidak pernah basi adalah
keluaran alatnya sendiri.

---

## Minta Audit Isi, Bukan Review PR

**Ditambahkan 17 Sep 2026.** Dua pekerjaan berbeda, dua mekanisme berbeda — dan mencampuradukkannya
pernah terjadi di repo ini:

| | **Review PR** (bagian sebelumnya) | **Audit isi** (bagian ini) |
|---|---|---|
| Pertanyaannya | *"bolehkah ini di-merge?"* | *"sehatkah isi ini?"* |
| Objeknya | satu PR | **satu jalur** di repo: `_meta`, `tools`, sebuah sistem, atau satu berkas |
| Keluarannya | verdict + keputusan merge | **laporan temuan** — tidak ada merge |
| Alatnya | `python3 tools/review_prompt.py --pr N` | `python3 tools/audit_prompt.py --objek <path>` |
| Hasilnya ditaruh di | komentar PR | **berkas ter-commit** di `_meta/_internal/audit/` (**Kanal A = UTAMA**), baris pertamanya `# AUDIT <objek> @<sha7>`. GitHub Issue = **alternatif yang terblokir** (403, terukur 17 Sep 2026) |
| Aturannya | `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` | `_meta/PROTOKOL_AUDIT_ISI.md` |

**Kapan pakai yang ini:** sesudah membangun sesuatu dan sebelum menyatakannya siap; untuk pemeriksaan
berkala; kalau kamu minta *"periksa semuanya"* tanpa menunjuk PR; atau kalau kamu mencurigai satu
**jenis** cacat yang mungkin tersebar di banyak tempat.

### Cara — 5 langkah

1. **Buka sesi agent BARU.** Jangan pakai sesi yang sedang mengerjakan objek itu — auditor yang
   mengaudit pekerjaannya sendiri tidak bisa independen.
2. Di sesi baru itu, minta agent membangkitkan prompt auditnya. **Contoh yang bisa kamu salin:**

   ```
   Bangkitkan prompt audit isi untuk objek `_meta` dengan kedalaman mendalam, lalu berhenti dan
   tunjukkan keluarannya ke aku. Jangan menulis prompt audit sendiri — pakai alatnya.
   ```

   Perintah yang akan dijalankan agent:

   ```bash
   python3 tools/audit_prompt.py --objek _meta --kedalaman mendalam
   ```

3. **Tempel seluruh keluaran perintah itu** ke **sesi auditor** (sesi ketiga, yang benar-benar mengaudit)
   sebagai pesan pertamanya.
4. Tunggu. Auditor menyerahkan hasilnya sebagai **berkas ter-commit** di `_meta/_internal/audit/` (Kanal A) — **bukan** GitHub Issue; kanal Issue terblokir 403 di lingkungan ini (terukur 17 Sep 2026).
5. Kembali ke sesi yang sedang bekerja, dan **cukup bilang**: *"audit sudah selesai."* Sesi itu
   mengambil hasilnya sendiri:

   ```bash
   python3 tools/ambil_verdict.py --terbaru
   ```

   **Kamu tidak perlu menyalin, meringkas, atau melaporkan apa pun.** Ini yang diminta pemilik
   17 Sep 2026 dan sekarang sudah jadi mekanisme.

### Perintah yang dipakai

| Perintah | Fungsi | Kapan dipakai | Keluaran diharapkan | Kalau gagal |
|---|---|---|---|---|
| `python3 tools/audit_prompt.py --objek <path>` | membangkitkan prompt audit yang **ter-pin** ke satu sha — **bukan** dikarang tangan | langkah 2 di atas | prompt 13 bagian + inventaris berkas yang diambil dari pohon kerja | exit 2 + pesan sebabnya (objek tak ada / sha tak sah / objek keluar repo). **Perbaiki argumennya; jangan menulis prompt tangan** |
| `python3 tools/audit_prompt.py --generic` | melihat bentuk prompt tanpa objek sungguhan | kalau mau memeriksa alatnya dulu | prompt dengan `<OBJEK>` dan `<SHA PIN>` | — |
| `python3 tools/ambil_verdict.py --terbaru` | mengambil hasil audit terbaru **tanpa perlu diberi tahu nomornya** | langkah 5 | badan Issue + semua komentar + verdict terbaca otomatis | exit 2: tidak ditemukan, atau ambigu. **Alat ini tidak pernah menyimpulkan "bersih" dari ketiadaan hasil** |
| `python3 tools/ambil_verdict.py --daftar` | melihat semua kandidat hasil audit | untuk memilih mana yang dimaksud | daftar terbaru di atas, dengan objek + sha | kosong = memang belum ada audit diserahkan |
| `gh label create audit-independen --description "hasil audit isi independen"` | membuat label kanalnya (**sekali saja**, di awal) | sebelum audit pertama | label terbuat | kalau label sudah ada, `gh` memberi tahu — itu bukan masalah |

### Apa yang terjadi sesudahnya

Auditor menulis Issue berisi 6 bagian wajib: **VERDICT** satu baris → **ringkasan angka** (berapa berkas
diperiksa, berapa kandidat, berapa dicabut) → **tabel temuan** terklasifikasi (`B`/`A`/`G`/`N`/`P` +
prioritas + bukti) → **temuan DI LUAR CAKUPAN** → **kandidat yang DICABUT** → **batasan audit**.
Putaran lanjutan ditambahkan sebagai **komentar**, tidak pernah menyunting temuan putaran pertama.

**Sesi yang diaudit kemudian membaca semuanya sendiri** — termasuk bagian "di luar cakupan" dan
"kandidat yang dicabut", karena keduanya bagian dari laporan, bukan sampah. **Membaca verdict ≠
menyetujuinya:** bertindak atas temuan tetap butuh keputusanmu.

### Satu aturan yang wajib kamu tahu

> **Cakupan membatasi apa yang DICARI dan apa yang boleh DIKLAIM. Cakupan TIDAK PERNAH membatasi
> apa yang dilaporkan.**

Artinya: kalau auditor menemukan masalah di luar objek yang kamu minta, ia **wajib tetap melaporkannya**
(dilabeli "di luar cakupan"), dan **tidak boleh** membuangnya supaya laporan terlihat rapi. Ia juga
**tidak boleh** mengklaim sudah memeriksa lebih dari yang benar-benar diperiksa, dan **tidak boleh**
memperbaiki temuan di luar cakupan tanpa mandatmu. Aturan lengkap: `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md`
bagian ATURAN CAKUPAN.

### Kalau gagal

| Gejala | Sebab | Langkah pertama |
|---|---|---|
| `ERROR: tidak ada --objek` | alat **sengaja menolak menebak** objeknya | sebut objeknya. Menebak = mengaudit sesuatu yang tidak kamu minta |
| `ERROR: objek X TIDAK ADA` | salah eja | daftar sistem ada di `_meta/INDEKS_SISTEM.md` |
| `tidak ditemukan hasil audit di kanal Issue` | audit belum diserahkan, **atau** auditor menaruhnya di tempat lain, **atau** label belum dibuat | **jangan simpulkan "bersih"**. Cek `gh issue list --state all`; buat labelnya sekali kalau belum |
| `ambigu: beberapa hasil audit` | alat **sengaja menolak menebak** | `--daftar` lalu `--issue <N>` |
| auditor mengembalikan prompt yang sudah disunting | pelanggaran aturan "prompt tidak boleh dikarang" | **tolak**, bangkitkan ulang, catat sebagai temuan |

**Kenapa prompt audit tidak boleh ditulis tangan:** kalau pihak yang diaudit boleh menulis instruksi untuk
pengadilnya sendiri, hasil audit mengukur **kepandaian menulis prompt**, bukan **kesehatan isi**. Alasan
yang sama kenapa `review_prompt.py` ada untuk PR.

**Yang sudah DIUJI dan hasilnya negatif — jangan dibaca sebagai "belum diuji":** pengiriman hasil
lewat `gh issue create` **ditolak HTTP 403** `Resource not accessible by integration` (terukur 17 Sep
2026 di lingkungan ini; `permissions` token semuanya `false`). Jadi kanal Issue bukan rancangan yang
belum disentuh: ia **sudah diuji dan terblokir**, dan karena itu kanal UTAMA adalah **Kanal A — berkas
ter-commit** di `_meta/_internal/audit/` (`_meta/PROTOKOL_AUDIT_ISI.md`).

**Yang masih belum terbukti:** keberhasilan kanal Issue *kalau* izin kelak diberikan — labelnya sudah
ada, tetapi keberadaan label tidak membuktikan bisa membuat Issue. Selama izin itu belum ada, jangan
mengandalkan Issue.

**Satu pengecualian read-only yang dinyatakan:** auditor boleh `commit + push` **tepat satu berkas**,
yaitu laporannya sendiri di `_meta/_internal/audit/`. Selain itu ia tetap read-only. Alasannya
integritas: laporan pengadil yang di-commit oleh pihak yang diaudit bisa diubah di jalan, sedangkan
commit milik auditor sendiri adalah bukti asal-usulnya.

---

## Setelah Baseline Di-merge — Prompt Handoff

Untuk melanjutkan pekerjaan setelah merge atau setelah sesi terputus, gunakan prompt lengkap yang tersimpan di `_meta/NEXT_SESSION_PROMPT.md`. Prompt tersebut lebih aman daripada hanya berkata "lanjutkan", karena agent diwajibkan memverifikasi ulang repository, branch, PR, manifest, handoff, index, dan konteks yang dibaca.

Prompt tersebut membangun ulang konteks dari file resmi. Ia tidak menjamin agent mengetahui hal yang hanya pernah dibahas di chat atau informasi yang tidak tersimpan di branch.

**Penting — Batasan Platform lmarena (bukan aturan kita, tapi fakta):**
- Setelah PR di-merge/close, sesi tersebut **tidak bisa** push lagi ke GitHub (platform cabut akses). File baru setelah merge akan terjebak di sesi. Karena itu pastikan semua sudah push sebelum merge, dan buka sesi baru dari `main` untuk kerja lanjutan. Detail ada di `_meta/PLATFORM_LMARENA.md`.
- Jika sesi tiba-tiba error / tidak bisa lanjut chat, gunakan workaround resmi Arena: tambah `/download-workspace` di akhir URL sesi untuk download zip workspace, lalu buka sesi baru dan lanjut dari STATUS.md terakhir.

## Kalau Kamu Sudah Tahu Persis Mau Ngapain (opsional, boleh dipakai langsung)

Prompt universal di atas selalu aman dipakai, tapi kalau kamu sudah yakin mau langsung ke suatu hal spesifik, boleh langsung pakai salah satu ini (tetap akan baca konteks yang perlu, cuma tidak perlu tanya dulu):

**Mau bangun sistem benar-benar baru:**
```
Aku mau bangun sistem baru untuk [SEBUTKAN DOMAINNYA]. Baca dulu
_meta/00_CARA_KERJA_META.md dan _meta/02_PRINSIP_UNIVERSAL.md, lalu
jalankan proses di _meta/01_DISCOVERY_LEVEL_0.md.
```

**Mau lanjut sistem yang sudah ada (kamu tahu nama sistemnya):**
```
Aku mau lanjut kerja di sistem [NAMA SISTEM]. Cek dulu
_meta/INDEKS_SISTEM.md untuk status terakhirnya, baca dokumen navigasi
di dalam folder sistem/sistem-[nama]/, baru kita lanjut.
```

**Mau pakai Claude chat biasa sebagai cadangan** (karena lmarena kurang maksimal saat itu):
Upload `_cadangan-claude/RINGKASAN_sistem-[nama].md` + dokumen spesifik yang mau dikerjakan, lalu ketik:
```
Ini ringkasan sistem yang sedang aku kerjakan, plus dokumen spesifik
yang mau [direvisi/didiskusikan/dst]. Baca dulu ringkasannya, pastikan
kamu paham ke mana hasil kerja ini akan dibawa, baru kita mulai.
```

---

## Mengeluarkan Satu Sistem Jadi Repo Sendiri

Kalau sebuah sistem sudah matang dan kamu mau memakainya di repo GitHub-nya sendiri
(terpisah dari repo ini), yang disalin adalah folder sistem itu sendiri. Tidak ada
ZIP, tidak ada folder dist, dan tidak ada daftar file yang harus kamu pilih manual.

Dari root repo master, jalankan gerbang ini:

    python3 tools/check_selfcontained.py --sistem sistem-nama-sistemnya --report

Kalau exit 0, folder itu adalah deliverable mandiri: salin foldernya apa adanya ke
repo tujuan. Kalau merah, keluaran alat adalah daftar kerja yang harus diperbaiki
di dalam folder sistem. Jangan menambal hasil salinan sementara.

Aturan penting:

- Semua rujukan di dalam folder sistem harus relatif terhadap folder itu. Rujukan
  berformat `sistem-nama-sistemnya/...` dari folder tersebut ke dirinya sendiri
  salah.
- Rujukan ber-backtick ke satu berkas `_meta/...` atau `tools/...` di dokumen aktif
  berarti salinan berlabel dari sumber itu harus ada di dalam folder sistem.
- Yang dinilai alat hanya dokumen aktif. Rujukan di dokumen bukti/log tidak
  ditagih salinan (tetapi tetap dicatat alat sebagai rujukan historis), dan
  penyebutan area berbentuk direktori — misalnya `_meta/` dengan garis miring di
  belakang — bukan kegagalan.
- Area yang tidak boleh keluar dari master (audit/handoff internal dan yang
  sejenis) tidak boleh disalin ke folder sistem: tulis sebagai provenance tanpa
  backtick.
- Riwayat/provenance boleh disebut tanpa backtick; riwayat lengkap tetap di master.

Aturan lengkapnya ada di `_meta/PAKET_REPO_MANDIRI.md`.


---

## Kalau Ragu, Pakai Prompt Universal Saja

Kamu tidak perlu menghafal kapan pakai prompt yang mana — **prompt universal di bagian paling atas SELALU aman dipakai**, di situasi apapun. Prompt-prompt spesifik di bawahnya cuma jalan pintas opsional kalau kamu sudah yakin, bukan keharusan.

---

## Istilah Singkat (kalau lupa)

- **`_meta/`** — instruksi cara kerja yang berlaku untuk semua sistem
- **`sistem-[nama]/`** — 1 sistem spesifik (misal sistem konten kreator, atau sistem baru nanti)
- **`_cadangan-claude/`** — ringkasan tiap sistem, dipakai kalau perlu bantuan Claude chat biasa
- **`_pegangan-kamu/`** — file milikmu sendiri, bebas diisi apa saja

Untuk istilah teknis lain (branch, PR, merge, commit) — lihat `sistem/sistem-konten-kreator/panduan/PANDUAN_PENGGUNA.md`, penjelasannya sama berlaku di sini.

Alur "apa yang terjadi saat aku membangun sistem baru" diringkas di `_meta/03_KONTRAK_WARISAN.md` — daftar hal yang otomatis ikut tertanam di setiap sistem (pegangan, log sesi, checkpoint, dll) tanpa perlu kamu minta satu-satu.
