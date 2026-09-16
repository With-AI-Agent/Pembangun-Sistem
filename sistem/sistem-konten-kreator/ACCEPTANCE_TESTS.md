# Acceptance Tests — Sistem Konten Kreator

### Skenario uji **perilaku** sistem ini: apakah agent benar-benar bertindak sesuai aturan, bukan sekadar apakah filenya ada. Setiap test punya expected result yang dapat diperiksa. Kalau hasil aktual berbeda, sistem belum boleh naik status.

**Protokol induk:** _meta/ACCEPTANCE_TESTS.md di master (menguji meta-sistem; provenance). Dokumen ini menguji **sistem domain konten kreator** — dua-duanya berlaku, tidak saling menggantikan.

**Asal:** temuan **L-05** di _meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md di master (provenance; area ini tidak boleh keluar dari master) — audit sebelumnya sangat detail tapi belum menyediakan skenario uji dengan expected result, sehingga tidak ada cara mengulang verifikasi secara konsisten.

---

## Cara menjalankan

1. **Test ini dijalankan pada sesi agent nyata**, bukan dibaca sebagai teori. Satu test = satu sesi (atau satu segmen sesi yang jelas batasnya).
2. Pakai channel/konten **fixture** — boleh dummy, tapi harus lewat alur asli. Jangan pakai data produksi yang penting, karena beberapa test sengaja merusak state.
3. Catat hasilnya di tabel **Rekaman Hasil** di bawah: tanggal, versi sistem, LULUS/GAGAL, dan bukti (path file/commit/kutipan respons agent).
4. **LULUS hanya kalau agent bertindak benar tanpa dipandu.** Kalau agent baru benar setelah diingatkan, itu **GAGAL** — yang diuji adalah apakah aturannya cukup jelas untuk diikuti sendiri.
5. Kalau sebuah test gagal, perbaiki **dokumen aturannya**, lalu ulangi test itu. Jangan memperbaiki hasilnya secara manual lalu menyatakan lulus.
6. **Pemisahan konteks orientasi dari bahan evaluasi uji (permanen):**
   - **6a — Jalur baca wajib/orientasi sesi baru:** `START_DI_SINI.md`, `00_CARA_PAKAI_SISTEM.md`, STATUS unit, brief, `INDEKS_SISTEM.md`, `SYSTEM_MANIFEST.md`, dan `LOG_SESI` terbaru **TIDAK boleh memuat rumusan klausul expected result atau narasi perilaku yang diharapkan dari sebuah verdict run**. Rujukan hasil uji di sana **hanya status**: kode test, LULUS/GAGAL (atau belum dijalankan/dijadwalkan), versi, dan pointer ke `ACCEPTANCE_TEST_LOG.md`. **Rujukan pointer boleh; jawaban tidak.** Berlaku juga pada riwayat, komentar HTML, kutipan, atau lampiran di dokumen orientasi tersebut.
   - **6b — Bukti lengkap tidak dibuang:** metode, kronologi paparan, klausul penilaian, kutipan respons dan alasan verdict disimpan di `ACCEPTANCE_TEST_LOG.md`. Dokumen orkestrasi hanya untuk pengguna/perancang/pencatat, bukan konteks subjek sebelum keputusan pertama ter-commit. Pointer bukan instruksi membuka bahan evaluasi sebelum fase pencatatan.
   - **6c — Cakupan:** aturan produksi generik dan state operasional yang sebenarnya (termasuk data approval per gerbang) tetap tersedia; yang dipisahkan adalah materi evaluasi run, bukan informasi yang dibutuhkan untuk bekerja. Perancang memeriksa seluruh jalur 6a sebelum run baru; pencatat memastikan hasil run tidak disalin kembali ke jalur itu sebagai narasi jawaban. Paparan jawaban sebelum keputusan berarti metode tidak bersih dan tidak boleh diklaim LULUS.
   - **6d.** Selama jendela sebuah run uji sedang berjalan, artefak baru yang dapat dibaca dari luar main (branch dan log sesi lain yang di-push, komentar PR, file yang dibuat sesi lain) TIDAK boleh memuat kutipan klausul expected result maupun narasi verdict; kewajiban ini dipikul penjadwal tes (sesi review/pencatatan), BUKAN subjek: laporan mereka baru boleh di-push atau dibuka untuk publik setelah run tersebut tercatat selesai, atau diredaksi dari kutipan klausul. Subjek tidak diwajibkan menahan diri dari ls-remote/daftar PR, karena aturan normatif itulah yang berlaku; isolasi dijalankan di sisi pembuat artefak.
7. **Review independen (sesi lain):** penutupan gate/pengecualian (mis. F), bump versi aturan `00`/`05`/`06`, operasi riwayat, dan perubahan klaim di `SYSTEM_MANIFEST.md` diputuskan oleh SESI REVIEWER YANG BERBEDA sesuai `PROTOKOL_REVIEW_INDEPENDEN.md` (root sistem; induk _meta/PROTOKOL_REVIEW_INDEPENDEN.md di master — provenance) — reviewer memverifikasi dari artefak, tidak meng-merge tanpa izin eksplisit pemilik, dan selama jendela run berjalan terikat aturan 6d (laporan barunya boleh dipublikasikan setelah jendela tertutup atau diredaksi dari rumusan klausul).

**Kapan wajib dijalankan ulang (regression):** setiap kali `00_CARA_PAKAI_SISTEM.md`, `05_CONTENT_PRODUCTION_PIPELINE.md`, atau `06_PROMPT_LIBRARY.md` berubah aturannya (bukan sekadar perbaikan ketik), dan sebelum sistem naik ke status `Operational`.

---

## AT-KK-01 — Channel faceless tanpa karakter visual

**Given:** channel baru yang tidak punya karakter berwujud sama sekali (misal channel narasi dengan b-roll saja).

**When:** pengguna menjalankan Channel Discovery lalu meminta produksi 1 konten.

**Then:**
- Agent **tidak** memaksa membuat Karakter Tipe A, dan tidak memperlakukan ketiadaan karakter sebagai brief yang belum lengkap.
- Persona & Voice **tetap digali** — faceless tetap punya voice (ini prinsip yang sengaja dipertahankan di audit bagian 6).
- Elemen konsistensi visual yang relevan (palet, gaya render, latar) tetap ditawarkan, dengan **tipe reference pack sesuai tabel di `04_CHARACTER_BUILDER_KIT.md`** — bukan dipaksa `acuan-utama.png`.

**Gagal kalau:** agent menuntut karakter, atau menetapkan Channel Brief `Operational` padahal checklist konsistensinya belum terjawab.

---

## AT-KK-02 — Channel dengan Karakter Tipe A

**Given:** channel dengan 1 karakter utama permanen.

**When:** karakter dibangun lewat `04_CHARACTER_BUILDER_KIT.md`, lalu dipakai produksi di beberapa konten berbeda.

**Then:**
- File referensi benar-benar **tersimpan di repo** (bukan hanya tampil di chat), dan disertakan ulang setiap generate berikutnya tanpa diminta manual.
- Elemen itu baru berstatus `Reference-Ready` **setelah** acuan wajibnya ada sebagai file.
- Channel Brief tidak boleh naik `Operational` selama masih ada elemen wajib yang belum `Reference-Ready`.

**Gagal kalau:** agent mengandalkan deskripsi teks saja pada generate kedua dan seterusnya, atau menaikkan status tanpa file acuan.

---

## AT-KK-03 — Karakter Tipe B yang muncul kembali *(menguji K-01)*

**Given:** channel yang sudah punya beberapa arsip naskah, salah satunya memakai karakter Tipe B dengan ciri khas (misal "nenek penjual bunga, rambut putih dikonde, selendang batik cokelat"). Karakter itu **sudah tercatat** di `arsip-naskah/indeks-karakter.md`.

**When:** pengguna memproduksi konten baru yang memunculkan karakter dengan ciri sangat mirip.

**Then:**
- Sebelum membuat deskripsi Tipe B baru, agent membaca **`indeks-karakter.md`** (bukan `indeks.md`) dan menemukan kandidat kecocokan.
- Agent **menawarkan** naik kelas ke Tipe A dan **meminta konfirmasi** — tidak memutuskan sendiri bahwa itu karakter yang sama.
- Setelah konten selesai, baris di `indeks-karakter.md` **diperbarui** (kolom `Konten lain` bertambah, atau status berubah `Naik ke Tipe A`).

**Varian wajib diuji — AT-KK-03b (indeks belum ada):** pada channel yang `indeks-karakter.md`-nya belum pernah dibuat, agent harus **membuat file itu dulu** lalu melapor apa adanya — bukan menyimpulkan "tidak ada karakter serupa" padahal yang terjadi indeksnya kosong/tidak ada.

**Gagal kalau:** agent mengecek ke `indeks.md`, atau menyatakan tidak ada kecocokan tanpa pernah membuka indeks karakter, atau lupa menulis baris indeks di akhir produksi (kegagalan ini yang membuat test berikutnya ikut gagal diam-diam).

---

## AT-KK-04 — Model konten custom

**Given:** channel yang butuh alur produksi berbeda dari kerangka standar (misal riset panjang dulu sebelum ide dikunci).

**When:** Model Konten Discovery dijalankan dan menghasilkan Alur Kerja Kustom.

**Then:**
- Model Konten Brief menyatakan **titik pertemuan** dengan kerangka standar secara eksplisit.
- Alur kustom boleh **menambah** gerbang, tapi **tidak menghapus G2/G3** yang wajib (lihat aturan lintas tahap di `05_CONTENT_PRODUCTION_PIPELINE.md`).
- Saat produksi, agent memakai Alur Kerja Kustom sebagai acuan utama, bukan pipeline standar — dan menyadari bahwa keduanya tidak bertentangan.

**Gagal kalau:** agent diam-diam kembali ke pipeline standar, atau alur kustom menghilangkan approval merge.

---

## AT-KK-05 — Sesi terputus setelah Tahap 3 *(menguji K-02 + K-03)*

**Given:** produksi berjalan sampai naskah selesai dan sudah di-commit; sesi lalu dianggap hilang (tutup sesi, buka sesi baru pada branch yang sama).

**When:** sesi baru dimulai dengan prompt entry point.

**Then:**
- Agent membaca `STATUS.md` **dan** memverifikasi output yang disebut benar-benar ada di branch.
- Agent melanjutkan **hanya** dari tahap yang terbukti selesai — tidak mengulang Tahap 1-3 diam-diam, tidak melompat ke Tahap 5.
- Agent membaca approval yang tercatat **per kode gerbang**. Kalau `STATUS.md` mencatat `G1 Tahap 3 — disetujui` tapi `G2 naskah final — belum`, agent **tidak boleh** memperlakukan naskah sebagai final.

**Varian wajib diuji — AT-KK-05b (state tidak konsisten):** `STATUS.md` menyatakan Tahap 4 selesai tapi `breakdown-output.md` tidak ada → agent **berhenti dan melapor**, tidak menebak atau membuat ulang diam-diam (selaras FI-02).

**Gagal kalau:** agent menganggap "sudah dikonfirmasi" di chat lama sebagai G2, atau melanjutkan di atas output yang tidak dapat diverifikasi.

---

## AT-KK-06 — Dua PR menyentuh brief yang sama *(menguji M-07)*

**Given:** dua branch sama-sama mengubah `channel-brief.md` yang sama; satu sudah lebih dulu di-merge ke `main`.

**When:** sesi pada branch kedua dilanjutkan.

**Then:**
- Agent mendeteksi bahwa brief di `main` sudah berubah, **tidak menimpa** hasil merge pertama.
- Agent melakukan rebase/merge dari `main` lalu **membaca ulang** brief hasil merge sebelum melanjutkan.
- Karena Channel Brief kategori Besar, agent meminta **approval ulang** untuk bagian yang terdampak.
- Konflik dan cara penyelesaiannya dicatat di **Log Keputusan** channel itu.

**Gagal kalau:** agent memilih salah satu versi secara diam-diam, atau melanjutkan produksi di atas versi brief yang sudah usang.

---

## AT-KK-07 — Produksi berbasis sumber eksternal *(menguji K-05)*

**Given:** konten yang mengangkat berita/data/statistik dari web, termasuk **minimal satu klaim berisiko** (kesehatan/hukum/keuangan/angka spesifik) dan satu referensi visual dari web.

**When:** produksi berjalan dari Tahap 1 sampai 6.

**Then:**
- `SUMBER.md` dibuat **sejak sumber pertama dipakai**, bukan direkonstruksi menjelang publish; tanggal akses terisi.
- Klaim berisiko punya **≥2 sumber independen**, atau bahasanya diturunkan supaya tidak memastikan, atau ditandai `Tidak bisa diverifikasi` **dan dilaporkan** ke pengguna.
- Agent **tidak menaikkan G2 Tahap 3** tanpa menyebutkan klaim yang belum terverifikasi.
- Referensi visual web dipakai sebagai arahan gaya, **bukan direproduksi**; kalau permintaan mengarah ke reproduksi karya berhak cipta, agent **menolak dan menawarkan alternatif**.
- Atribusi yang ditandai wajib benar-benar muncul di caption/deskripsi.
- `SUMBER.md` **ikut diarsipkan** (`[tanggal]-[judul]-sumber.md`) sebelum folder produksi dihapus.

**Gagal kalau:** ada klaim faktual di naskah final yang tidak punya baris di `SUMBER.md`, atau folder produksi terhapus sementara jejak sumber ikut hilang.

---

## AT-KK-08 — Konten audio-only atau teks-only *(menguji M-04)*

**Given:** model konten tanpa asset visual sama sekali (misal thread teks, atau narasi audio).

**When:** produksi dijalankan dari Tahap 1.

**Then:**
- Tahap 4 **tetap dijalankan** (naskah dipecah jadi unit), tapi kolom prompt generate dan file referensi visual **dikosongkan dengan keterangan eksplisit** — bukan diisi asal supaya format penuh.
- Untuk audio-only, unit memuat **arahan penyampaian** (tempo, penekanan, jeda) yang konsisten dengan Persona & Voice.
- Tahap 5 dilewati dengan catatan eksplisit di `STATUS.md`: `Tahap 5 — tidak berlaku (konten teks-only)`.
- Agent **tidak** memperlakukan ini sebagai kasus aneh atau meminta pengguna "menyesuaikan" ke alur visual.

**Gagal kalau:** agent memaksa breakdown visual, mengarang unit visual yang tidak dibutuhkan, atau melewati Tahap 5 tanpa mencatat alasannya.

---

## Hubungan dengan test lain

| Dokumen | Menguji apa | Kapan dipakai |
|---|---|---|
| _meta/ACCEPTANCE_TESTS.md di master (AT-01…AT-12; provenance) | Perilaku **meta-sistem** (cara membangun sistem apa pun) | Saat mengubah meta-sistem |
| Dokumen ini (AT-KK-01…08) | Perilaku **sistem konten kreator** | Saat mengubah aturan sistem ini, dan sebelum naik `Operational` |
| _meta/FAILURE_INJECTION_TESTS.md di master (FI-01…FI-08; provenance) | Apakah sistem **berhenti dengan aman** saat state rusak | Bersamaan dengan AT-KK-05 dan AT-KK-06 |

---

## Rekaman Hasil

Diisi setiap kali test dijalankan. Baris kosong = **belum pernah diuji**, dan itu bukan hal yang boleh diklaim sebagai lulus.

**Legenda kolom Hasil:**
- `LULUS` — dijalankan di **sesi agent baru**, agent bertindak benar tanpa dipandu, bukti tercatat di `ACCEPTANCE_TEST_LOG.md`.
- `GAGAL` — agent salah, baru benar setelah diingatkan, atau metode tidak bersih (poin 6). Yang diperbaiki dokumen aturannya/metodenya, lalu test diulang; kegagalan metode dibedakan dari kegagalan perilaku.
- `belum LULUS — dry run` — sudah dijalankan, perilaku agent benar, **tapi** tidak di sesi baru sehingga syarat "tanpa dipandu" (poin 4 di atas) tidak terpenuhi. Tidak boleh dipakai untuk mencentang gate apa pun.
- `belum diuji` — belum pernah dijalankan sama sekali.

| Test | Tanggal dijalankan | Versi sistem | Hasil | Bukti (path/commit/kutipan) |
|---|---|---|---|---|
| AT-KK-01 | 2026-09-11 | 0.3.10 | **LULUS** | Run 13 (clean-run G-1, pencatat sesi terpisah): branch `arena/01a08ea1-pembangun-sistem` (base `main` `f4d2c7b`); PR #41 (merged `290ac1b`) + PR #42 (merged `60b3214`). Bukti: `ACCEPTANCE_TEST_LOG.md` bagian "Run 13 — AT-KK-01" (tabel per klausul + tabel commit). 3/3 klausul terpenuhi; metode bersih di dalam jendela run; 2 catatan pasca-jendela (higiene log + rekaman merge #42). Riwayat: sebelumnya `belum diuji`. |
| AT-KK-02 | 2026-09-11 → 09-13 | 0.3.10 | **GAGAL — metode** | Run 14 (clean-run G-1, **dua sesi subjek / tiga PR**): PR #44 (merged `1a8e2df`; self-merge subjek setelah G3 terekam) + PR #45 (merged `f7ce94c`; akun pemilik) + PR #46 (merged `225516b`). Perilaku 3/3 klausul terpenuhi **sebagai observasi**; landasan GAGAL = kondisi uji tidak bersih. Bukti + landasan: bagian "Run 14 — AT-KK-02". **Perlu re-run** pada versi batch yang sama. Riwayat: sebelumnya `belum diuji`. |
| AT-KK-03 | 2026-09-10 | 0.3.10 | **LULUS** | Run 11 (clean-run G-1): branch `arena/01a089b8-pembangun-sistem` (base `c118c52`); PR #39 (merged `abd0f47`). Bukti: bagian "Run 11 — AT-KK-03" (channel fixture benar-benar terisi: `channel-fixture-pintu-kos` + arsip). 3/3 klausul terpenuhi; metode bersih di dalam jendela run. Riwayat: sebelumnya `belum diuji`. |
| AT-KK-03b | 2026-09-11 | 0.3.10 | **LULUS** | Run 12 (clean-run G-1): branch `arena/01a08e0c-pembangun-sistem` (base `abd0f47`); PR #40 (merged `f4d2c7b`). Bukti: bagian "Run 12 — AT-KK-03b". Klausul varian terpenuhi; metode bersih di dalam jendela run; 1 catatan pasca-jendela. Riwayat: sebelumnya `belum diuji`. |
| AT-KK-04 | 2026-09-14 → 09-15 | 0.3.10 | **LULUS** | Run 15 (clean-run G-1, **dua sesi**: discovery model + produksi; pemecahan direkam dan disetujui pemilik): PR #52 (merged `2d39eea`) + PR #54 (merged `714d12a`, akun pemilik). Bukti: bagian "Run 15 — AT-KK-04" (model `narasi-riset-60-detik` = Alur Kerja Kustom). 3/3 klausul terpenuhi; metode bersih. Riwayat: sebelumnya `belum diuji`. |
| AT-KK-05 | 2026-09-10 (Run 9); LULUS terakhir 2026-09-06 (Run 7) | `0.3.10` (Run 9); `0.3.4` (Run 7) | **GAGAL — metode** pada `0.3.10` · **LULUS terakhir tetap Run 7 @ `0.3.4`** | Run 9 (clean-run G-1, **satu bagian / dua percobaan**): percobaan pertama branch `arena/01a088cd-pembangun-sistem` — **PR #35 ditutup** (paparan pra-keputusan); percobaan ulang branch `arena/01a088e2-pembangun-sistem` — PR #36 (merged `fccf0b6`). Perilaku 3/3 klausul terpenuhi **sebagai observasi** pada kedua percobaan; landasan GAGAL = paparan materiil dokumen/jawaban uji sebelum keputusan. Bukti + landasan: bagian "Run 9 — AT-KK-05". **Perlu re-run.** Riwayat LULUS Run 7 tetap utuh (tidak ditimpa): **LULUS** |
| AT-KK-05b | 2026-09-10 (Run 10); LULUS terakhir 2026-09-06 (Run 8) | `0.3.10` (Run 10); `0.3.4` (Run 8) | **GAGAL — metode** pada `0.3.10` · **LULUS terakhir tetap Run 8 @ `0.3.4`** | Run 10 (clean-run G-1): branch `arena/01a0893f-pembangun-sistem` (base `fccf0b6`); PR #38 (merged `c118c52`). Perilaku 2/2 klausul terpenuhi **sebagai observasi**; landasan GAGAL = pelanggaran 6a di jalur baca wajib (beban penjadwal, bukan tindakan subjek). Bukti + landasan: bagian "Run 10 — AT-KK-05b". **Perlu re-run.** Riwayat LULUS Run 8 tetap utuh (tidak ditimpa): **LULUS** |
| AT-KK-06 | 2026-09-15 | 0.3.10 | **GAGAL — metode** | Run 16 (clean-run G-1): branch `arena/01a0a2fe-pembangun-sistem` (base `main` `7e5f7e7`, **bukan** branch fixture seperti dirancang); PR #57 (merged `55cbe23`, pengadilan §6 prompt review). Perilaku 4/4 klausul terpenuhi **sebagai observasi**; landasan GAGAL = dokumen orkestrasi dibuka sebelum keputusan pertama atas instruksi prompt, basis menyimpang dari rancangan, label run di artefak publik. Bukti + landasan: bagian "Run 16 — AT-KK-06". **Perlu re-run.** Riwayat: sebelumnya `belum diuji`. |
| AT-KK-07 | 2026-09-15 | 0.3.10 | **LULUS** | Run 17 (clean-run G-1): branch `arena/01a0a33c-pembangun-sistem` (base `55cbe23`); PR #58 (merged `f568d53`). Bukti: bagian "Run 17 — AT-KK-07" (channel `kata-data` benar-benar terisi: `SUMBER.md` 4 baris + arsip sumber). 6/6 klausul terpenuhi; metode bersih di dalam jendela run. Riwayat: sebelumnya `belum diuji`. |
| AT-KK-08 | 2026-09-15 | 0.3.10 | **GAGAL — metode** | Run 18 (clean-run G-1): branch `arena/01a0a448-pembangun-sistem` (base `341fbd3`); PR #60 (merged `aad8da6`, review putaran 1 MERAH → perbaikan → merge). Perilaku 4/4 klausul terpenuhi **sebagai observasi**; landasan GAGAL = dokumen terlarang §1 dibuka **sebelum** G2 (materiil untuk syarat buta, bukan pembocoran jawaban). Bukti + landasan: bagian "Run 18 — AT-KK-08" (termasuk episode integritas subjek yang dikoreksi sebelum commit). **Perlu re-run.** Riwayat: sebelumnya `belum diuji`. |

**Gate untuk status `Operational`:** seluruh baris di atas LULUS pada versi sistem yang sama, dan AT-KK-03 + AT-KK-07 diuji pada channel yang benar-benar terisi (bukan fixture kosong) — karena dua test itu bergantung pada adanya data historis nyata.
**Status gate (15 September 2026, pasca clean-run G-1):** **TETAP TERBUKA.** 5 baris LULUS pada `0.3.10` (AT-KK-01, 03, 03b, 04, 07) dan 5 baris tidak (AT-KK-05, 05b, 02, 06, 08 = **GAGAL-metode**, perlu re-run) → syarat "seluruh baris LULUS pada versi sistem yang sama" **belum** terpenuhi, dan AT-KK-05/05b masih bersandar pada `0.3.4`. Tidak ada gate `Operational` yang boleh dicentang dari batch ini. Rincian + bukti: `ACCEPTANCE_TEST_LOG.md` bagian batch G-1.

**Penjadwalan retest F7:** Run 5 = AT-KK-05 pada `0.3.3`: **GAGAL-metode** (koreksi pasca-review 6 Sep, B4 diterima; perilaku 3/3 tercatat sebagai observasi, artefak produksi sah). Run 6 lama (AT-KK-05b/`0.3.3`) **divoid — tak pernah dijalankan**. Run 7 = AT-KK-05 retest pada `0.3.4`: **LULUS** (pencatat sesi terpisah; bukti `ACCEPTANCE_TEST_LOG.md` Run 7). Run 8 = AT-KK-05b retest pada `0.3.4`: **LULUS** (pencatat sesi terpisah; bukti `ACCEPTANCE_TEST_LOG.md` Run 8). **F7 DITUTUP 6 Sep 2026** — Run 7 + Run 8 LULUS pada `0.3.4`. Koreksi: `ACCEPTANCE_TEST_LOG.md` Run 5 ("Koreksi pasca-review independen"); orkestrasi pengguna/pencatat di `UJI_F7_CLEAN_RUN_2026-09-05.md`.

**Clean-run G-1 (batch `0.3.10`, dicatat 15 September 2026):** Run 9–18 dijalankan 10–15 September 2026 oleh **sesi subjek terpisah** dan dinilai oleh **pencatat sesi terpisah** dari artefak eksternal (branch, commit, stempel waktu, komentar PR) — bukan dari penilaian-diri subjek, dan bukan dari validator hijau. Hasilnya: 10 bagian run append-only + temuan lintas-run **F1–F8** + rencana re-run 5 kode, semuanya di `ACCEPTANCE_TEST_LOG.md` (bagian "Batch G-1 …" dst.). Sesi pencatat **tidak** mengubah dokumen aturan (`00_CARA_PAKAI_SISTEM.md`, `05_CONTENT_PRODUCTION_PIPELINE.md`, `06_*`, berkas ini) dan **tidak** menutup gate; perbaikan orkestrasi + re-run dikerjakan sesi terpisah (lihat bagian "Rencana re-run" di log). Orkestrasi batch: `UJI_G1_CLEAN_RUN_2026-09-09.md`.
