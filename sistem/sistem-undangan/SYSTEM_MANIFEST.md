# System Manifest — Sistem Undangan

> Manifest ini adalah kartu identitas dan kontrak navigasi sebuah sistem domain. Ini bukan pengganti dokumen instruksi atau living document.

## Identitas

- **Nama sistem:** `sistem-undangan`
- **Tujuan utama:** mengubah **info acara + identitas pemilik** menjadi undangan **multi-format** (laman web, video, flyer, siap cetak) yang **konsisten dari satu sumber data**, sampai **terbit dan diserahkan ke client** — dipandu agent supaya pemilik yang tidak punya latar coding tidak perlu memikirkan hal teknis.
- **Pengguna/consumer:** pemilik repo (operator, **tidak punya basic coding**) + **client** penerima akhir undangan (tamu melihat hasilnya).
- **Pemilik keputusan:** pemilik repo.
- **Versi:** `0.6.0`
- **Tahap:** `draft` — `01_IDENTITAS_PEMILIK.md` terisi (**G0 LULUS** 20 Sep 2026, dinyatakan pemilik) + `02_PROFIL_JENIS_ACARA.md` terisi jenis acara pertama: pernikahan (**G1 LULUS 20 Sep 2026 — putusan pemilik via merge PR #88 `f60e950`, 16:48 UTC**) + `03_TEMPLATE_DATA_ACARA.md` terisi (**roadmap b1 (1/2), template biasa** — penurunan dari field L2 pernikahan; review isi pemilik selesai 20 Sep 2026 (PR #90) + **PR #90 MERGED `de9bd12` (20 Sep 2026 23:59:25 UTC) → b1 LULUS**) + `04_TEMPLATE_BRIEF_UNDANGAN.md` terisi (**roadmap b1 (2/2), template biasa** — brief Tahap 1–2; review isi pemilik selesai 20 Sep 2026 (PR #90) + **PR #90 MERGED `de9bd12` → b1 LULUS**); ubah ke `siap-pakai` saat sistem siap dipakai (cek W-01/W-02/W-03 kembali ketat; lihat `03_KONTRAK_WARISAN.md` bagian "Tahap pembangunan")
- **Status:** `Draft`
- **Tanggal dibuat:** 2026-09-17
- **Audit terakhir:** belum ada — **G0 LULUS 20 Sep 2026** (review isi lengkap oleh pemilik + PR #86 merged, `36c63d4`); **G1 (isi L2 pernikahan) LULUS 20 Sep 2026 — putusan pemilik via merge PR #88 (`f60e950`, 16:48 UTC)**; sifat putusan direkam jujur di log sesi slot 43 (dasar = approval butir-per-butir di chat, tanpa review dalam tersendiri; audit independen pasca-merge tersedia atas permintaan pemilik); benturan klasifikasi G1 (prompt 02 BESAR vs manifest Kecil vs rencana kerangka bagian 4 gerbang produksi-Sedang) **diputus pemilik: dibiarkan pada keadaan tercatat** — tidak memblokir, bisa dibuka lewat Log Keputusan dokumen 02; **roadmap b1 tuntas sampai draft 20 Sep 2026 (UTC): `03_TEMPLATE_DATA_ACARA.md` + `04_TEMPLATE_BRIEF_UNDANGAN.md` terisi (template biasa, tanpa keputusan baru pemilik; draft menunggu review isi PR)** — benturan label G2 (manifest vs 00 bagian 4) dilaporkan di Log Keputusan dokumen 04, tidak diputus sepihak; audit independen isi L1: terbuka atas permintaan pemilik; kelulusan pegangan W-01 menunggu jalur audit-nya sendiri (Syarat 4); **review isi PR b1 (03+04) dijalankan PEMILIK 20 Sep 2026 (sesi slot 44, log sesi): "setuju semua rekomendasi" — benturan label G2 DISelaraskan (baris Titik approval Besar di atas mengikuti 00 bagian 4) + baris Acceptance pegangan dikoreksi (fakta basi, koreksi 20 Sep 2026); draft menunggu merge PR #90 (tanpa auto-merge)**; **b1 LULUS 21 Sep 2026 — PR #90 MERGED `de9bd12` (20 Sep 2026 23:59:25 UTC); sync pasca-merge dijalankan sesi slot 45 (register T-18, STATUS.md, INDEKS, log sesi slot 45) — Versi TIDAK di-bump (tetap 0.6.0; preseden G1 LULUS dokumen 02 yang tidak menaikkan versi 0.4.0)**
- **Quality protocol:** **BELUM DIBUAT** di tahap kerangka. Direncanakan sebagai `QUALITY_ASSURANCE_AND_EVOLUTION.md` DI DALAM folder sistem ini (butir W-06 — wajib self-contained). Rujukan ke _meta/QUALITY_ASSURANCE_AND_EVOLUTION.md hanyalah provenance (asal aturan), BUKAN aturan aktif (sistem harus tetap berfungsi penuh saat foldernya diunduh jadi repo sendiri — lihat `03_KONTRAK_WARISAN.md`)

## Bentuk Sistem

- **Bentuk:** [ ] Bertingkat  [ ] Flat  [ ] Siklus  [x] Gabungan — **BERTINGKAT 3 lapis + SIKLUS 7 tahap** (dikunci pemilik 17 Sep 2026; alasan dan rinciannya di `00_RENCANA_KERANGKA.md` bagian 2)
- **Unit kerja utama:** **satu undangan konkret** (Lapis 3) — dari prompt pembuka sampai terbit & diserahkan
- **Kriteria satu unit selesai:** tayang/terbit + diserahkan ke client (Tahap 7 SIKLUS) + `STATUS.md` unit tertutup + aset & data acara terarsip
- **Titik approval Besar:** **G0** (identitas pemilik/L1), **G2** (desain & format dikunci — diselaraskan 2026-09-20, putusan pemilik, review isi PR #90; mengikuti `00_RENCANA_KERANGKA.md` bagian 4), **G5** (sebelum terbit/serah terima), dan **perubahan apa pun di L1** — semuanya **review isi lengkap oleh pemilik**
- **Titik approval Kecil:** **G1** (profil jenis acara/L2), **G3** (gerbang aset & resolusi), **G4** (pratinjau desain per format) — boleh diwakilkan agent dengan pencatatan

## Dokumen Navigasi

- **Entry point:** `PROMPT_ENTRI_UNIVERSAL.md` (W-01) — **sudah dibuat 18 Sep 2026**, jadi entry point tidak lagi sementara. Untuk memakai sistem: tempel blok prompt di berkas itu. Untuk memahami rancangan sistem: `00_RENCANA_KERANGKA.md` + `STATUS.md`. Untuk pegangan lengkap: `PANDUAN_PENGGUNA.md`
- **Dokumen instruksi aktif:** `01_IDENTITAS_PEMILIK.md` (**isi — G0 LULUS**, 20 Sep 2026); `02_PROFIL_JENIS_ACARA.md` (**isi — G1 LULUS**, jenis acara pertama: pernikahan, 20 Sep 2026); `03_TEMPLATE_DATA_ACARA.md` (**isi — b1 LULUS**, template biasa, 20 Sep 2026 (UTC); PR #90 MERGED `de9bd12`); `04_TEMPLATE_BRIEF_UNDANGAN.md` (**isi — b1 LULUS**, template biasa, 20 Sep 2026 (UTC); PR #90 MERGED `de9bd12`); 7 dokumen domain lainnya masih kerangka
- **Living documents:** `01_IDENTITAS_PEMILIK.md`, `02_PROFIL_JENIS_ACARA.md`, `03_TEMPLATE_DATA_ACARA.md`, `06_SPESIFIKASI_ASET_DAN_RESOLUSI.md`, `10_ARSITEKTUR_WEBSITE_INDUK.md`
- **Log keputusan:** bagian **"Log Keputusan"** di `00_RENCANA_KERANGKA.md` (W-05)
- **Ringkasan cadangan:** **belum ada** — W-09 dikerjakan saat sistem mendekati `siap-pakai`
- **Laporan audit:** **belum ada** — mekanisme tersedia dari meta (tools/audit_prompt.py --objek sistem/sistem-undangan); turunan self-contained di dalam folder belum ada (W-10, item **T-07** di _meta/DAFTAR_PEKERJAAN_TERBUKA.md)
- **Pegangan pengguna:** **SUDAH DIBUAT 18 Sep 2026** — `PANDUAN_PENGGUNA.md` (12 bagian: keadaan sistem dinyatakan terus terang masih kerangka, prompt pembuka, prompt penutup, istilah awam, 3 lapis, 7 tahap + 6 gerbang, bahan milik pemilik, 6 situasi masing-masing dengan 6 bidang, cara review & merge, tabel perintah 5 kolom, kebiasaan, catatan kualitas + Log Keputusan) dan `PROMPT_ENTRI_UNIVERSAL.md` (blok prompt **identik** dengan §2 pegangan — dua file satu sumber, diverifikasi programatik). Ditulis mengikuti Standar Kelulusan Manual 5 syarat. **KELULUSANNYA BELUM DINYATAKAN dan memang tidak boleh dinyatakan di sini** — Syarat 4 melarang penulis menilai sendiri: wajib audit sesi independen (lensa kemudahan pakai) **dan** uji pemakaian nyata oleh pemilik; kalau pemilik harus bertanya saat memakai, standarnya belum lulus dan pertanyaan itu adalah temuan. Alat penjaring repo induk melaporkan **0 kandidat** pada kedua berkas, dengan **kontrol positif** (berkas sistem lain yang pernah bermalasah tetap menjaring 2 dan 4 kandidat) sehingga angka 0 itu bermakna, bukan hampa

## Prinsip

| Prinsip meta-sistem | Berlaku? | Cara diterapkan | Alasan jika di-override |
|---|---|---|---|
| Hierarki | Ya | 3 lapis L1 (Identitas Pemilik) → L2 (Profil Jenis Acara) → L3 (Undangan Konkret); level atas dikunci dulu, bawah mewarisi. Penyimpangan boleh tetapi **wajib tercatat** | — |
| Chaining | Ya | **satu sumber data acara → banyak format** (web, video, flyer, cetak). Ini sebabnya konsistensi data jadi hal paling berbahaya di sistem ini | — |
| Approval bertingkat | Ya | 6 gerbang G0–G5 dalam 3 tingkat risiko (`00_RENCANA_KERANGKA.md` bagian 4) | — |
| Checkpoint & verifikasi | Ya, **diperkuat** | checkpoint **di tiap gerbang**, bukan di akhir — dipaksa fakta platform "tidak bisa push setelah PR merge/close". Penguatan: **gerbang aset G3** dengan 3 hasil terukur (bagian 4.3–4.5) | — |
| Log keputusan | Ya | di `00_RENCANA_KERANGKA.md` + wajib di tiap dokumen hidup dan per unit kerja | — |
| Quality assurance & evolusi (prinsip 6) | Ya | 3 lapis; **batas pentingnya dihormati: audit menghasilkan temuan, tidak otomatis mengubah keputusan yang sudah dikunci** | — |

**Tidak ada prinsip yang di-override.** Pemisahan Konsistensi Visual vs Non-Visual (dinyatakan **tidak universal** oleh meta) **dipakai dengan alasan eksplisit**: domain ini butuh **keduanya** — visual (undangan adalah benda visual) dan skema data (satu sumber → banyak format).

## Warisan (Kontrak)

Status butir `03_KONTRAK_WARISAN.md` untuk sistem ini — disalin dari bagian "Warisan" di `00_RENCANA_KERANGKA.md`; default SEMUA diterapkan, tidak ada yang di-override:

| Butir | Status (diterapkan / override) | Letak di folder sistem | Override? |
|---|---|---|---|
| W-01 pegangan | diterapkan — **berkasnya SUDAH dibuat 18 Sep 2026**; **kelulusannya BELUM dinyatakan** (Standar Kelulusan Manual syarat 4) | `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` — keduanya ADA di folder ini, blok prompt-nya identik | Tidak |
| W-02 LOG_SESI | diterapkan — **berkasnya belum dibuat** (belum ada unit kerja untuk dicatat) | direncanakan `12_LOG_SESI.md` | Tidak |
| W-03 field checkpoint STATUS | diterapkan — **belum ada unit** | direncanakan `STATUS.md` per unit kerja (1 undangan = 1 unit) | Tidak |
| W-04 manifest | **diterapkan — berkas ini** | `SYSTEM_MANIFEST.md` | Tidak |
| W-05 log keputusan | **diterapkan — sudah ada isinya** | bagian "Log Keputusan" di `00_RENCANA_KERANGKA.md` | Tidak |
| W-06 QA 3-lapis | diterapkan — **turunan self-contained belum dibuat** | direncanakan `QUALITY_ASSURANCE_AND_EVOLUTION.md` | Tidak |
| W-07 fakta platform | **diterapkan — bagian "Batasan Platform" di bawah** | berkas ini | Tidak |
| W-08 approval bertingkat | **diterapkan — 6 gerbang terdefinisi** | `00_RENCANA_KERANGKA.md` bagian 4 | Tidak |
| W-09 ringkasan cadangan | diterapkan — **dikerjakan saat mendekati siap-pakai** | direncanakan RINGKASAN di `_cadangan-claude/` | Tidak |
| W-10 audit isi + pengiriman hasil | **diterapkan sebagian** — mekanisme jalan dari meta, **turunan self-contained di dalam folder BELUM ADA** (belum ada di sistem anak mana pun) | item **T-07** di _meta/DAFTAR_PEKERJAAN_TERBUKA.md. **Sistem ini dilarang mengklaim W-10 penuh** sebelum turunannya dibuat | Tidak |

## Quality & Evolution

- **Lapisan self-audit sistem:** direncanakan 3 lapis (dokumen turunan W-06 belum dibuat di tahap kerangka)
- **Lapisan verifikasi output:** **gerbang G0–G5**, dengan **G3 terukur** (PSNR/SSIM + ambang DPI, `00_RENCANA_KERANGKA.md` bagian 4.3–4.5) dan **G4 pratinjau per format**
- **Trigger audit:** perubahan L1 (identitas pemilik) · perubahan ambang/spek teknis · keluhan client · kegagalan berulang · permintaan pemilik
- **Level audit default:** Sedang — **Mendalam** untuk G0, G5, dan perubahan L1
- **Prosedur rollback:** revert commit pada branch sesi; keputusan yang sudah dikunci **hanya** berubah lewat Log Keputusan + approval pemilik, **tidak** lewat hasil audit otomatis
- **Override quality protocol:** Tidak ada

## Dependency dan Risiko

- **Dependency eksternal:** Cloudflare free tier (Pages + Workers + D1 + KV + R2) untuk penerbitan · Remotion untuk video (**jebakan lisensi: gratis hanya ≤3 karyawan**, alternatif MIT/Apache sudah diriset) · `Pillow`/`OpenCV` untuk `Lanczos4` di gerbang aset · **opsional** `cv2.dnn_superres` + FSRCNN/ESPCN (keluar dari jalur kritis — lihat `00_RENCANA_KERANGKA.md` bagian 4.5)
- **Data yang wajib ada:** identitas pemilik (L1) · profil jenis acara (L2) · data acara per undangan (L3) · aset dengan **provenance dan ukuran DPI terukur**
- **Risiko utama:** (1) **inkonsistensi antar-format** karena satu sumber data dipakai banyak keluaran; (2) **aset kurang resolusi** lolos ke cetak — sudah dipagari G3 terukur; (3) **tautan yang sudah disebar ke tamu mati** saat naik fase domain — dipagari syarat *path wajib stabil lintas fase*; (4) **client non-coder tidak bisa merawat** sesudah serah terima; (5) sesi terputus sebelum checkpoint (fakta platform)
- **Batasan yang diketahui:** lingkungan kerja **tidak punya** font sistem, ffmpeg, chromium, ghostscript, ImageMagick-PDF; `pip install` **tidak bertahan antar sesi**; **semua API layanan eksternal terblokir** (hanya npm, PyPI, github.com, api.github.com, codeload.github.com); `raw.githubusercontent.com` **diblokir**
- **Prosedur recovery:** checkpoint di tiap gerbang + commit/push segera + `12_LOG_SESI.md` (sesudah dibuat) sebagai jalur pemulihan konteks

## Batasan Platform

- **Dipakai via lmarena?** Ya
- **Jika Ya:** fakta platform **disalin ke dalam folder ini** supaya sistem tetap berfungsi saat foldernya diunduh jadi repo sendiri (W-07 self-contained): branch arena otomatis dibuat; **tidak bisa push setelah PR merge/close** (platform mencabut akses); sesi bisa crash kapan saja; **riwayat git lokal bisa ter-reset/shallow DI TENGAH sesi** — pemulihan: `git fetch --unshallow --prune` lalu `git reset --mixed <sha-remote>`, **jangan** `pull --rebase`, **jangan** `--allow-unrelated-histories`; allowlist jaringan hanya npm/PyPI/GitHub; **aset wajib dibundel lokal**; **waktu-pakai ≠ waktu-bangun**. Terapkan **checkpoint tiap tahap** + **log sesi berkelanjutan** — tanpa commit+push sesi baru tidak bisa melanjutkan (FI-03), dan tanpa log sesi konteks (keputusan, koreksi, fakta penting) hilang permanen saat crash.
- **Jika Tidak:** —

## Acceptance

- [ ] Semua dokumen wajib tersedia — **belum: 7 dokumen masih kerangka + 4 terisi (01 — G0 LULUS; 02 — G1 LULUS, jenis acara pernikahan; 03 + 04 — **b1 LULUS**, PR #90 MERGED `de9bd12`)**
- [ ] Semua dependency valid — **sebagian: dependency penerbitan belum diuji dari lingkungan ini**
- [x] Status dan versi sudah diperbarui
- [x] Approval yang diperlukan sudah ada — **konfirmasi final pemilik 17 Sep 2026 untuk rencana kerangka (kategori BESAR)**
- [ ] Audit terakhir tercatat — **belum ada isi untuk diaudit**
- [ ] Ringkasan cadangan sinkron — **W-09 dikerjakan saat mendekati siap-pakai**
- [ ] Pegangan pengguna tersedia di dalam folder sistem — **berkasnya SUDAH dibuat 18 Sep 2026** (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md`); **kelulusannya belum dinyatakan** (Standar Kelulusan Manual syarat 4 — penulis tidak menilai sendiri; wajib audit sesi independen + uji pemakaian nyata pemilik) — **syarat naik ke `siap-pakai`**
