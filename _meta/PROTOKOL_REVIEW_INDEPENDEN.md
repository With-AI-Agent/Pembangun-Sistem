# Protokol Review Independen (Sesi Lain)

## Tujuan
Verifikasi akhir atas pekerjaan yang berdampak permanen dilakukan oleh SESI AI LAIN yang tidak mengerjakan dan tidak menilai dirinya sendiri. Prinsip: yang mengerjakan tidak memutus; yang memutus tidak punya kepentingan. Ini lapisan eksternal dari `QUALITY_ASSURANCE_AND_EVOLUTION.md` — bukan pengganti validator/FI, melainkan penutup yang memutuskan apakah bukti boleh masuk main.

## Prinsip inti
1. Pemutus eksternal: verdict atas acceptance run, klaim DONE, atau perubahan terkunci dibuat oleh sesi yang berbeda dari penulis/subjek/pencatat (pola: pencatat ≠ subjek).
2. Reviewer hanya memverifikasi dari artefak (git tree, commit, log, API), bukan dari narasi pihak yang direview. Klaim pihak reviewed = objek pemeriksaan, bukan bukti.
3. Aturan merge: reviewer TIDAK meng-merge/menyetujui atas namanya sendiri, KECALI pemilik pekerjaan mengizinkan eksplisit di prompt. Tidak ada auto-merge, kapan pun.
4. Independensi: reviewer tidak menulis di branch subjek/penulis; read-only terhadap branch orang lain.
5. Batas jendela (6d generalisasi): selama jendela run/uji atau proses lain yang sedang berjalan, artefak yang dipublikasikan reviewer (komentar PR, log, branch) tidak boleh memuat rumusan jawaban/kriteria yang belum tertutup uji; gunakan pointer SHA+baris.
6. Proporsional: kedalaman review mengikuti level trigger di bawah; review bukan ritual untuk pekerjaan remeh.
7. Putaran terbatas: maksimal 2 putaran (review → koreksi → review ulang). Putaran ke-2 gagal = eskalasi ke pemilik untuk keputusan final (termasuk opsi membatalkan).
8. Append-only: hasil review dicatat apa adanya, termasuk RED FLAG dan verdict yang merevisi verdict sebelumnya; jangan menghapus riwayat, jangan menghaluskan.

## Level trigger
- L1 WAJIB review independen: menutup pengecualian/gate acceptance (mis. F-closed), menaikkan versi aturan (00/05/06 atau setara), perubahan struktural `_meta/`, operasi riwayat (reset/revert/fungsi-forcing), merge yang mengubah klaim DONE/manifest.
- L2 DISARANKAN review ringkas (checklist, tanpa formalitas prompt panjang): PR dokumentasi besar, perubahan template yang diwarisi sistem lain, sanitasi/redaksi.
- L3 TIDAK perlu: commit rutin produksi, typo, housekeeping reversibel, PR hygiene kecil tanpa perubahan aturan. Override dari L1 ke L3 wajib dicatat pemiliknya di log dengan alasan.

## Anatomi prompt reviewer (wajib berisi)
1. Identitas: "kamu reviewer independen PR #N; kamu memutuskan, bukan melanjutkan".
2. Objek ter-pin: nomor PR + SHA basis + SHA head.
3. Daftar pemeriksaan terverifikasi-able (append-only diff, grep audit, jalankan tools, cek status via API) — bukan pertanyaan opini.
4. Bila ada sengketa penilaian (mis. materialitas paparan): pertanyaan yang harus dijawab EKSPLISIT + kalimat "kamu satu-satunya pemutus; jangan menelan mentah penilaian pihak yang dinilai".
5. Batasan: aturan 6d di atas; larangan menyentuh branch orang; larangan mengutip jawaban selama jendela terbuka.
6. Mekanika putusan: hijau → komentar (status+pointer) lalu merge hanya jika diizinkan; merah → jangan merge apa pun, laporkan + perintah reproduksi, PR dibiarkan OPEN, keputusan ke pemilik.

## Sumber prompt (disetujui pemilik 8 Sep 2026)

Alasan perubahan: **mekanisme harus bisa dipakai tanpa perantara sesi.** Sebelum ini, pemilik hanya punya prompt review kalau ada sesi perantara yang mengarangnya — artinya pihak yang direview menulis instruksi bagi pengadilnya, dan matinya satu sesi berarti tidak ada prompt sama sekali.

1. **Prompt review dibangkitkan alat, bukan dikarang.** Sumber resminya tools/review_prompt.py. Semua nomor PR, base sha, head sha, dan daftar berkas berasal dari data PR di GitHub + isi pohon kerja, bukan dari narasi siapa pun.
2. **Sesi yang membuka PR WAJIB menempel keluaran alat itu sebagai SATU BLOK BERPAGAR di badan pesan chat terakhir sesi** (python3 tools/review_prompt.py --pr <N>), utuh, tanpa disunting. Keluaran perintah yang terlipat bukan bukti; kalau blok itu tidak ada di badan pesan, langkah penutupan BELUM dikerjakan dan PR belum boleh dinilai. Kalau blok itu tidak ada, pemilik harus membuka sesi baru dari main dan membangkitkan sendiri dengan `python3 tools/review_prompt.py --pr <N>`.
3. **Kalau sesi mati sebelum sempat**, pemilik membangkitkannya sendiri dengan perintah yang sama — tidak perlu menunggu sesi perantara, tidak perlu menulis ulang prompt.
4. **Larangan:** sesi yang direview TIDAK boleh mengarang, menambah, memotong, atau menyunting isi prompt review untuk dirinya sendiri. Kalau ia merasa reviewer butuh konteks tambahan, konteks itu masuk ke **body PR** (objek yang diperiksa), bukan ke prompt (instruksi pengadil).
5. Pemilik juga tidak perlu menulis ulang prompt: versi placeholder siap tempel ada di `PANDUAN_PENGGUNA.md` §"Minta Review, Tanpa Perantara", dibangkitkan python3 tools/review_prompt.py --generic.
6. Alat itu deterministik untuk data PR yang sama, tidak menulis berkas apa pun kecuali diminta `--out`, dan gagal keras (exit non-zero) daripada mencetak prompt dengan sha kosong.

## Penulisan hasil
- Meta: bagian baru di `_meta/ACCEPTANCE_TESTS.md` (log review per peristiwa singkat) atau `LOG_SESI` sesi reviewer; yang substantif di log acceptance sistem terkait.
- Sistem domain: subbagian append-only di ACCEPTANCE_TEST_LOG.md-nya ("Koreksi pasca-review independen" adalah pola yang benar).
- Aturan lama penulis tetap berlaku: yang dilarang tetap dilarang (6a/6b/6d), reviewer hanya menambah lapisan verifikasi, tidak menghapus kewajiban self-check sebelum review.

## Warisan ke sistem domain
Setiap sistem yang dibangun meta ini mengemban Protokol Review Independen dengan cara: (1) mendaftar L1/L2/L3 versinya di dokumen QA sistemnya; (2) menyebut "review independen" sebagai langkah wajib pada alur yang menutup klaim DONE/gate; (3) menyiapkan varian 1-baris trigger review di PROMPT_ENTRI/panduan penggunanya ("untuk [kategori pekerjaan], buka sesi baru dan tempel prompt reviewer sesuai protokol"). Sistem boleh menurunkan level hanya dengan override tercatat di manifest.
