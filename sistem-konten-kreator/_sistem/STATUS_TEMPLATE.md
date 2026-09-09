# Status Produksi — [Channel] — [Judul Konten]

- **Status:** `in-progress | blocked | ready-for-review | approved | merged | abandoned`
- **Channel:**
- **Model konten:**
- **Tahap terakhir selesai:**
- **Tahap berikutnya:**
- **Output resmi:**
  - `naskah-draft.md`
  - `breakdown-output.md` (atau `breakdown-shot.md` / nama lain sesuai unit yang dipakai)
  - `assets/`
- **Sumber konteks yang dibaca:**
- **Sumber eksternal dipakai:** `Tidak ada` / ada — `SUMBER.md` dibuat, klaim belum terverifikasi: [daftar atau `tidak ada`]
- **Keputusan baru:**
- **Approval yang sudah diberikan:** *(tulis per gerbang dengan kodenya — lihat Prinsip Approval Bertingkat di `_sistem/00_CARA_PAKAI_SISTEM.md` dan tabel gerbang per tahap di `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md`. Contoh: `G1 Tahap 3 — disetujui 2026-09-04`, `G2 naskah final — disetujui 2026-09-04`, `G3 merge — belum`. Jangan tulis "sudah dikonfirmasi" tanpa kode gerbang: G1 tidak pernah berarti G2 atau G3.)*
  - `G1 [tahap]:` belum / disetujui [tanggal]
  - `G2 [objek yang dikunci]:` belum / disetujui [tanggal]
  - `G3 merge:` belum / disetujui [tanggal]
- **Commit terakhir:**
- **PR terkait:**
- **Pekerjaan belum tersimpan:** Tidak ada
- **Risiko atau blocker:**
- **Waktu pembaruan:**

## Aturan

- Perbarui file ini setelah setiap tahap yang menghasilkan dependency baru.
- Jangan menyatakan tahap tersedia untuk sesi berikutnya sebelum output sudah tersimpan di branch.
- Jika status atau output tidak dapat diverifikasi setelah sesi terputus, berhenti dan minta klarifikasi.
- Field `Pekerjaan belum tersimpan`: nilai WAJIB EXACT `Tidak ada` (case-sensitive, tanpa backtick); jika ada yang belum tersimpan, isi daftar path-nya. Provenance: _meta/PROTOKOL_CHECKPOINT_RECOVERY.md di master — aturan sudah turun ke template ini; file induk tidak diperlukan.
