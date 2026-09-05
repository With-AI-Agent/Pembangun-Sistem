# RENCANA VISUAL — Presentasi Tesis Fikih Hiasan Wanita

> **G2 — disetujui 5 September 2026.** Gaya harus tunduk pada aturan lantai (`_sistem/06_PRINSIP_DESIGN_BERBASIS_BUKTI.md`): judul assertion, coherence (tanpa hiasan tak perlu), redundancy (naskah masuk catatan, bukan slide), segmenting (1 pesan/slide), signaling. Semua pilihan estetika di bawah ditandai dasarnya; yang `[PENILAIAN AGENT]` boleh kamu ganti.

## Arah umum `[DIPUTUSKAN dari domain]`
- **Formal-akademik, RTL, teks Arab.** Audiens dosen penguji → bersih, kontras tinggi, tanpa dekorasi ramai.
- **Mode gambar: M0** di hampir semua slide; **S8** memakai **tabel perbandingan** (struktur, bukan gambar berlisensi). Aksen identitas: **1 gambar pola geometris M3 (AI)** dipasang **parsial** (pita sisi, bukan slide penuh) di semua slide — bebas teks (Aturan G-1, diverifikasi via visi 5 Sep 2026), tercatat di `DAFTAR_GAMBAR.md`. Tidak ada M1/M2-data/M4.
- Alasan M0: Mayer (coherence) — gambar dekoratif menambah beban kognitif; topik fikih tidak butuh foto. (M3 hanya untuk aksen brand yang sangat muted — diperbolehkan `01` bagian C & B.5.)

## Palet `[REKOMENDASI, dasar: PENILAIAN AGENT]` — pilih satu
| Opsi | Palet | Kesan | Rekomendasi? |
|---|---|---|---|
| **A** | Hijau tua `#0F3D2E` + emas lembut `#C9A227` + krem `#F7F3E9` | Islami-akademik, tenang | **YA (rekomendasi)** |
| B | Biru tua `#12365A` + abu-abu terang `#F2F4F7` + aksen `#2E86C1` | Netral-modern | alternatif |
| C | Monokrom hitam-putih + satu aksen marun `#7A1F2B` | Sangat formal | alternatif |
- **Default kalau kamu jawab "terserah": Opsi A.**
- Kontras teks-latar dijaga ≥ WCAG AA (teks gelap di latar krem, atau sebaliknya).

## Tipografi `[REKOMENDASI, dasar: PENILAIAN AGENT]`
- Font Arab: **Amiri** (judul) + **Scheherazade/New Roman Arab** (isi) bila tersedia; fallback: font Arab bawaan PowerPoint (Traditional Arabic). Karena `.pptx` hanya menyimpan nama font, PowerPoint yang mengganti bila tak ada.
- Ukuran (dinaikkan di v2): judul 34–40pt, isi 24–26pt (v1 terlalu kecil → terkesan belum jadi).

## Tata letak / geometri `[DIPUTUSKAN dari aturan G-2]`
- **RTL:** semua paragraf `rtl=1`, rata-kanan; judul di kanan-atas.
- Margin generos; area isi tidak penuh (ruang putih = coherence).
- Tabel S8: 5 kolom (المذهب × العلة), header baris emas, zebra ringan.
- Nomor halaman cetak tesis dicantumkan kecil di pojok (jejak sumber) — mis. "ص٦٦".

## Yang TIDAK dipakai
- Gambar internet (M4), ikon dekoratif, animasi muncul-per-baris (tidak bisa diverifikasi tanpa renderer). Gambar AI (M3) hanya 1 aksen pola — tidak untuk data/konsep slide (lihat Arah umum).

## Log Keputusan visual
| Tanggal | Keputusan | Dasar | Oleh |
|---|---|---|---|
| 2026-09-05 | M0 default; S8 tabel; palet A default; font Amiri | PENILAIAN AGENT + Mayer | agent (menunggu approval G2) |
| 2026-09-05 | v2: font isi 24–26, anchor MIDDLE, footer bar+nomor+ sumber, spine emas, rebalance isi ke temuan | Umpan balik pengguna (deck#1) | agent |
| 2026-09-05 | Sync pasca audit independen: header status (G2 disetujui), aksen M3 dicatat eksplisit (AP-04), rujukan lantai dikoreksi `_sistem/03`→`06` (AP-08) | `AUDIT_SISTEM_PRESENTASI_2026-09-05.md` | agent (audit) |
