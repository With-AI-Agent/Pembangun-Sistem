# Housekeeping Meta — 16 September 2026 (run klinik ke-2 Building Aplikasi, PR #63)

**Dibuat oleh:** sesi `arena/01a0a7d3-pembangun-sistem`, Tahap F (panen) + mandat pemilik
"Selesaikan dan bereskan dan sempurnakan dulu semuanya".
**Status:** sebagian **sudah dikerjakan** (arsip artefak root), sebagian **temuan yang butuh
keputusan pemilik per-item** (cabang remote + log sesi milik sesi lain) — tidak ada yang dihapus
atau ditulis ulang diam-diam.

Prinsip yang dipakai: **pensiunkan, jangan hapus** (Kebijakan Lebur Aturan 2 butir baru) dan
**izin per-item untuk tindakan destruktif** (Aturan 2) — termasuk untuk cabang remote dan log
milik sesi lain, walau pemilik sudah memberi mandat umum "bereskan semuanya".

---

## 1. SUDAH dikerjakan: 5 artefak review/audit di root repo

Dipindah ke `_meta/_internal/arsip-review-2026-09-16/` (+ README + banner arsip di 3 berkas
`REVIEW_*`; isi asli utuh). Alasan, bukti md5 duplikat, dan tabel "yang berlaku sekarang" ada di
README folder arsip itu. Root repo kini hanya memuat dua pegangan wajib
(`PANDUAN_PENGGUNA.md`, `PROMPT_ENTRI_UNIVERSAL.md`).

Rujukan yang tadinya menunjuk path root sudah disesuaikan di
`sistem/sistem-building-aplikasi/REKAM-KLINIK.md` (baris housekeeping) — kalau tidak, pemindahan
ini justru menciptakan rujukan menggantung.

**Opsional, butuh izin per-item** (duplikat byte-identik; kanoniknya tetap ada di sistem):

```bash
git rm _meta/_internal/arsip-review-2026-09-16/AUDIT_NPX_UPDATE.md \
       _meta/_internal/arsip-review-2026-09-16/AUDIT_ZIP_VS_NPX.md
```

## 2. TEMUAN: 5 branch `arena/*` di server tidak pernah punya PR

Diperiksa lewat API pembanding server (clone ini dangkal — `git log`/`merge-base` lokal tidak
sah): `gh api repos/With-AI-Agent/Pembangun-Sistem/compare/main...<branch>`.

| Branch | Status | Unik | Isi yang hanya ada di branch itu |
|---|---|---|---|
| `arena/01a0772b-pembangun-sistem` | DIVERGED (ahead 1) | 3 berkas | `LOG_SESI_2026-09-06_review-pr16.md`, `_meta/_internal/review-pr16-2026-09-06/README.md` (+180), `.../reproduce.py` (+254) — **bukti review PR #16 + skrip reproduksi**, tidak pernah masuk `main` |
| `arena/01a0776b-pembangun-sistem` | DIVERGED (ahead 2) | 1 berkas | `LOG_SESI_2026-09-06_5.md` (41 baris) di **root** — di `main` ada `_log-sesi/LOG_SESI_2026-09-06_5.md` (29 baris): versi berbeda, bukan salinan |
| `arena/01a07fc0-pembangun-sistem` | DIVERGED (ahead 1) | 1 berkas | `LOG_SESI_2026-09-08_2.md` (63 baris) di **root** — di `main` ada `_log-sesi/LOG_SESI_2026-09-08_2.md` (238 baris) |
| `arena/01a0a797-pembangun-sistem` | DIVERGED (ahead 1) | 1 berkas | `REVIEW_2026-09-16_INDEPENDEN.md` (+152) — **laporan review independen** yang dirujuk `REVIEW_PROMPT_DELTA_593ba79.md` |
| `arena/01a0a7ad-pembangun-sistem` | DIVERGED (ahead 1) | 1 berkas | `REVIEW_DELTA_593ba79.md` (+51) — laporan delta review (verdict HIJAU) untuk PR #59 |
| `uji-06-branch-b` | **BEHIND** (ahead 0) | 0 | tidak ada konten unik — branch sisa pengujian |

**Kenapa tidak dihapus/ditindak sendiri:** semuanya DIVERGED dan memegang **bukti kerja pihak
lain** (dua di antaranya laporan review independen, satu punya skrip reproduksi 254 baris).
Menghapus branch = menghapus satu-satunya salinan bukti itu; itu tindakan destruktif lintas sesi
yang butuh izin per-item. `uji-06-branch-b` nol kerugian (behind 0), tetapi tetap branch remote —
keputusannya milik pemilik.

**Rekomendasi (urut nilai):**
1. **Selamatkan bukti review dulu, baru rapikan.** Ambil 3 berkas review ke arsip meta:
   ```bash
   for b in arena/01a0a797-pembangun-sistem arena/01a0a7ad-pembangun-sistem arena/01a0772b-pembangun-sistem; do
     git fetch --depth 1 origin "$b" && git checkout FETCH_HEAD -- $(git diff --name-only main FETCH_HEAD | tr '\n' ' ')
   done
   # lalu pindahkan ke _meta/_internal/arsip-review-*/ dan commit lewat PR tersendiri
   ```
2. Bandingkan dua `LOG_SESI_*` root di branch dengan padanannya di `_log-sesi/` → bila isinya
   sudah tercakup, branch boleh dihapus; bila tidak, append selisihnya ke log yang benar.
3. Baru hapus branch (butuh izin per-item):
   ```bash
   git push origin --delete uji-06-branch-b            # nol kerugian (behind 0)
   git push origin --delete arena/01a0a7ad-pembangun-sistem   # dst., SETELAH butir 1 selesai
   ```

## 3. TEMUAN: log sesi ber-status OPEN milik sesi lain

Dipindai dengan field persis `- **Status:** OPEN` di `_log-sesi/*.md`: **satu** berkas,
`_log-sesi/LOG_SESI_2026-09-08_5.md` (PR #25 menunggu review/merge — keadaan yang sudah lewat).
**Tidak disunting**: log milik sesi lain hanya boleh ditutup oleh sesinya sendiri atau dengan
mandat eksplisit per-item; menebak "sudah basi" berisiko menimpa sesi yang benar-benar masih hidup.

Rekomendasi: pemilik membuka berkas itu dan mengganti statusnya jadi
`CLOSED — ditinggalkan/basi (PR #25 sudah lewat)`, atau memberi mandat ke sesi berikutnya untuk
melakukannya per-item.

## 4. Catatan aturan yang dipakai (supaya housekeeping berikutnya tidak mengulang pola ini)

- Artefak sekali-pakai (prompt review, catatan simulasi) **jangan di-commit ke root**: ia basi
  seketika setelah commit (C-07) dan root adalah hal pertama yang dibaca sesi baru. Yang
  otoritatif adalah **alat pembangkitnya** (`tools/review_prompt.py --pr <nomor>`).
- Dokumen duplikat byte-identik = dua sumber kebenaran. Simpan satu kanonik, tunjuk ke sana.
- Branch review yang memegang laporan = bukti yang tidak masuk `main`. Bila laporan review mau
  jadi bukti permanen, ia harus di-commit ke `_meta/_internal/` (atau ditempel ke PR), bukan
  ditinggal di branch yang tak ber-PR.
