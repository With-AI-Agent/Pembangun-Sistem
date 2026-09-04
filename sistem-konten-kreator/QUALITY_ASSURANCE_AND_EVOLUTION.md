# Quality Assurance & Evolution — Sistem Konten Kreator

## Status

- **Status:** aktif sebagai mekanisme default; sistem masih dalam remediation
- **Pemilik keputusan:** pengguna
- **Protokol induk:** `_meta/QUALITY_ASSURANCE_AND_EVOLUTION.md` pada master blueprint
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

## Status output

```text
Draft → Checked → Approved → Released → Observed
```

`Checked` bukan persetujuan publish. Output kategori Besar tetap harus direview pengguna sebelum merge/release.

## Log evolusi

| Tanggal | Lapisan | Observasi | Perubahan | Alasan | Bukti | Versi | Approval | Rollback |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
