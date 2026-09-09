# Sistem Kerja Fondasi Konten Kreator (v3 — GitHub + Agent)
### Untuk kamu yang membangun banyak channel konten dengan bantuan AI, dari nol — mulai dari nentuin channel mau ngomongin apa, sampai konten jadi dan siap publish. Sistem ini berhierarki: Brand Core → Channel → Model Konten → Produksi, dan sekarang hidup di 1 repo GitHub yang dikerjakan lewat AI agent (lmarena Agent) yang bisa baca-tulis file dan generate gambar langsung.

---

## Kenapa dokumen ini dibuat

Kamu mau serius jadi konten kreator dan mau memanfaatkan AI habis-habisan — bukan cuma sesekali minta ide, tapi AI jadi partner kerja di semua tahap: gali ide, bangun karakter, tulis naskah, generate visual, sampai publish. Masalahnya, kalau ini dikerjakan tanpa sistem, ada beberapa hal yang hampir pasti kejadian:

1. **Brand voice / karakter berubah-ubah.** Sesi kerja hari ini AI generate karakter dengan wajah dan gaya bicara tertentu, besok beda lagi — karena AI nggak pernah benar-benar "ingat", dia cuma menebak ulang dari instruksi yang kamu ketik saat itu. Tanpa referensi yang dikunci, hasilnya nggak akan pernah konsisten.
2. **Tiap channel baru dimulai dari nol.** Padahal banyak hal yang sebenarnya bisa dipakai ulang — cara gali ide, cara bikin karakter, cara generate gambar konsisten — itu semua generik, nggak perlu dipikirkan ulang dari awal tiap kali buka channel baru.
3. **Nggak ada pedoman baku, jadi tiap sesi kerja "mulai dari mikir cara kerja" dulu**, bukan langsung eksekusi. Ini boros waktu dan bikin hasil nggak konsisten dari hari ke hari.
4. **1 channel bisa punya beberapa cara produksi berbeda** (misal animasi 60 detik vs gambar statis + narasi), dan itu butuh detail teknis sendiri-sendiri tanpa merusak konsistensi level channel di atasnya.
5. **Konsistensi bukan cuma soal karakter.** Latar/lingkungan, palet warna, gaya render, props yang berulang, sampai suara/voice — semua ini butuh "jangkar" yang sama pentingnya dengan karakter, dan sering luput dipikirkan sampai sudah terlanjur berubah-ubah antar konten.
6. **Sesi kerja bisa sangat panjang dan berlapis** (misal: ekstrak ide dari buku → kumpulkan bahan → eksekusi konten satu per satu, tiap eksekusi ada beberapa tahap lagi) — di sesi sepanjang itu, ada risiko nyata AI "kehilangan jejak" apa yang sudah disepakati di tahap-tahap awal begitu sampai di tahap akhir.

Sistem ini dirancang meniru prinsip yang sama seperti sistem membangun aplikasi lewat AI coding agent: **pisahkan yang "dipikirkan sekali" dari yang "dipakai berulang"**, dan **kunci keputusan-keputusan penting di satu tempat** (sekarang benar-benar berupa file permanen di repo, bukan cuma teks di percakapan) supaya AI (dan kamu sendiri) nggak improvisasi ulang tiap sesi.

Ada 5 prinsip inti yang penting dipahami sejak awal:

**Prinsip Hierarki.** Sistem ini berlapis dari umum ke spesifik: **Brand Core** (kamu sebagai kreator, lintas semua channel) → **Channel** (1 saluran konten dengan niche & voice sendiri) → **Model Konten** (1 cara produksi/format spesifik dalam channel itu — bisa cuma beda detail teknis dari pipeline standar, BISA JUGA punya alur kerja sendiri dari akar kalau strukturnya memang beda total, misal ada tahap ekstraksi dari sumber eksternal yang menghasilkan banyak bahan sekaligus) → **Produksi harian** (1 konten spesifik). Tiap level mewarisi apa yang sudah dikunci di level atasnya, dan cuma menambahkan/meng-override yang spesifik di level itu — TIDAK mengulang dari nol. Hierarki ini sekarang tercermin langsung sebagai struktur folder fisik di repo (lihat bagian Struktur Repo di bawah), bukan cuma penamaan file.

**Prinsip Rantai (Chaining).** Karena tiap konten butuh alur kerja yang bisa berbeda-beda (ada yang perlu riset dulu, ada yang bisa langsung eksekusi, ada yang di tengah jalan muncul kebutuhan baru), pipeline produksi di sistem ini bukan template kaku yang kamu susun manual tahap demi tahap. Dengan agent, chaining ini sekarang bisa terjadi lebih langsung — agent membaca sendiri hasil tahap sebelumnya dari repo dan melanjutkan ke tahap berikutnya tanpa kamu perlu copy-paste prompt manual. Tapi ini TIDAK berarti agent boleh terus jalan tanpa henti — ada titik-titik approval yang wajib (lihat Prinsip Approval Bertingkat di bawah) supaya kamu tetap pegang kendali di hal-hal yang penting. Detail mekanismenya ada di `06_PROMPT_LIBRARY.md` bagian 0.

**Prinsip Pemisahan Suara vs Wujud, Diperluas jadi Pemisahan Konsistensi Visual vs Non-Visual.** "Konsistensi" itu sebenarnya bercabang jadi 2 keluarga berbeda sifat, yang perlu ditangani dengan cara berbeda:
- **Konsistensi Non-Visual** (Persona & Voice Channel) — gaya bahasa/tone/cara channel ini "bicara" ke penonton, termasuk karakteristik suara/voice kalau pakai text-to-speech. Ini **SELALU ada**, bahkan channel faceless sekalipun. Cukup dijaga lewat deskripsi + contoh nyata (naskah lama), tidak butuh file gambar.
- **Konsistensi Visual** (Bank Konsistensi Visual) — mencakup lebih dari sekadar karakter: **Karakter** (entitas berwujud, opsional, ada Tipe A permanen dan Tipe B per-konten), **Latar/lingkungan**, **Palet warna & gaya render**, dan **Props/objek berulang** — semua ini butuh jangkar berupa file gambar referensi yang dirujuk ulang tiap generate, bukan cuma deskripsi teks.

Kedua dokumen ini (Bank Konsistensi Visual dan Persona & Voice) TETAP terpisah secara fisik (beda cara pakai oleh agent), tapi WAJIB saling merujuk eksplisit di bagian yang terkait — misal bagian Karakter di Bank Konsistensi Visual mencantumkan rujukan ke gaya bicara karakter itu di Persona & Voice.

**Prinsip Approval Bertingkat.** Tidak semua hasil kerja agent butuh level pengawasan yang sama. Ada 2 sumbu yang WAJIB dibedakan dan sering tertukar: **kategori dampak** (seberapa besar akibat kalau salah) dan **jenis gerbang** (apa persisnya yang kamu izinkan saat itu).

*Kategori dampak:*
- **Besar** (Brand Core, Channel/Model Konten Brief, Bank Konsistensi Visual, konten produksi final) — kamu WAJIB review isi lengkapnya dulu sebelum di-merge ke `main`, karena kesalahan di sini bisa menyebar ke banyak konten ke depan atau susah dibalik.
- **Kecil** (Log Keputusan, Bank Ide Awal, catatan administratif) — agent cukup tanya ringan "mau saya merge sekarang?" tanpa kamu perlu baca detail, karena dampaknya lokal dan gampang diperbaiki lagi nanti kalau salah.

*Jenis gerbang (G1/G2/G3) — inilah yang menentukan agent boleh melakukan apa setelah kamu menjawab:*

| Kode | Nama | Pertanyaan yang diajukan agent | Kalau kamu setuju, agent boleh | TIDAK memberi izin untuk |
|---|---|---|---|---|
| **G1** | Review output tahap | "Hasil tahap ini sudah sesuai? Lanjut atau ulang?" | Lanjut ke tahap berikutnya dalam pipeline yang sama | Menganggap isinya final, atau merge ke `main` |
| **G2** | Approval keputusan besar | "Isi ini saya kunci sebagai keputusan resmi?" | Menetapkan isi sebagai sumber resmi yang diwarisi kerja berikutnya | Merge ke `main` |
| **G3** | Approval merge | "Perubahan ini saya merge ke `main`?" | Merge PR ke `main` | Menambah keputusan baru yang belum lewat G2 |

**Aturan yang mengikat agent:**
- G1 **tidak pernah** naik otomatis jadi G2 atau G3. "Oke lanjut" pada satu tahap BUKAN persetujuan isi final dan BUKAN izin merge.
- Agent WAJIB menyebutkan kode gerbang saat bertanya (misal: *"G1 — lanjut ke Tahap 4?"*), supaya jelas apa yang sedang kamu setujui.
- Kalau kamu memberi jawaban ambigu ("bagus", "sip") pada G2/G3, agent WAJIB minta penegasan eksplisit, bukan menafsirkannya sebagai approval.
- Semua approval yang sudah diberikan dicatat di `STATUS.md` beserta kode gerbangnya — supaya sesi berikutnya tahu persis sampai mana izin yang sudah ada (lihat `STATUS_TEMPLATE.md`).

**Prinsip Checkpoint & Verifikasi Konsistensi.** Karena sesi kerja bisa sangat panjang, ada 2 lapis pertahanan terhadap risiko agent "melenceng" dari yang sudah disepakati:
- **Checkpoint otomatis** — setiap kali sesi pindah dari 1 tahap besar ke tahap besar berikutnya, agent WAJIB berhenti sejenak dan meringkas ulang apa yang sudah disepakati, dengan cara membaca ulang sumber resmi (bukan mengandalkan ingatan sesi).
- **Perintah manual "cek konsistensi"** — bisa kamu panggil kapan saja, agent akan membandingkan hasil kerja terbaru dengan sumber resmi (Channel Brief, Bank Konsistensi Visual, Persona & Voice) dan melaporkan kalau ada yang melenceng.

---

## Aturan Folder Khusus — `panduan/`

Repo ini memiliki folder `panduan/` yang berisi `PANDUAN_PENGGUNA.md`. Ini adalah file khusus untuk pengguna manusia, BUKAN instruksi eksekusi untuk agent. Folder ini memiliki aturan eksplisit:

- **Agent TIDAK BOLEH memproses isi `panduan/` sebagai instruksi eksekusi** kecuali pengguna meminta secara eksplisit (misalnya: "tolong baca bagian Prompt Pembuka Universal di `panduan/PANDUAN_PENGGUNA.md`").
- File di `panduan/` hanya dibaca oleh agent saat pengguna meminta eksplisit — ini mencegah agent jadi bingung karena isi file tersebut berisi panduan praktis, bukan struktur kerja.
- Ini sesuai dengan keputusan desain sistem: semua instruksi eksekusi agent tetap di `_sistem/`, semua panduan praktis pengguna di `panduan/`.

---

## Mekanisme Universal — Satu Prompt Masuk

Sistem ini dirancang supaya kamu tidak perlu mikir ulang dari nol setiap masuk sesi. Mekanisme universal sudah tersedia di `panduan/PANDUAN_PENGGUNA.md` (bagian "Prompt Pembuka Universal"). Cukup masukkan prompt itu di awal sesi — agent akan:

1. Membaca `_sistem/START_DI_SINI.md` dan `_sistem/00_CARA_PAKAI_SISTEM.md`
2. Mendeteksi kondisi branch dan melaporkan PR menggantung
3. Menanyakan tujuan sesi ini
4. Membaca file sistem relevan secara otomatis (tanpa kamu tempel manual)
5. Membawa kamu langsung ke langkah yang tepat

> Ini berarti: kamu cukup masukkan prompt universal di chat pertama, lalu di chat kedua (atau dalam sesi yang sama setelah agent memahami konteks) kamu tinggal jelaskan apa yang kamu mau. Agent sudah tahu semua konteks sistem.

---

## Struktur Repo

Semua channel hidup dalam **1 repo GitHub** (bukan repo terpisah per channel — supaya Brand Core dan elemen lintas-channel punya 1 rujukan bersama, tidak perlu diduplikasi manual):

```
nama-repo/
├── _sistem/                          ← 10 dokumen sistem ini (00-08, plus START_DI_SINI.md)
│   ├── 00_CARA_PAKAI_SISTEM.md
│   ├── 01_BRAND_CORE.md              ← Brand Core, isi langsung di sini (1 untuk semua channel)
│   └── ...dst
│
├── konsistensi-lintas-channel/       ← Bank Konsistensi Visual untuk karakter/latar/dll yang dipakai >1 channel
│   └── [nama-elemen]/
│       ├── bank-konsistensi.md
│       └── referensi/
│           ├── acuan-utama.png       ← 1 gambar netral/default, WAJIB ada
│           ├── reference-sheet.png   ← grid multi-sudut/keadaan (turnaround), kalau perlu
│           └── tambahan-[keterangan].png (situasional, opsional)
│
├── channel-[nama-channel]/
│   ├── channel-brief.md              ← Channel Brief (termasuk Persona & Voice, checklist konsistensi)
│   ├── konsistensi-visual/           ← Bank Konsistensi Visual KHUSUS channel ini
│   │   └── [nama-elemen]/
│   │       ├── bank-konsistensi.md
│   │       └── referensi/
│   ├── model-konten/
│   │   └── [nama-model]/             ← Model Konten adalah FOLDER, bukan file tunggal
│   │       ├── brief.md
│   │       └── assets/               ← reference visual khusus model konten ini (opsional)
│   └── arsip-naskah/                 ← PERMANEN — naskah final konten yang sudah publish
│       ├── indeks.md                 ← tabel ringkas: judul, tanggal, topik singkat
│       ├── indeks-karakter.md        ← tabel karakter Tipe B: ciri ringkas + link arsip sumber
│       │                                (sumber data pengecekan karakter berulang — bukan indeks.md)
│       ├── [tanggal]-[judul].md      ← termasuk deskripsi karakter Tipe B yang dipakai, kalau ada
│       ├── [tanggal]-[judul]-metadata.md ← arsip ringan: prompt final, versi brief, daftar asset
│       └── [tanggal]-[judul]-sumber.md ← jejak sumber eksternal, kalau konten itu memakainya
│
└── _produksi-aktif/                  ← SEMENTARA — breakdown shot & asset visual produksi berjalan
    └── [channel]-[judul-konten]/
        ├── STATUS.md                 ← status persisten wajib (checkpoint & recovery)
        ├── SUMBER.md                 ← wajib begitu ada 1 sumber eksternal dipakai
        ├── naskah-draft.md
        ├── breakdown-output.md       ← unit output (shot/panel/section/segmen/bagian) per Model Konten
        │                                (boleh dinamai breakdown-shot.md kalau unitnya memang shot)
        └── assets/
```

**Aturan penting soal folder `_produksi-aktif/`:** begitu 1 konten selesai dan sudah kamu download/pakai, folder ini DIHAPUS dari repo (breakdown shot dan asset visual itu berat, bikin repo bengkak kalau menumpuk). Naskah finalnya sendiri (bukan breakdown/asset) dipindah dulu ke `arsip-naskah/` channel terkait sebelum folder produksi dihapus — begitu juga arsip ringan `[tanggal]-[judul]-metadata.md` (prompt final, versi brief, daftar asset) dan `SUMBER.md` kalau konten itu memakai sumber eksternal — naskah itu ringan (teks) dan berguna permanen untuk mencegah pengulangan topik tanpa sadar dan menjaga konsistensi gaya bahasa dari waktu ke waktu.

**Kenapa dipecah jadi beberapa file, bukan satu file besar?**
Karena tiap channel dan tiap model konten kebutuhannya beda — channel faceless nggak akan pernah buka bagian karakter, channel dengan 1 model konten nggak akan buka Model Konten Discovery berkali-kali. Kalau semua digabung satu file, bagian yang "harus dilewati" jadi bikin bingung dan file jadi terlalu panjang untuk dibaca ulang tiap hari.

---

## Empat Level Sistem

| Level | Dokumen Generator | Dokumen Hasil (living document, lokasi di repo) | Sifat |
|---|---|---|---|
| **1. Brand Core** | `01_BRAND_CORE.md` | `_sistem/01_BRAND_CORE.md` (isi di file yang sama) | 1 untuk semua channel, jarang berubah |
| **2. Channel** | `02_CHANNEL_DISCOVERY_PROMPT.md`, `04_CHARACTER_BUILDER_KIT.md` | `channel-[nama]/channel-brief.md` + `channel-[nama]/konsistensi-visual/` | 1 folder per channel |
| **3. Model Konten** | `07_MODEL_KONTEN_DISCOVERY_PROMPT.md` | `channel-[nama]/model-konten/[nama-model]/brief.md` | 1 folder per model konten, mewarisi dari Channel |
| **4. Produksi** | `05_CONTENT_PRODUCTION_PIPELINE.md` + `06_PROMPT_LIBRARY.md` | `_produksi-aktif/` (sementara) → naskah final pindah ke `arsip-naskah/` (permanen) | Dijalankan berulang tiap bikin 1 konten |

**Aturan pewarisan:**

> Begitu sebuah level sudah dikunci, **semua level di bawahnya WAJIB menyertakan konteks dari level di atasnya** sebagai dasar, dan hanya menambahkan/meng-override yang spesifik di level itu — TIDAK mengulang isi level atasnya, dan TIDAK generate "polos" tanpa konteks level atasnya. Ini yang paling sering menyebabkan brand voice dan karakter berubah-ubah antar sesi kalau dilanggar. Agent WAJIB membaca file level atasnya langsung dari repo (bukan menunggu kamu tempel isi filenya) — lihat bagian Entry Point Universal.
>
> Untuk karakter Tipe B (karakter per-konten, "yang diceritakan") — begitu dia muncul di 1 konten, deskripsinya WAJIB terus dibawa (chain) ke semua prompt lanjutan dalam konten yang sama, dan disimpan menempel ke arsip naskah konten itu (bukan file karakter mandiri). Sebelum membuat karakter Tipe B baru, agent WAJIB cek dulu ke arsip naskah channel — kalau ada kecocokan dengan karakter yang sudah pernah dipakai, agent menawarkan untuk menaikkannya jadi karakter Tipe A permanen. Keputusan akhir tetap di tangan kamu.
>
> Kalau di tengah kerja kamu (atau agent) menemukan alasan kuat untuk mengubah sesuatu yang sudah dikunci di level manapun, itu **keputusan sadar, bukan kebablasan** — update file level itu secara eksplisit (dan catat di Log Keputusan-nya, yang tetap dipertahankan sebagai tabel di dalam file, TIDAK digantikan git history karena beda level detail), jangan biarkan berubah diam-diam cuma karena sesi baru.

---

## Batasan Platform lmarena (fakta, bukan aturan kita)

Sistem ini dipakai via lmarena Agent Mode. Platform memiliki perilaku otomatis yang harus dipahami agar tidak salah asumsi — detail lengkap ada di `_meta/PLATFORM_LMARENA.md` di repo meta (salinan berlabelnya ikut folder ini, di _salinan-meta/):

1. **Branch arena otomatis dibuat:** Saat sesi dimulai, kamu boleh pilih base branch di UI, tapi setelah itu lmarena otomatis membuat branch baru `arena/...` dan semua kerja agent terjadi di situ. `main` hanya berubah setelah PR di-merge. Karena itu branch aktif yang harus diverifikasi adalah `arena/...`.

2. **Tidak bisa push setelah merge/close:** Setelah PR di-merge/close, platform mencabut token push untuk sesi tersebut. Sesi tersebut **tidak bisa** push lagi secara teknis (bukan "sebaiknya jangan"). File baru setelah merge akan terjebak di sesi. Workaround resmi: tambah `/download-workspace` di akhir URL sesi untuk download zip.

3. **Sesi bisa crash:** Chat tidak bisa lanjut, error halaman. Karena itu diskusi panjang yang belum jadi file + commit bisa hilang.

**Implikasi:** Karena fakta #2 dan #3, maka commit tiap tahap besar selesai dan **log sesi berkelanjutan** (aturan ringkas di bawah; aturan lengkap meta: _meta/PROTOKOL_CHECKPOINT_RECOVERY.md bagian "Log Sesi Berkelanjutan" di master (provenance)) bukan birokrasi, tapi syarat fisik supaya sesi baru bisa melanjutkan.

### Aturan Log Sesi (`LOG_SESI`) — self-contained

1. **Satu file per sesi:** `LOG_SESI_YYYY-MM-DD.md` di folder scope kerja (unit kerja, akar sistem, atau root repo bila lintas sistem).
2. **Update + commit + push segera** setelah tiap pertukaran yang menghasilkan informasi baru — bukan mekanis tiap giliran.
3. **Header "Keadaan Sesi" selalu segar** (agent baru membaca ini dulu): di mana kita sekarang, apa yang sudah disepakati, apa yang masih terbuka, langkah berikutnya.
4. **Yang dicatat:** keputusan/koreksi/kendala/preferensi pengguna (near-verbatim), proposal penting agent + dasarnya, kesepakatan & penolakan + alasan, fakta/hasil verifikasi sesi ini, perubahan state kerja, pertanyaan terbuka.
5. **Yang TIDAK dicatat:** konfirmasi ("oke"), basa-basi, pengulangan isi yang sudah ada di `STATUS.md`/Log Keputusan (tunjuk path-nya), dump chat. — Filter ini WAJIB; inilah yang membuat aturan ini efisien, bukan overkill (biaya over-recording = detik; under-recording = jam konteks hilang).
6. **Akhir sesi:** header diisi final → `CLOSED` (atau `OPEN` + "dilanjutkan di mana"). **Awal sesi baru:** cari `LOG_SESI_*.md` terbaru; yang `OPEN` → baca, laporkan keadaan, konfirmasi ke pengguna sebelum lanjut.

## Entry Point Universal — Cara Mulai atau Lanjut Sesi

Di awal sesi lmarena Agent, kamu bisa memilih repo DAN branch yang mau dipakai — termasuk melihat daftar branch lama yang belum di-merge dan memilih salah satu secara sengaja. Ini membedakan 2 skenario:

**Skenario A — Lanjut di jendela chat yang sama** (belum ditutup, cuma jeda): tidak butuh langkah khusus, lanjut seperti biasa. Checkpoint otomatis akan tetap jalan kalau kamu pindah ke tahap besar berikutnya.

**Skenario B — Buka chat/sesi baru** (baik untuk kerjaan baru maupun nerusin branch lama yang sudah dipilih): agent WAJIB menjalankan urutan ini di awal sesi, sebelum mengerjakan apa pun:

1. **Deteksi kondisi branch** — apakah branch ini baru/kosong (baru bercabang dari `main`), atau branch lama yang sudah ada progres? Kalau branch lama, agent baca dulu apa yang sudah dikerjakan (file yang ada, commit terakhir) SEBELUM bertanya apa-apa. Verifikasi via `git branch --show-current` karena branch `arena/...` dibuat otomatis (fakta platform).
2. **Cek & laporkan PR yang menggantung** — otomatis, tanpa diminta, apapun jenis sesi berikutnya. Juga cek apakah PR dari branch aktif sudah MERGED — jika ya, sesi ini **tidak bisa** push lagi (fakta platform #2), harus buka sesi baru dari `main`.
3. **Tanya tujuan sesi ini** — mau mengerjakan apa (Discovery/Produksi/revisi/lainnya), di channel/model konten/konten yang mana.
4. **Baca sendiri file konteks wajib** berdasarkan jawaban di atas — bukan "file yang relevan" menurut tafsiran agent, tapi daftar deterministik di tabel **Konteks Wajib per Jenis Sesi** di bawah. Kamu TIDAK perlu tempel manual isi file apa pun — agent membaca langsung dari repo.
5. **Deteksi jenis sesi** (Discovery vs Produksi) — supaya aturan merge yang berlaku sesuai (lihat Prinsip Approval Bertingkat).

### Konteks Wajib per Jenis Sesi

Tabel ini mengikat: begitu tujuan sesi diketahui (langkah 3), agent WAJIB membaca semua **File wajib** di baris yang cocok sebelum menulis apa pun. Ini menggantikan penilaian bebas soal apa yang "relevan".

| Tujuan sesi | File wajib (baca semua) | File kondisional | Output wajib |
|---|---|---|---|
| **Brand Core baru** | `_sistem/01_BRAND_CORE.md` | — | `_sistem/01_BRAND_CORE.md` terisi |
| **Channel baru** | Brand Core, `_sistem/02_CHANNEL_DISCOVERY_PROMPT.md`, `_sistem/03_TEMPLATE_CHANNEL_BRIEF.md` | Channel Brief lain (kalau ada elemen dipakai bersama) | `channel-[nama]/channel-brief.md` |
| **Elemen konsistensi visual baru** | Brand Core, Channel Brief channel itu, `_sistem/04_CHARACTER_BUILDER_KIT.md` | `konsistensi-lintas-channel/` kalau elemen dipakai >1 channel | `konsistensi-visual/[elemen]/` + acuan visual sesuai tipe elemen |
| **Model konten baru** | Brand Core, Channel Brief, `_sistem/07_MODEL_KONTEN_DISCOVERY_PROMPT.md`, `_sistem/08_TEMPLATE_MODEL_KONTEN_BRIEF.md` | Bank Konsistensi Visual channel itu | `channel-[nama]/model-konten/[model]/brief.md` |
| **Produksi konten** | Brand Core, Channel Brief, Model Konten Brief, `_sistem/05_CONTENT_PRODUCTION_PIPELINE.md`, `_sistem/06_PROMPT_LIBRARY.md` | Bank Konsistensi Visual (kalau konten ini visual), `arsip-naskah/indeks.md` (cek pengulangan topik), `arsip-naskah/indeks-karakter.md` (kalau ada karakter Tipe B) | `_produksi-aktif/[channel]-[judul]/STATUS.md` + output tiap tahap |
| **Lanjut produksi yang terputus** | `STATUS.md` konten itu, lalu semua file wajib baris "Produksi konten", plus protokol recovery meta (provenance: _meta/PROTOKOL_CHECKPOINT_RECOVERY.md bagian "Recovery saat sesi baru" di master — **4 aturan mengikat di bawah sudah cukup untuk berdiri sendiri**) | Output tahap sebelumnya yang tercatat di `STATUS.md` — **diverifikasi benar-benar ada di branch**, bukan sekadar diklaim STATUS | `STATUS.md` diperbarui |
| **Revisi dokumen terkunci** | Dokumen yang direvisi + semua dokumen yang mewarisinya (turunannya) | Log Keputusan terkait | Dokumen revisi + baris Log Keputusan |
| **Cek konsistensi** | Sumber resmi yang relevan dengan objek yang dicek (Channel Brief, Bank Konsistensi Visual, Persona & Voice) | Output kerja terakhir | Laporan temuan (tanpa mengubah file) |

**Aturan pemakaian tabel:**

- Kalau ada file wajib yang **tidak ditemukan**, agent berhenti dan melapor — bukan melanjutkan dengan asumsi. File wajib yang hilang biasanya berarti dependency belum dibuat atau belum di-merge ke `main`.
- File kondisional yang **dilewati wajib disebutkan alasannya** di laporan awal sesi (misal: "Bank Konsistensi Visual dilewati — konten ini teks-only"). Ini supaya kelalaian membaca bisa dibedakan dari keputusan sadar.
- Baris di atas adalah **minimum**, bukan batas atas. Kalau agent butuh file lain untuk mengerjakan tugasnya, silakan baca — tapi jangan kurang dari daftar wajib.
- **Khusus baris "Lanjut produksi yang terputus" — aturan recovery yang mengikat:**
  1. **Verifikasi, jangan percaya klaim.** Setiap output yang disebut `STATUS.md` wajib dicek keberadaannya **di branch** (misal `git ls-tree -r HEAD --name-only`, `git log -1 -- [file]`, atau buka file-nya), bukan diterima dari kalimat STATUS. STATUS bisa salah atau tertinggal; branch yang menentukan.
  2. **Lanjutkan hanya dari tahap yang terbukti selesai.** Jangan mengulang tahap yang output-nya sudah ada, dan jangan melompat ke tahap yang dependency-nya belum ada.
  3. **Approval dibaca per kode gerbang.** `G1` tahap mana pun **tidak pernah** berarti `G2` atau `G3` (lihat Prinsip Approval Bertingkat di atas). Pernyataan lama seperti "sudah dikonfirmasi"/"sudah oke" **tanpa kode gerbang bukan approval** — minta gerbangnya diulang secara eksplisit.
  4. **Kalau output diklaim ada tapi tidak ditemukan: berhenti dan melapor.** Jangan membuat ulang diam-diam, jangan menebak isinya, jangan mengoreksi atau menghapus `STATUS.md` tanpa keputusan pengguna. Ini fail-closed sesuai FI-02 di _meta/FAILURE_INJECTION_TESTS.md (provenance).

### Aturan Kerja Bersamaan (Obsidian ↔ Agent ↔ PR)

Repo ini disentuh dari beberapa arah sekaligus: kamu lewat Obsidian (dengan plugin git yang bisa push otomatis), agent lewat sesi lmarena, dan PR yang menunggu merge. Tanpa aturan, tiga arah ini bisa saling menimpa.

**Aturan dasar:**

1. **Satu tujuan per branch.** Jangan campur Discovery channel A dengan produksi konten channel B di branch yang sama — kalau salah satunya perlu direvisi sebelum merge, yang lain ikut tertahan.
2. **Pull sebelum mulai.** Agent memverifikasi branch aktif dan commit terakhir di awal sesi (Entry Point langkah 1). Kamu di Obsidian: pull dulu sebelum mengedit, terutama kalau sesi agent baru saja berjalan.
3. **Jangan edit file yang sedang dikerjakan agent.** Selama sesi agent aktif mengerjakan dokumen tertentu, jangan edit file itu dari Obsidian. Kalau perlu mengubahnya, katakan ke agent — biar agent yang menulis, atau minta agent berhenti dulu di file itu.
4. **File yang sedang dikerjakan dicatat.** Untuk produksi, `STATUS.md` sudah mencatat output resmi dan tahap berjalan — itu penanda de facto file mana yang sedang "dipegang" agent.

**Kalau konflik tetap terjadi:**

- **Konflik teks di file yang sama** — jangan hapus salah satu versi supaya "cepat beres". Baca keduanya, tentukan mana yang lebih baru/benar berdasarkan Log Keputusan dan `STATUS.md`, gabungkan secara sadar, lalu catat di Log Keputusan bahwa terjadi konflik dan bagaimana diselesaikan.
- **Dua branch mengubah Channel Brief yang sama** — merge yang lebih dulu selesai, lalu branch kedua WAJIB rebase/merge dari `main` dan **membaca ulang** brief hasil merge sebelum melanjutkan. Jangan lanjut di atas versi brief yang sudah usang.
- **Push otomatis plugin git di tengah sesi agent** — kalau agent menemukan commit baru yang bukan buatannya di branch yang sama, agent berhenti dan melapor, bukan menimpa. 
- **PR lama masih terbuka saat sesi baru dimulai** — dilaporkan di Entry Point langkah 2. Putuskan dulu: merge, tutup, atau lanjutkan di branch itu. Jangan mulai kerja baru yang menyentuh file sama sebelum itu diputuskan.
- **Branch keliru** — kalau ternyata kerja dilakukan di branch yang salah, jangan hapus branch atau `main`. Buat PR dari branch itu apa adanya, atau cherry-pick commit yang relevan ke branch yang benar; keputusan dicatat.

**Catatan penting soal platform:** lmarena Agent bisa diajak diskusi panjang TANPA harus baca-tulis file tiap kali merespons, kalau pengguna memintanya secara eksplisit. Ini berarti sesi Discovery yang butuh diskusi panjang tidak perlu pindah ke platform chat lain seperti versi sistem sebelumnya — cukup dilakukan di sesi agent yang sama, mulai dari mode diskusi, baru pindah ke mode eksekusi begitu hasilnya matang dan pengguna mengonfirmasi. **Tapi** karena fakta platform #3 (sesi bisa crash), maka selama mode diskusi agent tetap memelihara **log sesi** (`LOG_SESI_YYYY-MM-DD.md` — aturan di bagian "Aturan Log Sesi" di atas) dan commit+push setelah tiap pertukaran yang menghasilkan informasi baru — supaya tidak hilang kalau crash. *(Kalimat spesifik untuk memicu mode diskusi ada di `panduan/PANDUAN_PENGGUNA.md`, bukan di sini)*

---

## Alur Kerja Keseluruhan

```
SETUP SEKALI DI AWAL
├─ Bikin repo GitHub baru khusus sistem ini (GitHub otomatis buat branch `main`)
├─ Push commit awal berisi skeleton folder + 10 dokumen sistem ke `main`
├─ Isi 01_BRAND_CORE.md (siapa kamu sebagai kreator, batasan/nilai lintas channel)
│
BUKA CHANNEL BARU (diulang tiap kali ada ide channel)
├─ Tahap A: Jalankan 02_CHANNEL_DISCOVERY_PROMPT.md (boleh mode diskusi dulu di sesi
│           agent yang sama, baru dieksekusi jadi file begitu matang)
│           → hasil: channel-[nama]/channel-brief.md, termasuk Persona & Voice dan
│             checklist konsistensi yang WAJIB terisi
├─ Tahap B: KALAU channel butuh elemen visual yang harus konsisten (karakter, latar,
│           dll) → jalankan 04_CHARACTER_BUILDER_KIT.md
│           → hasil: channel-[nama]/konsistensi-visual/[elemen]/ terisi, termasuk
│             gambar referensi (acuan utama + reference sheet kalau perlu)
├─ Review isi PR (kategori Besar) → merge ke main
│
TETAPKAN MODEL KONTEN (diulang tiap kali ada cara produksi/format baru dalam channel itu)
├─ Jalankan 07_MODEL_KONTEN_DISCOVERY_PROMPT.md (dengan konteks Channel Brief-nya,
│  agent baca sendiri) — termasuk menentukan bentuk detail tiap tahap pipeline untuk
│  model konten ini (kerangka 6 tahap tetap, detail fleksibel per format)
│  → hasil: channel-[nama]/model-konten/[nama-model]/brief.md
├─ Review isi PR (kategori Besar) → merge ke main
│
PRODUKSI KONTEN HARIAN (diulang terus selama channel jalan, berbentuk RANTAI)
├─ Entry point universal jalan otomatis di awal sesi (baca Channel Brief, Bank
│  Konsistensi Visual, Model Konten Brief — agent baca sendiri, tidak perlu ditempel)
├─ Mulai dari Tahap 1 di 05_CONTENT_PRODUCTION_PIPELINE.md (cek override dari
│  Model Konten Brief dulu sebelum eksekusi tiap tahap)
├─ Checkpoint otomatis tiap pindah tahap besar — agent ringkas ulang dari sumber
│  resmi, bukan dari ingatan sesi
├─ Kamu bisa panggil "cek konsistensi" kapan saja untuk verifikasi manual
├─ Kalau muncul karakter Tipe B di tengah produksi → otomatis ikut ter-chain, dan
│  agent cek dulu ke arsip naskah channel apakah karakter serupa sudah pernah dipakai
├─ Hasil kerja disimpan sementara di _produksi-aktif/
├─ Begitu konten selesai penuh → agent tawarkan merge (kategori Besar untuk konten
│  final, direview isinya dulu) → naskah final dipindah ke arsip-naskah/, folder
│  _produksi-aktif/ dihapus setelah kamu download hasilnya
├─ Kalau ada keputusan baru yang harus dikunci permanen di level manapun →
│  update file level itu, JANGAN biarkan cuma di ingatan sesi ini
```

---

## Cara Pakai Ringkas

1. Bingung mulai dari mana? Buka `START_DI_SINI.md` — itu peta pendek yang mengarahkan ke file yang tepat sesuai kebutuhanmu saat itu.
2. Isi `01_BRAND_CORE.md` sekali di awal, di repo yang sudah disiapkan.
3. Untuk tiap ide channel: jalankan `02_CHANNEL_DISCOVERY_PROMPT.md` → hasil jadi `channel-[nama]/channel-brief.md`.
4. Kalau channel itu butuh elemen visual yang harus konsisten: jalankan `04_CHARACTER_BUILDER_KIT.md`.
5. Untuk tiap cara produksi/format dalam channel itu: jalankan `07_MODEL_KONTEN_DISCOVERY_PROMPT.md` → hasil jadi `channel-[nama]/model-konten/[nama-model]/brief.md`.
6. Setiap mau produksi konten: buka sesi agent, entry point universal otomatis jalan (baca Channel Brief + Model Konten Brief yang relevan), ikuti `05_CONTENT_PRODUCTION_PIPELINE.md`, pakai teknik dari `06_PROMPT_LIBRARY.md`.
7. Ulangi langkah 3-6 tiap kali ada channel/model konten baru — dokumen generator (02, 04, 05, 06, 07) dipakai ULANG, tidak pernah ditulis dari nol lagi.
8. Selalu review PR sesuai kategorinya (Besar = baca detail dulu, Kecil = konfirmasi ringan) sebelum merge ke `main`.

---

## Kenapa Sesi Discovery Tetap "Terasa" Terpisah dari Sesi Produksi

Diskusi Discovery (Channel maupun Model Konten) itu panjang dan penuh bolak-balik ("coba ide A", "eh ganti B"). Alasan aslinya dulu murni soal keterbatasan chat biasa (konteks bercampur dalam 1 jendela percakapan) — dengan agent yang membaca dari file repo, alasan itu sudah tidak berlaku dengan cara yang sama.

Tapi pemisahan ini tetap relevan, dengan alasan yang lebih konkret: Discovery dan Produksi adalah **2 tujuan yang berbeda**. Kalau keduanya dikerjakan BERSAMAAN dalam kondisi sama-sama belum selesai, itu WAJIB dipisah jadi sesi/branch berbeda — supaya 1 PR punya 1 tujuan jelas dan gampang direview (lihat Prinsip Approval Bertingkat). Tapi kalau Discovery-nya sudah selesai dan di-merge dulu, kamu BOLEH lanjut langsung ke Produksi di sesi/percakapan yang sama — tidak perlu memaksakan diri pindah sesi hanya karena beda tujuan, selama urutannya benar (selesai dulu satu, baru mulai yang lain).

Brief yang sudah jadi berfungsi sebagai **hasil saringan bersih** — itu yang dibawa ke sesi produksi, bukan transkrip diskusi mentahnya.
