# Indeks Sistem

### Daftar semua sistem yang ada di repo ini, dengan status dan tanggal terakhir disentuh. Dicatat MANUAL oleh agent setiap kali selesai kerja di suatu sistem — TIDAK mengandalkan pembacaan git history. Dibaca di awal sesi untuk menentukan apakah perlu menawarkan audit sebelum lanjut kerja (lihat `00_CARA_KERJA_META.md`).

---

## Cara pakai

- **Sebelum mulai kerja di suatu sistem:** cek baris sistem itu di tabel bawah. Kalau "Terakhir Disentuh" sudah lama (pengguna yang menilai apa itu "lama" — tidak ada angka pasti, tergantung konteks), tawarkan audit dulu.
- **Setelah selesai kerja di suatu sistem (apapun jenis kerjanya):** update baris sistem itu — tanggal hari ini, dan status terbaru.
- **Sistem baru:** tambah baris baru begitu `00_RENCANA_KERANGKA.md`-nya sudah di-merge ke `main` (lihat `01_DISCOVERY_LEVEL_0.md`).

---

## Daftar Sistem

| Nama Sistem | Folder | Status | Terakhir Disentuh | Catatan |
|---|---|---|---|---|
| Sistem Presentasi | `sistem-presentasi/` | **mandiri** — bukti: python3 tools/check_selfcontained.py --sistem sistem-presentasi --report (berakhir PASS) | 9 September 2026 | Folder lolos gerbang deliverable: dokumen master yang benar-benar dipakai ikut sebagai salinan berlabel di direktori _salinan-meta/, rujukan asal-usul dan area yang tidak boleh keluar dari master ditulis sebagai provenance tanpa backtick, dan rujukan ke diri sendiri ditulis relatif terhadap folder. Bukti terbaru di `sistem-presentasi/ACCEPTANCE_TEST_LOG.md`. |
| Sistem Konten Kreator | `sistem-konten-kreator/` | **mandiri** — bukti: python3 tools/check_selfcontained.py --sistem sistem-konten-kreator --report (berakhir PASS) | 10 September 2026 | Folder lolos gerbang deliverable: dokumen master yang benar-benar dipakai ikut sebagai salinan berlabel di direktori _salinan-meta/, rujukan asal-usul (termasuk protokol yang sudah punya varian sendiri di folder ini) dan area yang tidak boleh keluar dari master ditulis sebagai provenance tanpa backtick. Bukti terbaru di `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md`. Pasca-produksi 10 September 2026: unit produksi pintu-kos tuntas (PR #36, merge `fccf0b6`); folder `_produksi-aktif/` unit itu dihapus setelah verifikasi arsip di `main` (housekeeping, PR menyusul). |
| Sistem Klinik | `sistem-klinik/` | Kerangka dibuat, isi belum | 11 September 2026 | Baru di Discovery Level-0 (sesi 11 Sep 2026): sistem perawatan & penajaman mandiri-untuk-repo-milik-pemilik (sasarannya keadaan, bukan umur: sistem lama pra-meta maupun sistem baru pasca-meta yang mau di-upgrade/diksa) — kit suntik (default, melebur lalu hilang, idempoten) + bengkel (pengecualian, staging branch-only, tidak pernah merge main). Rencana kerangka + manifest + pegangan + STATUS dalam PR pembuka; dokumen `_sistem/01`–`06` menyusul. TIDAK mengklaim mandiri sampai tahap siap-pakai. |

*(Tambah baris baru di bawah ini untuk tiap sistem baru yang dibangun)*

> **Catatan tanggal:** kolom "Terakhir Disentuh" mengikuti tanggal UTC sesi; peristiwa bertanggal WIB ditandai di log terkait. Riwayat penanggalan uji: `sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md`.

---

## Yang sengaja TIDAK didaftarkan di tabel ini

- **`sistem-pilot-catatan-belajar/`** — bukan sistem domain, melainkan **fixture uji** untuk memvalidasi meta-sistem itu sendiri (behavioral test, recovery test FI-01 s/d FI-07). Statusnya `pilot-only — not released` di manifestnya sendiri. Pengecualian ini **keputusan sadar**, bukan kelalaian pencatatan — jangan "diperbaiki" dengan menambahkannya ke tabel di atas. Kalau suatu saat pilot ini dipromosikan jadi sistem nyata, itu keputusan tersendiri yang dicatat dulu.
- **Meta-sistem (`_meta/`)** — ini kerangka yang menaungi semua sistem, bukan salah satu isinya. Statusnya dilacak di `_meta/SYSTEM_MANIFEST.md` (saat ini `Released — v1.13.2`, terakhir disentuh 11 September 2026: pegangan pengguna wajib + log sesi berkelanjutan (level repo/meta kini di folder `_log-sesi/`) + kontrak warisan W-01…W-09 + tools regresi berbasis INDEKS + protokol review independen + folder sistem sebagai deliverable + cakupan gerbang mandiri diselaraskan dengan definisi dokumen aktif + dua sistem domain lama dituntaskan menjadi folder mandiri + penutupan administratif PR #27 dan pembersihan angka korpus Handoff + hasil audit Mendalam 9 Sep: 4 perbaikan dokumen + housekeeping + adaptasi skenario FI R4 untuk sistem multi-unit + adaptasi FI R4 lanjut untuk sistem Tahap kerangka (11 Sep)).
  - **Bagian baru v1.13.2 (11 Sep 2026):** adaptasi FI R4 — seleksi target skenario melewati sistem ber-Tahap kerangka (merah palsu saat sistem baru lahir; invarian fail-closed pada siap-pakai utuh; tanpa perubahan pin) + baris Jumlah di dokumen FI disinkron dari keluaran alat. Dideklarasikan sebagai berkas pelindung di PR #43 (pembukaan `sistem-klinik/`). Menunggu review independen L1.
  - **Bagian baru v1.13.0 (9 Sep 2026):** perubahan mekanisme log sesi atas permintaan pemilik — semua `LOG_SESI_*.md` level repo/meta pindah dari root repo ke folder `_log-sesi/` (19 file via `git mv`) dan aturan lokasinya diubah seragam di semua dokumen yang menentukan (TEMPLATE_LOG_SESI, entry point 00, P2 platform, protokol checkpoint/recovery, bootstrap prompt, blok prompt universal root + template pegangan, aturan 00 KK + 2 prompt pegangan KK, 11_LOG_SESI presentasi, 2 salinan berlabel PLATFORM_LMARENA disinkron). Agent sesi baru kini diarahkan mencari log ke `_log-sesi/`, bukan root. Regresi AT-KK berlaku (aturan 00 berubah — aturan lokasi saja). Menunggu review independen L1.
  - **Bagian baru v1.12.2 (9 Sep 2026):** hasil audit Mendalam 7 lensa 9 Sep 2026 (laporan: `_meta/_internal/AUDIT_META_SISTEM_2026-09-09.md`) — (B-1) instruksi "repo sendiri" sistem-konten-kreator/_sistem/START_DI_SINI.md dikoreksi dari alat pensiun tools/pack_repo.py ke gerbang aktif (KK 0.3.7→0.3.8); (A-1) blok konteks `NEXT_SESSION_PROMPT.md` jadi ringkasan orientasi anti-basi (langkah 6/9 = anchor transformasi builder, sengaja tidak disentuh); (P-1) kedua ringkasan `_cadangan-claude/` disinkronkan (W-09); (P-2) gate M-18 dicentang — kedua branch yatim terverifikasi tidak ada di remote; (P-3) ZIP artefak root dihapus atas keputusan pemilik; (P-4) 29 branch remote lama ber-PR-MERGED dihapus atas delegasi pemilik; 3 branch tanpa PR (01a0772b/01a0776b/01a07fc0 — sesi eksplisit-tanpa-PR) dipertahankan menunggu keputusan pemilik. Tanpa satu pun perubahan rule atau alat. Menunggu review independen L1.
  - **Bagian baru v1.12.1 (9 Sep 2026):** penutupan administratif PR #27 dan pembersihan angka korpus Handoff — `_meta/_internal/HANDOFF_NEXT_SESSION.md` tidak lagi mengutip angka korpus (sebut perintah, bukan hasilnya; tidak menambah salinan berlabel dan tidak menambah rujukan ber-backtick ke dokumen aktif); `LOG_SESI_2026-09-09.md` ditutup dengan status `CLOSED` dan koreksi orientasi dicatat bahwa klaim "log 7–8 September sudah ditutup administratif" kini benar karena PR #28 menutup `LOG_SESI_2026-09-08_3.md`. Atas izin pemilik (mandat ini adalah izinnya); menunggu review independen L1.
  - **Bagian baru v1.12.0 (9 Sep 2026):** dua sistem domain lama dituntaskan menjadi folder mandiri — salinan berlabel untuk dokumen master yang benar-benar dipakai saat sistem dijalankan, provenance tanpa backtick untuk rujukan asal-usul dan untuk area yang tidak boleh keluar dari master, serta rujukan ke diri sendiri yang ditulis relatif terhadap folder; `tools/check_selfcontained.py --semua` kini berakhir PASS. Tiga kerja administratif dari review PR #27 ikut dikerjakan (komentar skenario injeksi kegagalan diselaraskan ke SC6–SC10; log PR #23 ditutup administratif; `_meta/00_CARA_KERJA_META.md` mendapat satu butir penunjuk bahwa norma hidup dan cakupan penegakannya ada di `_meta/PAKET_REPO_MANDIRI.md` v2.1). Menunggu review independen L1; alat hanya disentuh pada teks komentar, tanpa satu pun nilai pin yang diubah.
  - **Bagian baru v1.11.0 (9 Sep 2026):** cakupan `tools/check_selfcontained.py` diselaraskan dengan aturan repo yang lain lewat definisi bersama di `tools/checkpoint_core.py` — yang ditegakkan hanya dokumen aktif (rujukan dokumen bukti/mentah dicetak sebagai rujukan historis, tidak ditagih salinan), rujukan berbentuk direktori adalah sebutan area dan bukan kegagalan, serta area yang tidak boleh keluar dari master diminta sebagai provenance tanpa backtick, bukan sebagai salinan berlabel (salinan yang terlanjur ada dari area itu = temuan). Norma diselaraskan di `_meta/PAKET_REPO_MANDIRI.md` v2.1 + AT-17 (L8–L10) supaya alat dan dokumen tidak berbeda; regresi baru SC6–SC10 diuji-mutasi. Dua sistem domain lama tetap belum mandiri — daftar kerjanya lebih pendek dan tetap milik PR B/C. Disetujui pemilik PR A2; menunggu review independen L1.
  - **Bagian baru v1.10.0 (8 Sep 2026):** protokol folder mandiri menggantikan packager lama; alat baru `tools/check_selfcontained.py` menjadi gerbang selesai; tools/pack_repo.py pensiun dengan jejak di `_meta/PAKET_REPO_MANDIRI.md`; template bersih membawa sistem-benih dengan validator dan satu salinan berlabel nyata. Disetujui pemilik PR A; menunggu review independen L1.
  - **Bagian baru v1.9.0 (8 Sep 2026):** prompt review independen dibangkitkan alat, bukan dikarang — pembangkit baru di `tools/` (nomor PR, base/head sha, daftar berkas pelindung diambil dari data PR di GitHub), bagian "Sumber prompt" di `_meta/PROTOKOL_REVIEW_INDEPENDEN.md`, satu baris checklist penutupan sesi di `_meta/00_CARA_KERJA_META.md` + `_meta/DEFINITION_OF_DONE.md`, bagian "Minta Review, Tanpa Perantara" di `PANDUAN_PENGGUNA.md` + langkah penutup di `PROMPT_ENTRI_UNIVERSAL.md`. Disetujui pemilik 8 Sep 2026 ("mekanisme harus bisa dipakai tanpa perantara sesi"). Menunggu review independen L1; penggabungan = keputusan pemilik langsung.
  - **File baru v1.6.0 (8 Sep 2026):** perbaikan akar masalah bukti basi — cakupan pemindaian jadi SATU definisi `dokumen_aktif()` di `tools/checkpoint_core.py`. Pada masa packager lama, definisi ini juga dipakai untuk benih subset meta; mekanisme itu kini pensiun. Berkas yang saat itu diubah termasuk checkpoint_core, validator, packager lama, injeksi kegagalan, protokol paket, acceptance tests, dan failure injection tests.
  - **File baru v1.5.0 (7 Sep 2026):** `_meta/PAKET_REPO_MANDIRI.md` lahir sebagai protokol paket repo mandiri lama; alat pelaksananya tools/pack_repo.py kini pensiun per keputusan pemilik 8 Sep 2026.
  - **File baru v1.4.0 (6 Sep 2026):** `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` — review independen oleh SESI LAIN sebagai lapisan verifikasi eksternal (permintaan pengguna pasca-F7); rujukan 1 baris di `QUALITY_ASSURANCE_AND_EVOLUTION.md`.

---

## Legenda Status

- **Kerangka dibuat, isi belum** — `00_RENCANA_KERANGKA.md` sudah ada dan di-merge, tapi dokumen-dokumen isinya belum mulai digali
- **Sedang dibangun** — sebagian dokumen sudah digali/ditulis, belum semua selesai
- **Selesai, belum diaudit** — semua dokumen yang direncanakan sudah ditulis, tapi belum melalui audit menyeluruh
- **Selesai, teraudit [n]x** — sudah melalui audit menyeluruh sebanyak n kali, siap dipakai
- **Aktif dipakai** — sedang dipakai untuk kerja produksi/operasional sehari-hari (bukan lagi tahap pembangunan)


## Catatan historis pemindahan repo mandiri lama — 2026-09-08

- Sistem Presentasi: percobaan pemindahan lama tidak menjadi bukti kemandirian folder. Status berlaku sekarang: belum mandiri — jalankan python3 tools/check_selfcontained.py --sistem sistem-presentasi.
- Sistem Konten Kreator: percobaan pemindahan lama tidak menjadi bukti kemandirian folder. Status berlaku sekarang: belum mandiri — jalankan python3 tools/check_selfcontained.py --sistem sistem-konten-kreator.
- **Pembaruan 9 September 2026 (menggantikan kalimat "berlaku sekarang" pada dua baris di atas):** kedua sistem kini **mandiri** menurut gerbang deliverable — perintah pembuktiannya sama, hasilnya PASS. Lihat tabel Daftar Sistem di atas; dua baris lama di atas sengaja dibiarkan sebagai riwayat.
