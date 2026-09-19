# Definition of Done — Meta-Sistem

Dokumen atau sistem **tidak boleh disebut selesai hanya karena file sudah ditulis**. Status selesai harus memenuhi checklist yang sesuai.

## Dokumen hasil

- [ ] Tujuan dan consumer jelas
- [ ] Input, proses, output, dan lokasi output jelas
- [ ] Status dokumen jelas
- [ ] Dependency dirujuk dengan path yang valid
- [ ] Tidak ada placeholder yang tidak disengaja
- [ ] Log keputusan tersedia jika dokumen hidup
- [ ] Approval sesuai tingkat risiko sudah diberikan
- [ ] Perubahan sudah di-commit
- [ ] PR sudah diproses sesuai aturan
- [ ] Penutupan sesi: PR dibuka → keluaran `tools/review_prompt.py --pr <N>` harus muncul sebagai satu blok berpagar di badan pesan chat terakhir, bukan keluaran perintah yang terlipat; kalau blok itu tidak ada, langkah penutupan dianggap BELUM dikerjakan dan PR belum boleh dinilai. Pemilik dapat membuka sesi baru dari main dan membangkitkan sendiri dengan `python3 tools/review_prompt.py --pr <N>` (`PROTOKOL_REVIEW_INDEPENDEN.md` §"Sumber prompt")
- [ ] Penyerahan prompt review/audit ke pemilik memuat **path absolut berkas + link** (link PR, permalink head, daftar berkas berubah) — dicetak alat sebagai BLOK SERAH TERIMA, bukan ditulis tangan (`PROTOKOL_REVIEW_INDEPENDEN.md` aturan 11)
- [ ] **Kuorum dilaporkan PER PUTARAN, dan putaran yang sedang berjalan tidak diganti nomornya** — `python3 tools/ambil_verdict.py --pr <N> --harapkan <jumlah hakim> [--putaran R]` mencetak blok KUORUM PER PUTARAN (agregat lintas putaran tetap fail-closed), dan prompt yang dibangkitkan ulang pada head yang sama tetap menamai putaran yang sedang berjalan (`hitung_putaran()`: kuorum belum lengkap ATAU head belum bergerak sejak verdict → putaran tetap). Nilai beku dari API tidak pernah dilabeli "SEKARANG": ujung branch base diukur terpisah dan pergerakannya dinyatakan (`PROTOKOL_REVIEW_INDEPENDEN.md` aturan 9 amendemen + aturan 12 dan 13)
- [ ] **Berkas bukti historis tidak disunting** — `ACCEPTANCE_TEST_LOG.md`, `LOG_SESI_*`, `DISKUSI_MENTAH_*`, laporan audit bertanggal, folder `_log-sesi/` dan arsip: kolom delesi harus 0 di bawah blok header, dan cacat tabel di sana cukup peringatan (keputusan pemilik 18 Sep 2026). Dokumen hidup/normatif tetap kegagalan keras (`tools/validate_repo.py` `POLA_BUKTI_HISTORIS`, dikunci TI6/TI7)
- [ ] **Link yang diserahkan adalah link ke BERKAS PROMPT ITU SENDIRI**, bukan hanya link ke PR — pemilik dan siapa pun yang membuka sesi hakim harus bisa membuka dan menyalin teks prompt tanpa akses ke mesin kerja agent. Caranya `python3 tools/review_prompt.py --pr <N> --out <path> --umumkan`: prompt ditempel ke kanal PR sebagai komentar penulis (BUKAN verdict, teruji lintas alat di regresi RP13) dan permalink-nya dicetak di blok serah terima. Kalau kanal itu tidak tersedia, agent wajib menyatakannya dan menempelkan teks prompt sebagai satu blok berpagar di badan pesan (`PROTOKOL_REVIEW_INDEPENDEN.md` aturan 11 amendemen giliran 20)

## Sistem domain

- [ ] Discovery Level-0 selesai
- [ ] Semua butir `03_KONTRAK_WARISAN.md` (W-01…W-10) diterapkan dan tercatat di bagian "Warisan" rencana kerangka + manifest — atau override-nya tercatat dengan alasan + approval eksplisit pengguna
- [ ] `tools/validate_repo.py` PASS terhadap sistem ini (penegakan mekanis butir W-01…W-04), dan baris `WARNINGS: N` dikutip apa adanya di laporan. **Warning tier hanya sah untuk berkas bukti historis yang append-only** (keputusan pemilik 18 Sep 2026 — riwayat tidak disunting demi kosmetika tabel); **warning di dokumen hidup berarti butir ini BELUM lulus**. Syarat lama (validator lulus tanpa satu pun peringatan) **dilaporkan tidak terukur oleh hakim putaran 4 review PR #74, lalu dicabut oleh penulis PR atas izin pemilik (giliran 22: perbaiki semua temuan), dengan dasar warning tier keputusan pemilik 18 Sep 2026** — hakim melaporkan, pemilik memutuskan, penulis melaksanakan. **Koreksi atribusi 19 Sep 2026** (temuan #2 hakim putaran 5: kalimat lama menulis pencabutan itu dilakukan oleh hakim, padahal hakim tidak berwenang mencabut syarat penerimaan); riwayat angkanya ada di `_meta/FAILURE_INJECTION_TESTS.md` (RP17, dan RP19 yang memindai pola janji gerbang di seluruh dokumen normatif hidup).
- [ ] Bentuk sistem dan batasannya terdokumentasi
- [ ] Manifest tersedia dan lengkap
- [ ] Entry point tersedia
- [ ] Pegangan pengguna tersedia di dalam folder sistem (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` — prompt pembuka + penutup; sesuai `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`)
- [ ] Mekanisme log sesi (`LOG_SESI`) diturunkan ke dalam folder sistem + prompt pembuka memuat langkah recovery log + prompt penutup memuat langkah menutup log
- [ ] Semua generator/template wajib tersedia
- [ ] Semua living document memiliki status dan log keputusan
- [ ] Jalur normal dan jalur recovery diuji
- [ ] Acceptance tests yang relevan di `ACCEPTANCE_TESTS.md` lulus
- [ ] Handoff prompt tersedia untuk sesi baru bila pekerjaan berlanjut lintas sesi
- [ ] Cross-reference dan dependency diverifikasi
- [ ] Audit minimal satu putaran selesai
- [ ] Ringkasan cadangan sinkron
- [ ] Index meta-sistem diperbarui
- [ ] Tidak ada PR terkait yang menggantung
- [ ] Versi rilis ditetapkan

## Siap dipakai produksi

Selain checklist sistem domain, harus ada:

- [ ] Pilot end-to-end berhasil
- [ ] Folder sistem adalah deliverable mandiri: `python3 tools/check_selfcontained.py --sistem <sistem> --report` exit 0. Alat menyalin hanya folder sistem, menjalankan `_sistem/validate_system.py` di salinan, menolak rujukan ke diri sendiri berprefiks folder, menolak rujukan ke satu BERKAS `_meta/`/`tools/` tanpa salinan berlabel, dan menolak salinan turunan basi/tanpa label. Cakupan penegakannya = dokumen aktif (satu definisi bersama): dokumen bukti/mentah tidak ditegakkan tetapi rujukannya terdaftar sebagai rujukan historis, penyebutan area berbentuk direktori bukan kegagalan, dan area yang tidak boleh keluar dari master diminta sebagai provenance tanpa backtick — bukan sebagai salinan. Aturan lengkap: `_meta/PAKET_REPO_MANDIRI.md`; skenario ujinya AT-17
- [ ] Failure mode penting sudah diuji
- [ ] Verifikasi output diuji terhadap contoh nyata
- [ ] Self-improvement tidak berjalan tanpa trigger dan acceptance criteria
- [ ] Prosedur backup dan restore berhasil diuji
- [ ] Batasan sistem dipahami pengguna
- [ ] Perubahan besar setelah rilis memiliki jalur migrasi
