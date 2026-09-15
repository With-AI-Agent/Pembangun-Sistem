# Rencana Kerangka — Sistem Klinik (Klinik Sistem)

> **Status:** DRAF untuk review menyeluruh pemilik — penggabungan = keputusan pemilik (gerbang setara G3). PR ini WAJIB direview isi lengkapnya, bukan konfirmasi ringan (kategori Besar sesuai alur `_meta/01_DISCOVERY_LEVEL_0.md`).
> **Dibuat:** 11 September 2026 (UTC) — sesi `arena/01a08f2c-pembangun-sistem`.
> **Sumber diskusi:** `LOG_SESI_2026-09-11_3.md` di folder `_log-sesi/` — Discovery Level-0 putaran 1–2 (ide mentah pengguna near-verbatim, empat keputusan yang sudah dikonfirmasi: pembagian mode bersyarat, jejak minimal, approval dua gerbang, pertanyaan paritas kit).
> **INI BARU RENCANA.** Setelah di-merge, langkah berikutnya adalah menulis prompt Discovery detail untuk tiap dokumen bertanda [GENERATOR] — BUKAN langsung menulis isi sistemnya.

---

## Untuk Siapa/Apa

**Pemakai:** pengguna sendiri (pemilik repo meta ini dan pemilik semua sistem target).

**Yang "dipakai/diperbaiki" sistem ini:** sistem-sistem milik pengguna — SEGALA umur (keputusan pemilik 11 Sep 2026, K-7) dan SELURUH lokasi (K-11, 14 Sep UTC/15 Sep WIB): repo mandiri eksternal ATAU folder sistem yang diletakkan pemilik di repo meta ini — (a) lama, pra-meta, sudah berjalan jauh; (b) lama, sudah jadi tapi belum dipakai; (c) BARU, dibangun setelah meta ini matang namun ingin ditingkatkan/diksa. Yang dinilai klinik adalah **keadaan, bukan umur**: mekanisme yang dibutuhkan tapi belum tertanam (pemulihan konteks sesi terputus, mekanisme audit), fungsi yang kurang optimal, panduan/prompt di bawah standar meta, atau keteringgalan dari versi kit terakhir. Sistem yang lahir lengkap tidak dapat "tanam dua kali" — dia dapat run kontrol + upgrade; mekanisme idempoten (rekam klinik + cap versi) menanganinya tanpa aturan tambahan.

**Tujuan akhir kalau sistem ini dipakai dengan benar:** satu folder kit disalin ke repo target + SATU prompt dikirim → agent di target terorientasi penuh, mengaudit sistem terhadap daftar periksa yang jelas (bukan feeling), menyusun rencana perbaikan, menanamkan mekanisme yang hilang dengan ikut konvensi target, meng-upgrade fungsi yang kurang optimal, memverifikasi hasilnya, mencatat jejak yang bisa dibaca sesi mana pun — lalu folder kitnya melebur dan hilang: **target terlihat normal, tapi sudah terukur lebih baik**. Kapan-kapan perlu kontrol ulang: salin kit terbaru, jalankan lagi (idempoten — yang sudah terpasang diverifikasi, bukan ditanam dua kali). Untuk target di repo meta (rawat inap, K-11): siklus A–F-gerbangnya sama persis — bedanya master aturan klinik dibaca di tempatnya (tanpa salin kit/stamp/peleburan) dan PR/merge mengikuti alur standar meta.

**Yang secara eksplisit BUKAN tujuan sistem ini:** mengubah isi/keputusan domain sistem target (naskah, catatan, data milik pengguna tidak disentuh tanpa persetujuan); menggantikan meta-sistem ini (klinik bukan tempat membangun sistem baru dari nol — itu alur `_meta/`); menjadi tempat tinggal sistem target EKSTERNAL (suntik tidak pernah meletakkan apa pun di repo meta). Catatan historis: klausul "menjadi repo tempat sistem target tinggal permanen" dulu melarang semua bentuk tinggal; **K-11 mengubahnya secara sadar** — pengecualian sadar kini ada: target rawat inap TINGGAL di repo ini sebagai warga kelas satu (keputusan pemilik 14 Sep UTC/15 Sep WIB).

---

## Bentuk Dasar

**Gabungan FLAT (level dokumen) + SIKLUS (level kerja).**

- **FLAT** di level dokumen: sistem ini satu book-of-rules (kit) berisi dokumen-dokumen sejajar. TIDAK ada hierarki turunan ala Brand Core → Channel → Model → Produksi, karena yang "diwariskan" bukan keputusan konten per-lapis, melainkan **aturan run yang sama** ke semua target. Prinsip Hierarki meta di sini perannya diambil alih oleh: versi kit + katalog cacat terkunci di meta, target hanya menerima HASIL (artefak tertanam) — tidak ada lapisan keputusan target yang mengalir balik ke kit, kecuali temuan cacat baru (lihat Yang Harus Konsisten #1).
- **SIKLUS** di level kerja: 1 RUN = 1 kunjungan ke 1 sistem target, dengan tahap yang sama setiap kali:

```
Tahap A  PENDAFTARAN       target dicatat (nama, keadaan: dipakai/belum, versi kit terakhir)
Tahap B  DIAGNOSIS         audit menyeluruh terhadap katalog cacat + kontrak tanaman; hasil = laporan temuan + rencana perubahan
   ── G-RENCANA (gerbang, pemilik) ──
Tahap C  TINDAKAN          eksekusi rencana mengikuti Kebijakan Lebur; hal berbahaya minta izin per-item
Tahap D  VERIFIKASI        cek ulang per item perubahan + regresi alat portabel + konsistensi rujukan internal target
Tahap E  CATATAN & PELEBURAN  rekam klinik ditulis, cap versi kit, folder kit hilang dari repo target
Tahap F  PANEN               WAJIB setiap run: cacat baru / celah aturan / ide perbaikan kit
                             dilaporkan sebagai usulan balik ke meta (bisa nol — "nihil panen"
                             adalah nilai sah; diam tanpa laporan = tidak sah)
   ── G-FINAL (gerbang, pemilik: isi perubahan + panen sekaligus diputuskan) ── → PR ke repo target
      (merge = hak pemilik, pola G3); panen yang disetujui menjadi PR ke sistem-klinik di meta
```

**Dua panggung, SATU siklus** (jawaban pertanyaan pembagian mode pengguna):

| Panggung | Nama | Kapan | Mekanisme |
|---|---|---|---|
| **Rawat jalan** (suntikan) — DEFAULT | agent kerja di repo TARGET | hampir selalu: audit, penanaman, perbaikan terdokumentasi | folder kit disalin ke workspace target, TIDAK pernah ikut commit; hasil akhir = perubahan tertanam + rekam klinik; histori disimpan git & PR repo target sendiri — repo meta nol bengkak |
| **Rawat inap** — folder di repo META (K-11) | agent kerja di repo META, di folder sistem target itu sendiri | pemilik meletakkan folder sistem di repo meta: rombakan struktural berat, diksa ulang, atau target memang mau tinggal di meta | **alur standar meta**: branch kerja → PR → merge ke `main` oleh pemilik (tanpa auto-merge); master aturan klinik dibaca di tempatnya (tanpa salin kit); sistem TETAP di repo sebagai warga kelas satu (terdaftar di INDEKS_SISTEM); penghapusan = keputusan sadar pemilik yang dicatat di log |

**Aturan Paritas Kit** (jawaban pertanyaan pengguna "bisa nggak suntikannya dibikin semaksimal bengkel?" — BISA, dan ini yang menjadikannya default): kit membawa SEMUA yang dibutuhkan satu run: seluruh dokumen aturan (turunan self-contained), katalog cacat, kebijakan lebur, kontrak tanaman, prosedur tawaran kapabilitas, dan subset alat periksa yang PORTABEL (stdlib-only, tidak tahu-bentuk-repo: cek field STATUS deterministik, cek rujukan internal, cek rekam klinik). Yang TETAP tidak bisa disuntikkan ke repo eksternal — dilayani panggung rawat inap (K-11), di mana sistem memang berada di dalam repo meta: (1) riwayat mentah arsip audit meta — solusinya bukan ikut masuk kit, hasilnya DISTILASI ke katalog cacat saat kit dibangun; (2) pembuatan alat baru ad-hoc; (3) kerja multi-repo paralel. **Promosi:** kalau sebuah kebutuhan yang hanya rawat inap yang mampu layani terbukti berulang saat suntikan, dia dipotabelkan lalu dipromosikan masuk kit (lewat PR ke meta, tercatat di Log Keputusan) — paritas adalah target yang bergerak, bukan potret sekali jadi.

**Hygiene anti-bengkak bengkel (K-9, pemilik 13 Sep 2026)** — catatan kritis pemilik diterima: "branch saja tidak masuk main" TIDAK membuat repo remote bebas bloat — objek branch yang di-push tetap masuk store dan bertahan selama ref PR hidup (GC tidak dijamin). Aturan tidak-merge-ke-main mencegah bloat PERMANEN (histori main, checkout, klon masa depan); karena itu ukuran salinan bengkel diperketat (dokumen yang dibedah saja; aset di-exclude dan tercatat), branch dihapus setelah pemulangan, PR hanya mengangkut laporan — dan paritas suntik yang membuat segalanya layak: panggung default itu TIDAK menaruh apa pun di meta, jejaknya hidup di git target sendiri. *(K-11, 14 Sep UTC/15 Sep WIB: konsekuensi PANGGUNG K-9 — staging `_bengkel/`, kuota ukuran salinan, pulangkan-via-patch, hapus-branch — DICABUT: rawat inap kini berjalan sebagai alur standar meta di folder sistem itu sendiri (merge ke main adalah norma). Kekhawatiran bengkak K-9 tetap dihormati lewat dua penjaga: hanya sistem yang PEMILIK LETAKKAN yang masuk, dan penghapusannya adalah hak sadar pemilik (dicatat); housekeeping PR "folder output sistem" (struktur `sistem/`, nama folder tidak berubah) ditangani terpisah — keputusan 15 Sep WIB.)*

---

## Yang Harus Konsisten

Tujuh jangkar ini yang membuat hasil klinik bisa dipercaya lintas target dan lintas waktu — dan membuat sistem ini sendiri HIDUP (berevolusi lewat gerbang, bukan lewat mood sesi):

1. **Katalog Cacat = satu-satunya tolok ukur, hidup, dan bertambah lewat bukti.** Satu daftar periksa (temuan → gejala → cara periksa → pola perbaikan → tingkat risiko) yang sama dipakai ke SEMUA target, sehingga mutu hasil tidak tergantung mood sesi. SEED awal dari temuan audit yang sudah tercatat di meta ini (temuan M-xx, F-xx, skenario FI, temuan review PR — ditambang saat `02` dibangun, hasilnya distilasi netral-domain). Setiap run yang menemukan cacat baru menamainya → PR ke katalog. Ini jawaban atas "cacat sulit dijelaskan": tidak perlu didaftar dari ingatan sekarang — run pertama yang mengajarkan, dan run itu tercatat.
2. **Kebijakan Lebur (merge policy)** — aturan tanam permanen: (a) cek dulu apakah target sudah punya padanan (panduan/log/status/aturan) → EXTEND dokumen itu, jangan bikin dokumen kembar; (b) file baru hanya kalau memang tidak ada padanannya; (c) overwrite/deleting konten target TIDAK PERNAH tanpa persetujuan per-item; (d) artefak tertanam ikut KONVENSI target (bahasa, penamaan, format mereka), bukan format kit; (e) folder kit tidak pernah masuk git target (di `.gitignore` kerja selama run, dibersihkan saat peleburan); (f) istilah klinik tidak menular ke istilah sehari-hari target — kecuali target sudah punya istilah serupa, maka punya target yang menang.
3. **Kontrak Tanaman** — syarat minimum "sistem sudah dirawat": setiap sistem target pasca-run punya (a) aturan log sesi berkelanjutan turunan (format disalin, langkah cari-log-OPEN di prompt pembuka + tutup-log di prompt penutup), (b) kontrak STATUS unit dengan field deterministik `Pekerjaan belum tersimpan: Tidak ada` (nilai persis sesuai parser checkpoint meta) + `Waktu pembaruan`, (c) log keputusan di dokumen hidupnya, (d) pegangan pengguna/prompt pembuka kalau belum ada, (e) bagian fakta platform lmarena dengan bahasa kausal (dipakai via lmarena: ya, karena ini lingkungan utama target — lihat Putaran 2 jawaban pengguna). Terjemahan mandiri-butir W-01…W-09 — ditanam lewat `04_KONTRAK_TANAMAN.md`, disederhanakan untuk sistem kecil (mis. satu STATUS global untuk sistem 1-unit, tapi field deterministik WAJIB).
4. **Versi kit + cap di rekam klinik** — setiap run meninggalkan `REKAM-KLINIK.md` (atau padanannya ikut konvensi target) yang memuat: tanggal run, versi kit saat itu, temuan, daftar perubahan + status approval-nya, dan apa yang DITOLAK pemilik (supaya run berikutnya tidak menawarkan ulang hal yang sudah ditolak tanpa alasan baru). Kit berikutnya membaca ini duluan → idempotensi + anti-regresi.
5. **Gerbang yang tidak bisa ditawar** — G-Rencana sebelum menyentuh target (apa pun panggungnya) dan G-Final sebelum peleburan/PR; overwrite dan install kapabilitas selalu per-item. Tidak ada mode "agent percaya diri lanjut".
6. **Format rekam yang sama untuk dua panggung** — satu run rawat-jalan maupun rawat-inap menghasilkan artefak identik (laporan diagnosis, rencana, catatan tindakan, verifikasi); supaya hasil rawat inap bisa dievaluasi dengan mata yang sama dengan hasil suntikan.
7. **Ritme evolusi kit (prinsip hidup, K-8)** — kit hanya berubah lewat PR ke meta yang di-merge: setiap rilis = versi naik + satu baris di Log Evolusi (di manifest) + `kit/` dibangun ulang oleh `06_RITME_KIT`. Target tahu ketinggalan-zamannya dari cap versi di rekam klinik; jika cap < versi kit terbaru, run berikutnya WAJIB menawarkan "naik ke vX" sebagai item rencana (boleh ditolak pemilik; penolakan dicatat). Yang mengalir BALIK dari target ke meta hanyalah panen (Tahap F) dan temuan katalog — bukan konten target.

---

## Titik Penguncian/Approval

Model yang disetujui pemilik 11 Sep 2026 (dua gerbang + per-item untuk hal berbahaya):

| Titik | Apa yang dikunci | Kategori | Aturan |
|---|---|---|---|
| **G-Rencana** | laporan temuan diagnosis + rencana perubahan lengkap (item per item, termasuk mana yang tanam/extend/nolak) | **Besar** — wajib, satu-satunya gerbang sebelum target disentuh | pemilik review isi rencana (level rencana, bukan per-file) |
| **Per-item override** | setiap kali mau menimpa/menghapus file/konten target yang sudah ada | **Besar** — tidak bisa dibalik diam-diam | izin eksplistik per item, tercatat di rekam klinik + Log Keputusan target bila target punya |
| **Per-item kapabilitas** | install plugin/skill/tool apa pun (hasil riset) | **Besar** | SELALU lewat tawaran (lihat 05_TAWARAN_KAPABILITAS), pemilik boleh bilang tidak; penolakan dicatat supaya tidak ditawari ulang |
| **G-Final** | isi perubahan selesai + hasil verifikasi | **Besar** — review isi lengkap | sebelum peleburan kit + PR |
| **Discharge / merge** | merge ke main repo target (atau alur standar meta pada rawat inap) | **Besar** = hak pemilik penuh | sama pola G3 meta; agent tidak pernah auto-merge |
| Konfirmasi ringan (tanpa jeda) | tambahan file baru non-destruktif (menanam yang hilang), log, STATUS, verifikasi read-only | Kecil | jalan + lapor di G-Final |

**Model tanya (K-10, pemilik 13 Sep 2026)** — per-item TIDAK berarti per-momen. Seluruh keputusan per-item (override & install kapabilitas & butir Besar lain) DITANYA DIBORONG: satu daftar bernomor lengkap, tiap butir dengan fungsi/tujuan/alasan + cara pasang + risiko + alternatif, maks ±5 butir per pesan; selalu ada slot terbuka bagi pemilik untuk mengusulkan yang belum masuk; jawaban dicatat persis. Tidak ada mode "jalan-sedikit-tanya-lagi" dan tidak ada mode "banting 10 pertanyaan sekaligus".

**Satu unit kerja (1 run) dianggap SELESAI** kalau: semua item disetujui terpasang; verifikasi per item lolos dan tercatat; rekam klinik + cap versi kit ditulis; folder kit hilang dari repo target (peleburan = hanya artefak hasil yang masuk repo); PR target terbuka TANPA auto-merge (atau pada rawat inap: merge ke main di meta); G3-merge dilakukan pemilik. Tidak ada status "selesai" sebelum checklist itu lolos (pola DEFINITION_OF_DONE).

---

## Rencana Dokumen

Tanda: [ATURAN] = dokumen aturan ditulis langsung dari rencana ini. [GENERATOR] = perlu prompt Discovery detail sendiri, ditulis dari nol dulu baru dijalankan (pola Langkah 3 alur meta). [TEMPLATE] = template diisi langsung.

### Root folder sistem ini (sistem/sistem-klinik/ di repo meta)

| Dokumen | Fungsi | Tanda |
|---|---|---|
| `00_RENCANA_KERANGKA.md` | file ini — kontrak kerangka, disetujui lewat PR ini | — (sudah ada) |
| `SYSTEM_MANIFEST.md` | identitas + Tahap + tabel Warisan (dari template meta, PR yang sama — pola M-14) | [TEMPLATE] |
| `START_DI_SINI.md` | entry point sistem: urutan baca per jenis sesi (bangun kit / run suntik / run rawat inap / audit kit) | [ATURAN] |
| `STATUS.md` | status pembangunan sistem ini sendiri (unit meta bagi validator; field deterministik W-03) | [TEMPLATE] |
| `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` | pegangan pengguna sisi META (W-01): prompt pembuka universal klinik + prompt penutup sesi | [ATURAN] ikut template pegangan meta |
| `10_LOG_SESI.md` | aturan log sesi sistem ini, self-contained (W-02); file log klinik di `_log-sesi/` level repo | [ATURAN] |
| `ACCEPTANCE_TESTS.md` + `ACCEPTANCE_TEST_LOG.md` | skenario uji perilaku kit di `_fixture/` (AT-KL-xx) + bukti per run | [ATURAN]/[TEMPLATE] |

### Dokumen inti `_sistem/`

| Dokumen | Fungsi | Tanda | Catatan |
|---|---|---|---|
| `_sistem/01_ALUR_RUN.md` | siklus Tahap A–F + dua gerbang + adaptasi tiap panggung (suntik/rawat inap); format laporan diagnosis & rencana; aturan berhenti fail-closed; aturan Tahap F Panen (nihil-panen sah, diam tidak sah) | [ATURAN] | ditulis langsung — prinsipnya sudah diputuskan di Discovery ini |
| `_sistem/02_KATALOG_CACAT.md` | daftar hidup: ID temuan, gejala, cara periksa, pola perbaikan, risiko; SEED dari arsip meta + tambahan per run; aturan promosi temuan run → katalog | **[GENERATOR]** | butuh prompt gali `02A_PROMPT_SEED_KATALOG.md` (menambang arsip temuan meta secara sistematis, menterjemahkan ke netral-domain, redaksi sesuai aturan bukti) |
| `_sistem/03_KEBIJAKAN_LEBUR.md` | enam aturan tanam (extend>create, per-item overwrite, konvensi target menang, kit tak pernah di-git, istilah tak menular, rekam klinik wajib); contoh benar/salah | [ATURAN] | keputusan sudah digali; tinggal ditulis |
| `_sistem/04_KONTRAK_TANAMAN.md` | syarat minimum sistem terawat = turunan W-01…W-09 untuk repo mandiri; per butir: apa yang ditanam, bentuk sederhana untuk sistem kecil, cara verifikasi per tanaman | **[GENERATOR]** | butuh prompt gali `04A_PROMPT_KONTRAK_TANAMAN.md` (banyak keputusan terjemahan per butir) |
| `_sistem/05_TAWARAN_KAPABILITAS.md` | mekanisme tawaran riset plugin/skill: pemetaan kebutuhan sistem → kandidat (riset internet) → tabel rekomendasi (apa, dari mana, cara install, risiko, pengganti lokal) → keputusan pemilik → TANAM ke repo target (isi/vendor + prosedur) → registrasi di manifest target → wajib ditawarkan di SETIAP run dan di alur bangun/audit meta | **[GENERATOR]** | butuh prompt gali `05A_PROMPT_KAPABILITAS.md`; semantik "install" per runtime (lmarena = skrip/vendor dalam repo, Claude Code = folder skill) adalah inti yang harus digali, bukan ditebak |
| `_sistem/06_RITME_KIT.md` | perakitan `kit/`: dokumen mana yang ikut (turunan berlabel versi), alat portabel subset, stamp versi, prosedur sync master→kit + cek otomatis "kit tidak basi", aturan promotable (kemampuan rawat inap → portabel), ritme rilis (Log Evolusi + tawaran naik-versi ke target lama) | [ATURAN] | bergantung 02/04/05 stabil lebih dulu |

### Folder distribusi `kit/`

Kit = hasil rakitan (bukan sumber kebenaran; sumbernya master `_sistem/`):

```
kit/
├── PROMPT-ENTRI-KIT.md      ← SATU prompt yang dikirim pemilik di sesi target; isi: orientasi,
│                                 baca rekam klinik dulu, mode run, gerbang-gerbang, aturan lebur
├── PROMPT-PENUTUP-KIT.md    ← tutup log sesi target (CLOSED), PR tanpa auto-merge, checklist peleburan
├── aturan/                  ← turunan self-contained 01–06 (label asal-usul + versi kit di header)
├── alat/                    ← skrip stdlib-only periksa-target (field STATUS, rujukan internal,
│                                 format rekam) — TIDAK tahu-bentuk-repo, tidak impor alat meta
├── TEMPLATE-REKAM-KLINIK.md
└── TEMPLATE-LOG-SESI-TARGET.md + TEMPLATE-STATUS-TARGET.md
```

### Panggung & fixture

| Lokasi | Fungsi | Tanda |
|---|---|---|
| `_fixture/sistem-kecil-sakit/` | mini-sistem dummy TANPA mekanisme (rekaan cacat dari katalog) untuk acceptance test kit end-to-end: suntik → harus menanam + melebur + rekam; suntik dua kali → harus idempoten; rusak sengaja field STATUS → detektor harus merah; AT-KL-03: varian rawat inap (master in-place di salinan fixture /tmp, artefak identik) | [TEMPLATE] (dibangun saat `01`–`04` selesai; AT-KL-03 ditambahkan 14 Sep UTC/15 Sep WIB, K-11) |
| Pangkalan rawat inap (K-11) | folder sistem target di repo meta — TIDAK ada staging khusus (staging _bengkel/ dihapus K-11); lokasi mengikuti konvensi folder sistem repo ini, **sumber path-nya = indeks sistem repo ini (provenance area meta — tidak di-hardcode di aturan klinik, tidak disalin ke folder sistem)** | [ATURAN] |

### Bagian B — patch meta (PR TERPISAH, setelah rencana ini merge)

Penanaman fitur #5 permintaan pemilik ke seluruh alur meta:
1. `_meta/00_CARA_KERJA_META.md` — di alur "Membangun Sistem Baru" (setelah Langkah 1 Discovery) dan alur "Melanjutkan/Mengaudit" (langkah 2): langkah WAJIB-BERTAJUK **menawarkan** riset kapabilitas (plugin/skill) — tawaran, boleh ditolak; penolakan dicatat di Log Keputusan supaya tidak ditawari ulang. Sumber aturan turunan: `_sistem/05_TAWARAN_KAPABILITAS.md` di folder ini (meta menyimpan salinan aktifnya sendiri — dua-duanya disinkron lewat acceptance test kit AT-KL).
2. `_meta/01_DISCOVERY_LEVEL_0.md` — satu poin pertanyaan: "kapabilitas eksternal apa yang kemungkinan dibutuhkan sistem ini?" (jawaban masuk rencana kerangka, jadi acuan Langkah 3+).
3. Versi meta naik (minor), regresi penuh dijalankan, review independen sesuai protokol meta.

### Langkah setelah rencana merge (urutan bangun; 1 dokumen penuh dulu, baru berikutnya)

1. `01_ALUR_RUN.md` (paling fundamental: gerbang-gerbang) → 2. `03_KEBIJAKAN_LEBUR.md` → 3. tulis + jalankan prompt `02A` (seed katalog) → 4. tulis + jalankan prompt `04A` (kontrak tanaman) → 5. tulis + jalankan prompt `05A` (kapabilitas) → 6. `06_RITME_KIT.md` + rakit kit pertama → 7. `START_DI_SINI` + pegangan final + `_fixture` + acceptance test pertama di fixture (suntik-2x idempoten) → 8. PR meta Bagian B → 9. run PERTAMA di dunia nyata = salah satu sistem pemilik — panggung pilihan pemilik: suntik (repo eksternal) atau rawat inap (folder di repo meta, K-11); hasil dan cacat barunya masuk katalog (clean-run penuh menyatu dengan run pertama — keputusan pemilik 14 Sep) → 10. `INDEKS_SISTEM.md` status naik "Sedang dibangun"→dst, `RINGKASAN_sistem-klinik.md` dibuat di `_cadangan-claude/` begitu struktur stabil.

---

## Prinsip yang Dipakai / Di-override

Dari `_meta/02_PRINSIP_UNIVERSAL.md`:

| Prinsip | Keputusan | Catatan |
|---|---|---|
| 1. Hierarki | **Di-override sebagai hierarki dokumen — diganti model "master→turunan berlabel"** | Bentuk flat; yang mengalir ke target bukan keputusan bertingkat, melainkan aturan kit + rekam. Penjelasan di Bentuk Dasar. Override cara penerapan (bukan penonaktifan butir kontrak): alasan = domain klinik lintas-target, tidak ada lapisan brief |
| 2. Rantai/Chaining | **Dipakai** | Tahap A–E berantai, agent baca artefak tahap sebelumnya dari repo target sendiri; gerbang tetap wajib |
| 3. Approval Bertingkat | **Dipakai, kriteria spesifik di atas** | Besar = G-Rencana, per-item overwrite, per-item kapabilitas, G-Final, merge; Kecil = tanam non-destruktif + log |
| 4. Checkpoint & Verifikasi | **Dipakai + merupakan ISI utama sistem** | Klinik justru MENANAM mekanisme ini ke target (Kontrak Tanaman #3); untuk dirinya sendiri: run = unit dengan STATUS/LOG; target mayoritas lmarena → fakta platform diturunkan lewat kit |
| 5. Log Keputusan | **Dipakai** | Dokumen hidup klinik (02, 04, 05, 06, manifest) wajib tabel Log Keputusan; yang ditanam ke target juga membawa tabelnya |
| 6. QA & Evolusi 3-lapis | **Dipakai, kedalaman bertahap** | L1 meta→klinik: acceptance test di `_fixture/`; L2 klinik internal: cek sinkronisasi kit (`06`); L3 klinik→target: laporan verifikasi per-run adalah objek outputnya. Rollback kit = PR balikan + rekam klinik menandai "diinapkan" |

---

## Warisan (Kontrak)

Default SEMUA diterapkan (tidak ada yang di-offer satu-satu; tidak ada penonaktifan — kolom override kosong semua). Catatan bentuk khusus sistem ini: W-01…W-09 di sini berlaku DUA KALI — ditanam di sistem klinik sendiri, DAN menjadi isi Kontrak Tanaman untuk target.

| Butir | Status | Diterapkan bagaimana di sistem ini |
|---|---|---|
| W-01 pegangan | diterapkan | `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` di root folder sistem ini (sisi meta); sisi target: kit membawa `PROMPT-ENTRI-KIT.md` + `PROMPT-PENUTUP-KIT.md` |
| W-02 LOG_SESI | diterapkan | aturan self-contained di `10_LOG_SESI.md`; turunan + template masuk `kit/`; langkah cari-OPEN/buka-tutup sudah di blok pembuka/penutup |
| W-03 field checkpoint STATUS | diterapkan | `STATUS.md` sistem ini (unit pembangunan) + template status target di kit, field deterministik exact; validator global ikut mengawasi |
| W-04 manifest | diterapkan | `SYSTEM_MANIFEST.md` di PR yang sama dengan rencana ini; `Tahap: kerangka` |
| W-05 log keputusan | diterapkan | tabel Log Keputusan di semua dokumen hidup (`02`, `04`, `05`, `06`, manifest); target yang ditanami juga menerima tabelnya |
| W-06 QA 3-lapis | diterapkan (ringkas, versi sistem di dalam folder) | acceptance tests fixture + cek ritme kit + prosedur audit; kedalaman naik bertahap per dokumen selesai |
| W-07 fakta platform | diterapkan | bagian Batasan Platform di manifest + di `01_ALUR_RUN.md` + di turunan kit (dipakai via lmarena: Ya — mayoritas; fallback non-lmarena didefinisikan netral-platform) |
| W-08 approval bertingkat | diterapkan | kriterianya digali di Discovery ini, dikunci di bagian Titik Penguncian + manifest |
| W-09 ringkasan cadangan | diterapkan (menyusul sesuai alur) | `RINGKASAN_sistem-klinik.md` dibuat di `_cadangan-claude/` begitu struktur stabil (Langkah 10 di atas); sebelum itu status "menyusul" tercatat di manifest |

---

## Keputusan Pemilik yang Sudah Masuk (11 Sep 2026)

| # | Keputusan | Isi |
|---|---|---|
| K-1 | Pembagian mode | Suntikan default; bengkel pengecualian; aturan paritas kit + promosi kemampuan; anti-bengkak (copy hanya di branch). Disetujui pemilik dengan pertanyaan paritas yang dijawab di Bentuk Dasar |
| K-2 | Jejak peleburan | Folder kit hilang; jejak = `REKAM-KLINIK.md` + cap versi; histori penuh di git/PR target — "ikut saran terbaik" |
| K-3 | Model approval | Dua gerbang + per-item untuk overwrite & install kapabilitas — "ikut saran terbaik" |
| K-4 | Fitur kapabilitas | Split dua bagian: `_sistem/05` di kit + patch meta PR terpisah — disetujui eksplisit |
| K-5 | Daftar cacat awal | Tidak diminta dari ingatan pemilik; seed = tambang arsip temuan meta, tumbuh per run — usulan agent, tidak ditolak pemilik |
| K-6 | Nama | "Klinik Sistem" (folder sistem ini: sistem/sistem-klinik/) — usulan setelah pemilik menolak opsi sendiri untuk memilih; "Medical Sistem" tidak dipakai (campur bahasa + mengesankan domain medis). Kalau pemilik berubah pikiran, cukup diganti di review PR ini — belum ada yang menyinggung nama lain |
| K-7 | Target tanpa-umur | Pemilik 11 Sep 2026 (near-verbatim): "target tuh sebenarnya bukan hanya sistem lama, tapi juga bisa aja sistem yang baru yang dibuat setelah meta sistem ditingkatkan" → sasaran = keadaan, bukan umur; sistem baru yang lahir lengkap dilayani lewat jalur kontrol/upgrade yang sama (idempoten) |
| K-8 | Sistem hidup (berevolusi) | Pemilik 11 Sep 2026: "sistem klinik ini juga kayanya perlu dibuat hidup dalam artian terus berkembang" → ditaatkan sebagai MEKANISME, bukan niat: Tahap F Panen wajib tiap run + ritme rilis kit lewat PR + cap versi = deteksi ketinggalan zaman (konsisten dengan QA-3-lapis prinsip 6; "hidup" tidak berarti "liar") |
| K-9 | Anti-bengkak bengkel diperketat | Pemilik 13 Sep 2026 mengkritisi desain: "branch yang tidak di-merge ke main pun tetap bikin bengkak" — BENAR: objek branch ter-push masuk store repo (dan bertahan selama ref PR hidup). Aturan yang dikunci: (a) copy masuk bengkel SEADANYA — kerangka + dokumen yang dibedah saja, aset besar tidak ikut (daftar yang di-exclude tercatat di laporan diagnosis); (b) branch dihapus setelah pemulangan (keputusan sadar pemilik, bukan diam-diam); (c) PR bengkel hanya mengangkut berkas laporan; (d) konsekuensi disadari: bengkak bengkel dibatasi + sementara — dan justru karena itu suntik (yang tak memasukkan apa pun ke git meta) adalah DEFAULT sementara bengkel pengecualian ber-kuota |
| K-10 | Model tanya approval (anti bertele-tele) | Pemilik 13 Sep 2026 (near-verbatim): "jangan tanya, gerik dikit, tanya lagi — usahain tanya sekalian; tapi jangan 10 sekaligus, pusing; tiap tawaran skill/plugin jelaskan fungsi/tujuan/alasannya; beri kesempatan aku mengusulkan yang belum masuk" → dituangkan: (1) SEMUA keputusan per-item ditanya dalam BORONGAN — daftar bernomor lengkap (grup per kategori, maks ±5 per pesan), tanpa mode jalan-sedikit-tanya-lagi di tengah run; hal baru di luar rencana boleh ditanya susulan, asal diborong lagi; (2) tiap tawaran kapabilitas memuat: APA → fungsi/tujuannya → mengapa target INI butuh → cara pasang → risiko bila pasang → alternatif lokal → konsekuensi bila tidak; (3) tiap borongan tawaran ditutup slot terbuka: "ada fungsi/skill/plugin yang kamu mau tapi belum ada di daftar?"; (4) semua jawaban (terima/tolak/tunda + usulan pemilik) dicatat persis di Log Keputusan + rekam klinik — penolakan tidak ditawari ulang tanpa alasan baru; seluruhnya menjadi bahan wajib saat menggali 01_ALUR_RUN + 05_TAWARAN_KAPABILITAS |
| K-11 | Rawat inap disatukan ke alur standar meta — panggung BENGKEL terpisah dihapus | Pemilik 14 Sep UTC/15 Sep WIB (inti near-verbatim): "yang bengkel itu ga usah dibikin sebagai sesuatu terpisah, melainkan disatukan dengan mekanisme audit dan penyempurnaan yang udh ada di meta sistem... yang dibuat terpisah itu cukup yang sistem suntik/rawat jalan nya aja... aku tinggal masukin folder repo sistem nya ke meta sistem ini... terus aku jalanin suatu prompt ataupun prompt universal... agent akan langsung membaca dan memahami... dan agent bakal tanya apa yang mau aku lakukan... sistem yang udh dibengkel itu biar aja gpp tetep berada di meta sistem ini kecuali klo emang aku mau hapus" → diratifikasi eksplisit setelah analisis agent. Konsekuensi yang dikunci: (a) `_bengkel/` dihapus; rawat inap = alur standar meta (branch→PR→merge ke main, tanpa auto-merge) dijalankan dengan aturan klinik (katalog cacat, G-Rencana/G-Final, K-10, REKAM-KLINIK); (b) rawat inap membaca MASTER `_sistem/01–06` di tempatnya — tanpa salin kit/stamp/peleburan; kit jadi eksklusif suntik (repo target eksternal); (c) sistem pasca rawat inap TETAP di repo sebagai warga kelas satu (terdaftar INDEKS_SISTEM); penghapusan = keputusan sadar pemilik, dicatat; (d) prompt universal root diperluas cabang rawat inap — agent orientasi lalu MENANYA apa yang mau dilakukan sebelum menyentuh apa pun; (e) SUPERSEDE: K-1 (bagian "bengkel pengecualian") dan konsekuensi panggung K-9 (staging/kuota/pulang-via-patch/hapus-branch). Versi naik 0.1.2 → 0.2.0 |
