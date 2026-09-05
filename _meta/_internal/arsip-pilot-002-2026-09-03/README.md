# Arsip — pilot-002 (3 September 2026), diselamatkan dari branch tanpa PR

**Diarsipkan:** 4 September 2026, sesi `arena/01a06d7b-pembangun-sistem`.
**Sumber:** branch `arena/01a067e8-pembangun-sistem` (commit `a5efba0`, 3 Sep 17:22) — branch yang **tidak pernah punya PR**. Diambil dengan `git show <branch>:<path>`, byte-per-byte, tanpa diedit.
**Kenapa diarsipkan:** lihat `_meta/_internal/CABANG_MENGGANTUNG_2026-09-04.md`.

---

## Isi folder ini

| File | Asal path di branch | Baris |
|---|---|---|
| `OUTPUT.md` | `sistem-pilot-catatan-belajar/unit-aktif/pilot-002/OUTPUT.md` | 311 |
| `STATUS.md` | `sistem-pilot-catatan-belajar/unit-aktif/pilot-002/STATUS.md` | 42 |
| `SESSION_REPORT_2026-09-03_BOOTSTRAP_S02.md` | `_meta/_internal/SESSION_REPORT_2026-09-03_BOOTSTRAP_S02.md` | 113 |
| `SUMBER_CHECKPOINT_RECOVERY.md` | `sistem-pilot-catatan-belajar/fixtures/SUMBER_CHECKPOINT_RECOVERY.md` | 62 |

**Status folder ini:** arsip sejarah / bukti mentah. **Bukan** dokumen instruksi aktif, **bukan** unit kerja aktif, dan tidak boleh dibaca sebagai status terkini. Run ini **sudah digantikan** oleh `sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral/` (4 Sep 2026) yang hasilnya lebih kuat (nyata, bukan "lulus desain").

---

## Kenapa tetap diselamatkan (bukan dihapus)

Karena run ini meninggalkan **empat hal yang belum pernah masuk `main` dan masih terbuka sampai sekarang.** Diverifikasi 4 Sep 2026 dengan `git grep` terhadap `origin/main`: `K-P3`, `K-P4`, `K-P5`, `Q-O2`, `Q-O3` → **tidak ada satu pun di `main`**.

### 1. Q-O2 — celah protokol, MASIH TERBUKA di `main`

Aturan recovery `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` baris 61 di `main` berbunyi:

> "Jangan mengulang tahap yang sudah berstatus `approved` atau `merged` **tanpa alasan**."

**Kriteria "alasan" yang sah tidak pernah didefinisikan.** Run 3 Sep menandai ini sebagai "celah nyata protokol — jangan beroperasi seolah kriterianya sudah ada". Diverifikasi ulang 4 Sep 2026: baris itu masih berbunyi sama, tanpa kriteria.

### 2. Q-O3 / K-P3 — celah protokol, MASIH TERBUKA di `main`

Template `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` baris 27 di `main` masih berupa field kosong `- Waktu pembaruan:` tanpa aturan interval atau granularitas. K-P3 mengusulkan granularitas lebih halus (tanggal + nama tahap) **lewat jalur proposal**, bukan edit diam-diam. Belum pernah diimplementasikan.

### 3. K-P4 — catatan meta yang belum dijawab

`WORKFLOW.md` pilot belum mendefinisikan mekanisme **verifikasi-ulang pasca-Apply**. Dicatat sebagai usulan ke meta-sistem lewat jalur proposal. Belum pernah dijawab.

### 4. K-P5 — ditangguhkan, tapi menunjuk celah nyata

Lokasi **draft proposal** belum dikontrakkan di repo: pada run 3 Sep, proposal K-P1/K-P2 "disampaikan di chat sesi sebelumnya (tidak ada file draft)". Ini celah yang relevan lintas sistem, karena perubahan aturan inti wajib lewat proposal (pola AT-05) tapi tidak ada tempat baku menaruh draftnya.

---

## Relevansi untuk kerja sekarang

Keempat hal di atas **bukan sampah sejarah**: celah Q-O2 dan Q-O3 ada di protokol yang akan dipakai juga oleh sistem baru (`sistem-presentasi/`), karena sistem itu akan memakai checkpoint berbasis `STATUS.md`. Menutup Q-O2/Q-O3 adalah pekerjaan meta-sistem, bukan pekerjaan sistem domain — jadi dicatat di sini supaya tidak hilang lagi.

## Tambahan 5 Sep 2026 (sesi `arena/01a0727c-pembangun-sistem`)

- **`run-awal-01a0679e/` ditambahkan.** Verifikasi ulang dengan `git ls-tree -r` + SHA-256 menemukan bahwa arsip di atas hanya byte-identik dengan branch `01a067e8` (run lanjut, 311 baris); run awal `01a0679e` punya 3 file berbeda versi (OUTPUT 87 baris, STATUS 36, SUMBER 62 — `SESSION_REPORT` identik). Ketiga file versi awal itu kini diselamatkan byte-per-byte (via `git show tmp/01a0679e:<path>`, tanpa diedit) supaya penghapusan kedua branch yatim (temuan M-18 audit meta 5 Sep, didelegasikan pengguna 5 Sep) bisa **nol kehilangan**.
- **Status 4 celah yang dicatat di atas:** Q-O2 dan Q-O3 **DITUTUP 5 Sep 2026** di `main` (PR #11, temuan F16 + penutupan Q-O2/Q-O3). K-P4 dan K-P5 belum ada keputusan — tetap terbuka, catatan ini tetap berlaku.
- **Nasib kedua branch:** dihapus dari remote **setelah** commit penyelamatan ini ter-merge ke `main` (urutan disepakati: aman dulu, baru hapus).

## Yang sengaja TIDAK dilakukan

- **Branch `arena/01a0679e` dan `arena/01a067e8` tidak dihapus.** Menghapus branch remote tidak bisa dibatalkan, dan tidak perlu buru-buru: setelah arsip ini masuk, branch itu redundan, jadi menghapusnya kapan pun nanti tidak menghilangkan apa pun. Keputusan dipegang pengguna.
- Isi file **tidak diedit, tidak dirapikan, tidak "diperbaiki"** — arsip harus tetap sama persis dengan aslinya supaya bisa dipakai sebagai bukti.
