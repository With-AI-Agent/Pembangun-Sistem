# System Manifest — Sistem Konten Kreator

- **Tujuan:** membangun dan memproduksi konten kreator berbantuan AI dari fondasi brand sampai konten siap publish.
- **Consumer:** operator/kreator solo dan agent kerja yang terhubung ke repository.
- **Status:** `candidate — audit P0+P1 closed, belum divalidasi pemakaian nyata`
- **Versi:** `0.3.0-audit-remediation`
- **Pemilik keputusan:** pengguna
- **Entry point agent:** `PROMPT_ENTRI_UNIVERSAL.md` (atau bagian Prompt Pembuka Universal di `panduan/PANDUAN_PENGGUNA.md`)
- **Entry point navigasi:** `_sistem/START_DI_SINI.md`
- **Instruksi utama:** `_sistem/00_CARA_PAKAI_SISTEM.md`
- **Living documents:** Brand Core, Channel Brief, Bank Konsistensi Visual, Model Konten Brief, arsip naskah
- **Audit acuan:** `_meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md` di master blueprint (audit independen yang sedang diremediasi)
- **Acceptance test:** `ACCEPTANCE_TESTS.md` (AT-KK-01 s/d AT-KK-08) — wajib dijalankan ulang setiap aturan `00`/`05`/`06` berubah; log eksekusi + bukti per run di `ACCEPTANCE_TEST_LOG.md`
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

## Batasan Platform

- **Dipakai via lmarena?** Ya — rujuk `_meta/PLATFORM_LMARENA.md` di repo meta
- **Fakta:** branch arena otomatis dibuat, tidak bisa push setelah PR merge/close (platform cabut akses), sesi bisa crash
- **Implikasi:** checkpoint tiap tahap + checkpoint diskusi ringan jika diskusi >5 giliran mendekati keputusan, karena tanpa commit sesi baru tidak bisa melanjutkan (FI-03) dan diskusi bisa hilang

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
- [ ] Prosedur checkpoint dan recovery diuji — *sebagian: mekanisme dasar terbukti di pilot-002 (FI-01 s/d FI-07), tapi itu menguji `STATUS.md` milik pilot. `_sistem/STATUS_TEMPLATE.md` sistem ini berubah 4 Sep 2026 (field approval per gerbang G1/G2/G3 + sumber eksternal). Versi barunya sudah dijalankan pada recovery nyata lewat **AT-KK-05 + AT-KK-05b dry run 4 Sep 2026** — perilaku agent benar (lanjut hanya dari tahap terbukti selesai, `G1 Tahap 3` tidak diperlakukan sebagai G2, state tidak konsisten dihentikan), tapi run itu **in-session dan terkontaminasi**, jadi belum memenuhi syarat "tanpa dipandu" di `ACCEPTANCE_TESTS.md` poin 4. Yang tersisa: jalankan ulang di sesi agent baru — prompt siap tempel di `ACCEPTANCE_TEST_LOG.md` bagian "Cara menjalankan ulang secara bersih"*
- [x] Audit P0 sudah ditutup — *K-01 s/d K-05 + M-01, lihat Log Evolusi*
- [ ] Pilot end-to-end berhasil — *belum: butuh 1 channel terisi penuh (L-04). Fixture `channel-fixture-narasi-sejarah` TIDAK menutup gate ini — dia bahan uji, berhenti di Tahap 3*
- [ ] Acceptance test sistem ini LULUS — *sebagian: AT-KK-05 + AT-KK-05b sudah dijalankan 4 Sep 2026 sebagai dry run in-session, hasilnya `belum LULUS` (terkontaminasi, tidak memenuhi syarat "tanpa dipandu"); 8 skenario lain belum diuji. Detail di `ACCEPTANCE_TEST_LOG.md`*

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
| L-05 acceptance test dapat diulang | P2 | **Sebagian** — 10 skenario ditulis di `ACCEPTANCE_TESTS.md` (AT-KK-01…08 + 2 varian); AT-KK-05 + AT-KK-05b sudah dijalankan 4 Sep 2026 sebagai dry run in-session (`belum LULUS`, terkontaminasi), 8 sisanya belum; fixture produksi pertama tersedia di `channel-fixture-narasi-sejarah/` + `_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/` |

## Log Evolusi

| Tanggal | Versi | Perubahan | Alasan |
|---|---|---|---|
| 3 Sep 2026 | 0.2.0-audit-remediation | K-02, K-04, M-03 ditutup | Hasil audit independen 3 Sep |
| 4 Sep 2026 | 0.3.0-audit-remediation | K-01, K-03, K-05, M-01, M-04 s/d M-09, L-02 ditutup | Menutup seluruh P0 dan P1 supaya sistem ini bisa dinilai layak jadi contoh resmi meta-sistem |
| 4 Sep 2026 | 0.3.0-audit-remediation | `ACCEPTANCE_TESTS.md` ditambahkan (L-05 sebagian) | Aturan baru P0/P1 belum punya cara verifikasi yang dapat diulang; tanpa ini "sudah diperbaiki" tidak bisa dibuktikan |
| 4 Sep 2026 | 0.3.0-audit-remediation | AT-KK-05 + AT-KK-05b dijalankan sebagai dry run; fixture produksi pertama dibuat; `ACCEPTANCE_TEST_LOG.md` ditambahkan | Gate "Prosedur checkpoint dan recovery diuji" dibuka kembali di commit `e463809` karena `STATUS_TEMPLATE.md` versi baru belum teruji. Run ini membuktikan template baru bisa dipakai recovery, tapi **tidak** diklaim LULUS karena dijalankan di sesi yang sama dengan yang membaca expected result (melanggar syarat "tanpa dipandu"). Verdict final menunggu sesi agent baru. Versi tidak dinaikkan: tidak ada dokumen aturan (`00`/`05`/`06`) yang berubah |
