# Content Production Pipeline

### Alur kerja untuk memproduksi SATU konten (video/post), dari ide sampai siap publish. Dipakai berulang-ulang setiap hari kerja. Generik untuk semua channel, tapi setiap tahap WAJIB menyertakan konteks dari Channel Brief channel yang sedang dikerjakan — agent membaca sendiri dari repo, tidak perlu ditempel manual.

---

## Ini bukan alur kaku — kerangka tetap, detail fleksibel per Model Konten

6 tahap di bawah ini adalah **kerangka besar** yang berlaku umum untuk hampir semua jenis konten. Tapi detail KONKRET di dalam tiap tahap — terutama Tahap 4 (Breakdown) — bisa sangat berbeda tergantung format: video butuh breakdown per shot, infografis butuh breakdown per section, komik butuh breakdown per panel, dst. Detail ini **ditentukan per Model Konten saat sesi Discovery-nya sendiri** (`07_MODEL_KONTEN_DISCOVERY_PROMPT.md`), bukan dipaksakan seragam di sini.

Selain itu, tiap konten bisa butuh urutan yang sedikit berbeda: ada yang perlu riset dulu sebelum naskah, ada yang bisa loncat langsung dari ide ke breakdown visual, ada yang di tengah jalan memunculkan karakter baru yang perlu dikunci dulu. Agent membaca hasil tahap sebelumnya langsung dari repo dan melanjutkan ke tahap berikutnya sesuai konteks — tidak kaku harus 1-2-3-4-5-6 persis kalau memang konten ini butuh urutan lain.

**Kalau konten yang mau diproduksi punya Model Konten Brief** (`channel-[nama]/model-konten/[nama-model]/brief.md`, lihat `07_MODEL_KONTEN_DISCOVERY_PROMPT.md`): **cek dulu Mode-nya di bagian 4 file itu sebelum mulai.**
- Kalau Mode = "Ikuti Kerangka Standar" → dokumen ini tetap jadi KERANGKA DEFAULT, cek bagian "Override Ringan" di Model Konten Brief sebelum eksekusi tiap tahap — kalau tahap itu punya override (termasuk bentuk konkret Breakdown: shot/section/panel/dll), ikuti versi override-nya.
- Kalau Mode = "Alur Kerja Kustom" → dokumen ini **BUKAN acuan utama**. Ikuti tahapan yang didefinisikan di bagian "Alur Kerja Kustom" Model Konten Brief tersebut. Begitu alur kustom itu sampai di "titik pertemuan" (biasanya begitu 1 ide/bahan konkret sudah didapat), BARU lanjut ke tahap-tahap standar di dokumen ini mulai dari tahap yang relevan (biasanya Tahap 3 Naskah, tapi cek titik pertemuan yang tercatat di Model Konten Brief-nya).

**Status persisten wajib:** setiap konten yang mulai dikerjakan harus memiliki `_produksi-aktif/[channel]-[judul-konten]/STATUS.md` berdasarkan `_sistem/STATUS_TEMPLATE.md`. File ini minimal mencatat status, tahap terakhir selesai, tahap berikutnya, path output resmi, sumber konteks yang dibaca, approval, commit/PR terkait, pekerjaan yang belum tersimpan, dan risiko. Setelah setiap tahap yang menghasilkan dependency baru, agent memperbarui status dan memastikan output tersedia di branch. Jika sesi terputus dan status/output tidak dapat diverifikasi, agent harus berhenti dan meminta klarifikasi, bukan menebak atau mengulang diam-diam.

**Aturan yang mengikat di semua tahap:**

> Di setiap tahap, agent WAJIB sudah membaca Channel Brief channel ini (niche, Persona & Voice, Konsistensi Visual) DAN Model Konten Brief-nya kalau ada (format teknis, detail tahap spesifik, override) — ini terjadi otomatis lewat Entry Point Universal di awal sesi (`00_CARA_PAKAI_SISTEM.md`), tidak perlu ditempel manual. Jangan generate apapun untuk channel ini "polos" tanpa konteks brief-nya — ini yang paling sering menyebabkan brand voice buyar.

**Checkpoint & verifikasi konsistensi:** setiap kali pindah dari 1 tahap besar ke tahap besar berikutnya, agent WAJIB berhenti sejenak dan meringkas ulang apa yang sudah disepakati — dengan membaca ulang sumber resmi (Channel Brief, Bank Konsistensi Visual, Persona & Voice), bukan mengandalkan ingatan sesi. Di titik manapun, perintah **"cek konsistensi"** bisa dipanggil untuk membandingkan hasil kerja terbaru dengan sumber resmi.

---

## Alur 6 Tahap (Kerangka Besar)

```
Tahap 1: Ideation        → dari topik luas jadi 1 ide konten spesifik
Tahap 2: Konsep & Angle   → tentukan sudut pandang, hook, struktur besar
Tahap 3: Naskah/Script    → tulis naskah lengkap (dialog/voice over/caption)
Tahap 4: Breakdown Visual → pecah naskah jadi unit visual konkret yang perlu
                            digenerate (bentuk detailnya — shot/section/
                            panel/dll — mengikuti Model Konten Brief)
Tahap 5: Generate Asset   → eksekusi generate gambar per unit visual,
                            tersimpan sebagai file di _produksi-aktif/
Tahap 6: Assembly & Publish Prep → edit jadi final, siapkan caption/judul/
                            thumbnail, pindahkan naskah final ke arsip
```

Semua tahap ini bisa dikerjakan dalam 1 sesi lmarena Agent yang sama — tidak perlu pindah platform. Tahap 1-3 lebih banyak diskusi/tulis, Tahap 4-6 makin banyak melibatkan generate gambar (dan tools eksternal untuk video, karena agent belum bisa generate video langsung).

---

## Tahap 1: Ideation

**Tujuan:** dari "aku mau bikin konten tentang X" jadi 1 ide konkret yang layak dikembangkan.

**Input:** Bank Ide Awal di Channel Brief (bagian 7), arsip naskah channel (untuk menghindari pengulangan topik tanpa sadar), atau observasi/tren baru.

**Prompt:**
```
Sebelum mulai: baca channel-[nama-channel]/channel-brief.md (niche, target
penonton, tone) dan channel-[nama-channel]/arsip-naskah/indeks.md (topik
yang sudah pernah dibahas, untuk dihindari pengulangan tanpa sadar).

Aku mau bikin 1 konten baru untuk channel ini. [PILIH SALAH SATU:]
- Kembangkan salah satu ide dari Bank Ide Awal jadi lebih konkret
- Ini topik/observasi baru yang mau aku angkat: "[TULIS DI SINI]"
- Aku belum ada ide sama sekali, tolong usulkan beberapa berdasarkan niche
  channel ini

Kasih 3-5 opsi ide konkret (bukan cuma judul, tapi 2-3 kalimat "ini
tentang apa dan kenapa menarik buat target penonton channel ini"). Untuk
tiap opsi, sebutkan juga kenapa ini cocok/pas sama tone & positioning
channel ini, DAN cek dulu ke arsip naskah apakah topik serupa sudah pernah
dibahas — kalau iya, sebutkan itu dan tanyakan apakah memang sengaja mau
diulang (format beda, versi lebih panjang, dst) atau sebaiknya ganti opsi.

Setelah aku pilih 1 ide, lanjutkan ke Tahap 2 (Konsep & Angle) di dokumen
yang sama ini, kecuali Model Konten Brief channel ini menentukan urutan
lain.
```

**Output:** 1 ide konten terpilih, dengan pengecekan pengulangan topik sudah dilakukan.

---

## Tahap 2: Konsep & Angle

**Tujuan:** ide jadi kerangka konten — bukan naskah penuh, tapi struktur besarnya.

**Prompt:**
```
Ide konten yang mau dikembangkan (dari Tahap 1): "[IDE TERPILIH]"

Bantu susun kerangka konten ini, sesuai Persona & Voice dan Gaya Visual
channel ini yang sudah dibaca sebelumnya:
1. Hook/pembuka (khusus untuk platform channel ini — harus menarik dalam
   beberapa detik pertama)
2. Struktur besar isi (3-5 poin/beat utama, urutan yang logis)
3. Closing/CTA yang sesuai tujuan channel ini
4. Perkiraan durasi/panjang yang pas untuk format ini

JANGAN keluar dari gaya bahasa dan hal yang harus dihindari yang sudah
dikunci di Channel Brief.

Lanjutkan ke Tahap 3 (Naskah/Script) setelah kerangka ini dikonfirmasi.
```

**Output:** kerangka konten (bukan naskah penuh).

---

## Tahap 3: Naskah/Script

**Tujuan:** kerangka jadi naskah lengkap siap direkam/divisualisasikan.

**Prompt:**
```
Kerangka konten (dari Tahap 2): "[KERANGKA]"

Tulis naskah lengkap berdasarkan kerangka ini, dengan gaya bahasa/narasi
mengikuti Persona & Voice Channel persis — ini berlaku SELALU, baik ada
karakter visual maupun tidak.

[KALAU CHANNEL PUNYA KARAKTER UTAMA/TIPE A YANG BICARA:] Pastikan dialog
benar-benar sesuai Voice Profile karakter tersebut (dari Bank Konsistensi
Visual channel ini) — termasuk kosakata khas dan hal yang TIDAK PERNAH
dikatakan karakter ini. Jangan generic.

[KALAU NASKAH INI MEMUNCULKAN KARAKTER BARU YANG BELUM PERNAH ADA DI
CHANNEL INI SEBELUMNYA (karakter Tipe B, one-off untuk konten ini saja):]
Sebelum menuliskan deskripsinya, cek dulu ke arsip naskah channel apakah
karakter dengan ciri serupa sudah pernah dipakai sebelumnya — kalau ada
kecocokan, tawarkan untuk menaikkannya jadi karakter Tipe A permanen
sebelum lanjut. Kalau memang karakter baru, buatkan deskripsi ringkas
(fisik + peran dalam cerita ini) mengikuti format "Karakter Per-Konten" di
06_PROMPT_LIBRARY.md bagian A2 — ini akan disimpan menempel ke arsip
naskah konten ini nanti di Tahap 6.

Format naskah: [SEBUTKAN FORMAT YANG DIMAU, misal per-shot dengan timing,
atau paragraf voice over biasa, dst — atau ikuti format yang sudah
ditentukan di Model Konten Brief kalau ada]

Lanjutkan ke Tahap 4 (Breakdown Visual) setelah naskah ini dikonfirmasi.
```

**Output:** naskah final (disimpan sementara di `_produksi-aktif/[channel]-[judul-konten]/naskah-draft.md`) + deskripsi karakter Tipe B kalau ada.

---

## Tahap 4: Breakdown Visual

**Tujuan:** naskah dipecah jadi unit visual konkret yang harus digenerate — bentuk unitnya (shot/section/panel/dll) mengikuti yang ditentukan di Model Konten Brief channel ini.

**Prompt:**
```
Naskah (dari Tahap 3): "[NASKAH]"

[KALAU DARI TAHAP 3 ADA DESKRIPSI KARAKTER TIPE B YANG BARU MUNCUL:
sertakan deskripsi itu di sini secara otomatis, sudah terbawa dari tahap
sebelumnya]

Pecah naskah ini jadi daftar unit visual, sesuai bentuk yang ditentukan di
Model Konten Brief channel ini (shot untuk video, section untuk
infografis, panel untuk komik, dll — kalau Model Konten Brief belum
menentukan ini, gunakan "shot" sebagai default). Untuk tiap unit,
tuliskan:
1. Nomor unit & bagian naskah yang terkait
2. Deskripsi visual apa yang perlu ditampilkan
3. Prompt generate yang siap pakai — gabungkan Prompt Master dari Bank
   Konsistensi Visual (karakter Tipe A dan/atau elemen lain yang relevan)
   dan/atau deskripsi karakter Tipe B kalau muncul di unit ini, dengan
   detail spesifik unit ini: pose, ekspresi, environment, angle. Pastikan
   deskripsi karakter Tipe B dipakai SAMA PERSIS di semua unit yang
   melibatkan dia dalam konten ini.
4. File referensi visual yang harus disertakan saat generate (acuan utama,
   reference sheet, dll dari folder konsistensi-visual/ elemen terkait)

Simpan hasil ke _produksi-aktif/[channel]-[judul-konten]/breakdown-shot.md
(atau nama file sesuai bentuk unit yang dipakai).

Lanjutkan ke Tahap 5 (Generate Asset) setelah breakdown ini dikonfirmasi.
```

**Output:** daftar unit visual dengan prompt siap pakai per unit, tersimpan di `_produksi-aktif/`.

---

## Tahap 5: Generate Asset

**Tujuan:** eksekusi generate gambar per unit visual dari breakdown Tahap 4, tersimpan sebagai file asli di repo.

Ini tahap paling banyak melibatkan kemampuan generate gambar agent — lihat `06_PROMPT_LIBRARY.md` untuk teknik-teknik generate yang lebih spesifik (konsistensi karakter antar unit, dst). Untuk video (agent belum bisa generate video langsung): breakdown & prompt dari Tahap 4 dipakai di tools eksternal (Veo/Dreamina/dst), hasilnya diupload kembali ke folder yang sama di `_produksi-aktif/`.

**Checklist tiap generate:**
- [ ] Sudah menyertakan file referensi (acuan utama, reference sheet) dari Bank Konsistensi Visual yang relevan?
- [ ] Kalau ada karakter Tipe B di unit ini — sudah pakai deskripsi/gambar yang SAMA dengan unit lain yang melibatkan karakter itu di konten ini?
- [ ] Sudah sesuai Gaya Visual yang dikunci di Channel Brief?
- [ ] Kalau hasil meleset jauh dari referensi — jangan langsung dipakai, generate ulang atau perbaiki prompt dulu
- [ ] Untuk unit pertama yang memunculkan karakter Tipe B: hasil generate-nya jadi acuan untuk unit-unit berikutnya di konten yang sama
- [ ] Hasil sudah tersimpan sebagai file di `_produksi-aktif/[channel]-[judul-konten]/assets/`?

---

## Tahap 6: Assembly & Publish Prep

**Tujuan:** gabungkan semua asset jadi konten final, siapkan metadata publish, dan arsipkan naskah final.

**Prompt (untuk bagian metadata, bukan editing teknisnya):**
```
Konten yang sudah jadi tentang: "[RINGKASAN SINGKAT KONTEN INI]"

Buatkan:
1. 3-5 opsi judul/hook text (sesuai gaya platform channel ini)
2. Caption lengkap sesuai Persona & Voice channel ini
3. Hashtag/tag yang relevan
4. (kalau perlu thumbnail) deskripsi konsep thumbnail yang menarik klik
   tapi tidak menyesatkan (sesuai nilai di Brand Core soal tidak clickbait
   kalau itu berlaku)
```

**Setelah metadata siap, langkah penutup produksi (WAJIB, jangan dilewat):**
1. Pindahkan naskah final dari `_produksi-aktif/[channel]-[judul-konten]/naskah-draft.md` ke `channel-[nama-channel]/arsip-naskah/[tanggal]-[judul].md` — sertakan juga deskripsi karakter Tipe B kalau ada.
2. Update `arsip-naskah/indeks.md` dengan entri baru (judul, tanggal, topik singkat).
3. Konten produksi final termasuk kategori Besar — siapkan PR, direview isi lengkapnya dulu sebelum merge.
4. Setelah kamu download hasil akhirnya, folder `_produksi-aktif/[channel]-[judul-konten]/` boleh dihapus dari repo (breakdown dan asset visual itu sementara, sudah tidak diperlukan lagi setelah naskah dipindah ke arsip dan hasil didownload).

**Output:** konten siap publish + metadata lengkap + naskah final di arsip.

---

## Setelah publish

Setiap selesai 1 konten, ada 2 jenis hal yang mungkin dipelajari — bedakan keduanya supaya tau mana yang harus diupdate ke level atas dan mana yang cukup dicatat:

**Kalau yang dipelajari MENGUBAH sesuatu yang sudah dikunci** (Persona & Voice, Bank Konsistensi Visual, atau override di Model Konten Brief) — ini **WAJIB naik level**, jangan cuma dicatat di sini:
1. Update file level yang relevan (Channel Brief atau Model Konten Brief)
2. Catat perubahannya di Log Keputusan level tersebut, dengan tanggal & alasan
3. Contoh: "ternyata gaya bahasa yang dikunci di Persona & Voice kerasa terlalu formal pas dieksekusi nyata, harus disantaikan" → ini mengubah hal yang dikunci, wajib update Channel Brief. Ini termasuk kategori Besar — review isi lengkap sebelum merge.

**Kalau yang dipelajari cuma insight taktis** (berguna untuk konten berikutnya, tapi tidak mengubah apapun yang sudah dikunci) — cukup dicatat di **Bank Ide Awal** atau tambahan baru di bagian bawahnya pada Channel Brief/Model Konten Brief terkait, tidak perlu dianggap "perubahan resmi". Ini termasuk kategori Kecil — cukup dikonfirmasi ringan sebelum merge:
- Contoh: "hook jenis pertanyaan retoris ternyata lebih works dari hook pernyataan untuk model konten ini" → ini insight berguna, catat saja, tidak mengubah apapun yang sudah dikunci

**Kalau ragu masuk kategori mana** — tanya: "apakah ini mengubah definisi/aturan yang sudah ditetapkan, atau cuma menambah pengetahuan taktis buat eksekusi berikutnya?" Yang pertama wajib naik (kategori Besar), yang kedua cukup dicatat (kategori Kecil).
