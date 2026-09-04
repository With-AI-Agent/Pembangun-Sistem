# Status Unit — pilot-002-behavioral

- **Status:** `in-progress`
- **Level pemeriksaan:** `Sedang`
- **Tahap terakhir selesai:** Capture
- **Tahap berikutnya:** Extract
- **Output resmi:** `OUTPUT.md` (draft, belum released), `../pilot-001/OUTPUT.md` sebagai pembanding
- **Sumber konteks yang dibaca:**
  - `../../SYSTEM_MANIFEST.md`
  - `../../WORKFLOW.md`
  - `../../OUTPUT_TEMPLATE.md`
  - `../../QUALITY.md`
  - `../../fixtures/SUMBER_NYATA_PILOT_002.md`
  - `../../../_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`
  - `../../../_meta/02_PRINSIP_UNIVERSAL.md`
  - `../../../_meta/FAILURE_INJECTION_TESTS.md`
  - `../../../_meta/_internal/HANDOFF_NEXT_SESSION.md`
  - `../../../_meta/_internal/BEHAVIORAL_AUDIT_2026-09-03.md`
- **Keputusan baru:** Memilih sumber nyata dari dokumen meta sendiri untuk menguji apakah protokol checkpoint cukup jelas untuk dipelajari dan diverifikasi
- **Approval:** Belum — masih tahap Capture, belum perlu approval pengguna
- **Commit/PR:** Branch `arena/01a06bce-pembangun-sistem`, commit akan dibuat setelah Capture
- **Pekerjaan belum tersimpan:** Tidak ada setelah commit ini
- **Blocker/risiko:** Tidak ada untuk tahap Capture; risiko utama ada di tahap recovery test nanti
- **Waktu pembaruan:** 2026-09-04T09:00Z

## Log Tahap

### Capture — 2026-09-04 — SELESAI
- **Input:** `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` + `02_PRINSIP_UNIVERSAL.md`
- **Output:** Identitas sumber tercatat di `fixtures/SUMBER_NYATA_PILOT_002.md`
- **Verifikasi:** File sumber ada, tanggal akses dicatat, tujuan belajar jelas: menguji behavioral pilot dan recovery nyata sesuai handoff
- **Checkpoint:** STATUS diperbarui, akan di-commit sebelum lanjut ke Extract
- **Recovery test plan:** Setelah commit Capture, akan simulasikan FI-03 (output di workspace belum commit) dengan menahan commit OUTPUT.md

### Extract — BELUM
### Structure — BELUM
### Verify — BELUM
### Apply — BELUM
### Observe — BELUM

## Catatan Recovery Test (rencana)
- Setelah Extract: simulasi FI-01 (hapus STATUS, cek fail-closed)
- Setelah Structure: simulasi FI-02 (STATUS released tanpa OUTPUT)
- Setelah Verify: simulasi FI-04 (STATUS menunjuk branch berbeda)
- Setiap simulasi harus menghasilkan state_is_safe = False, sesuai `tools/test_failure_injection.py`
