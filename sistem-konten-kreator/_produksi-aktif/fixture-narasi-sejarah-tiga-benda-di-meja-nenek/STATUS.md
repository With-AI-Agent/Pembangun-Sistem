# Status Produksi — Narasi Sejarah (fixture) — Tiga Benda di Meja Nenek

> **FIXTURE UJI** untuk AT-KK-05/05b. State awal Tahap 3 disiapkan ulang 2026-09-05 melalui PR #12; recovery sesi `arena/01a073cf-pembangun-sistem` memverifikasi output yang ada lalu menyiapkan **draft Tahap 4**, bukan mengulang naskah. Catatan recovery dan laporan awal: `LOG_SESI_2026-09-05_4.md` di root repo. Ini bukan klaim acceptance test LULUS atau produksi final.

- **Status:** `ready-for-review`
- **Channel:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/` (v1, `Operational`; brief terverifikasi ada di `origin/main` saat entry point)
- **Model konten:** `sistem-konten-kreator/channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md` (v1, `Operational`)
- **Tahap terakhir selesai:** penyusunan **draft Tahap 4 — Breakdown Output**, 7 segmen narasi yang mencakup seluruh 144 kata naskah tanpa perubahan. Tahap 4 belum lolos G1/G2; Tahap 3 tetap belum dikunci sebagai naskah final (G2 belum).
- **Tahap berikutnya:** keputusan **G2 naskah final (Tahap 3)**, termasuk penanganan temuan durasi; kemudian review **G1 dan G2 breakdown (Tahap 4)** secara eksplisit. **Tahap 5 tertahan** sampai dependency tersebut terpenuhi.
- **Output resmi:** *(daftar file persisten, bukan penanda approval isi)*
  - `naskah-draft.md` — **ADA**, draft Tahap 3 asli tetap utuh, 144 kata; **belum final/G2**
  - `breakdown-output.md` — **ADA**, draft Tahap 4, 7 **segmen narasi**; **belum G1/G2**, bukan dasar acquire yang dikunci
  - `assets/` — **BELUM ADA**; Tahap 5 belum dimulai, bukan dilewati sebagai teks-only
- **Sumber konteks yang dibaca:**
  - `_sistem/START_DI_SINI.md` dan `_sistem/00_CARA_PAKAI_SISTEM.md`
  - `_sistem/01_BRAND_CORE.md` — **masih template kosong**, gap fixture dilaporkan; tidak diisi atau dianggap lengkap
  - `channel-fixture-narasi-sejarah/channel-brief.md` — termasuk Persona & Voice, konsistensi dan larangan visual; dibaca ulang pada checkpoint Tahap 4
  - `channel-fixture-narasi-sejarah/model-konten/narasi-60-detik/brief.md` — unit segmen narasi, acquire b-roll berlisensi; dibaca ulang sebelum breakdown
  - `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md` — gerbang per tahap, fact-check dan rights-check
  - `_sistem/06_PROMPT_LIBRARY.md` — dibaca, checkpoint/chaining diterapkan
  - `_sistem/STATUS_TEMPLATE.md`
  - `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` di root repo — dibaca, terutama Recovery saat sesi baru
  - `channel-fixture-narasi-sejarah/arsip-naskah/indeks.md` dan `indeks-karakter.md` — ada dan kosong; tidak ada entri baru atau promosi karakter
  - `naskah-draft.md` — dibaca ulang dari file, bukan dari ingatan; commit sumber diverifikasi saat entry point
  - Bank Konsistensi Visual dilewati secara sadar: brief/model tidak mewajibkan elemen acuan; tidak ada karakter visual baru
- **Sumber eksternal dipakai:** `Tidak ada` — naskah personal dummy fixture; detail pukul lima bukan klaim sejarah hasil riset. B-roll/VO baru direncanakan, belum diperoleh. `SUMBER.md` wajib dibuat sejak bahan eksternal pertama benar-benar dipakai nanti; tidak mengklaim stok atau lisensi sudah tersedia.
- **Keputusan baru:**
  - Angle dari checkpoint lama tetap: pintu masuk cerita adalah radio tua, bukan meja secara keseluruhan. Tidak mengulang Tahap 1–3 atau menambah dua benda untuk memaksakan judul kerja.
  - Pengguna di sesi lama menyebut naskah "sudah oke, sudah dikonfirmasi" tanpa kode gerbang. Pernyataan itu **tetap bukan approval G2/G3**.
  - Instruksi pengguna 2026-09-05: lanjut produksi sampai gerbang keputusan, commit+push tiap tahap, PR tanpa auto-merge. Ini izin recovery/penyiapan draft, **bukan** penguncian naskah/breakdown atau izin merge.
  - Draft breakdown dibuat dengan izin G1 Tahap 3 yang sudah tercatat. Seluruh pemenggalan, timing, dan arahan acquire masih usulan; perubahan naskah atau brief harus diputuskan dahulu oleh pengguna.
- **Approval yang sudah diberikan:**
  - `G1 Tahap 1 (Ideation):` disetujui 2026-09-04
  - `G1 Tahap 2 (Konsep & Angle):` disetujui 2026-09-04
  - `G1 Tahap 3 (Naskah/Script):` disetujui 2026-09-04 — hanya izin lanjut; naskah sumber tidak diubah pada recovery ini
  - `G2 naskah final (Tahap 3):` **belum** — gerbang yang perlu keputusan pengguna sekarang
  - `G1 Tahap 4 (Breakdown Output):` **belum** — draft tersedia untuk review, tidak dianggap diterima
  - `G2 breakdown (Tahap 4):` **belum** — menunggu naskah final dan review breakdown
  - `G1 Tahap 5 (Assets):` belum — tahap belum dimulai
  - `G2 konten final + metadata (Tahap 6):` belum — tahap belum dimulai
  - `G3 merge:` **belum** — pengguna melarang auto-merge
- **Commit terakhir:** `706060d391753e97954a49ccd6275ec8d061ff22` — commit naskah sumber yang sudah diverifikasi sebelum recovery. SHA commit draft breakdown akan dicatat pada checkpoint setelah output baru di-commit; verifikasi masing-masing dengan `git log -1 --format=%H -- [path output]`, bukan memakai commit STATUS sendiri.
- **PR terkait:** belum ada pada checkpoint penyusunan draft; akan dibuka sebagai PR draft untuk review, bukan approval merge
- **Pekerjaan belum tersimpan:** Tidak ada
- **Risiko atau blocker:**
  - **G2 naskah final belum diberikan**; tidak boleh mengunci breakdown, membuat/mengambil aset, mengarsipkan naskah final, atau menganggap konten siap publish. G1/G2 breakdown juga belum diberikan; G3 terpisah.
  - **Durasi belum sesuai brief:** hitungan VO 144 kata pada 130 kata/menit ≈66,46 detik tanpa jeda, atau ≈69,46 detik dengan enam jeda antarseggmen 0,5 detik. Batas model 55–65 detik; waktu ini estimasi, bukan hasil audio terukur. Rekomendasi untuk diputuskan: revisi draft naskah dahulu (tanpa mengubah voice/angle), lalu review ulang. Melonggarkan durasi atau mengubah tempo/brief memerlukan G2 tersendiri; belum diusulkan sebagai keputusan terkunci.
  - Judul kerja menyebut tiga benda, tetapi naskah berfokus pada radio. Jangan menetapkannya sebagai judul publish yang menjanjikan tiga pembahasan tanpa review metadata.
  - Brand Core belum terisi; channel ini fixture, bukan bukti kesiapan produksi nyata. Belum ada asset atau hak/lisensi yang diverifikasi.
- **Waktu pembaruan:** 2026-09-05 — recovery terverifikasi; draft Tahap 4 disimpan, menunggu keputusan G2 naskah final

## Aturan

- Perbarui file ini setelah setiap tahap yang menghasilkan dependency baru.
- Jangan menyatakan tahap tersedia untuk sesi berikutnya sebelum output sudah tersimpan di branch dan di-push.
- Jika status atau output tidak dapat diverifikasi setelah sesi terputus, berhenti dan minta klarifikasi; jangan membuat ulang atau mengoreksi klaim output diam-diam.
- Semua approval dicatat per kode gerbang. G1 tidak naik otomatis menjadi G2 atau G3.
