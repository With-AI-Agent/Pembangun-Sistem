# Audit Independen — Sistem Presentasi (level Sedang)

**Dibuat:** 5 September 2026 — sesi `arena/01a0706d-pembangun-sistem` (audit independen oleh sesi agent BARU, pertama kali)
**Objek:** `sistem-presentasi/` versi `0.2.0` `Built & terverifikasi` di commit `b5ffd81` (pasca-PR #9)
**Level:** `Sedang` (checklist lengkap + cross-check + review ringkas) — sesuai "Level audit default" di `SYSTEM_MANIFEST.md`
**Sifat:** sesuai `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md`, audit ini **hanya menghasilkan temuan dan rekomendasi** — tidak ada aturan/dokumen/output yang diubah oleh audit ini. Perbaikan menunggu keputusan pengguna (proposal → approval).

---

## 1. Metode & Bukti

Semua klaim di bawah diverifikasi ulang oleh sesi ini, bukan diwarisi dari sesi sebelumnya.

| Bukti | Cara verifikasi | Hasil |
|---|---|---|
| Kelengkapan struktur sistem | `PYTHONPATH=/tmp/pptxlib python3 _sistem/validate_system.py` | exit 0, "SAKTI/struktur lengkap? YA", 1 deck ditemukan |
| QA deck #1 | `python3 _sistem/qa_deck.py keluaran/....pptx 14` | exit 0 — 14 slide, 14 gambar, 0 fail, 0 warn |
| Dependency | `bash _sistem/install_deps.sh` | exit 0 (python-pptx, Pillow, pypdf, python-docx, matplotlib) |
| **Reproducible build** | `build_deck_v6.py` dijalankan ulang; konten pptx hasil rebuild diekstrak & di-diff dengan pptx committed (teks, tabel, notes per slide) | **Identik** (selisih byte hanya metadata timestamp tertanam) |
| G-1 gambar bebas teks | `gambar/pola-geometris.png` **dilihat langsung via visi sesi ini** (aturan 07.G-1 lapis b) | Lolos: pola geometris murni, **tidak ada teks/angka/watermark** |
| Hal 66–67 tesis | dirender via PyMuPDF (110 dpi) lalu dibaca visi | konsisten dengan kartu 7 (lihat temuan AP-03) |
| Hal 151 tesis | dirender + dibaca visi | benar xatimah doxologi; konsisten kartu 12 & jejak slide S13 |
| Jejak commit | `git fetch --unshallow` lalu `git show 9b017ee`, `git show 486246e` | keduanya ada: 9b017ee = edit v7 pada `build_deck_v6.py` + pptx + preview; 486246e = upload `tesis.pdf` (2.413.839 byte) oleh pemilik |
| Isi 14 slide (baca-balik) | ekstrak penuh teks+tabel+notes pptx final | semua slide berjejak halaman; nama pembimbing/universitas kosong (tidak dikarang); Q1–Q3 tanpa jawaban sesuai perintah pemilik |
| Cakupan validator meta | `grep tools/validate_repo.py` | klaim manifest TERVERIFIKASI: `ACTIVE_DOC_GLOBS = ["_meta/*.md"]` + `PANDUAN_PENGGUNA.md` — dokumen `sistem-presentasi/*` tidak dipindai rujukan & tidak masuk `REQUIRED_FILES` |

---

## 2. Temuan

ID `AP-nn`. Prioritas: **P1** = bertentangan prinsip/aturan inti sistem, **P2** = inkonsistensi state antar dokumen (risiko recovery), **P3** = housekeeping/risiko rendah.

| ID | Prioritas | Lapisan | Temuan | Bukti | Rekomendasi |
|---|---|---|---|---|---|
| AP-01 | **P1** | Skrip | `export_html.py` **hardcode path relatif ke root repo** (`sistem-presentasi/deck-aktif/presentasi-tesis-fikih-hiasan-wanita/keluaran/...`). Hanya jalan bila CWD = root repo ini. Ini **melanggar prinsip self-contained/portabel** (aturan 01.D; manifest: "Self-contained / portabel: Ya (wajib) — folder dapat diunduh jadi repo tersendiri") — di repo standalone path `sistem-presentasi/...` tidak ada. Skrip build lain CWD-independen (pakai `HERE`), jadi perilaku skrip tidak seragam. | Dijalankan dari folder deck → `PackageNotFoundError`; sumber baris 6-7 `export_html.py` | Ubah jadi relatif-`HERE` seperti `build_deck_v6.py`; perbaiki blok "Menjalankan build" di `START_DI_SINI.md` agar menyatakan CWD yang benar |
| AP-02 | **P1** | Skrip | `install_deps.sh` **tidak memasang PyMuPDF**, padahal jalur VISI (render→baca) adalah **jalur baca WAJIB** untuk bahan Arab (aturan 09; manifest: "Jalur VISI adalah jalur baca utama untuk Arab: TERVERIFIKASI BENAR" — render-nya memakai PyMuPDF). Sesi baru yang mengikuti `START_DI_SINI.md` step-by-step tidak bisa merender PDF Arab. | `install_deps.sh` hanya: python-pptx, Pillow, pypdf, python-docx, matplotlib. Audit ini harus `pip install pymupdf` ad-hoc di luar skrip | Tambah `pymupdf` ke daftar install + verifikasi import di `install_deps.sh` |
| AP-03 | **P2** | Deck (state) | **Kontradiksi 3 dokumen soal hal 67** tesis: `STATUS.md` "kartu 7 (العلة) hal 67 lanjutan **belum dibaca**"; catatan integritas `PEMAHAMAN_BAHAN.md` "hal 67 … **belum dibaca**"; sedangkan `CHECKLIST_CAKUPAN.md` "hal 67 **telah dibaca penuh**" dan isi kartu 7 memuat detail berlabel (67) (Maliki/Syafi'i/Hanbali/kesimpulan penulis). **Diverifikasi sesi ini via visi hal 67:** halaman itu memang berisi kelanjutan per mazhab + kesimpulan penulis + hadits wanita — cocok dengan kartu 7. **Kesimpulan: hal 67 SUDAH dibaca; dua catatan "belum dibaca" usang.** | `/tmp` render hal 67 vs kartu 7; teks ketiganya | Perbaiki `STATUS.md` + catatan integritas `PEMAHAMAN_BAHAN.md` (hapus "belum dibaca"); hapus butir "Petunjuk pemulihan #3" yang memerintahkan membaca hal 67 dulu. Catat di Log |
| AP-04 | **P2** | Deck (state) | **Kontradiksi mode gambar:** `RENCANA_VISUAL.md` bilang "Mode gambar: **M0** di hampir semua slide … **Tidak ada M3/M4**" dan "Yang TIDAK dipakai: **Gambar AI (M3)**", tetapi `DAFTAR_GAMBAR.md` mencatat 1 gambar **M3 (AI)** (`pola-geometris.png`) yang dipasang di ke-14 slide (terverifikasi ada di pptx: QA menghitung 14 gambar). `RENCANA_VISUAL.md` usang — M3 ditambahkan saat revisi v2 tanpa update dokumen. | `DAFTAR_GAMBAR.md` baris 1; `RENCANA_VISUAL.md` bagian "Arah umum" & "Yang TIDAK dipakai"; `qa_deck.py` → `gambar: 14` | Update bagian mode gambar `RENCANA_VISUAL.md` (M0 + aksen M3) + Log Keputusan |
| AP-05 | **P2** | Deck (state) | **Header status usang** di 3 living document: `BRIEF.md` "Status: **draft Tahap 1 — menunggu konfirmasi pengguna di G2**"; `RENCANA_VISUAL.md` "**G2 — menunggu approval**"; `OUTLINE.md` "**G2 — menunggu approval pengguna**" — padahal G1/G2/G3 semua disetujui (5 Sep) dan deck `completed` (v7). Sesi baru yang recovery bisa salah membaca tahap. | Header ketiga file vs `STATUS.md` (semua gate disetujui) | Update header + Log ketiga file ke status final |
| AP-06 | **P3** | Deck (state) | `OUTLINE.md` tidak sinkron struktur final: (a) "Jumlah slide: **13**" padahal final **14** (judul + 13 butir, satu bagian=satu slide); (b) S11 menggabungkan معالجة+تحقق padahal final dipisah (S11/S12); (c) S7 menulis "rekonstruksi **4** pertanyaan" padahal pemilik minta **Q1–Q3 saja** (3); (d) assertion S12 "و**سُئل** الله القبول" padahal slide final memakai "ن**سأل** الله القبول" (bentuk korektif 02.G) — slide sudah benar, dokumen yang usang. | Baca OUTLINE.md vs ekstrak 14 slide | Sinkronkan OUTLINE ke struktur final + Log |
| AP-07 | **P3** | Deck (state) | `STATUS.md` field "Output resmi: **belum ada berkas `.pptx`/`.html`**" padahal `keluaran/` (pptx + preview.html + index.html) sudah ter-commit di main. Template T6 meminta `[belum / path keluaran]`. | `git ls-files` keluaran/ (3 file ter-commit) vs STATUS.md | Isi field dengan path `keluaran/` |
| AP-08 | **P3** | Sistem (naming) | **Tabrakan penamaan G1/G2/G3:** `_generator/G1_DISCOVERY_BRIEF.md` (dipakai Tahap 1) vs gerbang approval G1 (pasca Tahap 2); `G3_DISCOVERY_KETENTUAN.md` (Discovery ketentuan institusi, opsional) vs gerbang G3 (approval Berkas Final, selalu) — tidak ada hubungannya. Bukti dampak nyata: `RENCANA_VISUAL.md` merujuk "aturan lantai (`_sistem/03`)" — nomor **rencana lama**; di penomoran final lantai ada di `_sistem/06` (03 = Memahami Kebutuhan). Renumbering rencana→final meninggalkan rujukan basi. | Nama file `_generator/` vs tabel gerbang `00_RENCANA_KERANGKA.md`/manifest; baris 3 `RENCANA_VISUAL.md` | (a) Perbaiki rujukan `_sistem/03`→`06` di `RENCANA_VISUAL.md`; (b) pertimbangkan ganti nama file generator (mis. `GEN_1_BRIEF`) atau tambahkan catatan pembatas di `START_DI_SINI.md` — keputusan pengguna |
| AP-09 | **P3** | Deck (struktur) | `BRIEF.md` menyimpang dari template T1: bagian "Perkataan pemilik (verbatim)" tidak ada di dalam BRIEF (ditaruh di file terpisah `PERKATAAN_PEMILIK_VERBATIM.md` yang **tidak ada di daftar file baku** deck); field "Preferensi penyajian" (T1/aturan 03.B) tidak diisi. | T1 vs BRIEF.md; `REQ_DECK` di `validate_system.py` tidak mencakup PERKATAAN_PEMILIK_VERBATIM.md | Dua opsi: (a) taruh verbatim di BRIEF sesuai T1 & hapus file terpisah, atau (b) resmikan `PERKATAAN_PEMILIK_VERBATIM.md` sebagai file baku (update T1 + `REQ_DECK` + 03.A.1). Isi field preferensi penyajian |
| AP-10 | **P3** | Repo (housekeeping) | `RINGKASAN_sistem-presentasi.md` berada di `_meta/_cadangan-claude/`, padahal struktur repo (dan Langkah 8 `00_RENCANA_KERANGKA.md`) menempatkan ringkasan cadangan di `_cadangan-claude/` root (di situ ada `RINGKASAN_sistem-konten-kreator.md`). Manifest menulis path-nya dengan benar (termasuk prefix `_meta/`), tapi lokasinya menyimpang dari konvensi meta. | `ls _cadangan-claude/` vs `ls _meta/_cadangan-claude/` | Pindahkan ke `_cadangan-claude/` root + koreksi path di manifest |
| AP-11 | P3 (sudah diketahui) | Meta | Cakupan `tools/validate_repo.py` belum mencakup `sistem-presentasi/*` (tidak ada di `REQUIRED_FILES`, tidak dipindai rujukan) — sehingga "VALIDATION PASSED" di level meta tidak menjamin dokumen sistem ini terperiksa. **Bukan temuan baru**: sudah dicatat eksplisit di `SYSTEM_MANIFEST.md` (bagian Lapisan self-audit) sebagai item terbuka. | `tools/validate_repo.py` baris REQUIRED_FILES + `ACTIVE_DOC_GLOBS` | Perluas `REQUIRED_FILES` + cakupan scan ke `sistem-presentasi/` (bisa digabung dengan audit meta berkala) |

### Catatan untuk pemilik (bukan temuan sistem)

- **Q2 (السؤال الثاني) masih rekonstruksi berlabel** — labelnya ada di speaker notes slide S7, **bukan di slide**. Pemilik sudah tahu (STATUS: "Q2 & nama pembimbing menunggu tinjauan"), tapi kalau slide dipresentasikan, penanda "rekonstruksi" tidak terlihat oleh mata. Opsi: tambah label kecil di slide, atau pemilik mengonfirmasi/mengganti naskah Q2.
- Pemilik menyatakan akan **menambah butir** kemudian — struktur deck memang sudah dirancang satu bagian=satu slide (mudah ditambah).

---

## 3. Yang Lolos Verifikasi (tidak ada temuan)

1. **Struktur sistem lengkap** sesuai rencana: `_sistem/01–10`, `_generator/G1–G3`, `_template/T1–T9`, validator, QA, acceptance tests, `START_DI_SINI.md` (self-contained).
2. **Reproducibility build:** rebuild dari skrip committed menghasilkan konten identik (dibuktikan diff struktural per slide).
3. **Jejak sumber (jangkar #1):** ke-14 slide berjejak halaman; spot-check via visi (hal 6, 66–67, 151) konsisten dengan kartu & isi slide; tidak ditemukan klaim tanpa jejak; field yang tidak ada di bahan (pembimbing/universitas) dikosongkan, bukan dikarang.
4. **G-1 (teks tak terbakar):** gambar M3 diverifikasi bebas teks via visi sesi ini; kepatuhan G-2 (geometri parsial, rasio aspect-safe via crop) konsisten dengan `DAFTAR_GAMBAR.md` + implementasi build.
5. **QA per-produksi:** `qa_deck.py` exit 0 (rtl, font complex-script, notes, tashkeel/bidi, gambar).
6. **Keputusan & log:** semua living document punya Log Keputusan; keputusan besar (G1/G2/G3) tercatat dengan tanggal; koreksi pengguna (v1→v7) tertinggal di `PELAJARAN_DECK_01.md` + Log.
7. **Konsistensi rujukan antar dokumen aktif:** semua rujukan bernomor di `_sistem/01–10`, `_generator/`, `ACCEPTANCE_TESTS.md` memakai penomoran final yang benar (kecuali 1 kasus di dokumen deck — AP-08).
8. **Commit jejak** di `BRIEF.md` (486246e) & `STATUS.md` (9b017ee) tervalidasi ada dan isinya cocok.

## 4. Utang Verifikasi (bukan temuan — kondisi yang tercatat)

- **Acceptance test AT-SP-01 … AT-SP-14 belum dijalankan** (hanya AT-SP-15 SIMULASI end-to-end yang tereksekusi, via deck #1). Bukti per run di `ACCEPTANCE_TEST_LOG.md`.
- Cakupan validator meta (AP-11) — item terbuka yang sudah didokumentasikan di manifest.
- Tinjauan bahasa Arab oleh penutur/kompeten asli (gerbang 02.G) — by design butuh manusia; deck #1 disetujui G3 oleh pengguna, tapi review penutur asli untuk slide S7-Q2 belum terjadi (menunggu pemilik).

## 5. Kondisi Berhenti & Langkah Berikutnya

Audit selesai; tidak ada perubahan file dari audit ini (selain laporan + pembaruan indeks yang diwajibkan repo). **Langkah berikutnya = keputusan pengguna** atas:

1. Temuan P1 (AP-01, AP-02) — perbaikan skrip, dampak kecil & terbalik; disarankan dikerjakan.
2. Temuan P2 (AP-03, AP-04, AP-05) — sinkronisasi living document deck #1; tidak menyentuh aturan.
3. Temuan P3 (AP-06 s/d AP-10) — housekeeping; AP-08b (ganti nama generator) & AP-09 (pilih opsi a/b) butuh keputusan desain.
4. AP-11 — perluasan validator meta (level meta-sistem, bisa terpisah).
5. Utang acceptance test AT-SP-01…14 — kapan dieksekusi (setelah temuan P1–P2 ditutup, atau sekarang).

Perbaikan apa pun mengikuti jalur: proposal → approval pengguna → implementasi di branch ini → PR. Urutan pelaksanaan bila disetujui semua: P1 dulu (skrip), lalu P2 (state deck), baru P3 (housekeeping) — supaya deck #1 tidak disentuh dua kali.
