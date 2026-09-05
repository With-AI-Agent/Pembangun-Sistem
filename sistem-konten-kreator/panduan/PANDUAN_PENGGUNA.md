---
agent_instruction: IGNORE for execution — USER GUIDE ONLY
user_guide_only: true
folder: panduan/
purpose: Panduan praktis pengguna + sumber prompt universal — agent hanya membaca file ini jika diminta eksplisit oleh pengguna. Untuk instruksi eksekusi agent, baca dokumen di `_sistem/`.
---

# Panduan Pengguna — Sistem Konten Kreator (GitHub + lmarena Agent)

### Dokumen ini UNTUK KAMU sendiri — bukan bagian dari 10 dokumen sistem, tapi SENGAJA MASUK REPO supaya kamu selalu punya akses. AGENT TIDAK BOLEH MENGANGGAP INI SEBAGAI INSTRUKSI EKSEKUSI KECUALI KAMU MINTA SECARA EKSPLISIT. File ini berisi panduan praktis, pedoman, dan juga **prompt pembuka universal** yang bisa kamu pakai dalam keadaan apa pun.

---

## Prompt Pembuka Universal (Gunakan Ini Setiap Sesi Baru)

Salin atau arahkan agent untuk membaca bagian ini di awal setiap sesi — baik sesi baru, sesi lanjutan, diskusi, produksi konten, pembuatan channel, atau apa pun:

```
Kamu adalah lmarena Agent yang terhubung ke repo sistem konten kreator ini.
Sebelum melakukan apa pun:

1. Baca `_sistem/START_DI_SINI.md` dan `_sistem/00_CARA_PAKAI_SISTEM.md`
2. Deteksi kondisi branch saat ini (baru/kosong vs lama/ada progres?)
3. Cek dan laporkan status semua PR yang masih terbuka
4. Tanyakan: "Apa tujuan sesi ini?" (misal: mulai dari nol, buat channel baru,
   produksi konten, revisi, diskusi, cek konsistensi, atau lainnya)
5. Berdasarkan jawaban, baca sendiri file sistem yang relevan — TANPA
   perlu aku tempel manual isinya
6. Jangan mulai eksekusi/menulis file apa pun sebelum aku konfirmasi tujuan
   sesi ini sudah jelas

Setelah itu, bawa aku langsung ke langkah yang tepat sesuai tujuan.
```

> Catatan: prompt ini dirancang supaya kamu cukup masukkan ini di chat pertama, lalu di chat kedua (atau dalam sesi yang sama setelah agent memahami) kamu tinggal jelaskan apa yang kamu mau. Agent sudah tahu semua konteks sistem.

---

## Prompt Penutup Sesi (Gunakan di Akhir Sesi)

Sebelum menutup sesi — mau merge, mau jeda, atau sesi sudah panjang — tempel ini supaya sesi berikutnya bisa melanjutkan tanpa kehilangan apa pun (ditambahkan 5 Sep 2026; aturan meta-sistem mewajibkan pegangan pengguna memuat prompt pembuka **dan** penutup):

```
Tutup sesi ini dengan benar:
1. Update STATUS.md unit kerja yang disentuh (tahap selesai, tahap
   berikutnya, waktu pembaruan).
2. Cek working tree: semua perubahan WAJIB ter-commit dan ter-push —
   tanpa itu sesi baru tidak bisa melanjutkan.
3. Ringkaskan kondisi akhir: commit terakhir, status PR, dan langkah
   aman berikutnya.
4. Kalau aku mau merge PR: pastikan semua sudah push SEBELUM merge —
   setelah merge/close, sesi ini TIDAK BISA push lagi (batasan
   platform); kerja lanjutan harus dari sesi baru yang dibuka dari main.
```

---

## Istilah yang perlu kamu tahu (versi awam)

- **Repo** — folder besar di GitHub tempat semua dokumen sistem dan hasil kerja kamu tersimpan. Ibaratnya "markas" tempat semua file hidup.
- **Branch** — semacam "salinan kerja" dari repo. Setiap kali kamu buka sesi baru di lmarena Agent, dia otomatis bikin 1 salinan kerja sendiri, supaya kerjaan yang belum selesai tidak mengacaukan versi utama.
- **`main`** — versi "asli/utama" dari repo, yang dianggap sudah bersih dan siap dipakai. Ini otomatis ada begitu kamu bikin repo baru di GitHub.
- **Commit** — semacam "menyimpan" perubahan yang sudah dibuat.
- **Push** — mengirim perubahan yang sudah di-commit itu ke GitHub (supaya benar-benar tersimpan di sana, bukan cuma di komputer/sesi kerja).
- **PR (Pull Request)** — permintaan untuk memindahkan hasil kerja dari branch (salinan kerja) ke `main` (versi utama). Ini semacam "usulan" yang kamu review dulu sebelum disetujui.
- **Merge** — tombol "setujui dan gabungkan" — begitu kamu klik ini di GitHub, hasil kerja di PR itu resmi masuk ke `main`.

**Analogi sederhana:** bayangkan `main` itu dokumen Google Docs asli yang penting, dan tiap kali kamu minta agent kerja, dia bikin salinan dulu untuk coba-coba. Begitu hasilnya bagus, dia "usulkan" (PR) supaya salinan itu dipindahkan ke dokumen asli — dan kamu yang klik setuju (merge).

---

## Langkah 1 — Bikin Repo Baru (sekali di awal)

1. Buka GitHub, buat repo baru (nama bebas, misal `sistem-konten-kreator`).
2. Begitu dibuat, GitHub otomatis kasih kamu branch `main` — kamu tidak perlu bikin ini manual.
3. Upload ke repo itu **10 dokumen sistem** apa adanya, tanpa diedit:
   - `_sistem/START_DI_SINI.md`
   - `_sistem/00_CARA_PAKAI_SISTEM.md`
   - `_sistem/01_BRAND_CORE.md`
   - `_sistem/02_CHANNEL_DISCOVERY_PROMPT.md`
   - `_sistem/03_TEMPLATE_CHANNEL_BRIEF.md`
   - `_sistem/04_CHARACTER_BUILDER_KIT.md`
   - `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md`
   - `_sistem/06_PROMPT_LIBRARY.md`
   - `_sistem/07_MODEL_KONTEN_DISCOVERY_PROMPT.md`
   - `_sistem/08_TEMPLATE_MODEL_KONTEN_BRIEF.md`
4. Pastikan file-file ini masuk langsung ke `main` (bukan ke branch lain) — ini fondasi awal yang harus bersih.
5. **Kebiasaan penting:** jangan pernah hapus branch `main` selama repo ini masih dipakai, meskipun terlihat "tidak ke-update". Kalau ada yang terasa tidak sesuai, itu biasanya karena ada PR yang belum di-merge — bukan karena `main`-nya salah.

---

## Langkah 2 — Hubungkan lmarena Agent ke Repo

Ikuti cara lmarena menghubungkan ke repo GitHub (sesuai yang sudah pernah kamu lakukan sebelumnya). Setiap kali kamu buka sesi baru, kamu bisa memilih repo dan branch mana yang mau dipakai.

---

## Langkah 3 — Kalimat Pembuka untuk Berbagai Situasi

### Situasi: Mulai dari nol total (belum ada Brand Core)

```
Aku baru mulai pakai sistem ini. Tolong baca dulu `_sistem/START_DI_SINI.md` dan
`_sistem/00_CARA_PAKAI_SISTEM.md` dari repo ini untuk paham struktur sistemnya.
Setelah itu, bantu aku mulai dari `_sistem/01_BRAND_CORE.md`.
```

### Situasi: Punya ide channel baru

```
Aku mau bikin channel baru. Tolong jalankan proses di
`_sistem/02_CHANNEL_DISCOVERY_PROMPT.md`.
```

### Situasi: Mau bangun karakter/latar/elemen visual untuk channel yang sudah ada

```
Channel [nama channel] sudah ada, aku mau bangun [karakter / latar / dll]
untuk channel ini. Tolong jalankan proses di `_sistem/04_CHARACTER_BUILDER_KIT.md`.
```

### Situasi: Mau bikin cara produksi/format baru dalam channel yang sudah ada

```
Untuk channel [nama channel], aku mau bikin model konten baru. Tolong
jalankan proses di `_sistem/07_MODEL_KONTEN_DISCOVERY_PROMPT.md`.
```

### Situasi: Mau produksi 1 konten

```
Aku mau produksi konten untuk channel [nama channel], model konten
[nama model konten kalau ada]. Tolong baca dulu semua file yang relevan,
lalu mulai dari `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md`.
```

### Situasi: Mau diskusi dulu, belum mau agent langsung eksekusi/menulis file

Tambahkan ini SEBELUM kalimat permintaanmu:
```
Sebelum mulai: aku mau diskusi dulu, jangan langsung tulis atau commit
apa pun ke repo sampai aku bilang "oke, tulis sekarang".
```

### Situasi: Lanjut sesi lama yang belum di-merge

1. Waktu mulai sesi baru, pilih branch lama yang mau dilanjutkan (bukan biarkan dia bikin branch baru).
2. Cukup ketik:
```
Lanjutkan kerjaan di branch ini.
```
Agent akan otomatis membaca apa yang sudah dikerjakan di branch itu sebelum bertanya lebih lanjut.

### Situasi: Merasa hasil kerja mulai melenceng dari yang sudah disepakati

```
Cek konsistensi.
```
Agent akan membandingkan hasil kerja terbaru dengan Channel Brief, Bank Konsistensi Visual, dan Persona & Voice yang sudah dikunci, lalu melaporkan kalau ada yang melenceng.

### Situasi: Hasil suatu tahap kurang pas, mau diulang

```
Hasil tahap [sebutkan, misal "Naskah"] ini kurang pas karena: [jelaskan].
Tolong ulang dengan arahan tambahan: [arahan baru].
```

---

## Langkah 4 — Cara Review & Merge

Setiap kali agent selesai mengerjakan sesuatu yang penting (Brand Core, Channel Brief, Bank Konsistensi Visual, Model Konten Brief, atau konten final), dia akan menyiapkan **PR** dan memberitahumu.

**Untuk hal-hal besar ini (kategori Besar) — WAJIB kamu baca dulu isinya** sebelum klik merge di GitHub. Jangan asal setuju.

**Untuk hal-hal kecil** (catatan, ide-ide, log), agent cukup tanya ringan "boleh di-merge?" — kamu bisa jawab cepat tanpa perlu baca detail.

**Cara merge di GitHub (garis besar):** buka PR yang dimaksud di GitHub, baca perubahannya, kalau sudah oke klik tombol "Merge pull request".

---

## Langkah 5 — Kebiasaan yang Perlu Dijaga

1. **Selalu merge sebelum lanjut kerjaan lain yang beda tujuan** di sesi yang sama — kalau belum sempat, boleh, tapi ingat kerjaan itu masih "menggantung" sampai di-merge.
2. **Jangan hapus branch `main`** apapun alasannya — kalau ada yang terasa aneh (misal hasil kerja lama "tidak update"), itu biasanya soal PR yang belum di-merge, bukan `main`-nya salah.
3. **Setiap sesi baru (kecuali lanjut di jendela chat yang sama)**, agent akan otomatis cek PR yang menggantung dan tanya kamu mau kerjakan apa — ini bagian dari sistem yang sudah dirancang supaya kamu tidak perlu ingat semuanya sendiri.
4. **Kalau ragu apakah harus mulai sesi baru atau lanjut yang sekarang** — aturannya: kalau kerjaan sebelumnya sudah di-merge, boleh lanjut kerjaan lain di sesi yang sama. Kalau belum di-merge dan mau kerjakan hal lain yang beda tujuan, sebaiknya sesi baru.

---

## Kalau Ada yang Bingung

Kembali ke `_sistem/START_DI_SINI.md` di repo untuk peta singkat, atau `_sistem/00_CARA_PAKAI_SISTEM.md` untuk penjelasan lebih lengkap soal cara kerja sistem ini secara keseluruhan.
