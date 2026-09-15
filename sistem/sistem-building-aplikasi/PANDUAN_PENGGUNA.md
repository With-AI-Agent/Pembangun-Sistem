---
agent_instruction: IGNORE for execution — USER GUIDE ONLY
user_guide_only: true
purpose: Pegangan praktis pemilik Sistem Building Aplikasi + sumber prompt pembuka & penutup sesi. Agent hanya membaca file ini jika diminta eksplisit atau via prompt entri.
---

# Pegangan Pengguna — Sistem Building Aplikasi

**Apa ini:** sistem untuk membangun **aplikasi** untuk kamu yang **tidak paham coding sama sekali**. Kamu cukup cerita ide (mentah pun jadi) — agent yang mengurus diskusi Fondasi (6 dokumen: Discovery → PRD → Tech Spec → Agent Guide → Roadmap → Cross-Check) lalu eksekusi Coding task demi task sampai aplikasi jadi. Hasil akhir = aplikasi yang bisa dipakai + fondasi yang bisa dilanjutkan sesi lain tanpa kamu jelaskan ulang.

---

## Prompt Pembuka Universal (Gunakan Ini SETIAP Sesi Baru)

Salin blok di bawah ke chat pertama — dalam keadaan apa pun (fondasi, coding, audit, siklus baru). Detailnya ada di `PROMPT_ENTRI_UNIVERSAL.md` (identik).

```
Cek dulu apakah ada file PROJECT_STATE.md di root repo ini.

Kalau TIDAK ADA (repo kosong/baru): ini proyek baru. Baca AGENT_SYSTEM.md di repo ini secara penuh (di folder sistem-building-aplikasi/ bila sistem ini ada di repo meta, atau di root bila sudah jadi repo standalone), lalu mulai dari TAHAP 1 (Discovery) sesuai AGENT_SYSTEM.md.

Kalau ADA: baca isinya, lihat nilai STATUS-nya, lalu ikuti instruksi yang sesuai di AGENT_SYSTEM.md untuk STATUS tersebut (FONDASI_TAHAP_2_PRD s/d CODING_AKTIF / SIKLUS_BARU).

Setelah kamu tahu posisi kita:

1. Baca SYSTEM_MANIFEST.md dan STATUS.md di folder sistem-building-aplikasi/ (atau root bila standalone) untuk paham identitas, tahap, dan pekerjaan belum tersimpan.
2. Verifikasi kondisi branch/working tree — branch arena/... dibuat otomatis platform lmarena; jangan asumsi main. Laporkan branch aktif, commit terakhir, dan working tree bersih/kotor.
3. Cek dan laporkan semua PR yang masih terbuka (gh pr list --state all) — PR menggantung dari sesi lama bisa membuatmu bekerja dari dasar ketinggalan.
4. Cari file LOG_SESI_*.md terbaru (di _log-sesi/ atau folder sistem-building-aplikasi/_log-sesi/). Kalau keadaannya OPEN, BACA dan laporkan keadaan sesi sebelumnya SEBELUM bertanya tujuan — jangan minta aku menjelaskan ulang konteks yang sudah tercatat di sana.
5. Laporkan posisi: sedang di tahap/fase apa, dan apa yang akan kamu kerjakan sekarang — sebelum mulai bekerja.
6. Berdasarkan jawabanku tentang tujuan sesi, baca sendiri file yang relevan (/docs/*, PROJECT_STATE.md, DECISIONS_LOG.md) — TANPA perlu aku tempel manual.
7. Jangan menulis/eksekusi apa pun sebelum tujuan sesi dikonfirmasi.

Sebagai langkah TERAKHIR nanti sebelum sesi ini berakhir (baik karena tahap/task selesai, atau karena aku minta checkpoint), WAJIB update PROJECT_STATE.md + STATUS.md + tutup LOG_SESI (CLOSED) supaya sesi berikutnya tahu harus lanjut dari mana.
```

---

## Prompt Penutup Sesi (Gunakan di Akhir Sesi)

Sebelum menutup sesi — kerja mau di-merge, mau jeda, atau sesi sudah panjang — tempel ini:

```
Tutup sesi ini dengan benar:
1. Update PROJECT_STATE.md (STATUS + DETAIL + UPDATE TERAKHIR) sesuai tahap/fase yang baru selesai — tulis tahap BERIKUTNYA sebagai STATUS.
2. Update STATUS.md di folder sistem-building-aplikasi/ (tahap selesai, tahap berikutnya, pekerjaan belum tersimpan = Tidak ada, waktu pembaruan = YYYY-MM-DD — peristiwa).
3. Tutup log sesi ini: file _log-sesi/ — isi final "Keadaan Sesi" (yang selesai, yang terbuka, langkah berikutnya) dan tandai CLOSED kalau tuntas (atau OPEN + "dilanjutkan di ...").
4. Cek working tree: semua perubahan WAJIB ter-commit dan ter-push — tanpa itu sesi baru tidak bisa melanjutkan (fakta platform).
5. Kalau ada /docs baru/selesai, pastikan sudah ter-commit dan PROJECT_STATE sudah menunjuk tahap berikutnya.
6. Ringkaskan kondisi akhir: commit terakhir, status PR, dan langkah aman berikutnya.
7. Kalau aku mau merge PR: pastikan semua sudah push SEBELUM merge — setelah merge/close, sesi ini TIDAK BISA push lagi (batasan platform); kerja lanjutan harus dari sesi baru yang dibuka dari main.
```

---

## Istilah yang perlu kamu tahu (versi awam)

- **Repo** — folder besar di GitHub tempat semua dokumen + kode aplikasimu tersimpan. "Markas" kerja.
- **Branch** — "salinan kerja" repo. Tiap sesi agent otomatis dapat branch sendiri (`arena/...` atau `tahap-1-discovery`), supaya kerja yang belum selesai tidak mengacaukan versi utama.
- **`main`** — versi utama yang dianggap bersih & siap dipakai. Hasil kerja baru masuk sini setelah kamu **merge**.
- **Commit** — "menyimpan" perubahan di branch.
- **Push** — mengirim commit ke GitHub (baru bener-bener aman; kalau sesi crash sebelum push, kerja hilang).
- **PR (Pull Request)** — "usulan" memindahkan hasil branch ke `main`. Kamu review dulu, baru merge.
- **Merge** — kamu setuju & menggabungkan PR ke `main`. Hasil kerja resmi jadi.
- **PROJECT_STATE.md** — file penunjuk "kita lagi di tahap apa" — dibaca otomatis agent tiap sesi, supaya kamu nggak perlu jelaskan ulang.
- **DECISIONS_LOG.md** — catatan keputusan teknis nyata selama coding (misal: "RLS pakai policy X") — wajib dibaca sebelum ubah area berisiko.
- **Fondasi vs Coding** — Fondasi = 6 dokumen perencanaan (belum ada kode); Coding = eksekusi task di ROADMAP jadi kode betulan.

**Analogi:** `main` itu naskah asli yang penting; agent bikin fotokopian (branch), corat-coret di situ, lalu "mengusulkan" (PR) untuk ditempel ke naskah asli (merge).

---

## Kalimat Pembuka untuk Berbagai Situasi

### Situasi: Mau mulai aplikasi baru (ide masih mentah)
```
Aku mau bikin aplikasi baru. Ide mentahnya: "[tulis ide kamu di sini, se-mentah apa pun]".
Pakai Prompt Pembuka di atas, mulai Tahap 1 Discovery — gali dulu sebelum tulis dokumen.
```

### Situasi: Lanjutkan Fondasi (sudah ada /docs sebagian)
```
Lanjutkan Fondasi. Cek PROJECT_STATE.md dulu — kita di tahap berapa? Lanjut diskusi tahap itu sampai aku bilang "cukup, tulis draftnya".
```

### Situasi: Lanjutkan Coding (Fondasi sudah beres)
```
Lanjutkan Coding. Baca PROJECT_STATE.md, ROADMAP.md (mana yang [x] dan [ ]), dan DECISIONS_LOG.md dulu — baru eksekusi task berikutnya sesuai TECH_SPEC & AGENT_GUIDE.
```

### Situasi: Audit / cek konsistensi sebelum lanjut
```
Tolong audit dulu sebelum lanjut. Cek konsistensi /docs (Tahap 6 Cross-Check) — apakah ada yang tidak sinkron antara PRD, TECH_SPEC, dan ROADMAP? Laporkan temuan + saran perbaikan.
```

### Situasi: Mau bikin siklus baru (v1, v2 setelah MVP jadi)
```
Aku mau mulai siklus baru v1. Versi yang sudah jalan: [MVP/v1]. Konteks tambahan:
- Yang sudah bagus: [...]
- Yang bermasalah: [...]
- Feedback nyata: [...]
- Ide fitur baru: [...]
Ikuti Tahap 0.5 di AGENT_SYSTEM.md.
```

---

## Cara review & merge

1. Agent kerja di branch → commit + push → buka PR (tanpa auto-merge).
2. Kamu buka PR di GitHub, lihat file yang berubah (tab Files changed).
3. Kalau oke → **Merge pull request** (tombol hijau). Kalau belum → tulis komentar di PR, agent perbaiki di sesi baru.
4. **Setelah merge, sesi itu tidak bisa push lagi** — ini batasan platform lmarena, bukan aturan kita. Kerja lanjutan = buka sesi baru dari `main`.

---

## Kebiasaan yang perlu dijaga

- **Checkpoint tiap tahap/task + commit & push** — jangan tunda.
- **Log sesi berkelanjutan** (`_log-sesi/`) — agent update setelah tiap pertukaran penting, header "Keadaan Sesi" selalu segar, `CLOSED` di akhir. Kalau sesi crash, sesi baru baca log `OPEN` itu — kalau tidak ada, backstop = `PROJECT_STATE.md` + `STATUS.md`.
- **PROJECT_STATE.md selalu di-update sebagai langkah TERAKHIR** setiap sesi — tanpa ini sesi baru buta.
- **Jangan lanjut kerja di sesi yang PR-nya sudah merge** — file baru akan terjebak tidak bisa di-push. Buka sesi baru.
- **DECISIONS_LOG wajib dibaca** sebelum ubah Area Berisiko Tinggi — jangan tebak dari kode.
- Kalau sesi panjang dan agent mulai ngawur: tempel prompt **"STOP dulu sebelum lanjut kerja. Aku mau kamu melakukan Checkpoint & Handoff..."** (lihat AGENT_SYSTEM.md §Checkpoint & Handoff).

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-15 | Pegangan dibuat pada run klinik pertama (rawat inap, kit v0.2.0) — G-Rencana 1-9 disetujui | W-01: sistem belum punya pegangan (PANDUAN_PEMAKAIAN lama melarang masuk repo) — pegangan baru mengikuti template meta 2-file identik, portabel untuk repo standalone |
