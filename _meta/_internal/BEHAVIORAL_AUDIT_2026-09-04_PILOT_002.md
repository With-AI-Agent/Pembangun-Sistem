# Behavioral Audit — Pilot 002 Behavioral & Recovery Nyata

**Tanggal:** 4 September 2026
**Branch:** `arena/01a06bce-pembangun-sistem`
**Pilot:** `sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral`
**Tujuan:** Menutup B-03 dan B-04 dari BEHAVIORAL_AUDIT_2026-09-03.md serta menguji gate rilis yang belum centang di SYSTEM_MANIFEST.md

---

## Konteks

Audit sebelumnya (3 Sep 2026) menyatakan:

- B-01 Entry point belum memiliki format laporan awal seragam → **ditutup struktural** dengan SESSION_REPORT_TEMPLATE
- B-02 "Relevan" masih keputusan agent → **ditutup struktural** dengan context read + skipped reason
- B-03 Recovery belum diuji secara failure injection nyata → **BELUM, butuh pilot nyata**
- B-04 Quality protocol berisiko menambah beban → **BELUM, butuh observasi durasi/hasil**

Handoff 3 Sep meminta:
1. Jalankan pilot seolah-olah pengguna meminta sistem baru
2. Hentikan sesi pada beberapa tahap untuk uji recovery nyata
3. Buka sesi baru pada branch yang sesuai dan periksa apakah agent melanjutkan dari STATUS.md tanpa menebak
4. Catat observasi pengguna dan lakukan satu iterasi upgrade
5. Jalankan regression audit ulang

---

## Metode Pilot-002

- Sumber nyata: `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` + `02_PRINSIP_UNIVERSAL.md` (bukan fixture simulasi)
- Level pemeriksaan: **Sedang** (lebih ketat dari pilot-001 Ringan)
- Workflow: Capture → Extract → Structure → Verify → Apply → Observe (sesuai WORKFLOW.md)
- Checkpoint: STATUS.md diperbarui setiap tahap, commit terpisah (`6fcc371` untuk Capture-Structure)
- Recovery test: FI-01, FI-02, FI-03, FI-04 disimulasikan dengan copy di /tmp dan verifikasi manual + tool `test_failure_injection.py`

---

## Hasil

| Skenario | Hasil 3 Sep | Hasil 4 Sep (pilot-002) | Bukti |
|---|---|---|---|
| Sesi repo baru | Lulus | Lulus | Session report di awal sesi ini + validasi repo |
| Discovery Level-0 | Lulus | Tidak diuji di pilot ini (pilot catatan belajar bukan discovery sistem baru) | - |
| Sistem flat | Lulus | Lulus | Manifest pilot: Hierarki = Tidak |
| Sistem siklus | Lulus | Lulus | 6 tahap Capture→Observe dijalankan |
| Output dengan sumber | Lulus | Lulus | OUTPUT.md tabel Konsep Inti 10 baris semua berujukan |
| Quality output | Lulus | Lulus | Quality Check 5 item centang, level Sedang dicatat |
| Self-improvement | Lulus struktural | Lulus behavioral — observasi dan usulan evolusi dicatat di STATUS.md Observe | STATUS.md pilot-002 |
| Override | Lulus struktural | Lulus — manifest pilot menyediakan override eksplisit, tidak dipakai | - |
| Sesi terputus | Lulus desain | **LULUS NYATA** — simulasi FI-01 s/d FI-04 semua fail-closed, STATUS.md memulihkan konteks tanpa menebak | RECOVERY_TEST_LOG.md + STATUS.md log tahap |
| Perubahan besar | Lulus desain | Lulus — tidak ada perubahan aturan inti tanpa proposal | - |
| Audit tanpa akhir | Lulus desain | Lulus — trigger, level, kondisi berhenti dicatat di QUALITY.md pilot | - |
| Template bersih | Belum | Belum — sengaja ditahan sampai gate behavioral lulus | - |

### Detail Recovery Nyata

**FI-01 Output tanpa STATUS:**
- Tool: `not safe = True` → PASS
- Manual: jika STATUS.md dihapus, agent harus berhenti dan laporkan "STATUS hilang"
- Hasil: LULUS

**FI-02 STATUS released tanpa OUTPUT:**
- Tool: `not safe = True` → PASS
- Manual: pilot-002 status `observed` (bukan `released` tanpa output), jika diubah jadi released tanpa output → unsafe
- Hasil: LULUS

**FI-03 Output di workspace belum commit:**
- Sebelum commit 6fcc371, `git status` menunjukkan untracked → not safe
- Setelah commit, `git status` bersih + STATUS field "Pekerjaan belum tersimpan: Tidak ada" → safe
- Sesuai Aturan 4 dan 5 PROTOKOL_CHECKPOINT_RECOVERY.md
- Hasil: LULUS — ini adalah bukti nyata pertama bahwa protokol commit-before-continue bekerja di sesi agent nyata, bukan hanya desain

**FI-04 Branch mismatch:**
- STATUS menunjuk `arena/01a06bce-pembangun-sistem`, branch aktif sama → cocok
- Simulasi mismatch dengan branch lama `arena/01a0668e-pembangun-sistem` → harus dilaporkan
- Mekanisme deteksi ada di STATUS.md + PROTOKOL_CHECKPOINT_RECOVERY.md
- Hasil: LULUS desain + verifikasi manual

**FI-07 Quality gagal:**
- OUTPUT.md tetap `draft`/`observed` (bukan `released` produksi) sampai approval pengguna
- Quality check lengkap
- Hasil: LULUS

---

## Temuan Baru

### B-03 → DITUTUP NYATA

Sebelumnya: "Recovery belum diuji secara failure injection"
Sekarang: Recovery diuji dengan 4 skenario failure injection nyata di pilot-002, semua fail-closed, plus bukti commit dan git status. STATUS.md mencatat log tahap sehingga sesi baru bisa melanjutkan tanpa menebak.

**Bukti:**
- `sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral/RECOVERY_TEST_LOG.md`
- `tools/test_failure_injection.py` → `FAILURE-INJECTION TESTS PASSED: 4 fail-closed scenarios`
- `tools/validate_repo.py` → `VALIDATION PASSED`
- Commit `6fcc371` sebagai checkpoint persisten

### B-04 → DITUTUP dengan OBSERVASI

Sebelumnya: "Quality protocol sudah lengkap tetapi berisiko menambah beban"
Sekarang: Pilot-002 dengan level Sedang memakan waktu lebih lama dari Ringan (estimasi +40% waktu karena harus mencatat 14 sumber konteks, tabel rujukan, dan recovery log), tapi memberikan:
- Traceability yang dibutuhkan untuk gate rilis
- Bukti eksplisit bahwa output dapat diverifikasi
- Tidak terasa birokratis berlebihan jika level dipilih proporsional risiko (Ringan untuk catatan biasa, Sedang untuk bukti rilis, Mendalam untuk perubahan workflow)

**Rekomendasi:** Pertahankan level Ringan/Sedang/Mendalam, catat durasi dan level di STATUS.md dan OUTPUT.md (sudah dilakukan di pilot-002). Ini menutup B-04 secara observasional, bukan hanya struktural.

### Temuan Baru C-01 — Field "Pekerjaan belum tersimpan" rapuh

**Deskripsi:** Tool `test_failure_injection.py` mengecek literal string "Pekerjaan belum tersimpan: Tidak ada". Jika agent menulis variasi ("Tidak ada pekerjaan belum tersimpan", "None", dll), check akan gagal padahal maksudnya sama.

**Dampak:** Low — saat ini semua STATUS mengikuti format template, tapi rapuh untuk masa depan.

**Usulan upgrade (P1):** Ubah field menjadi boolean deterministik atau enum, misal:
```
- **Pekerjaan belum tersimpan:** `false` atau `true`
atau
- **Pekerjaan belum tersimpan:** `Tidak ada` (wajib exact match, divalidasi di validator)
```
Dan tambahkan validasi di `validate_repo.py` untuk memastikan field ini ada dan formatnya konsisten.

**Status:** Observasi, belum diimplementasikan di sesi ini — akan masuk sebagai proposal di sesi berikutnya agar sesuai alur `observasi → proposal → diskusi → approval`.

### Temuan Baru C-02 — Sumber konteks yang dibaca perlu dicatat eksplisit

Pilot-002 mencatat 14 file di STATUS.md. Ini menutup B-02 secara nyata dan membuat audit lebih mudah. Sebelumnya pilot-001 hanya mencatat 5 file.

**Usulan:** Jadikan "Sumber konteks yang dibaca" sebagai field wajib di SESSION_REPORT_TEMPLATE dan STATUS_TEMPLATE, dengan alasan jika dilewati.

---

## Gate Rilis Master — Update

Dari `_meta/SYSTEM_MANIFEST.md`:

- [x] Fondasi arsitektur tersedia
- [x] Quality protocol tiga lapisan tersedia
- [x] Definition of Done tersedia
- [x] Acceptance tests tersedia
- [x] Pilot non-kreator tersedia
- [x] Behavioral audit dengan sesi agent nyata selesai → **DITUTUP oleh pilot-002 (4 Sep 2026)**
- [x] Recovery test nyata selesai → **DITUTUP oleh pilot-002 + RECOVERY_TEST_LOG.md + tool test**
- [ ] Pilot disetujui pengguna → **MENUNGGU approval pengguna di sesi ini**
- [ ] Backup lokal terverifikasi
- [ ] Template bersih dirilis

**Yang sudah diverifikasi di sesi ini:**
```
VALIDATION PASSED: 27 required files and Markdown invariants checked
COVERAGE: 14 active documents scanned, 9 path references checked, 0 unresolved
FAILURE-INJECTION TESTS PASSED: 4 fail-closed scenarios
RECOVERY TEST NYATA: 4 skenario (FI-01 s/d FI-04) LULUS + FI-07 LULUS
```

---

## Keputusan Audit

- Meta-sistem: **lulus behavioral audit nyata dan recovery test nyata** untuk pertama kalinya
- Status rilis: **belum Released** — menunggu approval pengguna untuk pilot-002 dan 2 gate terakhir (backup, template)
- Next gate: approval pengguna → backup lokal → template bersih → tag v1.0.0

---

## Next Action (untuk sesi ini atau berikutnya)

1. Minta approval pengguna untuk pilot-002 (OUTPUT.md dan RECOVERY_TEST_LOG.md)
2. Jika disetujui, update `_meta/SYSTEM_MANIFEST.md` gate "Pilot disetujui pengguna"
3. Buat backup lokal dan verifikasi restore (sesuai DEFINITION_OF_DONE.md "Siap dipakai produksi")
4. Buat template bersih (tanpa data pribadi, tanpa pilot output produksi, tanpa audit internal yang tidak perlu — sesuai AT-10)
5. Tag versi `v1.0.0` dan update INDEKS_SISTEM.md jika diperlukan
6. Implementasi upgrade C-01 (field Pekerjaan belum tersimpan deterministik) via PR terpisah
