# 02 — Basis Pengetahuan Desain Visual & Komunikasi (Sistem Presentasi)

> **Self-contained.** Hasil riset internet (5 Sep 2026) + kaidah yang wajib dipakai agent saat memproduksi deck. Sistem **mewajibkan agent melakukan riset visual** sebelum/seraya mendesain (lihat bagian F) — dokumen ini adalah seed, bukan pengganti riset.

## A. Prinsip desain inti (sintesis riset)
1. **Alignment** — setiap elemen punya koneksi visual ke elemen lain; snap ke grid, jangan "kira-kira". [1][4]
2. **Contrast** — kontras teks-latar tinggi; beda ukuran/tebal untuk hierarki. Uji terbaca dari ~3 m. [1][3]
3. **Whitespace / negative space** — sisakan 15–20% area kosong; ruang kosong = napas, bukan kekurangan. [1][3]
4. **Consistency / Repetition** — kunci palet, font, layout lewat master; ulangi elemen identitas agar deck terasa satu. [1][4]
5. **Proximity** — kelompokkan yang berkaitan; pisahkan yang berbeda. [3][4][5]
6. **Hierarchy** — pandu mata: judul → pesan kunci → detail (skala tipografi H1→body). [1][2][3]
7. **Aturan angka:** ≤2 keluarga font; palet 3 warna (60-30-10); body ≥18–24pt; 16:9; animasi hemat (80% slide tanpa animasi). [1][3]

## B. Aspect ratio gambar (WAJIB — bug deck#1: dekorasi "gepeng")
- **Jangan pernah stretch.** Saat menempatkan gambar pada kotak w×h, rasio tampilan HARUS sama dengan rasio area sumber, kalau tidak akan gepeng.
- Implementasi: baca dimensi asli gambar; hitung crop fraksi sehingga `(crop_w*W_img)/(crop_h*H_img) == w/h` target; pakai param `crop` add_picture. Lihat `build_deck_v4.py`.
- Untuk pita/aksen vertikal dari pola lanskap: crop strip vertikal sempit, jangan stretch penuh.

## C. Tipografi RTL / bidi (Arab) — hindari artefak tanda baca
- Set `rtl=1`, `algn=right`, `a:ea`/`a:cs`. Shaping diserahkan ke PowerPoint.
- **Hindari tanda netral yang membingungkan bidi** di tengah teks Arab: kurung ASCII `( )`, em-dash `—`, tanda `+` di awal/akhir frasa. Ganti dengan konstruksi kata (mis. "لحديث المرأة" bukan "(حديث المرأة)"), atau bungkus dengan RLM/LRM bila terpaksa.
- Satu arah alignment per slide; jangan campur rata-kanan dan rata-kiri dalam satu blok.

## D. Mode penyajian isi: BULLET vs PARAGRAF
- Tidak semua pengguna mau poin-poin. Sistem wajib mendukung dua mode per slide:
  - **Bullet** untuk daftar/rincian yang benar-benar terpisah.
  - **Paragraf ringkas** (2–4 kalimat) untuk narasi/penjelasan mengalir — sering lebih disukai untuk bahan akademik.
- Pilih mode per slide sesuai karakter isi & preferensi pengguna (catat di BRIEF/OUTLINE). Default akademik: campuran — assertion judul + paragraf ringkas atau bullet secukupnya.

## E. Checklist multi-skill (presentasi = banyak keahlian)
Sebelum G3, agent wajib memeriksa ia telah memakai: **keilmuan/akademik** (isi akurat, berjejak), **bahasa** (Arab/Indonesia idiomatik, bidi benar), **desain grafis** (A+B+C), **komunikasi visual** (hierarki, whitespace), **kreativitas** (metafora/visual yang melayani isi), **pedagogi audiens** (apa yang dicari penguji). Jika ada yang lemah, perbaiki atau riset.

## F. Mandat riset visual
- Agent **wajib** melakukan riset internet tentang desain/komunikasi visual bila ragu atau saat menaikkan kualitas (web_search/fetch). Hasil riset yang terpakai dicatat ke dokumen ini (dengan sumber) agar menumpuk jadi pengetahuan sistem.
- Sumber seed: [1] deckary.com (5 prinsip PPT), [2] chroniclehq.com, [3] study.com, [4] slideshare CRAP, [5] mauriziolacava.com (Gestalt).

## Log
| Tanggal | Keputusan | Oleh |
|---|---|---|
| 2026-09-05 | Dokumen dibuat dari riset; aturan B (aspect), C (bidi), D (paragraf), E (multi-skill), F (mandat riset) ditetapkan | agent |
