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

**Melanjutkan setelah jeda = sync check WAJIB.** Setiap kali agent melanjutkan setelah jeda — jeda menunggu approval di gerbang, jeda sesi, atau kembali di jendela yang sama — agent WAJIB menjalankan sync check dengan `main` (aturan lengkap: `00_CARA_PAKAI_SISTEM.md`, Prinsip Checkpoint) SEBELUM mengeksekusi langkah berikutnya. Kata "lanjut"/"setuju" dari pemilik adalah approval isi, **bukan pengganti** sync check.

---

## Alur 6 Tahap (Kerangka Besar)

```
Tahap 1: Ideation        → dari topik luas jadi 1 ide konten spesifik
Tahap 2: Konsep & Angle   → tentukan sudut pandang, hook, struktur besar
Tahap 3: Naskah/Script    → tulis naskah lengkap (dialog/voice over/caption)
Tahap 4: Breakdown Output → pecah naskah jadi unit output konkret yang perlu
                            diproduksi (bentuk unitnya — shot/panel/section/
                            segmen audio/dll — mengikuti Model Konten Brief)
Tahap 5: Generate/Acquire Assets → hasilkan atau kumpulkan asset per unit
                            (generate gambar, rekam/siapkan audio, atau
                            tidak ada asset sama sekali untuk konten
                            teks-only), tersimpan di _produksi-aktif/
Tahap 6: Assembly & Publish Prep → edit jadi final, siapkan caption/judul/
                            thumbnail, pindahkan naskah final ke arsip
```

Semua tahap ini bisa dikerjakan dalam 1 sesi lmarena Agent yang sama — tidak perlu pindah platform. Tahap 1-3 lebih banyak diskusi/tulis, Tahap 4-6 makin banyak melibatkan generate gambar (dan tools eksternal untuk video, karena agent belum bisa generate video langsung).

---

## Gerbang Approval per Tahap

Definisi G1/G2/G3 ada di `00_CARA_PAKAI_SISTEM.md` (Prinsip Approval Bertingkat). Tabel ini menetapkan gerbang mana yang berlaku di tiap tahap, supaya agent tidak berhenti terlalu sering, tidak jalan terus tanpa izin, dan tidak menganggap "lanjut" sebagai "boleh merge".

| Tahap | Gerbang wajib | Apa yang ditanyakan | Catatan |
|---|---|---|---|
| 1. Ideation | **G1** | Ide terpilih sudah sesuai? Lanjut atau cari ide lain? | Belum ada yang dikunci; murah untuk diulang |
| 2. Konsep & Angle | **G1** | Kerangka/angle ini dipakai? | Kalau angle mengubah sesuatu yang dikunci di Channel Brief → naik jadi **G2** |
| 3. Naskah/Script | **G1 + G2** | G1: naskah cukup untuk lanjut? G2: naskah ini dikunci sebagai naskah final? | G2 wajib karena naskah final jadi dasar breakdown dan diarsipkan permanen |
| 4. Breakdown Output | **G1 + G2** | G1: breakdown sudah benar? G2: breakdown ini dikunci untuk generate asset? | G2 wajib karena generate asset memakai biaya/waktu nyata dan sulit dibatalkan setelah jalan |
| 5. Generate/Acquire Assets | **G1** | Asset hasil generate diterima, atau ada yang perlu regenerate? | Perubahan elemen Bank Konsistensi Visual di tengah jalan → **G2** terpisah |
| 6. Assembly & Publish Prep | **G2 + G3** | G2: konten final + metadata disetujui? G3: merge PR ke `main`? | Konten produksi final = kategori Besar, review isi lengkap sebelum merge |

**Aturan tambahan yang berlaku lintas tahap:**

- Kalau di tengah tahap manapun muncul kebutuhan mengubah **Brand Core, Channel Brief, Model Konten Brief, atau Bank Konsistensi Visual**, itu selalu **G2 tersendiri** — tidak boleh menumpang pada G1 tahap yang sedang berjalan, karena dampaknya keluar dari konten ini.
- Model Konten Brief boleh **menambah** gerbang (misal G2 tambahan untuk storyboard), tapi **tidak boleh menghapus** G2/G3 yang ada di tabel ini. Penambahan dicatat di brief model konten itu.
- Setiap gerbang yang lolos dicatat di `STATUS.md` dengan kodenya (`G1 Tahap 3 — disetujui [tanggal]`), bukan sekadar "sudah dikonfirmasi".

---

## Aturan Sumber Eksternal, Fakta, dan Hak Cipta

Berlaku setiap kali konten memakai bahan dari luar kepala sendiri: riset web, berita, data/statistik, kutipan, cerita orang lain, gambar/musik/footage pihak ketiga, atau adaptasi karya yang sudah ada. Sistem ini bisa menghasilkan konten yang konsisten secara brand tapi bermasalah secara fakta atau hak cipta — dua hal itu tidak saling menutupi, jadi diperiksa terpisah.

### Pencatatan sumber (wajib, sejak sumber pertama dipakai)

Begitu ada satu saja sumber eksternal dipakai, buat `_produksi-aktif/[channel]-[judul-konten]/SUMBER.md` dan isi terus selama produksi — jangan direkonstruksi belakangan dari ingatan:

| # | Klaim/bahan yang dipakai | Sumber (URL/judul/penerbit) | Tanggal akses | Jenis | Status verifikasi | Lisensi/hak | Atribusi wajib? |
|---|---|---|---|---|---|---|---|
| 1 | | | | fakta / data / kutipan / visual / audio / ide-adaptasi | `Terverifikasi` / `Belum` / `Tidak bisa diverifikasi` | | ya + bunyinya / tidak |

Aturan pengisian:

- **Tanggal akses wajib** — halaman web berubah dan bisa hilang; tanpa tanggal, klaim tidak bisa ditelusuri ulang.
- **`Terverifikasi`** hanya boleh dipakai kalau klaim itu benar-benar dicek, bukan karena "sumbernya kelihatan kredibel".
- Klaim berisiko (kesehatan, hukum, keuangan, keselamatan, tuduhan ke pihak tertentu, angka statistik spesifik, klaim sejarah) **wajib punya minimal 2 sumber independen** atau diturunkan bahasanya jadi tidak memastikan.
- Kalau agent tidak bisa memverifikasi, tulis `Tidak bisa diverifikasi` dan **laporkan ke pengguna** — jangan diam-diam tetap dipakai seolah sudah pasti.

### Gerbang fact-check dan rights-check

- **Tahap 3 (Naskah), bagian dari G2:** naskah tidak boleh dikunci sebelum setiap klaim faktual di dalamnya punya baris di `SUMBER.md` dengan status verifikasi terisi. Kalau ada yang `Belum`/`Tidak bisa diverifikasi`, agent menyebutkannya saat meminta G2 — pengguna yang memutuskan: verifikasi dulu, turunkan bahasanya, atau hapus klaimnya.
- **Tahap 5 (Generate/Acquire Assets), bagian dari G1:** referensi visual dari web boleh dipakai sebagai **arahan gaya/komposisi**, tidak boleh direproduksi mendekati aslinya. Karya berhak cipta yang masih dilindungi (karakter milik pihak lain, logo, foto berlisensi, musik) tidak boleh dijadikan asset final tanpa hak yang jelas. Agent WAJIB menolak dan menawarkan alternatif kalau permintaan mengarah ke sana, bukan mengerjakannya lalu memberi peringatan kecil.
- **Tahap 6 (Publish Prep), bagian dari G2:** atribusi yang ditandai wajib di `SUMBER.md` harus benar-benar sudah masuk ke caption/deskripsi/on-screen sesuai yang dicatat.

### Setelah konten selesai

`SUMBER.md` **ikut diarsipkan** bersama naskah final ke `arsip-naskah/[tanggal]-[judul]-sumber.md` sebelum folder produksi dihapus. Jejak sumber adalah satu-satunya cara menjawab keberatan/klaim yang muncul berbulan-bulan setelah publish — kalau ikut terhapus, konten tidak bisa dipertanggungjawabkan lagi.

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

**Gerbang G1** — lanjutkan ke Tahap 3 (Naskah/Script) setelah kerangka ini disetujui lanjut. Kalau angle yang dipilih ternyata mengubah sesuatu yang sudah dikunci di Channel Brief, hentikan dan ajukan **G2** terpisah dulu.
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

**Gerbang G1 + G2** — G1 untuk lanjut ke Tahap 4 (Breakdown Output), dan G2 untuk mengunci naskah ini sebagai naskah final (dasar breakdown sekaligus yang nanti diarsipkan permanen). Tanyakan keduanya eksplisit; jangan anggap "lanjut" sudah berarti naskah dikunci.

**Sebelum meminta G2:** kalau naskah ini memuat klaim faktual atau bahan dari sumber eksternal, jalankan gerbang fact-check — tiap klaim harus punya baris di `SUMBER.md` dengan status verifikasi terisi (lihat bagian "Aturan Sumber Eksternal, Fakta, dan Hak Cipta"). Sebutkan klaim yang masih `Belum`/`Tidak bisa diverifikasi` saat meminta G2.
```

**Output:** naskah final (disimpan sementara di `_produksi-aktif/[channel]-[judul-konten]/naskah-draft.md`) + deskripsi karakter Tipe B kalau ada.

---

## Tahap 4: Breakdown Output

**Tujuan:** naskah dipecah jadi unit output konkret yang harus diproduksi — bentuk unitnya mengikuti yang ditentukan di Model Konten Brief channel ini.

**Bentuk unit menurut jenis konten** (semuanya kasus normal, bukan pengecualian):

| Jenis konten | Unit | Asset yang dihasilkan Tahap 5 |
|---|---|---|
| Video | shot / scene | gambar per shot (atau footage dari tools eksternal) |
| Komik/carousel | panel / slide | gambar per panel |
| Infografis | section | gambar/grafik per section |
| Audio-only (podcast, narasi) | segmen audio | tidak ada asset visual; unit = blok naskah + arahan penyampaian, plus cover art kalau perlu |
| Teks-only (thread, artikel, caption panjang) | bagian/paragraf | **tidak ada asset sama sekali** — Tahap 5 hanya berisi verifikasi akhir, tidak ada yang digenerate |

Kalau konten ini **tidak memerlukan asset visual**, Tahap 4 tetap dijalankan (naskah tetap perlu dipecah jadi unit supaya konsisten dan bisa diperiksa), tapi kolom prompt generate dan file referensi visual **dikosongkan dengan keterangan eksplisit** — bukan diisi asal supaya formatnya penuh. Tahap 5 lalu dilewati dengan catatan di `STATUS.md`: `Tahap 5 — tidak berlaku (konten teks-only)`. Ini keputusan sadar yang tercatat, bukan tahap yang terlupakan.

**Prompt:**
```
Naskah (dari Tahap 3): "[NASKAH]"

[KALAU DARI TAHAP 3 ADA DESKRIPSI KARAKTER TIPE B YANG BARU MUNCUL:
sertakan deskripsi itu di sini secara otomatis, sudah terbawa dari tahap
sebelumnya]

Pecah naskah ini jadi daftar unit output, sesuai bentuk yang ditentukan di
Model Konten Brief channel ini (shot untuk video, panel untuk komik,
section untuk infografis, segmen untuk audio-only, bagian untuk teks-only
— kalau Model Konten Brief belum menentukan ini, tanyakan dulu, jangan
asumsikan "shot"). Untuk tiap unit, tuliskan:
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

Untuk konten tanpa asset visual (audio-only/teks-only): lewati poin 3 dan
4, tulis "tidak berlaku — konten [audio-only/teks-only]", dan sebagai
gantinya cantumkan arahan penyampaian per unit (tempo, penekanan, jeda)
yang konsisten dengan Persona & Voice channel ini.

Simpan hasil ke _produksi-aktif/[channel]-[judul-konten]/breakdown-output.md
(atau nama file sesuai bentuk unit yang dipakai, misal breakdown-shot.md).

**Gerbang G1 + G2** — G1 untuk lanjut ke Tahap 5 (Generate/Acquire Assets), dan G2 untuk mengunci breakdown ini sebagai dasar generate. G2 wajib di sini karena generate asset memakai biaya/waktu nyata dan sulit dibatalkan setelah jalan.
```

**Output:** daftar unit visual dengan prompt siap pakai per unit, tersimpan di `_produksi-aktif/`.

---

## Tahap 5: Generate/Acquire Assets

**Tujuan:** hasilkan atau kumpulkan asset per unit dari breakdown Tahap 4, tersimpan sebagai file asli di repo. "Acquire" karena tidak semua asset digenerate agent — ada yang direkam, diambil dari stok berlisensi, atau dibuat di tools eksternal.

**Kalau konten ini tidak punya asset** (teks-only): tahap ini dilewati, catat `Tahap 5 — tidak berlaku (konten teks-only)` di `STATUS.md`, lalu langsung ke Tahap 6. **Kalau audio-only:** yang dikumpulkan adalah file audio (rekaman/TTS) dan cover art kalau ada — checklist visual di bawah tidak berlaku, tapi konsistensi Persona & Voice tetap diperiksa.

Ini tahap paling banyak melibatkan kemampuan generate gambar agent — lihat `06_PROMPT_LIBRARY.md` untuk teknik-teknik generate yang lebih spesifik (konsistensi karakter antar unit, dst). Untuk video (agent belum bisa generate video langsung): breakdown & prompt dari Tahap 4 dipakai di tools eksternal (Veo/Dreamina/dst), hasilnya diupload kembali ke folder yang sama di `_produksi-aktif/`.

**Checklist tiap generate (untuk konten yang punya asset visual):**
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
2a. **Kalau konten ini memakai sumber eksternal:** pindahkan `_produksi-aktif/[channel]-[judul-konten]/SUMBER.md` ke `arsip-naskah/[tanggal]-[judul]-sumber.md`, dan pastikan atribusi yang ditandai wajib sudah benar-benar masuk ke caption/deskripsi/on-screen.
2b. **Kalau konten ini memakai karakter Tipe B:** update juga `arsip-naskah/indeks-karakter.md` — tambah baris baru untuk karakter yang belum pernah tercatat, atau tambahkan konten ini ke kolom **Konten lain** pada baris yang sudah ada. Ini WAJIB dan terpisah dari langkah 2: `indeks.md` tidak menyimpan ciri karakter, sehingga tanpa langkah ini pengecekan karakter berulang di produksi berikutnya (`06_PROMPT_LIBRARY.md` bagian A2 langkah 1) akan membaca indeks kosong. Lihat format minimumnya di bagian 9 `03_TEMPLATE_CHANNEL_BRIEF.md`.
3. **Gerbang G2 lalu G3** — konten produksi final termasuk kategori Besar. Minta **G2** dulu (konten final + metadata disetujui isinya), baru siapkan PR dan minta **G3** (izin merge ke `main`) sebagai pertanyaan terpisah. Dua-duanya dicatat di `STATUS.md`; jangan merge hanya berbekal G2.
4. **Buat arsip ringan reproducibility** — sebelum folder produksi dihapus, simpan `arsip-naskah/[tanggal]-[judul]-metadata.md` berisi jejak yang tidak ikut terbawa naskah:

   ```
   Model konten      : [nama model + versi brief yang dipakai]
   Versi brief       : Channel Brief v[x], Model Konten Brief v[y]
   Prompt final      : [prompt generate yang benar-benar dipakai per unit visual,
                        termasuk file referensi yang disertakan]
   Daftar asset      : [nama file + di mana disimpan di luar repo]
   Elemen konsistensi: [elemen Bank Konsistensi Visual yang dirujuk]
   Karakter Tipe B   : [kalau ada]
   Sumber eksternal  : [rujuk [tanggal]-[judul]-sumber.md kalau ada]
   Catatan produksi  : [hal yang perlu diketahui kalau konten ini dibuat ulang]
   ```

   Alasannya: naskah saja tidak cukup untuk membuat ulang atau melanjutkan konten ini nanti — prompt final dan versi brief yang dipakai justru bagian yang paling mudah hilang. Ini ringan (teks) sehingga asset berat tetap boleh disimpan di luar Git tanpa kehilangan jejak.

5. Setelah kamu download hasil akhirnya, folder `_produksi-aktif/[channel]-[judul-konten]/` boleh dihapus dari repo (breakdown dan asset visual itu sementara, sudah tidak diperlukan lagi setelah naskah dipindah ke arsip dan hasil didownload) — **syaratnya langkah 1, 2, 2a, 2b, dan 4 sudah benar-benar dilakukan**, karena setelah folder dihapus jejaknya tidak bisa diambil lagi. Agent WAJIB memverifikasi file arsip itu benar-benar ada sebelum menghapus, bukan menganggapnya sudah dibuat.

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
