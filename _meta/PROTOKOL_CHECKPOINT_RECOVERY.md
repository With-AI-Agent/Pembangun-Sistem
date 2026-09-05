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
- Validator `tools/validate_repo.py` dan `tools/test_failure_injection.py` mengecek `Tidak ada` untuk menentukan safe state (parser keduanya menerima bentuk bold `**Pekerjaan belum tersimpan:**` dan nilai dalam backtick — disatukan tingkat ketelitiannya di audit meta 5 Sep, temuan M-02)
- Alasan: field ini dipakai oleh fail-closed check otomatis (FI-03). Format bebas menyebabkan false negative. Field ABSEN (tidak ada sama sekali) = selalu TIDAK AMAN, bukan dianggap aman.
- **Aturan `Waktu pembaruan` (Q-O3 — ditutup 5 Sep 2026, audit meta):** diisi pada SETIAP checkpoint dan di akhir sesi; format `YYYY-MM-DD — <peristiwa singkat>` (jam tidak wajib). Konvensi lokal unit tidak boleh lagi dianggap "aturan sumber yang belum ada".

## Aturan checkpoint

1. Agent membaca sumber resmi sebelum membuat checkpoint.
2. Agent menyimpan output tahap ke path yang disebutkan, bukan hanya menampilkannya di chat.
3. Agent memperbarui status setelah output tersimpan.
4. Untuk output yang menjadi dependency tahap berikutnya, agent meng-commit dan push checkpoint sebelum menyatakan tahap tersebut tersedia untuk sesi baru. **Alasan kausal:** Karena sesi bisa crash kapan saja (fakta platform di `PLATFORM_LMARENA.md` #3), file yang hanya di workspace belum aman untuk sesi baru (FI-03). Tanpa commit+push, sesi baru **tidak bisa** melanjutkan.
5. Agent tidak menyatakan pekerjaan “aman dilanjutkan” jika output hanya berada di workspace tetapi belum tersedia di branch/remote. **Alasan kausal:** Remote belum punya file-nya, jadi sesi baru tidak bisa baca — bukan policy, tapi constraint fisik git.
6. Setelah checkpoint, agent menjelaskan apakah pengguna perlu review, approve, atau hanya mengetahui status.

## Log Sesi Berkelanjutan (LOG_SESI — pengganti "checkpoint diskusi ringan")

**Fakta platform:** Sesi lmarena bisa menjadi unusable di tengah jalan (chat tidak bisa lanjut, error halaman, kadang tidak bisa dibuka lagi). Agent sesi baru **tidak punya akses ke chat sesi lama** — ingatan yang bertahan hanya file di repo. Workaround resmi (tambah `/download-workspace` di URL) tetap ada, tapi bergantung pada tindakan pengguna *setelah* crash — bukan mekanisme utama.

**Kenapa "checkpoint kalau >5 giliran" diganti:** aturan lama berbasis ambang + judgment ("mendekati keputusan") — sebelum ambang tercapai tidak ada yang tercatat, dan diskusi eksploratif tidak selalu "mendekati" keputusan. Akibatnya konteks bisa hilang dalam jumlah besar. Masalahnya bukan "checkpoint terlalu jarang", tapi checkpoint diposisikan sebagai mekanisme darurat padahal seharusnya pencatatan adalah **mode normal**.

**Policy baru — catat berkelanjutan, bukan checkpoint periodik:**
- Setiap sesi yang menghasilkan informasi penting memelihara satu file **`LOG_SESI_YYYY-MM-DD.md`** (format: `TEMPLATE_LOG_SESI.md`), di folder scope kerja (unit/deck, sistem, atau root repo).
- Agent **append + update header "Keadaan Sesi" + commit + push segera setelah tiap pertukaran yang menghasilkan informasi baru** — bukan mekanis tiap giliran.
- **Yang dicatat:** keputusan/koreksi/kendala/preferensi pengguna (near-verbatim), proposal/klaim penting agent + dasarnya, kesepakatan & penolakan + alasan, fakta/hasil verifikasi sesi ini, perubahan state kerja, pertanyaan terbuka.
- **Yang TIDAK dicatat:** konfirmasi, basa-basi, pengulangan isi yang sudah ada di `STATUS.md`/Log Keputusan (tunjuk path-nya), dump chat. (Filter ini WAJIB — inilah yang membuat mekanisme ini efisien, bukan overkill.)
- **Akhir sesi:** header "Keadaan Sesi" diisi final dan ditandai `CLOSED` (atau `OPEN` + "dilanjutkan di mana" kalau memang lanjut sesi lain).
- **Alasan kausal:** biaya over-recording = beberapa detik per pertukaran; biaya under-recording = hilangnya jam konteks (pengguna menjelaskan ulang, keputusan di-litigate ulang). Asimetri biaya ini yang menentukan desain: catat yang penting, segera, dan biarkan floor-nya tetap aman.

**Kapan file tidak perlu dibuat:** sesi yang benar-benar tanpa informasi baru (mis. cuma cek status lalu selesai) — cukup commit terakhir + keadaan `CLOSED` tidak diperlukan sama sekali.

## Recovery saat sesi baru

1. Baca manifest sistem.
2. Baca status unit kerja yang aktif.
3. Verifikasi file output dan commit terakhir.
4. Verifikasi branch dan PR terkait. **Alasan kausal:** Branch `arena/...` dibuat otomatis oleh platform (fakta #1 di `PLATFORM_LMARENA.md`), jadi harus verifikasi `git branch --show-current`. Juga cek `gh pr list --state all --limit 20` — jika PR dari branch aktif sudah MERGED/CLOSED, maka sesi ini **tidak bisa** push lagi (fakta #2), harus buka sesi baru dari `main`. (Perintahnya `--state all`: PR merged/closed tidak terlihat di `--state open` — temuan M-04 audit 5 Sep 2026.)
5. Jangan mengulang tahap yang sudah berstatus `approved` atau `merged` tanpa alasan. **Kriteria "alasan sah" (Q-O2 — ditutup 5 Sep 2026, audit meta):** (a) instruksi eksplisit pengguna yang BARU, dikutip + tanggal, dicatat di STATUS unit; atau (b) bukti kecacatan ber-rujukan (path file/commit/hasil test) dicatat di STATUS unit. Selain dua itu → berhenti dan tanya pengguna; jangan menebak dan jangan mengulang diam-diam.
6. Jika status ambigu, berhenti dan tanyakan pengguna; jangan menebak.
7. Cari `LOG_SESI_*.md` **terbaru** (root repo, folder sistem, folder unit yang disentuh). Kalau keadaannya `OPEN` → **baca, laporkan keadaan sesinya, dan konfirmasi ke pengguna** sebelum lanjut — itu konteks sesi sebelumnya yang tidak boleh ditanya ulang. File `DISKUSI_MENTAH_*.md` lama (pra-v1.2.0) diperlakukan sama sebagai arsip diskusi.

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

**Skenario B — Sesi crash di tengah diskusi/kerja (tanpa penutupan yang benar):**
- **Fakta:** Sesi menjadi unusable (chat tidak bisa lanjut, error halaman); kadang tidak bisa dibuka lagi.
- **Mitigasi:** Buka sesi baru; entry point otomatis mencari `LOG_SESI_*.md` terbaru — yang `OPEN` berisi keadaan terakhir (apa yang disepakati, apa yang terbuka, langkah berikutnya). Baca header "Keadaan Sesi" dulu, kronologi hanya kalau perlu, lalu lanjut dari commit terakhir yang terbukti aman. Jangan menebak keputusan yang belum tercatat di log.
- **Backstop:** kalau log tidak ada/kosong (sesi lama pra-mekanisme ini, atau agent lalai), gunakan `/download-workspace` (tambah di akhir URL sesi) jika masih bisa diakses, dan laporkan ke pengguna apa yang *tidak* bisa dipulihkan — jangan mengarang konteks.
