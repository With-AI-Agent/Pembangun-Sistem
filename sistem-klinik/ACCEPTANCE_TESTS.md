# Skrip Acceptance Test (AT-KL)

Uji end-to-end untuk memastikan kit Klinik bekerja dengan benar pada sistem target.

## AT-KL-01: Idempotensi dan Penanaman Dasar
1. Salin `kit/` ke `_fixture/sistem-kecil-sakit/`.
2. Agent diinstruksikan merawat target (Tahap A-E).
3. **Ekspektasi (Run 1):** Sistem target menerima W-01 s/d W-09 versi sederhana (misal, STATUS disisipkan ke README). Rekam klinik terbentuk. Kit terhapus (Tahap Lebur).
4. **Ekspektasi (Run 2):** Agent melaporkan tidak ada yang perlu diperbaiki karena target sudah sehat (Idempoten).
5. **Ekspektasi (Run 3 - Detektor Merah):** Ubah paksa `STATUS` di README target menjadi "rusak" lalu jalankan `validate_target.py` dari `alat/`. Harus exit 1.

## AT-KL-02: Cek Kit Basi (Fail-Closed)
1. Salin `kit/` versi lama (misalnya tanggal/versi di bawah `SYSTEM_MANIFEST.md`) ke target target uji.
2. Jalankan Agent Klinik.
3. **Ekspektasi:** Agent menolak bekerja (fail-closed) pada Tahap B Diagnosis karena mendeteksi bahwa kit/ versi usang dibandingkan manifest, dan mewajibkan sinkronisasi/update kit terlebih dahulu.

*(AT ini dieksekusi secara manual oleh QA saat rilis versi baru)*

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-14 | Menambahkan AT-KL-02 (Cek Kit Basi) | Memenuhi syarat dari 06_RITME_KIT.md §2 dan hasil eskalasi review putaran 2. |
