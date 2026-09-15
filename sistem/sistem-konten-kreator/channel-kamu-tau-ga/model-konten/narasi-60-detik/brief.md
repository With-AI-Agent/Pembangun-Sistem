# Model Konten Brief — Narasi 60 Detik (Channel: Kamu Tau Ga?)

### Dokumen "hidup" milik SATU model konten, dibaca BERSAMAAN dengan Channel Brief channel-nya.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [x] **Draft** — sudah digali via Model Konten Discovery 2026-09-11_2
- [x] **Reviewed** — sudah dibaca lengkap oleh pemilik 2026-09-11
- [x] **Approved** — isi dikunci lewat gerbang **G2** 2026-09-11 (`setuju_g2`)
- [x] **Merged** — PR #41 MERGED 2026-09-11 via `gh pr merge 41 --merge` — merge commit `290ac1b` — G3 `setuju_g3` final `merge_sekarang` setelah review HIJAU
- [x] **Operational** — sudah `Merged` dan semua dependency wajib ada (Channel Brief Operational, unit segmen narasi ditetapkan)

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [x] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [x] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan — unit kerjanya **segmen narasi** (lihat bagian 4)
- [x] Override terhadap Channel Brief sudah dinyatakan eksplisit — tidak ada override Persona & Voice, struktur fleksibel (hook + konteks + penutup masa kini)
- [x] Gerbang tambahan sudah dicatat — tidak ada gerbang tambahan, G2/G3 bawaan tetap; fact-check gate di Tahap 0 dan Tahap 3 sesuai pipeline
- [x] Channel Brief induknya sudah berstatus `Operational` — PR #41 MERGED 2026-09-11
- [x] Sudah `Merged` ke `main` — PR #41 MERGED commit `290ac1b`

**Versi:** `1` — **Terakhir diperbarui:** `2026-09-11`

## Mewarisi dari: `channel-kamu-tau-ga/channel-brief.md`

Semua yang dikunci di sana (Persona & Voice penasaran ringan witty 140-150 kata/menit, Konsistensi Visual semua tidak berlaku, Gaya Visual b-roll makro bersih) berlaku di sini tanpa override, kecuali yang dinyatakan eksplisit di bawah.

---

## 1. Identitas Model Konten

- **Nama model konten:** Narasi 60 Detik
- **Definisi singkat:** satu cerita tentang sejarah 1 benda sehari-hari, dinarasikan voice over penasaran ringan, durasi 55-65 detik (±130-150 kata), visual murni b-roll makro benda tanpa wajah. Satu-satunya model konten channel ini untuk fase awal (roadmap: Long 2-3 menit nanti).

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:** 55-65 detik, setara 130-150 kata naskah pada tempo 140-150 kata/menit (lebih cepat dari fixture 130). Hook pertanyaan wajib di 0-3 detik.
- **Struktur konten khas format ini:** fleksibel tergantung benda, tapi WAJIB punya 3 elemen: (1) Hook pertanyaan retoris "Kamu tau ga, kenapa...?" (0-5 dtk), (2) Konteks — asal-usul singkat atau kebiasaan yang menempel pada benda itu (5-35 dtk) + yang berubah / kenapa masih begitu (35-52 dtk), (3) Penutup yang mengembalikan ke masa kini / kebiasaan hari ini (52-60 dtk). Tidak kaku 4 beat, tapi 3 elemen itu harus ada.
- **Platform paling cocok untuk format ini:** YouTube Shorts, TikTok, Instagram Reels — vertikal 9:16.

## 3. Gaya Visual Spesifik

- **Pendekatan visual:** sama seperti Channel Brief — b-roll makro benda sehari-hari, framing bersih, depth of field dangkal, background kayu/kain/putih tulang, palet hangat netral krem-cokelat muda-abu hangat. Tidak ada animasi, tidak ada karakter, tidak ada reenactment orang.
- **Kalau ada elemen Konsistensi Visual dari channel:** tidak ada yang perlu ditampilkan — channel ini tidak mengunci elemen visual apa pun sebagai file reference (semua tidak berlaku). Jadi tidak ada penyesuaian.

## 4. Alur Kerja Produksi

**Mode:** [ ] Ikuti Kerangka Standar (dengan override ringan)  /  [x] Alur Kerja Kustom

### Kalau Mode = Ikuti Kerangka Standar

Tidak berlaku — model ini memakai Alur Kerja Kustom (lihat bawah).

### Kalau Mode = Alur Kerja Kustom

- **Kenapa model konten ini butuh alur kustom (beda dari kerangka standar):** Channel ini membahas klaim sejarah benda sehari-hari — risiko klaim tanpa sumber tinggi (area berisiko di Channel Brief). Pipeline standar baru melakukan fact-check di Tahap 3 (Naskah) sebagai gerbang G2, tapi untuk channel ini riset dan verifikasi harus terjadi **sebelum** ideation final dan konsep, supaya ide yang dipilih sudah punya sumber terverifikasi minimal 2 sumber independen. Jadi ada Tahap 0 Riset Awal & Verifikasi Fakta yang mendahului Ideation. Ini bukan ekstraksi massal (1 sumber jadi banyak konten), tapi verifikasi fakta per benda. Karena itu alur kustom diperlukan.

- **Tahapan alur kerja:**

| No | Nama Tahap | Input | Proses/Tools | Output |
|---|---|---|---|---|
| 0 | Riset Awal & Verifikasi Fakta | Benda dari Bank Ide Awal atau observasi baru (contoh: tutup panci berlubang) | Web search (depth 2-3), kumpulkan minimal 2 sumber independen untuk klaim utama, catat di SUMBER.md dengan tanggal akses, status verifikasi, lisensi; turunkan bahasa kalau tidak bisa verifikasi | `SUMBER.md` awal + ringkasan fakta terverifikasi (1-2 paragraf) + daftar klaim yang belum bisa diverifikasi (kalau ada) |
| 1 | Ideation | Ringkasan fakta terverifikasi + arsip indeks.md (cek pengulangan topik) + Bank Ide | Buat 3-5 opsi angle konkret per benda (bukan cuma judul, tapi 2-3 kalimat kenapa menarik + kaitannya dengan kebiasaan masa kini); cek indeks.md apakah topik serupa pernah dibahas | 1 ide terpilih (benda + angle spesifik) |
| 2 | Konsep & Angle | Ide terpilih + Persona & Voice Channel | Susun kerangka: hook pertanyaan 3 detik, struktur fleksibel (konteks + yang berubah), closing balik masa kini, perkiraan durasi; JANGAN keluar dari Persona & Voice | Kerangka konten (bukan naskah penuh) |
| 3 | Naskah/Script | Kerangka + SUMBER.md awal + Persona & Voice | Tulis naskah 130-150 kata, gaya penasaran ringan witty, kalimat pendek, hook "Kamu tau ga...?" di awal, penutup balik masa kini; sertakan sumber untuk tiap klaim faktual; sebelum G2, verifikasi semua klaim punya baris di SUMBER.md dengan status Terverifikasi | `naskah-draft.md` 130-150 kata + SUMBER.md final |
| 4 | Breakdown Output | Naskah final + SUMBER.md | Pecah naskah jadi 5-7 segmen narasi (unit = segmen narasi, bukan shot); tiap segmen: nomor, bagian naskah, deskripsi visual b-roll makro, prompt generate b-roll (tanpa wajah), file referensi tidak berlaku | `breakdown-output.md` 5-7 segmen |
| 5 | Generate/Acquire Assets | Breakdown-output.md | Generate b-roll via text-to-image (prompt makro benda, background polos/kayu) atau acquire stok berlisensi; checklist: tanpa wajah, tanpa logo, palet hangat, rasio 9:16 1080x1920; simpan di `_produksi-aktif/[channel]-[judul]/assets/` + CATATAN-ASSET.md hash | 5-7 JPG b-roll + CATATAN-ASSET |
| 6 | Assembly & Publish Prep | Naskah + assets + SUMBER.md | Buat 3-5 opsi judul hook, caption lengkap Persona & Voice, hashtag, thumbnail konsep tanpa clickbait; pindahkan naskah final ke arsip, update indeks, buat metadata.md, arsip SUMBER.md | `publish-prep.md`, `final-content.md`, arsip naskah, indeks, metadata, sumber |

- **Titik pertemuan dengan kerangka standar:** Tahap 0 Riset adalah tambahan di depan. Setelah Tahap 0 selesai, Tahap 1-6 di atas pada dasarnya memetakan ke kerangka standar: Tahap 1 Ideation = Tahap 1 pipeline standar, Tahap 2 Konsep = Tahap 2 standar, Tahap 3 Naskah = Tahap 3 standar (dengan G1+G2), Tahap 4 Breakdown = Tahap 4 standar (G1+G2), Tahap 5 Generate = Tahap 5 standar (G1), Tahap 6 Assembly = Tahap 6 standar (G2+G3). Jadi setelah Tahap 0, lanjut mengikuti definisi gerbang G1/G2/G3 di `05_CONTENT_PRODUCTION_PIPELINE.md`.

- **Catatan tools yang belum pasti:** Generate b-roll bisa pakai text-to-image internal (generate_image tool) atau stok berlisensi — belum dikunci satu tools, fleksibel per konten. TTS untuk VO belum dipakai di tahap produksi repo (naskah saja), tapi karakteristik suara sudah didefinisikan di Channel Brief untuk produksi eksternal.

## 5. Contoh Konkret

Konten "Kenapa Tutup Panci Ada Lubang Kecil": 
- Tahap 0 Riset: cari kenapa tutup panci kaca ada lubang kecil — 2 sumber (artikel produsen cookware + artikel sains dapur) bilang untuk pelepasan uap mencegah tekanan & bunyi bergetar. Catat di SUMBER.md.
- Tahap 1 Ideation: angle terpilih — "Lubang kecil itu bukan cacat produksi, tapi penyelamat tutup panci biar tidak bergetar & air tidak meluap"
- Tahap 2 Konsep: Hook "Kamu tau ga, kenapa tutup panci selalu ada lubang kecilnya?" → konteks dulu tutup panci tanpa lubang bergetar & berbahaya → yang berubah: ditambah lubang kecil sebagai ventilasi → penutup: sekarang semua tutup panci punya, tapi jarang yang tau fungsinya.
- Tahap 3 Naskah: 138 kata, tempo 145 kata/menit, witty.
- Tahap 4 Breakdown: 6 segmen (hook tutup panci close-up, konteks panci zaman dulu, masalah uap, solusi lubang, demo uap keluar, penutup panci di dapur modern)
- Tahap 5 Assets: 6 JPG b-roll makro tutup panci, uap, panci di kompor, background kayu/putih.
- Tahap 6 Publish: judul opsi, caption, hashtag #kamutauga #sejarahbenda #dapur

## 6. Log Keputusan Model Konten

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-11 | Model Konten Brief v1 Draft — Narasi 60 Detik untuk Kamu Tau Ga? | Discovery 1 putaran — durasi 55-65 dtk, struktur fleksibel hook+konteks+penutup, alur kustom dengan Tahap 0 Riset |
| 2026-09-11 | Mode Alur Kerja Kustom dipilih, bukan standar | Pemilik pilih `kustom_riset` — risiko klaim sejarah tanpa sumber, butuh verifikasi sebelum ideation |
| 2026-09-11 | Gaya visual sama seperti Channel Brief, tidak ada override | Pemilik pilih `sama_channel` — b-roll makro bersih |
| 2026-09-11 | G2 Approved — Model Konten Brief v1 dikunci | Pemilik setuju via ask_user `setuju_g2` — lanjut produksi 1 konten |
| 2026-09-11 | G3 MERGED PR #41 — Model Konten Brief v1 Operational | Review HIJAU tanpa BLOCKER, G3 `merge_sekarang` — merge commit `290ac1b` — validasi PASS |
