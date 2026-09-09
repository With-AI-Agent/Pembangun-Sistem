# System Manifest — Sistem Konten Kreator

- **Tujuan:** membangun dan memproduksi konten kreator berbantuan AI dari fondasi brand sampai konten siap publish.
- **Consumer:** operator/kreator solo dan agent kerja yang terhubung ke repository.
- **Status:** `candidate — audit P0+P1 closed, belum divalidasi pemakaian nyata`
- **Versi:** `0.3.7`
- **Tahap:** siap-pakai
- **Pemilik keputusan:** pengguna
- **Entry point agent:** `PROMPT_ENTRI_UNIVERSAL.md` (atau bagian Prompt Pembuka Universal di `panduan/PANDUAN_PENGGUNA.md`)
- **Entry point navigasi:** `_sistem/START_DI_SINI.md`
- **Instruksi utama:** `_sistem/00_CARA_PAKAI_SISTEM.md`
- **Living documents:** Brand Core, Channel Brief, Bank Konsistensi Visual, Model Konten Brief, arsip naskah
- **Audit acuan (provenance):** _meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md di master blueprint — P0+P1 ditutup 4 Sep, P2 sebagian (lihat tabel temuan di bawah)
- **Acceptance test:** **F7 DITUTUP 6 Sep 2026** — AT-KK-05 / Run 7 **LULUS** + AT-KK-05b / Run 8 **LULUS**, keduanya `0.3.4`. Riwayat: Run 4 **GAGAL** (`0.3.2`); Run 5 **GAGAL-metode** (`0.3.3`, koreksi pasca-review); Run 6 lama **void**. Status/bukti: `ACCEPTANCE_TEST_LOG.md` (Run 7 + Run 8).
- **Referensi historis (bukan instruksi aktif):** `_sistem/09_AUDIT_MIGRASI_GITHUB_AGENT.md` — ditandai `agent_instruction: reference_only`, dikecualikan dari template bersih
- **Backup/template:** belum dirilis

## Bentuk Sistem

- **Struktural:** bertingkat — Brand Core → Channel → Model Konten → Produksi
- **Operasional:** siklus produksi dengan opsi workflow custom per Model Konten
- **Unit kerja:** satu sistem domain, satu channel, satu model konten, atau satu konten produksi
- **Kriteria siap produksi:** brief terkait berstatus `Operational`, dependency valid, dan konteks wajib berhasil diverifikasi

## Prinsip yang Berlaku

| Prinsip | Status | Penerapan |
|---|---|---|
| Hierarki | Berlaku | Level bawah mewarisi dan hanya meng-override secara eksplisit |
| Chaining | Berlaku dengan checkpoint | Output tahap disimpan dan status diperbarui; tidak hanya mengandalkan chat |
| Approval bertingkat | Berlaku | Keputusan yang menyebar/sulit dibalik wajib review isi |
| Checkpoint & recovery | Berlaku | Setiap tahap yang menjadi dependency berikutnya memiliki status persisten |
| Log keputusan | Berlaku | Living document mencatat tanggal, perubahan, dan alasan |

## Warisan (Kontrak) — meta v1.3.0

W-01 pegangan ✔ (`panduan/PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md`); W-02 LOG_SESI ✔ (section di `_sistem/00_CARA_PAKAI_SISTEM.md` + prompt); W-03 field checkpoint ✔ (`_sistem/STATUS_TEMPLATE.md` + fixture); W-04 manifest ✔; W-05 log keputusan ✔ (Log Evolusi + per dokumen); W-06 QA ✔ (`QUALITY_ASSURANCE_AND_EVOLUTION.md` di folder ini); W-07 fakta platform ✔ (bagian Batasan Platform inline); W-08 approval ✔ (G1/G2/G3); W-09 ringkasan cadangan ✔ (disinkronkan 5 Sep). Tidak ada override.

## Batasan Platform

- **Dipakai via lmarena?** Ya — rujuk `_meta/PLATFORM_LMARENA.md` di repo meta (salinan berlabelnya ikut folder ini, di _salinan-meta/)
- **Fakta:** branch arena otomatis dibuat, tidak bisa push setelah PR merge/close (platform cabut akses), sesi bisa crash
- **Implikasi:** checkpoint tiap tahap + **log sesi berkelanjutan** (`LOG_SESI_YYYY-MM-DD.md` — aturan ringkas self-contained di `_sistem/00_CARA_PAKAI_SISTEM.md`), karena tanpa commit sesi baru tidak bisa melanjutkan (FI-03) dan konteks sesi (keputusan, koreksi, fakta penting) hilang permanen saat crash (agent sesi baru tidak punya akses ke chat sesi lama)

## Risiko Utama

- Drift voice/visual akibat konteks tidak dibaca.
- Karakter Tipe B terulang tanpa terdeteksi.
- Output tahap belum tersimpan ketika sesi terputus (fakta platform #2 + #3 di PLATFORM_LMARENA.md — tidak bisa push setelah merge, sesi bisa crash).
- Asset eksternal hilang atau tidak dapat direproduksi.
- Sumber eksternal memiliki masalah fakta, hak cipta, atau atribusi.

## Gate Sebelum Status Operational

- [x] Semua dokumen instruksi aktif tersedia
- [ ] Brand Core dan brief terkait sudah approved/merged — *belum: belum ada channel nyata yang diisi*
- [x] Index arsip naskah dan index karakter tersedia bila relevan — *kontrak & format ditetapkan (K-01); sudah diinstansiasi (masih kosong) di fixture `channel-fixture-narasi-sejarah/arsip-naskah/` 4 Sep 2026; instansiasi channel nyata tetap menyusul*
- [x] Workflow standar/custom sudah dinyatakan eksplisit — *termasuk jalur non-visual (M-04)*
- [x] Prosedur checkpoint dan recovery diuji — **DITUTUP 6 Sep 2026 (retest selesai).** AT-KK-05 / Run 7 **LULUS** + AT-KK-05b / Run 8 **LULUS**, keduanya `0.3.4`. Riwayat retest: Run 4 **GAGAL** (`0.3.2`); Run 5 **GAGAL-metode** (`0.3.3`); Run 6 lama **void**. Historis: Run 2 + Run 3 **LULUS** (`0.3.1`). Status/bukti: `ACCEPTANCE_TEST_LOG.md`.

- [x] **Folder mandiri menurut AT-17** — 9 Sep 2026, versi `0.3.7`: python3 tools/check_selfcontained.py --sistem sistem-konten-kreator --report berakhir PASS dari root repo master (validator sistem dijalankan di salinan folder yang hanya berisi folder ini). Salinan berlabel ada di direktori _salinan-meta/; bukti: `ACCEPTANCE_TEST_LOG.md` bagian "Folder mandiri AT-17".
- [x] **Paket repo mandiri LULUS** (riwayat; mekanisme packager sudah pensiun) — 7 Sep 2026, versi `0.3.6`. tools/pack_repo.py mode pemeriksaan hijau (0 pemblokir); hasil pack lolos validator repo (0 warning) + validator sistem di DALAM hasil pack. Protokol: _meta/PAKET_REPO_MANDIRI.md di master (provenance); bukti: `ACCEPTANCE_TEST_LOG.md` bagian "Paket repo mandiri"
- [x] Audit P0 sudah ditutup — *K-01 s/d K-05 + M-01, lihat Log Evolusi*
- [ ] Pilot end-to-end berhasil — belum; temuan L-04 masih terbuka.
- [ ] Acceptance test sistem ini LULUS — **belum**. AT-KK-05 / Run 7 `0.3.4` **LULUS**; Run 5 / AT-KK-05 `0.3.3` GAGAL-metode (koreksi pasca-review); Run 6 lama void; Run 8 / AT-KK-05b `0.3.4` **LULUS**; AT-KK-01/02/03/03b/04/06/07/08 belum diuji. Status/bukti: `ACCEPTANCE_TEST_LOG.md`.

## Temuan Audit yang Masih Terbuka

Dari _meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md di master (provenance):

| Kode | Prioritas | Status |
|---|---|---|
| K-01 deteksi Tipe B tanpa sumber data | P0 | **Ditutup** 4 Sep 2026 |
| K-02 recovery sesi terputus | P0 | **Ditutup** 3 Sep 2026 |
| K-03 approval tidak dibedakan | P0 | **Ditutup** 4 Sep 2026 |
| K-04 kontradiksi kemampuan video | P0 | **Ditutup** 3 Sep 2026 |
| K-05 sumber, fakta, hak cipta | P0 | **Ditutup** 4 Sep 2026 |
| M-01 konteks wajib deterministik | P0 | **Ditutup** 4 Sep 2026 |
| M-02 kontrak output living document | P1 | **Sebagian** — status, versi, checklist kelengkapan, log keputusan sudah ada di template brief; belum diterapkan ke semua living document |
| M-03 rujukan panduan ambigu | P2 | **Ditutup** 3 Sep 2026 |
| M-04 jalur produksi non-visual | P1 | **Ditutup** 4 Sep 2026 |
| M-05 acuan utama terlalu absolut | P1 | **Ditutup** 4 Sep 2026 |
| M-06 reproducibility setelah folder dihapus | P1 | **Ditutup** 4 Sep 2026 |
| M-07 conflict/concurrency | P1 | **Ditutup** 4 Sep 2026 |
| M-08 status locked vs merged | P1 | **Ditutup** 4 Sep 2026 |
| M-09 audit historis di folder aktif | P2 | **Ditutup** 4 Sep 2026 |
| L-01 kata "otomatis" perlu dibatasi | P2 | **Sebagian** — klaim utama sudah dilunakkan; sisa kalimat minor belum disisir |
| L-02 klaim agent tahu semua konteks | P2 | **Ditutup** 4 Sep 2026 |
| L-03 batas ukuran arsip & indexing | P2 | **Terbuka** |
| L-04 contoh channel terisi penuh | P2 | **Terbuka** — gate pilot end-to-end |
| L-05 acceptance test dapat diulang | P2 | **Sebagian**. AT-KK-05 / Run 7 **LULUS** + AT-KK-05b / Run 8 **LULUS**, keduanya `0.3.4` — **F7 DITUTUP 6 Sep 2026**. Riwayat: Run 4 **GAGAL** (`0.3.2`); Run 5 **GAGAL-metode** (`0.3.3`); Run 6 lama **void**. 8 skenario lain belum diuji. Status/bukti: `ACCEPTANCE_TEST_LOG.md` |

## Log Evolusi

| Tanggal | Versi | Perubahan | Alasan / bukti |
|---|---|---|---|
| 3 Sep 2026 | 0.2.0-audit-remediation | K-02, K-04, M-03 ditutup | Audit independen 3 Sep |
| 4 Sep 2026 | 0.3.0-audit-remediation | K-01, K-03, K-05, M-01, M-04 s/d M-09, L-02 ditutup | Audit P0/P1 |
| 4 Sep 2026 | 0.3.0-audit-remediation | Acceptance test tersedia; L-05 sebagian | `ACCEPTANCE_TEST_LOG.md` |
| 4 Sep 2026 | 0.3.0-audit-remediation | AT-KK-05 / AT-KK-05b, Run 1: **belum LULUS — dry run** | `ACCEPTANCE_TEST_LOG.md` Run 1 |
| 4 Sep 2026 | 0.3.1-audit-remediation | Pembaruan aturan recovery; AT-KK-05 / Run 2: **LULUS** | `ACCEPTANCE_TEST_LOG.md` Run 1–2 |
| 5 Sep 2026 | 0.3.2-warisan-sync | Sinkronisasi kontrak warisan meta v1.3.0; F7 **TERBUKA** | `ACCEPTANCE_TEST_LOG.md` |
| 5 Sep 2026 | 0.3.1-audit-remediation | AT-KK-05b / Run 3: **LULUS** | `ACCEPTANCE_TEST_LOG.md` Run 3 |
| 6 Sep 2026 | 0.3.2-warisan-sync | AT-KK-05 / Run 4: **GAGAL**; F7 **TERBUKA** | `ACCEPTANCE_TEST_LOG.md` Run 4 |
| 6 Sep 2026 | **0.3.3** | Aturan metode pada `ACCEPTANCE_TESTS.md` poin 6/6a dan struktur rujukan diperbarui; dokumen `00`/`05`/`06` tidak diubah | F7 **TERBUKA**; Run 5 / AT-KK-05 dan Run 6 / AT-KK-05b **dijadwalkan**, `0.3.3`. Rincian: `ACCEPTANCE_TEST_LOG.md` Run 4 |
| 6 Sep 2026 | 0.3.3 | AT-KK-05 / Run 5: **berjalan** (dicatat; PR #14 review, belum merged); F7 **TERBUKA** | `ACCEPTANCE_TEST_LOG.md` Run 5 |
| 6 Sep 2026 | **0.3.4** | Koreksi pasca-review: verdict Run 5 → GAGAL-metode; aturan 6d (`ACCEPTANCE_TESTS.md` poin 6); reset state uji Run 7; dokumen `00`/`05`/`06` tidak diubah | F7 **TERBUKA**; Run 6 lama **void**; Run 7 / AT-KK-05 + Run 8 / AT-KK-05b **dijadwalkan**, `0.3.4`. Rincian: `ACCEPTANCE_TEST_LOG.md` (koreksi pasca-review) |
| 6 Sep 2026 | 0.3.4 | AT-KK-05 / Run 7: **LULUS** (pencatat sesi terpisah, M2); F7 **TERBUKA** (menunggu Run 8) | `ACCEPTANCE_TEST_LOG.md` Run 7 |
| 6 Sep 2026 | 0.3.4 | AT-KK-05b / Run 8: **LULUS** (pencatat sesi terpisah, M2); **F7 DITUTUP** — Run 7 + Run 8 LULUS pada `0.3.4` | `ACCEPTANCE_TEST_LOG.md` Run 8 |
| 6 Sep 2026 | **0.3.5** | Protokol Review Independen diwariskan dari meta v1.4.0: file baru `PROTOKOL_REVIEW_INDEPENDEN.md` (root sistem — varian KK: audit paparan di penutupan gate + materialitas dinilai reviewer; pencatatan run tidak dipegang sesi subjek (M2); 6d berlaku juga untuk reviewer selama jendela run) + rujukan di `_sistem/START_DI_SINI.md`, `QUALITY_ASSURANCE_AND_EVOLUTION.md` (level trigger KK), `ACCEPTANCE_TESTS.md` (poin 7; poin 1–6 tidak diubah), `panduan/PANDUAN_PENGGUNA.md` (varian 1-baris; blok pembuka/penutup tidak disentuh) | Alasan: dokumen protokol baru yang TIDAK mengubah aturan 00/05/06 → regresi acceptance AT-KK tidak terpicu (diff `00`/`05`/`06` = 0 baris; induk: _meta/PROTOKOL_REVIEW_INDEPENDEN.md di master) |
| 9 Sep 2026 | **0.3.7** | Folder ini menjadi **mandiri menurut AT-17**: rujukan asal-usul — termasuk protokol review independen, protokol QA, dan protokol kemandirian yang sudah punya varian sendiri di folder ini — serta area yang tidak boleh keluar dari master ditulis sebagai provenance tanpa backtick; satu dokumen master yang benar-benar dipakai saat sistem dijalankan, fakta platform (butir W-07), dibawa sebagai salinan berlabel di direktori _salinan-meta/. Dokumen `00`/`05`/`06` **tidak diubah** → regresi AT-KK tidak terpicu | Bukti: `ACCEPTANCE_TEST_LOG.md` bagian "Folder mandiri AT-17" (perintah + keluaran gerbang mandiri, PASS). **Menunggu review independen L1** — PR tanpa merge |
| 7 Sep 2026 | **0.3.6** | Sistem menjadi **dapat dibangkitkan jadi repo mandiri**: validator sistem sendiri `_sistem/validate_system.py` (BARU, self-contained — root dihitung sendiri, tanpa impor kode luar, tidak tahu-menahu soal `_meta/` maupun `tools/`); gate baru "Paket repo mandiri LULUS"; rujukan protokol 1 baris di `QUALITY_ASSURANCE_AND_EVOLUTION.md` + 1 baris di `_sistem/START_DI_SINI.md`. Dokumen `00`/`05`/`06` **tidak diubah** → regresi AT-KK tidak terpicu | Bukti: `ACCEPTANCE_TEST_LOG.md` bagian "Paket repo mandiri" (perintah + keluaran validator DI DALAM hasil pack, keduanya PASS/0-warning). Protokol: _meta/PAKET_REPO_MANDIRI.md di master (provenance). **Menunggu review independen L1** — tidak ada gate acceptance lain yang diklaim tertutup |
