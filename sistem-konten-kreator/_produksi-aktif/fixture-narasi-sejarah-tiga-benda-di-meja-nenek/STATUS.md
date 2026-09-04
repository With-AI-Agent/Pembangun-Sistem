# Status Produksi — Narasi Sejarah (fixture) — Tiga Benda di Meja Nenek

> **FIXTURE UJI** untuk AT-KK-05/05b (`sistem-konten-kreator/ACCEPTANCE_TESTS.md`). Mengikuti `_sistem/STATUS_TEMPLATE.md` versi 2026-09-04 (approval per kode gerbang + field sumber eksternal).

- **Status:** `ready-for-review` (Tahap 6 metadata + arsip disiapkan; menunggu G2 konten final + G3 merge)
- **Channel:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/` (v1, `Operational`)
- **Model konten:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md` (v1, `Operational`)
- **Tahap terakhir selesai:** Tahap 6 — Assembly & Publish Prep (metadata disiapkan; naskah final diarsipkan; indeks diperbarui). Tahap 5 **dilewati sadar** — fixture uji, tidak menghasilkan/meng-akuisi asset nyata.
- **Tahap berikutnya:** G2 konten final + G3 merge. Setelah G3 dan hasil didownload, folder produksi sementara boleh dihapus.
- **Output resmi:**
  - `naskah-draft.md` — **ADA** di folder ini (final; juga diarsipkan di `channel-fixture-narasi-sejarah/arsip-naskah/2026-09-04-tiga-benda-di-meja-nenek.md`)
  - `breakdown-output.md` — **ADA** di folder ini (**dikunci G2**, 9 segmen)
  - `metadata.md` — **ADA** di folder ini (`_produksi-aktif/.../metadata.md`)
  - `assets/` — **TIDAK ADA** (Tahap 5 dilewati — fixture uji)
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
  - `G1 Tahap 4 (Breakdown):` disetujui 2026-09-04 — breakdown disepakati sebagai dasar Tahap 5
  - `G2 breakdown (Tahap 4):` **disetujui 2026-09-04** — `breakdown-output.md` (9 segmen) dikunci sebagai dasar generate/acquire asset
  - `G1 Tahap 5 (Asset):` — **dianggap tidak diperlukan** (Tahap 5 dilewati sadar pada fixture uji; tidak ada asset yang digenerate)
  - `G2 konten final + metadata (Tahap 6):` **belum** — sedang diminta
  - `G3 merge:` belum
- **Commit terakhir:** `08a2354...` — lihat `git log -1 --format=%H -- sistem-konten-kreator/channel-fixture-narasi-sejarah/arsip-naskah/2026-09-04-tiga-benda-di-meja-nenek.md` setelah commit berikutnya. *(Field ini menunjuk commit output, bukan commit `STATUS.md` sendiri.)*
- **PR terkait:** tidak ada (branch `arena/01a06d25-pembangun-sistem` sudah di-push; PR belum dibuat)
- **Pekerjaan belum tersimpan:** `Tidak ada`
- **Risiko atau blocker:** Naskah **sudah** dikunci G2 (final); breakdown **sudah** dikunci G2. Konten belum di-merge (`G3` belum) dan belum punya asset nyata karena Tahap 5 dilewati — konten ini murni fixture uji, tidak untuk dipublish. Perlu **G2 konten final + metadata** sebelum G3 merge.
- **Waktu pembaruan:** 2026-09-04

## Aturan

- Perbarui file ini setelah setiap tahap yang menghasilkan dependency baru.
- Jangan menyatakan tahap tersedia untuk sesi berikutnya sebelum output sudah tersimpan di branch.
- Jika status atau output tidak dapat diverifikasi setelah sesi terputus, berhenti dan minta klarifikasi.
