# PELAJARAN DARI DECK NYATA #1 (tesis fikih hiasan wanita)

> ## ⚠️ STATUS: BUKAN SAMPLE — WAJIB DIBACA DULU
> **Deck ini (.pptx tesis fikih hiasan wanita) dan PROSES PEMBUATANNYA BUKAN sample/contoh/templat.**
> Pernyataan pengguna (5 Sep 2026): percobaan ini banyak cacatnya — termasuk prosesnya yang tidak sesuai keinginan pengguna: **sesi perancangan visual, perancangan isi, dan sebagainya dilewati begitu saja**. Maka:
> - **JANGAN** menyalin deck ini atau jalannya proses ini sebagai contoh produksi.
> - **JANGAN** menganggap urutan/keputusan di repo deck ini sebagai pola ideal.
> - Ambil **hanya** pelajaran anti-pola di bawah (yaitu "jangan lakukan X"); lalu produksi berikutnya wajib mengikuti alur penuh `_sistem/01–10` + gerbang **G1/G2/G3**, dengan **sesi perancangan isi dan perancangan visual yang benar-benar dilakukan bersama pengguna dan disetujui eksplisit SEBELUM build**.
> Dokumen ini berstatus *catatan kegagalan + pelajaran*, bukan *contoh keberhasilan*.

> Ditulis 5 Sep 2026 setelah pengguna melihat v1 di PowerPoint dan memberi umpan balik jujur.
> Tujuan: agar deck berikutnya langsung bagus, tidak mengulang kelemahan v1.

## Cacat proses pembuatan (alasan deck ini BUKAN sample)
1. **Sesi perancangan isi & perancangan visual dilewati/diremehkan** — tidak benar-benar dirancang bersama pengguna sebelum build; akibatnya revisi bolak-balik (v1–v7).
2. Kedalaman isi baru dipenuhi setelah beberapa kali keluhan ("isi terlalu ringkas", lalu "isi lebih panjang sesuai tesis") — seharusnya ditangkap di sesi perancangan isi.
3. Ada keputusan yang seharusnya gerbang approval eksplisit tetapi berjalan terlalu cepat tanpa diskusi desain yang memadai.
4. Sebagian konten (heading السؤال الثاني) masih rekonstruksi berlabel, bukan verbatim — produksi diajukan sebelum bahan tuntas.
→ Deck berikutnya: lakukan Tahap 1–3 (Brief → Pahami bahan → **Outline+Rencana Visual dengan sesi perancangan isi & visual bersama pengguna**) secara penuh, baru build.

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
