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

## Sistem domain

- [ ] Discovery Level-0 selesai
- [ ] Semua butir `03_KONTRAK_WARISAN.md` (W-01…W-09) diterapkan dan tercatat di bagian "Warisan" rencana kerangka + manifest — atau override-nya tercatat dengan alasan + approval eksplisit pengguna
- [ ] `tools/validate_repo.py` PASS dengan 0 warning terhadap sistem ini (penegakan mekanis butir W-01…W-04)
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
