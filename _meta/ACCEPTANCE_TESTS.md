# Acceptance Tests — Meta-Sistem

Tes ini memvalidasi perilaku sistem, bukan hanya keberadaan file. Setiap test memiliki expected result; jika hasil aktual berbeda, sistem belum boleh diberi status `Released`.

## AT-01 — Entry point repo baru

**Given:** repository baru hanya memiliki struktur master dan belum memiliki sistem domain.  
**When:** pengguna menjalankan prompt universal.  
**Then:** agent membaca entry point meta-sistem, memeriksa PR, membaca index, menjelaskan bahwa belum ada sistem domain, lalu menanyakan tujuan sesi tanpa menulis file.

## AT-02 — Discovery Level-0

**Given:** pengguna menyebut domain baru dengan ide yang masih mentah.  
**When:** agent menjalankan Discovery Level-0.  
**Then:** agent menggali consumer, bentuk sistem, konsistensi, unit selesai, dan approval; menghasilkan rencana kerangka; tidak langsung mengisi sistem domain.

## AT-03 — Penerapan prinsip

**Given:** rencana kerangka sudah selesai.  
**When:** agent menyiapkan sistem domain.  
**Then:** manifest mencatat prinsip yang berlaku, cara penerapan, override, risiko, dan dependency.

## AT-04 — Checkpoint dan recovery

**Given:** agent berhenti setelah satu tahap dan sesi lama tidak tersedia.  
**When:** agent membuka sesi baru pada branch yang sama.  
**Then:** agent membaca manifest dan STATUS, memverifikasi output serta commit, lalu melanjutkan hanya dari tahap yang dapat dibuktikan selesai. Jika ambigu, agent berhenti dan bertanya.

## AT-05 — Perubahan keputusan besar

**Given:** pengguna mengusulkan perubahan pada aturan inti.  
**When:** agent menganalisis usulan.  
**Then:** agent membuat proposal berisi masalah, bukti, trade-off, metrik, regression check, dan rollback; tidak langsung mengubah aturan.

## AT-06 — Self-improvement sistem domain

**Given:** sistem domain mengalami failure mode berulang.  
**When:** agent mengusulkan upgrade.  
**Then:** observasi, analisis, keputusan, perubahan, versi, bukti verifikasi, dan rollback tercatat; hasil lama tidak dihapus sebelum versi baru lulus regression check.

## AT-07 — Verifikasi output

**Given:** sistem menghasilkan output yang akan dipakai atau dipublikasikan.  
**When:** agent menyelesaikan output.  
**Then:** output berstatus Draft, Checked, Approved, Released, atau Observed; checklist sesuai jenis output dilakukan; status Checked tidak dianggap Approved.

## AT-08 — Override eksplisit

**Given:** pengguna meminta satu lapisan quality assurance tidak digunakan.  
**When:** agent membuat sistem domain.  
**Then:** agent memastikan permintaan eksplisit, mencatat alasan, dampak, dan approval di manifest, serta menjelaskan risiko yang tersisa.

## AT-09 — Konflik antar branch

**Given:** dua pekerjaan menyentuh dokumen keputusan yang sama.  
**When:** agent menemukan konflik.  
**Then:** agent tidak menimpa perubahan; ia mengidentifikasi konflik, memisahkan tujuan, dan meminta approval ulang jika keputusan Besar terdampak.

## AT-10 — Pembuatan template

**Given:** master blueprint dan pilot sudah lulus.  
**When:** template bersih dibuat.  
**Then:** template tidak membawa data pribadi, output produksi, audit internal, atau keputusan domain contoh; entry point dan kontrak minimum tetap tersedia. Sejak audit 5 Sep 2026 (M-01/M-16), Then juga mencakup: (a) SEMUA `_meta/*.md` aktif dan SEMUA `tools/*.py` ikut terbawa (dijaga guard kelengkapan — rujukan aktif yang tidak ikut = build GAGAL); (b) salinan `SYSTEM_MANIFEST.md` master membawa banner "sejarah master, bukan identitas repo ini"; (c) hasil ekstrak lolos smoke test `validate_repo.py` + `test_failure_injection.py` di repo kosong tanpa sistem terdaftar.

## AT-11 — Regression setelah upgrade

**Given:** aturan universal atau template diubah.  
**When:** perubahan masuk tahap verifikasi.  
**Then:** contoh sistem lama, cross-reference, manifest, template, ringkasan, dan skenario failure yang relevan diuji ulang.

## AT-12 — Batas audit

**Given:** tidak ada bukti masalah dan tidak ada perubahan besar.  
**When:** sistem beroperasi normal.  
**Then:** tidak ada audit mendalam tanpa trigger; pemeriksaan ringan tetap berjalan sesuai kontrak output.

## AT-13 — Recovery konteks dari log sesi pasca crash

**Given:** sebuah sesi memelihara `LOG_SESI_YYYY-MM-DD.md` (header "Keadaan Sesi" + kronologi) yang berkeadaan `OPEN`, lalu sesi itu crash tanpa penutupan yang benar; tidak ada commit baru setelah update log terakhir.  
**When:** pengguna membuka sesi baru dan menjalankan prompt pembuka universal.  
**Then:** agent menemukan log terbaru, membacanya, dan **melaporkan keadaan sesi sebelumnya** (apa yang disepakati, apa yang terbuka, langkah berikutnya) sebelum bertanya tujuan sesi — tanpa meminta pengguna menjelaskan ulang konteks yang sudah tercatat; jika ada keputusan yang belum tercatat di log, agent menyebutkannya sebagai celah, bukan menebaknya.

## AT-14 — Kontrak warisan otomatis untuk sistem baru

**Given:** pengguna memulai sistem baru dengan Discovery Level-0; tidak menyebut-nyebut pegangan, LOG_SESI, field checkpoint, atau aturan platform.
**When:** agent menyusun `00_RENCANA_KERANGKA.md` dan skeleton sistem.
**Then:** agent TANPA diminta menerapkan seluruh butir `03_KONTRAK_WARISAN.md` (W-01…W-09) dan melaporkan tabel "Warisan" dengan status tiap butir; TIDAK menawarkan butir satu per satu sebagai pertanyaan; jika ada butir yang dinilai tidak cocok untuk domain itu, agent BERHENTI pada butir itu, menjelaskan apa yang hilang tanpanya, dan meminta keputusan eksplisit pengguna sebelum melewati — override tercatat di manifest dengan alasan + approval; `tools/validate_repo.py` menandai ERROR bila butir yang bisa dicek mekanis tidak ada, meski untuk sistem yang belum ada di daftar file statis validator mana pun (penegakan berbasis INDEKS, bukan daftar manual).

## AT-15 — PENSIUN: paket repo mandiri lama (digantikan AT-17)

AT-15 lama menguji mekanisme paket repo mandiri berbasis packager, ZIP/dist, profil repo, daftar putih rujukan-absen, dan subset meta. Skenario itu **pensiun 8 September 2026** dan digantikan AT-17.

Alasan pensiun: keputusan pemilik menetapkan folder sistem sebagai deliverable. Mekanisme lama memindahkan kerja penyatuan/glue ke pemilik, sedangkan folder yang langsung dipakai lebih murah dipertahankan. Jejak historis tetap tinggal di master; jangan menghidupkan AT-15 lama sebagai pengaman tambahan.

## AT-17 — Folder sistem = deliverable mandiri

**Given:** sebuah folder sistem terdaftar di `INDEKS_SISTEM.md`, dan PR mengklaim folder itu selesai/mandiri/siap dipakai sebagai repo sendiri. Penguji adalah sesi baru yang tidak ikut membangun sistem itu dan tidak diberi pengetahuan tersirat apa pun.
**When:** penguji menjalankan prosedur di bawah, apa adanya, dari root repo master.
**Then:** seluruh kriteria LULUS di bawah terpenuhi. Satu saja tidak terpenuhi = folder sistem itu belum boleh mengklaim mandiri atau "Siap dipakai produksi" (`DEFINITION_OF_DONE.md`). Aturan normatifnya: `_meta/PAKET_REPO_MANDIRI.md`.

**Prosedur uji (bisa diulang, tanpa pengetahuan tersirat):**

```bash
# 0. baseline master harus hijau lebih dulu — kalau merah, hentikan; itu
#    masalah lain, bukan hasil uji ini
python3 tools/validate_repo.py

# 1. jalankan gerbang mandiri pada sistem yang diklaim selesai
python3 tools/check_selfcontained.py --sistem <nama-folder-sistem> --report ; echo "exit=$?"

# 2. uji negatif: jalankan salinan alat dari folder yang tidak punya _meta/
#    (alat ini alat master, bukan alat tersembunyi repo mandiri)
rm -rf /tmp/uji-folder-mandiri
cp -R <root repo master>/<nama-folder-sistem> /tmp/uji-folder-mandiri
mkdir -p /tmp/uji-folder-mandiri/tools
cp <root repo master>/tools/check_selfcontained.py /tmp/uji-folder-mandiri/tools/check_selfcontained.py
cd /tmp/uji-folder-mandiri
python3 tools/check_selfcontained.py --semua ; echo "exit=$?"

# 3. bila PR menambah salinan berlabel, rusak satu label di salinan repo
#    sementara lalu pastikan alat master gagal; jangan merusak master
rm -rf /tmp/uji-repo-label-rusak
cp -R <root repo master> /tmp/uji-repo-label-rusak
cd /tmp/uji-repo-label-rusak
python3 -c "from pathlib import Path; root=Path('<nama-folder-sistem>'); files=[p for p in root.rglob('*') if p.is_file() and p.read_bytes().startswith(b'> Salinan turunan.')]; assert files, 'tidak ada salinan berlabel untuk dimutasi'; p=files[0]; lines=p.read_text(encoding='utf-8').splitlines(); p.write_text('\n'.join(lines[1:])+'\n', encoding='utf-8'); print(p)"
python3 tools/check_selfcontained.py --sistem <nama-folder-sistem> --report ; echo "exit=$?"
```

**Kriteria LULUS (semuanya, tanpa penilaian rasa):**

| # | Kriteria | Bukti yang harus terlihat |
|---|---|---|
| L1 | Langkah 0 hijau | validator master PASS dengan `WARNINGS: 0` |
| L2 | Langkah 1 menyalin hanya folder sistem dan menjalankan validator sistem di salinan | keluaran alat menampilkan perintah `python3 _sistem/validate_system.py`, baris `HASIL: PASS` dari validator sistem, dan exit 0 |
| L3 | Tidak ada rujukan ke diri sendiri memakai prefiks folder | tidak ada temuan `[SELF-PREFIX]` |
| L4 | Semua rujukan ber-backtick ke `_meta/...` atau `tools/...` punya salinan berlabel di dalam folder | tidak ada temuan `[MISSING-LABELED-COPY]` |
| L5 | Semua salinan turunan punya label wajib pada tiga baris pertama | tidak ada temuan `[DERIVED-NO-LABEL]` atau `[LABEL-FORMAT]` |
| L6 | Salinan berlabel tidak basi terhadap master | tidak ada temuan `[STALE-COPY]` atau `[LABEL-SOURCE]`; bila ada perbedaan yang disengaja, label menyebut perbedaan dan body PR mendaftarkan kasusnya |
| L7 | Langkah 2 membuktikan alat hanya alat master | exit 2 dan pesan menyatakan alat master harus dijalankan dari repo yang memiliki `_meta/` |

**Catatan pelaksanaan:** langkah negatif dijalankan di salinan sementara. Merusak master untuk keperluan uji dilarang. Untuk PR yang hanya mengubah alat/protokol meta, sistem domain yang belum termasuk scope boleh tetap merah; keluaran merahnya wajib ditempel utuh sebagai daftar kerja PR berikutnya.


## AT-16 — Larangan angka korpus dalam bukti permanen

**Given:** Log Evolusi, manifest, atau indeks mencatat bukti numerik.
**When:** angka itu dihitung dari korpus dokumen dan dapat berubah karena penulisan dokumen atau log sesi.
**Then:** angka tersebut dilarang dikutip dalam sel **Bukti**, termasuk jika ditemani atau dipin ke SHA. Verdict dan angka stabil tetap boleh atau wajib dicatat. `tools/validate_repo.py` gagal bila sel kolom **Bukti** Log Evolusi memuat angka yang berdekatan dengan `rujukan`, `path references`, `dokumen`, atau `active documents`.
