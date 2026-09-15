# Status Produksi — Kisah Sudut Kota — Warung Kopi yang Pindah Tiga Kali

- **Status:** `in-progress`
- **Channel:** Kisah Sudut Kota (`sistem/sistem-konten-kreator/channel-fixture-kisah-sudut-kota/`, Channel Brief **v3**)
- **Model konten:** Kartu Teks 8–10 **v1 `Approved`** (G2-a 2026-09-15) — kerangka standar + override ringan, unit = kartu teks
- **Tahap terakhir selesai:** Tahap 2 Konsep & Angle (**G1 disetujui** 2026-09-15); Tahap 3 naskah r1 **ditulis + terverifikasi skrip, menunggu G1 + G2**
- **Tahap berikutnya:** G1+G2 Tahap 3 → Tahap 4 Breakdown (unit kartu teks)
- **Output resmi:**
  - `ideation.md` (Tahap 1 — 4 opsi + cek arsip + ide terpilih, G1 disetujui)
  - `konsep-angle.md` (Tahap 2 — angle + hook + peta 9 kartu + kepatuhan batasan; **G1 disetujui**)
  - `naskah-draft.md` (Tahap 3 — naskah r1, 9 kartu, 179 kata; **menunggu G1 + G2**)
  - `cek-kartu.py` (pemeriksa batas model — PASS, sudah diuji-mutasi)
  - `breakdown-output.md` — belum (unit: kartu teks)
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
  - `G1 Tahap 3 (Naskah):` belum
  - `G2 naskah final:` belum
  - `G1 Tahap 4 (Breakdown):` belum
  - `G2 breakdown:` belum
  - `Tahap 5:` tidak berlaku (konten teks-only)
  - `G2 konten final:` belum
  - `G3 merge:` belum
- **Commit terakhir:** (diisi saat commit)
- **PR terkait:** belum ada
- **Pekerjaan belum tersimpan:** Tidak ada
- **Risiko atau blocker:** tidak ada
- **Waktu pembaruan:** 2026-09-15

## Aturan

- Perbarui file ini setelah setiap tahap yang menghasilkan dependency baru.
- Jangan menyatakan tahap tersedia untuk sesi berikutnya sebelum output sudah tersimpan di branch.
- Jika status atau output tidak dapat diverifikasi setelah sesi terputus, berhenti dan minta klarifikasi.
- Field `Pekerjaan belum tersimpan`: nilai WAJIB EXACT `Tidak ada` (case-sensitive, tanpa backtick); jika ada yang belum tersimpan, isi daftar path-nya.
