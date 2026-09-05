# System Manifest — Sistem Konten Kreator

- **Tujuan:** membangun dan memproduksi konten kreator berbantuan AI dari fondasi brand sampai konten siap publish.
- **Consumer:** operator/kreator solo dan agent kerja yang terhubung ke repository.
- **Status:** `candidate — audit P0+P1 closed, belum divalidasi pemakaian nyata`
- **Versi:** `0.3.2-warisan-sync`
- **Tahap:** siap-pakai
- **Pemilik keputusan:** pengguna
- **Entry point agent:** `PROMPT_ENTRI_UNIVERSAL.md` (atau bagian Prompt Pembuka Universal di `panduan/PANDUAN_PENGGUNA.md`)
- **Entry point navigasi:** `_sistem/START_DI_SINI.md`
- **Instruksi utama:** `_sistem/00_CARA_PAKAI_SISTEM.md`
- **Living documents:** Brand Core, Channel Brief, Bank Konsistensi Visual, Model Konten Brief, arsip naskah
- **Audit acuan (provenance):** `_meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md` di master blueprint — P0+P1 ditutup 4 Sep, P2 sebagian (lihat tabel temuan di bawah)
- **Acceptance test:** `ACCEPTANCE_TESTS.md` (AT-KK-01 s/d AT-KK-08) — wajib diulang setiap aturan `00`/`05`/`06` berubah; bukti per run di `ACCEPTANCE_TEST_LOG.md`. **F7 tetap TERBUKA:** retest terpicu perubahan `00` pada `0.3.2-warisan-sync`; persiapan PR #12 sudah merged. **Update 6 Sep 2026 WIB: Run 4 (AT-KK-05) GAGAL integritas metode**, rinciannya di log Run 4 dan Rekaman Hasil. Retest AT-KK-05b pada 0.3.2 belum dijalankan. Remediasi aturan untuk mencegah paparan jawaban melalui konteks wajib masih proposal yang memerlukan review/approval; implementasi, kenaikan versi, dan sesi subjek baru belum diklaim selesai. Run 4 tidak boleh dipakai menutup F7; kedua skenario harus LULUS pada versi perbaikan yang sama. Gate historis 0.3.1 di bawah tidak diubah oleh pencatatan ini.
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

- **Dipakai via lmarena?** Ya — rujuk `_meta/PLATFORM_LMARENA.md` di repo meta
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
- [x] Prosedur checkpoint dan recovery diuji — **DITUTUP 5 Sep 2026.** Kedua klausul LULUS pada versi sistem yang sama (`0.3.1-audit-remediation`), keduanya clean run di sesi agent baru: **AT-KK-05 LULUS** 4 Sep 2026 di `arena/01a06d25-pembangun-sistem` (jalur normal — lanjut hanya dari Tahap 4, `G1 Tahap 3` tidak diperlakukan sebagai G2; bukti `ACCEPTANCE_TEST_LOG.md` Run 2), dan **AT-KK-05b LULUS** 5 Sep 2026 di `arena/01a06d58-pembangun-sistem` (state tidak konsisten — STATUS mengklaim Tahap 4 selesai + `breakdown-output.md` ADA padahal file tidak ada; agent berhenti dan melapor `BLOCKED`, tidak membuat ulang diam-diam, tidak mengoreksi STATUS sendiri, selaras FI-02/FI-03; bukti `ACCEPTANCE_TEST_LOG.md` Run 3). Mekanisme dasar FI-01 s/d FI-07 sudah terbukti di pilot-002. *Catatan cakupan: gate ini menutup jalur checkpoint/recovery saja — bukan acceptance test sistem secara keseluruhan (lihat gate di bawah).*

<!-- riwayat gate (sebelum ditutup):
- [ ] Prosedur checkpoint dan recovery diuji — *sebagian + 1 klausul LULUS: **AT-KK-05 LULUS** pada clean run sesi baru 4 Sep 2026 (versi `0.3.1-audit-remediation`) di `arena/01a06d25-pembangun-sistem` — agent lanjut hanya dari Tahap 4, `G1 Tahap 3` tidak diperlakukan sebagai G2, dan tidak membaca `ACCEPTANCE_TESTS.md`/handoff sebelum memutuskan; bukti di `ACCEPTANCE_TEST_LOG.md` Run 2. Tapi **AT-KK-05b (state tidak konsisten) belum diuji** (`belum diuji` di Rekaman Hasil), jadi gate ini **tetap tidak dicentang**. Mekanisme dasar FI-01 s/d FI-07 sudah terbukti di pilot-002; yang tersisa untuk menutup gate: jalankan AT-KK-05b (copy fixture ke /tmp, klaim Tahap 4 + `breakdown-output.md` ADA tanpa membuat file, agent harus berhenti dan melapor)*
-->

- [x] Audit P0 sudah ditutup — *K-01 s/d K-05 + M-01, lihat Log Evolusi*
- [ ] Pilot end-to-end berhasil — *belum: butuh 1 channel terisi penuh (L-04). Fixture `channel-fixture-narasi-sejarah` TIDAK menutup gate ini — dia bahan uji, berhenti di Tahap 3*
- [ ] Acceptance test sistem ini LULUS — *sebagian: **AT-KK-05 LULUS** (clean run 4 Sep 2026) dan **AT-KK-05b LULUS** (clean run 5 Sep 2026), keduanya pada versi `0.3.1-audit-remediation`; 8 skenario lain (AT-KK-01/02/03/03b/04/06/07/08) **belum diuji**, jadi gate ini tetap terbuka. Detail di `ACCEPTANCE_TEST_LOG.md` Run 2 dan Run 3*

## Temuan Audit yang Masih Terbuka

Dari `_meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md`:

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
| L-05 acceptance test dapat diulang | P2 | **Sebagian** — 10 skenario ditulis di `ACCEPTANCE_TESTS.md` (AT-KK-01…08 + 2 varian); **AT-KK-05 LULUS** clean run 4 Sep dan **AT-KK-05b LULUS** clean run 5 Sep 2026 (keduanya `0.3.1-audit-remediation`; baris ini disinkronkan 5 Sep — sebelumnya masih menyebut 05b "belum diuji", temuan M-19 audit meta); 8 sisanya belum diuji; fixture tersedia di `channel-fixture-narasi-sejarah/` + `_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/` |

## Log Evolusi

| Tanggal | Versi | Perubahan | Alasan |
|---|---|---|---|
| 3 Sep 2026 | 0.2.0-audit-remediation | K-02, K-04, M-03 ditutup | Hasil audit independen 3 Sep |
| 4 Sep 2026 | 0.3.0-audit-remediation | K-01, K-03, K-05, M-01, M-04 s/d M-09, L-02 ditutup | Menutup seluruh P0 dan P1 supaya sistem ini bisa dinilai layak jadi contoh resmi meta-sistem |
| 4 Sep 2026 | 0.3.0-audit-remediation | `ACCEPTANCE_TESTS.md` ditambahkan (L-05 sebagian) | Aturan baru P0/P1 belum punya cara verifikasi yang dapat diulang; tanpa ini "sudah diperbaiki" tidak bisa dibuktikan |
| 4 Sep 2026 | 0.3.0-audit-remediation | AT-KK-05 + AT-KK-05b dijalankan sebagai dry run; fixture produksi pertama dibuat; `ACCEPTANCE_TEST_LOG.md` ditambahkan | Gate "Prosedur checkpoint dan recovery diuji" dibuka kembali di commit `e463809` karena `STATUS_TEMPLATE.md` versi baru belum teruji. Run ini membuktikan template baru bisa dipakai recovery, tapi **tidak** diklaim LULUS karena dijalankan di sesi yang sama dengan yang membaca expected result (melanggar syarat "tanpa dipandu"). Verdict final menunggu sesi agent baru. Versi tidak dinaikkan: tidak ada dokumen aturan (`00`/`05`/`06`) yang berubah |
| 4 Sep 2026 | 0.3.1-audit-remediation | Aturan recovery dipertegas di `00_CARA_PAKAI_SISTEM.md`: baris "Lanjut produksi yang terputus" kini mewajibkan `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` bagian "Recovery saat sesi baru", output tahap diverifikasi **di branch**, plus 4 aturan mengikat (verifikasi bukan percaya klaim / lanjut hanya dari tahap terbukti selesai / approval per kode gerbang / berhenti kalau output diklaim ada tapi hilang) | Temuan dry run AT-KK-05: prosedur recovery cuma disebut satu kalimat di `05` dan tidak dirujuk tabel Konteks Wajib, jadi agen yang patuh tabel bisa melewati verifikasi branch (FI-02/FI-03). Diterapkan **sebelum** run bersih pertama — belum ada test berstatus LULUS, jadi tidak ada baseline yang dibatalkan. Konsekuensi: run bersih AT-KK-05 wajib dijalankan pada 0.3.1, dan dry run sebelumnya tercatat sebagai uji 0.3.0 |
| 5 Sep 2026 | 0.3.2-warisan-sync | Sinkronisasi kontrak warisan meta v1.3.0: tabel Warisan ditambahkan; wording provenance ("Audit acuan", rujukan recovery di `00_CARA_PAKAI_SISTEM.md` baris Lanjutan terputus → aturan inline menang, `_meta` opsional); fix M-19 (baris L-05 basi menyebut AT-KK-05b "belum diuji" padahal LULUS 5 Sep); ringkasan cadangan disinkronkan | Permintaan pengguna: butir wajib harus tertanam & TERUKUR untuk semua sistem. **KOREKSI 5 Sep (review PR #11, F7):** klaim awal "perubahan wording/pencatatan saja, regresi TIDAK terpicu" SALAH — baris tabel File wajib di `00_CARA_PAKAI_SISTEM.md` (baris "Lanjut produksi yang terputus") memang BERUBAH: protokol recovery meta dari "wajib dibaca" menjadi provenance/opsional, digantikan 4 aturan inline mengikat. Itu perubahan aturan `00` → klausul regresi acceptance test TERPICU dan belum dijalankan → **pengecualian tercatat: clean-run acceptance dijadwalkan first task sesi berikutnya** (sesi pembuat tidak memenuhi syarat uji buta karena sudah membaca expected result — alasan sama yang dipakai reviewer independen) |
| 5 Sep 2026 | 0.3.1-audit-remediation | **AT-KK-05b LULUS** pada clean run sesi baru (`ACCEPTANCE_TEST_LOG.md` Run 3); gate "Prosedur checkpoint dan recovery diuji" **ditutup/dicentang** | AT-KK-05 (jalur normal) sudah LULUS 4 Sep pada versi yang sama; yang tersisa untuk menutup gate hanyalah varian state tidak konsisten. Run 3 membuktikan agent **berhenti dan melapor** saat `STATUS.md` mengklaim `breakdown-output.md` ADA padahal tidak ada — tidak membuat ulang diam-diam, tidak mengoreksi STATUS sendiri (FI-02/FI-03 terpenuhi). Versi tidak dinaikkan: tidak ada dokumen aturan (`00`/`05`/`06`) yang berubah, hanya pencatatan hasil. Gate "Acceptance test sistem ini LULUS" tetap terbuka — 8 skenario lain belum diuji |
| 6 Sep 2026 (WIB) | 0.3.2-warisan-sync | **Run 4 AT-KK-05 GAGAL integritas metode** dicatat di `ACCEPTANCE_TEST_LOG.md`; F7 tetap terbuka | Perilaku recovery memenuhi klausul Then, tetapi subjek telah membaca ringkasan expected result melalui manifest sebelum keputusan pertama. Tidak ada gate yang diubah atau status dinaikkan; aturan/versi belum diubah, remediasi dan retest pada sesi baru masih wajib setelah review/approval terpisah. Revisi naskah produksi bukan remediasi metode dan tidak mengubah verdict. |
