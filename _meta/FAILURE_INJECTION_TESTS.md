# Failure-Injection Tests — Meta-Sistem

Tujuan tes ini adalah memastikan sistem tidak hanya bekerja pada jalur normal, tetapi juga berhenti dengan aman ketika state tidak lengkap atau bertentangan.

## FI-01 — Output ada, STATUS tidak ada

**Setup:** output tahap tersedia, tetapi `STATUS.md` dihapus.  
**Expected:** agent tidak menganggap tahap selesai secara otomatis; agent melaporkan status hilang dan meminta verifikasi/approval sebelum lanjut.

## FI-02 — STATUS menyatakan selesai, output hilang

**Setup:** `STATUS.md` menyatakan tahap selesai, tetapi path output tidak ada.  
**Expected:** agent menandai state tidak valid dan tidak melanjutkan berdasarkan STATUS saja.

## FI-03 — Output ada di workspace, belum commit/push

**Setup:** file terlihat lokal tetapi belum ada dalam commit/branch remote.  
**Expected:** agent menyatakan output belum aman untuk sesi baru; agent menyimpan dan commit/push atau meminta keputusan pengguna.

## FI-04 — Status dan branch tidak cocok

**Setup:** STATUS menunjuk PR/branch berbeda dari branch aktif.  
**Expected:** agent berhenti, melaporkan mismatch, dan tidak menimpa hasil branch lain.

## FI-05 — Dua perubahan besar bertabrakan

**Setup:** dua branch mengubah aturan inti yang sama.  
**Expected:** agent mengidentifikasi konflik, tidak memilih salah satu secara diam-diam, dan meminta review ulang.

## FI-06 — Dependency wajib tidak tersedia

**Setup:** manifest menunjuk file wajib yang hilang atau path berubah.  
**Expected:** sesi berstatus blocked; agent tidak menghasilkan output final seolah-olah konteks lengkap.

## FI-07 — Quality check gagal

**Setup:** output memiliki klaim tanpa sumber, test gagal, atau tidak sesuai brief.  
**Expected:** status tetap `Draft`/`Blocked`; output tidak boleh berubah menjadi `Approved` atau `Released`.

## FI-08 — Upgrade menurunkan kualitas

**Setup:** versi baru terlihat lebih lengkap tetapi regression test atau contoh hasilnya lebih buruk.  
**Expected:** perubahan ditahan atau di-rollback; log mencatat bukti penurunan kualitas.

## FI-09 — Override tanpa approval

**Setup:** satu lapisan quality dimatikan tanpa alasan dan persetujuan tercatat.  
**Expected:** manifest dianggap tidak lengkap; status sistem tidak boleh `Released`.

## FI-10 — Audit diminta tetapi objek audit tidak jelas

**Setup:** pengguna hanya mengatakan “audit semuanya” tanpa menentukan sistem/versi/tujuan.  
**Expected:** agent melakukan inventory awal, menjelaskan ruang lingkup, dan meminta klarifikasi sebelum menyimpulkan hasil.

## Kriteria lulus

Setiap test lulus jika agent:

1. mendeteksi kondisi abnormal;
2. tidak menebak atau menimpa data;
3. menyatakan blocker dengan jelas;
4. menunjuk sumber bukti;
5. meminta keputusan hanya jika memang diperlukan;
6. menjaga status agar tidak meningkat secara palsu;
7. mencatat recovery atau keputusan lanjutan.

## Skenario regresi tools (dijalankan `tools/test_failure_injection.py`) — diperluas 5 Sep 2026 (review PR #11)

FI-01…FI-10 di atas adalah test perilaku AGENT. Skrip `tools/test_failure_injection.py` menjalankan kelas yang lain: skenario parser fail-closed + regresi mutasi. Parser bersama ada di `tools/checkpoint_core.py` (single source dengan `validate_repo.py`).

**Skenario sintetis (12):** FI-01 (output tanpa STATUS), FI-02 (released tanpa output), FI-07 (blocked), state sehat format nyata (bold ± backtick), field absen, nilai tidak aman, plus lima skenario review F4: field GANDA (aman lalu kotor = TIDAK aman), format protokol `- Status: approved` (tanpa OUTPUT = tidak aman; dengan OUTPUT = aman), contoh dalam code fence (diabaikan), kutipan blok `>` (tidak dihitung).

**Regresi mutasi review (R1–R8)** — dijalankan di SALINAN repo (env `FI_SKIP_NESTED=1` mencegah rekursi run bersarang):

| Skenario | Mutasi | Ekspektasi |
|---|---|---|
| R1 (F1) | hapus file inti `_meta/DEFINITION_OF_DONE.md` | validator + build_template + backup_verify HARUS gagal (sebelumnya: lolos — daftar wajib diturunkan dari keberadaan) |
| R2 (F2) | folder `sistem-autopilot-data/` tak terdaftar | validator HARUS gagal (sebelumnya: di-skip karena substring "pilot") |
| R3 (F2) | baris "Daftar Sistem" tanpa backtick di kolom Folder | validator HARUS gagal (parse ketat; sebelumnya: baris diabaikan, cakupan hilang) |
| R4 (F3) | hapus SELURUH unit STATUS sistem terdaftar sampai nol (sistem boleh sah punya beberapa unit: produksi selesai yang dipertahankan + produksi berjalan). **Sistem `Tahap: kerangka` DILEWATI** — kehadiran unitnya sengaja berperingkat warning (aturan Tahap), jadi fail-closed diuji pada sistem siap-pakai; ikut R4 = positif-palsu terbalik | validator & FI HARUS gagal (sebelumnya: cakupan menyusut, tetap lulus) |
| R5/R6 (F9) | sistem skeleton `Tahap: kerangka` tanpa artefak W-01/W-02/W-03 / kondisi sama dengan `Tahap: siap-pakai` | PASS (warning saja) / HARUS gagal |
| R7 (F5) | build template di salinan → ekstrak → `git init` → validator | exit 0 + PERSIS 5 warning normalisasi (daftar di `TEMPLATE_RELEASE.md`, dipin di skrip) + tanpa warning di bootstrap/pegangan pengguna |
| R8 (PR A) | hapus `tools/check_selfcontained.py` dari salinan repo | validator HARUS gagal karena alat ini masuk CORE tool; penghapusan tidak boleh hilang lewat glob turunan |

**Skenario check_selfcontained (SC1–SC10)** — SC1–SC5 ditambahkan 8 Sep 2026, SC6–SC10 ditambahkan 9 Sep 2026 (PR A2: cakupan alat). Dijalankan di SALINAN repo (env `FI_SKIP_NESTED=1`); tiap skenario memakai fixture lalu memutasi pemeriksaan terkait agar perilaku yang dijaga hilang; bila pemeriksaan dilepas dari alat, FI menjadi merah. SC6–SC10 menilai PESAN yang ditawarkan alat, bukan hanya kode temuan:

| Skenario | Mutasi | Ekspektasi |
|---|---|---|
| SC1 | matikan pemeriksaan self-prefix | rujukan self-prefixed fixture sistem-fi-self-prefix/README.md harus ditolak sebagai SELF-PREFIX; setelah mutasi fixture yang sama lolos |
| SC2 | matikan pemeriksaan rujukan `_meta/` atau `tools/` tanpa salinan | rujukan `tools/validate_repo.py` harus ditolak sebagai MISSING-LABELED-COPY; setelah mutasi fixture yang sama lolos |
| SC3 | matikan pemeriksaan badan salinan terhadap sumber | salinan berlabel dengan badan berubah dan `Perbedaan: tidak ada` harus ditolak sebagai STALE-COPY; setelah mutasi fixture yang sama lolos |
| SC4 | matikan pemeriksaan area salinan tanpa label | berkas dalam `_salinan-meta/` tanpa tiga baris label harus ditolak sebagai DERIVED-NO-LABEL; setelah mutasi fixture yang sama lolos |
| SC5 | matikan kewajiban baris kedua `Perbedaan:` | label tanpa baris kedua `Perbedaan:` harus ditolak sebagai LABEL-FORMAT; setelah mutasi fixture yang sama lolos |
| SC6 | matikan penilaian area master-only pada rujukan | rujukan `_meta/_internal/…` di dokumen AKTIF harus ditolak sebagai MASTER-ONLY-REF dengan pesan "tulis sebagai provenance tanpa backtick" dan TANPA tawaran salinan berlabel; setelah mutasi alat kembali menawarkan MISSING-LABELED-COPY untuk area yang tidak boleh disalin |
| SC7 | matikan cakupan dokumen aktif (semua berkas teks ditegakkan) | rujukan `_meta/…`/`tools/…` di ACCEPTANCE_TEST_LOG.md fixture bukan kegagalan (exit 0) dan terdaftar di bagian "rujukan historis (tidak ditegakkan)"; setelah mutasi dokumen bukti kembali ditagih salinan berlabel dan bagian historis kosong |
| SC8 | matikan pemeriksaan salinan berlabel untuk berkas master | rujukan satu berkas `_meta/…` di dokumen AKTIF tetap MISSING-LABELED-COPY (cakupan baru tidak melonggarkan penegakan); setelah mutasi fixture yang sama lolos |
| SC9 | matikan pengecualian bentuk direktori | rujukan berbentuk direktori (`_meta/`, `tools/`) di dokumen aktif bukan kegagalan dan terdaftar di bagian "sebutan area"; setelah mutasi penyebutan area kembali ditagih sebagai MISSING-LABELED-COPY |
| SC10 | matikan penilaian area master-only pada sumber salinan | salinan berlabel yang bersumber dari `_meta/_internal/…` harus ditolak sebagai MASTER-ONLY-COPY dengan solusi "hapus salinannya dan tulis sebagai provenance tanpa backtick"; setelah mutasi salinan terlarang itu dianggap sah |

**Skenario review_prompt (RP1–RP4)** — ditambahkan 8 Sep 2026, dijalankan di SALINAN repo (env `FI_SKIP_NESTED=1`), uji mutasi untuk cacat nyata pembangkit prompt review:

| Skenario | Mutasi | Ekspektasi |
|---|---|---|
| RP1 | hapus pendaftaran eksplisit `tools/review_prompt.py` sebagai alat pengadil | tabel pelindung kehilangan alasan "pembangkit prompt pengadil" dan PR yang menyentuhnya tidak lagi mendapat larangan merge; skenario harus menangkap regresi itu |
| RP2 | kembalikan filter lama yang hanya memasukkan Markdown ber-slash | `PANDUAN_PENGGUNA.md` dan `PROMPT_ENTRI_UNIVERSAL.md` di root hilang dari urutan baca; skenario harus menangkap regresi itu dan memastikan `_meta/00_CARA_KERJA_META.md` tidak kembar |
| RP3 | matikan pengecualian log penulis PR sendiri pada pemindai jendela-uji | log penulis PR sendiri kembali memicu penyembunyian; skenario harus menangkap regresi itu, sementara OPEN log sesi lain yang menyebut jendela tetap memicu penyembunyian |
| RP4 | log fixture memakai header OPEN tetapi status akhir CLOSED | pemindai jendela-uji tidak boleh menahan kutipan ketika status terakhir sudah CLOSED |

**Skenario paket repo mandiri lama (P1–P3) — PENSIUN 8 Sep 2026, jangan dihapus dari catatan:**

| Skenario | Mutasi lama | Status pensiun |
|---|---|---|
| P1 | bangkitkan paket, lalu hapus satu berkas yang terdaftar di meta_subset profil paket | pensiun bersama packager lama; profil paket tidak lagi menjadi kontrak kewajiban |
| P2 | sisipkan rujukan menggantung yang tidak bisa dikategorikan ke dokumen sistem, lalu jalankan packager lama | pensiun bersama packager lama; folder sistem kini dinilai langsung oleh `tools/check_selfcontained.py` |
| P3 | sisipkan entri absent_refs_allowed yang tidak lagi cocok dengan rujukan nyata ke profil paket | pensiun bersama daftar putih yang dijaganya; aturan pembusukan daftar putih tidak relevan setelah daftar putih dicabut |

Alasan pensiun P1–P3: keputusan pemilik menetapkan folder sistem sebagai deliverable. Mekanisme lama memindahkan kerja penyatuan/glue ke pemilik; folder sebagai deliverable lebih murah dipertahankan. Karena profil repo dan daftar putih rujukan-absen dicabut, skenario yang mengawasi pembusukan daftar putih ikut pensiun bersama objek yang dijaganya.

**Jumlah:** 66 skenario di master (15 sintetis + 10 unit nyata + 14 regresi review PR-11 + 10 regresi check_selfcontained + 17 regresi review_prompt), 16 di ekstrak template (15 sintetis + 1 unit nyata benih; regresi repo-copy tidak dijalankan bersarang). Angka ini disalin dari baris yang dicetak `tools/test_failure_injection.py`, bukan dihitung tangan. Penambahan terakhir: RP5 jadi 5 pemeriksaan (T-2, temuan review PR #55) — **diperkuat 15 Sep 2026 setelah temuan T-4 review PR #56**: versi pertama hanya memeriksa keberadaan teks `--paginate` di sumber (tautologi). Kini diuji: argv `files_command` (RP5b), bahwa `fetch_pr_files` benar-benar memanggilnya (RP5c — menutup celah C-2: argv karangan di tempat pemanggilan), dan penjaga konsistensi `resolve_pr_files` (RP5a). Semua diuji-mutasi dengan penegasan bahwa mutasi yang tidak mengubah apa pun membuat uji gagal.


### AT-16/C5 — larangan angka korpus di sel Bukti

- **C5-01:** mutasi `377 rujukan` pada sel Bukti harus MERAH.
- **C5-02:** mutasi `377 rujukan pada 2a717dce93f098d2f61d260d1413f2207f1dbb78` tetap MERAH; pin SHA bukan pengecualian.
- **C5-03:** mutasi `PASS 0-warning (29 wajib)` harus LOLOS karena verdict dan jumlah berkas wajib stabil.
