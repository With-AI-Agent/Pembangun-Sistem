# RINGKASAN CADANGAN — Sistem Presentasi

> Ringkasan untuk sesi cadangan (Claude chat biasa). Sumber kebenaran tetap repo (branch `arena/01a06d7b-pembangun-sistem` → merge ke `main` 5 Sep 2026). Entry point: `sistem-presentasi/START_DI_SINI.md`.

## Identitas
- **Versi:** `0.2.0` · **Status:** Built & terverifikasi (audit otomatis 5 Sep 2026: `validate_system.py` exit 0; `qa_deck.py` 14 slide exit 0; `install_deps.sh` exit 0).
- **Tujuan:** bahan (dokumen/topik) → berkas presentasi (default `.pptx`) yang setia sumber, berjejak halaman, RTL-bila-Arab, proses lanjut-antar-sesi.
- **Self-contained:** seluruh aturan aktif di `sistem-presentasi/_sistem/01–10`; `_meta` hanya provenance.

## Struktur inti
- `_sistem/01–10` (aturan desain/isi/gambar, knowledge+riset, paham kebutuhan, QA, anti-ngarang, desain berbasis bukti, mode gambar M0–M4 + lisensi, perancangan berbasis rekomendasi, pemahaman bahan via VISI utk Arab, render+verifikasi) + `qa_deck.py` + `validate_system.py` + `install_deps.sh`.
- `_generator/G1–G3`, `_template/T1–T9`, `ACCEPTANCE_TESTS.md`, `START_DI_SINI.md`, `SYSTEM_MANIFEST.md`.
- Alur: Brief → Pahami bahan (G1) → Outline+Rencana Visual (G2) → Produksi → Verifikasi (G3).

## Pelajaran keras (jangan dilanggar)
- **Deck #1 (tesis fikih hiasan wanita) BUKAN sample/contoh** — prosesnya cacat (sesi perancangan isi & visual dilewati; revisi v1–v7). Ambil hanya pelajaran anti-pola di `sistem-presentasi/PELAJARAN_DECK_01.md`; ikuti aturan `_sistem/01–10` + gerbang penuh.
- Arab: ekstraksi PDF teracak → **jalur VISI wajib** untuk kutipan; kompetensi = tata bahasa/idiom, bukan harakat.
- Unduh biner hanya via GitHub; preview/viewer tidak bisa unduh.
- `/tmp` tidak persisten → `install_deps.sh` tiap sesi.

## Bagian yang BELUM selesai (per 5 Sep 2026)
1. Deck aktif: heading السؤال الثاني belum verbatim (rekonstruksi berlabel, menunggu tinjauan pemilik); nama pembimbing kosong; pemilik akan menambah butir → slide susulan.
2. Audit independen manusia belum dilakukan.
3. Q-O2/Q-O3 (celah protokol recovery `_meta`) masih terbuka di level meta.
4. Font Arab + `arabic_reshaper` utk preview PIL/HTML belum diverifikasi.
