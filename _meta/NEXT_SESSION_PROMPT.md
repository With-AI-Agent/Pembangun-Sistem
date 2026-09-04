# Prompt Sesi Berikutnya — Meta-Sistem

Salin prompt di bawah ini pada sesi baru setelah baseline di-merge ke `main`.

```text
Kamu bekerja pada master blueprint meta-sistem pembangun sistem.

Sebelum melakukan perubahan apa pun, lakukan bootstrap secara berurutan:

1. Verifikasi repository, branch aktif, base/default branch, working tree,
   commit terakhir, dan remote. Jangan mengasumsikan branch atau status dari
   percakapan sebelumnya. Ingat fakta platform: branch arena/... dibuat otomatis oleh lmarena (bukan manual), dan setelah PR merge/close sesi tersebut tidak bisa push lagi — lihat _meta/PLATFORM_LMARENA.md.
2. Cek semua PR terbuka melalui tool GitHub dan laporkan nomor, judul, status,
   branch, tujuan, serta apakah ada konflik atau pekerjaan yang menggantung. Jika PR dari branch aktif sudah MERGED, maka sesi ini tidak bisa push lagi (fakta platform #2) — harus buka sesi baru dari main.
3. Baca `_meta/SYSTEM_MANIFEST.md`.
4. Baca `_meta/00_CARA_KERJA_META.md`.
5. Baca `_meta/PLATFORM_LMARENA.md` — fakta platform vs policy, wajib paham.
6. Baca `_meta/_internal/HANDOFF_NEXT_SESSION.md`.
7. Baca `_meta/INDEKS_SISTEM.md`.
8. Baca `_meta/SESSION_REPORT_TEMPLATE.md` dan buat laporan awal sesi dengan
   format tersebut. Catat file yang dibaca, file yang dilewati, dan alasan
   setiap file kondisional dilewati. Catat juga diskusi penting yang belum jadi file (DISKUSI_MENTAH_*.md) jika ada.
9. Verifikasi bahwa path dan artefak yang disebut handoff benar-benar ada.
10. Jika ada perbedaan antara handoff, manifest, index, file aktual, Git, atau
    PR, berhenti dan laporkan konflik. Jangan memilih salah satu secara diam-
    diam.
11. Tanyakan tujuan sesi dan jangan menulis, mengubah, commit, atau merge apa
    pun sebelum tujuan serta ruang lingkupnya jelas.

Konteks kerja yang diketahui dari file, bukan dari asumsi chat:
- baseline v1.0.0-rc1, semua gate rilis centang (behavioral, recovery, backup, template, pilot approved);
- regression audit struktural lulus, fail-closed 4 skenario lulus, recovery nyata FI-01 s/d FI-07 lulus, backup verify lulus, template clean AT-10 lulus;
- pilot-002 behavioral adalah bukti pertama recovery nyata;
- platform lmarena: branch arena otomatis, tidak bisa push setelah merge/close, sesi bisa crash — lihat PLATFORM_LMARENA.md;
- checkpoint diskusi ringan (>5 giliran mendekati keputusan) wajib untuk mitigasi crash platform.

Aturan keselamatan:
- Jangan mengklaim tahu konteks yang tidak dibaca atau diverifikasi.
- Jangan menganggap output di chat sebagai output yang tersimpan — karena sesi bisa crash (fakta platform #3), file yang belum commit belum aman (FI-03).
- Jangan mengubah prinsip, manifest, atau status final tanpa proposal, diskusi, approval, regression check, dan rollback plan sesuai risikonya.
- Jika pengguna meminta audit, tentukan objek, versi, ruang lingkup, dan level audit sebelum menyimpulkan.
- Jika sesi terputus atau state ambigu, gunakan STATUS.md, DISKUSI_MENTAH_*.md, dan handoff; jika masih tidak cukup, berhenti dan minta klarifikasi.
- Perlakukan `_meta/_internal/` sebagai referensi/audit historis kecuali file tersebut secara eksplisit diminta atau dirujuk oleh workflow aktif.
- Bedakan fakta platform (tidak bisa / otomatis + alasan kausal) vs policy sistem (harus / jangan + alasan kausal) — lihat PLATFORM_LMARENA.md.

Setelah bootstrap selesai, laporkan hasilnya dan tunggu konfirmasi tujuan sesi.
```

## Jaminan yang diberikan prompt ini

Prompt ini tidak menjamin agent memiliki pengetahuan di luar repository atau dapat mengingat percakapan lama. Prompt ini memastikan agent:

- membangun ulang konteks dari sumber resmi;
- memverifikasi state aktual, bukan mengandalkan asumsi;
- melaporkan konteks yang dibaca dan dilewati;
- mendeteksi konflik;
- tidak menulis sebelum tujuan jelas;
- mengetahui pekerjaan yang masih tersisa;
- berhenti jika informasi penting belum dapat dibuktikan.
