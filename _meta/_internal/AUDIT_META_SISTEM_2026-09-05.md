# Audit Menyeluruh Meta-Sistem — 2026-09-05

**Objek:** `_meta/` v1.2.0 + `PANDUAN_PENGGUNA.md` root + `tools/` + artefak turunan meta (`_cadangan-claude/`, `.gitignore`, template bersih/backup)
**Versi yang diaudit:** baseline `31e2591` (main) + sesi `arena/01a070c7-pembangun-sistem`
**Level:** **Mendalam** (multi-lensa + uji skenario/eksekusi, sesuai tabel level di `QUALITY_ASSURANCE_AND_EVOLUTION.md`)
**Sistem turunan** (`sistem-presentasi/`, `sistem-konten-kreator/`): dibaca **hanya sebagai bukti warisan** — yang disentuh hanyalah file *warisan* (kontrak STATUS, manifest wording, ringkasan cadangan). Isi domain tidak diaudit.
**Lensa yang dipakai (7):** (1) konsistensi rujukan silang; (2) kontradiksi antar-dokumen aktif; (3) klaim vs bukti eksekusi (tool dijalankan, output diperiksa terhadap data nyata, bukan dibaca saja); (4) jalur gagal (FI/DoD benar-benar menegakkan?); (5) kemudahan pakai dari kacamata pengguna awam (prompt pembuka, alur); (6) propagasi aturan ke sistem masa depan (template, manifest template, DoD, Discovery, validator); (7) kesehatan repo (git, .gitignore, artefak terjebak).
**Klasifikasi temuan:** `B` bug · `A` ambiguitas · `G` gap proses · `N` kebutuhan baru · `P` preferensi/housekeeping.

> Konteks pemicu (AT-12: audit mendalam butuh trigger): permintaan eksplisit pengguna 5 Sep 2026 — "pemeriksaan dan audit menyeluruh... memastikan betul-betul tidak ada cacat" + kebutuhan baru #4 (warisan wajib untuk sistem masa depan). Trigger sah.

---

## Ringkasan penilaian

Struktur, kedalaman alasan kausal, dan mekanisme checkpoint/recovery meta **baik** — tidak ada temuan pada jalur normal inti (entry point, approval, checkpoint format, protokol recovery secara konsep). Semua cacat yang ditemukan ada di **lapis pengawasnya**: alat, template distribusi, dan sinkronisasi antar-dokumen. Ini konsisten dengan pola 3 audit sebelumnya (3–5 Sep): pembacaan dokumen saja meloloskan ketiganya; temuan P1 di bawah baru kelihatan karena **dieksekusi**, bukan dibaca.

## Temuan

### P1 — cacat yang merusak fungsi

**M-01 (B, P1) — Template bersih & backup tidak membawa aturan wajib v1.1.0/v1.2.0.**
`tools/build_template.py::INCLUDE` dan `tools/backup_verify.py::ESSENTIAL` adalah daftar statis yang berhenti di v1.0.0; dua file wajib yang terbit setelahnya — `_meta/PANDUAN_PENGGUNA_TEMPLATE.md` dan `_meta/TEMPLATE_LOG_SESI.md` — tidak ikut (diverifikasi: hasil build `template_clean/` benar-benar tanpa keduanya, padahal 6 dokumen di dalam template merujuknya → repo hasil-ekstraksi punya rujukan putus ke aturan "WAJIB"). Backup 19 file juga tanpa keduanya → restore tidak memulihkan seluruh meta. Risiko utama manifest ("Master dan template berkembang tidak sinkron") **terujud tanpa ada validator yang menangkapnya**.
*Perbaikan:* INCLUDE/ESSENTIAL menjadi **dinamis** (semua `_meta/*.md` top-level + `tools/`), plus **gerak kelengkapan** di build (template tanpa salah satu `_meta/*.md` aktif = build GAGAL) + pembaruan daftar wajib `TEMPLATE_RELEASE.md`.

**M-02 (B, P1) — Bukti "fail-closed" menguji format yang tidak dipakai siapa pun.**
`tools/test_failure_injection.py::state_is_safe()` mencari literal `Pekerjaan belum tersimpan: Tidak ada`, sedangkan SEMUA STATUS/template nyata di repo memakai bentuk bold `**Pekerjaan belum tersimpan:** Tidak ada` (dan `validate_repo.py` C-01 sengaja menerima bentuk bold + backtick → dua checkerrepo tidak sepasang). Diukur langsung: `state_is_safe()` = `False` untuk **keempat** unit nyata (pilot-001, pilot-002-behavioral, fixture konten-kreator, deck presentasi). Klaim gate "Executable fail-closed check lulus" benar secara harfiah tapi **tidak membuktikan apa pun tentang data nyata** — lulus hanya terhadap fixture sintetis yang ditulis skrip sendiri.
*Perbaikan:* parser toleran (regex, sama tingkat dengan C-01) + skenario baru memakai **format nyata** + skenario "field absen = tidak aman"; `test_failure_injection` dan `validate_repo` disatukan tingkat ketelitiannya.

**M-03 (G, P1) — Kontrak checkpoint tidak ditegakkan ke semua unit.**
`validate_repo.py` C-01 hanya men-scan `sistem-pilot-catatan-belajar/unit-aktif/*/STATUS.md` dan 2 STATUS_TEMPLATE. Akibat nyata terverifikasi: `sistem-presentasi/_template/T6_STATUS.md` **tidak punya** field "Pekerjaan belum tersimpan" sama sekali → `deck-aktif/.../STATUS.md` warisannya juga tidak punya → fail-closed checkpoint mustahil dievaluasi pada unit presentasi. (Ini kelas cacat yang sama dengan yang ditemukan audit independen presentasi 5 Sep, tapi di sisi meta.)
*Perbaikan:* field ditambahkan ke `T6_STATUS.md` + `STATUS.md` deck aktif (warisan, diizinkan pengguna 16:50); cek C-01 digeneralisasi ke SEMUA unit di `sistem-*/{unit-aktif,_produksi-aktif,deck-aktif}/` dari INDEKS.

### P2 — inkonsistensi yang membingungkan/menyesatkan agen

**M-04 (B, P2) — Instruksi cek PR salah perintah.** `PLATFORM_LMARENA.md` P3 menyuruh `gh pr list --state open`, tapi P4 dan `PROTOKOL` langkah recovery #4 butuh tahu PR branch aktif yang sudah **MERGED/CLOSED** — tidak akan pernah terlihat dengan `--state open`. (Sesi nyata 5 Sep ini harus pakai `--state all` untuk bekerja benar; bukti di `arsip.../SESSION_REPORT_2026-09-05` dan praktik sesi.) *Perbaikan:* perintah standar `gh pr list --state all --limit 20` di P3, PROTOKOL, dan `NEXT_SESSION_PROMPT`.

**M-05 (G, P2) — Entry point `00_CARA_KERJA` belum memuat langkah recovery log.** Daftar "wajib di awal sesi" hanya 3 langkah (laporan, PR, INDEKS); langkah cari `LOG_SESI` `OPEN` hanya ada di PANDUAN root (langkah 4), `NEXT_SESSION_PROMPT` (langkah 2), PROTOKOL (#7), TEMPLATE_LOG_SESI. Karena PANDUAN root adalah sumber prompt universal yang sebenarnya, divergensi ini senyap. *Perbaikan:* tambah langkah 4 di `00_CARA_KERJA`.

**M-06 (A, P2) — `SESSION_REPORT_TEMPLATE` tidak punya tempat untuk LOG_SESI.** Tidak ada baris "log terbaru + keadaan" → laporan awal tidak pernah mewajibkan pelaporan hasil langkah recovery; AT-13 tidak punya artefak pembukti. *Perbaikan:* baris `LOG_SESI terbaru` + entri tabel konteks wajib.

**M-07 (G, P2) — Struktur repo di `00_CARA_KERJA` tidak menyebut `tools/`** (dan file `_meta/` baru: `NEXT_SESSION_PROMPT`, `TEMPLATE_RELEASE`, `TEMPLATE_LOG_SESI`, `PANDUAN_PENGGUNA_TEMPLATE`, `_internal/`). Agen baru tidak tahu regresi struktural bisa dijalankan. *Perbaikan:* blok struktur dilengkapi + satu baris "cara menjalankan tool".

**M-08 (G, P2) — "Audit multi-lensa" didefinisikan sebagai level tapi lensanya tidak pernah dikodifikasi.** Backlog P1 audit 3 Sep ("checklist audit berbasis beberapa lensa") tidak pernah dikerjakan; kata "multi-lensa" hanya muncul sekali. Kualitas audit bergantung auditor. *Perbaikan:* tabel lensa (7, dari audit ini) masuk `QUALITY_ASSURANCE_AND_EVOLUTION.md` sebagai isi minimal level Mendalam + klasifikasi temuan wajib (B/A/G/N/P) ditulis eksplisit.

**M-09 (B, P2) — Ringkasan cadangan basi.** `RINGKASAN_sistem-presentasi.md` masih `0.2.0`, `_sistem/01–10`, "audit independen belum dilakukan" (aktual 0.4.0, 11 dokumen, teraudit) — padahal checklist manifest presentasi mencentang "Ringkasan cadangan sinkron". `RINGKASAN_sistem-konten-kreator.md` menunjuk `PANDUAN_PENGGUNA.md` di root folder sistem (aktual: `panduan/`) dan struktur/ status pra-0.3.1. *Perbaikan:* kedua ringkasan disinkronkan.

**M-10 (G, P2) — Q-O2 / Q-O3 masih terbuka sejak 3 Sep dan merambat.** Protokol: "Jangan mengulang tahap `approved`/`merged` tanpa alasan" tanpa kriteria "alasan" (Q-O2); interval "Waktu pembaruan" tak diatur (Q-O3). Dua dokumen sistem (manifest presentasi, ringkasan cadangan) sekarang memuat catatan "celah terbuka". Ditutup dengan aturan minimal (kriteria keputusan ini: didelegasikan pengguna "lakukan yang terbaik"; bisa di-revert di review PR): **Q-O2** — alasan sah = kutipan instruksi eksplisit pengguna yang lebih baru ATAU bukti kecacatan berpath (file/commit); tanpa itu → berhenti dan tanya. **Q-O3** — "Waktu pembaruan" diisi pada SETIAP checkpoint dan akhir sesi; format `YYYY-MM-DD — <peristiwa singkat>`.

**M-11 (G, P2) — Kebocoran self-containment di manifest sistem turunan (bukti prinsip, perbaikan file warisan diizinkan).** `sistem-presentasi/SYSTEM_MANIFEST.md` menunjuk `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` dan `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` sebagai protokol **aktif** — padahal prinsip self-contained (00_CARA_KERJA, 5 Sep) mensyaratkan aturan operasional di dalam folder dan `_meta` hanya provenance; folder ini mengklaim diri bisa diunduh jadi repo standalone (START_DI_SINI baris 3). Konten-kreator lebih sehat: fakta platform + LOG_SESI sudah diturunkan ke `00_CARA_PAKAI_SISTEM.md`; wording manifestnya cukup diberi label provenance. *Perbaikan:* wording field di kedua manifest → "turunan aktif di folder: X; induk (provenance): _meta/Y"; cek otomatis "rujukan `_meta/` dalam dokumen sistem harus berlabel provenance" TIDAK dibuat (terlalu rapuh untuk nilai) — ditegakkan via kontrak warisan (M-13) + DoD.

**M-12 (P, P2) — `.obsidian/workspace.json` ter-track.** State UI lokal berubah tiap buka vault → noise diff dan sumber konflik sync; isi file lain di `.obsidian/` (pengaturan vault) wajar tetap ikut. *Perbaikan:* ignore `workspace.json` saja.

### P3 — kecil, tetap dihitung

- **M-13 (N, P3→di-promosikan jadi pekerjaan inti sesi ini):** **Kontrak Warisan tidak terpusat.** Item wajib untuk SEMUA sistem (self-contained; pegangan 2-file; LOG_SESI; checkpoint/STATUS berfield deterministik; manifest; log keputusan di dokumen hidup; QA 3-lapis; fakta platform) tersebar di `00_CARA_KERJA` (narasi), `02_PRINSIP` #4/#6, DoD, Discovery L-0 poin 5, manifest template — tanpa daftar induk, tanpa titik "laporkan penerapan", tanpa validator generik. **Keputusan pengguna 16:50: desain "kontrak warisan"** — default AKTIF, agent MENGIMPLEMENTASIKAN + MELAPORKAN daftar penerapan (bukan menawarkan satu-satu), dan **hanya penonaktifan** yang wajib lewat konfirmasi eksplisit + override tercatat. Implementasi: dokumen baru `_meta/03_KONTRAK_WARISAN.md` (tabel butir × sumber aturan × cara tanam × cara verifikasi × prosedur override), dirujuk dari 00/01-Discovery/DoD/manifest-template/ACCEPTANCE (AT-14), ditegakkan `validate_repo.py` (cek generik per sistem dari INDEKS: folder manifest+pegangan+PROMPT_ENTRI; cek field STATUS unit).
- **M-14 (A, P3):** `01_DISCOVERY` prompt menyebut "4 hal" padahal ada 5 poin (5: Batasan Platform); "Setelah selesai" langkah 1–2 mengurutkan manifest-copy SETELAH merge sementara `00_CARA_KERJA` langkah 2 mengatakannya sebelum isi dibangun. → selaraskan ("5 hal"; manifest + skeleton ikut PR rencana kerangka).
- **M-15 (P, P3):** meta melanggar standarnya sendiri soal pegangan: template mewajibkan DUA file (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md`), meta root hanya punya satu. → tambah `PROMPT_ENTRI_UNIVERSAL.md` root (blok identik, diberi catatan sinkron).
- **M-16 (P, P3):** template bersih membawa `_meta/SYSTEM_MANIFEST.md` master utuh (gate v1.0.0, log evolusi, SHA repo ini) — "sebagai referensi versi" memang diniatkan, tapi tanpa penanda, repo baru membaca sejarah repo ini sebagai manifestnya sendiri. → build menambahkan **banner** 3 baris di salinan: "salinan dari master; repo BARU ini mulai dari manifest `0.1.0` sesuai template".
- **M-17 (P, P3):** rujukan istilah teknis di `PANDUAN_PENGGUNA.md` root menunjuk "`PANDUAN_PENGGUNA.md` di dalam `sistem-konten-kreator/`" — aktual `sistem-konten-kreator/panduan/PANDUAN_PENGGUNA.md`. → perbaiki path.
- **M-18 (P, P3):** 2 branch yatim `arena/01a0679e`, `arena/01a067e8` (pilot-002, sudah diarsipkan byte-per-byte + didokumentasikan `CABANG_MENGGANTUNG_2026-09-04.md`). Penghapusan remote permanen = **tetap keputusan pengguna**, tidak dilakukan sesi ini.

## Yang diperiksa dan BERSIH (negatif bernilai)

Tidak ada merge marker / code fence rusak (rglob seluruh .md); versi & status konsisten INDEKS ↔ manifest meta ↔ manifest kedua sistem ↔ LOG_SESI (tidak ada konflik M-xx di sini); 120 rujukan path di 50 dokumen aktif lolos (7 warning presentasi = nama historis **sudah diberi label eksplisit** "Renumbering (5 Sep)" di dokumen → bukan cacat; 4 warning = artefak gitignore yang diketahui — masuk whitelist di M-01-fix agar "0 warning" jadi baseline sehat); `00_CARA_KERJA`→`09_AUDIT_MIGRASI...` resolve (file ada); format deterministik C-01 di pilot/konten-kreator lolos; tidak ada dokumen aktif yang saling bertentangan soal fakta platform (bahasa "tidak bisa" konsisten); prinsip anti-overkill LOG_SESI konsisten di semua titik turunannya.

## Rencana regressi (setelah perbaikan)

1. `validate_repo.py` PASS dengan **0 warning** (whitelist artefak + exclusion beralasan); 2. `test_failure_injection.py` PASS ≥6 skenario termasuk format nyata + field absen; 3. `build_template.py` PASS + guard kelengkapan + **smoke test ekstrak**: unzip ke repo kosong, jalankan validator+FI di sana → harus PASS; 4. `backup_verify.py` PASS dengan ESSENTIAL dinamis; 5. diff prompt pembuka PANDUAN vs PROMPT_ENTRI (root & 2 sistem) identik; 6. cek ulang rujukan ke file yang berubah nama/lokasi.

## Status proses

Audit ini menghasilkan temuan + proposal. Implementasi (termasuk M-10 dan M-13 yang disetujui lewat delegasi "lakukan yang terbaik" 16:50) berjalan pada sesi/branch `arena/01a070c7-pembangun-sistem`, commit terpisah per langkah, satu PR; review isi lengkap oleh pengguna sebelum merge (kategori Besar).

## Addendum (ditemukan saat implementasi, 5 Sep)

**M-19 (B, P2) — Baris temuan L-05 basi di `sistem-konten-kreator/SYSTEM_MANIFEST.md`.** Tabel "Temuan Audit yang Masih Terbuka" masih menulis "**AT-KK-05b belum diuji**" padahal gate di file yang sama (baris 54) dan Log Evolusi (baris 99) mencatat LULUS 5 Sep — satu file, dua status, bertentangan. (Baris unchecked pada baris 57 TIDAK termasuk temuan: ia berada dalam `<!-- riwayat gate -->` — komentar riwayat yang disengaja, diverifikasi.) **Diperbaiki di sesi ini** (baris L-05 disinkronkan + dicatat di Log Evolusi `0.3.2-warisan-sync`).

**Koreksi cakupan M-07:** perintah regresi ditambahkan sebagai teks di bawah Entry Point 00_CARA_KERJA (bukan hanya blok struktur). **Bukti smoke test template** (regressi #3) dijalankan riil pada sesi ini di `/tmp/tpl_smoke`: validator & FI exit 0 di repo tanpa sistem; 8 warning di ekstrak = rujukan artefak khusus master → dinormalisasi sebagai ekspektasi di `TEMPLATE_RELEASE.md` (bukan cacat).

## Hasil akhir sesi implementasi

Semua M-01…M-17 & M-19 **diperbaiki** pada branch ini; M-18 tetap keputusan pengguna. Regresi akhir: `validate_repo.py` **PASS 0-warning** (24 required glob-dinamis; 67 dokumen; 186 rujukan; 2 sistem + kontrak warisan ditegakkan generik), `test_failure_injection.py` **PASS 11 skenario** (6 sintetis + 4 konsistensi unit nyata — deck presentasi kini termasuk), `backup_verify.py` PASS 29 file byte-exact, `build_template.py` PASS + guard kelengkapan + smoke ekstrak PASS, `validate_system.py` presentasi PASS. Versi: meta `1.3.0`; presentasi `0.4.1`; konten-kreator `0.3.2-warisan-sync`.

## Addendum 2 — Hasil review independen PR #11 + perbaikan (5 Sep)

**Sumber:** sesi agent terpisah menjalankan prompt review adversarial (eksekusi, bukan pembacaan) atas branch ini; VERDICT **REQUEST_CHANGES**, 16 temuan (7×P1, 7×P2, 1×P3, 1×P4). Reviewer membuktikan **4 PASS palsu** dengan mutation testing (bukan membaca klaim): (1) hapus `_meta/DEFINITION_OF_DONE.md` → validator/build/backup tetap exit 0; (2) folder `sistem-autopilot-data/` tak terdaftar → lolos (pengecualian substring "pilot"); (3) baris "Daftar Sistem" tanpa backtick → diabaikan parser; (4) field `Pekerjaan belum tersimpan` ganda (aman lalu kotor) → tetap "aman". Dua bug lama (M-01/M-02) juga dibuktikan langsung dari `origin/main` (build lama: 2 file wajib hilang dari ZIP; FI lama: `False` untuk 4 unit nyata).

**Catatan metodis:** beberapa item "TIDAK" di laporan reviewer (B2/B5/B6, A5/A6) bersumber dari **kesalahan nama file di checklist review yang saya susun** (mis. `PANDUAN_MEMULAI_DARI_SKRIP.md` vs aktual `PANDUAN_PENGGUNA.md`; `sistem-presentasi/tools/` vs `_sistem/`) — reviewer memisahkan hal ini secara eksplisit dari cacat substantif, dan padanan aktualnya diperiksa dan lulus (termasuk hash identik blok prompt). Baris gateunchecked `0.3.1` di manifest KK yang terlihat "bertentangan" ternyata berada dalam `<!-- riwayat gate -->` (arsip berlabel, disengaja).

**Status per temuan (semua P1–P4 sudah dijawab di PR ini):**

| # | Temuan (ringkas) | Jawaban |
|---|---|---|
| F1 (P1) | Daftar wajib diturunkan dari file yang masih ada → hapus sumber wajib lolos diam-diam | **Diperbaiki.** `checkpoint_core.CORE_REQUIRED` (inventaris inti statis = kewajiban, terpisah dari keberadaan) dipakai validator + build_template + backup; glob-derived tetap untuk file baru (sifat M-01 terjaga). Regresi R1: hapus file inti → 3 tools HARUS gagal. |
| F2 (P1) | Parser INDEKS memaafkan baris tanpa backtick; except substring "pilot" | **Diperbaiki.** `parse_index` ketat (kolom Folder harus persis `` `sistem-<nama>/` ``; baris lain = error; folder di disk tak terdaftar = error; pilot dikecualikan per NAMA EKSAK). Regresi R2+R3. |
| F3 (P1) | Unit/field hilang = cakupan menyusut, bukan gagal | **Diperbaiki.** Sistem terdaftar WAJIB punya ≥1 `STATUS.md` unit (enumerasi semua layout, bukan 3 pola tetap); FI juga gagal bila sistem terdaftar tanpa unit. Regresi R4. (Layout per-sistem deklaratif = follow-up, tidak di sini.) |
| F4 (P1) | Parser menerima bukti keselamatan palsu (duplikat, kutipan, format protokol tak terlihat) | **Diperbaiki.** Parser bersama `checkpoint_core`: line-anchored (kutipan `>`/prosa tak dihitung), isi fence diabaikan, field ganda = tidak deterministik = tidak aman, status format-tolerant (`- Status: approved` dikenali). 5 skenario sintetis baru + FI/validator memakai parser yang sama. |
| F5 (P1) | 8 warning ekstrak ternyata 2 di antaranya dependensi AKTIF yang hilang (bootstrap HANDOFF; istilah → panduan KK) | **Diperbaiki.** Transformasi builder idempotent pada salinan template: langkah 6 bootstrap jadi kondisional; istilah teknis di-inline. Daftar normalisasi mengecil jadi **persis 4** (histori master berlabel) dan DIPIN di FI (R7) + `TEMPLATE_RELEASE.md`. |
| F6 (P1) | Klaim self-contained presentasi salah — manifest masih mewajibkan `tools/validate_repo.py` (tidak ada di folder standalone) | **Diperbaiki.** Instruksi self-audit manifest presentasi kini menunjuk `_sistem/validate_system.py` (lokal); validator master = konteks/provenance. Klaim body PR dikoreksi. |
| F7 (P1) | Perubahan aturan `00` KK diklaim "cuma wording, regresi tidak terpicu" — salah | **Dikoreksi + pengecualian tercatat.** Baris Log Evolusi 0.3.2 & baris acceptance manifest KK kini mengakui perubahan aturan `00` (baris File wajib recovery) → klausul regresi TERPICU, belum dijalankan; **clean-run acceptance dijadwalkan first task sesi berikutnya** (sesi pembuat & reviewer sama-sama tidak memenuhi syarat uji buta). Keputusan final: lihat PR. |
| F8 (P2) | Template T6 (dan KK/pilot) mencampurkan petunjuk ke dalam nilai field → instaniasi gagal parser | **Diperbaiki.** Nilai field kini exact `Tidak ada` di 3 template; petunjuk dipindah ke bagian Petunjuk/Aturan; validator memeriksa template dengan parser yang sama (harus parse exact). |
| F9 (P2) | Checker tak memahami override sah / tahap pembangunan | **Diperbaiki.** `Tahap: kerangka/siap-pakai` di manifest (template default `kerangka`); kerangka menurunkan W-01/W-02/W-03 menjadi warning; baris Warisan `override` membebaskan cek butir itu hanya jika alasan/dampak/tanggal/approval lengkap; 9 butir wajib ada. Regresi R5/R6. |
| F10 (P2) | Precedence kontrak hanya untuk yang bisa dicek validator | **Diperbaiki.** `02_PRINSIP_UNIVERSAL.md`: kontrak menang untuk SELURUH W-01…W-09 (termasuk W-08 yang diverifikasi proses); penyesuaian ≠ penonaktifan. |
| F11 (P2) | Header LOG_SESI tertinggal dari kronologi | **Diperbaiki** (snapshot "Keadaan Sesi" di-update saat addendum ini ditulis). |
| F12 (P2) | Status/versi saling bertentangan (INDEKS 0.4.0/0.3.1/1.2.0; acceptance presentasi "Q-O2/Q-O3 terbuka") | **Diperbaiki.** INDEKS: `0.4.1` / `0.3.2-warisan-sync` / `1.3.0`; acceptance presentasi selaras baris Prosedur recovery. |
| F13 (P2) | Resolver meminjam file sistem lain → dependensi lokal hilang lolos | **Diperbaiki.** Resolusi di-scope per dokumen: dokumen dalam folder sistem hanya me-resolve sistem sendiri + `_meta/` + root; dokumen level master tetap lintas-sistem. |
| F14 (P2) | URL eksternal terdeteksi sebagai path repo | **Diperbaiki.** URI (skema `...:`) dikecualikan sebelum resolusi. Batasan lama tetap jujur: bare filename & path ber-spasi tidak di-judge. |
| F15 (P3) | Hitungan drift (6 vs 7 sintetis; "10 skenario" di manifest; "keempat" di Discovery; "11 dokumen" ringkasan KK) | **Diperbaiki.** Output FI kini dihitung dinamis dari koleksi; manifest meta, Discovery ("kelima"), ringkasan KK (12 dokumen) diselaraskan. **Koreksi label historis:** komposisi FI saat "11 skenario" = **7 sintetis + 4 unit nyata** (bukan 6+4). |
| F16 (P4) | Q-O2 "bukti kecacatan" bisa dibaca approval baru | **Diperbaiki.** PROTOKOL: alasan sah = dasar *mengusulkan* via jalur perubahan (usulan → klasifikasi dampak → approval), bukan approval otomatis; scope terbatas kecacatan terbukti. |

**Regresi akhir pasca perbaikan:** `validate_repo.py` PASS 0-warning (25 required; 67 dokumen; ~200 rujukan; 2 sistem), `test_failure_injection.py` **PASS 29 skenario** di master (12 sintetis + 4 unit nyata + 13 regresi R1–R7) dan **24 di ekstrak template**, `backup_verify.py` PASS (30 file byte-exact), `build_template.py` PASS + smoke ekstrak: validator exit 0 dengan **persis 4 warning normalisasi** (dipin di R7), `validate_system.py` presentasi PASS. `qa_deck.py` tidak di-rerun — reviewer memverifikasi (22 blob identik) bahwa tidak ada slide/skrip deck yang disentuh; satu-satunya file deck yang berubah adalah STATUS (field checkpoint, sudah dibuka PR).
