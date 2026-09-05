# 10 — Render `.pptx` & Verifikasi (3 jalur, larangan klaim kosong)

## Build (reproducible)
- `python-pptx` (+Pillow/lxml) tidak default; install `--target` lalu `PYTHONPATH`. `/tmp` tidak persisten → hasil ke `keluaran/` di repo.
- RTL Arab: `rtl=1`, `algn=right`, font complex-script `a:ea`/`a:cs`; shaping diserahkan ke PowerPoint.
- Gambar: geometri eksplisit; rasio aspect-safe (crop) — 07.G-2.
- Template pengguna: bila ada `.pptx` master, buka & isi placeholder (hapus elemen tak terpakai utuh, bukan dikosongkan).

## Verifikasi — laporan WAJIB menyebut jalur mana yang dipakai
- **(a) Struktural lewat kode** — `qa_deck.py` (04): baca ulang, rtl/ea, tashkeel/bidi, notes, gambar-crop, tabel; ukur teks vs kotak (deteksi meluber).
- **(b) Preview HTML hampiran** — `export_html.py`; jujur: ini hampiran, bukan render PowerPoint.
- **(c) Pengguna membuka `.pptx`** — putusan final.

**Larangan klaim kosong:** jangan tulis "sudah kucek tampilannya" tanpa menyebut (a)/(b)/(c).

## Log
| Tanggal | Keputusan | Oleh |
|---|---|---|
| 2026-09-05 | Ditulis dari kerangka + batasan terverifikasi | agent |
