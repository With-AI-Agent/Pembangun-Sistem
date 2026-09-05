# PELAJARAN DARI DECK NYATA #1 (tesis fikih hiasan wanita)

> Ditulis 5 Sep 2026 setelah pengguna melihat v1 di PowerPoint dan memberi umpan balik jujur.
> Tujuan: agar deck berikutnya langsung bagus, tidak mengulang kelemahan v1.

## Umpan balik pengguna (verbatim inti)
- "Keliatannya ga bagus."
- "Isinya juga kurang sesuai sama yang diharapkan."

## Diagnosis (dua kelemahan nyata v1)
1. **Desain terlalu minimalis / terkesan belum selesai.**
   - Font isi terlalu kecil (22pt), kotak isi di-anchor atas sehingga menyisakan ruang kosong besar di bawah.
   - Elemen identitas (pita kanan tipis) terlihat seperti scrollbar, bukan desain.
   - Tidak ada footer konsisten (nomor slide + sumber) yang memberi kesan "dibuat profesional".
2. **Isi terlalu berat ke metode/struktur, ringan di HASIL.**
   - v1 menaruh 4+ slide untuk metode/prosedur, tapi hanya 1 slide substantif (العلة).
   - Audiens sidang ingin melihat **temuan/hukum** lebih dulu, baru metode.

## Perbaikan yang diterapkan di v2 (`build_deck_v2.py`)
- Font judul 34–40pt, isi 24–26pt; kotak isi `vertical_anchor=MIDDLE` (isi terpusat, tak ada ruang kosong menganga).
- Footer bar hijau penuh-lebar di bawah: nomor slide (angka Arab) kiri + jejak halaman kanan, teks emas.
- Spine kanan = hijau lebar + garis emas, terbaca sebagai identitas, bukan scrollbar.
- Slide judul diberi bingkai emas agar "jadi".
- **Rebalance isi:** temuan/hasil (dari ملخص hal 6) ditaruh di depan (S2–S4), metode/prosedur dipadatkan (S8–S9).

## Pelajaran operasional utk deck berikutnya
- Mulai dari **temuan/kesimpulan**, bukan dari metode. Metode cukup 1–2 slide.
- Font isi minimal 24pt; selalu `MIDDLE` anchor; selalu footer bar + nomor + sumber.
- Uji tampilan dengan membuka hasil (preview/PowerPoint) sebelum diajukan, bukan hanya baca-balik struktur.
- **Unduh:** di lingkungan ini viewer/preview TIDAK bisa unduh biner; link web dipagari token.
  Jalur unduh yang didukung = **GitHub** (file page → Download raw). Jangan janjikan unduh via preview.
