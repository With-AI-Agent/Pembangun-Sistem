# Prompt Review Independen — PR #74

> Dibangkitkan `tools/review_prompt.py` dari data PR di GitHub. Semua nomor, sha, dan daftar berkas di bawah
> berasal dari data itu + isi pohon kerja — bukan dari narasi pihak yang direview.


## 1. Siapa kamu

Kamu **sesi review independen**. Kamu tidak mengerjakan PR ini, tidak melanjutkannya, dan tidak
memperbaikinya. Kamu memutuskan.

- Mulai **tanpa konteks** dari sesi mana pun: yang kamu percaya hanya artefak (git tree, commit, log, API).
- **Read-only** terhadap repo dan terhadap branch orang lain: jangan commit, jangan push, jangan sunting berkas repo.
- Salinan kerja **hanya di `/tmp`** (mis. `git clone`/`git archive` ke `/tmp/review-<nomor>`); jalankan alat di sana.
- Klaim penulis PR = **objek pemeriksaan**, bukan bukti.

## 2. Urutan baca (jangan dilewati)

1. `LOG_SESI_*.md` yang masih berkeadaan `OPEN` (seluruhnya, dari yang terlama)
2. `_meta/00_CARA_KERJA_META.md`
3. `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` (seluruhnya)
4. `PANDUAN_PENGGUNA.md` — dokumen root yang disentuh PR
5. `PROMPT_ENTRI_UNIVERSAL.md` — dokumen root yang disentuh PR
6. `_log-sesi/LOG_SESI_2026-09-17.md` — log sesi penulis PR
7. `_meta/03_KONTRAK_WARISAN.md` — disentuh PR
8. `_meta/DAFTAR_PEKERJAAN_TERBUKA.md` — disentuh PR
9. `_meta/INDEKS_SISTEM.md` — disentuh PR
10. `_meta/NEXT_SESSION_PROMPT.md` — disentuh PR
11. `_meta/PANDUAN_PENGGUNA_TEMPLATE.md` — disentuh PR
12. `_meta/PLATFORM_LMARENA.md` — disentuh PR
13. `_meta/PROTOKOL_AUDIT_ISI.md` — disentuh PR
14. `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` — disentuh PR
15. `_meta/SYSTEM_MANIFEST.md` — disentuh PR
16. `_meta/TANGGAPAN_MASUKAN_PEMILIK.md` — disentuh PR
17. `_meta/_internal/AUDIT_MANUAL_DAN_MEKANISME_REVIEW_2026-09-17.md` — disentuh PR
18. `_meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md` — disentuh PR
19. `_meta/_internal/RENCANA_KERANGKA_DRAFT_sistem-undangan_2026-09-17.md` — disentuh PR
20. `_meta/_internal/audit/AUDIT_PROTOKOL_REVIEW_INDEPENDEN_8be158f.md` — disentuh PR
21. `sistem/sistem-building-aplikasi/SYSTEM_MANIFEST.md` — dokumen sistem yang disentuh PR
22. `sistem/sistem-building-aplikasi/_salinan-meta/PLATFORM_LMARENA.md` — dokumen sistem yang disentuh PR
23. `sistem/sistem-klinik/SYSTEM_MANIFEST.md` — dokumen sistem yang disentuh PR
24. `sistem/sistem-konten-kreator/SYSTEM_MANIFEST.md` — dokumen sistem yang disentuh PR
25. `sistem/sistem-konten-kreator/_salinan-meta/PLATFORM_LMARENA.md` — dokumen sistem yang disentuh PR
26. `sistem/sistem-presentasi/SYSTEM_MANIFEST.md` — dokumen sistem yang disentuh PR
27. `sistem/sistem-presentasi/_salinan-meta/PLATFORM_LMARENA.md` — dokumen sistem yang disentuh PR
28. `sistem/sistem-undangan/00_RENCANA_KERANGKA.md` — dokumen sistem yang disentuh PR
29. `sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md` — dokumen sistem yang disentuh PR
30. `sistem/sistem-undangan/02_PROFIL_JENIS_ACARA.md` — dokumen sistem yang disentuh PR
31. `sistem/sistem-undangan/03_TEMPLATE_DATA_ACARA.md` — dokumen sistem yang disentuh PR
32. `sistem/sistem-undangan/04_TEMPLATE_BRIEF_UNDANGAN.md` — dokumen sistem yang disentuh PR
33. `sistem/sistem-undangan/05_DISCOVERY_DESAIN_PROMPT.md` — dokumen sistem yang disentuh PR
34. `sistem/sistem-undangan/06_SPESIFIKASI_ASET_DAN_RESOLUSI.md` — dokumen sistem yang disentuh PR
35. `sistem/sistem-undangan/07_SPESIFIKASI_CETAK_PREPRESS.md` — dokumen sistem yang disentuh PR
36. `sistem/sistem-undangan/08_PIPELINE_VIDEO.md` — dokumen sistem yang disentuh PR
37. `sistem/sistem-undangan/09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` — dokumen sistem yang disentuh PR
38. `sistem/sistem-undangan/10_ARSITEKTUR_WEBSITE_INDUK.md` — dokumen sistem yang disentuh PR
39. `sistem/sistem-undangan/11_AMPLOP_DIGITAL.md` — dokumen sistem yang disentuh PR
40. `sistem/sistem-undangan/Input-Pengguna/README.md` — dokumen sistem yang disentuh PR
41. `sistem/sistem-undangan/STATUS.md` — dokumen sistem yang disentuh PR
42. `sistem/sistem-undangan/SYSTEM_MANIFEST.md` — dokumen sistem yang disentuh PR
43. `tools/ambil_verdict.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)
44. `tools/audit_prompt.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)
45. `tools/build_template.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)
46. `tools/check_manuals.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)
47. `tools/checkpoint_core.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)
48. `tools/review_prompt.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)
49. `tools/test_failure_injection.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)
50. `tools/validate_repo.py` — alat yang disentuh PR (baca kodenya, jangan hanya diff-nya)

## 3. Objek ter-pin

| Objek | Nilai |
|---|---|
| PR | #74 — meta v1.17.0-v1.19.0 + SISTEM KE-6 DIBUKA: sistem-undangan (kerangka) — gerbang aset diputuskan oleh pengukuran, bukan perkiraan |
| Base ref | `main` |
| Base sha | `ac57016b48503f958de2c2c12ac72246b6593746` |
| Head ref | `arena/01a0ae7a-pembangun-sistem` |
| Head sha | `3543612766e5d23098185e0c571657e1a7c4db13` |
| Berkas berubah | 49 |

Semua pemeriksaan dilakukan **pada dua sha itu**, bukan pada "main terbaru" atau pada branch yang bergerak:

```bash
git diff --stat ac57016b48503f958de2c2c12ac72246b6593746 3543612766e5d23098185e0c571657e1a7c4db13
git diff --numstat ac57016b48503f958de2c2c12ac72246b6593746 3543612766e5d23098185e0c571657e1a7c4db13
```

Berkas yang di-declare berubah oleh data PR:

- `PANDUAN_PENGGUNA.md`
- `PROMPT_ENTRI_UNIVERSAL.md`
- `_log-sesi/LOG_SESI_2026-09-17.md`
- `_meta/03_KONTRAK_WARISAN.md`
- `_meta/DAFTAR_PEKERJAAN_TERBUKA.md`
- `_meta/INDEKS_SISTEM.md`
- `_meta/NEXT_SESSION_PROMPT.md`
- `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`
- `_meta/PLATFORM_LMARENA.md`
- `_meta/PROTOKOL_AUDIT_ISI.md`
- `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md`
- `_meta/SYSTEM_MANIFEST.md`
- `_meta/TANGGAPAN_MASUKAN_PEMILIK.md`
- `_meta/_internal/AUDIT_MANUAL_DAN_MEKANISME_REVIEW_2026-09-17.md`
- `_meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md`
- `_meta/_internal/RENCANA_KERANGKA_DRAFT_sistem-undangan_2026-09-17.md`
- `_meta/_internal/audit/AUDIT_PROTOKOL_REVIEW_INDEPENDEN_8be158f.md`
- `_meta/_internal/uji/uji_upscaling.py`
- `sistem/sistem-building-aplikasi/SYSTEM_MANIFEST.md`
- `sistem/sistem-building-aplikasi/_salinan-meta/PLATFORM_LMARENA.md`
- `sistem/sistem-klinik/SYSTEM_MANIFEST.md`
- `sistem/sistem-konten-kreator/SYSTEM_MANIFEST.md`
- `sistem/sistem-konten-kreator/_salinan-meta/PLATFORM_LMARENA.md`
- `sistem/sistem-presentasi/SYSTEM_MANIFEST.md`
- `sistem/sistem-presentasi/_salinan-meta/PLATFORM_LMARENA.md`
- `sistem/sistem-undangan/00_RENCANA_KERANGKA.md`
- `sistem/sistem-undangan/01_IDENTITAS_PEMILIK.md`
- `sistem/sistem-undangan/02_PROFIL_JENIS_ACARA.md`
- `sistem/sistem-undangan/03_TEMPLATE_DATA_ACARA.md`
- `sistem/sistem-undangan/04_TEMPLATE_BRIEF_UNDANGAN.md`
- `sistem/sistem-undangan/05_DISCOVERY_DESAIN_PROMPT.md`
- `sistem/sistem-undangan/06_SPESIFIKASI_ASET_DAN_RESOLUSI.md`
- `sistem/sistem-undangan/07_SPESIFIKASI_CETAK_PREPRESS.md`
- `sistem/sistem-undangan/08_PIPELINE_VIDEO.md`
- `sistem/sistem-undangan/09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md`
- `sistem/sistem-undangan/10_ARSITEKTUR_WEBSITE_INDUK.md`
- `sistem/sistem-undangan/11_AMPLOP_DIGITAL.md`
- `sistem/sistem-undangan/Input-Pengguna/README.md`
- `sistem/sistem-undangan/STATUS.md`
- `sistem/sistem-undangan/SYSTEM_MANIFEST.md`
- `sistem/sistem-undangan/_sistem/validate_system.py`
- `tools/ambil_verdict.py`
- `tools/audit_prompt.py`
- `tools/build_template.py`
- `tools/check_manuals.py`
- `tools/checkpoint_core.py`
- `tools/review_prompt.py`
- `tools/test_failure_injection.py`
- `tools/validate_repo.py`

## 4. Cek standar (semua wajib, semua harus bisa direproduksi)

1. **Kelengkapan vs isi PR** — setiap hal yang dijanjikan body PR benar-benar ada di diff; setiap hal di diff
   punya penjelasan di body. Selisih dua arah = temuan.
2. **Append-only** — `git diff --numstat <base> <head>` untuk berkas log/bukti (`LOG_SESI_*.md`,
   `ACCEPTANCE_TEST_LOG.md`, dokumen bukti): kolom delesi **harus 0** — KECUALI blok header
   "Keadaan Sesi" pada `LOG_SESI_*.md`. Blok itu WAJIB disegarkan saat penutupan sesi (header
   `OPEN` menjadi `CLOSED`, ringkasan keadaan diperbarui), jadi perubahan baris DI DALAM blok itu
   SAH dan bukan temuan. Batas blok = awal berkas sampai baris `## Kronologi` (atau penanda setara);
   perubahan di ATAS batas = wajar bila hanya di blok header; perubahan di BAWAH batas (entri
   kronologi) = **BLOCKER**. Entri lama yang diedit/dihapus/dihaluskan = **BLOCKER**, bukan catatan
   kecil. (Penyelarasan 15 Sep 2026: aturan segarkan-header ada di `_meta/TEMPLATE_LOG_SESI.md` dan
   `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` — tanpa pengecualian ini dua aturan saling mengunci.)
   Pengecualian redaksi 6d: delesi/edit di bawah batas `## Kronologi` adalah SAH (bukan BLOCKER) jika
   dan hanya jika 4 syarat ini terpenuhi: (i) dideklarasikan di body PR per berkas + nomor baris persis;
   (ii) pola edit = penggantian pemetaan run/sisi/verdict/state-fixture menjadi pointer netral (pola 6d;
   preseden: ACCEPTANCE_TEST_LOG.md "Sanitasi 6 Sep" + Rencana re-run); (iii) fakta proses yang bukan
   pola tersebut dipertahankan byte-exact; (iv) otorisasi pemilik tercatat di body PR + log sesi penulis.
   Artefak newline-EOF: "delesi" teks yang byte-identik yang terjadi semata karena baris terakhir berkas
   tidak punya newline pengakhir (append memberikannya) BUKAN delesi konten dan bukan temuan; syarat
   "kolom delesi = 0" diukur atas konten entri kronologi.
3. **Klaim luar diverifikasi lewat API** — status PR/rilis/komentar/merge dicek dengan `gh api`, bukan dibaca
   dari body PR. Kalau body menyebut angka rilis/ID/URL, panggil API-nya sendiri.
4. **Angka direproduksi sendiri** — setiap angka yang dikutip di bukti (jumlah skenario, jumlah warning, jumlah
   rujukan, sha) kamu hitung ulang di salinan `/tmp` pada head sha. Angka yang tidak kamu reproduksi = belum diverifikasi.
5. **Disiplin klaim** — tidak boleh ada gerbang/gate yang dinyatakan tertutup oleh pihak yang tidak berhak
   menutupnya. Cari kalimat berstatus ("LULUS", "DITUTUP", "selesai", "terpenuhi") dan tanyakan: siapa yang
   menutup, dengan bukti apa, dan apakah dia berwenang.
6. **Skala** — perubahan apa pun di luar yang dideklarasikan body PR = temuan, sekecil apa pun dan sebaik apa pun niatnya.
7. **Tidak terverifikasi = MERAH.** Bukan "kemungkinan besar benar", bukan "tampaknya wajar".

Regresi wajib dijalankan di salinan `/tmp` pada head sha:

```bash
python3 tools/validate_repo.py          # harus PASS, 0 warning
python3 tools/test_failure_injection.py # harus PASS; jumlah skenario = _meta/FAILURE_INJECTION_TESTS.md
```

## 5. Berkas pelindung (dihitung dari pohon + diff, bukan ditulis manual)

Aturan untuk **setiap** berkas di tabel ini: kalau PR menyentuhnya **tanpa declare eksplisit di body → temuan**;
kalau yang disentuh adalah **pin** → **JANGAN merge, laporkan ke pemilik**.

| Berkas pelindung | Disentuh PR ini? | Kenapa dilindungi |
|---|---|---|
| `tools/checkpoint_core.py` | **YA** | memuat pin regresi |
| `tools/test_failure_injection.py` | **YA** | memuat pin regresi |
| `_meta/PROTOKOL_REVIEW_INDEPENDEN.md` | tidak | protokol review independen |
| `tools/review_prompt.py` | **YA** | pembangkit prompt pengadil |
| `tools/audit_prompt.py` | **YA** | pembangkit prompt pengadil (kanal audit isi) |
| `tools/ambil_verdict.py` | **YA** | pengambil hasil pengadil dari GitHub |
| `_meta/PROTOKOL_AUDIT_ISI.md` | **YA** | protokol audit isi |
| `_meta/TEMPLATE_RELEASE.md` | tidak | dokumen mekanisme rilis |
| `sistem/sistem-klinik/_sistem/05A_PROMPT_KAPABILITAS.md` | tidak | aturan sistem domain (00/05/06) |
| `sistem/sistem-klinik/_sistem/05_TAWARAN_KAPABILITAS.md` | tidak | aturan sistem domain (00/05/06) |
| `sistem/sistem-klinik/_sistem/06_RITME_KIT.md` | tidak | aturan sistem domain (00/05/06) |
| `sistem/sistem-konten-kreator/_sistem/00_CARA_PAKAI_SISTEM.md` | tidak | aturan sistem domain (00/05/06) |
| `sistem/sistem-konten-kreator/_sistem/05_CONTENT_PRODUCTION_PIPELINE.md` | tidak | aturan sistem domain (00/05/06) |
| `sistem/sistem-konten-kreator/_sistem/06_PROMPT_LIBRARY.md` | tidak | aturan sistem domain (00/05/06) |
| `sistem/sistem-presentasi/_sistem/05_SUMBER_DAN_ANTI_NGARANG.md` | tidak | aturan sistem domain (00/05/06) |
| `sistem/sistem-presentasi/_sistem/06_PRINSIP_DESIGN_BERBASIS_BUKTI.md` | tidak | aturan sistem domain (00/05/06) |

## 6. Aturan keputusan

**Semua cek hijau, tanpa satu pun BLOCKER:**

```bash
gh pr merge 74 --merge
```

lalu jalankan ulang di `main` terbaru dan **tempel keluaran persisnya** di komentar review:

```bash
python3 tools/validate_repo.py
python3 tools/test_failure_injection.py
```

**Ada satu saja MERAH:** jangan menggabungkan apa pun. Tulis komentar terstruktur:

- **temuan** (satu kalimat, tanpa hedging) → **bukti** (perintah + keluaran + sha/baris) → **perintah perbaikan**
  (apa yang harus diubah, oleh siapa).
- Sebut **putaran ke berapa** review ini (maksimal 2 putaran; putaran ke-2 gagal = eskalasi ke pemilik).
- PR dibiarkan `OPEN`.

**Tidak pernah, dalam keadaan apa pun:** memperbaiki sendiri versi, wording, pin, transkrip, atau isi berkas
penulis. Reviewer yang menambal temuannya sendiri sudah berhenti jadi reviewer.

## 7. Pengecualian pengadil (baca sebelum menyentuh tombol merge)

**BERLAKU untuk PR ini.** PR ini menyentuh alat pengadil:

- `_meta/PROTOKOL_AUDIT_ISI.md`
- `tools/ambil_verdict.py`
- `tools/audit_prompt.py`
- `tools/checkpoint_core.py`
- `tools/review_prompt.py`
- `tools/test_failure_injection.py`

Karena itu: **JANGAN melakukan merge apa pun**, sekalipun semua cek hijau. Tugasmu berhenti pada
**melaporkan**. PR yang mengubah alat pengadil tidak boleh dieksekusi oleh pengadil yang diubahnya —
penggabungan adalah keputusan pemilik langsung.

## 8. Batas publikasi (6d)

Tidak terdeteksi `LOG_SESI` berkeadaan `OPEN` dari sesi lain yang menyebut jendela uji berjalan. Aturan 6d tetap berlaku:
kalau kamu menemukan jendela terbuka saat membaca, ganti kutipan rumusan jawaban/kriteria dengan pointer
SHA+baris di semua artefak yang kamu publikasikan.

Pointer log penulis PR yang tidak memicu penyembunyian (tetap dibaca sebagai konteks, bukan sebagai jendela sesi lain):
- pointer SHA+baris: `3543612766e5d23098185e0c571657e1a7c4db13` → `_log-sesi/LOG_SESI_2026-09-17.md:5`

