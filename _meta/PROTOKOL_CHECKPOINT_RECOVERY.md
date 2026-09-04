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
- Pekerjaan yang belum tersimpan: `Tidak ada` atau daftar path yang belum tersimpan
- Risiko atau blocker:
- Waktu pembaruan:
```

**Aturan format deterministik untuk `Pekerjaan belum tersimpan`:**
- Nilai HARUS exact `Tidak ada` jika tidak ada pekerjaan belum tersimpan (case-sensitive, tanpa variasi seperti "tidak ada", "None", "n/a")
- Jika ada pekerjaan belum tersimpan, nilai HARUS berupa daftar path atau deskripsi singkat yang dimulai dengan selain `Tidak ada` (misal: `- [path] belum commit`)
- Validator `tools/validate_repo.py` dan `tools/test_failure_injection.py` mengecek literal `Tidak ada` untuk menentukan safe state
- Alasan: field ini dipakai oleh fail-closed check otomatis (FI-03). Format bebas menyebabkan false negative.

## Aturan checkpoint

1. Agent membaca sumber resmi sebelum membuat checkpoint.
2. Agent menyimpan output tahap ke path yang disebutkan, bukan hanya menampilkannya di chat.
3. Agent memperbarui status setelah output tersimpan.
4. Untuk output yang menjadi dependency tahap berikutnya, agent meng-commit dan push checkpoint sebelum menyatakan tahap tersebut tersedia untuk sesi baru. **Alasan kausal:** Karena sesi bisa crash kapan saja (fakta platform di `PLATFORM_LMARENA.md` #3), file yang hanya di workspace belum aman untuk sesi baru (FI-03). Tanpa commit+push, sesi baru **tidak bisa** melanjutkan.
5. Agent tidak menyatakan pekerjaan “aman dilanjutkan” jika output hanya berada di workspace tetapi belum tersedia di branch/remote. **Alasan kausal:** Remote belum punya file-nya, jadi sesi baru tidak bisa baca — bukan policy, tapi constraint fisik git.
6. Setelah checkpoint, agent menjelaskan apakah pengguna perlu review, approve, atau hanya mengetahui status.

## Checkpoint Diskusi Ringan (baru — untuk mitigasi crash platform)

**Fakta platform:** Sesi lmarena bisa menjadi unusable di tengah jalan (chat tidak bisa lanjut, error halaman). Arena sendiri sediakan workaround `/download-workspace`.

**Policy karena fakta tersebut:**
- Jika diskusi sudah >5-7 giliran dan mendekati keputusan, agent **harus** buat file `DISKUSI_MENTAH_YYYY-MM-DD_HHMM.md` di `unit-aktif/[id]/` atau `_meta/_internal/discussions/` berisi ringkasan diskusi, opsi yang dipertimbangkan, keputusan yang hampir diambil, pertanyaan terbuka.
- Status `in-progress`, commit dengan pesan `checkpoint diskusi: ...`
- **Kapan tidak perlu:** Diskusi pendek <3 giliran atau masih eksplorasi awal — tidak perlu, cukup lanjut chat (efisien vs aman).
- **Alasan kausal:** Menyelamatkan konteks dari crash platform tanpa harus log semua chat. Ini balance antara "sedih diskusi panjang hilang" vs "sistem jadi tidak efisien kalau semua harus dicatat".

## Recovery saat sesi baru

1. Baca manifest sistem.
2. Baca status unit kerja yang aktif.
3. Verifikasi file output dan commit terakhir.
4. Verifikasi branch dan PR terkait. **Alasan kausal:** Branch `arena/...` dibuat otomatis oleh platform (fakta #1 di `PLATFORM_LMARENA.md`), jadi harus verifikasi `git branch --show-current`. Juga cek `gh pr list` — jika PR sudah MERGED/CLOSED, maka sesi ini **tidak bisa** push lagi (fakta #2), harus buka sesi baru dari `main`.
5. Jangan mengulang tahap yang sudah berstatus `approved` atau `merged` tanpa alasan.
6. Jika status ambigu, berhenti dan tanyakan pengguna; jangan menebak.
7. Jika ada file `DISKUSI_MENTAH_*.md` yang lebih baru dari STATUS.md, baca itu juga sebagai konteks diskusi yang belum jadi file final — ini hasil dari checkpoint diskusi ringan.

## Recovery saat konflik

- Jangan menimpa perubahan tanpa menunjukkan konflik.
- Identifikasi file, branch, dan keputusan yang bertabrakan.
- Pisahkan perubahan jika dua tujuan tidak berkaitan.
- Minta approval ulang jika konflik menyentuh keputusan Besar.

## Recovery saat platform failure (baru)

**Skenario A — PR sudah merge tapi lanjut kerja di sesi lama:**
- **Fakta:** Platform mencabut akses push setelah merge (tidak bisa push lagi).
- **Gejala:** `git push` gagal, atau file baru tidak muncul di GitHub.
- **Mitigasi:** Buka sesi baru dari `main`, jangan pakai sesi lama. Jika sudah terlanjur ada file terjebak, gunakan workaround resmi Arena: tambah `/download-workspace` di akhir URL sesi untuk download zip workspace, lalu pindahkan manual ke sesi baru.

**Skenario B — Sesi crash di tengah diskusi panjang:**
- **Fakta:** Sesi menjadi unusable (chat tidak bisa lanjut, error halaman).
- **Mitigasi:** Buka sesi baru, baca STATUS.md terakhir + `DISKUSI_MENTAH_*.md` jika ada. Lanjutkan dari tahap terakhir yang terbukti aman (commit terakhir). Jangan menebak keputusan yang belum di-commit.
