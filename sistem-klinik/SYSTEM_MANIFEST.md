# System Manifest — Sistem Klinik

> Manifest ini adalah kartu identitas dan kontrak navigasi sebuah sistem domain. Ini bukan pengganti dokumen instruksi atau living document.

## Identitas

- **Nama sistem:** Sistem Klinik (Klinik Sistem) — merawat sistem-sistem mandiri milik pengguna, segala umur (K-7, 11 Sep 2026): lahir sebelum meta dan belum terawat, atau lahir sesudahnya dan ingin ditingkatkan/diksa ulang
- **Tujuan utama:** satu folder kit disalin ke repo sistem target + satu prompt → agent mengaudit terhadap katalog cacat, menanam mekanisme yang hilang, meng-upgrade, memverifikasi, mencatat rekam klinik, memanen temuan untuk evolusi kit (Tahap F), lalu kit melebur dan hilang — target terlihat normal tapi terukur lebih baik; dapat diulang kapan saja dan idempoten
- **Pengguna/consumer:** pemilik repo ini sendiri; tidak ada audiens eksternal
- **Pemilik keputusan:** pemilik repo (semua gerbang Besar + merge di repo target adalah haknya)
- **Versi:** `0.2.0`
- **Tahap:** siap-pakai — cek W-01/W-02/W-03 kembali ketat sudah dilakukan 14 Sep (validator ketat hijau; lihat _meta/03_KONTRAK_WARISAN.md bagian "Tahap pembangunan" — provenance)
- **Status:** `Siap dipakai` — seluruh Langkah 1–7 rencana selesai (dokumen 01–06 + kit terakit + START_DI_SINI + acceptance test lulus, bukti ACCEPTANCE_TEST_LOG.md); flip Tahap atas delegasi pemilik 14 Sep (Log Keputusan); K-11 (14 Sep UTC/15 Sep WIB): panggung BENGKEL dihapus — rawat inap kini = alur standar meta di folder sistem target + aturan klinik, kit eksklusif suntik; versi 0.2.0. Menyusul (bukan syarat pakai): PR housekeeping "folder output sistem" (keputusan 15 Sep WIB — sesi berikutnya, struktur `sistem/`, nama folder tidak berubah), PR meta Bagian B, RINGKASAN cadangan (W-09, Langkah 10), run pertama.
- **Tanggal dibuat:** 11 September 2026 (UTC)
- **Audit terakhir:** 14 September 2026 — audit matkangan pra-run + acceptance test pertama (AT-KL-01/02); CATATAN JUJUR: audit itu berjalan SEBELUM perubahan aturan inti 01 di PR ini → trigger audit (c) kini terpicu dan audit susulan dijadwalkan (keputusan pemilik 14 Sep: cukup perbaikan artefak + verifikasi putaran 2; clean-run penuh menyatu dengan run pertama)
- **Quality protocol (versi sistem ini — self-contained):** trigger audit, level default, dan prosedur rollback dirinci di bagian "Quality & Evolution" manifest ini; verifikasi output oleh ACCEPTANCE_TESTS.md (dibangun saat dokumen jadi; memakai `_fixture/`). Induk: _meta/QUALITY_ASSURANCE_AND_EVOLUTION.md di master = provenance saja (sistem harus tetap berfungsi penuh bila foldernya diunduh standalone)

## Bentuk Sistem

- **Bentuk:** [ ] Bertingkat  [x] Flat  [ ] Siklus  [x] Gabungan (FLAT di level dokumen + SIKLUS di level kerja; dua panggung satu siklus (K-11): rawat-jalan/suntik = target di repo eksternal (kit), rawat-inap = folder sistem target di repo meta ini — alur standar meta + aturan klinik)
- **Unit kerja utama:** 1 run = 1 kunjungan ke 1 sistem target (Tahap A Pendaftaran → B Diagnosis → [G-Rencana] → C Tindakan → D Verifikasi → E Catatan → F Panen → [G-Final] → Peleburan & PR/serah-terima — sinkron urutan kanonik di 01_ALUR_RUN)
- **Kriteria satu unit selesai:** semua item disetujui terpasang + verifikasi tercatat + REKAM-KLINIK ditulis dengan cap versi kit + folder kit hilang dari git target (suntik) atau sistem target ter-merge ke `main` + terdaftar di INDEKS (rawat inap, K-11) + PR terbuka tanpa auto-merge; merge = pemilik
- **Titik approval Besar:** G-Rencana (sebelum menyentuh target); per-item overwrite/hapus konten target; per-item install kapabilitas (plugin/skill — selalu tawaran); G-Final; merge/discharge
- **Titik approval Kecil:** penanaman file baru non-destruktif, log, STATUS, verifikasi read-only — jalan + lapor di G-Final

## Dokumen Navigasi

- **Entry point:** `START_DI_SINI.md` (selesai dibangun 14 Sep — urutan baca per jenis sesi: pembangunan / siap-run suntik / run rawat inap / audit kit / review PR; jenis sesi 3 ditulis ulang K-11, 14 Sep UTC/15 Sep WIB)
- **Dokumen instruksi aktif:** `_sistem/01_ALUR_RUN.md` dan `_sistem/03_KEBIJAKAN_LEBUR.md` sudah dibangun (dokumen lainnya: 02, 04, 05, 06 juga sudah dibangun).
- **Living documents:** 02_KATALOG_CACAT — daftar hidup; dokumen ini; STATUS.md
- **Log keputusan:** tabel Log Keputusan di bawah (dokumen hidup lain membawa tabelnya masing-masing saat dibangun — W-05)
- **Ringkasan cadangan:** belum ada — _cadangan-claude/RINGKASAN_sistem-klinik.md dibuat saat struktur stabil (W-09, status "menyusul" tercatat resmi di sini)
- **Laporan audit:** belum ada sebagai dokumen tersendiri — bukti audit matkangan 14 Sep: ACCEPTANCE_TEST_LOG.md + entri log sesi 2026-09-14; audit susulan pasca-perubahan aturan 01 menyusul (trigger (c), lihat field "Audit terakhir")
- **Pegangan pengguna:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` di dalam folder sistem ini — final 14 Sep saat flip siap-pakai: prompt pembuka kini menunjuk START_DI_SINI.md sebagai entry point wajib (klausa kondisional era kerangka dihapus identik di kedua berkas)

## Prinsip

| Prinsip meta-sistem | Berlaku? | Cara diterapkan | Alasan jika di-override |
|---|---|---|---|
| Hierarki | Di-override (cara penerapan, bukan penonaktifan) | Model master→turunan berlabel: aturan tinggal di _sistem/, kit membawa turunan berlabel versi; target menerima hasil, bukan mewarisi keputusan antar-lapis | Bentuk klinik flat-lintas-target; tidak ada lapisan brief yang bisa diwariskan; digali dan disepakati di Discovery Level-0 11 Sep 2026 |
| Chaining | Ya | Tahap A–E berantai; agent baca artefak tahap sebelumnya langsung dari repo target; gerbang tetap menghentikan | — |
| Approval bertingkat | Ya (kriteria spesifik di Bentuk Sistem) | Besar/Kecil dikunci di 00_RENCANA_KERANGKA.md bagian Titik Penguncian | — |
| Checkpoint & verifikasi | Ya — dan merupakan ISI sistem | Mekanisme pemulihan justru ditanam ke target (Kontrak Tanaman); untuk dirinya: run punya STATUS + LOG_SESI | — |
| Log keputusan | Ya | Semua dokumen hidup (02, 04, 05, 06, manifest) wajib tabel; tanaman ke target membawa tabelnya | — |
| Quality assurance & evolusi (prinsip 6) | Ya, kedalaman bertahap | L1: acceptance test di _fixture (AT-KL); L2: cek ritme kit (06_RITME_KIT); L3: laporan verifikasi per run = objek output; rollback = PR balikan + rekam menandai | — |

## Warisan (Kontrak)

Status butir 03_KONTRAK_WARISAN.md (provenance) untuk sistem ini — salinan bagian "Warisan" di 00_RENCANA_KERANGKA.md; default SEMUA diterapkan:

| Butir | Status (diterapkan / override) | Letak di folder sistem | Override? |
|---|---|---|---|
| W-01 pegangan | diterapkan | PANDUAN_PENGGUNA.md + PROMPT_ENTRI_UNIVERSAL.md (root sistem); sisi target: PROMPT-ENTRI-KIT.md + PROMPT-PENUTUP-KIT.md di kit | — |
| W-02 LOG_SESI | diterapkan | 10_LOG_SESI.md (aturan self-contained sistem ini); turunan untuk target masuk kit | — |
| W-03 field checkpoint STATUS | diterapkan | STATUS.md (unit pembangunan sistem ini; field deterministik exact); TEMPLATE-STATUS-TARGET.md masuk kit | — |
| W-04 manifest | diterapkan | SYSTEM_MANIFEST.md ini — dibuat pada PR yang sama dengan rencana kerangka (pola M-14) | — |
| W-05 log keputusan | diterapkan | tabel Log Keputusan di bawah + di semua dokumen hidup saat dibangun | — |
| W-06 QA 3-lapis | diterapkan (ringkas di dalam folder) | bagian Quality & Evolution ini + ACCEPTANCE_TESTS.md/_fixture; aturan tidak dihilangkan, hanya dikedalaman-bertahapkan | — |
| W-07 fakta platform | diterapkan | bagian Batasan Platform di bawah + diturunkan ke 01_ALUR_RUN dan turunan kit | — |
| W-08 approval bertingkat | diterapkan | kriteria Besar/Kecil konkret dikunci di 00_RENCANA_KERANGKA.md Titik Penguncian + Bentuk Sistem di atas | — |
| W-09 ringkasan cadangan | diterapkan — menyusuli alur (dibuat saat struktur stabil) | _cadangan-claude/RINGKASAN_sistem-klinik.md di master (belum dibuat — dicatat sadar, bukan kelalaian) | — |

## Quality & Evolution

- **Lapisan self-audit sistem:** setiap perubahan aturan di _sistem/ atau kit/ wajib lolos ACCEPTANCE_TESTS (termasuk uji idempotensi di fixture) + cek ritme kit (sinkron master→kit) sebelum merge
- **Lapisan verifikasi output:** per run, laporan verifikasi Tahap D adalah objek output (diperiksa G-Final oleh pemilik); regresi alat portabel dijalankan di repo target, hasilnya dicatat di rekam klinik
- **Trigger audit:** (a) setiap 3 run selesai, (b) temuan cacat yang berulang di 2+ target, (c) perubahan dokumen aturan inti, (d) perintah pemilik
- **Level audit default:** Sedang (ringan saat kerangka, naik saat kit pertama dipakai run nyata)
- **Prosedur rollback:** perubahan aturan kit/_sistem = PR balikan + baris di rekam klinik target menyatakan "mekanisme X dinonaktifkan via rollback <commit/PR>"; tidak pernah menghapus diam-diam tanaman di target tanpa persetujuan per-item
- **Override quality protocol:** Tidak ada

## Dependency dan Risiko

- **Dependency eksternal:** untuk run rawat-jalan: akses sesi agent di repo target (mayoritas lmarena; kadang Claude Code/Antigravity — aturan ditulis netral-platform dengan bagian khusus lmarena). Untuk tawaran kapabilitas: akses internet riset + kelayakan vendor per-runtime (digali di 05A, BELUM diasumsikan terbukti)
- **Data yang wajib ada:** REKAM-KLINIK (atau padanan konvensi target) di setiap sistem terawat — tanpa itu run berikutnya kehilangan dasar idempotensi
- **Risiko utama:** (1) kit dianggap invasif oleh agent target (mitigasi: Kebijakan Lebur #2 + kit tak pernah masuk git); (2) katalog cacat jadi dogma basi (mitigasi: hidup, Log Keputusan, trigger audit); (3) paritas kit mendorong duplikasi alat meta (mitigasi: 06_RITME_KIT — subset portabel, bukan fork)
- **Batasan yang diketahui:** target repo besar di luar meta = pakai panggung suntik (kit), TIDAK disalin ke repo meta (K-11) — bila aset sangat besar menghendaki begitu, keputusan + alasannya dicatat di laporan diagnosis (Tahap A langkah 6); target tanpa git/gh (repo lokal sederhana) = panggung rawat inap (letakkannya di repo ini — alurnya di sini punya git+gh); kemampuan alat di environment target TIDAK dijamin sama dengan meta — alat portabel harus stdlib-only dan diuji di `_fixture/`, bukan diasumsikan
- **Prosedur recovery:** aturan pemulihan per sesi = turunan checkpoint meta yang ditanam (log sesi + STATUS deterministik); untuk sistem ini sendiri: LOG_SESI + STATUS di repo meta — pola standar

## Batasan Platform

- **Dipakai via lmarena?** Ya
- **Jika Ya:** fakta platform menurunkan sistem ini secara kausal (provenance: _meta/PLATFORM_LMARENA.md — tidak bisa, bukan jangan): (1) branch arena otomatis dibuat, kerja TIDAK terjadi di main; (2) setelah PR di-merge/di-close sesi TIDAK BISA push lagi — file pasca-merge terjebak, workaround /download-workspace; karena itu run klinik di repo target pun wajib menyelesaikan semua commit sebelum pemilik me-merge, dan PR rawat inap wajib di-merge sebelum sesi kehilangan akses push (fakta 2); (3) sesi bisa crash — karena itu aturan log sesi berkelanjutan + STATUS deterministik wajib bagi sistem ini DAN merupakan isi Kontrak Tanaman yang ditanam ke target (mekanisme pemulihan konteks adalah produk utama klinik). Pemakaian target di runtime lain (Claude Code/Antigravity — jarang): aturan ditulis netral-platform; bagian lmarena menjadi opsional-aktif sesuai environment target.
- **Jika Tidak:** —

## Acceptance

- [x] Semua dokumen wajib tersedia (tuntas 14 Sep — Langkah 1–7 rencana; START_DI_SINI dibuat, AT lulus; dicentang saat flip siap-pakai)
- [x] Semua dependency valid (akses sesi agent di repo target + riset kapabilitas dinyatakan sebagai kebutuhan, bukan asumsi terbukti — dinyatakan jujur di Dependency)
- [x] Status dan versi sudah diperbarui (0.2.0 / Siap dipakai — flip atas delegasi pemilik 14 Sep; K-11 + naik versi 14 Sep UTC/15 Sep WIB)
- [x] Approval yang diperlukan sudah ada (review menyeluruh rencana = merge PR #43; Langkah 7 = mandat pemilik 14 Sep; flip+ratifikasi = delegasi eksplisit 14 Sep, ratifikasi akhir di gerbang merge PR ini)
- [ ] Audit terakhir tercatat — catatan matkangan 14 Sep ada (ACCEPTANCE_TEST_LOG + log sesi), tetapi laporan audit formal belum ada dan audit susulan pasca-perubahan aturan 01 (trigger (c)) belum dijalankan — jujur belum tercentang
- [ ] Ringkasan cadangan sinkron (menyusul — W-09, Langkah 10 rencana; tercatat sadar, bukan kelalaian)
- [x] Pegangan pengguna tersedia di dalam folder sistem (prompt pembuka + prompt penutup) — dua file root ada sejak kerangka; prompt pembuka terbukti bekerja (sesi 14 Sep dibuka dengannya)

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-11 | Manifest dibuat bersama rencana kerangka (satu PR) | Pola M-14: manifest menyusul setelah merge adalah temuan lama — dilarang |
| 2026-09-11 | Prinsip Hierarki di-override cara penerapan (master→turunan berlabel) | Bentuk flat-lintas-target diputuskan di Discovery Level-0; penyesuaian cara bukan penonaktifan butir W — tidak butuh prosedur override kontrak |
| 2026-09-11 | Nama sistem: Sistem Klinik (Klinik Sistem); "Medical Sistem" dicoret | Rekomendasi agent atas pertanyaan pemilik — "Medical" campur bahasa + mengesankan domain medis; metafora klinik membuat mode (rawat-jalan=suntik, rawat-inap=bengkel, rekam=riwayat) konsisten dan mudah dijelaskan |
| 2026-09-13 | K-9 hygiene anti-bengkak bengkel: salinan minimal, aset di-exclude (tercatat), branch dihapus pasca-pemulangan, PR = laporan saja | Kritis pemilik: branch ter-push tetap masuk store meski tak di-merge ke main — bengkak dibatasi+sementara; suntik tetap default karena nol-byte di meta (tabel K rencana + _bengkel/README) |
| 2026-09-13 | K-10 model tanya approval: borongan ≤±5 butir/pesan + penjelasan fungsi/tujuan/alasan per tawaran + slot usulan pemilik; jawaban dicatat persis | Permintaan eksplisit pemilik 13 Sep 2026 — bahan gali wajib 01_ALUR_RUN dan 05_TAWARAN_KAPABILITAS (tabel K + Titik Penguncian rencana) |
| 2026-09-13 | Baris "Unit kerja utama" disinkron: menyebut F Panen + urutan kanonik E→F→[G-Final]→Peleburan | Rekonsiliasi diagram-vs-gerbang rencana disetujui pemilik 13 Sep (ask_user: setuju + sync_sekarang); sumber: 01_ALUR_RUN bagian 2 + Log Keputusannya |
| 2026-09-11 | Target diperluas jadi tanpa-umur (K-7): sistem pra-meta maupun pasca-meta semuanya boleh disuntik | Pemilik menyatakan sendiri saat review rencana: "target tuh sebenarnya bukan hanya sistem lama, tapi juga bisa aja sistem yang baru yang dibuat setelah meta sistem ditingkatkan" — sasaran = keadaan, bukan umur; tidak perlu aturan baru, idempotensi (rekam klinik + cap versi) sudah melayani sistem yang lahir lengkap |
| 2026-09-14 | Langkah 7 rencana dikerjakan: START_DI_SINI.md lahir; acceptance test pertama dijalankan di fixture; temuan pre-audit AT-KL-02 diperbaiki (aturan anti-kit-usang di 01 §1.3 + Tahap A.4) → versi naik 0.1.1→0.1.2 | Mandat pemilik 14 Sep: "pastiin dulu sistem kliniknya udh matang" → tuntaskan Langkah 7 dulu; perbaikan aturan = hasil acceptance test sungguhan, bukan rencana awal (detail di ACCEPTANCE_TEST_LOG.md) |
| 2026-09-14 | Flip Tahap kerangka → siap-pakai; ratifikasi v0.1.2; PR penutup sesi dibuka | Delegasi eksplisit pemilik 14 Sep pada tiga gerbang (dua butir: "Dalam hal ini Aku ikut yang menurut kamu terbaik"; butir ketiga: "Dalam hal ini juga") — prasyarat flip dicek objektif (dokumen lengkap, AT lulus, validator hijau, syarat 03_KEBIJAKAN_LEBUR "run nyata baru sah setelah Tahap = siap-pakai"); ratifikasi PR = keputusan pemilik di gerbang merge |
| 2026-09-14 | Respons review independen putaran 1 PR #51 (MERAH, putaran 1/2): §1.3 benar-benar diisi (edit pertama hilang — kesalahan proses, transparan di log), 6/6 stamp kit `versi-kit 0.1.2`, bukti AT dikoreksi append-only (angka volatil dicabut, deviasi W-09 dideklarasikan), pegangan difinalkan (klausa kerangka dihapus), INDEKS disinkron dengan flip, kejujuran audit diperbaiki (checklist di-un-tick) | Reviewer putaran 1 menemukan 7 temuan + 1 tak terverifikasi — SEMUA diterima; pemilik memutuskan 14 Sep: flip DIPERTAHANKAN, F-8 cukup perbaikan artefak + putaran 2 (clean-run penuh menyatu dengan run pertama); ratifikasi akhir = review putaran 2 |
| 2026-09-14 UTC / 15 Sep WIB | K-11 diterapkan di seluruh sistem: panggung BENGKEL (staging `_bengkel/`) DIHAPUS — rawat inap kini = folder sistem target di repo meta + alur standar meta (branch→PR→merge, tanpa auto-merge) dijalankan dengan aturan klinik; master dibaca in-place (tanpa salin kit/stamp/peleburan); kit eksklusif suntik; versi 0.1.2 → 0.2.0; sistem pasca rawat inap TETAP warga kelas satu (INDEKS), hapus = keputusan sadar pemilik; ide pemilik "folder output untuk semua sistem" diterima sebagai housekeeping PR TERPISAH (struktur `sistem/`, nama folder tidak berubah; timing: sesi berikutnya pasca-merge PR ini) | Ratifikasi eksplisit pemilik (bukan delegasi) setelah analisis agent — alasan inti di 01_ALUR_RUN Log Keputusan baris K-11. Dampak audit: perubahan aturan inti → trigger (c) terpicu → audit penuh + acceptance re-run (termasuk AT-KL-03 baru) dijalankan dalam PR yang sama, sebelum merge |
| 2026-09-11 | Prinsip hidup ditalangkan sebagai mekanisme (K-8): Tahap F Panen wajib per run + ritme rilis kit lewat PR + cap versi = deteksi basi | Pemilik: "sistem klinik ini juga kayanya perlu dibuat hidup dalam artian terus berkembang" — agent setuju dengan syarat: hidup lewat gerbang (nihil-panen sah, diam tidak sah), bukan lewat mood; selaras Prinsip 6 QA & Evolusi |
