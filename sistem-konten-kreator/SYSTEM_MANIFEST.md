# System Manifest — Sistem Konten Kreator

- **Tujuan:** membangun dan memproduksi konten kreator berbantuan AI dari fondasi brand sampai konten siap publish.
- **Consumer:** operator/kreator solo dan agent kerja yang terhubung ke repository.
- **Status:** `candidate — remediation in progress`
- **Versi:** `0.2.0-audit-remediation`
- **Pemilik keputusan:** pengguna
- **Entry point agent:** `PROMPT_ENTRI_UNIVERSAL.md` (atau bagian Prompt Pembuka Universal di `panduan/PANDUAN_PENGGUNA.md`)
- **Entry point navigasi:** `_sistem/START_DI_SINI.md`
- **Instruksi utama:** `_sistem/00_CARA_PAKAI_SISTEM.md`
- **Living documents:** Brand Core, Channel Brief, Bank Konsistensi Visual, Model Konten Brief, arsip naskah
- **Audit aktif:** `_sistem/09_AUDIT_MIGRASI_GITHUB_AGENT.md` (referensi historis) dan `_meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md` di master blueprint
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

## Risiko Utama

- Drift voice/visual akibat konteks tidak dibaca.
- Karakter Tipe B terulang tanpa terdeteksi.
- Output tahap belum tersimpan ketika sesi terputus.
- Asset eksternal hilang atau tidak dapat direproduksi.
- Sumber eksternal memiliki masalah fakta, hak cipta, atau atribusi.

## Gate Sebelum Status Operational

- [ ] Semua dokumen instruksi aktif tersedia
- [ ] Brand Core dan brief terkait sudah approved/merged
- [ ] Index arsip naskah dan index karakter tersedia bila relevan
- [ ] Workflow standar/custom sudah dinyatakan eksplisit
- [ ] Prosedur checkpoint dan recovery diuji
- [ ] Audit P0 sudah ditutup
- [ ] Pilot end-to-end berhasil
