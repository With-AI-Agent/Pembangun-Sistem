# Status Produksi — Narasi Sejarah (fixture) — Tiga Benda di Meja Nenek

> **FIXTURE UJI** untuk AT-KK-05/05b (`sistem-konten-kreator/ACCEPTANCE_TESTS.md`). Mengikuti `_sistem/STATUS_TEMPLATE.md` versi 2026-09-05 (approval per kode gerbang + field sumber eksternal + field checkpoint). State Tahap 3 ini **disiapkan ulang 2026-09-05** (gulung-ulang dari hasil Run 2/3; lihat `UJI_F7_CLEAN_RUN_2026-09-05.md`).

- **Status:** `in-progress`
- **Channel:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/` (v1, `Operational`)
- **Model konten:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md` (v1, `Operational`)
- **Tahap terakhir selesai:** Tahap 3 — Naskah/Script. Draft naskah selesai (144 kata, target model 130-145) dan tersimpan sebagai file.
- **Tahap berikutnya:** Tahap 4 — Breakdown Output. Bentuk unit: **segmen narasi** (ditetapkan di Model Konten Brief bagian 4), file target `breakdown-output.md`.
- **Output resmi:**
  - `naskah-draft.md` — **ADA** di folder ini
  - `breakdown-output.md` — **BELUM ADA** (Tahap 4 belum pernah dijalankan)
  - `assets/` — **BELUM ADA** (Tahap 5 belum pernah dijalankan)
- **Sumber konteks yang dibaca:**
  - `_sistem/01_BRAND_CORE.md` — dibaca, tapi **masih template kosong**; repo ini belum punya Brand Core terisi
  - `channel-fixture-narasi-sejarah/channel-brief.md`
  - `channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md`
  - `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md` (tabel gerbang per tahap)
  - `_sistem/06_PROMPT_LIBRARY.md`
  - `channel-fixture-narasi-sejarah/arsip-naskah/indeks.md` dan `indeks-karakter.md` — keduanya ada dan masih kosong
- **Sumber eksternal dipakai:** `Tidak ada`
- **Keputusan baru:**
  - Angle dikunci: pintu masuk cerita adalah radio tua, bukan meja secara keseluruhan.
  - Pengguna menyebut naskah ini "sudah oke, sudah dikonfirmasi" di sesi sebelumnya. **Pernyataan itu tidak disertai kode gerbang**, jadi tidak dicatat sebagai approval apa pun.
- **Approval yang sudah diberikan:**
  - `G1 Tahap 1 (Ideation):` disetujui 2026-09-04
  - `G1 Tahap 2 (Konsep & Angle):` disetujui 2026-09-04
  - `G1 Tahap 3 (Naskah/Script):` disetujui 2026-09-04
  - `G2 naskah final (Tahap 3):` **belum**
  - `G2 breakdown (Tahap 4):` belum — tahapnya belum dijalankan
  - `G3 merge:` belum
- **Commit terakhir:** `706060d391753e97954a49ccd6275ec8d061ff22` — commit terakhir yang menyimpan **output produksi** (`naskah-draft.md`). Verifikasi: `git log -1 --format=%H -- sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/naskah-draft.md`. *(Field ini sengaja menunjuk commit output, bukan commit `STATUS.md` sendiri — `STATUS.md` berubah lebih sering, jadi angka di sini tidak perlu ikut berubah setiap status diperbarui.)*
- **PR terkait:** tidak ada
- **Pekerjaan belum tersimpan:** `Tidak ada`
- **Risiko atau blocker:** Naskah **belum** berstatus final. G1 Tahap 3 hanya izin melanjutkan, bukan penguncian isi (lihat definisi G1/G2 di `_sistem/00_CARA_PAKAI_SISTEM.md`). Breakdown Tahap 4 boleh disiapkan sebagai draft, tapi tidak boleh dikunci atau dipakai untuk generate asset sebelum G2 naskah final diberikan.
- **Waktu pembaruan:** 2026-09-05

## Aturan

- Perbarui file ini setelah setiap tahap yang menghasilkan dependency baru.
- Jangan menyatakan tahap tersedia untuk sesi berikutnya sebelum output sudah tersimpan di branch.
- Jika status atau output tidak dapat diverifikasi setelah sesi terputus, berhenti dan minta klarifikasi.
