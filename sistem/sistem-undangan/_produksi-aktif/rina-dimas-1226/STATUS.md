# Status Unit — Undangan Uji Coba b3 — `rina-dimas-1226`

> **CATATAN KOREKSI 2026-09-21:** field `Pekerjaan belum tersimpan` pernah diisi daftar pekerjaan **berikutnya** — itu salah makna (protokol checkpoint: field ini soal pekerjaan **belum tersimpan/ter-commit**). Ditemukan oleh gerbang FI repo dan dikoreksi di commit yang sama; daftar pekerjaan berikutnya kini ada di barisnya sendiri di bawah. Dilaporkan terbuka, bukan didiamkan.
>
> **UNIT UJI COBA, BUKAN CLIENT.** Dibuat untuk menjalankan **ROADMAP JALAN PRODUKSI PERTAMA
> butir (2) b3** (handoff log sesi slot 44; dikerjakan sesi slot 45): satu undangan pernikahan
> **fiktif/sendiri** yang dijalankan **sampai terbit**, supaya seluruh jalur (data → desain →
> aset → rakit → terbit → serah terima) terbukti dengan bukti nyata, bukan klaim.
> Semua data di unit ini **fiktif** dan ditandai begitu di layar (`web/data-acara.json` bagian `meta`).

- **Status:** `aktif` — uji coba b3 (fase portofolio L1; bukan client)
- **Unit:** `sistem/sistem-undangan/_produksi-aktif/rina-dimas-1226/`
- **Slug (permanen, dokumen 09 bagian 3):** `rina-dimas-1226` — nama mempelai + bulan-tahun; **tidak
  boleh berubah** sesudah tersebar. Rencana fase 1: `lee-studio.pages.dev/rina-dimas-1226`
- **L2 yang dipakai:** `02_PROFIL_JENIS_ACARA.md` — jenis acara **pernikahan** (cakupan umum, G1 LULUS)
- **Model desain (G2, putusan pemilik 21 Sep 2026 paket E1–E4):** **Modern minimalis** (netral + 1 aksen;
  Montserrat dominan; whitespace; nyaris tanpa ornamen)
- **Pekerjaan belum tersimpan:** Tidak ada
- **Tahap terakhir selesai (2026-09-21 (UTC)):** **Tahap 1–6** — intake & brief (G0), data acara
  tervalidasi (G1) lewat gerbang data yang **kini ditegakkan alat** (`_sistem/validate_unit.py`),
  spesifikasi desain (G2), aset (G3 — unit ini **0 aset raster**; lihat catatan bukti di bawah),
  rakit & pratinjau (**G4**), dan **terbit sebagai pratinjau nyata** (server sesi, alamat dicatat di
  `uji-b3.md`). **Tahap 7 (Serah Terima) dijalankan sebagai LATIHAN** — lihat `uji-b3.md`. Catatan versi terbit: `catatan-versi.md` **v1**. Uji render otomatis **30/30 lulus**; alat baru `_sistem/validate_unit.py` **rc=0** (diuji mutasi 3/3); flyer & QR **sinkron** dengan rekaman data (rc=0).
- **Pekerjaan berikutnya setelah berkas ini tersimpan (BUKAN pekerjaan belum tersimpan):** (1) **pemeriksaan pemilik di HP** — daftar periksa Terbit butir 1/2/7/8, flyer butir 9, pengalaman amplop (`uji-b3.md` bagian 2–4); (2) **deploy Cloudflare fase 1 oleh pemilik** (Tahap 6 yang sesungguhnya; lingkungan sesi ini diblokir dari Cloudflare); (3) **uji rekening nyata** (baca balik digit per digit + cross-check G5) saat ada client; (4) **alat G3 (hitung DPI efektif + `Lanczos4`) belum dibuat** — unit ini 0 aset raster, jadi gerbang resolusi belum teruji; (5) **butir 6 daftar periksa Serah Terima** (catatan serah terima) ditulis sesudah (1) beres
- **Tahap berikutnya:** (a) **pemilik menjalankan 4 langkah di `uji-b3.md` bagian 7** (periksa di HP → jalur uji amplop & personalisasi → flyer → **deploy Cloudflare**); (b) **deploy Cloudflare fase 1 dijalankan PEMILIK** mengikuti
  `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` bagian 4 (lingkungan sesi ini tidak bisa menembus
  Cloudflare — item terbuka yang sudah tercatat); (c) sesudah itu dokumen 09 bagian 4/6 **dinyatakan
  terbukti** untuk langkah yang benar-benar dijalankan, dan sisanya dinyatakan apa adanya.
- **Sumber konteks yang dibaca:** `00_RENCANA_KERANGKA.md` (siklus 7 tahap · gerbang G0–G5 · kebijakan
  domain 3 fase) · `01_IDENTITAS_PEMILIK.md` (merek, font, palet, nada, serah terima) ·
  `02_PROFIL_JENIS_ACARA.md` (pernikahan: field, konvensi, pantangan) · `03_TEMPLATE_DATA_ACARA.md`
  (skema + gerbang data) · `04_TEMPLATE_BRIEF_UNDANGAN.md` (brief) · `05_DISCOVERY_DESAIN_PROMPT.md`
  (batas janji, menu arah, format) · `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` (Langkah 0, dua tingkat aset,
  G3, bukti per aset) · `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` (langkah terbit + 2 daftar periksa) ·
  `11_AMPLOP_DIGITAL.md` (kapan tampil/tidak, titik verifikasi) · `_sistem/validate_unit.py` (gerbang data)
- **Log keputusan unit:** `log-keputusan-unit.md` (termasuk penyimpangan yang dinyatakan sadar)
- **Bukti uji:** `uji-b3.md` (daftar periksa Terbit 10 butir · Serah Terima 7 butir · amplop 5 butir —
  diisi **apa adanya**, termasuk yang belum bisa diuji dari lingkungan ini)

## Catatan bukti yang tidak boleh dibaca sebagai lebih dari kenyataannya

1. **Aset raster = 0 pada uji coba ini.** Undangan dibangun **tanpa foto** (sah per `02` bagian 6:
   *"tanpa foto = sah → desain ornament-driven"*). Artinya **gerbang resolusi G3 tidak teruji pada
   uji coba ini** — yang teruji hanya aturan **bukti per aset** (alat `validate_unit.py` menolak aset
   raster yang tidak punya baris di `web/aset/daftar-aset.json`). **Alat hitung DPI efektif + `Lanczos4`
   belum dibuat** dan tetap terbuka.
2. **Amplop digital tidak diaktifkan** (putusan E3): rekening pemilik belum ada, dan nomor rekening
   nyata tidak layak ditaruh di repo. Yang diuji: aturan **"data kosong → bagian tidak dirender"**,
   ditambah jalur uji `?uji=amplop` yang memakai nomor **jelas fiktif** + berlabel UJI COBA di layar.
   **Uji rekening nyata (baca balik digit per digit + cross-check G5) tetap BELUM dijalankan.**
3. **Terbit = pratinjau nyata dari sesi ini**, bukan Cloudflare. Deploy fase 1 dijalankan pemilik
   (dokumen 09 bagian 4). Sampai itu, kalimat "undangan sudah terbit di `lee-studio.pages.dev/...`"
   **belum boleh** diucapkan.
4. **CMS/panel & penyimpanan ucapan/RSVP yang sebenarnya** belum ada (dokumen 10 ditunda) — mode uji
   memakai penyimpanan sementara di perangkat tamu dan **ditandai jelas** di layar.
