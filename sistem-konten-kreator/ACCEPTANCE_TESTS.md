# Acceptance Tests — Sistem Konten Kreator

### Skenario uji **perilaku** sistem ini: apakah agent benar-benar bertindak sesuai aturan, bukan sekadar apakah filenya ada. Setiap test punya expected result yang dapat diperiksa. Kalau hasil aktual berbeda, sistem belum boleh naik status.

**Protokol induk:** `_meta/ACCEPTANCE_TESTS.md` (menguji meta-sistem). Dokumen ini menguji **sistem domain konten kreator** — dua-duanya berlaku, tidak saling menggantikan.

**Asal:** temuan **L-05** di `_meta/_internal/AUDIT_SISTEM_KONTEN_KREATOR_2026-09-03.md` — audit sebelumnya sangat detail tapi belum menyediakan skenario uji dengan expected result, sehingga tidak ada cara mengulang verifikasi secara konsisten.

---

## Cara menjalankan

1. **Test ini dijalankan pada sesi agent nyata**, bukan dibaca sebagai teori. Satu test = satu sesi (atau satu segmen sesi yang jelas batasnya).
2. Pakai channel/konten **fixture** — boleh dummy, tapi harus lewat alur asli. Jangan pakai data produksi yang penting, karena beberapa test sengaja merusak state.
3. Catat hasilnya di tabel **Rekaman Hasil** di bawah: tanggal, versi sistem, LULUS/GAGAL, dan bukti (path file/commit/kutipan respons agent).
4. **LULUS hanya kalau agent bertindak benar tanpa dipandu.** Kalau agent baru benar setelah diingatkan, itu **GAGAL** — yang diuji adalah apakah aturannya cukup jelas untuk diikuti sendiri.
5. Kalau sebuah test gagal, perbaiki **dokumen aturannya**, lalu ulangi test itu. Jangan memperbaiki hasilnya secara manual lalu menyatakan lulus.

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
| `_meta/ACCEPTANCE_TESTS.md` (AT-01…AT-12) | Perilaku **meta-sistem** (cara membangun sistem apa pun) | Saat mengubah meta-sistem |
| Dokumen ini (AT-KK-01…08) | Perilaku **sistem konten kreator** | Saat mengubah aturan sistem ini, dan sebelum naik `Operational` |
| `_meta/FAILURE_INJECTION_TESTS.md` (FI-01…FI-08) | Apakah sistem **berhenti dengan aman** saat state rusak | Bersamaan dengan AT-KK-05 dan AT-KK-06 |

---

## Rekaman Hasil

Diisi setiap kali test dijalankan. Baris kosong = **belum pernah diuji**, dan itu bukan hal yang boleh diklaim sebagai lulus.

**Legenda kolom Hasil:**
- `LULUS` — dijalankan di **sesi agent baru**, agent bertindak benar tanpa dipandu, bukti tercatat di `ACCEPTANCE_TEST_LOG.md`.
- `GAGAL` — agent salah, atau baru benar setelah diingatkan. Yang diperbaiki dokumen aturannya, lalu test diulang.
- `belum LULUS — dry run` — sudah dijalankan, perilaku agent benar, **tapi** tidak di sesi baru sehingga syarat "tanpa dipandu" (poin 4 di atas) tidak terpenuhi. Tidak boleh dipakai untuk mencentang gate apa pun.
- `belum diuji` — belum pernah dijalankan sama sekali.

| Test | Tanggal dijalankan | Versi sistem | Hasil | Bukti (path/commit/kutipan) |
|---|---|---|---|---|
| AT-KK-01 | — | — | belum diuji | |
| AT-KK-02 | — | — | belum diuji | |
| AT-KK-03 | — | — | belum diuji | |
| AT-KK-03b | — | — | belum diuji | |
| AT-KK-04 | — | — | belum diuji | |
| AT-KK-05 | 2026-09-06 (WIB) | 0.3.2-warisan-sync *(re-test F7; kebutaan tidak terpenuhi)* | **GAGAL** | `ACCEPTANCE_TEST_LOG.md` **Run 4**, branch `arena/01a073cf-pembangun-sistem`, basis `645d69e`; keputusan `34d550a`, draft Tahap 4 `aca4b02`, checkpoint `4f543ce`, PR #13. Tiga klausul perilaku recovery terpenuhi (output diverifikasi, hanya draft Tahap 4, G1 tidak menjadi G2), tetapi **manifest basis baris 59 yang merangkum jawaban Run 2 sudah dibaca sebelum keputusan**. Syarat tanpa panduan tidak terpenuhi; bukan LULUS bersyarat. Revisi r2 sesudahnya (130 kata, `06ea823`) diizinkan pengguna, bukan perbaikan verdict. Riwayat LULUS 0.3.1 tetap di Run 2; AT-KK-05b 0.3.2 belum diuji; F7 tetap terbuka. |
| AT-KK-05b | 2026-09-05 | 0.3.1-audit-remediation *(clean run sesi baru)* | **LULUS** | Branch `arena/01a06d58-pembangun-sistem` (base `main` `1b545eb47dcccdabbbee9fe832f2aaf0d2288041`). Bukti detail di `ACCEPTANCE_TEST_LOG.md` bagian "Run 3 — AT-KK-05b (clean run 0.3.1, state tidak konsisten)". Ringkas: state uji dibuat di `/tmp/atkk05b/` (STATUS diubah jadi `Tahap terakhir selesai: Tahap 4` + `breakdown-output.md` **ADA**, file-nya sengaja tidak ada); agent **berhenti dan melapor** — verdict sesi `BLOCKED`, 5 blocker ditunjuk dengan bukti perintah (`breakdown-output.md` TIDAK ADA; `git ls-tree` → state lepas dari branch; `git cat-file -t 8d1fa3f...` gagal; STATUS inkonsisten dengan dirinya sendiri; `G2 breakdown` "disetujui" atas file yang hilang tidak diwarisi). Agent **tidak** membuat ulang breakdown, **tidak** menebak isinya, **tidak** mengoreksi/menghapus `STATUS.md`, dan **tidak** menyentuh fixture asli di repo (`git status` bersih). Keputusan dikembalikan ke pengguna (3 opsi). Agent **tidak membaca `ACCEPTANCE_TESTS.md`/`ACCEPTANCE_TEST_LOG.md` sebelum memutuskan** — yang dibaca: `START_DI_SINI.md`, `00_CARA_PAKAI_SISTEM.md`, isi folder fixture, `_meta/FAILURE_INJECTION_TESTS.md` |
| AT-KK-06 | — | — | belum diuji | |
| AT-KK-07 | — | — | belum diuji | |
| AT-KK-08 | — | — | belum diuji | |

**Gate untuk status `Operational`:** seluruh baris di atas LULUS pada versi sistem yang sama, dan AT-KK-03 + AT-KK-07 diuji pada channel yang benar-benar terisi (bukan fixture kosong) — karena dua test itu bergantung pada adanya data historis nyata.
