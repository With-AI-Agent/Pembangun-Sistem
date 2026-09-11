# Naskah Draft — Melati Terakhir di Pasar Kosong

- **Channel:** `channel-fixture-narasi-sejarah` (Narasi Sejarah — FIXTURE)
- **Model konten:** Narasi 60 Detik v1 — target 130-145 kata, durasi 55-65 detik, tempo ±130 kata/menit
- **Tahap:** 3 — Naskah/Script
- **Ide terpilih:** Opsi 1 — Melati Terakhir Sebagai Jam Pasar (G1 Tahap 1 disetujui 2026-09-10)
- **Konsep:** Konsep-angle.md G1 Tahap 2 disetujui 2026-09-10 — hook "Dulu, ada satu genggam melati..." + 4 beat (benda pintu masuk 0-8, konteks kebiasaan 8-35, yang berubah 35-52, penutup masa kini 52-60)
- **Jumlah kata VO:** **131** — dihitung whitespace dari bagian Naskah saja (wc -w = 131)
- **Rencana durasi:** **63,46 detik estimasi** = 60,46 detik pada 130 kata/menit (131 kata) + enam jeda antarparagraf masing-masing 0,5 detik (3 detik). **Belum diukur lewat rekaman/TTS** — jika pembacaan nyata melewati 65 detik, laporkan & minta keputusan revisi, jangan percepat voice diam-diam.
- **Sumber eksternal:** tidak ada — cerita personal fiksi fixture, bukan klaim sejarah hasil riset. Detail "pasar mulai kosong karena pindah" adalah setting cerita, bukan data statistik yang perlu verifikasi.
- **Karakter Tipe B:** reuse — Nenek Penjual Bunga (rambut putih dikonde rendah, selendang batik cokelat, payung biru pudar, keranjang anyam di lengan, pojok pasar subuh) — tercatat di `indeks-karakter.md`, bukan karakter baru. Deskripsi lengkap menempel di bawah (format A2).
- **Gerbang fact-check sebelum G2:** tidak ada klaim faktual yang butuh SUMBER.md — semua klaim adalah observasi fiksi. Tidak ada SUMBER.md yang wajib.
- **Approval:** menunggu G1+G2 Tahap 3

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

- Konsisten di seluruh konten: deskripsi di atas dibawa ke semua unit visual yang memunculkannya (Prompt Library A2)
- Status indeks: sudah tercatat di `indeks-karakter.md` sebagai Tipe B (konten pertama `2026-09-09-penjual-bunga-di-pasar-subuh.md`), konten kedua `2026-09-10-melati-terakhir-di-pasar-kosong.md` sudah ditambahkan ke kolom Konten lain di Tahap 6 langkah 2b (PR #39 diff) — G2 disetujui 2026-09-10 — koreksi review PR #39 putaran 2 (dokumen ini snapshot Tahap 3, status final ada di STATUS.md + final-content.md)
- Tidak ada karakter Tipe B baru di konten ini

## Persona & Voice Check (sebelum minta G2)

- **Gaya bahasa:** santai tapi tertata, kalimat pendek (rata-rata 5-7 kata), banyak jeda — contoh asli "Meja itu tidak pernah pindah. Yang pindah, orang-orang yang duduk di sekitarnya." — terpenuhi
- **Tone:** hangat & agak melankolis, tanpa mendramatisir — tidak ada kata "tragis, sangat sedih, mengharukan sekali" — hanya fakta kecil
- **Kosakata khas:** "dulu" (paragraf 1), "konon" (paragraf 2), "yang tersisa" implisit di "satu genggam terakhir", "tidak ada yang mencatat" (paragraf terakhir) — terpenuhi
- **HARUS ADA:** satu benda/ruang konkret sebagai pintu masuk — melati (benda) + sudut pasar (ruang) — terpenuhi
- **TIDAK BOLEH ADA:** klaim sejarah tanpa rujuk — tidak ada; nama tokoh nyata — tidak ada; nada menggurui — tidak ada kalimat "kita harus belajar"; clickbait — tidak menjanjikan yang tidak ada di naskah — terpenuhi
- **Pembuka khas:** "Dulu, ada satu benda yang..." → dipakai varian "Dulu, ada satu genggam melati yang selalu habis paling akhir." — terpenuhi
- **Penutup khas:** "Sekarang benda itu sudah tidak ada. Tapi caranya mengatur hari kita, masih." → dipakai varian "Sekarang melati itu tidak ada di sudut itu. Tapi caranya memberi tahu kapan hari selesai, masih." — terpenuhi, mengembalikan ke masa kini

## Catatan produksi untuk Tahap 4

- Unit breakdown = segmen narasi (sesuai Model Brief) — bukan shot
- 7 segmen direncanakan (S1 Hook, S2 Detail benda, S3 Konteks kebiasaan, S4 Penanda waktu, S5 Insiden pasar kosong, S6 Aksi melipat payung, S7 Penutup masa kini) — akan dirinci di breakdown-output.md
- Visual: b-roll netral, tidak ada wajah dikenali, palet cokelat kayu/krem/hijau tua pudar + putih melati + biru pudar
- Sumber eksternal tetap Tidak ada — tidak perlu SUMBER.md

## Next — UPDATE koreksi review PR #39 putaran 2

**G1+G2 Tahap 3 disetujui 2026-09-10** — naskah 131 kata terkunci, lanjut ke Tahap 4 Breakdown (sudah selesai) — koreksi review putaran 2
