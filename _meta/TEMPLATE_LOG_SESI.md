# Template Log Sesi (LOG_SESI)

> Format untuk file `LOG_SESI_YYYY-MM-DD.md` — ingatan persisten SATU sesi. Agent sesi baru **tidak punya akses ke chat sesi lama**; yang bertahan hanya file di repo. Aturan lengkap: `PROTOKOL_CHECKPOINT_RECOVERY.md` (bagian "Log Sesi Berkelanjutan").
>
> **Lokasi file** = folder scope kerja: unit/deck (`deck-aktif/<deck>/`), sistem (`sistem-[nama]/`), atau folder `_log-sesi/` di root repo (kerja lintas-sistem/level meta — tidak langsung di root). Satu file per sesi; kalau dua sesi sehari, suffix `_2`.
>
> **Anti-bising (WAJIB dipatuhi — ini yang membuat mekanisme ini bukan overkill):**
> - **CATAT:** keputusan/koreksi/kendala/preferensi pengguna (near-verbatim, bukan parafrase bebas); proposal/klaim penting agent + dasarnya (1–3 baris); kesepakatan & penolakan + alasan; fakta/hasil verifikasi yang ditemukan sesi ini; perubahan state kerja; pertanyaan terbuka.
> - **JANGAN CATAT:** konfirmasi ("oke", "siap"), basa-basi, pengulangan isi yang sudah ada di `STATUS.md`/Log Keputusan (tunjuk path-nya), dump chat mentah.
> - **Kapan update:** setelah tiap pertukaran yang menghasilkan INFORMASI BARU (bukan mekanis tiap giliran). Update + commit + push segera.

---

## Template file

```markdown
# Log Sesi — [YYYY-MM-DD] (sesi/branch: [arena/...])

## Keadaan Sesi (selalu segar — agent baru BACA INI DULU)
- **Keadaan:** `OPEN` | `CLOSED`
- **Segar pada:** [YYYY-MM-DD] · FI [N] · manifest v[X.Y.Z] · head terukur `[sha7]`
  <!-- WAJIB untuk log `OPEN`: baris ini DIPERIKSA ALAT, dan harus **TEPAT SATU** serta **DI DALAM blok
       header ini** — baris yang sama di kronologi atau di dalam pagar kode TIDAK dihitung (regresi
       RP22f–h). `validate_repo.py` membandingkan [N] dengan `_meta/FAILURE_INJECTION_TESTS.md`,
       v[X.Y.Z] dengan `- **Versi:**` di `_meta/SYSTEM_MANIFEST.md`, dan [YYYY-MM-DD] dengan tanggal
       terbaru di berkas log ini; bila git tersedia, [sha7] harus HEAD sampai HEAD~3. Tidak cocok =
       VALIDATION FAILED (regresi RP22a–e). Log `CLOSED` dikecualikan seluruhnya.
       Arti `head terukur`: head yang terukur KETIKA header ini disegarkan — bukan head tempat angka
       FI/manifest itu berlaku, karena commit penyegaran belum ada saat barisnya ditulis. Format lama
       `head [sha7] · [YYYY-MM-DD] · FI [N] · manifest v[X.Y.Z]` DITOLAK dengan pesan migrasi: ia
       memasangkan sha dengan angka yang tidak pernah benar pada sha itu (temuan #3 hakim C putaran 7
       PR #74).
       Pemeriksaan FI/manifest/sha hanya KERAS selama log ini "live", yaitu disentuh salah satu dari 4
       commit terakhir; bila tidak live ketiganya turun menjadi warning beralasan sedangkan pemeriksaan
       tanggal tetap keras. Sebabnya: penjaga yang selalu keras membuat `main` VALIDATION FAILED
       seketika sesudah merge — log OPEN milik satu sesi tidak bisa disegarkan oleh sesi lain (temuan #2
       hakim C putaran 7, direproduksi pada squash merge maupun merge commit; dikunci RP23a–f dengan
       `.git` nyata). Segarkan baris ini setiap pertukaran bermakna — header adalah satu-satunya bagian
       log yang dikecualikan dari append-only justru supaya bisa disegarkan; membiarkannya basi adalah
       pelanggaran mekanisme, bukan sekadar ketinggalan (temuan #9 hakim putaran 5 PR #74, terulang
       sebagai temuan #3 putaran 6). -->
- **Scope:** [meta / sistem-[nama] / unit: <path>]
- **Di mana kita sekarang:** [1–3 baris: benang kerja/diskusi aktif]
- **Sudah disepakati:** [bullet]
- **Masih terbuka / tertunda:** [bullet]
- **Langkah berikutnya:** [1 baris]

## Kronologi (append, terbaru di bawah)
### [HH:MM] — [topik]
- **Pengguna:** [pernyataan penting — near-verbatim]
- **Agent:** [proposal/klaim penting + dasar — 1–3 baris]
- **Hasil:** [setuju / ditolak + alasan / terbuka]

### [HH:MM] — [topik]
...
```

## Siklus

1. **Awal sesi:** file belum ada → agent tidak wajib membuatnya *seketika*; dibuat pada pertukaran bermakna pertama (atau lebih awal kalau sesi langsung kerja berat).
2. **Selama sesi:** append + update header "Keadaan Sesi" setelah tiap pertukaran bermakna — **termasuk baris `- **Segar pada:**` yang kini diperiksa alat** (angka FI, versi manifest, tanggal, dan `head terukur` harus cocok dengan keadaan hidup; log `OPEN` yang header-nya basi = VALIDATION FAILED, regresi RP22a–e); commit + push segera.
3. **Akhir sesi (prompt penutup):** header diisi final → `CLOSED` (atau `OPEN` kalau kerja memang dilanjutkan sesi lain — tuliskan "dilanjutkan di mana").
4. **Sesi baru (entry point):** cari `LOG_SESI_*.md` terbaru di folder `_log-sesi/`, folder sistem, dan folder unit yang disentuh; kalau yang terbaru `OPEN` → baca, laporkan keadaan, **konfirmasi ke pengguna** sebelum lanjut. Jangan bertanya ulang konteks yang sudah tercatat.
