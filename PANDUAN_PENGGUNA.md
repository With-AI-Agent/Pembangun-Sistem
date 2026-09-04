# Panduan Pengguna — Meta-Sistem Pembangun Sistem

### Dokumen ini UNTUK KAMU sendiri — bukan bagian dari `_meta/`, boleh ikut repo (ditandai jelas ini bukan instruksi kerja untuk agent). Kalau bingung mulai dari mana, baca dokumen ini duluan.

---

## 1 Prompt Universal — Pakai Ini SETIAP KALI Mulai Sesi Baru

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
2. Cek _meta/INDEKS_SISTEM.md untuk tahu sistem apa saja yang sudah ada
   dan statusnya masing-masing.

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

## Kalau Ragu, Pakai Prompt Universal Saja

Kamu tidak perlu menghafal kapan pakai prompt yang mana — **prompt universal di bagian paling atas SELALU aman dipakai**, di situasi apapun. Prompt-prompt spesifik di bawahnya cuma jalan pintas opsional kalau kamu sudah yakin, bukan keharusan.

---

## Istilah Singkat (kalau lupa)

- **`_meta/`** — instruksi cara kerja yang berlaku untuk semua sistem
- **`sistem-[nama]/`** — 1 sistem spesifik (misal sistem konten kreator, atau sistem baru nanti)
- **`_cadangan-claude/`** — ringkasan tiap sistem, dipakai kalau perlu bantuan Claude chat biasa
- **`_pegangan-kamu/`** — file milikmu sendiri, bebas diisi apa saja

Untuk istilah teknis lain (branch, PR, merge, commit) — lihat `PANDUAN_PENGGUNA.md` di dalam `sistem-konten-kreator/`, penjelasannya sama berlaku di sini.
