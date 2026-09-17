# Kontrak Warisan — Hal yang WAJIB Tertanam di Semua Sistem

### Daftar induk butir yang otomatis melekat pada SETIAP sistem yang dibangun oleh meta-sistem ini — yang sudah ada maupun yang akan dibangun nanti. Ini kontrak penyerahan, bukan prinsip berperilaku (untuk itu lihat `02_PRINSIP_UNIVERSAL.md`). Dibuat 5 Sep 2026 atas permintaan pengguna setelah audit meta menyeluruh (temuan M-13): aturan wajib sebelumnya tersebar di 6 dokumen tanpa daftar induk, sehingga bergantung pada ingatan agent dan bisa terlupakan diam-diam.

---

## Induk juga subjek kontrak ini (ditambahkan 17 Sep 2026)

**Sebelum tanggal ini, meta-sistem DIKECUALIKAN dari kontraknya sendiri secara struktural** — dan pengecualian
itu tidak disadari oleh alat mana pun. Tiga bukti pengecualiannya:

1. Judul dokumen ini hanya menyebut *"SETIAP sistem yang **dibangun oleh** meta-sistem ini"*.
2. `_meta/INDEKS_SISTEM.md` menyatakan: *"Meta-sistem (`_meta/`) — ini kerangka yang menaungi semua sistem,
   **bukan salah satu isinya**"* (pernyataan itu **benar** untuk tujuan pendaftaran sistem domain, tetapi ikut
   membuat induk terlepas dari kewajiban).
3. `tools/validate_repo.py` memeriksa butir Warisan **hanya** pada manifest sistem terdaftar di INDEKS.

**Akibat yang terukur:** audit 17 Sep 2026 menemukan induknya sendiri **tidak** menerapkan 3 butir —
**W-03** (tidak ada field checkpoint deterministik yang hidup), **W-07** (manifest meta tidak punya bagian
Batasan Platform padahal meta-lah penulis aturan platformnya), dan **W-09** (4 ringkasan cadangan ada untuk
sistem anak, **tidak ada** untuk meta sendiri). **Ketiganya lolos tanpa terdeteksi selama ini.**

**Aturan sekarang:**

- **Induk TUNDUK pada kontrak yang ia tulis.** Kepatuhannya dideklarasikan di tabel
  **`## Warisan Meta`** dalam `_meta/SYSTEM_MANIFEST.md`, dan **ditegakkan mekanis** oleh
  `tools/validate_repo.py`: setiap butir wajib punya **baris** deklarasi `| W-nn …`.
- **Gap boleh, diam tidak boleh.** Butir yang genuinely tidak berbentuk sama di level meta **wajib dinyatakan
  sebagai gap** (GAP M-n) beserta buktinya dan dua pilihan sahnya (adopsi, atau override tercatat sesuai
  aturan 3 di bawah). **Yang tidak sah: tidak berstatus.**
- **Yang ditagih dari induk adalah DEKLARASI STATUS, bukan keberadaan artefak yang seragam.** Sengaja begitu:
  memaksa bentuk artefak yang sama di level meta akan menghasilkan **kepatuhan palsu** — centang tanpa
  substansi. Contoh nyata: meta tidak punya "unit kerja" ber-`STATUS.md`, jadi W-03 di level meta dijawab
  dengan bentuk setara (header Keadaan Sesi di LOG_SESI + field Status/Versi di manifest), dan **ketiadaan
  field deterministiknya dinyatakan sebagai gap**, bukan disulap jadi centang.
- **Butir baru yang ditambahkan ke kontrak ini otomatis berlaku juga untuk induk** — `WARISAN_ITEMS` di
  `tools/checkpoint_core.py` adalah satu daftar yang dipakai kedua pemeriksaan (sistem terdaftar **dan** meta).

## Aturan main kontrak

1. **Default aktif.** Saat membangun sistem baru, agent MENERAPKAN seluruh butir di bawah sejak kerangka (Discovery Level-0) — TANPA perlu diminta, dan TANPA menawarkan tiap butir satu per satu (birokrasi). Yang dilaporkan: satu tabel "Warisan" berisi status tiap butir.
2. **Laporkan, jangan diam.** Penerapan tiap butir dicatat di `00_RENCANA_KERANGKA.md` (kolom "Warisan") lalu disalin ke `SYSTEM_MANIFEST.md` sistem — supaya sesi baru bisa MEMERIKSA, bukan percaya.
3. **Hanya penonaktifan yang butuh keputusan pengguna.** Kalau sebuah butir tidak cocok untuk domain itu (atau pengguna menolaknya), agent BERHENTI, menjelaskan apa yang hilang kalau butir itu tidak diterapkan, dan meminta konfirmasi eksplisit. Override dicatat di manifest sistem: butir, alasan, dampak, tanggal, approval. "Tidak dilakukan karena lupa" bukan override valid.
4. **Diverifikasi otomatis.** `tools/validate_repo.py` + `tools/test_failure_injection.py` (parser bersama: `tools/checkpoint_core.py`) mengecek butir yang dapat dicek mekanis untuk SETIAP sistem terdaftar di `INDEKS_SISTEM.md`: keberadaan berkas W-01 & W-04, string platform W-07, turunan LOG_SESI W-02, keberadaan + field checkpoint unit W-03, dan kelengkapan 9 butir Warisan di manifest. Mekanisme anti-lubang (diperketat 5 Sep 2026 setelah review independen PR #11): **inventaris inti statis** (file inti yang DIHAPUS membuat validator/build/backup gagal — kewajiban tidak diturunkan dari keberadaan); **parse INDEKS ketat** (baris valid hanya dengan kolom Folder persis backticked; folder `sistem-*/` di disk yang tak terdaftar = error); **unit diharapkan, bukan hanya ditemukan** (sistem terdaftar tanpa satu pun `STATUS.md` unit = error — cakupan tidak boleh menyusut jadi nol); **parser fail-closed bersama** (field ganda / kutipan contoh / contoh dalam fence = TIDAK AMAN); **override tervalidasi + Tahap pembangunan** (lihat bagian di bawah). Sistem baru otomatis tercakup begitu didaftarkan — tidak ada lagi "validator lupa didaftarkan" (gaya kegagalan temuan M-01/M-03 audit 5 Sep 2026).
5. **Self-contained.** Butir yang diturunkan ke sistem HARUS berada di dalam folder sistem (ikut saat folder diunduh jadi repo standalone). Rujukan ke `_meta/` hanya provenance, dan harus diberi label jelas; aturan operasionalnya sendiri tidak boleh bergantung padanya.

## Tahap pembangunan & override tervalidasi (diperketat 5 Sep 2026, review PR #11)

- **Field `Tahap` di manifest sistem** — `- **Tahap:** kerangka` atau `- **Tahap:** siap-pakai` (default bila tidak tertulis: `siap-pakai`). `kerangka` = sistem baru didaftarkan sebagai skeleton (rencana kerangka di-merge, isi belum dibangun): cek keberadaan W-01 (pegangan), W-02 (turunan LOG_SESI), dan W-03 (unit STATUS) menjadi **warning, bukan error** — sesuai rumus W-01 "dibuat saat sistem memasuki tahap siap-pakai". Yang lain tetap ketat sejak kerangka: manifest (W-04) + fakta platform (W-07) wajib, karena manifest sendiri yang menjadi pembawa field `Tahap`. Saat sistem siap dipakai, `Tahap` diubah ke `siap-pakai` dan seluruh cek kembali ketat.
- **Override hanya valid jika lengkap.** Baris tabel Warisan dengan status `override` membebaskan pengecekan mekanis butir itu HANYA bila baris memuat keempat label `alasan:`, `dampak:`, `tanggal:`, `approval:` (isi kolom Override) — sesuai prosedur override di bawah. Override setengah jadi = error validator, bukan jalan tol diam-diam.

## Daftar butir

| # | Butir | Apa yang harus ada di sistem | Sumber aturan (meta) | Cara penanaman di sistem | Cara verifikasi |
|---|---|---|---|---|---|
| W-01 | **Pegangan pengguna 2-file** | `PROMPT_ENTRI_UNIVERSAL.md` (blok pembuka, siap tempel) + `PANDUAN_PENGGUNA.md` (root atau `panduan/`; pembuka + PENUTUP sesi + istilah + review/merge) | `PANDUAN_PENGGUNA_TEMPLATE.md` | dibuat saat sistem memasuki tahap siap-pakai; blok pembuka/penutup identik dengan salinannya di file lain sistem itu | validator: keberadaan kedua file; audit: diff blok prompt |
| W-02 | **Log sesi berkelanjutan (`LOG_SESI`)** | aturan ringkas self-contained di dalam folder sistem + langkah "cari log `OPEN`" di prompt pembuka + langkah "tutup log `CLOSED`" di prompt penutup | `PROTOKOL_CHECKPOINT_RECOVERY.md` §"Log Sesi Berkelanjutan" + `TEMPLATE_LOG_SESI.md` (format disalin/diturunkan, bukan dirujuk) | salin aturan relevan ke `_sistem/` (mis. `XX_LOG_SESI.md`) dan tempel langkahnya ke pegangan | validator: string `LOG_SESI` ada di dokumen aktif sistem |
| W-03 | **Kontrak checkpoint unit kerja** | setiap unit punya `STATUS.md` (atau setara) yang memuat field deterministik `**Pekerjaan belum tersimpan:** Tidak ada` (exact) + `Waktu pembaruan` (tiap checkpoint & akhir sesi, format `YYYY-MM-DD — <peristiwa>`); template STATUS sistem memuat field ini | `PROTOKOL_CHECKPOINT_RECOVERY.md` (format + aturan deterministik, Q-O3 closed 5 Sep) | field ditanam di TEMPLATE status unit, bukan hanya di unit contoh | validator: field ada di SEMUA STATUS unit + template |
| W-04 | **Manifest sistem** | `SYSTEM_MANIFEST.md` di root folder sistem, disalin dari `SYSTEM_MANIFEST_TEMPLATE.md` (termasuk bagian Batasan Platform + tabel Warisan) | `SYSTEM_MANIFEST_TEMPLATE.md` | dibuat bersama rencana kerangka, dalam PR yang sama | validator: keberadaan + cek "Dipakai via lmarena" |
| W-05 | **Log Keputusan di dokumen hidup** | setiap dokumen yang isinya bisa berubah punya tabel Log Keputusan (tanggal, perubahan, ALASAN) | `02_PRINSIP_UNIVERSAL.md` prinsip 5 | disertakan sejak dokumen pertama ditulis; template sistem mengalaminya | audit lintas-sesi (belum mekanis) |
| W-06 | **QA & evolusi 3-lapis** | sistem punya cara self-audit + verifikasi output + trigger audit + rollback; kedalaman mengikuti risiko | `QUALITY_ASSURANCE_AND_EVOLUTION.md` | boleh diringkas, TIDAK boleh dihilangkan; versi ringkasnya ditulis DI DALAM folder sistem | audit lintas-sesi; field manifest "Override quality protocol" |
| W-07 | **Fakta platform lmarena** | bagian "Batasan Platform" berisi 3 fakta platform dengan bahasa kausal ("tidak bisa", bukan "jangan"): branch `arena/` otomatis, tidak bisa push setelah merge/close, sesi bisa crash | `PLATFORM_LMARENA.md` | salin 3 fakta + implikasi sistemnya ke dokumen cara-pakai/manifest sistem | manifest: cek string "Dipakai via lmarena" |
| W-08 | **Approval Bertingkat** | kriteri Besar vs Kecil konkret untuk domain ini, didaftarkan di manifest + rencana kerangka | `02_PRINSIP_UNIVERSAL.md` prinsip 3 | digali di Discovery Level-0 poin 4, dikunci di rencana kerangka | review pengguna sebelum merge (proses PR) |
| W-09 | **Ringkasan cadangan** | `_cadangan-claude/RINGKASAN_sistem-[nama].md` di repo master: identitas, versi, struktur, bagian belum selesai, ke mana hasil kerja dibawa | `00_CARA_KERJA_META.md` langkah 7 alur sistem baru | ditulis saat struktur stabil; DIPERBARUI setiap perubahan struktural (bukan tiap revisi kecil) — kedaluwarsa = temuan audit (M-09, 5 Sep) | audit meta: sinkron vs manifest |
| W-10 | **Audit isi + pengiriman hasil** | sistem punya cara **diaudit isinya** lewat prompt yang **DIBANGKITKAN ALAT** (bukan dikarang tangan) + kanal penyerahan hasil yang bisa **diambil sendiri** oleh sesi yang diaudit + ATURAN CAKUPAN tersedia di dalam folder | `PROTOKOL_AUDIT_ISI.md` + `QUALITY_ASSURANCE_AND_EVOLUTION.md` bagian ATURAN CAKUPAN | sebut di pegangan/entry point sistem: `python3 tools/audit_prompt.py --objek sistem/<nama>` untuk mengaudit sistem ini, dan `python3 tools/ambil_verdict.py --terbaru` untuk mengambil hasilnya; salin ATURAN CAKUPAN ke dokumen QA sistem (boleh diringkas, tidak boleh dihilangkan — pola W-06) | validator: butir disebut di manifest; **cek artefak turunan di dalam folder BELUM mekanis** — dicatat sadar sebagai gap, bukan diklaim sudah |

## Prosedur override (satu-satunya jalur penonaktifan)

```
agent menemukan butir tidak cocok / pengguna menolak
→ agent jelaskan: butir, apa yang hilang tanpanya, risiko tersisa
→ keputusan pengguna (eksplisit, dicatat near-verbatim di LOG_SESI)
→ tulis di SYSTEM_MANIFEST.md sistem: override W-0n, alasan, dampak, tanggal, approval
→ update CHECKLIST terkait (DoD s/d override tercatat, jangan diam)
```

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-17 | **Butir W-10 (Audit isi + pengiriman hasil) DITAMBAH** — kontrak jadi 10 butir; `WARISAN_ITEMS` di `tools/checkpoint_core.py` 9→10; fixture `MINI_MANIFEST` di `tools/test_failure_injection.py` ikut ditambah barisnya (kalau tidak, skenario FI yang harus PASS jadi MERAH); baris status ditambahkan ke manifest meta + 4 sistem terdaftar. **3 jalur pengadil baru** didaftarkan di `ARBITER_PATH_REASONS` (`review_prompt.py`) dan `ARBITER_PATHS` (`audit_prompt.py`) — kedua daftar **diverifikasi sinkron** (6 jalur masing-masing) | Mekanisme audit isi **sudah dibangun** lebih dulu (`tools/audit_prompt.py`, `tools/ambil_verdict.py`, `PROTOKOL_AUDIT_ISI.md`) — **sengaja dalam urutan itu**: kontrak aturan 3 menuntut butir yang **bisa ditanam**, jadi menambahkan W-10 sebelum alatnya ada akan memaksa 4 sistem mengklaim kepatuhan pada sesuatu yang tidak ada. Menjawab tuntutan pemilik T29+T30 dan perluasannya (*"mekanisme itu juga harus tertanam di meta sistem … bukan pada sistem-sistem yang dibangun nya saja, tapi juga pada induk sistem itu sendiri"*). **Status 4 sistem ditulis "diterapkan sebagian" secara jujur**: mekanisme jalan dari meta, tetapi **turunan self-contained di dalam folder belum ada** — dan **cek artefak turunannya belum mekanis**, dinyatakan sebagai gap, bukan diklaim selesai |
| 2026-09-17 | Bagian **"Induk juga subjek kontrak ini"** ditambahkan; kepatuhan meta dideklarasikan di tabel `## Warisan Meta` pada `_meta/SYSTEM_MANIFEST.md` dan **ditegakkan mekanis** oleh `tools/validate_repo.py` (butir wajib berupa **baris** `| W-nn …`, bukan disebut di prosa) | **Instruksi eksplisit pemilik 17 Sep 2026:** *"mekanisme itu juga harus tertanam di meta sistem. Artinya bukan pada sistem-sistem yang dibangun nya saja, tapi juga pada induk sistem itu sendiri."* Audit menemukan pengecualian struktural itu nyata dan **sudah bocor**: 3 butir (W-03, W-07, W-09) tidak diterapkan induknya sendiri dan tidak terdeteksi alat mana pun, karena validator hanya memeriksa sistem terdaftar di INDEKS. W-07 **ditutup** di commit yang sama; W-03 dan W-09 **dinyatakan sebagai gap** menunggu keputusan pemilik (adopsi atau override tercatat). Cek validatornya sendiri **diuji mutasi 5 kasus** — versi pertama cek menghasilkan **PASS palsu** (menghapus baris W-09 tetap hijau karena kalimat prosa "W-01…W-09" sudah memenuhi `W-09`); diperketat jadi wajib-baris dan kelima kasus lulus |
| 2026-09-05 | Dokumen dibuat (meta v1.3.0) | Permintaan pengguna pasca audit menyeluruh: butir wajib harus otomatis tertanam pada sistem yang AKAN dibangun, bukan hanya diselaraskan ke yang sudah ada; desain "kontrak warisan" (default aktif, hanya penonaktifan dikonfirmasi) disetujui pengguna 16:50 WIB; temuan M-13/AUDIT_META_SISTEM_2026-09-05 |
| 2026-09-05 | Diperketat pasca review independen PR #11: inventaris inti statis, parse INDEKS ketat, unit diharapkan, parser bersama fail-closed, bagian "Tahap pembangunan & override tervalidasi" | Reviewer (sesi agent terpisah, VERDICT: REQUEST_CHANGES) membuktikan 4 PASS palsu — hapus file inti lolos, folder `sistem-autopilot-data` lolos (pengecualian substring "pilot"), baris INDEKS tanpa backtick diabaikan, field duplikat lolos — plus 2 dependensi aktif hilang di bootstrap template; perbaikan F1–F16 di PR #11 yang sama, di-pin sebagai regresi R1–R7 |
