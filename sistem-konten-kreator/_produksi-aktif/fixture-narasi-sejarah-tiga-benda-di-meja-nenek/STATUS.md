# Status Produksi — Narasi Sejarah (fixture) — Tiga Benda di Meja Nenek

> **FIXTURE UJI** untuk AT-KK-05/05b (`sistem-konten-kreator/ACCEPTANCE_TESTS.md`). Mengikuti `_sistem/STATUS_TEMPLATE.md` versi 2026-09-04 (approval per kode gerbang + field sumber eksternal).

- **Status:** `in-progress`
- **Channel:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/` (v1, `Operational`)
- **Model konten:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md` (v1, `Operational`)
- **Tahap terakhir selesai:** Tahap 4 — Breakdown Output (**dikunci G2**, 9 segmen). Disusun sebagai draft, lalu disetujui sebagai dasar Tahap 5.
- **Tahap berikutnya:** Tahap 5 — Generate/Acquire Assets (kumpulkan b-roll/foto berlisensi per segmen; bukan generate karakter). Menunggu G1 Tahap 4 sebelum eksekusi nyata.
- **Output resmi:**
  - `naskah-draft.md` — **ADA** di folder ini (draft Tahap 3, belum G2 final)
  - `breakdown-output.md` — **ADA** di folder ini (**draft** Tahap 4, belum G2)
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
  - `G2 naskah final (Tahap 3):` **disetujui 2026-09-04** — naskah `naskah-draft.md` dikunci sebagai naskah final
  - `G1 Tahap 4 (Breakdown):` **belum** — G2 breakdown sudah disetujui; G1 lanjut ke Tahap 5 diminta sebelum eksekusi
  - `G2 breakdown (Tahap 4):` **disetujui 2026-09-04** — `breakdown-output.md` (9 segmen) dikunci sebagai dasar generate/acquire asset
  - `G3 merge:` belum
- **Commit terakhir:** `e2d234d65f04802fbdcf4ba9d17dec55c83dd7cb` — commit yang menyimpan **output produksi** (`breakdown-output.md`) di sesi ini. Verifikasi: `git log -1 --format=%H -- sistem-konten-kreator/_produksi-aktif/fixture-narasi-sejarah-tiga-benda-di-meja-nenek/breakdown-output.md`. *(Field ini menunjuk commit output, bukan commit `STATUS.md` sendiri.)*
- **PR terkait:** tidak ada
- **Pekerjaan belum tersimpan:** `Tidak ada`
- **Risiko atau blocker:** Naskah **belum** berstatus final. G1 Tahap 3 hanya izin melanjutkan, bukan penguncian isi (lihat definisi G1/G2 di `_sistem/00_CARA_PAKAI_SISTEM.md`). `breakdown-output.md` saat ini **draft** — tidak boleh dikunci atau dipakai untuk generate asset sebelum **G2 naskah final** dan **G2 breakdown** diberikan. Tahap 5 hanya mengumpulkan b-roll/foto berlisensi, bukan generate karakter.
- **Waktu pembaruan:** 2026-09-04

## Aturan

- Perbarui file ini setelah setiap tahap yang menghasilkan dependency baru.
- Jangan menyatakan tahap tersedia untuk sesi berikutnya sebelum output sudah tersimpan di branch.
- Jika status atau output tidak dapat diverifikasi setelah sesi terputus, berhenti dan minta klarifikasi.
