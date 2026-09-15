# Status Produksi — Kisah Sudut Kota — Warung Kopi yang Pindah Tiga Kali

- **Status:** `ready-for-review`
- **Channel:** Kisah Sudut Kota (`sistem/sistem-konten-kreator/channel-fixture-kisah-sudut-kota/`, Channel Brief **v3**)
- **Model konten:** Kartu Teks 8–10 **v1 `Approved`** (G2-a 2026-09-15) — kerangka standar + override ringan, unit = kartu teks
- **Tahap terakhir selesai:** **seluruh 6 tahap selesai** (Tahap 5 tidak berlaku — teks-only). **G2 konten final + metadata disetujui 2026-09-15**
- **Tahap berikutnya:** **PR #60 terbuka (MERGEABLE, tanpa auto-merge)** → review independen → **G3 merge = keputusan pemilik** → folder produksi dihapus setelah konten dipakai/diunduh
- **Output resmi:**
  - `ideation.md` (Tahap 1 — 4 opsi + cek arsip + ide terpilih, G1 disetujui)
  - `konsep-angle.md` (Tahap 2 — angle + hook + peta 9 kartu + kepatuhan batasan; **G1 disetujui**)
  - `naskah-draft.md` (Tahap 3 — naskah **FINAL** G2 dikunci, 9 kartu, 179 kata)
  - `breakdown-output.md` (Tahap 4 — 9 kartu teks, 0 asset; **G1 + G2 disetujui**)
  - `publish-prep.md` (Tahap 6 — 5 opsi judul + caption + hashtag + tanpa thumbnail; **G2 disetujui**)
  - arsip: naskah + metadata + entri indeks (**ditulis, G2 disetujui**)
  - `cek-kartu.py` (pemeriksa batas model + breakdown — PASS, keduanya sudah diuji-mutasi)
  - `assets/` — **tidak akan ada**: konten teks-only, Tahap 5 tidak berlaku
- **Sumber konteks yang dibaca:** `channel-fixture-kisah-sudut-kota/channel-brief.md` v3, `model-konten/kartu-teks-8-10/brief.md` v1, `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md`, `_sistem/06_PROMPT_LIBRARY.md`, `_sistem/01_BRAND_CORE.md` (masih generator kosong — gap dilaporkan), `arsip-naskah/indeks.md` (1 entri), `arsip-naskah/indeks-karakter.md` (1 entri). **Bank Konsistensi Visual dilewati — channel tidak mengunci elemen visual apa pun dan model ini teks-only tanpa gambar.**
- **Sumber eksternal dipakai:** Tidak ada
- **Keputusan baru:**
  - Unit produksi ditempatkan di **`_produksi-aktif/` root**, bukan `sistem/sistem-konten-kreator/_produksi-aktif/` — mengikuti pola pasca-housekeeping PR #57 (sama seperti `kata-data-2-jam-sekali-jalan` dan `kamu-tau-ga-tutup-panci-lubang-kecil`). Konsekuensi yang dinyatakan sadar: `validate_system.py` baris 186 hanya memindai `_produksi-aktif` di dalam folder sistem, jadi unit ini **di luar cakupan validator** — gap tooling pra-ada yang sudah dicatat `LOG_SESI_2026-09-15_3.md` baris 110, di luar scope PR konten.
  - Produksi dijalankan sebelum brief model `Merged` (masih `Approved`) — sesuai instruksi pemilik dan preseden PR #54 / PR #58. Status `Approved` dipertahankan, tidak dinaikkan jadi `Operational` sebelum merge.
  - Angka "tiga kali" diperlakukan sebagai premis naratif dari Bank Ide Awal channel (bukan klaim faktual) — alasan tercatat di `ideation.md`.
- **Approval yang sudah diberikan:**
  - `G1 Tahap 1 (Ideation — ide "Warung kopi yang pindah tiga kali tanpa ganti nama"):` disetujui 2026-09-15
  - `G1 Tahap 2 (Konsep & Angle — peta 9 kartu):` disetujui 2026-09-15
  - `G1 Tahap 3 (Naskah):` disetujui 2026-09-15
  - `G2 naskah final (9 kartu, 179 kata):` disetujui 2026-09-15
  - `G1 Tahap 4 (Breakdown — 9 kartu teks):` disetujui 2026-09-15
  - `G2 breakdown:` disetujui 2026-09-15
  - `Tahap 5:` tidak berlaku (konten teks-only) — 0 asset, tercatat di sini sebagai keputusan sadar
  - `G2 konten final + metadata:` disetujui 2026-09-15
  - `G3 merge:` belum — PR tanpa auto-merge, merge = keputusan pemilik
- **Commit terakhir:** lihat `git log --oneline origin/main..HEAD` (branch `arena/01a0a448-pembangun-sistem`)
- **PR terkait:** **PR #60** (OPEN, MERGEABLE, tanpa auto-merge) — https://github.com/With-AI-Agent/Pembangun-Sistem/pull/60
- **Pekerjaan belum tersimpan:** Tidak ada
- **Risiko atau blocker:** tidak ada
- **Waktu pembaruan:** 2026-09-15 (PR #60 terbuka — menunggu G3)

## Aturan

- Perbarui file ini setelah setiap tahap yang menghasilkan dependency baru.
- Jangan menyatakan tahap tersedia untuk sesi berikutnya sebelum output sudah tersimpan di branch.
- Jika status atau output tidak dapat diverifikasi setelah sesi terputus, berhenti dan minta klarifikasi.
- Field `Pekerjaan belum tersimpan`: nilai WAJIB EXACT `Tidak ada` (case-sensitive, tanpa backtick); jika ada yang belum tersimpan, isi daftar path-nya.
