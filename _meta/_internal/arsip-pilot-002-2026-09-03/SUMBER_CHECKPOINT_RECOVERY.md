# Snapshot Sumber — Protokol Checkpoint & Recovery

- **Path asal:** `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`
- **Snapshot dibuat:** 2026-09-03
- **sha256 konten asli:** `bb0b857a1a7d1e606476c7942c2fac9bc846f8006d05652cfaa4a390fbe2a63a`
- **Cara pakai:** salinan beku ini dipakai sebagai bahan belajar unit `pilot-002` supaya ekstraksi tetap dapat ditelusuri ke versi sumber yang persis dibaca. Jika file asli berubah, snapshot ini tidak otomatis ikut berubah — perbedaan itu harus dicatat, bukan diasumsikan.

---

# Protokol Checkpoint & Recovery

## Tujuan

Checkpoint bukan sekadar ringkasan di chat. Checkpoint adalah catatan persisten agar sesi berikutnya dapat melanjutkan pekerjaan tanpa mengandalkan ingatan percakapan.

## Format checkpoint

Setiap unit kerja atau tahap besar yang menghasilkan input untuk tahap berikutnya wajib memperbarui file status yang sesuai.

```markdown
# Status — [Nama Unit Kerja]

- Status: `in-progress | blocked | ready-for-review | approved | merged | abandoned`
- Tahap terakhir selesai:
- Tahap berikutnya:
- Output resmi:
  - `[path]`
- Sumber konteks yang dibaca:
  - `[path]`
- Keputusan baru:
- Approval yang sudah diberikan:
- Commit terakhir:
- PR terkait:
- Pekerjaan yang belum tersimpan:
- Risiko atau blocker:
- Waktu pembaruan:
```

## Aturan checkpoint

1. Agent membaca sumber resmi sebelum membuat checkpoint.
2. Agent menyimpan output tahap ke path yang disebutkan, bukan hanya menampilkannya di chat.
3. Agent memperbarui status setelah output tersimpan.
4. Untuk output yang menjadi dependency tahap berikutnya, agent meng-commit dan push checkpoint sebelum menyatakan tahap tersebut tersedia untuk sesi baru.
5. Agent tidak menyatakan pekerjaan “aman dilanjutkan” jika output hanya berada di workspace tetapi belum tersedia di branch/remote.
6. Setelah checkpoint, agent menjelaskan apakah pengguna perlu review, approve, atau hanya mengetahui status.

## Recovery saat sesi baru

1. Baca manifest sistem.
2. Baca status unit kerja yang aktif.
3. Verifikasi file output dan commit terakhir.
4. Verifikasi branch dan PR terkait.
5. Jangan mengulang tahap yang sudah berstatus `approved` atau `merged` tanpa alasan.
6. Jika status ambigu, berhenti dan tanyakan pengguna; jangan menebak.

## Recovery saat konflik

- Jangan menimpa perubahan tanpa menunjukkan konflik.
- Identifikasi file, branch, dan keputusan yang bertabrakan.
- Pisahkan perubahan jika dua tujuan tidak berkaitan.
- Minta approval ulang jika konflik menyentuh keputusan Besar.
