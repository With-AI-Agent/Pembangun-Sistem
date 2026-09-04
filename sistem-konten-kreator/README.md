# Konten_Projects — Sistem Konten Kreator (Feat lmarena)

Repo ini berisi sistem lengkap untuk membangun dan memproduksi konten kreator dengan bantuan AI agent (lmarena Agent). Semua dokumen sistem hidup di folder `_sistem/`. File panduan pengguna hidup di `panduan/`.

## Struktur Cepat

- `SYSTEM_MANIFEST.md` — kartu identitas, dependency, risiko, dan gate rilis
- `_sistem/` — dokumen instruksi sistem (00–08, START_DI_SINI, status template, dan audit historis)
- `panduan/` — PANDUAN_PENGGUNA.md (panduan praktis + prompt universal)
- `channel-[nama]/` — akan dibuat saat ada channel baru
- `konsistensi-visual/` / `konsistensi-lintas-channel/` — bank konsistensi visual
- `_produksi-aktif/` — produksi sementara (dihapus setelah konten selesai)

## Cara Memulai (Universal)

1. Pastikan agent terhubung ke repo ini.
2. Gunakan prompt universal di `panduan/PANDUAN_PENGGUNA.md` (bagian "Prompt Pembuka Universal").
3. Agent membaca konteks wajib untuk jenis sesi itu (tabel "Konteks Wajib per Jenis Sesi" di `_sistem/00_CARA_PAKAI_SISTEM.md`), cek branch dan PR menggantung, lalu tanya tujuan sesi.

Untuk panduan lengkap, baca `panduan/PANDUAN_PENGGUNA.md`.
