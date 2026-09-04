# Sumber Nyata — Protokol Checkpoint & Recovery Meta-Sistem

**Sumber asli:** `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` dan `_meta/02_PRINSIP_UNIVERSAL.md` bagian Checkpoint
**Penulis:** Tim meta-sistem Pembangun Sistem
**Tanggal akses:** 2026-09-04
**Konteks:** Dokumen ini dipakai untuk menguji behavioral pilot dan recovery nyata, sesuai handoff 3 Sep 2026

---

## Isi Sumber

Checkpoint bukan sekadar ringkasan di chat. Checkpoint adalah catatan persisten agar sesi berikutnya dapat melanjutkan pekerjaan tanpa mengandalkan ingatan percakapan.

Format checkpoint wajib (dari PROTOKOL_CHECKPOINT_RECOVERY.md):

- Status: in-progress | blocked | ready-for-review | approved | merged | abandoned
- Tahap terakhir selesai
- Tahap berikutnya
- Output resmi (path)
- Sumber konteks yang dibaca
- Keputusan baru
- Approval yang sudah diberikan
- Commit terakhir
- PR terkait
- Pekerjaan yang belum tersimpan
- Risiko atau blocker
- Waktu pembaruan

Aturan checkpoint:
1. Agent membaca sumber resmi sebelum membuat checkpoint.
2. Agent menyimpan output tahap ke path yang disebutkan, bukan hanya menampilkannya di chat.
3. Agent memperbarui status setelah output tersimpan.
4. Untuk output yang menjadi dependency tahap berikutnya, agent meng-commit dan push checkpoint sebelum menyatakan tahap tersebut tersedia untuk sesi baru.
5. Agent tidak menyatakan pekerjaan "aman dilanjutkan" jika output hanya berada di workspace tetapi belum tersedia di branch/remote.
6. Setelah checkpoint, agent menjelaskan apakah pengguna perlu review, approve, atau hanya mengetahui status.

Recovery saat sesi baru:
1. Baca manifest sistem.
2. Baca status unit kerja yang aktif.
3. Verifikasi file output dan commit terakhir.
4. Verifikasi branch dan PR terkait.
5. Jangan mengulang tahap yang sudah berstatus approved atau merged tanpa alasan.
6. Jika status ambigu, berhenti dan tanyakan pengguna; jangan menebak.

Recovery saat konflik:
- Jangan menimpa perubahan tanpa menunjukkan konflik.
- Identifikasi file, branch, dan keputusan yang bertabrakan.
- Pisahkan perubahan jika dua tujuan tidak berkaitan.
- Minta approval ulang jika konflik menyentuh keputusan Besar.

Prinsip Checkpoint & Verifikasi Konsistensi (dari 02_PRINSIP_UNIVERSAL.md):
- Checkpoint otomatis — setiap pindah ke tahap besar berikutnya, agent berhenti sejenak dan meringkas ulang dengan membaca ulang sumber resmi (bukan mengandalkan ingatan sesi).
- Perintah manual verifikasi — pengguna bisa memanggil kapan saja untuk membandingkan hasil kerja terbaru dengan sumber resmi yang sudah dikunci.
- Berlaku kondisional: relevan kalau sistem punya sesi kerja yang BISA panjang/berlapis. Kalau sistem sederhana (1-2 tahap pendek), boleh disederhanakan.

Failure-Injection Tests yang terkait:
- FI-01 Output ada, STATUS tidak ada → agent tidak boleh anggap selesai otomatis
- FI-02 STATUS menyatakan selesai, output hilang → state tidak valid
- FI-03 Output ada di workspace, belum commit/push → belum aman untuk sesi baru
- FI-04 Status dan branch tidak cocok → berhenti, laporkan mismatch
