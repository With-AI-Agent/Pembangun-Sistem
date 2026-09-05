---
agent_instruction: IGNORE for execution — USER GUIDE ONLY
user_guide_only: true
purpose: Pegangan praktis pengguna Sistem Presentasi + sumber prompt pembuka & penutup sesi. Agent hanya membaca file ini jika diminta eksplisit oleh pengguna. Untuk instruksi eksekusi agent, baca dokumen di `START_DI_SINI.md` dan `_sistem/`.
---

# Pegangan Pengguna — Sistem Presentasi

### Dokumen ini UNTUK KAMU sendiri — sengaja masuk repo (dan ikut terbawa kalau sistem ini diunduh jadi repo tersendiri) supaya kamu selalu punya akses. **AGENT tidak boleh menganggap ini instruksi eksekusi kecuali kamu minta secara eksplisit.**

**Apa ini:** sistem untuk mengubah **bahan** (dokumenmu: PDF/Word/topik yang perlu diriset) menjadi **berkas presentasi** (default `.pptx`) yang setia pada sumbernya — setiap pernyataan berjejak halaman/URL, tidak ada yang dikarang, struktur berbasis bukti, dan prosesnya bisa dilanjutkan sesi lain kalau terputus. Consumer akhir = audiens presentasimu (misal dosen penguji sidang).

---

## Prompt Pembuka Universal (Gunakan Ini SETIAP Sesi Baru)

Salin blok di bawah ke chat pertama — dalam keadaan apa pun (deck baru, deck lanjutan, revisi, audit, cek status). Detailnya ada di `PROMPT_ENTRI_UNIVERSAL.md`.

```
Kamu adalah lmarena Agent yang terhubung ke repo sistem presentasi ini.
Sebelum melakukan apa pun:

1. Baca `START_DI_SINI.md` dan `SYSTEM_MANIFEST.md` di akar sistem.
2. Deteksi kondisi branch saat ini (baru/kosong vs lama/ada progres) dan cek working tree.
3. Cek dan laporkan status semua PR yang masih terbuka.
4. Cek status deck di `deck-aktif/` (baca `STATUS.md` tiap deck: tahap, gerbang G1/G2/G3) dan laporkan ringkas.
5. Tanyakan: "Apa tujuan sesi ini?" (deck baru dari bahan, lanjut deck, revisi deck, audit/cek konsistensi, atau lainnya)
6. Berdasarkan jawaban, baca sendiri file yang relevan (`_sistem/01–10`, dokumen living deck) — TANPA perlu aku tempel manual isinya.
7. Kalau melanjutkan deck, ikuti "Petunjuk pemulihan" di `STATUS.md` deck itu; jangan mengulang kerja yang sudah tercatat selesai.
8. Jangan mulai eksekusi/menulis file apa pun sebelum aku konfirmasi tujuan sesi ini sudah jelas.

Setelah itu, bawa aku langsung ke langkah yang tepat sesuai tujuan.
```

---

## Prompt Penutup Sesi (Gunakan di Akhir Sesi)

Sebelum menutup sesi — kerja mau di-merge, mau jeda, atau sesi sudah panjang — tempel ini supaya sesi berikutnya bisa melanjutkan tanpa kehilangan apa pun:

```
Tutup sesi ini dengan benar:
1. Update STATUS.md deck yang disentuh (tahap selesai, tahap berikutnya, waktu pembaruan).
2. Cek working tree: semua perubahan WAJIB ter-commit dan ter-push — tanpa itu sesi baru tidak bisa melanjutkan.
3. Kalau ada deck baru/selesai, pastikan folder deck lengkap (bahan + dokumen + skrip + keluaran) dan ter-commit.
4. Ringkaskan kondisi akhir: commit terakhir, status PR, dan langkah aman berikutnya.
5. Kalau aku mau merge PR: pastikan semua sudah push SEBELUM merge — setelah merge/close, sesi ini TIDAK BISA push lagi (batasan platform); kerja lanjutan harus dari sesi baru yang dibuka dari main.
```

---

## Istilah yang perlu kamu tahu (versi awam)

- **Repo** — folder besar di GitHub tempat semua dokumen sistem + deck-deckmu tersimpan. "Markas" kerja.
- **Branch** — "salinan kerja" repo. Tiap sesi agent otomatis dapat branch sendiri (nama `arena/...`), supaya kerja yang belum selesai tidak mengacaukan versi utama.
- **`main`** — versi utama yang dianggap bersih & siap dipakai.
- **Commit** — "menyimpan" perubahan di branch.
- **Push** — mengirim commit ke GitHub (bener-bener tersimpan; kalau sesimu crash dan belum push, kerja hilang).
- **PR (Pull Request)** — "usulan" memindahkan hasil branch ke `main`. Kamu review dulu.
- **Merge** — kamu setuju & menggabungkan PR ke `main`. Hasil kerja resmi jadi.
- **G1/G2/G3** — gerbang approval di sistem ini: **G1** = agent sudah paham bahannya (wajib untuk bahan besar), **G2** = outline + rencana visual disetujui, **G3** = berkas final disetujui. Agent wajib berhenti di tiap gerbang dan menunggu kamu.

**Analogi:** `main` itu dokumen asli yang penting; agent bikin salinan dulu, kerjanya di situ, lalu "mengusulkannya" (PR) ke kamu untuk digabung (merge).

---

## Kalimat Pembuka untuk Berbagai Situasi

### Situasi: Deck baru dari bahan (PDF/Word/topik)
```
Mau bikin deck baru. Bahannya: [sebutkan file/topik + tempel/link kalau ada].
Ikuti alur 5 tahap dari Tahap 1 (Brief) — jangan lompat ke build.
```

### Situasi: Lanjutkan deck yang sudah ada
```
Lanjutkan deck [nama]. Cek dulu STATUS.md-nya, laporkan sampai tahap mana
dan apa yang belum, baru kita lanjut.
```

### Situasi: Revisi deck (hasil kurang pas)
```
Revisi deck [nama]: [jelaskan apa yang kurang — isi/visual/struktur].
Jangan ubah yang sudah benar; catat revisinya di Log Keputusan deck.
```

### Situasi: Cek konsistensi / audit deck
```
Audit deck [nama]: cocokkan isi slide vs bahan (jejak halaman), cek
STATUS.md sinkron, jalankan qa_deck.py, laporkan temuan tanpa mengubah
apa pun dulu.
```

### Situasi: Diskusi dulu, belum mau agent menulis
```
Mau diskusi dulu, jangan tulis file apa pun: [topik diskusi].
```

---

## Cara Review & Merge

1. Hasil kerja agent selalu lewat **branch + PR** — tidak pernah langsung ke `main`.
2. Tinjau PR di GitHub (file apa yang berubah). Untuk deck: buka `preview.html` (hampiran — bukan render PowerPoint) dan/atau buka `.pptx`-nya sendiri (putusan final selalu di kamu).
3. **Gerbang G1/G2/G3 = kamu yang menyetujui**, lewat chat ("disetujui"/"perbaiki X") — agent mencatatnya di `STATUS.md` deck.
4. Merge PR **setelah kamu yakin**. Peringatan penting: **setelah PR di-merge, sesi agent yang membuat PR itu TIDAK BISA push lagi** (platform mencabut akses). Jadi: minta agent pastikan semua ter-push sebelum kamu merge, lalu buka sesi BARU (dari `main`) untuk kerja lanjutan.
5. Unduh berkas: di lingkungan lmarena, viewer/preview tidak bisa mengunduh biner — jalur unduh yang didukung = halaman file GitHub → *Download raw*.

---

## Kebiasaan yang Perlu Dijaga

- **Commit tiap tahap + push** — bukan birokrasi: kalau sesi crash (bisa terjadi kapan saja), yang belum di-commit hilang.
- **Checkpoint diskusi** — kalau diskusi sudah panjang (>5 giliran) dan mendekati keputusan, minta agent simpan ke file dulu.
- **Jangan lanjut kerja di sesi yang PR-nya sudah di-merge** — file baru akan terjebak. Buka sesi baru dari `main`.
- **Sesi crash?** — workaround resmi: tambahkan `/download-workspace` di akhir URL sesi (download zip), lalu buka sesi baru dan lanjut dari `STATUS.md` deck terakhir.
- **Bahan Arab/scan** — agent membacanya lewat jalur "visi" (render halaman → dibaca), bukan ekstraksi teks mentah. Kalau halaman penting perlu, minta agent tunjukkan buktinya (halaman mana yang dibaca).

---

## Kalau Ada yang Bingung

Baca `START_DI_SINI.md` (peta sistem untuk agent), atau mulai sesi baru dengan **Prompt Pembuka Universal** di atas — agent akan laporkan kondisi sistem dan bertanya apa yang kamu mau. Kalau ada PR lama yang menggantung dari sesi sebelumnya, agent juga wajib melaporkannya di awal sesi.
