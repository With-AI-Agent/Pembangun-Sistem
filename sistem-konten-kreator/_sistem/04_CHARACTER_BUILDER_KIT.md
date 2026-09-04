# Bank Konsistensi Visual — Kit Pembangun

### Dipakai untuk membangun elemen visual yang harus konsisten berulang di suatu channel — KARAKTER UTAMA (Tipe A), dan/atau LATAR/LINGKUNGAN, PALET WARNA & GAYA RENDER, PROPS/OBJEK BERULANG. Tujuan utamanya menjawab langsung masalah konsistensi yang sering muncul: wajah/wujud berubah-ubah, kepribadian berubah-ubah, gaya visual berubah-ubah, latar tidak konsisten. Hasil akhir tiap elemen disimpan di `channel-[nama-channel]/konsistensi-visual/[nama-elemen]/` (atau `konsistensi-lintas-channel/[nama-elemen]/` kalau dipakai lebih dari 1 channel).

> **Catatan:** kalau yang kamu butuh adalah karakter yang cuma muncul di 1 konten spesifik dan tidak akan dipakai berulang (karakter "yang diceritakan", bukan karakter utama channel) — itu Tipe B, caranya beda dan lebih ringan, lihat bagian **A2** di `06_PROMPT_LIBRARY.md`, bukan kit ini.
>
> Perlu diingat juga: Voice/gaya bicara channel secara umum sudah ada tempatnya sendiri di bagian **3. Persona & Voice Channel** pada Channel Brief — itu WAJIB diisi untuk semua channel bahkan tanpa elemen visual sama sekali. Kit ini fokus ke elemen yang punya WUJUD visual yang perlu dikonsistenkan — karakter, dan juga latar/palet/props kalau relevan untuk channel ini.

---

## Sebelum mulai: elemen ini cuma dipakai 1 channel, atau lintas-channel?

Defaultnya, 1 elemen (karakter, latar, dst) dianggap milik 1 channel — hasilnya disimpan di `channel-[nama-channel]/konsistensi-visual/[nama-elemen]/`. **Tapi kalau elemen ini sengaja dirancang untuk muncul di lebih dari 1 channel** (misal karakter yang sama nongol sebagai cameo/crossover di channel lain, atau latar yang dipakai bersama), JANGAN disalin manual ke tiap channel — itu bikin beberapa salinan yang gampang divergen begitu salah satu diedit tanpa yang lain ikut diupdate.

**Kalau elemen ini lintas-channel:**
1. Simpan di folder mandiri: `konsistensi-lintas-channel/[nama-elemen]/` (bukan di dalam folder 1 channel tertentu)
2. Di Channel Brief tiap channel yang memakai elemen ini, bagian terkait (4. Konsistensi Visual) cukup diisi rujukan ke lokasi ini — jangan copy isinya
3. Kalau elemen ini perlu tampil beda gaya visual di channel yang berbeda (misal karakter digambar ulang gaya lain), itu dicatat sebagai override di level **Model Konten Brief** channel terkait (`assets/` folder model konten itu) — bukan mengubah Bank Konsistensi Visual aslinya
4. Kalau ada perubahan pada elemen ini, cukup update 1 folder `konsistensi-lintas-channel/[nama-elemen]/` — otomatis berlaku untuk semua channel yang merujuknya, catat perubahan di Log Keputusan file bank konsistensi itu sendiri

**Kalau elemen ini cuma untuk 1 channel** (kasus paling umum) — lanjut seperti biasa, hasilnya disimpan langsung di `channel-[nama-channel]/konsistensi-visual/`, tidak perlu folder terpisah.

---

## Kenapa elemen visual sering "nggak konsisten" — dan bagaimana ini dijawab

Masalah yang sering dialami biasanya berasal dari akar yang sama: **elemen dideskripsikan ulang dengan kata-kata setiap kali generate, tanpa referensi yang benar-benar dikunci**. Kata-kata itu ambigu — AI menginterpretasikan ulang deskripsi visual untuk gambar atau video deskripsi yang sama dengan cara sedikit beda tiap kali, apalagi kalau deskripsinya nggak lengkap/detail.

Kit ini menjawab beberapa lapis konsistensi secara terpisah, karena solusinya beda-beda:

| Yang buyar | Kenapa | Cara menjawabnya |
|---|---|---|
| **Wajah/fisik/wujud** | Deskripsi teks terlalu longgar untuk generate gambar secara konsisten, serta video melalui tools eksternal | Bangun deskripsi visual super detail + file gambar referensi yang WAJIB disimpan permanen di repo dan dipakai ulang tiap generate |
| **Kepribadian/gaya bicara** (khusus karakter) | Nggak ada "aturan bicara" eksplisit, AI menebak dari konteks tiap kali | Bangun Voice Profile: pola bicara, kosakata khas, hal yang TIDAK akan dikatakan karakter ini — saling rujuk dengan Persona & Voice di Channel Brief |
| **Gaya visual/art style** | Istilah gaya visual (misal "anime style") itu luas dan hasilnya beda-beda | Kunci referensi gaya secara spesifik + simpan sample output yang "disetujui" sebagai acuan tambahan di folder referensi yang sama |
| **Latar/lingkungan** | Sama seperti wajah — deskripsi teks longgar, setting bisa "bergeser" tiap generate | Sama pendekatannya seperti karakter: deskripsi detail + gambar referensi |
| **Props/objek berulang** | Detail kecil (bentuk, warna spesifik) gampang hilang di deskripsi teks | Gambar referensi khusus objek itu, terutama kalau detailnya penting untuk pengenalan penonton |

---

## Tahap 1: Bangun Profil Elemen (Diskusi)

Jalankan di sesi lmarena Agent yang sama dengan repo, mode diskusi dulu (proses ini WAJIB berupa diskusi bolak-balik, bukan langsung ditulis ke file di percobaan pertama):

```
Peran kamu: Character & Visual Consistency Development Partner untuk konten
kreator.

Sebelum mulai: baca channel-[nama-channel]/channel-brief.md dari repo ini
untuk konteks niche, tone, target penonton, dan Persona & Voice channel.

Elemen yang mau dibangun: [KARAKTER / LATAR / PALET & GAYA RENDER / PROPS —
sebutkan yang mana]

Ide awal (boleh sangat mentah):
"[TULIS APAPUN YANG ADA DI KEPALA SOAL ELEMEN INI]"

Gali lewat diskusi (3-5 pertanyaan per giliran) sampai bisa merumuskan
jawaban LENGKAP dan SPESIFIK (bukan umum). Sesuaikan poin gali berikut
dengan jenis elemennya:

UNTUK KARAKTER:
1. FISIK — detail yang cukup presisi untuk dipakai ulang sebagai prompt
   generate gambar secara konsisten, serta menjadi acuan untuk video yang dibuat melalui tools eksternal:
   - Usia, bentuk wajah, warna & gaya rambut, warna mata, tinggi/postur
   - Ciri khas yang membedakan dari karakter generik (bekas luka, aksesoris
     tetap, gaya pakaian khas, dsb)
   - Ekspresi/pose default yang sering muncul
2. KEPRIBADIAN:
   - 3-5 sifat inti (bukan generik seperti "baik", tapi spesifik dan bisa
     kontradiktif/kompleks supaya terasa nyata)
   - Motivasi/apa yang dia inginkan dalam konteks channel ini
   - Kelemahan/hal yang bikin dia "manusiawi", bukan sempurna
3. VOICE / GAYA BICARA — paling penting untuk konsistensi naskah:
   - Formal/santai, cepat/lambat, banyak bicara/pendiam
   - Kosakata atau frasa khas yang sering dia pakai
   - Hal yang TIDAK PERNAH dia katakan/lakukan (batasan karakter, supaya
     nggak "OOC"/out of character)
   - Kalau relevan: aksen, logat, bahasa campuran yang dia pakai

UNTUK LATAR/LINGKUNGAN:
1. Deskripsi detail tempat (ruangan/lokasi/dunia) — ukuran, pencahayaan,
   elemen dekorasi khas, suasana
2. Ciri khas yang membedakan dari latar generik sejenis
3. Variasi yang boleh ada (misal siang/malam, musim) vs yang harus tetap
   sama setiap kali

UNTUK PALET WARNA & GAYA RENDER (kalau belum cukup terjawab di Channel
Brief bagian 5):
1. Palet warna spesifik (bukan cuma "warna cerah", tapi kode warna atau
   deskripsi presisi)
2. Gaya render/art style spesifik (bukan "anime style" saja, tapi misal
   "gaya shonen era 2000an dengan garis tebal dan warna flat")
3. Referensi pembanding kalau ada (boleh sebut nama karya lain sebagai
   ACUAN GAYA, bukan untuk ditiru)

UNTUK PROPS/OBJEK BERULANG:
1. Deskripsi detail objek — bentuk, warna, ukuran, material
2. Konteks pemakaian (selalu dipegang siapa, muncul di adegan seperti apa)

Setiap beberapa putaran kasih ringkasan checkpoint. Setelah dikonfirmasi
"cukup, tulis draftnya", rangkum jadi:

# Bank Konsistensi Visual — [Nama Elemen]

## Jenis Elemen
[Karakter / Latar / Palet & Gaya Render / Props]

## Deskripsi (Prompt-Ready)
[deskripsi detail siap dipakai sebagai prompt generate gambar, dalam 1
paragraf padat + poin-poin ciri khas]

## Kepribadian (khusus kalau elemen ini karakter)
[sifat inti, motivasi, kelemahan]

## Voice Profile (khusus kalau elemen ini karakter)
[gaya bicara + daftar eksplisit hal yang tidak akan dikatakan/dilakukan —
cantumkan juga rujukan silang: "lihat juga Persona & Voice Channel di
channel-brief.md bagian 3"]

## Gaya Visual
[istilah gaya spesifik + referensi]

## Prompt Master (Reusable)
[SATU prompt deskripsi visual yang dipadatkan, siap dipakai sebagai
starting point yang konsisten setiap generate]

Setelah draft ini dikonfirmasi final, tulis ke
channel-[nama-channel]/konsistensi-visual/[nama-elemen]/bank-konsistensi.md
(atau konsistensi-lintas-channel/[nama-elemen]/ kalau lintas-channel),
commit, push, siapkan PR untuk direview sebelum merge ke main.
```

---

## Tahap 2: Kunci Referensi Visual (Generate & Simpan ke Repo)

Deskripsi teks saja, sebagus apapun, masih longgar untuk generate visual berulang. Setelah Tahap 1 selesai dan di-merge:

**Tentukan dulu tipe reference pack elemen ini** — bentuk acuan yang tepat berbeda per jenis elemen, jadi `acuan-utama.png` TIDAK wajib untuk semua:

| Tipe elemen | Bentuk acuan wajib | Tambahan yang berguna |
|---|---|---|
| **Karakter** (Tipe A) | `acuan-utama.png` — kondisi netral/default | `reference-sheet.png` (turnaround, ekspresi), `tambahan-[keterangan].png` |
| **Props/objek berulang** | `acuan-utama.png` | Beberapa sudut kalau bentuknya rumit |
| **Latar/lingkungan** | Minimal 2-3 gambar sudut/kondisi berbeda (`sudut-[keterangan].png`) — bukan satu gambar tunggal, karena latar memang berubah menurut waktu/cuaca/posisi kamera | Denah/peta sederhana kalau ruangnya kompleks |
| **Palet warna** | `palet.png` (swatch) + daftar kode warna hex di `bank-konsistensi.md` | Contoh penerapan pada 1-2 adegan |
| **Gaya render** | `style-sheet.png` — beberapa contoh yang mewakili gaya, plus **contoh negatif** (`contoh-negatif-[keterangan].png`) yang menunjukkan gaya yang harus dihindari | Kata kunci prompt yang terbukti menghasilkan gaya itu |
| **Elemen abstrak** (mood, atmosfer) | Deskripsi terstruktur + contoh positif/negatif; boleh tanpa acuan tunggal | Referensi eksternal sebagai arahan gaya (catat di `SUMBER.md`, jangan direproduksi) |

Kalau elemen ini tidak cocok dengan baris manapun, tetapkan tipe reference pack-nya secara eksplisit di `bank-konsistensi.md` beserta alasannya — jangan memaksakan `acuan-utama.png` hanya supaya seragam.

1. Generate gambar dari **Prompt Master** yang sama, pakai kemampuan generate gambar agent — hasilnya WAJIB disimpan sebagai file asli di folder `referensi/` elemen ini, bukan cuma ditampilkan di chat.
2. Simpan acuan wajib sesuai tipe reference pack di tabel atas. Untuk tipe yang memakai **acuan utama** (`acuan-utama.png`): gambar tunggal kondisi paling netral/default, dipakai kalau tidak ada kebutuhan spesifik.
3. Kalau elemen ini butuh variasi sudut pandang atau keadaan yang jauh beda dari acuan utama (misal karakter perlu ekspresi marah selain netral, atau latar perlu terlihat dari beberapa sisi) — buat juga **reference sheet** (`reference-sheet.png`): 1 file grid berisi beberapa sudut/keadaan sekaligus (teknik "character turnaround sheet"). Ini TIDAK menggantikan acuan utama, melainkan tambahan.
4. Kalau ada kebutuhan situasional lain (misal 1 outfit spesifik yang cuma dipakai 1 model konten), simpan sebagai file tambahan dengan nama yang jelas (`tambahan-[keterangan].png`).
5. **Mulai sekarang, setiap kali generate gambar terkait elemen ini lewat agent, agent WAJIB menyertakan file referensi yang relevan** (bisa gabung beberapa sekaligus — acuan utama + reference sheet, sampai 10 gambar referensi dalam 1 kali generate) — tidak perlu diminta manual setiap kali. Untuk video (agent belum bisa generate video langsung, lihat `05_CONTENT_PRODUCTION_PIPELINE.md` Tahap 5) — file-file referensi ini yang sama juga dipakai sebagai acuan visual di tools eksternal (Veo/Dreamina/dst).
6. Sample output produksi yang nanti ternyata dianggap sudah pas gayanya dan layak jadi acuan tambahan — simpan juga ke folder `referensi/` yang sama, bukan kategori terpisah.

---

## Tahap 3: Simpan & Kaitkan ke Channel Brief

1. **Kalau elemen ini untuk 1 channel saja:** hasil Tahap 1 & 2 sudah tersimpan di `channel-[nama-channel]/konsistensi-visual/[nama-elemen]/`. Update bagian **4. Konsistensi Visual** di `channel-brief.md` channel terkait — cukup rujukan ke lokasi ini, jangan copy isinya.
2. **Kalau elemen ini lintas-channel:** hasil tersimpan di `konsistensi-lintas-channel/[nama-elemen]/`, dan tiap Channel Brief yang memakainya cukup tulis rujukan (lihat bagian "Sebelum mulai" di atas).
3. Kalau elemen ini karakter, pastikan bagian Voice Profile-nya saling merujuk dengan Persona & Voice di Channel Brief (bagian 3) — supaya keterkaitan gaya bicara ↔ karakter tetap terlihat meski dokumennya terpisah.
4. Setelah ini dikunci, setiap prompt produksi (naskah, generate gambar lewat agent, atau generate video lewat tools eksternal) untuk elemen ini WAJIB menyertakan Bank Konsistensi Visual-nya — lihat `05_CONTENT_PRODUCTION_PIPELINE.md` dan `06_PROMPT_LIBRARY.md`.
5. **Tetapkan status `Reference-Ready`** di `bank-konsistensi.md` elemen ini — hanya boleh setelah acuan wajib sesuai tipe reference pack-nya benar-benar ADA sebagai file di `referensi/`, bukan sekadar direncanakan. Status ini yang dipakai Channel Brief untuk naik ke `Operational`; kalau ada elemen wajib yang belum `Reference-Ready`, Channel Brief-nya belum boleh dipakai produksi.

---

## Kapan boleh mengubah Bank Konsistensi Visual yang sudah dikunci

Elemen ini boleh berkembang — itu wajar dan kadang bagus untuk storytelling (karakter yang matang, latar yang direnovasi dalam cerita, dst). Tapi bedanya dengan "nggak konsisten" adalah: perubahan ini **sadar dan tercatat**, bukan kebetulan karena AI melenceng. Kalau ada perubahan:

1. Diskusikan dulu apakah ini pengembangan yang disengaja atau cuma AI "melenceng" — bisa pakai perintah "cek konsistensi" (lihat `00_CARA_PAKAI_SISTEM.md`) untuk membantu memastikan.
2. Kalau disengaja → update `bank-konsistensi.md` yang relevan (di folder channel kalau 1-channel, atau di `konsistensi-lintas-channel/` kalau lintas-channel), catat juga di Log Keputusan yang relevan dengan tanggal & alasan. Bank Konsistensi Visual termasuk kategori Besar — perubahan ini WAJIB direview isi lengkapnya sebelum merge.
3. Kalau AI melenceng tanpa alasan jelas → itu tanda Prompt Master/referensi visual belum cukup kuat, perkuat detailnya (tambah reference sheet kalau perlu), bukan biarkan mengambang.
4. Kalau elemen ini lintas-channel dan perubahan itu HANYA berlaku untuk 1 channel tertentu (bukan semua channel yang memakainya) — itu bukan perubahan Bank Konsistensi Visual aslinya, tapi override di level Model Konten Brief channel tersebut (folder `assets/`-nya), supaya channel lain yang memakai elemen yang sama tidak ikut terdampak.
