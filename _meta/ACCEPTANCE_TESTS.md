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

## AT-15 — Sistem jadi dapat dibangkitkan jadi repo mandiri yang tervalidasi

**Given:** sebuah sistem domain sudah terdaftar di `INDEKS_SISTEM.md` dan hendak diberi (atau sudah memegang) status "Siap dipakai produksi". Penguji adalah sesi baru yang **tidak** ikut membangun sistem itu dan tidak diberi pengetahuan tersirat apa pun.
**When:** penguji menjalankan prosedur di bawah, apa adanya, dari root repo master.
**Then:** ketujuh kriteria LULUS di bawah terpenuhi. Satu saja tidak terpenuhi = sistem itu **belum** boleh mengklaim "Siap dipakai produksi" (`DEFINITION_OF_DONE.md`). Aturan normatifnya: `_meta/PAKET_REPO_MANDIRI.md`.

**Prosedur uji (bisa diulang, tanpa pengetahuan tersirat):**

```bash
# 0. baseline master harus hijau lebih dulu — kalau merah, hentikan; itu
#    masalah lain, bukan hasil uji ini
python3 tools/validate_repo.py

# 1. mode pemeriksaan: tidak menulis apa pun
python3 tools/pack_repo.py <nama-folder-sistem> --check ; echo "exit=$?"

# 2. run sungguhan ke folder di luar repo
python3 tools/pack_repo.py <nama-folder-sistem> --out /tmp/uji-pack-1 ; echo "exit=$?"

# 3. verifikasi DI DALAM hasil pack
cd /tmp/uji-pack-1 && python3 tools/validate_repo.py ; echo "exit=$?"
cd /tmp/uji-pack-1/<nama-folder-sistem> && python3 _sistem/validate_system.py ; echo "exit=$?"

# 4. determinisme
cd <root repo master>
python3 tools/pack_repo.py <nama-folder-sistem> --out /tmp/uji-pack-2 >/dev/null
diff -r /tmp/uji-pack-1 /tmp/uji-pack-2 ; echo "exit=$?"

# 5. tidak ada isi dokumen yang ditulis ulang
diff -r <root repo master>/<nama-folder-sistem> /tmp/uji-pack-1/<nama-folder-sistem>

# 6. negatif: sistem yang dirusak HARUS gagal (di SALINAN sementara, bukan di master)
cp -r <root repo master> /tmp/uji-rusak && cd /tmp/uji-rusak
rm <nama-folder-sistem>/_sistem/validate_system.py
python3 tools/pack_repo.py <nama-folder-sistem> --check ; echo "exit=$?"

# 7. pemindahan ke luar sandbox (L7) — self-contained.
#    Pointer: butir 4–7 bagian "Memindahkan paket ke luar sandbox"
#    di _meta/PAKET_REPO_MANDIRI.md. Draft tanpa aset tidak memenuhi.
#    Pin sumber: snapshot bersih pada SHA yang dicatat di berita acara
#    PAKET_REPO.md / entri bukti, BUKAN HEAD cabang kerja.
#    Bangkitkan paket pada SHA itu:
python3 tools/pack_repo.py <nama-folder-sistem> --zip
#    Unggah ZIP packager ke DRAFT yang sudah ada (jangan membuat release
#    baru, jangan mengganti tag):
gh release upload <tag-paket> <berkas-zip> --repo With-Ai-Agent/Pembangun-Sistem --clobber
#    Verifikasi state aset terunggah (jumlah aset >= 1, state=uploaded):
gh api repos/With-Ai-Agent/Pembangun-Sistem/releases --jq '.[] | {id, tag_name, draft, assets: [.assets[] | {name, state, size}]}'
#    Unduh ulang aset dan cocokkan sha256 dengan byte ZIP lokal.
#    Kalimat tegas: draft tanpa aset tidak memenuhi langkah ini.
```

**Kriteria LULUS (semuanya, tanpa penilaian rasa):**

| # | Kriteria | Bukti yang harus terlihat |
|---|---|---|
| L1 | Langkah 1 hijau | bagian "(d) DAFTAR PEMBLOKIR — 0", baris `CHECK HIJAU`, `exit=0` |
| L2 | Langkah 2 selesai dan foldernya ada | baris `PACK OK:` dan `exit=0`. Kalau exit non-nol, folder memang sudah dihapus — itu perilaku yang benar, bukan kegagalan alat |
| L3 | Langkah 3 hijau dua-duanya | validator repo: `WARNINGS: 0` + `exit=0`; validator sistem: `HASIL: PASS` + `exit=0` |
| L4 | Langkah 4 dan 5 bersih | `diff -r` langkah 4 **kosong** (`exit=0`). `diff -r` langkah 5 kosong, atau selisihnya HANYA berkas yang tercantum sebagai dikecualikan di `PAKET_REPO.md` — tidak boleh ada satu pun berkas yang **isinya** berbeda |
| L5 | Langkah 6 merah | `exit` non-nol dan pemblokirnya menyebut validator sistem yang hilang. Uji ini gagal kalau langkah 6 justru hijau |
| L6 | Angka bukti tidak basi | angka bukti yang dihitung dari korpus dokumen dilarang dikutip dalam sel Bukti; angka stabil tetap boleh dicatat. Jika isi paket bergeser, verifikasi ulang paket dan tulis entri baru tanpa mengutip angka korpus |
| L7 | paket tersedia bagi pemilik di luar sandbox (repo mandiri ter-push ATAU aset release dengan nama paket-<sistem>-<versi>-<sha>) | URL repo privat + commit ter-push, ATAU URL release di master privat + aset ZIP terunggah dan terverifikasi; draft tanpa aset tidak memenuhi langkah ini. Pointer: langkah 7 blok "Prosedur uji" + butir 4–7 bagian "Memindahkan paket ke luar sandbox" |

**Catatan pelaksanaan:** langkah 6 dijalankan di salinan sementara. Merusak master untuk keperluan uji dilarang. Bersihkan `/tmp/uji-*` setelah selesai; hasil pack tidak pernah di-commit ke master.

**Kenapa L6 ada (akar masalah B1/B2):** sebelum 8 Sep 2026, benih subset `_meta/` memindai SEMUA `.md` sistem, termasuk `ACCEPTANCE_TEST_LOG.md` (dokumen bukti). Akibatnya, menulis entri bukti ikut mengubah subset `_meta/` — angka yang baru dicatat langsung basi di sha berikutnya. Perbaikannya: benih = dokumen aktif saja (definisi tunggal di `tools/checkpoint_core.py`, dijelaskan di `_meta/PAKET_REPO_MANDIRI.md` bagian 3b). Dengan itu menulis bukti tidak mengubah isi paket, dan L6 menutup kelas regresi "bukti basi" secara terukur.


## AT-16 — Angka bukti volatile dipin ke SHA

**Given:** Log Evolusi, manifest, atau indeks mencatat bukti numerik.
**When:** angka itu adalah jumlah `rujukan` yang dapat berubah karena penulisan dokumen/log sesi.
**Then:** angka ditulis sebagai `(<n> pada <sha>)` atau tidak ditulis; verdict dan angka stabil tetap boleh/wajib dicatat. `tools/validate_repo.py` **gagal** bila sel kolom **Bukti** Log Evolusi memuat kata `rujukan` tanpa `pada <sha>`. Ini mencegah bukti basi (pelajaran empat siklus PR #21→#24).
