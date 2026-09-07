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
```

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
(terpisah dari repo ini), kamu **tidak perlu** memilah-milah file satu per satu.
Satu perintah, dijalankan dari root repo ini:

```bash
# 1. lihat dulu apa yang akan ikut, tanpa menulis apa pun
python3 tools/pack_repo.py sistem-nama-sistemnya --check

# 2. kalau baris terakhirnya CHECK HIJAU, bangkitkan folder repo mandirinya
python3 tools/pack_repo.py sistem-nama-sistemnya
```

Hasilnya satu folder siap di-upload: folder sistemnya utuh, hanya dokumen `_meta/`
yang benar-benar dipakai sistem itu, dua alat pemeriksa, pegangan pengguna, dan
`PAKET_REPO.md` yang mencatat asal-usulnya + perintah verifikasinya. Isi dokumen
tidak ditulis ulang sama sekali.

Tiga hal yang perlu kamu tahu, sisanya urusan alatnya:

- **Kalau perintahnya gagal, foldernya memang tidak ada.** Alat ini tidak
  meninggalkan paket setengah jadi. Pesan gagalnya menyebut apa yang harus
  diperbaiki — perbaikannya dilakukan di repo ini, bukan di hasil pack.
- **Hasil pack tidak di-commit ke repo ini.** Repo ini tetap satu-satunya sumber
  kebenaran; paketnya selalu bisa dibangkitkan ulang kapan saja.
- **Empat perintah untuk mengunggahnya ke GitHub** sudah dituliskan di dalam
  `PAKET_REPO.md` di folder hasil — tinggal ikuti dari atas ke bawah.

Aturan lengkapnya (apa yang ikut, apa yang sengaja tidak, kenapa) ada di
`_meta/PAKET_REPO_MANDIRI.md`.

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
