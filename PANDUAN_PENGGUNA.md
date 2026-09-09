# Panduan Pengguna — Meta-Sistem Pembangun Sistem

### Dokumen ini UNTUK KAMU sendiri — bukan bagian dari `_meta/`, boleh ikut repo (ditandai jelas ini bukan instruksi kerja untuk agent). Kalau bingung mulai dari mana, baca dokumen ini duluan.

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
4. Minta agent cari file `LOG_SESI_*.md` terbaru (root repo / folder sistem /
   folder unit kerja); kalau keadaannya `OPEN`, BACA dulu dan laporkan apa yang
   terjadi di sesi terakhir — jangan minta aku menjelaskan ulang konteks yang
   sudah tercatat di sana.

Berdasarkan itu, tanya aku: aku mau ngapain di sesi ini — bangun sistem
baru, lanjut/audit sistem yang sudah ada, atau hal lain. Kalau aku mau
lanjut sistem yang sudah lama tidak disentuh, ingatkan dulu apakah perlu
diaudit sebelum lanjut. Kalau aku sebut sistem tertentu, BARU baca lebih
dalam folder sistem-[nama]/ itu — jangan baca seluruh isi repo di awal,
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
di dalam folder sistem-[nama]/, baru kita lanjut.
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

Untuk istilah teknis lain (branch, PR, merge, commit) — lihat `sistem-konten-kreator/panduan/PANDUAN_PENGGUNA.md`, penjelasannya sama berlaku di sini.

Alur "apa yang terjadi saat aku membangun sistem baru" diringkas di `_meta/03_KONTRAK_WARISAN.md` — daftar hal yang otomatis ikut tertanam di setiap sistem (pegangan, log sesi, checkpoint, dll) tanpa perlu kamu minta satu-satu.
