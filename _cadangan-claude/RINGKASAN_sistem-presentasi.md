# RINGKASAN CADANGAN — Sistem Presentasi

> Ringkasan untuk sesi cadangan (Claude chat biasa). Sumber kebenaran tetap repo. Entry point: `sistem-presentasi/START_DI_SINI.md`. (Disinkronkan 5 Sep 2026 oleh audit meta — sebelumnya basi di `0.2.0`, temuan M-09.)

## Identitas
- **Versi:** `0.4.1` · **Status:** Built & terverifikasi; **teraudit 1x independen** (5 Sep, 11 temuan AP-01…AP-11 semua diperbaiki di v0.3.0). v0.4.0: turunan `LOG_SESI` (`_sistem/11_LOG_SESI.md`); v0.4.1: field checkpoint `Pekerjaan belum tersimpan` di `T6_STATUS.md` + sinkronisasi kontrak warisan meta v1.3.0 (tabel Warisan di manifest).
- **Tujuan:** bahan (dokumen/topik) → berkas presentasi (default `.pptx`) yang setia sumber, berjejak halaman, RTL-bila-Arab, proses lanjut-antar-sesi.
- **Self-contained:** seluruh aturan aktif di `sistem-presentasi/_sistem/01–11`; rujukan `_meta/` = provenance. Pegangan: `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` (blok identik).

## Struktur inti
- `_sistem/01–11`: aturan desain/isi/gambar · knowledge desain+riset · paham kebutuhan/tujuan · QA produksi · sumber & anti-ngarang · desain berbasis bukti · mode gambar M0–M4 + lisensi · perancangan berbasis rekomendasi · pemahaman bahan mendalam · render & verifikasi · **11_LOG_SESI**. + `qa_deck.py` + `validate_system.py` + `install_deps.sh`.
- `_generator/G1–G3`, `_template/T1–T9` (T6 = STATUS dengan field checkpoint deterministik), `ACCEPTANCE_TESTS.md`, `SYSTEM_MANIFEST.md` (termasuk tabel Warisan W-01…W-09).
- Alur: Brief → Pahami bahan (G1) → Outline+Rencana Visual (G2) → Produksi → Verifikasi (G3). Sesi: prompt pembuka memulihkan `LOG_SESI` `OPEN`; prompt penutup menutupnya.

## Pelajaran keras (jangan dilanggar)
- **Deck #1 (tesis fikih hiasan wanita) BUKAN sample/contoh** — prosesnya cacat (sesi perancangan isi & visual dilewati; revisi v1–v7). Ambil hanya pelajaran anti-pola di `sistem-presentasi/PELAJARAN_DECK_01.md`; ikuti aturan `_sistem/01–11` + gerbang penuh.
- Arab: ekstraksi PDF teracak → **jalur VISI wajib** untuk kutipan; kompetensi = tata bahasa/idiom, bukan harakat.
- Unduh biner hanya via GitHub; preview/viewer tidak bisa unduh.
- `/tmp` tidak persisten → `install_deps.sh` tiap sesi.

## Bagian yang BELUM selesai (per 5 Sep 2026)
1. Acceptance test AT-SP-01…AT-SP-14 belum dieksekusi (hanya AT-SP-15) — debt tercatat di body PR #10.
2. Review Q2 oleh pemilik (heading belum verbatim; rekonstruksi berlabel; pembimbing kosong; pemilik akan menambah butir → slide susulan).
3. Font Arab + `arabic_reshaper` utk preview PIL/HTML belum diverifikasi.
4. ~~Q-O2/Q-O3 celah protokol meta~~ — **DITUTUP 5 Sep di meta v1.3.0**; deck STATUS kini memuat field checkpoint penuh.
