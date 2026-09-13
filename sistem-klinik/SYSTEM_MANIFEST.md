# System Manifest — Sistem Klinik

> Manifest ini adalah kartu identitas dan kontrak navigasi sebuah sistem domain. Ini bukan pengganti dokumen instruksi atau living document.

## Identitas

- **Nama sistem:** Sistem Klinik (Klinik Sistem) — merawat sistem-sistem mandiri milik pengguna, segala umur (K-7, 11 Sep 2026): lahir sebelum meta dan belum terawat, atau lahir sesudahnya dan ingin ditingkatkan/diksa ulang
- **Tujuan utama:** satu folder kit disalin ke repo sistem target + satu prompt → agent mengaudit terhadap katalog cacat, menanam mekanisme yang hilang, meng-upgrade, memverifikasi, mencatat rekam klinik, memanen temuan untuk evolusi kit (Tahap F), lalu kit melebur dan hilang — target terlihat normal tapi terukur lebih baik; dapat diulang kapan saja dan idempoten
- **Pengguna/consumer:** pemilik repo ini sendiri; tidak ada audiens eksternal
- **Pemilik keputusan:** pemilik repo (semua gerbang Besar + merge di repo target adalah haknya)
- **Versi:** `0.1.0`
- **Tahap:** kerangka — ubah ke `siap-pakai` saat sistem siap dipakai (cek W-01/W-02/W-03 kembali ketat; lihat _meta/03_KONTRAK_WARISAN.md bagian "Tahap pembangunan" — provenance)
- **Status:** `Proposed` — rencana kerangka menunggu review menyeluruh pemilik di PR pembuka sistem ini
- **Tanggal dibuat:** 11 September 2026 (UTC)
- **Audit terakhir:** belum ada (sistem baru; audit pertama terjadwal setelah dokumen inti + kit pertama jadi — lihat 00_RENCANA_KERANGKA.md bagian "Langkah setelah rencana merge")
- **Quality protocol (versi sistem ini — self-contained):** trigger audit, level default, dan prosedur rollback dirinci di bagian "Quality & Evolution" manifest ini; verifikasi output oleh ACCEPTANCE_TESTS.md (dibangun saat dokumen jadi; memakai `_fixture/`). Induk: _meta/QUALITY_ASSURANCE_AND_EVOLUTION.md di master = provenance saja (sistem harus tetap berfungsi penuh bila foldernya diunduh standalone)

## Bentuk Sistem

- **Bentuk:** [ ] Bertingkat  [x] Flat  [ ] Siklus  [x] Gabungan (FLAT di level dokumen + SIKLUS di level kerja; dua panggung satu siklus: rawat-jalan/suntik = default, rawat-inap/bengkel = pengecualian)
- **Unit kerja utama:** 1 run = 1 kunjungan ke 1 sistem target (Tahap A Pendaftaran → B Diagnosis → [G-Rencana] → C Tindakan → D Verifikasi → E Catatan → F Panen → [G-Final] → Peleburan & PR/serah-terima — sinkron urutan kanonik di 01_ALUR_RUN)
- **Kriteria satu unit selesai:** semua item disetujui terpasang + verifikasi tercatat + REKAM-KLINIK ditulis dengan cap versi kit + folder kit hilang dari git target + PR target terbuka tanpa auto-merge (atau patch bengkel diserahkan); merge = pemilik
- **Titik approval Besar:** G-Rencana (sebelum menyentuh target); per-item overwrite/hapus konten target; per-item install kapabilitas (plugin/skill — selalu tawaran); G-Final; merge/discharge
- **Titik approval Kecil:** penanaman file baru non-destruktif, log, STATUS, verifikasi read-only — jalan + lapor di G-Final

## Dokumen Navigasi

- **Entry point:** START_DI_SINI.md (dibangun setelah rencana merge; sementara: baca 00_RENCANA_KERANGKA.md dulu)
- **Dokumen instruksi aktif:** belum dibangun — rencana lengkap + fungsi tiap dokumen ada di 00_RENCANA_KERANGKA.md bagian "Rencana Dokumen"
- **Living documents:** 02_KATALOG_CACAT (menyusul dibuat) — daftar hidup; dokumen ini; STATUS.md
- **Log keputusan:** tabel Log Keputusan di bawah (dokumen hidup lain membawa tabelnya masing-masing saat dibangun — W-05)
- **Ringkasan cadangan:** belum ada — _cadangan-claude/RINGKASAN_sistem-klinik.md dibuat saat struktur stabil (W-09, status "menyusul" tercatat resmi di sini)
- **Laporan audit:** belum ada
- **Pegangan pengguna:** `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` di dalam folder sistem ini — sudah ada sejak kerangka (W-01); diperluas saat sistem siap-pakai

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
| W-01 pegangan | diterapkan | PANDUAN_PENGGUNA.md + PROMPT_ENTRI_UNIVERSAL.md (root sistem); sisi target: PROMPT-ENTRI-KIT.md + PROMPT-PENUTUP-KIT.md di kit (menyusul dibangun) | — |
| W-02 LOG_SESI | diterapkan | 10_LOG_SESI.md (aturan self-contained sistem ini); turunan untuk target masuk kit (menyusul) | — |
| W-03 field checkpoint STATUS | diterapkan | STATUS.md (unit pembangunan sistem ini; field deterministik exact); TEMPLATE-STATUS-TARGET.md masuk kit (menyusul) | — |
| W-04 manifest | diterapkan | SYSTEM_MANIFEST.md ini — dibuat pada PR yang sama dengan rencana kerangka (pola M-14) | — |
| W-05 log keputusan | diterapkan | tabel Log Keputusan di bawah + di semua dokumen hidup saat dibangun | — |
| W-06 QA 3-lapis | diterapkan (ringkas di dalam folder) | bagian Quality & Evolution ini + ACCEPTANCE_TESTS.md/_fixture (menyusul); aturan tidak dihilangkan, hanya dikedalaman-bertahapkan | — |
| W-07 fakta platform | diterapkan | bagian Batasan Platform di bawah + diturunkan ke 01_ALUR_RUN dan turunan kit (menyusul) | — |
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
- **Batasan yang diketahui:** target repo besar = tidak layak disalin ke meta (bengkel tetap dibatasi branch); sesi target mungkin tanpa gh/git remote (bengkel-fallback manual); kemampuan alat di environment target TIDAK dijamin sama dengan meta — alat portabel harus stdlib-only dan diuji di `_fixture/`, bukan diasumsikan
- **Prosedur recovery:** aturan pemulihan per sesi = turunan checkpoint meta yang ditanam (log sesi + STATUS deterministik); untuk sistem ini sendiri: LOG_SESI + STATUS di repo meta — pola standar

## Batasan Platform

- **Dipakai via lmarena?** Ya
- **Jika Ya:** fakta platform menurunkan sistem ini secara kausal (provenance: _meta/PLATFORM_LMARENA.md — tidak bisa, bukan jangan): (1) branch arena otomatis dibuat, kerja TIDAK terjadi di main; (2) setelah PR di-merge/di-close sesi TIDAK BISA push lagi — file pasca-merge terjebak, workaround /download-workspace; karena itu run klinik di repo target pun wajib menyelesaikan semua commit sebelum pemilik me-merge, dan hasil bengkel dipulangkan sebelum close PR; (3) sesi bisa crash — karena itu aturan log sesi berkelanjutan + STATUS deterministik wajib bagi sistem ini DAN merupakan isi Kontrak Tanaman yang ditanam ke target (mekanisme pemulihan konteks adalah produk utama klinik). Pemakaian target di runtime lain (Claude Code/Antigravity — jarang): aturan ditulis netral-platform; bagian lmarena menjadi opsional-aktif sesuai environment target.
- **Jika Tidak:** —

## Acceptance

- [ ] Semua dokumen wajib tersedia (menyusul — baru boleh dicentang di tahap siap-pakai)
- [ ] Semua dependency valid
- [x] Status dan versi sudah diperbarui (0.1.0 / Proposed — 11 Sep 2026)
- [ ] Approval yang diperlukan sudah ada (review menyeluruh rencana kerangka oleh pemilik = gerbang merge PR ini)
- [ ] Audit terakhir tercatat
- [ ] Ringkasan cadangan sinkron (menyusul — W-09)
- [x] Pegangan pengguna tersedia di dalam folder sistem (prompt pembuka + prompt penutup) — dua file root sudah ada sejak kerangka

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
| 2026-09-11 | Prinsip hidup ditalangkan sebagai mekanisme (K-8): Tahap F Panen wajib per run + ritme rilis kit lewat PR + cap versi = deteksi basi | Pemilik: "sistem klinik ini juga kayanya perlu dibuat hidup dalam artian terus berkembang" — agent setuju dengan syarat: hidup lewat gerbang (nihil-panen sah, diam tidak sah), bukan lewat mood; selaras Prinsip 6 QA & Evolusi |
