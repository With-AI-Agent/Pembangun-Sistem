---
agent_instruction: reference_only
active: false
document_type: historical_audit
---

> **REFERENSI HISTORIS — BUKAN INSTRUKSI AKTIF.**
> Dokumen ini adalah catatan audit migrasi yang sudah selesai dieksekusi (per 1 September 2026). Agent **tidak boleh** memperlakukan isinya sebagai aturan kerja yang berlaku sekarang: keputusan di dalamnya sudah dituangkan ke dokumen instruksi aktif (`00`–`08`), dan sebagian sudah berubah oleh audit berikutnya. Baca file ini **hanya** kalau perlu menelusuri alasan historis sebuah keputusan, atau kalau pengguna memintanya secara eksplisit.
>
> Kalau isi file ini bertentangan dengan dokumen instruksi aktif, **dokumen aktif yang menang** — dan konflik itu wajib dilaporkan, bukan ditebak. Karena sifatnya historis, file ini **dikecualikan dari template bersih**.

# Audit Migrasi — Sistem Lama (Chat Manual) → Sistem Baru (GitHub + lmarena Agent)

### Dokumen ini adalah HASIL AUDIT, bukan revisi final. Isinya: setiap asumsi di 10 dokumen lama yang berubah/perlu diputuskan ulang karena sekarang ada akses baca-tulis repo GitHub via agent + kemampuan generate gambar dalam sesi yang sama. Setiap poin butuh KEPUTUSAN kamu sebelum dokumen sumbernya direvisi — dokumen ini tidak menebak jawabannya untukmu.

---

## Fakta dasar yang jadi acuan audit ini (dari yang kamu sampaikan)

- lmarena Agent bisa baca DAN tulis ke repo GitHub kamu
- lmarena Agent bisa generate gambar dalam sesi kerja yang sama (belum jelas untuk video — kemungkinan perlu tools lain seperti Veo/Dreamina)
- Repo yang dipakai sama terus, tapi tiap sesi/percakapan baru otomatis membuat branch baru (TERVERIFIKASI, lihat Kategori 1)
- **Di awal tiap sesi, kamu bisa memilih repo DAN branch mana yang mau dipakai** — termasuk melihat daftar nama branch yang sudah ada (baru maupun lama yang belum di-merge) dan memilih salah satu secara sengaja. Ini fakta penting untuk mekanisme "lanjut kerjaan lama di sesi/chat baru" (lihat 2.1 bagian entry point universal).
- Tujuan kamu: hasil maksimal, bukan cepat. Semua penyesuaian yang relevan harus tercakup, tidak boleh ada yang kelewat.

---

## KATEGORI 1 — Fakta Teknis TERVERIFIKASI (hasil tes langsung ke lmarena Agent, 31 Agustus 2026)

Sudah diuji langsung (bukan tebakan lagi) di repo `resto-pro2` (repo lain, dipakai kebetulan untuk tes — BUKAN repo sistem konten). Semua di bawah ini fakta terkunci, kecuali disebutkan sebaliknya.

### 1.1 Perilaku branch per sesi — TERKONFIRMASI
- **Ya, otomatis.** Tiap sesi baru dapat branch sendiri, agent tidak pernah kerja langsung di `main`.
- **Pola nama bukan acak:** `arena/[kode-sesi-hex]-[nama-repo]`, contoh `arena/01a055b6-resto-pro2`.
- **Tidak pernah auto-merge.** Agent selalu berhenti di level Pull Request, menunggu kamu review & merge manual. (Dikonfirmasi juga: agent secara teknis PUNYA akses tool untuk merge PR, tapi alur kerja yang didesain tetap mewajibkan PR untuk direview manusia dulu — bukan keterbatasan teknis, tapi memang aturan main yang dipegang.)
- **Temuan tambahan (di luar rencana tes awal, penting — SUDAH DIKOREKSI, lihat Catatan Revisi):** repo `resto-pro2` ditemukan tanpa branch `main` saat tes. **Penyebabnya BUKAN sistem branch Arena** — `main` memang otomatis dibuat GitHub waktu repo pertama kali dibuat (ini perilaku standar GitHub, di luar kendali Arena). Penyebab sebenarnya: kamu sendiri menghapus branch `main` itu manual beberapa hari sebelum tes, karena repo itu memang hampir mau dihapus. Yang TETAP jadi fakta valid: begitu `main` sudah tidak ada (dengan sebab apapun), default branch jatuh ke branch Arena terakhir, dan sesi-sesi berikutnya bercabang dari situ, bukan dari `main` — jadi risikonya bukan "main otomatis hilang", tapi "main bisa hilang kalau ada tindakan yang menghapusnya, dan begitu hilang, konsekuensinya branch-branch saling menyimpang tanpa `main` sebagai acuan bersama".
- **Auto-save vs commit:** perubahan file tersimpan otomatis di workspace kerja agent tiap langkah, tapi ini BEDA dari benar-benar masuk ke GitHub — tetap butuh `commit` + `push` eksplisit (agent yang melakukan ini, tapi baik kamu maupun agent perlu sadar 2 tahap ini terpisah).

### 1.2 Kemampuan generate gambar — TERKONFIRMASI, lebih luas dari dugaan awal
- **Berhasil generate DAN simpan sebagai file asli di repo** (bukan cuma URL sementara), ikut ter-commit, format JPG/JPEG/PNG.
- **Path/folder tujuan wajib ditentukan** — kalau kamu tidak sebutkan foldernya, agent akan MEMILIH SENDIRI lokasi yang masuk akal berdasarkan konteks repo (di tes ini, agent otomatis pilih `public/images/brand/` karena itu gambar brand) dan otomatis bikin foldernya kalau belum ada. *(Catatan: skenario "path benar-benar kosong tanpa konteks apapun" belum diuji murni — anggap ini perilaku yang diharapkan, bukan hasil tes 100% pasti.)*
- **Kemampuan tambahan yang baru ketahuan** (di luar 3 tes awal): bisa membaca & mengedit gambar yang sudah ada (restyle), bisa menggabungkan sampai **10 gambar referensi sekaligus** dalam satu generate — ini LANGSUNG relevan untuk kebutuhan "reference image karakter Tipe A" di sistem lama. Ada juga tool cari gambar di web lalu simpan ke repo (untuk CARI, bukan generate).
- Soal kualitas dibanding Midjourney dkk — belum ada perbandingan langsung, tapi dari 1 sample banner yang dihasilkan, kualitasnya cukup baik untuk dipakai produksi nyata (bukan sekadar draft kasar).

### 1.3 Kemampuan video — TERKONFIRMASI TIDAK BISA
- **Tidak ada tool generate video** di lingkungan Arena Agent saat ini. Untuk video, tetap wajib pakai tools eksternal (Veo/Dreamina dkk), hasilnya nanti diupload balik ke repo — sesuai dugaan awal.
- **Temuan tambahan:** agent BISA generate audio narasi/voice-over (ucapan biasa dari teks), TAPI tidak bisa musik atau nyanyian. Ini relevan untuk Tahap 3 (Naskah) kalau formatnya butuh voice over — bisa langsung dieksekusi di agent tanpa tools luar, meskipun video final-nya tetap harus dirakit di luar.

**Catatan keberlakuan:** semua fakta di atas adalah kondisi toolset Arena Agent per 31 Agustus 2026. Kalau Arena menambah fitur baru (misal video) di kemudian hari, poin-poin ini perlu diverifikasi ulang, bukan dianggap permanen selamanya.

---

## KATEGORI 0 — Langkah Persiapan Repo (baru, ditemukan dari hasil tes, belum ada di sistem lama sama sekali)

Kamu belum punya repo untuk sistem konten ini — repo yang dipakai tes (`resto-pro2`) itu proyek lain yang tidak terkait, kebetulan dipakai untuk tes karena mau dihapus.

**Akar masalah sebenarnya di `resto-pro2` (sudah dikonfirmasi lengkap):** ini BUKAN soal sistem branch Arena yang berbahaya. Kronologinya: agent kerja di branch Arena (bukan `main`) → deploy dilakukan dari `main` (yang belum berubah) → hasil deploy kelihatan tidak berubah karena perubahan memang belum di-*merge* ke `main` → penyebab aslinya adalah **belum ada pemahaman soal konsep merge**, bukan bug/perilaku aneh dari tool → sebagai respons, default branch diganti dan `main` dihapus manual — ini "solusi" yang tidak menyasar akar masalah aslinya (harusnya: merge dulu, baru deploy), dan malah menghilangkan titik acuan bersama yang bikin branch-branch Arena saling menyimpang.

Kesimpulannya: **tool-nya (GitHub + Arena) sudah aman by default** — `main` otomatis ada, branch Arena otomatis terpisah dari `main`, tidak ada auto-merge yang bisa "menimpa" main tanpa sepengetahuan siapa pun. Yang perlu dijaga hanyalah pemahaman dasar soal konsep branch/merge — supaya keputusan yang diambil (kalau nanti ada masalah serupa) menyasar akar masalahnya, bukan solusi yang malah menghilangkan struktur pengaman.

*(Catatan: pemahaman detail teknis "cara klik merge di GitHub" sengaja BELUM dibahas tuntas di sini — konsepnya sudah cukup untuk kelanjutan dokumen ini, detail eksekusi nyata akan dipelajari nanti pas repo sistem konten sungguhan sudah dipegang.)*

**Yang perlu diputuskan/dilakukan saat bikin repo baru nanti:**
- Setelah repo dibuat di GitHub (otomatis dapat `main`), pastikan commit pertama (skeleton folder + 10 dokumen sistem yang sudah direvisi) masuk ke `main` itu
- Sebelum deploy/pakai hasil kerja apapun dari sesi agent, **selalu merge branch Arena ke `main` dulu** — ini langkah yang terlewat di kasus `resto-pro2`
- Jangan ganti default branch atau hapus `main` sebagai respons cepat kalau ada yang terlihat "tidak berubah" — itu biasanya tanda belum di-merge, bukan tanda `main`/default branch-nya salah

---

## KATEGORI 2 — Keputusan Struktural (perlu dijawab sebelum revisi dokumen)

### 2.1 Struktur folder repo

**Kondisi sekarang:** semua file flat di 1 folder (`CHANNEL_[nama].md`, `KARAKTER_[nama].md`, `CHANNEL_[nama]_MODEL_[nama-model].md` semua sejajar, dibedakan cuma dari nama file).

**Kenapa ini perlu diputuskan ulang:** dengan repo asli, flat structure begini masalah begitu jumlah channel dan model konten bertambah — apalagi sekarang ada ASSET BINER (gambar) yang perlu tempat, bukan cuma markdown. Sistem lama juga belum punya tempat untuk hasil produksi (naskah jadi, breakdown shot, gambar shot) sama sekali — dokumen lama eksplisit bilang "tidak disimpan permanen, kecuali insight yang layak dicatat balik" (lihat tabel 4 Level di `00`). Dengan repo, keputusan itu layak ditinjau ulang — apakah SEKARANG hasil produksi harian juga layak disimpan permanen di repo (karena "download tinggal pakai" adalah salah satu tujuan awalmu)?

**Yang perlu diputuskan:**

✅ **SUDAH DIPUTUSKAN — repo tunggal vs repo per channel:**
- **1 repo untuk SEMUA channel** (bukan repo terpisah per channel), dengan folder terpisah per channel di dalamnya.
- Alasan: Brand Core butuh 1 rujukan bersama (kalau repo terpisah, Brand Core harus di-duplikat manual ke tiap repo — persis masalah yang coba dihindari sistem lama soal file lintas-channel). Batas ukuran repo GitHub itu besar dan dipengaruhi terutama oleh FILE BINER (gambar/video) yang menumpuk, bukan oleh banyaknya channel/folder — jadi bukan alasan kuat untuk pisah repo dari awal. Kalau nanti repo memang jadi berat karena data nyata (bukan kekhawatiran di muka), pemisahan channel tertentu ke repo sendiri bisa diputuskan belakangan berdasarkan angka nyata.

✅ **SUDAH DIPUTUSKAN — status hasil produksi harian (disimpan permanen atau sementara):**

Dipisah jadi 2 sub-kategori, karena beda jenis file punya pertimbangan beda:

| Jenis hasil produksi | Status | Alasan |
|---|---|---|
| **Naskah final** (teks) tiap konten yang sudah selesai/publish | **PERMANEN**, diarsipkan | Ukuran file teks kecil (tidak bikin repo bengkak, beda dari asset visual). Berguna untuk: (1) mencegah agent/kamu mengulang topik yang sama tanpa sadar, kecuali memang sengaja diulang dengan alasan jelas (format beda, versi lebih panjang, dst); (2) referensi nyata untuk menjaga konsistensi gaya bahasa lintas waktu — lebih kuat daripada cuma mengandalkan deskripsi abstrak di Persona & Voice |
| **Breakdown shot & gambar/asset visual per-shot** | **SEMENTARA** — ada di repo selama proses produksi konten itu berjalan, dihapus dari repo setelah konten selesai & sudah didownload/dipakai | File biner ini yang sebenarnya bikin repo bengkak, bukan naskah. Kamu download dulu ke lokal, baru hapus dari repo. |

**Cara arsip naskah final supaya tidak berantakan:** 1 folder arsip per channel, isinya naskah + metadata ringkas (judul, tanggal publish, topik singkat) — supaya gampang di-scan agent maupun kamu untuk cek "topik ini sudah pernah dibahas". Kalau nanti jumlahnya sudah sangat banyak dan mulai berat untuk DIBACA SEMUA oleh agent (bukan soal ukuran file, tapi jumlah file), baru dipertimbangkan meringkas jadi 1 file indeks per channel — tapi ini keputusan nanti, bukan sekarang.

**Yang WAJIB permanen (di luar naskah, sudah dari poin 2.2 di bawah, dicatat ulang di sini untuk kelengkapan gambaran folder):**
- Dokumen sistem (Brand Core, Channel Brief, Model Konten Brief)
- Character Bible + gambar referensi karakter Tipe A
- Sample output visual yang "disetujui" sebagai acuan gaya

**Masih perlu dirancang (langkah selanjutnya):**
✅ **SUDAH DIPUTUSKAN — lokasi file karakter lintas-channel:**
- Folder tersendiri di level ROOT repo, sejajar dengan folder channel-channel (bukan di dalam folder salah satu channel), misalnya `karakter-lintas-channel/`. Alasan: begitu dilihat sekilas dari struktur repo, langsung jelas dia bukan properti 1 channel tertentu — kalau ditaruh di dalam folder salah satu channel, akan membingungkan seolah dia milik channel itu padahal dipakai bersama.

**Masih perlu dirancang:**
- Nama-nama folder konkret (skeleton struktur repo secara nyata) — lihat di bawah

✅ **SUDAH DIPUTUSKAN — cakupan "konsistensi" diperluas, bukan cuma karakter:**

Ditemukan saat diskusi: sistem lama (`04_CHARACTER_BUILDER_KIT.md`) cuma bicara soal karakter, padahal kebutuhan konsistensi channel bisa mencakup lebih dari itu. Dipetakan jadi 2 keluarga besar dengan sifat berbeda:

| Keluarga | Contoh aspek | Butuh apa | Nama dokumen |
|---|---|---|---|
| **Visual** (butuh jangkar gambar) | Karakter, latar/lingkungan, palet warna & gaya render, props/objek berulang | File gambar referensi yang bisa di-attach ke prompt generate gambar | **Bank Konsistensi Visual** (menggantikan/memperluas cakupan Character Bible) |
| **Non-visual** (cukup teks) | Gaya bahasa, tone, struktur naskah/formula, karakteristik suara/voice (kalau pakai TTS) | Deskripsi + contoh nyata (naskah lama dari arsip) | **Persona & Voice** (sudah ada di Channel Brief, cukup diperluas cakupannya) |

**Keputusan:** TETAP 2 dokumen terpisah (bukan digabung 1 file besar), alasannya teknis: agent generate gambar butuh attach file, agent generate teks butuh baca deskripsi — beda cara pakai, digabung 1 file besar cuma bikin agent harus "menyaring" tiap kali dipakai. TAPI keduanya WAJIB saling merujuk eksplisit di bagian yang terkait (misal bagian Karakter di Bank Konsistensi Visual mencantumkan "lihat juga gaya bicara di Persona & Voice bagian X") — supaya keterkaitannya (karakter ↔ gaya bicara ↔ suara) tetap terlihat tanpa harus jadi 1 file fisik.

**Checklist konsistensi (wajib diisi eksplisit saat Discovery, Channel Brief maupun Model Konten Brief):** channel/model konten ini butuh konsisten di aspek VISUAL yang mana (kalau ada), dan aspek NON-VISUAL yang mana (kalau ada) — dijawab eksplisit satu-satu, tidak diasumsikan atau dilewat begitu saja. Bagian yang tidak relevan untuk channel itu boleh ditandai "tidak berlaku", tapi tetap harus dipikirkan, bukan dihilangkan diam-diam.

**Draft skeleton struktur folder (berdasarkan semua keputusan di atas, untuk didiskusikan/disetujui):**

```
nama-repo/
├── _sistem/                          ← 10+ dokumen sistem (00-09, hasil revisi kita)
│   ├── 00_CARA_PAKAI_SISTEM.md
│   ├── 01_BRAND_CORE.md              ← Brand Core, isi langsung di sini (1 untuk semua channel)
│   ├── ...dst (dokumen generator lainnya)
│
├── konsistensi-lintas-channel/       ← Bank Konsistensi Visual untuk karakter/latar/dll yang dipakai >1 channel
│   └── [nama-elemen]/                ← misal nama karakter, atau nama latar
│       ├── bank-konsistensi.md
│       └── referensi/
│           ├── acuan-utama.png       ← 1 gambar netral/default, dipakai kalau tidak ada kebutuhan spesifik
│           ├── reference-sheet.png   ← 1 file grid: beberapa sudut pandang/keadaan sekaligus (turnaround)
│           └── tambahan-[keterangan].png (kalau ada kebutuhan situasional lain)
│
├── channel-[nama-channel-1]/
│   ├── channel-brief.md              ← isi Channel Brief channel ini (termasuk Persona & Voice, checklist konsistensi)
│   ├── konsistensi-visual/           ← Bank Konsistensi Visual KHUSUS channel ini (bukan lintas-channel)
│   │   └── [nama-elemen]/            ← karakter, latar, palet, dll — sesuai checklist channel ini
│   │       ├── bank-konsistensi.md
│   │       └── referensi/
│   │           ├── acuan-utama.png
│   │           └── reference-sheet.png (kalau perlu)
│   ├── model-konten/
│   │   ├── [nama-model-1]/           ← Model Konten sekarang FOLDER, bukan file tunggal
│   │   │   ├── brief.md              ← isi Model Konten Brief
│   │   │   └── assets/               ← reference visual KHUSUS model konten ini (kalau beda dari channel)
│   │   └── [nama-model-2]/
│   │       └── brief.md
│   └── arsip-naskah/                 ← PERMANEN — naskah final konten yang sudah publish
│       ├── indeks.md                 ← tabel ringkas: judul, tanggal, topik singkat
│       ├── 2026-08-31-judul-a.md
│       └── 2026-09-02-judul-b.md
│
├── channel-[nama-channel-2]/
│   └── (struktur sama seperti di atas)
│
└── _produksi-aktif/                  ← SEMENTARA — breakdown shot & asset visual, dihapus setelah konten selesai & didownload
    └── [channel]-[judul-konten-berjalan]/
        ├── naskah-draft.md
        ├── breakdown-shot.md
        └── assets/
            ├── shot-01.png
            └── shot-02.png
```

**Catatan cara baca skeleton ini:**
- `_sistem/` dan `_produksi-aktif/` diberi awalan underscore supaya selalu tampil di urutan paling atas/mudah dibedakan dari folder channel biasa (konvensi umum, bukan aturan teknis wajib)
- Elemen konsistensi visual (karakter, latar, dst) yang cuma dipakai 1 channel taruh di `channel-[nama]/konsistensi-visual/`, yang lintas-channel taruh di root `konsistensi-lintas-channel/`
- Model Konten Brief yang cuma butuh teks (tidak ada assets visual khusus) tetap boleh folder-nya cuma berisi `brief.md` saja — folder `assets/` opsional, dibuat kalau memang dibutuhkan, bukan wajib default kosong
- `_produksi-aktif/` isinya HANYA konten yang sedang dikerjakan, bukan arsip — begitu selesai & didownload, foldernya dihapus. Naskah finalnya sendiri (bukan breakdown/asset) dipindah ke `arsip-naskah/` channel terkait sebelum folder produksi dihapus

---

## 2.6 — Mekanisme Anti-Melenceng untuk Sesi Panjang (BARU, di luar rencana awal Kategori 2)

**Latar belakang:** pola kerja produksi konten kamu bisa sangat panjang & berlapis dalam 1 sesi (contoh nyata yang kamu sebutkan: ekstrak buku → pelajari → ekstrak ide → kumpulan bahan/naskah → eksekusi per konten → tiap eksekusi ada beberapa tahap lagi). Semakin panjang & berlapis sebuah sesi, semakin besar risiko di tahap-tahap akhir agent sudah "melenceng" dari apa yang disepakati di tahap-tahap awal — bukan karena sesi baru (itu sudah ditangani sistem file + entry point), tapi karena SATU sesi yang sama kehilangan jejak di tengah jalan.

✅ **SUDAH DIPUTUSKAN — solusi 2 lapis:**

**Lapis 1 — Pencegahan (checkpoint wajib):**
Setiap kali sesi pindah dari 1 tahap besar ke tahap besar berikutnya, agent WAJIB berhenti sejenak dan meringkas ulang apa yang sudah disepakati sejauh ini — dengan cara MEMBACA ULANG sumber resminya (Channel Brief, Bank Konsistensi Visual, Persona & Voice, dst yang relevan), bukan mengandalkan ingatannya sendiri dari histori chat sejauh ini. Ringkasan ini ditunjukkan ke kamu sebelum lanjut ke tahap berikutnya.

**Lapis 2 — Deteksi & pemulihan manual:**
Kamu bisa memanggil kapan saja, di titik manapun dalam sesi, sebuah perintah pendek semacam **"cek konsistensi"** — begitu dipanggil, agent membandingkan apa yang baru saja dia hasilkan dengan sumber resmi (Channel Brief, Bank Konsistensi Visual, Persona & Voice — sesuai checklist konsistensi channel/model konten itu), dan melaporkan kalau ada yang melenceng. Ini jaring pengaman kalau Lapis 1 kebetulan lolos/tidak cukup.

**Alasan 2 lapis, bukan 1:** Lapis 1 sendirian berisiko jadi rutinitas kosong (meringkas tapi tidak benar-benar sinkron ulang ke sumber asli). Lapis 2 sendirian berarti kamu harus sadar sendiri ada yang melenceng — padahal itu justru risiko yang coba dihindari. Biaya kedua lapis ini RENDAH kalau ternyata jarang kepakai (checkpoint singkat, "cek konsistensi" tinggal tidak dipanggil kalau tidak perlu), tapi perlindungannya besar kalau memang sering dibutuhkan.

**Kaitan dengan checklist konsistensi (2.1):** checklist itu jadi acuan KONKRET untuk kedua lapis ini — agent tahu persis apa saja yang harus dicek ulang/dibandingkan (karakter? latar? gaya bahasa? suara?), bukan "cek konsistensi" yang abstrak tanpa arah jelas.

---

## 2.7 — Entry Point Universal (BARU, menjawab kebutuhan "sistem yang bikin mudah mulai/lanjut sesi")

**Latar belakang:** menggantikan `START_DI_SINI.md` versi manusia dari sistem lama — sekarang jadi 1 instruksi standar yang dipakai tiap kali buka sesi (baru maupun lanjutan), supaya kamu tidak perlu mikir ulang dari nol tiap kali, dan agent otomatis tahu harus baca apa & tanya apa.

✅ **SUDAH DIPUTUSKAN — fakta teknis yang jadi dasar rancangan (terverifikasi langsung olehmu):** di awal sesi, kamu bisa memilih repo DAN branch yang mau dipakai, termasuk melihat daftar nama branch yang sudah ada (baru maupun lama yang belum di-merge) dan memilih salah satu secara sengaja. Ini artinya "melanjutkan kerjaan lama di sesi/chat baru" TIDAK butuh mekanisme rumit — cukup kamu pilih branch lama yang sesuai di awal sesi.

✅ **SUDAH DIPUTUSKAN — 2 skenario awal sesi, ditangani beda:**

| Skenario | Ciri | Yang terjadi |
|---|---|---|
| **A — Lanjut di jendela chat yang sama** (belum ditutup, cuma jeda) | Agent masih punya konteks percakapan, branch masih sama | Tidak butuh entry point khusus — cukup lanjut seperti biasa, checkpoint Lapis 1 (2.6) otomatis jalan kalau pindah tahap besar |
| **B — Buka chat/sesi baru** (baik untuk kerjaan baru maupun nerusin branch lama) | Branch baru OTOMATIS dibuat, KECUALI kamu sengaja pilih branch lama yang sudah ada | Entry point universal bekerja penuh (langkah-langkah di bawah) |

✅ **SUDAH DIPUTUSKAN — urutan langkah entry point universal (untuk Skenario B):**

1. **Deteksi kondisi branch** — agent cek: branch ini baru/kosong, atau branch lama yang sudah ada progress/isi sebelumnya?
   - Kalau branch LAMA (ada isi) → agent baca dulu apa yang sudah dikerjakan di branch ini (baca file yang sudah ada, baca commit terakhir) SEBELUM bertanya apa-apa — supaya tidak nanya hal yang jawabannya sudah ada di branch itu sendiri
   - Kalau branch BARU (kosong, baru bercabang dari `main`) → lanjut ke langkah 2
2. **Cek & laporkan PR yang menggantung** (sesuai keputusan 2.4) — otomatis, tanpa diminta, di awal sesi manapun
3. **Tanya tujuan sesi ini** — mau mengerjakan apa (Discovery/Produksi/revisi/lainnya), di channel/model konten/konten yang mana
4. **Baca sendiri file yang relevan** berdasarkan jawaban langkah 3 — Brand Core selalu, lalu Channel Brief/Bank Konsistensi Visual/Persona & Voice/Model Konten Brief sesuai yang relevan dengan jawaban tadi — TANPA kamu perlu tempel manual isi file (ini juga menjawab poin 3.1 di Kategori 3 nanti)
5. **Deteksi jenis sesi** (Discovery vs Produksi) dari jawaban langkah 3 — supaya aturan merge yang dipakai nanti sesuai (2.4)

**Catatan penting:** langkah 1 (deteksi kondisi branch) ini yang membuat entry point universal berbeda dari sekadar checklist statis — dia ADAPTIF tergantung kamu masuk ke branch kosong atau branch yang sudah ada kerjaan. Ini detail yang perlu ditulis eksplisit nanti waktu entry point ini dijadikan dokumen/prompt konkret, bukan cuma "baca file lalu tanya" yang generik.

**Masih perlu dirancang (langkah selanjutnya, di luar dokumen audit ini):** menulis entry point universal ini jadi dokumen/prompt konkret siap pakai (kemungkinan jadi dokumen baru menggantikan `START_DI_SINI.md`, atau bagian dari `00_CARA_PAKAI_SISTEM.md` yang direvisi) — ini masuk pekerjaan Kategori 3 (menulis ulang gaya prompt), dilakukan setelah semua Kategori 2 selesai dibahas, sesuai urutan yang sudah kita sepakati di awal.

---



### 2.2 Asset biner (gambar referensi karakter, sample output visual) — ✅ SELESAI DIBAHAS (31 Agustus 2026)

**Kondisi sekarang:** `04_CHARACTER_BUILDER_KIT.md` Tahap 2 bilang "kalau memungkinkan" simpan gambar referensi, dan itu disimpan di luar sistem dokumen ini sepenuhnya (tidak ada folder yang didefinisikan) — cuma "catat lokasi/nama file" di Tahap 3.

**Kenapa ini berubah:** dengan agent yang bisa generate gambar DAN commit ke repo, "kalau memungkinkan" seharusnya naik jadi WAJIB dan otomatis, bukan manual kamu upload sendiri. Ini juga jadi pusat solusi masalah #1 yang disebutkan sistem lama sendiri (wajah karakter berubah-ubah) — sekarang bisa benar-benar dijawab tuntas kalau referensi gambarnya persisten di repo dan SELALU dirujuk agent tiap generate.

✅ **SUDAH DIPUTUSKAN — struktur folder asset:** sudah tercermin di skeleton 2.1 — `konsistensi-visual/[nama-elemen]/referensi/` (per channel) atau `konsistensi-lintas-channel/[nama-elemen]/referensi/` (lintas channel).

✅ **SUDAH DIPUTUSKAN — jenis-jenis file referensi per elemen (bukan cuma 1 gambar):**

| Jenis | Isi | Fungsi |
|---|---|---|
| **Acuan utama** (`acuan-utama.png`) | 1 gambar tunggal, kondisi paling netral/default | Dipakai kalau tidak ada kebutuhan spesifik — WAJIB ada untuk tiap elemen yang butuh konsistensi visual |
| **Reference sheet** (`reference-sheet.png`) | 1 file GRID berisi beberapa sudut pandang (depan/samping/belakang) atau beberapa keadaan (ekspresi/pose) sekaligus dalam 1 gambar — teknik "character turnaround sheet" yang lazim dipakai di produksi visual (animasi, game, komik) | Dipakai kalau butuh variasi sudut/keadaan yang jauh beda dari acuan utama, supaya bentuk/wujud elemen itu terjaga dari berbagai sisi — TIDAK menggantikan acuan utama, tapi tambahan |
| **Referensi tambahan** (opsional, situasional) | Foto lepas untuk kebutuhan khusus (misal 1 outfit yang cuma dipakai 1 model konten tertentu) | Dipakai kasus per kasus, tidak wajib ada |

Catatan teknis pendukung: agent terbukti bisa menggabungkan sampai 10 gambar referensi sekaligus dalam 1 kali generate (Kategori 1.2) — jadi acuan utama, reference sheet, dan referensi tambahan bisa dipakai BERSAMAAN dalam 1 generate kalau situasinya butuh, tidak saling menggantikan satu sama lain.

✅ **SUDAH DIPUTUSKAN — Prompt Master dipasangkan otomatis dengan gambar:** YA, otomatis. Kalau elemen itu punya file referensi, agent WAJIB menyertakannya tiap kali generate gambar terkait elemen itu — tidak perlu kamu ingat-ingat untuk minta secara manual tiap kali.

✅ **SUDAH DIPUTUSKAN — sample output visual yang "disetujui":** digabung ke folder `referensi/` yang sama (bukan kategori terpisah), karena fungsinya sama seperti referensi lain — bedanya cuma asal-usulnya (referensi awal dibuat sengaja sebagai acuan, sample yang disetujui itu hasil produksi yang kebetulan dianggap sudah pas gayanya dan layak jadi acuan untuk berikutnya).

### 2.3 Karakter Tipe B (per-konten, one-off) — ✅ SELESAI DIBAHAS (31 Agustus 2026)

**Kondisi sekarang:** deskripsinya cuma di-chain dalam teks sepanjang sesi produksi, TIDAK disimpan permanen kecuali dia "naik kelas" jadi Tipe A.

**Kenapa ini layak ditinjau:** kalau semua kerja sekarang di 1 repo yang persisten, "tidak disimpan permanen" jadi pilihan yang lebih sengaja, bukan keterbatasan teknis chat biasa (di chat biasa, memang nggak ada tempat nyimpen kalau bukan di percakapan itu sendiri). Sekarang ada opsi: simpan tetap sebagai bagian dari folder konten itu (bukan sebagai file karakter permanen terpisah), supaya kalau suatu saat dicek ulang "karakter ini pernah dipakai di konten mana saja", ada jejaknya — bukan cuma mengandalkan ingatanmu untuk mendeteksi "eh ini kepake lagi, harus naik kelas ke Tipe A".

✅ **SUDAH DIPUTUSKAN — di mana deskripsi karakter Tipe B disimpan:** BUKAN file karakter mandiri terpisah (itu tetap khusus Tipe A) — melainkan menempel ke arsip konten yang memakainya, di `arsip-naskah/` channel terkait (baik sebagai bagian dari file naskah itu sendiri, atau file kecil terpisah di folder arsip yang sama). Ini konsisten dengan keputusan arsip naskah permanen yang sudah diambil di 2.1 — begitu naskah final 1 konten diarsipkan, deskripsi karakter Tipe B yang dipakai konten itu ikut terekam di situ juga.

✅ **SUDAH DIPUTUSKAN — siapa yang mendeteksi "saatnya naik kelas ke Tipe A":** AGENT, otomatis — bukan mengandalkan kamu ingat sendiri. Caranya: begitu agent mau membuat karakter Tipe B baru untuk 1 konten, dia CEK DULU ke arsip channel terkait (`arsip-naskah/indeks.md`) apakah karakter dengan ciri serupa sudah pernah dipakai sebelumnya. Kalau ketemu kecocokan, agent menawarkan ke kamu: "karakter ini kelihatannya sudah dipakai di konten X sebelumnya, mau dinaikkan jadi karakter permanen (Tipe A)?" — keputusan akhir tetap di tangan kamu, tapi deteksinya otomatis.

**Kaitan dengan bagian lain:** langkah deteksi ini menempel ke entry point universal (2.7) — jadi bagian dari langkah "baca file relevan" saat mulai sesi produksi baru, bukan mekanisme terpisah yang berdiri sendiri.

### 2.4 Branch & merge strategy — ✅ SELESAI DIBAHAS (31 Agustus 2026)

**Kondisi sekarang:** sistem lama sama sekali tidak punya konsep versioning — "Log Keputusan" di tiap Brief adalah pengganti manual untuk riwayat perubahan.

**Sudah TERBUKTI lewat tes (bukan lagi teori):** branch per sesi otomatis, tidak pernah auto-merge. Dan meski penyebab hilangnya `main` di repo tes kemarin ternyata tindakan manual (bukan perilaku bawaan Arena), konsekuensinya tetap nyata dan relevan: begitu `main` tidak ada/tidak diacu dengan benar, branch-branch Arena BISA saling menyimpang tanpa ketahuan (lihat Kategori 1.1 dan Kategori 0). Jadi poin ini levelnya naik dari "perlu dipikirkan" jadi **prioritas tertinggi untuk diputuskan** — karena begitu repo sistem konten mulai dipakai produksi harian sungguhan, PR yang menumpuk tanpa aturan jelas akan jadi masalah nyata dalam hitungan minggu, bukan cuma risiko teoretis.

**Yang perlu diputuskan:**

✅ **SUDAH DIPUTUSKAN — kapan branch/PR dianggap siap merge:**
- **Sesi Discovery** (Brand Core, Channel Discovery, Model Konten Discovery, Character Builder) — auto-tawarkan merge begitu diskusi selesai dan dokumennya ditulis final. Sifatnya jarang ada "draft yang dibuang" di level ini, jadi cukup sederhana: selesai ditulis → agent tawarkan merge.
- **Sesi Produksi** (1 konten dari ide sampai publish) — bukan tiap tahap kecil, tapi begitu 1 konten selesai penuh (Tahap 6 Assembly & Publish selesai). Ini jadi patokan jelas, bukan penilaian subjektif "kayaknya sudah bagus".
- **Prinsip umum yang berlaku LINTAS semua jenis sesi (bukan cuma pipeline produksi):** begitu ada hasil kerja yang dianggap FIX/final — apapun jenis sesinya, termasuk sesi di luar alur produksi konten yang terstruktur — agent WAJIB menawarkan merge di titik itu secara aktif, bukan menunggu kamu ingat sendiri. Ini keputusan sadar untuk menutup celah yang menyebabkan masalah di `resto-pro2` (lupa/tidak tahu perlu merge).
- **Status keputusan ini:** dianggap ATURAN AWAL yang masuk akal, bukan final permanen. Kalau setelah dipakai beberapa minggu ternyata terlalu sering "berisik" menawarkan merge (misal kalau ritme kerja kamu jadi banyak sesi kecil-kecil per hari), ini boleh disesuaikan — tapi itu keputusan sadar yang dicatat di Log Keputusan, bukan berubah diam-diam.

✅ **SUDAH DIPUTUSKAN — PR yang menggantung (belum dijawab saat sesi ditutup):**
- Agent WAJIB cek status PR yang masih terbuka di AWAL setiap sesi baru, otomatis tanpa diminta — apapun jenis sesi berikutnya (Discovery maupun Produksi) — dan laporkan ringkasannya ke kamu sebelum mulai kerja baru. Ini mencegah PR menggantung terlupakan sampai menumpuk.

✅ **SUDAH DIPUTUSKAN — kemampuan teknis agent untuk merge (terverifikasi langsung ke lmarena Agent):**
- Agent SECARA TEKNIS bisa merge PR — lewat akses shell generik (`bash`) yang di dalamnya ada GitHub CLI (`gh`) terautentikasi, BUKAN tombol/tool khusus bernama "merge".
- Defaultnya agent TIDAK PERNAH auto-merge tanpa instruksi eksplisit — ini prinsip desain (PR sebagai gerbang review manusia), bukan keterbatasan teknis.
- **Pengaman bawaan tool:** bahkan kalau diminta eksplisit "tolong merge", agent tetap akan konfirmasi singkat dulu (PR nomor berapa, metode merge apa — merge commit/squash/rebase) sebelum benar-benar eksekusi. Ini berlaku selalu, di luar aturan tambahan yang kita buat sendiri.

✅ **SUDAH DIPUTUSKAN — siapa yang review sebelum merge (dengan pengaman ganda dari poin di atas):**

Prinsip pembagian: **kalau kesalahan di suatu perubahan bisa "menyebar" ke banyak konten ke depan atau susah dibalik lagi, itu kategori Besar (wajib direview isinya dulu oleh kamu). Kalau dampaknya cuma di 1 tempat kecil dan gampang diperbaiki lagi nanti, itu kategori Kecil (agent boleh tanya ringan tanpa kamu perlu baca detail, tapi tool tetap minta konfirmasi kamu sebelum eksekusi).**

| Kategori | Termasuk | Cara approval |
|---|---|---|
| **Besar** | Brand Core, Channel Brief, Model Konten Brief (baru/revisi); Character Bible Tipe A (baru/revisi); Konten produksi final (siap publish) | Kamu review ISI PR dulu, baru bilang "merge" |
| **Kecil** | Log Keputusan, Bank Ide Awal, catatan administratif lain yang tidak mengubah keputusan inti | Agent tanya ringan "mau saya merge sekarang?" — kamu tinggal jawab ya/tidak tanpa perlu baca detail isi PR |

*(Kalau nanti muncul jenis perubahan baru yang belum masuk tabel ini, uji pakai prinsip di atas — bukan ditebak asal, dan sebaiknya ditambahkan ke tabel begitu ketemu supaya konsisten ke depannya.)*

✅ **SUDAH DIPUTUSKAN — sesi yang menyentuh lebih dari 1 tujuan/pekerjaan:**

Bukan soal apakah 1 sesi PERCAKAPAN bisa menghasilkan 2 branch sekaligus (setahu kita dari Kategori 1.1: 1 sesi = 1 branch, otomatis dari sistemnya) — tapi soal APAKAH 2 pekerjaan berbeda tujuan boleh terjadi berurutan di jendela chat/percakapan yang sama.

**Prinsipnya: beda tujuan yang dikerjakan BERSAMAAN dan sama-sama belum selesai = harus dipisah (mulai sesi/branch baru). Beda tujuan yang dikerjakan BERURUTAN, di mana pekerjaan pertama sudah selesai/di-merge dulu sebelum pekerjaan kedua dimulai = boleh 1 sesi/branch yang sama, tidak masalah.**

Contoh yang TIDAK masalah: revisi Channel Brief selesai → di-merge → di percakapan yang sama, lanjut produksi 1 konten. Karena begitu sudah di-merge, `main` sudah aman dan bersih, jadi pekerjaan berikutnya otomatis "mulai dari nol" secara bersih juga — tidak ada campur aduk.

Contoh yang PERLU dipisah: di tengah revisi Channel Brief (belum di-merge, masih draft), muncul keinginan sekaligus produksi 1 konten di branch yang sama — ini akan mencampur 2 pekerjaan yang SAMA-SAMA belum kelar dalam 1 PR, susah dipisah kalau salah satu perlu di-revert tanpa mengganggu yang lain.

✅ **SUDAH DIPUTUSKAN — status Log Keputusan vs git history:**
- Log Keputusan TETAP dipertahankan sebagai tabel di dalam file (Channel Brief, Model Konten Brief, dst) — TIDAK digantikan sepenuhnya oleh commit message/git history.
- Alasan: commit message biasanya ditulis singkat/teknis ("update channel brief"), sementara Log Keputusan berisi ALASAN di balik keputusan itu — beda level detail. Kalau file ini dibuka lagi berbulan-bulan kemudian, alasan keputusan harus langsung terbaca di situ, tidak perlu menggali git log.

### 2.5 Sesi Discovery yang "sengaja dipisah" (Brand Core, Channel Discovery, Model Konten Discovery) — ✅ SELESAI DIBAHAS (31 Agustus 2026)

**Kondisi sekarang:** `00_CARA_PAKAI_SISTEM.md` di bagian akhir menjelaskan alasannya eksplisit — diskusi Discovery itu "panjang dan penuh bolak-balik", kalau dicampur sesi produksi harian, "context yang berantakan ikut kebawa".

**Kenapa ini perlu ditinjau ulang:** alasan asli itu ditulis dengan asumsi SEMUA terjadi di 1 sesi CHAT yang sama (context window chat itu sendiri yang jadi masalah). Dengan agent+repo, alasan itu sudah TIDAK RELEVAN dengan cara yang sama — agent baca dari file repo, bukan scroll-back chat, jadi masalah "konteks campur aduk dalam 1 jendela percakapan" sudah teratasi secara struktural.

✅ **SUDAH DIPUTUSKAN:** pemisahan Discovery vs Produksi TETAP ADA, tapi alasannya berubah — bukan lagi soal keterbatasan teknis chat, melainkan penerapan langsung dari prinsip yang sudah disepakati di 2.4 (sesi multi-tujuan): Discovery dan Produksi adalah 2 TUJUAN BERBEDA, jadi berlaku aturan yang sama seperti tujuan berbeda lainnya — **wajib dipisah sesi/branch HANYA kalau keduanya dikerjakan BERSAMAAN dalam kondisi sama-sama belum selesai**. Kalau Discovery sudah selesai dan di-merge dulu, baru lanjut Produksi di percakapan yang sama, itu TIDAK masalah — sama seperti kasus lain yang sudah dibahas di 2.4.

**Kesimpulan:** bukan aturan baru yang berdiri sendiri — ini murni penerapan prinsip 2.4 ke kasus Discovery vs Produksi secara spesifik. Poin 2.5 ini bisa dianggap sebagai konfirmasi/klarifikasi, bukan keputusan terpisah.

---

**STATUS KATEGORI 2: SELESAI SEPENUHNYA** (2.1, 2.2, 2.3, 2.4, 2.5 semua sudah dibahas dan dikunci). Langkah selanjutnya: Kategori 3 (menulis ulang gaya prompt berdasarkan semua keputusan struktural di atas).

---

## KATEGORI 3 — Prompt yang perlu ditulis ulang gayanya (bukan isinya) — ✅ SELESAI DIBAHAS (31 Agustus 2026)

Ini bukan soal isi/logika prompt berubah, tapi CARA prompt itu ditulis — karena semua prompt di sistem lama ditulis dengan asumsi "kamu, manusia, yang copy-paste hasil dari 1 AI ke sesi lain secara manual". Dengan agent yang punya akses baca-tulis file langsung, sebagian instruksi itu jadi berlebihan atau perlu diganti bentuknya.

### 3.1 Instruksi "TEMPEL ISI FILE X DI SINI" — ✅ DIPUTUSKAN

Muncul berulang di HAMPIR SEMUA prompt (`01`, `02`, `04`, `05` semua tahap, `07`) — misalnya:
> `"[TEMPEL RINGKASAN CHANNEL BRIEF DI SINI]"`
> `"[TEMPEL ISI 01_BRAND_CORE.md ATAU RINGKASANNYA DI SINI]"`

**Keputusan:** SEMUA instruksi "tempel isi file" diganti jadi instruksi "baca file di path X" — konsisten dengan entry point universal (2.7) yang sudah mengharuskan agent baca sendiri file relevan tanpa ditempel manual. Kalau pengguna ingin kontrol lebih spesifik (fokus ke bagian tertentu saja), itu tetap bisa dilakukan lewat instruksi langsung saat itu ("fokus ke bagian X saja"), bukan lewat mekanisme tempel-manual permanen di template prompt.

### 3.2 Chain Instruction (`06` bagian 0) — ✅ SUDAH TERJAWAB lewat keputusan 2.4

Titik approval (kapan agent berhenti minta persetujuan) sudah dikunci di 2.4: kategori Besar (Brand Core, Channel/Model Konten Brief, Character Bible, konten final) selalu direview isi dulu oleh pengguna; kategori Kecil (Log Keputusan, Bank Ide) cukup dikonfirmasi ringan. Chain Instruction versi baru akan mengikuti pembagian ini — bukan auto-lanjut tanpa jeda, dan bukan juga berhenti di tiap langkah kecil tanpa kecuali. Tidak ada keputusan tambahan yang diperlukan di sini, sub-poin ini murah dianggap referensi silang ke 2.4.

### 3.3 Prompt yang ditujukan untuk "sesi chat terpisah" (`01`, `02`, `04` Tahap 1, `07`) — ✅ DIPUTUSKAN

**Kondisi sekarang:** instruksi seperti "Jalankan di sesi chat terpisah (Claude/GPT, mode chat biasa)" — eksplisit menyebut chat biasa, BUKAN agent.

**Fakta baru yang mengubah jawaban (terverifikasi dari pengalaman pengguna):** lmarena Agent BISA diajak diskusi panjang biasa (brainstorming, bolak-balik) TANPA harus baca-tulis file tiap kali merespons — caranya cukup instruksi eksplisit di awal ("sekarang aku mau nanya aja, ga usah lakuin apa-apa dulu..."). Tidak ada toggle/fitur mode khusus, murni instruksi bahasa biasa.

**Keputusan:** TIDAK PERLU pindah ke platform chat terpisah (Claude/GPT chat biasa) sama sekali. Sesi Discovery yang butuh diskusi panjang & bolak-balik tetap bisa dilakukan sepenuhnya DI DALAM sesi lmarena Agent yang sama — dengan pola: mulai di mode diskusi (eksplisit instruksikan "jangan eksekusi dulu"), baru pindah ke mode eksekusi (menulis file, commit) begitu hasil diskusi sudah matang dan siap difinalkan. Instruksi lama yang menyebut platform terpisah dihapus/diganti dengan pola perilaku ini.

**Kaitan dengan 2.5:** ini konsisten dengan keputusan 2.5 (Discovery vs Produksi tetap dipisah sebagai TUJUAN, bukan sebagai PLATFORM) — pemisahannya sekarang murni soal sesi/branch (kapan boleh gabung, kapan wajib pisah, sudah diputuskan di 2.4/2.5), bukan lagi soal "harus pindah aplikasi/chat lain".

---

**STATUS KATEGORI 3: SELESAI SEPENUHNYA.** Langkah selanjutnya: Kategori 4 (konfirmasi cepat hal yang kemungkinan tidak berubah).

---

## KATEGORI 4 — Hal yang KEMUNGKINAN TIDAK berubah (tapi perlu dikonfirmasi, bukan diasumsikan)

Supaya kamu bisa lihat mana yang sudah aman tanpa perlu didiskusikan panjang:

- **Prinsip Hierarki** (Brand Core → Channel → Model Konten → Produksi) — ✅ Dikonfirmasi tetap valid, cuma cara penyimpanannya yang berubah (jadi folder fisik, bukan sekadar penamaan file)
- **Prinsip Pemisahan Suara vs Wujud** (Persona/Voice vs Karakter Visual) — ✅ Dikonfirmasi tetap, ini konsep, tidak terpengaruh tools
- **Aturan pewarisan** (level bawah tidak boleh mengulang isi level atas, cukup merujuk) — ✅ Dikonfirmasi tetap berlaku, malah lebih gampang ditegakkan karena agent bisa cek langsung apakah suatu Model Konten Brief "mengulang" isi Channel Brief-nya atau tidak
- **6 Tahap Pipeline Produksi** (Ideation → Konsep → Naskah → Breakdown Visual → Generate Asset → Assembly) — ⚠️ **DIREVISI, bukan sekadar dikonfirmasi.** Kekhawatiran valid muncul: model konten yang beda jenis (video, infografis, komik, dst) bisa butuh detail tahap yang sangat berbeda — memaksakan 1 pipeline kaku untuk semua berisiko memaksa format tidak cocok atau kehilangan detail penting. **Keputusan: "kerangka tetap, detail fleksibel"** — 6 Tahap sebagai KERANGKA BESAR tetap dipertahankan (levelnya cukup umum untuk hampir semua jenis konten), TAPI detail konkret di dalam tiap tahap (misal Tahap Breakdown itu berupa "shot" untuk video, "section" untuk infografis, "panel" untuk komik) DITENTUKAN per Model Konten saat sesi Discovery Model Konten (`07`/`08`) — lahir dari diskusi dengan agent saat itu, bukan dipaksakan template kaku di depan. Ini konsisten dengan Model Konten Brief yang sudah jadi folder (2.1), didesain untuk bisa punya detail spesifik miliknya sendiri.
- **Tipe A vs Tipe B karakter** — ✅ Dikonfirmasi konsepnya tetap sama, tempat penyimpanan Tipe B sudah diputuskan di 2.3
- **Konten `06` bagian A, B, C, D, E** (teknik konsistensi karakter, voice, riset ide, prompt visual, adaptasi platform) — ini murni teknik prompting, tidak terikat platform, kemungkinan besar tetap valid apa adanya *(belum eksplisit dikonfirmasi pengguna — lihat catatan di bawah)*

---

**STATUS KATEGORI 4: SELESAI, dengan 1 catatan.** 5 dari 6 poin dikonfirmasi tetap seperti semula. 1 poin (6 Tahap Pipeline) direvisi jadi "kerangka tetap, detail fleksibel per Model Konten". Poin terakhir (konten teknik prompting `06` A-E) belum eksplisit ditanya ke pengguna — bisa dikonfirmasi cepat kalau diperlukan, tapi levelnya cukup teknis/rendah risiko sehingga tidak menghambat kelanjutan kerja.

---

**SELURUH AUDIT (Kategori 0-4) SUDAH SELESAI DIBAHAS.** Semua keputusan struktural, teknis, dan prinsip sudah dikunci. Langkah selanjutnya adalah EKSEKUSI: merevisi 10 dokumen sistem asli (`00` sampai `08`, plus `START_DI_SINI.md`) berdasarkan seluruh keputusan di audit ini — pekerjaan ini di luar cakupan dokumen audit itu sendiri (dokumen ini adalah PETA keputusan, bukan dokumen sistem final).

---

## Ringkasan: urutan pembahasan yang disarankan

Status per 31 Agustus 2026: **Kategori 1 sudah selesai diverifikasi** (lihat hasil tes di atas). Urutan yang tersisa:

1. ~~Verifikasi Kategori 1~~ ✅ SELESAI — hasil tes sudah masuk ke dokumen ini
2. **Kategori 0** (repo belum ada) — perlu disadari sebagai langkah nyata sebelum kerja lain dimulai, meski belum harus dieksekusi sekarang selama masih tahap diskusi/desain dokumen
3. **Kategori 2**, urutan disarankan: **2.4 (branch & merge strategy) duluan** — karena sudah terbukti lewat tes ini yang paling berisiko kalau dibiarkan tanpa aturan — baru lanjut 2.1 (struktur folder) → 2.2 (asset biner) → 2.3 (Tipe B) → 2.5 (sesi Discovery)
4. **Kategori 3** (gaya penulisan ulang prompt) setelah Kategori 2 clear — supaya prompt yang ditulis ulang sudah mengikuti struktur/aturan yang sudah diputuskan
5. **Kategori 4** cukup dikonfirmasi cepat di akhir, tidak perlu dibahas panjang

---

## Catatan Revisi
- **31 Agustus 2026 (revisi 1):** Kategori 1 diubah dari daftar pertanyaan jadi fakta terverifikasi, berdasarkan tes langsung ke lmarena Agent di repo `resto-pro2` (repo lain, dipakai kebetulan untuk tes, bukan repo sistem konten). Ditambahkan Kategori 0 (repo sistem konten belum ada, perlu langkah penyiapan eksplisit). Poin 2.4 (branch & merge strategy) dinaikkan prioritasnya jadi yang pertama dibahas di Kategori 2.
- **31 Agustus 2026 (revisi 2 — koreksi):** klaim di revisi 1 bahwa "repo bisa otomatis kehilangan main tanpa dikelola" TIDAK AKURAT. Faktanya: GitHub otomatis membuat `main` begitu repo baru dibuat (perilaku standar GitHub, bukan soal Arena). `main` di `resto-pro2` hilang karena dihapus manual oleh pemilik repo.
- **31 Agustus 2026 (revisi 3):** Kronologi lengkap dikonfirmasi — default branch di `resto-pro2` diganti MANUAL oleh pemilik repo (bukan oleh Arena), sebagai respons keliru terhadap gejala "hasil deploy tidak berubah" yang sebenarnya disebabkan belum paham konsep merge (perubahan di branch Arena belum dipindahkan ke `main` sebelum deploy). Kategori 0 diperbarui untuk mencerminkan akar masalah yang benar: bukan risiko dari tool, tapi gap pemahaman soal branch/merge.
- **31 Agustus 2026 (revisi 4):** Poin 2.4 (kapan branch/PR siap merge) DIPUTUSKAN — beda aturan untuk sesi Discovery (auto-tawarkan merge begitu dokumen final ditulis) vs sesi Produksi (tawarkan merge begitu 1 konten selesai penuh, bukan tiap tahap kecil). Prinsip umum: agent WAJIB aktif menawarkan merge begitu ada hasil yang dianggap fix, di jenis sesi manapun — bukan menunggu diingat manual. Status: aturan awal, boleh disesuaikan nanti berdasar pengalaman pemakaian nyata, dengan perubahan dicatat di Log Keputusan.
- **31 Agustus 2026 (revisi 5):** 3 sub-poin 2.4 lagi DIPUTUSKAN: (a) agent wajib cek & laporkan PR menggantung di awal tiap sesi baru, otomatis; (b) diverifikasi langsung ke lmarena Agent — agent secara teknis bisa merge (lewat shell/gh, bukan tool khusus) tapi defaultnya tidak pernah tanpa instruksi eksplisit, dan tetap minta konfirmasi metode merge walau diminta; (c) pembagian review Besar vs Kecil ditetapkan dengan prinsip "menyebar & susah dibalik = Besar (review manual), lokal & gampang diperbaiki = Kecil (agent boleh tanya ringan)" — lengkap dengan tabel kategorinya. Sisa 2.4 yang masih terbuka: branch untuk sesi multi-tujuan, dan status Log Keputusan vs git history.
- **31 Agustus 2026 (revisi 6):** 2 sisa sub-poin 2.4 DIPUTUSKAN, sehingga **poin 2.4 (branch & merge strategy) SELESAI sepenuhnya**: (a) sesi multi-tujuan — bukan soal 1 sesi menghasilkan 2 branch sekaligus (itu tetap 1 sesi = 1 branch, otomatis), tapi soal urutan kerja: beda tujuan yang dikerjakan BERSAMAAN & sama-sama belum selesai wajib dipisah sesi/branch, tapi kalau pekerjaan pertama sudah di-merge dulu sebelum yang kedua dimulai, boleh 1 sesi/percakapan yang sama, tidak masalah; (b) Log Keputusan TETAP dipertahankan sebagai tabel di file, TIDAK digantikan git history, karena beda level detail (commit message = teknis singkat, Log Keputusan = alasan di balik keputusan).
- **31 Agustus 2026 (revisi 7):** Poin 2.1 (struktur folder repo) mulai diputuskan: (a) 1 repo untuk semua channel, folder terpisah per channel — bukan repo terpisah per channel; (b) hasil produksi harian dipecah 2 kategori — naskah final PERMANEN diarsipkan per channel (teks, ringan, mencegah pengulangan topik tanpa sadar & jaga konsistensi gaya bahasa), sementara breakdown shot/asset visual per-shot tetap SEMENTARA (dihapus dari repo setelah didownload, karena itu yang bikin repo bengkak). Masih perlu dirancang: lokasi file karakter lintas-channel, skeleton folder konkret, dan "entry point universal" (prompt standar pembuka tiap sesi).
- **31 Agustus 2026 (revisi 8):** Poin 2.1 diperluas signifikan dari diskusi soal cakupan "konsistensi": disadari bahwa konsistensi bukan cuma soal karakter, tapi juga latar/lingkungan, palet warna, gaya render, props (semua butuh jangkar visual) DAN gaya bahasa, tone, suara/voice (cukup teks+contoh, bukan jangkar visual) — dipetakan jadi 2 keluarga, TETAP 2 dokumen terpisah (Bank Konsistensi Visual vs Persona & Voice) karena beda cara pakai oleh agent, tapi wajib saling merujuk eksplisit. Ditambahkan checklist konsistensi wajib diisi saat Discovery. Skeleton folder diperbarui: `karakter-lintas-channel/` → `konsistensi-lintas-channel/` (cakupan lebih luas dari sekadar karakter), `channel/karakter/` → `channel/konsistensi-visual/`, dan Model Konten sekarang FOLDER (bukan file tunggal) supaya bisa punya `assets/` sendiri kalau perlu. **Ditambahkan poin baru 2.6 — Mekanisme Anti-Melenceng untuk Sesi Panjang**: solusi 2 lapis (checkpoint wajib tiap pindah tahap besar, membaca ulang sumber resmi bukan mengandalkan ingatan sesi; + perintah manual "cek konsistensi" yang bisa dipanggil kapan saja) untuk mengatasi risiko agent kehilangan jejak konteks di sesi yang sangat panjang & berlapis (pola kerja nyata pengguna: ekstrak buku → ide → naskah → eksekusi per konten bertahap).
- **31 Agustus 2026 (revisi 9):** **Ditambahkan poin baru 2.7 — Entry Point Universal.** Diverifikasi fakta teknis penting: di awal sesi, pengguna bisa memilih repo DAN branch (termasuk melihat daftar branch lama yang belum di-merge dan memilih salah satu secara sengaja) — ini menyederhanakan mekanisme "lanjut kerjaan lama di sesi baru" jadi cukup "pilih branch yang sesuai", tidak perlu mekanisme rumit tambahan. Dirancang 2 skenario (lanjut di chat yang sama vs buka chat baru) dan 5 langkah urutan entry point untuk Skenario B: deteksi kondisi branch (baru/kosong vs lama/ada isi) → cek PR menggantung → tanya tujuan sesi → baca file relevan otomatis → deteksi jenis sesi (Discovery/Produksi). Penulisan entry point ini jadi dokumen/prompt konkret ditunda ke tahap Kategori 3, sesuai urutan kerja yang sudah disepakati.
- **31 Agustus 2026 (revisi 10):** **Poin 2.2 (asset biner) SELESAI dibahas sepenuhnya.** Struktur folder mengikuti skeleton 2.1. Ditetapkan 3 jenis referensi per elemen: acuan utama (wajib, 1 gambar netral), reference sheet (baru — konsep "character turnaround sheet"/grid multi-sudut dari pengalaman pengguna dengan Google Flow, dipakai untuk kebutuhan variasi sudut/keadaan, TIDAK menggantikan acuan utama), dan referensi tambahan situasional (opsional). Ketiganya bisa dipakai bersamaan (agent terbukti bisa gabung sampai 10 gambar referensi sekaligus). Prompt Master WAJIB otomatis dipasangkan dengan file gambar tiap generate — tidak perlu diminta manual. Sample output visual yang disetujui digabung ke folder referensi yang sama, bukan kategori terpisah.
- **31 Agustus 2026 (revisi 11):** **Poin 2.3 (karakter Tipe B) SELESAI dibahas sepenuhnya.** Deskripsi karakter Tipe B disimpan menempel ke arsip naskah konten yang memakainya (`arsip-naskah/` channel terkait), bukan file karakter mandiri terpisah. Deteksi "saatnya naik kelas ke Tipe A" jadi tugas OTOMATIS agent — agent cek dulu ke arsip channel sebelum bikin karakter Tipe B baru, tawarkan naik kelas kalau ada kecocokan dengan karakter lama, keputusan akhir tetap di tangan pengguna. Menempel ke entry point universal (2.7) sebagai bagian dari langkah baca file relevan.

**Status Kategori 2 setelah revisi 11:** 2.1 selesai, 2.2 selesai, 2.3 selesai, 2.4 selesai. Tersisa: 2.5 (apakah sesi Discovery masih perlu dipisah dari sesi Produksi).
- **31 Agustus 2026 (revisi 12):** **Poin 2.5 SELESAI dibahas — KATEGORI 2 SELESAI SEPENUHNYA.** Alasan asli pemisahan Discovery/Produksi (konteks chat berantakan) dikonfirmasi sudah tidak relevan dengan agent+repo. Tapi pemisahan tetap berlaku sebagai penerapan langsung prinsip sesi multi-tujuan dari 2.4: Discovery dan Produksi adalah 2 tujuan berbeda, wajib dipisah HANYA kalau dikerjakan bersamaan dalam kondisi sama-sama belum selesai; kalau salah satu sudah di-merge dulu, boleh lanjut di sesi yang sama. Bukan keputusan baru, murni klarifikasi penerapan 2.4. Langkah berikutnya: Kategori 3 (menulis ulang gaya prompt).
- **31 Agustus 2026 (revisi 13):** **KATEGORI 3 SELESAI SEPENUHNYA.** 3.1: semua instruksi "tempel isi file" diganti "baca file di path X", konsisten dengan entry point universal (2.7). 3.2: sudah terjawab lewat 2.4 (titik approval Besar/Kecil), tidak ada keputusan tambahan. 3.3: fakta baru diverifikasi — lmarena Agent BISA diajak diskusi panjang tanpa eksekusi file, cukup instruksi eksplisit ("jangan eksekusi dulu, aku cuma mau nanya"), sehingga TIDAK PERLU pindah platform (Claude/GPT chat biasa) sama sekali untuk sesi Discovery — cukup pola diskusi-dulu-baru-eksekusi di sesi agent yang sama. Instruksi lama yang menyebut "jalankan di sesi chat terpisah" dihapus. Langkah berikutnya: Kategori 4 (konfirmasi cepat).
- **31 Agustus 2026 (revisi 14 — FINAL, seluruh audit selesai):** **KATEGORI 4 SELESAI.** 5 dari 6 poin dikonfirmasi tetap tanpa perubahan (Hierarki, Pemisahan Suara/Wujud, Aturan Pewarisan, Tipe A/B karakter, teknik prompting `06` A-E). 1 poin DIREVISI: 6 Tahap Pipeline Produksi tidak lagi dianggap kaku sama untuk semua — jadi "kerangka tetap, detail fleksibel": kerangka 6 tahap dipertahankan sebagai struktur umum, tapi detail konkret tiap tahap (terutama Breakdown) ditentukan per Model Konten saat sesi Discovery-nya sendiri, bukan dipaksakan template seragam di depan — merespons kekhawatiran valid bahwa jenis konten berbeda (video/infografis/komik) butuh detail tahap yang berbeda. **DENGAN INI, SELURUH AUDIT (Kategori 0, 1, 2, 3, 4) SUDAH SELESAI DIBAHAS DAN DIKUNCI.** Langkah selanjutnya adalah tahap eksekusi: merevisi 10 dokumen sistem asli satu per satu berdasarkan seluruh keputusan yang terkumpul di audit ini.

---

## STATUS EKSEKUSI (dimulai 31 Agustus 2026, sesi lanjutan setelah audit selesai)

Tahap ini di luar cakupan audit di atas — audit ini adalah PETA keputusan, sedangkan eksekusi adalah kerja menulis ulang dokumen sungguhan berdasarkan peta itu. Dicatat di sini supaya progres tidak hilang kalau sesi terputus.

**Keputusan tambahan yang muncul saat eksekusi (belum ada di Kategori 0-4 di atas):**
- **Dokumen baru: `PANDUAN_PENGGUNA.md`** — terpisah dari 10 dokumen sistem yang di-upload ke repo (yang itu murni instruksi UNTUK AGENT, diupload apa adanya tanpa modifikasi pengguna). `PANDUAN_PENGGUNA.md` ini untuk PENGGUNA sendiri (bukan diupload ke repo) — isinya langkah konkret mulai dari nol (bikin repo, upload dokumen sistem, kalimat yang diketik ke agent di tiap skenario umum, istilah teknis dijelaskan awam). Dibuat PALING TERAKHIR, setelah semua 10 dokumen sistem selesai direvisi, karena isinya merujuk detail final dari semua dokumen itu.

**Progres revisi 10 dokumen sistem (checklist, urutan sesuai struktur dokumen):**
- [x] `00_CARA_PAKAI_SISTEM.md` — SELESAI direvisi
- [x] `START_DI_SINI.md` — SELESAI direvisi
- [x] `01_BRAND_CORE.md` — SELESAI direvisi
- [x] `02_CHANNEL_DISCOVERY_PROMPT.md` — SELESAI direvisi
- [x] `03_TEMPLATE_CHANNEL_BRIEF.md` — SELESAI direvisi
- [x] `04_CHARACTER_BUILDER_KIT.md` — SELESAI direvisi (diganti nama konsep jadi Bank Konsistensi Visual)
- [x] `05_CONTENT_PRODUCTION_PIPELINE.md` — SELESAI direvisi
- [x] `06_PROMPT_LIBRARY.md` — SELESAI direvisi
- [x] `07_MODEL_KONTEN_DISCOVERY_PROMPT.md` — SELESAI direvisi
- [x] `08_TEMPLATE_MODEL_KONTEN_BRIEF.md` — SELESAI direvisi
- [x] `PANDUAN_PENGGUNA.md` (dokumen baru, dibuat terakhir) — SELESAI dibuat

**SEMUA 11 DOKUMEN (10 dokumen sistem + PANDUAN_PENGGUNA.md) SUDAH SELESAI.** Tahap eksekusi audit ini tuntas sepenuhnya per 1 September 2026.

---

## AUDIT MENYELURUH PASCA-EKSEKUSI (1 September 2026)

Dilakukan atas permintaan eksplisit pengguna untuk memastikan tidak ada yang tertinggal — bukan sekadar percaya diri bahwa penulisan per-dokumen sudah benar. Metode: cross-check sistematis semua 11 file satu sama lain dan terhadap 10 dokumen asli, mencari 4 jenis masalah: (1) sisa istilah lama yang belum diganti, (2) konsep/paragraf dari dokumen asli yang hilang tanpa sengaja saat revisi, (3) inkonsistensi rujukan antar dokumen (nomor bagian, nama path), (4) keputusan di audit ini yang ternyata tidak sungguh masuk ke file final.

**Ditemukan dan diperbaiki:**
1. `00_CARA_PAKAI_SISTEM.md` — sisa istilah "Character Bible" nyantol di daftar kategori Besar (seharusnya sudah full jadi "Bank Konsistensi Visual"), sudah diperbaiki.
2. `05_CONTENT_PRODUCTION_PIPELINE.md` — **bug lebih signifikan:** 1 paragraf logika penting dari dokumen asli (soal harus cek Mode "Ikuti Kerangka Standar" vs "Alur Kerja Kustom" di Model Konten Brief sebelum mengikuti dokumen ini sebagai acuan) hilang total saat revisi, tergantikan kalimat baru yang diam-diam cuma mengasumsikan Mode Standar. Ini inkonsistensi nyata dengan `07`/`08` yang tetap mempertahankan konsep Mode Kustom lengkap. Sudah diperbaiki — paragraf logika Mode dikembalikan dan disesuaikan dengan istilah/path baru.

**Diverifikasi AMAN (tidak ada masalah):**
- Semua rujukan nomor bagian Channel Brief (bagian 3, 5, 7, 8) dari dokumen lain — cocok persis dengan isi `03` final.
- Semua path folder (`konsistensi-visual/`, `arsip-naskah/`, `_produksi-aktif/`, dll) — konsisten ejaan di semua 11 file.
- Konsep-konsep kunci dari dokumen asli (Area Berisiko Tinggi, Log Keputusan, GERBANG ALUR KERJA, Contoh Konkret, drift, dst) — semua masih ada di versi revisi, tidak ada yang hilang tanpa sengaja (kecuali kasus poin 2 di atas, sudah diperbaiki).
- Word count semua dokumen revisi LEBIH PANJANG dari asli — tidak ada tanda pemangkasan drastis yang mencurigakan.
- Keputusan kunci audit (reference sheet, deteksi otomatis Tipe B, checklist konsistensi, Entry Point Universal, kategori Besar/Kecil, perintah "cek konsistensi", cek PR menggantung) — semua terverifikasi tersebar ke dokumen yang relevan, bukan cuma disebut sekali lalu dilupakan.
- Kalimat pemicu mode diskusi — terverifikasi HANYA ada di `PANDUAN_PENGGUNA.md`, tidak bocor ke dokumen sistem manapun (konsisten dengan aturan pemisahan yang sudah dikoreksi sebelumnya).

**Kesimpulan audit:** sistem sudah solid dan konsisten, dengan 1 bug signifikan (poin 2) dan 1 sisa istilah kecil (poin 1) yang berhasil ditemukan lewat pengecekan sistematis dan sudah diperbaiki. Ini menunjukkan pengecekan menyeluruh seperti ini bernilai nyata — tidak cukup mengandalkan "sudah ditulis dengan hati-hati" tanpa verifikasi silang eksplisit.

---

## AUDIT PUTARAN KEDUA (1 September 2026) — atas permintaan eksplisit pengguna setelah sesi sempat terputus berkali-kali

Pengguna secara wajar meminta verifikasi ulang menyeluruh karena sesi terputus berkali-kali menimbulkan keraguan — bukan meragukan kompetensi, tapi minta bukti konkret sebelum download. Dilakukan audit lebih dalam dari putaran pertama, dengan metode: (1) bersihkan file lama yang membingungkan, (2) grep sistematis untuk placeholder/tanda belum selesai, (3) verifikasi struktur markdown (heading, tabel), (4) bandingkan SEMUA heading dari 10 dokumen asli vs revisi satu per satu, (5) **baca ulang utuh ke-11 file dari awal sampai akhir** (bukan cuma grep sepotong), (6) verifikasi byte-per-byte working directory vs folder yang bisa didownload pengguna.

**Ditemukan dan diperbaiki:**
1. File-file LAMA (versi pra-revisi) masih tertinggal sejajar dengan folder `revisi/` di root folder output — berisiko pengguna salah download versi lama tanpa sadar. Sudah dihapus, hanya folder `revisi/` (11 file final) dan `09_AUDIT` yang tersisa di root.
2. `04_CHARACTER_BUILDER_KIT.md` — 5 kemunculan frasa "generate gambar/video" yang menyesatkan (seolah agent bisa generate video langsung, padahal sudah terverifikasi TIDAK BISA di Kategori 1.3). Diperbaiki jadi presisi: agent generate gambar, video lewat tools eksternal dengan referensi visual yang sama.
3. `00_CARA_PAKAI_SISTEM.md` dan `03_TEMPLATE_CHANNEL_BRIEF.md` — rujukan "di sistem versi aplikasi" (analogi ke coding agent yang dipakai di awal diskusi kita) diperhalus/dihapus supaya dokumen berdiri sendiri tanpa bergantung konteks luar yang tidak dijelaskan di dalam sistem ini sendiri.

**Diverifikasi AMAN lewat pembacaan utuh (tidak ada masalah):**
- Semua 10 dokumen asli dibandingkan heading-per-heading dengan versi revisi — semua konsep dari asli punya padanan di revisi (berganti istilah sesuai keputusan, atau bertambah sesuai keputusan baru), tidak ada yang hilang tanpa jejak.
- Tidak ada placeholder/TODO/tanda belum selesai tersisa di manapun.
- Semua tabel markdown well-formed (termasuk 2 tabel di `08` yang sengaja beda jumlah kolom — bukan bug).
- Path `channel-brief.md`, `bank-konsistensi.md`, `brief.md`, `arsip-naskah/indeks.md` — semua konsisten dengan skeleton resmi di `00`.
- Isi `07` dan `08` (Mode Standar vs Mode Kustom) sekarang **cocok persis** dengan `05` setelah perbaikan bug di atas — dicek eksplisit karena ini titik yang paling rawan bug (3 dokumen saling merujuk dan harus konsisten satu sama lain).
- `PANDUAN_PENGGUNA.md` — daftar 10 dokumen untuk diupload dihitung ulang, tepat 10, cocok dengan checklist audit; tidak menyebut kemampuan video yang keliru.
- Verifikasi byte-per-byte akhir: seluruh 11 file di working directory identik 100% dengan yang ada di folder `outputs/revisi/` yang bisa didownload pengguna — tidak ada file yang "ketinggalan" tersinkron.

**Status akhir: sistem sudah diperiksa 2 putaran independen, ditemukan dan diperbaiki total 5 masalah kecil-menengah (1 di putaran pertama, 4 di putaran kedua — termasuk 1 bug presisi soal kemampuan video yang cukup penting), tidak ada masalah baru ditemukan di pembacaan akhir. Sistem siap didownload.**

**Cara kerja yang disepakati:** 1 dokumen direvisi penuh → pengguna review → baru lanjut ke dokumen berikutnya (bukan revisi banyak sekaligus), supaya kesalahan interpretasi kecil tidak menyebar ke dokumen-dokumen berikutnya sebelum ketahuan.

**ATURAN — cara menempatkan konten di dokumen sistem vs `PANDUAN_PENGGUNA.md` (dikoreksi 31 Agustus 2026, menggantikan versi sebelumnya yang terlalu ketat):**

Pengguna TIDAK meminta pemisahan ketat/prinsipil antara "konten untuk agent" dan "konten untuk pengguna" — yang penting adalah (a) tidak bikin rancu cara kerja, dan (b) semua yang pengguna butuh tetap ADA di `PANDUAN_PENGGUNA.md`, tidak boleh cuma ada di dokumen sistem lalu hilang dari pandangan pengguna. Tumpang tindih antar dokumen tidak masalah selama itu tidak bikin bingung.

**Tes yang dipakai untuk memutuskan penempatan:** apakah instruksi ini MENENTUKAN KUALITAS/CARA KERJA agent (struktur pertanyaan Discovery, format output yang diharapkan, urutan proses, dll)? Kalau ya — **WAJIB tetap penuh di dokumen sistem**, meskipun bentuknya terlihat seperti "instruksi untuk orang" (prompt di `02`, `04`, `06`, `07` semuanya masuk kategori ini, jangan dipindah/dipangkas ke panduan pengguna). Kalau instruksi itu murni pengetahuan praktis yang tidak menentukan cara kerja agent (misal: kalimat pemicu mode diskusi, cara bikin repo baru) — itu cocok di `PANDUAN_PENGGUNA.md`, dan BOLEH juga disebut ringan di dokumen sistem sebagai konteks tambahan, tidak perlu dihindari.

**Revisi dari kesalahan sebelumnya:** aturan versi awal (pelanggaran ditemukan di `00`/`01`, dikoreksi dengan memindahkan kalimat pemicu ke panduan pengguna) — koreksi itu SENDIRI masih valid untuk kasus spesifik itu (kalimat pemicu memang murni pengetahuan praktis, bukan instruksi substantif). Yang salah bukan koreksinya, tapi PRINSIP UMUM yang ditarik darinya ("harus terpisah ketat") — itu terlalu jauh dan tidak diminta pengguna. 8 dokumen sisanya (terutama `02`, `04`, `06`, `07` yang penuh prompt substantif) TIDAK perlu dipangkas isinya demi pemisahan — prompt-prompt itu tetap utuh di dokumen sistem.
