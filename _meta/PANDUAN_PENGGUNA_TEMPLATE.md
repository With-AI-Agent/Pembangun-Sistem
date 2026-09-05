# Template Pegangan Pengguna — Sistem [Nama Sistem]

> Template untuk `PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` setiap sistem yang dibangun di repo ini. **WAJIB** ada di dalam folder sistem itu sendiri (self-contained — ikut terbawa kalau sistem diunduh jadi repo standalone; lihat `00_CARA_KERJA_META.md`, prinsip pegangan pengguna).
>
> **Aturan dua file:**
> 1. `PROMPT_ENTRI_UNIVERSAL.md` di root folder sistem — berisi **satu blok prompt pembuka** siap tempel + catatan pemakaian singkat. (Agent: file ini adalah sumber prompt pembuka; isinya boleh dirujuk dokumen sistem lain.)
> 2. `PANDUAN_PENGGUNA.md` (root folder sistem, atau subfolder `panduan/`) — pegangan lengkap bagi **pengguna**. Tandai jelas di awal: `agent_instruction: IGNORE for execution — USER GUIDE ONLY`. Agent **tidak boleh** memperlakukannya sebagai instruksi eksekusi kecuali diminta eksplisit.
>
> Standar yang dikejar: **sama mudahnya dipakai dengan meta-sistem ini sendiri** — pengguna cukup menempel SATU prompt pembuka, lalu agent otomatis terorientasi penuh (apa sistemnya, cara kerja, ketentuan, kondisi repo, PR menggantung) tanpa perlu ditempel manual.

---

## Isi WAJIB `PANDUAN_PENGGUNA.md` (per bagian)

### 1. Pembuka
- 1 paragraf: apa sistem ini, untuk siapa, hasil akhirnya apa (bahasa awam).
- Penanda `agent_instruction: IGNORE for execution — USER GUIDE ONLY` (+ penjelasan: dokumen ini untuk pengguna, bukan instruksi agent).

### 2. Prompt Pembuka Universal (PALING PENTING — wajib ada di paling atas setelah pembuka)
Blok prompt siap salin. Wajib memuat instruksi ke agent:
1. Baca dokumen entry point sistem (mis. `START_DI_SINI.md`) + dokumen cara-pakai/sistem utamanya.
2. Verifikasi kondisi branch/working tree (branch aktif `arena/...` dibuat otomatis platform; jangan asumsi `main`).
3. **Cek dan laporkan semua PR yang masih terbuka** (level repo — dari sistem/apapun, kalau multi-sistem).
4. Cek status sistem (manifest/index) dan laporkan ringkas.
5. Tanya tujuan sesi; berdasarkan jawaban, baca sendiri file yang relevan — tanpa perlu ditempel manual.
6. Jangan menulis/eksekusi apa pun sebelum tujuan sesi dikonfirmasi.

### 3. Prompt Penutup Sesi (wajib ada)
Blok prompt siap salin untuk akhir sesi. Wajib memuat instruksi ke agent:
1. Update `STATUS.md` unit kerja (tahap selesai, tahap berikutnya, waktu pembaruan).
2. Cek working tree — semua perubahan ter-commit dan ter-push (tanpa commit+push, sesi baru tidak bisa melanjutkan — fakta platform).
3. Update indeks sistem (kolom "terakhir disentuh" + status) kalau bekerja di suatu sistem.
4. Kalau kerja berlanjut lintas sesi: tulis laporan sesi/handoff sesuai template repo.
5. Ringkaskan kondisi akhir (commit terakhir, PR, langkah aman berikutnya).
6. Kalau PR akan di-merge: pastikan semua sudah push **sebelum** merge — setelah merge/close, sesi ini **tidak bisa push lagi** (fakta platform); kerja lanjutan harus dari sesi baru yang dibuka dari `main`.

### 4. Istilah (versi awam)
Repo, branch, `main`, commit, push, PR, merge — masing-masing 1–2 kalimat + analogi sederhana.

### 5. Kalimat pembuka untuk berbagai situasi
Minimal 3 situasi spesifik sistem ini (misal: mulai unit kerja baru, lanjut unit lama, revisi hasil, cek konsistensi/audit). Tiap situasi = 1 blok kalimat siap tempel.

### 6. Cara review & merge
Bagaimana pengguna meninjau hasil (PR), kapan merge, dan apa konsekuensinya (sesi tak bisa push pasca-merge).

### 7. Kebiasaan yang perlu dijaga
Checkpoint tiap tahap + commit & push; checkpoint diskusi ringan (diskusi >5 giliran mendekati keputusan); jangan lanjut kerja di sesi yang PR-nya sudah merge; workaround sesi crash (download workspace) + lanjut dari `STATUS.md`.

---

## Catatan kualitas

- Prompt pembuka/penutup harus **portabel**: memakai path relatif folder sistem, tidak menggandeng path repo meta — supaya tetap benar saat sistem berdiri sebagai repo standalone.
- Setiap perubahan aturan sistem yang memengaruhi alur sesi wajib diikuti pembaruan bagian 2–3 pegangan (agar satu-prompt tetep cukup).
- Pegangan ikut dicek kelengkapannya oleh validator sistem (lihat `validate_system.py` masing-masing) dan `tools/validate_repo.py` (file root sistem).
