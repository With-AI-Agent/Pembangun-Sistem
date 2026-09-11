# Naskah Final — Melati Terakhir di Pasar Kosong

- **Channel:** `channel-fixture-narasi-sejarah/` (Narasi Sejarah — FIXTURE)
- **Model konten:** Narasi 60 Detik (v1) — target 130–145 kata, durasi 55–65 detik, tempo ±130 kata/menit
- **Tahap:** 3 — Naskah/Script (naskah final produksi 2026-09-10, dikunci G2)
- **Jumlah kata VO:** **131** — dihitung dari bagian Naskah saja, berdasarkan pemisah whitespace (wc -w = 131)
- **Rencana durasi:** **63,46 detik estimasi** = 60,46 detik pada 130 kata/menit + enam jeda antarparagraf masing-masing 0,5 detik. **Belum diukur lewat rekaman/TTS** — jika pembacaan nyata melewati 65 detik, laporkan & minta keputusan revisi.
- **Sumber eksternal:** tidak ada — cerita personal fiksi fixture, bukan klaim sejarah hasil riset. Detail "pasar mulai kosong karena pindah" adalah setting cerita, bukan data statistik.
- **Karakter Tipe B:** reuse — Nenek Penjual Bunga (rambut putih dikonde rendah, selendang batik cokelat, payung biru pudar, keranjang anyam berisi melati putih) — deskripsi lengkap menempel di bawah; baris indeks di `indeks-karakter.md` diperbarui (konten kedua di kolom Konten lain)
- **Judul tayang resmi yang diusulkan:** "Melati Terakhir di Pasar yang Mulai Kosong" (Opsi 1 dari publish-prep.md — **G2 disetujui 2026-09-10**, G3 ditunda PR #39 OPEN — koreksi review putaran 1)
- **Topik singkat:** melati terakhir sebagai penanda waktu pasar tutup; payung biru dilipat sebelum tengah hari di sudut pasar yang mulai kosong karena pindah

> **Produksi 2026-09-10_4** — branch `arena/01a089b8-pembangun-sistem` — Tahap 1 G1 disetujui, Tahap 2 G1 disetujui, Tahap 3 G1+G2 disetujui (naskah final terkunci 131 kata), Tahap 4 G1+G2 disetujui (breakdown 7 segmen S2 koreksi 22→20), Tahap 5 G1 disetujui (7 asset b-roll), Tahap 6 G2 disetujui G3 ditunda PR #39 OPEN. Sumber: `sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-melati-terakhir-di-pasar-kosong/` — arsip ini dipindahkan pada Tahap 6 langkah 1. Koreksi review PR #39 putaran 1: S2 22→20 kata, total tetap 131.

---

## Naskah (voice over)

Dulu, ada satu genggam melati yang selalu habis paling akhir.

Bukan yang paling harum. Yang paling terakhir.

Konon, nenek itu datang sebelum lapak lain dibuka.

Rambut putih dikonde. Selendang batik cokelat. Payung biru pudar di dua sisi.

Tangannya menyusun melati tanpa menghitung.

Satu per satu. Di keranjang anyam.

Sudut itu gelap. Tapi sejuk. Melati tidak cepat layu.

Yang lewat tahu. Kalau melati masih ada, pasar belum tutup.

Pagi itu, lapak sebelah tidak dibuka.

Lalu sebelahnya lagi.

Pasar mulai kosong. Bukan karena sepi. Karena pindah.

Di keranjang, tinggal satu genggam terakhir.

Nenek menjualnya ke pembeli terakhir.

Lalu melipat payung birunya.

Untuk pertama kali, payung itu dilipat sebelum tengah hari.

Sekarang melati itu tidak ada di sudut itu.

Tapi caranya memberi tahu kapan hari selesai, masih.

Tidak ada yang mencatat kapan pasar tutup.

---

## Karakter Tipe B (reuse, format A2)

```
KARAKTER PER-KONTEN: Nenek Penjual Bunga
Fisik: perempuan tua usia lanjut, rambut putih dikonde rendah, selendang batik cokelat digulung di bahu, payung biru pudar, keranjang anyam berisi melati putih di lengan, biasanya dilihat dari belakang/samping — wajah tidak detail (mengikuti aturan channel: tidak ada wajah yang bisa dikenali)
Peran dalam konten ini: tokoh yang diceritakan — subjek pandangan narator; pintu masuk cerita lewat benda melati, bukan deskripsi tokoh panjang
```

- Konsisten di seluruh konten: deskripsi di atas dibawa ke semua unit visual yang memunculkannya (lihat bagian A2 di `_sistem/06_PROMPT_LIBRARY.md` — S2,S3,S5,S6).
- Status indeks: sudah tercatat di `indeks-karakter.md` sebagai Tipe B (konten pertama `2026-09-09-penjual-bunga-di-pasar-subuh.md`), konten kedua ini `2026-09-10-melati-terakhir-di-pasar-kosong.md` ditambahkan ke kolom Konten lain pada Tahap 6 langkah 2b.
- Tidak ada karakter Tipe B baru di konten ini.

## Jejak produksi (ringkas)

- **Ideation:** 4 opsi, ide terpilih Opsi 1 Melati Terakhir Sebagai Jam Pasar — cek pengulangan vs arsip 2026-09-09 Penjual Bunga di Pasar Subuh — angle beda (akhir/transisi vs rutinitas)
- **Konsep & Angle:** hook "Dulu, ada satu genggam melati yang selalu habis paling akhir." + 2 varian (total 3 varian termasuk hook), struktur 4 beat (0-8 benda pintu masuk, 8-35 konteks kebiasaan, 35-52 yang berubah, 52-60 penutup masa kini), estimasi 132 kata / 63,92 dtk, visual b-roll 7 segmen
- **Naskah:** 131 kata, 63,46 dtk estimasi, Persona & Voice check lengkap (santai tertata kalimat pendek, hangat-melankolis, kosakata khas dulu/konon/tidak ada yang mencatat, HARUS ADA benda/ruang melati+sudut pasar, TIDAK BOLEH ADA dipatuhi, pembuka/penutup khas varian dipakai)
- **Breakdown:** 7 segmen narasi (S1 17 kata, S2 20 [koreksi 22→20 review PR #39 putaran 1], S3 20, S4 10, S5 23, S6 18, S7 23), b-roll netral, prompt generate per segmen (Prompt Library D), file referensi tidak ada (channel faceless — keterangan eksplisit)
- **Assets:** 7 JPG b-roll netral vertical 9:16, total 1,7 MB, hash tercatat di CATATAN-ASSET.md, checklist Tahap 5 lengkap, S2 sebagai acuan visual awal
- **Publish prep:** 5 opsi judul, caption panjang & pendek Persona & Voice, hashtag, thumbnail konsep tanpa clickbait
