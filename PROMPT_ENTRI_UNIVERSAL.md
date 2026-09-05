# Prompt Pembuka Universal — Meta-Sistem

> Satu blok prompt siap tempel untuk MEMULAI sesi apa pun di repo meta ini. File ini dan `PANDUAN_PENGGUNA.md` §1 harus berisi blok yang **identik** — kalau mengubah satu, ubah keduanya (dicek saat audit; selisihnya pernah jadi temuan M-15, audit meta 5 Sep 2026). Ini arahan kerja, bukan jaminan agent sudah tahu segalanya: kalau file wajib hilang atau bertentangan, agent harus berhenti dan melapor.

## Prompt

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

## Prompt Penutup Sesi

Blok penutup (update STATUS, tutup `LOG_SESI`, cek tree, update INDEKS, handoff, ringkasan, aturan merge) ada di `PANDUAN_PENGGUNA.md` §"Prompt Penutup Sesi" — pakai itu sebelum menutup sesi.
