# Acceptance Test Log — Sistem Building Aplikasi

> Bukti eksekusi skenario ACCEPTANCE_TESTS.md — dicatat per run. Angka stabil dikutip, rujukan volatil tidak dikutip.

## Run 2026-09-15 — Run Klinik Pertama (kit v0.2.0, panggung rawat inap)

- **Tanggal:** 2026-09-15
- **Pelaksana:** agent sesi arena/01a0a48f-pembangun-sistem (run klinik pertama, rawat inap)
- **Kit:** v0.2.0 (master in-place, rawat inap — tanpa salin kit)
- **Target:** sistem/sistem-building-aplikasi (rename SISTEM-BUILDING-APLIKASI → sistem-building-aplikasi)

### Hasil Skenario

| Skenario | Hasil | Bukti |
|---|---|---|
| AT-01 Entry Point | PASS | PROMPT_ENTRI_UNIVERSAL.md + PANDUAN_PENGGUNA.md blok identik (validator pegangan PASS) |
| AT-02 Checkpoint | PASS | STATUS.md field Pekerjaan belum tersimpan: Tidak ada tepat 1x, Waktu pembaruan: 2026-09-15 — Verifikasi D lulus + REKAM-KLINIK cap v0.2.0 + Panen nihil; validate_system.py PASS |
| AT-03 Log Sesi | PASS | _log-sesi/LOG_SESI_2026-09-15.md CLOSED; 10_LOG_SESI.md ada |
| AT-04 Pegangan Identik | PASS | diff blok PANDUAN vs PROMPT = identik (validator pegangan PASS) |
| AT-05 Self-Containment | PASS | tools/check_selfcontained.py --sistem sistem-building-aplikasi --report PASS (1 salinan berlabel, 0 temuan) |
| AT-06 Fondasi Gerbang | PASS | AGENT_SYSTEM.md §Tahap 1-6 menunggu "cukup, tulis draftnya" — agen tidak menulis tanpa approval |
| AT-07 DECISIONS_LOG | PASS | AGENT_SYSTEM.md §DECISIONS_LOG mewajibkan baca + STOP bila ubah Area Berisiko Tinggi |

### Verifikasi Alat (Tahap D)

- _sistem/validate_system.py: PASS
- tools/validate_repo.py: PASS 0 warning (102 docs/327 refs/4 sistem)
- tools/check_selfcontained.py --semua: PASS (4 sistem)
- tools/test_failure_injection.py: PASS 72 skenario (15 sintetis + 13 unit nyata + 14 PR-11 + 10 check_selfcontained + 20 review_prompt)
- tools/backup_verify.py: PASS (backup 36 files, restore OK)
- tools/build_template.py: PASS (smoke extract + template clean)

### Catatan

Run ini adalah run pertama Klinik (pola F-8) — AT dijalankan penulis perubahan; verifikasi pihak kedua = review independen PR ini + run berikutnya. Panen F = nihil (tidak ada cacat baru di luar C-01…C-06).

## Run 2026-09-16 — Run Klinik Ke-2 (kit v0.2.0, panggung rawat inap, audit menyeluruh)

- **Tanggal:** 2026-09-16
- **Pelaksana:** agent sesi arena/01a0a7d3-pembangun-sistem (run klinik ke-2, rawat inap)
- **Kit:** v0.2.0 (master in-place — cap REKAM-KLINIK run 1 juga v0.2.0, jadi tanpa tawaran naik versi, tidak fail-closed)
- **Pemicu:** pemilik mau memakai sistem ini tapi ragu "beneran siap pakai dan aman", setelah menemukan `PANDUAN_PEMAKAIAN.md` yang menyebut hanya `AGENT_SYSTEM.md` yang masuk repo baru. Permintaan pemilik: audit + pemeriksaan mendalam, **baca dan periksa semua berkas folder tanpa terkecuali, termasuk berkas khusus pengguna**.
- **Lingkup yang dibaca:** 13 berkas root, 4 arsip audit + validator + 10 template di `_sistem/`, `docs/README.md`, `_log-sesi/` arsip, `_salinan-meta/`, `skills/README.md` + 2 `CATALOG.md`, dan inventaris 1.802 berkas vendor di `skills/` (scan keamanan, bukan baca satu-satu — konten vendor pihak ketiga).

### Hasil Skenario

| Skenario | Hasil | Bukti |
|---|---|---|
| AT-01 Entry Point | PASS | `PROMPT_ENTRI_UNIVERSAL.md` + blok pertama `PANDUAN_PENGGUNA.md` identik (cek validator `check_pegangan` PASS); semua berkas yang dirujuk prompt ADA di repo hasil copy (AT-08 butir 6) |
| AT-02 Checkpoint | PASS | `STATUS.md` `**Pekerjaan belum tersimpan:** Tidak ada` tepat 1x + `**Waktu pembaruan:** 2026-09-16 — Run klinik ke-2 …`; validator exit 0 |
| AT-03 Log Sesi | PASS | `10_LOG_SESI.md` (7 aturan) + `_log-sesi/LOG_SESI_2026-09-15.md` CLOSED berpenanda arsip; log run ke-2 di level repo meta: _log-sesi/LOG_SESI_2026-09-16.md (di luar folder ini, jadi ditulis sebagai provenance tanpa backtick) |
| AT-04 Pegangan Identik | PASS | cek `check_pegangan` PASS (blok prompt tidak diubah run ini) |
| AT-05 Self-Containment | PASS | `tools/check_selfcontained.py --sistem sistem-building-aplikasi --report` → temuan 0, `HASIL SISTEM: PASS` (1 salinan berlabel `_salinan-meta/PLATFORM_LMARENA.md`) |
| AT-06 Fondasi Gerbang | PASS (bukti dokumen) | `AGENT_SYSTEM.md` Tahap 1-6: "JANGAN tulis dokumen final sebelum user bilang 'cukup, tulis draftnya'" — **belum diuji perilaku nyata** (butuh run Fondasi pertama); dinyatakan apa adanya, bukan diklaim teruji |
| AT-07 DECISIONS_LOG | PASS (bukti dokumen) | `AGENT_SYSTEM.md` § Aturan Mengikat + Stop Conditions — sama seperti AT-06, bukti dokumen |
| **AT-08 Copy → Repo Standalone** | **PASS** | `cp -r` ke `/tmp/app-uji` + `rm _Notes.md` + `git init` + commit `d779211`: validator lokal **exit 0 tanpa `tools/`**; `find skills -mindepth 1 -maxdepth 1 -type d \| wc -l` = **56**; `du -sh skills` = **26M**; 1.832 berkas; `.git` 14M; `tools/` TIDAK ada, `_meta/` TIDAK ada, `PROJECT_STATE.md` TIDAK ada (→ proyek baru, Tahap 1); 14 berkas yang dirujuk prompt entri **semua ADA**; **rujukan berprefix menggantung = 0** (run final; pada run pertama cek ini menangkap 3 rujukan menggantung yang justru berasal dari prose log run ke-2 sendiri — rujukan ke log level repo meta, path upstream Archive.zip, dan nama berkas terpotong elipsis — ketiganya diperbaiki, bukan dikecualikan) |
| **AT-09 Anti-Pedoman-Usang-Hidup** | **PASS (5/5 mutasi terdeteksi)** | Kondisi bersih exit 0; mutasi (a) penanda arsip `PANDUAN_PEMAKAIAN.md` dihapus → GAGAL, (b) header `skills/README.md` 56→52 dirs → GAGAL, (c) suntik "hanya `AGENT_SYSTEM.md`" ke `START_DI_SINI.md` → GAGAL, (d) suntik `` tools/validate_repo.py `` ke `STATUS.md` → GAGAL, (e) atribut `**Verifikasi:**` dihapus dari `_sistem/templates/ROADMAP.md` → GAGAL; semua dikembalikan → PASS lagi |

### Verifikasi Alat (Tahap D, keluaran mentah)

- `python3 sistem/sistem-building-aplikasi/_sistem/validate_system.py` → `SYSTEM-BUILDING-APLIKASI VALIDATOR: PASS`, exit 0 (**9 berkas wajib** + 5 cek baru run ke-2)
- `python3 tools/validate_repo.py` → `VALIDATION PASSED: 29 required files and Markdown invariants checked` / `COVERAGE: 104 active documents scanned, 354 path references checked, 0 unresolved` / `SYSTEMS CHECKED: 4 registered + pilot excluded by design` / `WARNINGS: none`
  - Catatan jujur: sempat **2 warning** (`AGENT_SYSTEM.md:150-151` unresolved `discovery-interview-prep/SKILL.md`, `prd-development/SKILL.md`) akibat teks baru run ini → diperbaiki jadi path penuh → 0 unresolved. Tidak dibiarkan lolos.
- `python3 tools/check_selfcontained.py --semua --report` → `HASIL AKHIR: PASS` (4 sistem); building: temuan 0, salinan berlabel 1, rujukan historis 2, sebutan area `tools/` 3 + `ACCEPTANCE_TESTS.md` 2 (sebutan area, tidak ditegakkan)
- `python3 tools/test_failure_injection.py` → `FAILURE-INJECTION TESTS PASSED: 72 scenarios (15 sintetis + 13 unit nyata + 14 regresi review PR-11 + 10 regresi check_selfcontained + 20 regresi review_prompt)`
- Tidak dijalankan run ini: tools/backup_verify.py, tools/build_template.py (PASS pada PR #59; tidak ada berkas yang mereka uji yang diubah run ini)

### Scan keamanan `skills/` (read-only, 1.802 berkas / 26M)

- Kredensial nyata (`ghp_`, `sk-`, `AKIA`, `xox*`, `-----BEGIN … PRIVATE KEY`): **0**; `.env`/`.pem`/`.key`/nested `.git`: **0**
- `curl … | sh`: **1**, sebagai teks dokumentasi di `skills/README.md` (bukan perintah); `base64 -d | sh`: 0; `eval(`: 0
- `rm -rf`: **11** — semua di skrip/CI/docs vendor dengan target variabel lokal (`$SESSION_DIR`, `$TEMP_DIR`, `.probe`, DerivedData); `sudo`: **4** — semua `sudo xcode-select -s` (docs/CI iOS)
- 37 berkas ber-bit executable + 127 skrip `sh/py/js/ts` (wajar untuk skill vendor); skill Google butuh OAuth browser
- **Kesimpulan:** tidak ada indikasi malware atau kebocoran kredensial. Risiko nyata = bobot 26M per repo aplikasi (keputusan pemilik) + 5 folder skill di-rename terhadap `name:` upstream (catatan `skills/README.md` § Integritas vendor)

### Temuan yang diperbaiki (11 Critical + 9 Minor)

Critical: K-1 dua pedoman aktif bertentangan (`PANDUAN_PEMAKAIAN.md` vs `PANDUAN_PENGGUNA.md`); K-2 manifest basi (dokumen wajib, 7 vs 10 template, 8.1M/52 dirs); K-3 RINGKASAN cadangan basi total (W-09); K-4 `STATUS.md` narasi run "sedang berjalan"/"Merge PR (G-Final)"; K-5 `AGENT_SYSTEM.md` melarang folder `panduan-owner` yang tidak ada; K-6 kalimat ganda akhir Tahap 5; K-7 aturan branch deskriptif bertentangan dengan fakta platform branch `arena/...` otomatis (juga di `_sistem/templates/AGENT_OPERATING_GUIDE.md`); K-8 `_sistem/templates/ROADMAP.md` mencontohkan bentuk singkat yang DILARANG `AGENT_SYSTEM.md` Tahap 5; K-9 LANGKAH 0 bisa deadlock di sesi perawatan sistem (profil sengaja kosong → "JANGAN lanjut ke proyek"); K-10 `skills/README.md` 9 kontradiksi internal (header 26M/56 dirs vs "Registrasi 8.1M, 52 dirs", "hemat 85%", ukuran per-skill basi, `banner` vs `banner-design`, `awesome-agent-skills` 224K vs 16K nyata, 18 vs 17 sub-skill, hub 35M/42k vs 71M/787 valid); K-11 angka katalog `248+797`/`1045` tidak selaras dengan `CATALOG.md` (787 skill valid dari 797 direktori).

Minor: M-1 perintah copy `commit -m "… 8.1M"`; M-2 `skills/vercel-deploy/Archive.zip` (TIDAK dihapus — lihat catatan pembatalan); M-3 bukti kesiapan struktural saja (→ AT-08 dry-run); M-4 `REKAM-KLINIK.md` tanpa penanda arsip saat ikut ter-copy; M-5 arsip `_sistem/02_TAWARAN_KAPABILITAS_PLUS_AUDIT.md` menyebut "skills/ 8.1M" sebagai keadaan kini; M-6 6 direktori agregat tanpa `SKILL.md` di akar (aturan resolve belum eksplisit); M-7 rujukan `_cadangan-claude/` ber-backtick di dokumen aktif (area yang tidak ikut keluar dari master); M-8 `_Notes.md` (catatan pribadi + tautan chat) ikut ter-copy ke repo aplikasi tanpa penanda; M-9 `docs/README.md` menyebut folder "kosong" padahal berisi `README.md`, dan menyebut "keenamnya" tanpa menyebut 10 template.

### Catatan pembatalan item rencana (jujur, bukan disamarkan)

Item 8 rencana (disetujui pemilik di G-Rencana) adalah **hapus `skills/vercel-deploy/Archive.zip`** sebagai sampah biner. Bukti baru membatalkannya: berkas itu **bagian dari repo upstream** vercel-labs/agent-skills (path upstream skills/deploy-to-vercel/Archive.zip — folder lokal kita `skills/vercel-deploy/`, ukuran identik 11.314 bytes; `SKILL.md` 11.786 bytes juga identik) — menghapusnya akan **membatalkan jaminan "byte-identik dengan `npx`"** yang dijanjikan `skills/README.md` dan membuat `npx skills update` melihat selisih. Tindakan yang diambil: **dipertahankan + didokumentasikan** (`skills/README.md` § Integritas vendor butir 2: jangan diekstrak/dipakai). Penyimpangan dari rencana ini dilaporkan ke pemilik di G-Final; pemilik tetap boleh memerintahkan penghapusan.

### Catatan pola F-8 (verifikasi pihak kedua)

Run ini kembali dijalankan oleh penulis perubahan (agent yang sama yang memperbaiki). Yang membedakan dari run 1: AT-08/AT-09 memberi **bukti eksekusi** (dry-run nyata + uji mutasi 5/5), bukan hanya bukti baca dokumen, dan review independen PR ini menjadi verifikasi pihak kedua. AT-06/AT-07 tetap **bukti dokumen** — dinyatakan apa adanya; verifikasi perilaku sesungguhnya = run Fondasi Tahap 1 pertama di repo aplikasi nyata.

### Panen (Tahap F)

**Tidak nihil.** Satu cacat di luar katalog C-01…C-06 ditemukan dan diusulkan jadi butir baru: **C-07 "Dokumen Pengganti yang Tidak Dipensiunkan (superseded-but-live)"** — ditambah ke `sistem/sistem-klinik/_sistem/02_KATALOG_CACAT.md` lewat mekanisme promosi (Aturan Promosi butir 4). Celah aturan kit yang ketahuan: Kebijakan Lebur melarang overwrite/hapus tanpa izin (benar), tetapi **tidak ada butir yang mewajibkan dokumen yang digantikan diberi penanda arsip** — akibatnya run 1 meninggalkan pedoman lama yang hidup dan menyesatkan. Usulan: penanda arsip jadi bagian Kontrak Tanaman/planting checklist.
