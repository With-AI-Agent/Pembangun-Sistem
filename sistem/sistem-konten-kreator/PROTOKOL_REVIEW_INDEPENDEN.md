# Protokol Review Independen — Varian Sistem Konten Kreator

**Protokol induk:** _meta/PROTOKOL_REVIEW_INDEPENDEN.md di master (meta v1.4.0; provenance). Dokumen ini mengemban protokol induk di sistem ini dan menambah 3 ketentuan spesifik KK. Prinsip inti, level trigger umum, anatomi prompt reviewer, mekanika putusan, dan penulisan hasil mengikuti induknya — bagian ini hanya menambah, tidak mengurangi (yang dilarang induk tetap dilarang).

## Tambahan spesifik KK

1. **Penutupan pengecualian/gate (mis. F):** prompt reviewer **WAJIB** memuat permintaan **audit paparan** — apa yang tersedia di `main` (basis run) vs apa yang tercatat dibaca subjek — dan **materialitas paparan dinilai reviewer**, bukan pencatat/penjadwal. (Dasar: cacat metode M1 pada Run 5 — paparan rumusan jawaban pra-keputusan — ditutup oleh aturan 6d + orkestrasi Run 7/8; rinciannya di `ACCEPTANCE_TEST_LOG.md`.)
2. **Pesan pencatatan run uji tidak boleh dipegang sesi subjek (M2):** peran pencatat run dijalankan sesi yang terpisah dari sesi subjek; pola pencatat ≠ subjek adalah prasyarat LULUS, bukan opsional.
3. **Jendela run aktif — berlaku untuk reviewer juga (6d):** selama jendela sebuah run uji sedang berjalan, laporan review/pencatatan pihak lain (termasuk reviewer) hanya boleh di-push setelah jendela tersebut tertutup, atau diredaksi dari rumusan klausul expected result (rujukan pola 6d di `ACCEPTANCE_TESTS.md`); selama jendela terbuka, gunakan pointer SHA+baris.

## Level trigger KK (pendaftaran sesuai warisan protokol induk)

- **L1 (WAJIB review independen):** penutupan pengecualian/gate (mis. F), bump versi aturan `00`/`05`/`06`, operasi riwayat (reset/revert/fungsi-forcing), perubahan `SYSTEM_MANIFEST.md` yang memuat klaim (DONE/versi/gate/acceptance).
- **L2 (DISARANKAN review ringkas):** mengikuti protokol induk — PR dokumentasi besar, perubahan template yang diwarisi sistem lain, sanitasi/redaksi.
- **L3 (TIDAK perlu):** commit produksi biasa, typo, housekeeping reversibel. Override dari L1 ke L3 wajib dicatat pemiliknya di log dengan alasan.
