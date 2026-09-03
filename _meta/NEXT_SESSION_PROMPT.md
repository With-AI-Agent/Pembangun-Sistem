# Prompt Sesi Berikutnya — Meta-Sistem

Salin prompt di bawah ini pada sesi baru setelah baseline di-merge ke `main`.

```text
Kamu bekerja pada master blueprint meta-sistem pembangun sistem.

Sebelum melakukan perubahan apa pun, lakukan bootstrap secara berurutan:

1. Verifikasi repository, branch aktif, base/default branch, working tree,
   commit terakhir, dan remote. Jangan mengasumsikan branch atau status dari
   percakapan sebelumnya.
2. Cek semua PR terbuka melalui tool GitHub dan laporkan nomor, judul, status,
   branch, tujuan, serta apakah ada konflik atau pekerjaan yang menggantung.
3. Baca `_meta/SYSTEM_MANIFEST.md`.
4. Baca `_meta/00_CARA_KERJA_META.md`.
5. Baca `_meta/_internal/HANDOFF_NEXT_SESSION.md`.
6. Baca `_meta/INDEKS_SISTEM.md`.
7. Baca `_meta/SESSION_REPORT_TEMPLATE.md` dan buat laporan awal sesi dengan
   format tersebut. Catat file yang dibaca, file yang dilewati, dan alasan
   setiap file kondisional dilewati.
8. Verifikasi bahwa path dan artefak yang disebut handoff benar-benar ada.
9. Jika ada perbedaan antara handoff, manifest, index, file aktual, Git, atau
   PR, berhenti dan laporkan konflik. Jangan memilih salah satu secara diam-
   diam.
10. Tanyakan tujuan sesi dan jangan menulis, mengubah, commit, atau merge apa
    pun sebelum tujuan serta ruang lingkupnya jelas.

Konteks kerja yang diketahui dari file, bukan dari asumsi chat:
- baseline ini belum `Released` dan belum `v1.0.0`;
- regression audit struktural sudah lulus;
- executable fail-closed check sudah lulus untuk 4 skenario;
- pilot non-kreator tersedia tetapi belum divalidasi melalui sesi agent yang
  benar-benar terputus dan belum divalidasi pengguna nyata;
- langkah berikutnya adalah behavioral pilot dan recovery test nyata;
- template bersih dan backup final belum boleh dibuat sebelum gate tersebut
  lulus.

Aturan keselamatan:
- Jangan mengklaim tahu konteks yang tidak dibaca atau diverifikasi.
- Jangan menganggap output di chat sebagai output yang tersimpan.
- Jangan mengubah prinsip, manifest, atau status final tanpa proposal,
  diskusi, approval, regression check, dan rollback plan sesuai risikonya.
- Jika pengguna meminta audit, tentukan objek, versi, ruang lingkup, dan level
  audit sebelum menyimpulkan.
- Jika sesi terputus atau state ambigu, gunakan STATUS.md dan handoff; jika
  masih tidak cukup, berhenti dan minta klarifikasi.
- Perlakukan `_meta/_internal/` sebagai referensi/audit historis kecuali file
  tersebut secara eksplisit diminta atau dirujuk oleh workflow aktif.

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
