# Prompt Sesi Berikutnya — Meta-Sistem

Salin prompt di bawah ini pada sesi baru setelah baseline di-merge ke `main`.

```text
Kamu bekerja pada master blueprint meta-sistem pembangun sistem.

Sebelum melakukan perubahan apa pun, lakukan bootstrap secara berurutan:

1. Verifikasi repository, branch aktif, base/default branch, working tree,
   commit terakhir, dan remote. Jangan mengasumsikan branch atau status dari
   percakapan sebelumnya. Ingat fakta platform: branch arena/... dibuat otomatis oleh lmarena (bukan manual), dan setelah PR merge/close sesi tersebut tidak bisa push lagi — lihat _meta/PLATFORM_LMARENA.md.
2. Cek PR melalui tool GitHub dengan `gh pr list --state all --limit 20` dan laporkan nomor, judul, status,
   branch, tujuan, serta apakah ada konflik atau pekerjaan yang menggantung. `--state all` WAJIB (bukan `--state open`) supaya PR dari branch aktif yang sudah MERGED/CLOSED terlihat — jika PR dari branch aktif sudah MERGED, sesi ini tidak bisa push lagi (fakta platform #2) — harus buka sesi baru dari main.
   Cari juga `LOG_SESI_*.md` terbaru (folder `_log-sesi/` / folder sistem / folder unit);
   kalau keadaannya `OPEN`, BACA dan laporkan keadaan sesi sebelumnya —
   itu konteks yang tidak boleh ditanya ulang.
3. Baca `_meta/SYSTEM_MANIFEST.md`.
4. Baca `_meta/00_CARA_KERJA_META.md`. Bila kerja menyentuh sistem manapun atau berupa audit lintas-sistem, lanjut baca `_meta/03_KONTRAK_WARISAN.md` (daftar butir yang wajib tertanam di semua sistem — default aktif, override butuh konfirmasi pengguna).
5. Baca `_meta/PLATFORM_LMARENA.md` — fakta platform vs policy, wajib paham.
6. Baca `_meta/_internal/HANDOFF_NEXT_SESSION.md`.
7. Baca `_meta/INDEKS_SISTEM.md`.
   **Lanjut baca dua berkas ini — WAJIB, bukan opsional** (keduanya diperiksa `tools/validate_repo.py`,
   jadi kewajiban ini tidak bisa hilang diam-diam):
   - `_meta/DAFTAR_PEKERJAAN_TERBUKA.md` — semua pekerjaan yang belum selesai ada di sini, dan berkas
     ini **satu-satunya tempat sah** menaruhnya. Sesi yang tidak membacanya akan mengulang pekerjaan
     yang sudah dijadwalkan atau **melupakan utang yang sudah dijanjikan ke pemilik**.
   - `_meta/TANGGAPAN_MASUKAN_PEMILIK.md` — setiap masukan pemilik wajib punya **respons** dengan
     kosakata status tertutup; **`TERCATAT` bukan status yang sah**. Kalau kerja sesi ini menyentuh
     sebuah tuntutan, **perbarui barisnya sebelum sesi selesai**. Instruksi pemilik 17 Sep 2026:
     *"jangan cuma dicatat tapi juga harus direspon/dieksekusi."*
8. Baca `_meta/SESSION_REPORT_TEMPLATE.md` dan buat laporan awal sesi dengan
   format tersebut. Catat file yang dibaca, file yang dilewati, dan alasan
   setiap file kondisional dilewati. Catat juga diskusi penting yang belum jadi file (DISKUSI_MENTAH_*.md) jika ada.
9. Verifikasi bahwa path dan artefak yang disebut handoff benar-benar ada.
10. Jika ada perbedaan antara handoff, manifest, index, file aktual, Git, atau
    PR, berhenti dan laporkan konflik. Jangan memilih salah satu secara diam-
    diam.
11. Tanyakan tujuan sesi dan jangan menulis, mengubah, commit, atau merge apa
    pun sebelum tujuan serta ruang lingkupnya jelas.

Konteks kerja yang diketahui dari file, bukan dari asumsi chat (ini orientasi saja — blok ini sengaja bebas angka versi/klaim status agar tidak pernah basi; versi dan status AKTUAL selalu dibaca dari file yang disebut, bukan dari baris ini):
- Meta-sistem berstatus `Released`; versi + gate aktual: `_meta/SYSTEM_MANIFEST.md`.
- Sistem domain terdaftar + status + versi aktual: `_meta/INDEKS_SISTEM.md`; manifest tiap sistem di root foldernya.
- Bukti pertama recovery nyata: pilot-002 behavioral (riwayat; jejaknya di area master-only, disebut tanpa backtick).
- Regression struktural dijaga alat di `tools/` — jalankan sendiri untuk verifikasi, jangan percaya klaim sesi sebelumnya.
- platform lmarena: branch `arena/` dibuat otomatis, tidak bisa push setelah merge/close, sesi bisa crash — lihat `_meta/PLATFORM_LMARENA.md`;
- log sesi berkelanjutan (`LOG_SESI_YYYY-MM-DD.md`) wajib untuk mitigasi crash platform: append + commit + push setelah tiap pertukaran yang menghasilkan informasi baru; header "Keadaan Sesi" selalu segar; `CLOSED` di akhir sesi. Filter anti-bising WAJIB — lihat `PROTOKOL_CHECKPOINT_RECOVERY.md` bagian "Log Sesi Berkelanjutan".

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
