# Template Release — Meta-Sistem

**Tujuan:** Menentukan apa yang termasuk template bersih dan bagaimana memverifikasinya (AT-10)


### C5 — Larangan angka korpus dalam bukti permanen

Di dokumen permanen (terutama Log Evolusi, manifest, dan indeks), angka yang dapat berubah akibat penulisan dokumen itu sendiri **tidak boleh dikutip sebagai angka mutlak**. Jumlah `rujukan` adalah volatile karena setiap entri `LOG_SESI` dapat menambahnya. Angka tersebut dilarang dikutip sama sekali. Verdict dan angka stabil (misalnya jumlah berkas wajib) tetap wajib dicatat. `tools/validate_repo.py` menolak sel **Bukti** Log Evolusi yang menyebut `rujukan` tanpa pin `pada <sha>` (AT-16). Aturan ini lahir dari empat siklus PR #21→#24 yang mengejar angka bukti basi; ini adalah kontrol integritas, bukan gaya penulisan.

## Definisi Template Bersih

Template bersih adalah salinan siap pakai untuk membuat repo baru, yang **tidak** membawa:

- data pribadi
- output produksi (contoh: arsip naskah, unit-aktif, OUTPUT.md produksi)
- audit internal (`_meta/_internal/`)
- keputusan domain contoh (misal isi `sistem-konten-kreator/` yang spesifik ke konten kreator)

Template **wajib** membawa (diselaraskan dengan temuan M-01/M-16 audit 5 Sep 2026):

- SEMUA `_meta/*.md` top-level — daftar ini **tidak lagi manual**: `tools/build_template.py` memakai inventaris inti statis (`checkpoint_core.CORE_META_FILES`) ∪ glob folder, jadi file meta baru otomatis ikut, dan file inti yang DIHAPUS membuat BUILD GAGAL (kewajiban tak diturunkan dari keberadaan — review F1); guard rujukan aktif tetap menyangga
- SEMUA `tools/*.py` (termasuk `checkpoint_core.py`) — tanpa validator/FI/backup/template, repo hasil ekstrak kehilangan regresi struktural dan penegakan kontrak warisan (dulu tidak ikut: cacat M-01 kelas distribusi)
- entry point pengguna (`PANDUAN_PENGGUNA.md`) + prompt entri (`PROMPT_ENTRI_UNIVERSAL.md`)
- indeks sistem dikosongkan (`_meta/INDEKS_SISTEM.md` dengan header + baris kosong)
- manifest meta (`_meta/SYSTEM_MANIFEST.md`) sebagai referensi versi — **diberi banner otomatis** oleh builder bahwa isinya sejarah master, bukan identitas repo baru (M-16)
- `.gitignore`, `.gitattributes`
- folder kosong `_pegangan-kamu/` dan `_cadangan-claude/` dengan `.gitkeep`

## Cara Build

```bash
python3 tools/build_template.py
```

Output:
- `_meta/_internal/template_clean/` — folder template bersih
- `_meta/_internal/template_clean.zip` — zip siap distribusi

## Transformasi self-containment (review PR #11, F5 — 5 Sep 2026)

Dua instruksi AKTIF di dokumen master menunjuk file yang sengaja tidak ikut template; builder menulisi ulang HANYA di salinan template (master tak berubah), dan transformasi **idempotent** (build ulang di repo hasil ekstrak = no-op):

1. `NEXT_SESSION_PROMPT.md` langkah 6 — "Baca `_meta/_internal/HANDOFF_NEXT_SESSION.md`" → "kalau ada, bacanya; di repo baru file ini TIDAK ada, lewati tanpa konflik" (sebelumnya: langkah bootstrap aktif menunjuk file yang tidak ikut — cacat, bukan warning).
2. `PANDUAN_PENGGUNA.md` bagian Istilah Singkat — rujukan ke panduan pengguna sistem konten kreator (path-nya tidak ditulis backtick di sini agar baris ini tidak menjadi warning) → definisi singkat branch/commit/PR/merge inline + penunjuk ke PANDUAN_PENGGUNA.md tiap sistem (W-01).

Jika anchor transformasi tidak ketemu dan teks targetnya pun tidak ada (dokumen berubah) = build GAGAL. Tidak ada template dengan bootstrap basi yang lolos diam-diam.

## Verifikasi

`tools/build_template.py` melakukan verifikasi AT-10:

- tidak ada `_internal` di dalam template
- tidak ada `sistem-konten-kreator/`
- tidak ada `sistem-pilot-`
- tidak ada `arsip-naskah`
- tidak ada `unit-aktif`
- **kelengkapan (M-01):** setiap `_meta/*.md` yang dirujuk dari dokumen aktif `_meta/` HARUS ikut terbawa; sumber INCLUDE yang hilang = build gagal

Jika ada pelanggaran, build gagal.

**Smoke test pasca-build (wajib setiap kali template/validator berubah):** ekstrak zip ke direktori kosong, `git init`, lalu jalankan di sana `python3 tools/validate_repo.py` dan `python3 tools/test_failure_injection.py` — keduanya harus PASS (exit 0) tanpa ada sistem terdaftar; validator di sana harus menghasilkan PERSIS 5 warning normalisasi di bawah, dan FI berjalan 24 skenario. Ini membuktikan template berdiri sendiri (diverifikasi 5 Sep 2026; diperketat pasca review PR #11; lihat `AUDIT_META_SISTEM_2026-09-05.md` Addendum 2; warning ke-5 dipin 6 Sep 2026, meta v1.4.0).

**Yang normal di repo hasil ekstrak — PERSIS 5 warning (daftar normalisasi, dipin di FI skenario R7):** semuanya rujukan historis master yang dilabeli (bukan instruksi aktif); exit code tetap 0. (Format daftar sengaja tanpa backtick pada path-nya: baris ini mendokumentasikan warning, bukan menunjuk dependensi — ia sendiri tidak boleh menjadi warning.)

1. lokasi 00_CARA_KERJA_META.md:111 → target sistem-konten-kreator/_sistem/09_AUDIT_MIGRASI_GITHUB_AGENT.md — konteks "alasan detail" historis
2. lokasi 00_CARA_KERJA_META.md:111 → target sistem-konten-kreator/_sistem/00_CARA_PAKAI_SISTEM.md — konteks pemakaian harian historis
3. lokasi SYSTEM_MANIFEST.md:89 → target sistem-pilot-catatan-belajar/unit-aktif/pilot-002-behavioral/OUTPUT.md — bukti rilis di manifest ber-banner "sejarah master"
4. lokasi SYSTEM_MANIFEST.md:93 → target _sistem/11_LOG_SESI.md — rujukan turunan di sejarah rilis master (relatif sistem presentasi)
5. lokasi SYSTEM_MANIFEST.md (baris Log Evolusi v1.4.0) → target sistem-konten-kreator/ACCEPTANCE_TEST_LOG.md — kolom Bukti v1.4.0: implementasi prompt reviewer terbukti pada Run 7/8 (provenance, bukan instruksi aktif; dipin 6 Sep 2026, meta v1.4.0)

Rujukan ke `_meta/_internal/…` tidak pernah di-warn (area histori; tidak pernah ikut template — tidak bisa menjadi dependensi operasional). **Bootstrap mandiri (F5):** tidak boleh ADA warning di `NEXT_SESSION_PROMPT.md` maupun `PANDUAN_PENGGUNA.md` — jika muncul, artinya instruksi aktif menunjuk file yang tidak ikut. Target "0 warning" tetap hanya berlaku di master blueprint.

## Backup

Backup esensial dilakukan via:

```bash
python3 tools/backup_verify.py
```

Output:
- `_meta/_internal/backups/backup_essential.zip`
- Verifikasi restore ke temp dir dan bandingkan manifest

## Status Rilis

- Template bersih: built dan verified 2026-09-04 via `tools/build_template.py`; **rebuilt & re-verified 2026-09-05** (pasca review PR #11: transformasi self-containment + daftar 4 warning dipin); **re-verified 2026-09-06** (meta v1.4.0: warning normalisasi ke-5 dipin — rujukan provenance Log Evolusi v1.4.0 ke acceptance log KK)
- Backup: created dan verified 2026-09-04 via `tools/backup_verify.py`; **re-verified 2026-09-05** (inventaris inti statis, 30 file)

Kedua artefak disimpan di `_meta/_internal/` (bukan bagian dari template bersih itu sendiri).
