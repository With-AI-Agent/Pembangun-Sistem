# Quality Assurance & Evolution — Sistem Konten Kreator

## Status

- **Status:** aktif sebagai mekanisme default; sistem masih dalam remediation
- **Pemilik keputusan:** pengguna
- **Protokol induk (provenance — dokumen ini tetap berfungsi tanpanya):** _meta/QUALITY_ASSURANCE_AND_EVOLUTION.md pada master blueprint
- **Override:** tidak ada

## Lapisan 1 — Memeriksa sistem ini sendiri

Audit dipicu ketika terjadi drift berulang, perubahan tool AI, perubahan struktur repo, perubahan aturan produksi, atau temuan pilot. Agent menulis temuan dan proposal terlebih dahulu; tidak mengubah Channel Brief, pipeline, atau aturan konsistensi secara diam-diam. Perubahan besar memerlukan review isi dan PR.

Minimum regression check:

- [ ] Entry point masih menunjuk ke file yang benar
- [ ] Hierarki Brand Core → Channel → Model Konten → Produksi tetap konsisten
- [ ] Pipeline standar dan workflow custom tidak saling bertentangan
- [ ] Prosedur checkpoint/recovery masih dapat dijalankan
- [ ] Arsip dan indeks masih memiliki data yang dibutuhkan
- [ ] Klaim kemampuan tool masih sesuai toolset aktual
- [ ] Acceptance test di `ACCEPTANCE_TESTS.md` dijalankan ulang untuk skenario yang terdampak perubahan (wajib kalau yang berubah aturan di `00`/`05`/`06`)
- [ ] Pekerjaan L1 (lihat level trigger di bawah) sudah melewati review independen sesi lain sebelum klaim ditutup

## Review independen (sesi lain) — level trigger KK

Rujukan: `PROTOKOL_REVIEW_INDEPENDEN.md` (root sistem); protokol induk: _meta/PROTOKOL_REVIEW_INDEPENDEN.md di master (meta v1.4.0; provenance). Reviewer = sesi yang berbeda dari penulis/subjek/pencatat; memverifikasi dari artefak; tidak meng-merge tanpa izin eksplisit pemilik.
- **L1 (WAJIB review independen):** penutupan pengecualian/gate (mis. F), bump versi aturan `00`/`05`/`06`, operasi riwayat (reset/revert/fungsi-forcing), perubahan `SYSTEM_MANIFEST.md` yang memuat klaim (DONE/versi/gate).
- **L2 (DISARANKAN review ringkas):** mengikuti protokol induk (PR dokumentasi besar, perubahan template, sanitasi/redaksi).
- **L3 (TIDAK perlu):** commit produksi biasa, typo, housekeeping reversibel.

## Lapisan 2 — Memeriksa kesehatan sistem saat digunakan

Setelah produksi, catat observasi berikut jika relevan:

- apakah brief cukup spesifik untuk dieksekusi ulang;
- apakah voice/visual drift terjadi;
- apakah tahap tertentu sering diulang;
- apakah status produksi dan arsip lengkap;
- apakah workflow standar/custom membingungkan;
- apakah kebutuhan baru perlu menjadi aturan permanen atau cukup insight taktis.

Perubahan pada Brand Core, Channel Brief, Model Konten Brief, dan Bank Konsistensi Visual adalah perubahan Besar. Insight taktis boleh dicatat sebagai perubahan Kecil selama tidak mengubah keputusan yang dikunci.

## Lapisan 3 — Memeriksa output

Sebelum output dianggap released, agent memeriksa sesuai jenisnya:

### Naskah dan metadata

- [ ] Sesuai Channel Brief dan Model Konten Brief
- [ ] Persona & Voice konsisten
- [ ] Klaim faktual memiliki sumber atau ditandai sebagai opini/fiksi
- [ ] Tidak ada bagian draft yang tertinggal
- [ ] Metadata publish tidak menyesatkan
- [ ] Deskripsi karakter Tipe B ikut diarsipkan jika dipakai

### Visual/audio/asset

- [ ] Reference pack yang relevan digunakan
- [ ] Hasil tidak menyimpang dari elemen yang dikunci tanpa alasan
- [ ] Asset eksternal memiliki sumber dan hak penggunaan yang jelas
- [ ] File dapat dibuka dan formatnya sesuai
- [ ] Output yang dipakai pengguna sudah diunduh sebelum folder sementara dihapus

## Pengeluaran jadi repo mandiri

Sistem ini harus tetap lolos validasi ketika foldernya dikeluarkan jadi repo sendiri — protokol + cara mengujinya di _meta/PAKET_REPO_MANDIRI.md (repo master; provenance); di sisi sistem, alat yang menilai isinya adalah `_sistem/validate_system.py` yang ikut folder ini.

## Status output

```text
Draft → Checked → Approved → Released → Observed
```

`Checked` bukan persetujuan publish. Output kategori Besar tetap harus direview pengguna sebelum merge/release.

## Log evolusi

| Tanggal | Lapisan | Observasi | Perubahan | Alasan | Bukti | Versi | Approval | Rollback |
|---|---|---|---|---|---|---|---|---|
| 2026-09-04 | 1 | Dry run AT-KK-05 menemukan tabel "Konteks Wajib per Jenis Sesi" baris *Lanjut produksi yang terputus* tidak memuat langkah verifikasi output terhadap branch, dan satu-satunya rujukan ke _meta/PROTOKOL_CHECKPOINT_RECOVERY.md di master hanya untuk field `Pekerjaan belum tersimpan` di `STATUS_TEMPLATE.md` | Rujukan protokol recovery ditambahkan ke baris tabel itu + 4 aturan recovery mengikat di `00_CARA_PAKAI_SISTEM.md` | Agen yang patuh pada tabel bisa melewati verifikasi branch, sehingga FI-02 (output diklaim ada tapi hilang) dan FI-03 (output belum commit) tidak terdeteksi | Minimum regression check 6/7 item terverifikasi — detail di `ACCEPTANCE_TEST_LOG.md` bagian "Regression check 0.3.1". Item ke-7 (acceptance test diulang) **sengaja belum dicentang**: AT-KK-05/05b baru dry run di 0.3.0, run bersih di 0.3.1 belum dilakukan. tools/validate_repo.py PASS 29 file/16 dokumen/41 referensi | `0.3.1-audit-remediation` | Menunggu review PR #5 | Revert commit `002702f` + commit perbaikan ini; tidak ada data produksi yang berubah |
