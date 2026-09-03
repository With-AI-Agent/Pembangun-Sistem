# Behavioral Audit — Meta-Sistem dan Pilot

**Tanggal:** 3 September 2026  
**Status:** Simulasi perilaku selesai; validasi pengguna nyata dan recovery tool belum selesai.

## Metode

Audit dilakukan dengan menjalankan alur secara konseptual dari sudut pandang agent, bukan hanya mencocokkan nama file. Setiap tahap diperiksa terhadap input, konteks wajib, tindakan, output, gerbang, dan recovery.

## Hasil

| Skenario | Hasil | Catatan |
|---|---|---|
| Sesi repo baru | Lulus | Entry point mengarahkan baca manifest, quality, index, lalu bertanya tujuan |
| Sesi melanjutkan sistem | Lulus bersyarat | Manifest dan status tersedia; branch/PR aktual tetap harus diverifikasi tool |
| Discovery Level-0 | Lulus | Prompt memisahkan diskusi dari penulisan rencana |
| Sistem flat | Lulus | Pilot menandai Hierarki tidak berlaku tanpa memaksakannya |
| Sistem siklus | Lulus | Pilot memiliki enam tahap dengan output berantai |
| Sistem gabungan | Lulus struktural | Meta-system mendukung bentuk berbeda, tetapi belum diuji pada sistem kompleks |
| Output dengan sumber | Lulus | Pilot memisahkan fakta, inferensi, dan ketidakpastian |
| Quality output | Lulus | Checklist output hadir dan status tidak langsung dianggap approved |
| Self-improvement | Lulus struktural | Trigger, proposal, diskusi, regression, dan rollback ditentukan |
| Override | Lulus struktural | Manifest memuat alasan dan approval override |
| Sesi terputus | Lulus desain | STATUS tersedia; belum dilakukan pemutusan sesi agent aktual |
| Perubahan besar | Lulus desain | Perubahan tidak boleh langsung dilakukan tanpa proposal dan approval |
| Audit tanpa akhir | Lulus desain | Ada trigger, level, dan kondisi berhenti |
| Template bersih | Belum | Belum dibuat sebelum master lulus pilot |

## Temuan Behavioral

### B-01 — Entry point belum memiliki format laporan awal yang seragam

Agent diminta membaca dan melaporkan kondisi, tetapi belum ada format wajib untuk melaporkan branch, PR, status sistem, blocker, dan keputusan yang dibutuhkan. Ini membuat kualitas entry point masih bergantung pada gaya agent.

**Status:** Ditutup secara struktural. Format `SESSION_REPORT` sudah ditambahkan dan dipasang pada entry point.

### B-02 — “Relevan” masih merupakan keputusan agent

Meta-sistem sudah memiliki manifest dan tabel konteks sebagai arah, tetapi belum mewajibkan setiap sesi mencatat file yang dibaca dan alasan file kondisional tidak dibaca.

**Status:** Ditutup secara struktural. Session report memiliki `context read` dan `context skipped with reason`.

### B-03 — Recovery belum diuji secara failure injection

Desain STATUS terlihat memadai, tetapi belum diketahui apakah agent dapat benar-benar melanjutkan jika file berhenti di tengah penulisan, commit belum ada, atau dua output memiliki status berbeda.

**Perbaikan berikutnya:** lakukan simulasi failure injection pada setiap tahap pilot dan dokumentasikan expected behavior.

### B-04 — Quality protocol sudah lengkap tetapi berisiko menambah beban

Pilot menunjukkan protokol dapat dipasang, tetapi belum mengukur biaya waktu/kompleksitas dibanding manfaat. Ini harus diobservasi agar sistem tidak menjadi terlalu birokratis.

**Perbaikan berikutnya:** gunakan level Ringan/Sedang/Mendalam dan catat durasi/hasil pada pilot nyata.

## Keputusan Audit

- Meta-sistem **belum** diberi status Released.
- Pilot **belum** masuk index sebagai sistem aktif.
- Template bersih **belum** dibuat.
- Backup final **belum** dibuat.
- B-01 dan B-02 akan ditutup pada revisi entry point berikutnya.
- B-03 dan B-04 membutuhkan uji pilot yang melibatkan sesi agent dan/atau pengguna.

## Executable Failure-Injection Check

Pada tahap lanjutan, `tools/test_failure_injection.py` dijalankan terhadap state sementara yang mensimulasikan:

- output tanpa `STATUS.md`;
- status `released` tanpa output;
- status `blocked`;
- state sehat dengan output dan tidak ada pekerjaan yang belum tersimpan.

Hasil:

```text
FAILURE-INJECTION TESTS PASSED: 4 fail-closed scenarios
```

Tes ini memvalidasi kontrak file dan perilaku fail-closed secara deterministik. Ini belum menggantikan pengujian sesi agent yang benar-benar terputus atau review pengguna.


## Session Report Check

Pilot menghasilkan laporan sesi dengan branch, PR, konteks dibaca, konteks dilewati beserta alasan, output terakhir, blocker, dan tujuan sesi. Secara struktural ini menutup B-01 dan B-02 untuk jalur pilot. Verifikasi tool dan interaksi pengguna nyata tetap diperlukan untuk membuktikan perilaku di luar fixture.
