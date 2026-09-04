# Temuan Repo — Branch Menggantung Tanpa PR (4 September 2026)

**Dibuat:** sesi `arena/01a06d7b-pembangun-sistem`, sebagai bagian entry point tingkat repo (cek "PR menggantung" di `_meta/00_CARA_KERJA_META.md`).
**Status:** temuan, **belum** ditindaklanjuti — menunggu keputusan pengguna. Tidak ada file yang dihapus atau dipindahkan.

---

## Ringkasan

- **PR terbuka: TIDAK ADA.** `gh pr list --state open` → `[]`; `gh pr status` → "You have no open pull requests". Seluruh 8 PR yang pernah ada berstatus MERGED. Issue terbuka: 0.
- **TAPI ada 11 branch `arena/*` di server**, dan **2 di antaranya tidak pernah punya PR**. Kedua branch itu memegang **4 file yang tidak ada di `main`**.
- Isi ke-4 file itu adalah artefak mentah **pilot-002 tanggal 3 September 2026**, yang **sudah digantikan** oleh `pilot-002-behavioral` (4 Sep) di `main`. **Kesimpulannya sudah terbawa ke `main`** — kolom "Hasil 3 Sep" di tabel `_meta/_internal/BEHAVIORAL_AUDIT_2026-09-04_PILOT_002.md` baris 40-48 adalah ringkasan dari run 3 Sep itu. Jadi yang tertinggal adalah **bukti mentahnya**, bukan kesimpulannya.

## Kenapa sebelumnya tidak kelihatan

Clone yang dipakai sesi ini punya refspec terbatas:

```
$ git config --get-all remote.origin.fetch
+refs/heads/main:refs/remotes/origin/main
```

Karena itu `git branch -r` hanya menampilkan `origin/main`, dan branch `arena/*` di server tidak terlihat. Pemeriksaan harus pakai `git ls-remote --heads origin`, bukan `git branch -r`.

**Pelajaran untuk entry point berikutnya:** cek branch menggantung dengan `git ls-remote --heads origin`, dan kalau clone dangkal (`git rev-parse --is-shallow-repository` → `true`), jalankan `git fetch --unshallow` dulu — kalau tidak, hitungan "commit di luar main" salah (sempat terbaca 17/16/13 commit padahal sebenarnya artefak kedangkalan).

## Data

### Perbandingan ujung `main` vs ujung tiap branch (`git diff --stat origin/main..<branch>`)

| Branch | PR | File yang tidak ada di `main` | Keterangan |
|---|---|---|---|
| `arena/01a0668e` | #1 merged | **tidak ada** | isinya sudah semua di `main` |
| `arena/01a0685f` | #2 merged | **tidak ada** | isinya sudah semua di `main` |
| `arena/01a06bce` | #3 merged | — | identik/lebih tua dari `main` |
| `arena/01a06c5d` | #4 merged | — | lebih tua dari `main` |
| `arena/01a06cee` | #5 merged | — | lebih tua dari `main` |
| `arena/01a06d25` | #6 merged | — | lebih tua dari `main` |
| `arena/01a06d58` | #7 merged | — | lebih tua dari `main` |
| `arena/01a06d65` | #8 merged | **tidak ada** | `git diff` → IDENTIK dengan `main` |
| `arena/01a0679e` | **tidak ada** | **4 file** | run pilot-002 3 Sep (OUTPUT.md 87 baris) |
| `arena/01a067e8` | **tidak ada** | **4 file yang sama** | run pilot-002 3 Sep, lebih lanjut (OUTPUT.md 311 baris) — ini yang paling lengkap |
| `arena/01a06d7b` | sesi ini | — | branch aktif sesi ini |

### Ke-4 file yang tidak ada di `main`

```
_meta/_internal/SESSION_REPORT_2026-09-03_BOOTSTRAP_S02.md
sistem-pilot-catatan-belajar/fixtures/SUMBER_CHECKPOINT_RECOVERY.md
sistem-pilot-catatan-belajar/unit-aktif/pilot-002/OUTPUT.md
sistem-pilot-catatan-belajar/unit-aktif/pilot-002/STATUS.md
```

Diperiksa dengan `comm -23 <(git ls-tree -r --name-only <branch> | sort) <(git ls-tree -r --name-only origin/main | sort)`.

Catatan: di `main`, folder `unit-aktif/pilot-002/` sudah **diganti nama** jadi `unit-aktif/pilot-002-behavioral/` dan fixture `SUMBER_CHECKPOINT_RECOVERY.md` diganti `SUMBER_NYATA_PILOT_002.md`. `git grep SUMBER_CHECKPOINT_RECOVERY origin/main` → tidak ada hasil.

## Verifikasi bahwa kesimpulannya tidak hilang

`_meta/_internal/BEHAVIORAL_AUDIT_2026-09-04_PILOT_002.md` di `main` punya tabel dengan dua kolom hasil:

| Skenario | Hasil 3 Sep | Hasil 4 Sep (pilot-002) |
|---|---|---|
| Sesi terputus | Lulus desain | **LULUS NYATA** — FI-01 s/d FI-04 fail-closed |
| Self-improvement | Lulus struktural | Lulus behavioral |

Kolom "Hasil 3 Sep" itulah ringkasan run yang artefak mentahnya tertinggal di dua branch tanpa PR. Jadi run 3 Sep **tidak dilupakan**, melainkan **digantikan** oleh run 4 Sep yang lebih kuat (nyata, bukan sekadar lulus desain).

## Pilihan tindak lanjut (keputusan pengguna)

1. **Biarkan apa adanya** — tidak merusak apa pun, tapi branch tanpa PR tetap membingungkan sesi berikutnya.
2. **Selamatkan 4 file itu** ke `_meta/_internal/arsip-pilot-002-2026-09-03/` sebagai bukti mentah sejarah, lalu hapus 2 branch tanpa PR.
3. **Hapus 2 branch tanpa PR** tanpa menyelamatkan file, dengan alasan: kesimpulannya sudah ada di audit 4 Sep, artefak mentahnya superseded.
4. **Hapus semua branch `arena/*` lama yang PR-nya sudah merged** (housekeeping terpisah) — aman karena isinya sudah di `main`, tapi tetap keputusan pengguna.

Yang **tidak** dilakukan tanpa keputusan eksplisit: menghapus branch apa pun, atau memindahkan file ke `main`.
