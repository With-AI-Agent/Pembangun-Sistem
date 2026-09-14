# Skrip Acceptance Test (AT-KL)

Uji end-to-end untuk memastikan Sistem Klinik bekerja dengan benar pada sistem target. Cakupan panggung: AT-KL-01/02 = panggung **SUNTIK** (target = fixture, kit disalin ke sana); AT-KL-03 = panggung **RAWAT INAP** (target = folder sistem di repo, master dibaca in-place — K-11).

## AT-KL-01: Idempotensi dan Penanaman Dasar
1. Salin `kit/` ke salinan `_fixture/sistem-kecil-sakit/` (sandbox di luar repo — kit tidak pernah ikut commit git).
2. Agent diinstruksikan merawat target (siklus penuh Tahap A–F + dua gerbang, sesuai 01_ALUR_RUN).
3. **Ekspektasi (Run 1):** Sistem target menerima W-01 s/d W-09 versi sederhana (misal, STATUS disisipkan ke README). Rekam klinik terbentuk. Kit terhapus (Tahap Lebur).
4. **Ekspektasi (Run 2):** Agent melaporkan tidak ada yang perlu diperbaiki karena target sudah sehat (Idempoten).
5. **Ekspektasi (Run 3 - Detektor Merah):** Ubah paksa `STATUS` di README target menjadi "rusak" lalu jalankan `validate_target.py` dari `alat/`. Harus exit 1.

## AT-KL-02: Cek Kit Basi (Fail-Closed) — hanya panggung suntik (kit tidak ada di panggung rawat inap, K-11)
1. Salin `kit/` versi lama (misalnya tanggal/versi di bawah `SYSTEM_MANIFEST.md`) ke target uji.
2. Jalankan Agent Klinik.
3. **Ekspektasi:** Agent menolak bekerja (fail-closed) pada Tahap B Diagnosis karena mendeteksi bahwa kit/ versi usang dibandingkan manifest, dan mewajibkan sinkronisasi/update kit terlebih dahulu.

*(AT ini dieksekusi secara manual oleh QA saat rilis versi baru)*

## AT-KL-03: Varian Rawat Inap (Target = Folder Sistem di Repo — K-11)
1. Buat salinan `_fixture/sistem-kecil-sakit/` di sandbox (mis. /tmp) yang direpresentasikan sebagai "folder sistem target yang diletakkan pemilik di repo ini". **SALINAN KIT TIDAK DIPAKAI** — panggung rawat inap membaca master `_sistem/01–06` in-place: tidak ada folder `kit/` di sandbox, tidak ada stamp, tidak ada `.gitignore` kerja untuk kit (tidak ada peleburan kit).
2. Agent menjalankan siklus rawat inap sesuai 01_ALUR_RUN §1.2/§12: pendaftaran (folder tamu diperlakukan utuh — Tahap A langkah 6), diagnosis berbasis katalog (read-only total), rencana + G-Rencana, tindakan (metode Kebijakan Lebur), verifikasi (alat portabel `kit/alat/validate_target.py` tetap dipakai — stdlib-only, tidak tahu bentuk repo; dibaca in-place dari repo), catatan (REKAM-KLINIK sesuai TEMPLATE-REKAM-KLINIK + cap versi kit berjalan + STATUS deterministik di target), panen.
3. **Ekspektasi (Run 1):** (a) NOL jejak kit di sandbox — tidak ada folder `kit/`, tidak ada stamp, tidak ada entri ignore kerja; (b) artefak IDENTIK dengan suntik (butir 1.6): laporan diagnosis, rencana, REKAM-KLINIK + cap versi, STATUS field deterministik; (c) `validate_target.py` exit 0 pasca-tanam; (d) PR yang dihasilkan = **PR meta normal** — deskripsinya menyebut TANPA auto-merge, merge = pemilik, dan sistem TETAP di repo sebagai warga kelas satu (bukan patch/download, bukan hapus-branch).
4. **Ekspektasi (Run 2 — idempoten):** ulangi pada salinan yang sama: REKAM-KLINIK dibaca duluan, semua mekanisme terverifikasi terpasang, rencana kosong, NOL perubahan (bukti: `git status` bersih / `git commit` menolak "nothing to commit").

*(AT ini dieksekusi oleh sesi penerapan K-11 dan di-re-run pada tiap audit ritme kit — 06_RITME_KIT §4; bukti memakai struktur + exit code, bukan angka volatil — C-04)*

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-14 | Menambahkan AT-KL-02 (Cek Kit Basi) | Memenuhi syarat dari 06_RITME_KIT.md §2 dan hasil eskalasi review putaran 2. |
| 2026-09-14 UTC / 15 Sep WIB | AT-KL-03 lahir (varian rawat inap: master in-place, tanpa salin kit, artefak identik, idempoten, PR meta normal) + teks AT-KL-01/02 disinkron ke dua panggung baru | K-11: varian panggung baru wajib terbukti mekanis seperti varian lain; sandbox di luar repo (pola AT-KL-01: kit/kerja tidak pernah masuk git) |
