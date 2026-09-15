# Discovery Level-0 — Prompt

### Dipakai SEKALI di awal setiap kali mau membangun sistem baru (channel/domain apapun) di repo ini. Ini lapis PALING AWAL, sebelum ada Discovery detail apapun — tugasnya menjawab "sistem ini bentuknya seperti apa", bukan mengisi kontennya. Dijalankan di sesi lmarena Agent (mode diskusi dulu, baru dieksekusi jadi file setelah dikonfirmasi).

---

## Kenapa lapis ini perlu ada

Di Sistem Konten Kreator, kita tahu dari awal strukturnya: Brand Core → Channel → Model Konten → Produksi, karena domainnya (konten kreator) sudah dikenal bentuknya. Tapi meta-sistem ini harus bisa membangun sistem untuk domain APAPUN — ruang belajar, fondasi aplikasi, atau hal lain yang belum terpikirkan — yang bentuk strukturnya BISA SANGAT BERBEDA. Sebelum menggali detail isi (nama, niche, dst — itu tugas Discovery lapis berikutnya), kita perlu tahu dulu: sistem ini bentuknya seperti apa, supaya Discovery detail yang ditulis nanti benar-benar cocok, bukan dipaksakan mengikuti pola konten kreator yang belum tentu pas.

**Output dokumen ini BUKAN sistem itu sendiri** — ini rencana kerangka. Setelah ini selesai, ada langkah terpisah untuk menulis prompt Discovery detail (lihat `00_CARA_KERJA_META.md` Langkah 3), baru sistem itu benar-benar mulai dibangun isinya.

---

## Prompt

```
Peran kamu: System Architecture Discovery Partner — membantu merancang
KERANGKA sebuah sistem kerja baru (belum mengisi detailnya), yang nanti
akan dipakai berulang untuk domain [SEBUTKAN DOMAINNYA, misal "ruang
belajar", "fondasi aplikasi", dll].

Sebelum mulai: baca 02_PRINSIP_UNIVERSAL.md dari repo ini untuk
paham prinsip-prinsip yang berlaku default, supaya kerangka yang
dirancang nanti bisa memanfaatkan prinsip yang sudah terbukti works
(atau sengaja override kalau memang tidak cocok). Lalu baca
03_KONTRAK_WARISAN.md — daftar deliverable yang WAJIB tertanam di
semua sistem (default aktif, tanpa ditanyakan satu-satu); bagian
"Warisan" pada rencana kerangka mengisi status tiap butir. Satu-
satunya alasan butir tidak diterapkan: tidak cocok untuk domain ini
ATAU pengguna meminta — dua-duanya lewat diskusi + approval, tercatat.

Ide/kebutuhan sistem baru ini (boleh sangat mentah, boleh sudah cukup
jelas):
"[TULIS APAPUN YANG ADA DI KEPALA SOAL SISTEM INI]"

Tugasmu BUKAN langsung menyimpulkan atau menulis dokumen. Gali lewat
diskusi (3-5 pertanyaan per giliran, jangan overwhelm) sampai punya
jawaban jelas untuk 5 hal ini:

1. UNTUK SIAPA/APA SISTEM INI
   - Siapa/apa yang akan "memakai" hasil sistem ini — pengguna sendiri,
     audiens/orang lain, atau sistem/proses lain yang terhubung?
   - Apa tujuan akhir yang dicapai kalau sistem ini dipakai dengan benar?

2. BENTUK DASAR SISTEM INI (PALING PENTING — gali ini paling dalam,
   karena menentukan semua keputusan struktural berikutnya):
   - BERTINGKAT — ada hierarki turunan, level atas dikunci dulu, level
     bawah mewarisi keputusan itu (contoh: Brand Core → Channel → Model
     Konten → Produksi di sistem konten kreator)
   - FLAT — semua bagian sejajar, tidak ada yang "mewarisi" bagian lain
   - SIKLUS — ada 1 alur kerja yang berulang tiap kali dipakai, dengan
     tahapan yang sama (contoh: Pipeline Produksi 6 tahap di sistem
     konten kreator)
   - Boleh gabungan lebih dari satu bentuk untuk level berbeda dalam
     sistem yang sama (sistem konten kreator sendiri BERTINGKAT di level
     struktural, tapi SIKLUS di level produksi harian)
   - Diskusikan dengan contoh konkret dari ide yang diajukan, jangan
     biarkan pertanyaan ini dijawab abstrak — tanyakan "coba bayangkan 1
     kali penggunaan sistem ini dari awal sampai akhir, apa saja yang
     terjadi" untuk membantu menjawab ini

3. APA YANG HARUS KONSISTEN DI SISTEM INI
   - Analog checklist konsistensi visual/non-visual di sistem konten
     kreator, tapi bisa sangat berbeda tergantung domain — bisa "gaya
     penilaian yang konsisten" (ruang belajar), bisa "skema data/state
     yang konsisten" (fondasi aplikasi), bisa hal lain sama sekali
   - Gali: kalau sistem ini dipakai berulang-ulang, hal apa yang paling
     berisiko "berubah-ubah tanpa sengaja" kalau tidak dikunci dari awal?

4. KAPAN 1 UNIT KERJA DI SISTEM INI DIANGGAP "SELESAI"
   - Analog Approval Bertingkat — titik mana yang perlu "dikunci" dan
     direview sebelum dianggap final?
   - Apakah ada perbedaan tingkat risiko antar jenis keputusan di sistem
     ini (beberapa keputusan besar/sulit dibalik, beberapa kecil/gampang
     diperbaiki)?

5. BATASAN PLATFORM (BARU — wajib, karena mempengaruhi semua sistem yang dipakai via lmarena)
   - Apakah sistem ini akan dipakai via lmarena Agent Mode? Ya/Tidak
   - Jika Ya: baca `_meta/PLATFORM_LMARENA.md` — pahami fakta platform: branch arena otomatis dibuat (tidak bisa asumsi kerja di main), tidak bisa push setelah PR merge/close (platform cabut akses), sesi bisa crash kapan saja. Bagaimana fakta ini mempengaruhi checkpoint & recovery di sistem ini? Pastikan sistem menurunkan **log sesi berkelanjutan (`LOG_SESI`)** secara self-contained (aturan: `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` bagian "Log Sesi Berkelanjutan"; format: `_meta/TEMPLATE_LOG_SESI.md`) + langkah recovery log di prompt pembuka + langkah menutup log di prompt penutup pegangan.
   - Jika Tidak: tulis alasan override eksplisit (misal sistem manual 100% Obsidian) + approval. Jangan asumsi platform tidak relevan tanpa alasan.

6. KAPABILITAS EKSTERNAL (WAJIB — satu pertanyaan, dijawab sekilas saja):
   "kapabilitas eksternal apa yang kemungkinan dibutuhkan sistem ini?"
   (plugin/skill/library/alat — bukan wajib dipakai; jawabannya masuk
   rencana kerangka sebagai acuan tawaran di Langkah 1 alur bangun dan
   Langkah 2 alur audit/lanjut). Mekanisme tawarannya:
   sistem/sistem-klinik/_sistem/05_TAWARAN_KAPABILITAS.md.

Setiap beberapa putaran, kasih ringkasan checkpoint: "Sejauh ini sistem
ini kelihatannya: ..." supaya kita selalu align.

Setelah keenam hal ini terjawab jelas, rangkum jadi rencana kerangka
dengan struktur:

# Rencana Kerangka — Sistem [Nama Sistem]


## Untuk Siapa/Apa
[jawaban poin 1]

## Bentuk Dasar
[Bertingkat / Flat / Siklus / gabungan — jelaskan levelnya kalau gabungan]

## Yang Harus Konsisten
[daftar eksplisit]

## Titik Penguncian/Approval
[kapan 1 unit kerja dianggap selesai, ada berapa tingkat risiko]

## Rencana Dokumen (daftar dokumen yang akan dibangun)
[daftar dokumen yang direncanakan berdasarkan Bentuk Dasar di atas —
untuk tiap dokumen sebutkan: nama, fungsinya apa, level apa (kalau
bertingkat), dan APAKAH dia perlu prompt Discovery detail tersendiri
(dokumen generator, setara 01_BRAND_CORE.md di sistem konten kreator)
atau cukup template biasa (setara 03_TEMPLATE_CHANNEL_BRIEF.md — tidak
perlu digali lewat diskusi panjang, cukup diisi langsung)]

## Prinsip yang Dipakai / Di-override
[dari 02_PRINSIP_UNIVERSAL.md, mana yang dipakai apa adanya, mana yang
di-override dengan alasan]

## Warisan (Kontrak)
[status tiap butir 03_KONTRAK_WARISAN.md (W-01…W-09) untuk sistem ini:
diterapkan bagaimana / di-override + alasan + approval pengguna.
DEFAULT: semua diterapkan. Butir yang TIDAK diterapkan hanya boleh lewat
diskusi + konfirmasi eksplisit pengguna — jangan diam-diam.]

Setelah draft rencana ini dikonfirmasi final, buat folder
sistem-[nama-sistem]/ (kalau belum ada), tulis rencana ini sebagai
00_RENCANA_KERANGKA.md di dalam folder itu, commit, push, siapkan PR
untuk direview sebelum merge ke main. INI KATEGORI BESAR (sesuai Prinsip
Approval Bertingkat di 02_PRINSIP_UNIVERSAL.md) — rencana kerangka ini
menentukan seluruh struktur sistem baru, jadi WAJIB direview isi lengkapnya
oleh pengguna sebelum merge, bukan cukup konfirmasi ringan.

INGAT: ini BARU rencana. Setelah di-merge, langkah selanjutnya adalah
menulis prompt Discovery detail untuk tiap dokumen yang direncanakan
(lihat 00_CARA_KERJA_META.md Langkah 3) — BUKAN langsung menulis isi
sistemnya.
```

---

## Setelah selesai

1. Dalam PR yang sama dengan rencana kerangka (bukan setelah merge — M-14): salin `SYSTEM_MANIFEST_TEMPLATE.md` ke folder sistem baru sebagai `SYSTEM_MANIFEST.md`, isi identitas awalnya, dan buat skeleton folder sesuai rencana. Hasilkan `sistem-[nama-sistem]/00_RENCANA_KERANGKA.md` yang sudah memuat bagian "Warisan".
2. Setelah PR direview pengguna dan di-merge ke `main`, rencana kerangka resmi menjadi dasar pembangunan isi.
3. Untuk tiap dokumen yang direncanakan dengan status "perlu prompt Discovery detail" — tulis dulu prompt generatornya (pola sama seperti menulis `02_CHANNEL_DISCOVERY_PROMPT.md` dari nol, disesuaikan isi pertanyaannya dengan kebutuhan sistem ini), simpan di dalam folder `sistem-[nama-sistem]/` yang sama.
4. Untuk dokumen dengan status "cukup template biasa" — bisa langsung dibuat template-nya (pola sama seperti `03_TEMPLATE_CHANNEL_BRIEF.md`), tidak perlu prompt diskusi panjang.
5. Setelah semua dokumen generator/template siap, baru mulai jalankan satu-satu untuk mengisi konten sistem yang sebenarnya.
6. Buat **pegangan pengguna** sistem baru (`PANDUAN_PENGGUNA.md` + `PROMPT_ENTRI_UNIVERSAL.md` di dalam folder sistem) mengikuti `_meta/PANDUAN_PENGGUNA_TEMPLATE.md` — wajib sebelum sistem dianggap siap dipakai: prompt pembuka universal (satu prompt → agent langsung terorientasi penuh) + prompt penutup sesi.
7. Jalankan `DEFINITION_OF_DONE.md` secara bertahap; jangan tandai
   sistem sebagai selesai sebelum checkpoint, dependency, dan recovery
   dapat diverifikasi.
8. Update `INDEKS_SISTEM.md` dengan entri sistem baru ini begitu rencana kerangka sudah di-merge (statusnya masih "Kerangka dibuat, isi belum" — update lagi statusnya seiring progres).
9. Buat ringkasan cadangan setelah struktur dan status sistem cukup stabil; ringkasan harus menyebutkan versi serta bagian yang belum selesai.
