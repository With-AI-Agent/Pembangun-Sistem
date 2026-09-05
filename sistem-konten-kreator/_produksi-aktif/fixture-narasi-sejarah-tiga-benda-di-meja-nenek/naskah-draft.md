# Naskah Draft — Tiga Benda di Meja Nenek

- **Channel:** `channel-fixture-narasi-sejarah/` (FIXTURE)
- **Model konten:** Narasi 60 Detik (v1) — **tetap**, target 130–145 kata, durasi 55–65 detik, tempo ±130 kata/menit
- **Revisi:** **r2**, 2026-09-06 WIB — pemadatan r1 atas izin eksplisit pengguna; bukan pengulangan diam-diam saat recovery
- **Tahap:** 3 — Naskah/Script (**draft revisi**, belum dikunci G2)
- **Jumlah kata VO:** **130** — dihitung dari bagian Naskah saja, berdasarkan pemisah whitespace
- **Rencana durasi:** **63 detik estimasi** = 60 detik pada 130 kata/menit + enam jeda antarparagraf masing-masing 0,5 detik. **Belum diukur lewat rekaman/TTS**; tambahan jeda internal/intonasi harus diperiksa saat produksi audio nanti.
- **Approval revisi:** izin membuat r2 sudah diberikan; review **G1 Tahap 3 r2** dan **G2 naskah final r2** belum. G1 historis atas r1 bukan penguncian r2.
- **Sumber eksternal:** tidak ada — cerita personal dummy/fiksi fixture, bukan klaim sejarah hasil riset. “Pukul lima” adalah detail cerita, bukan temuan faktual yang diverifikasi.
- **Karakter Tipe B:** tidak ada wujud karakter baru; nenek/anak-anak hanya disebut dalam VO, visual tetap b-roll benda sesuai model

> **FIXTURE UJI — BELUM FINAL.** Pengguna memilih revisi dalam batas brief, **bukan** perubahan brief atau penguncian naskah. Fokus tetap radio tua sebagai pengatur pagi; voice hangat, sedikit melankolis, tidak menggurui. Judul masih judul kerja, bukan metadata publish yang disetujui.

---

## Naskah (voice over)

Ada satu benda di sudut meja nenek: radio tua cokelat, dengan tombol aus di satu sisi.

Dulu, radio itu membangunkan satu rumah. Bukan alarm. Suara penyiar pagi pukul lima, lalu berita, lalu lagu yang itu-itu lagi.

Nenek tidak benar-benar mendengarkannya. Yang dia dengar adalah urutannya. Kalau lagunya berganti, air sudah matang. Kalau penyiar menyebut cuaca, anak-anak harus sudah mandi.

Radio itu bukan hiburan. Radio itu jam.

Sekarang radionya tidak ada. Diganti ponsel yang bisa bangun sendiri, yang bisa kita suruh diam, yang layarnya kita lihat sebelum melihat siapa pun.

Tapi urutan paginya masih sama. Air dimasak dulu, baru anak-anak dibangunkan. Hanya saja sekarang tidak ada yang memberi tanda, jadi kami menebak-nebak sendiri kapan pagi seharusnya mulai.

Yang berubah bukan kebiasaannya. Yang berubah: kita tidak lagi tahu siapa yang dulu mengaturnya.

---

## Jejak revisi dan pemeriksaan durasi

| Versi | Kata VO | Dasar @130 kata/menit | Enam jeda × 0,5 detik | Hasil estimasi |
|---|---:|---:|---:|---|
| r1 — sebelum revisi | 144 | 66,46 detik | 3 detik | **69,46 detik**, melebihi brief 55–65 detik |
| r2 — draft ini | **130** | **60 detik** | **3 detik** | **63 detik**, berada dalam target secara estimasi; belum pengukuran audio |

- r1 tetap dapat diperiksa pada commit `706060d391753e97954a49ccd6275ec8d061ff22`; temuan durasi awal tetap tersimpan di STATUS dan LOG_SESI, tidak dihapus atau dianggap keliru.
- Pemadatan: paragraf 1 dari 20 → 16 kata; paragraf 2 dari 24 → 20; paragraf 3 dari 28 → 23; paragraf 5 dari 24 → 23. Paragraf 4/6/7 tetap utuh. Total berkurang 14 kata, tanpa menambah klaim/benda/tokoh baru atau mengubah angle.
- Pembuka 16 kata ≈7,38 detik ucapan +0,5 detik jeda = **7,88 detik**, sesuai acuan hook 0–8 detik secara estimasi. Penutup tetap membawa cerita ke masa kini. Pembagian beat rinci belum dikunci.
- Jeda 0,5 detik dipasang di enam pergantian gagasan utama/antarparagraf. Jangan mempercepat voice diam-diam untuk mengejar durasi; jika pembacaan nyata nanti melewati 65 detik, laporkan dan minta keputusan revisi, bukan mengubah brief sendiri.

## Dependency Tahap 4 dan gerbang berikutnya

- `breakdown-output.md` yang sudah ada masih berasal dari **r1 (144 kata)**. Ditandai **draft lama/tidak sinkron**, bukan dianggap breakdown untuk r2 atau ditulis ulang sebelum review naskah.
- **G1 Tahap 3 r2:** apakah revisi ini cukup untuk melanjutkan penyesuaian draft breakdown?
- **G2 naskah final r2:** apakah teks revisi ini dikunci sebagai naskah final? **Belum ada approval.**
- Setelah dasar naskah disetujui, selaraskan breakdown sebagai **segmen narasi** sesuai model, lalu minta **G1 dan G2 breakdown** secara eksplisit. Tahap 5 belum dimulai, G2 konten final dan G3 merge juga belum diberikan.
