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

## Sistem domain

- [ ] Discovery Level-0 selesai
- [ ] Bentuk sistem dan batasannya terdokumentasi
- [ ] Manifest tersedia dan lengkap
- [ ] Entry point tersedia
- [ ] Pegangan pengguna tersedia di dalam folder sistem (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` — prompt pembuka + penutup; sesuai `_meta/PANDUAN_PENGGUNA_TEMPLATE.md`)
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
- [ ] Failure mode penting sudah diuji
- [ ] Verifikasi output diuji terhadap contoh nyata
- [ ] Self-improvement tidak berjalan tanpa trigger dan acceptance criteria
- [ ] Prosedur backup dan restore berhasil diuji
- [ ] Batasan sistem dipahami pengguna
- [ ] Perubahan besar setelah rilis memiliki jalur migrasi
