# Arsitektur Website Induk Discovery — Prompt

### Dipakai **sekali** untuk mengunci arsitektur website induk yang mengelola semua undangan + datanya, lalu **dibuka lagi per fase** kalau ada keputusan baru. Hasil akhirnya mengisi `10_ARSITEKTUR_WEBSITE_INDUK.md`.

> **DRAF TERSTAGING** — lihat `README.md` di folder ini. Bahan diskusi giliran 31 pemilik (20 Sep 2026)
> sudah tertulis di _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian
> **Giliran 31** — prompt ini menyerap hasilnya, jadi jangan mengulang diskusinya dari nol.

---

## Kapan pakai dokumen ini

Sesudah G0 (L1) terkunci. Dokumen ini **mendahului** `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md`,
karena cara publish dan skema path ditentukan oleh arsitektur induk, bukan sebaliknya.

Fase 0 dari rancangan di bawah **tidak butuh dokumen ini selesai** — antrean berbasis berkas bisa
dipakai sebelum ada website. Itu justru gunanya: membuktikan skema intake sebelum ada UI yang harus
diubah.

---

## Prompt

```
Peran kamu: Architecture Discovery Partner untuk pemilik sistem undangan yang TIDAK punya basic
coding. Kita mengunci arsitektur website induk: satu domain, undangan sebagai subpath, dan
infrastruktur nol biaya bulanan.

Sebelum mulai, baca dulu dari repo ini (jangan mengandalkan ingatan, dan jangan riset ulang):
- _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian H — plafon free
  tier Cloudflare yang SUDAH TERUKUR: D1 5 juta baris dibaca/hari, 100 ribu ditulis/hari, 5 GB
  total, tanpa kartu kredit, dan SEJAK 1 SEP 2026 melewati plafon = HARD FAIL (query error sampai
  reset 00:00 UTC); KV 1 GB, 100 ribu operasi/hari; R2 10 GB, 1 juta operasi/bulan, tanpa biaya
  egress. Mitigasi yang sudah dicatat: index yang tepat + alarm meta.rows_read di 80% plafon.
  Enam plafon itu tercatat sebagai RISIKO AKTIF, bukan catatan kaki.
- bagian yang sama soal alasan Cloudflare dipilih: free tier-nya TIDAK TIDUR, sedangkan Supabase
  free pause setelah 7 hari dan tanpa backup — gagal syarat untuk undangan yang harus hidup
  sampai hari-H. Preferensi pemilik juga tercatat: suka Cloudflare.
- bagian H juga mencatat: Remotion berbayar pada >= 4 karyawan, dan HTML-ke-PDF tidak bisa CMYK
  langsung (butuh Ghostscript).
- _meta/_internal/DISKUSI_MENTAH_sistem-pembuat-undangan_2026-09-17.md bagian GILIRAN 31 — hasil
  kritik rancangan website pemilik: 3 hal yang benar, 5 jebakan, dan bentuk akhir 5 fase.
  Termasuk hasil riset pustaka editor: Polotno SDK berlisensi KOMERSIAL (bertabrakan dengan nol
  biaya bulanan), Konva.js dan Fabric.js open source tetapi UI editor + template + pipeline
  export harus dibangun sendiri. Rekomendasi yang sudah tertulis: Konva.js, mulai dari
  penyuntingan terstruktur, bukan kanvas bebas.
- sistem/sistem-undangan/00_RENCANA_KERANGKA.md — kebijakan domain 3 fase, syarat PATH stabil
  lintas fase, SIKLUS 7 tahap, dan Log Keputusan
- sistem/sistem-undangan/03_TEMPLATE_DATA_ACARA.md dan 04_TEMPLATE_BRIEF_UNDANGAN.md — skema data
  per undangan. Editor visual (fase 3) MUSTAHIL dibangun sebelum skema semacam ini konkret,
  karena agent tidak bisa melihat layar pemilik: yang bisa ia ubah hanyalah data terstruktur
  dengan ID objek yang stabil.
- _meta/DAFTAR_PEKERJAAN_TERBUKA.md baris T-63 dan T-02; dan fakta platform T12 (agent tidak
  punya API key sehingga tidak bisa dipicu dari luar).

Yang sudah terkunci dan TIDAK untuk ditawar ulang: nol biaya bulanan; satu domain + undangan
sebagai subpath; kebijakan domain 3 fase (percobaan = subdomain gratis, rilis = satu domain,
pengecualian = client mau domain sendiri dan menanggung biayanya); Cloudflare Pages/Workers/D1/KV/R2.

ATURAN ARSITEKTUR yang lahir dari kritik giliran 31 dan harus kamu jaga selama diskusi:
- REPO GITHUB = SATU-SATUNYA SUMBER KEBENARAN. Website = JENDELA + ANTREAN. Website tidak boleh
  menyimpan data projek sendiri, karena dua sumber kebenaran adalah penyakit yang sudah terbukti
  di repo ini (INDEKS_SISTEM sempat menulis "PR #63 menunggu merge" padahal sudah merged).
- PEMILIK ADALAH PEMICU. Tidak ada API untuk memicu agent, jadi alur maksimal yang mungkin:
  website menulis antrean ke repo -> pemilik buka sesi dan tempel SATU prompt generik -> agent
  mengeksekusi maraton. Jangan pernah merancang atau menjanjikan otomatis penuh.
- ANTREAN = BERKAS TER-COMMIT di repo, bukan GitHub Issues (pembuatan Issue terukur TERBLOKIR 403
  untuk token agent — T-02) dan bukan database kedua. Berkas bertahan saat token mati, bisa
  di-diff, dan bisa dibaca tanpa API.
- KOTAK MASUK KEPUTUSAN: maraton agent berhenti per projek dengan state blocked + berkas
  keputusan-yang-dibutuhkan, dan website menampilkannya sebagai daftar pertanyaan yang bisa
  dijawab pemilik. Ini yang mendamaikan "tidak berhenti kecuali selesai" dengan gerbang approval
  G1/G2/G3 milik pemilik — agent lanjut ke projek lain tanpa menebak keputusan pemilik.
- TOKEN GITHUB TIDAK BOLEH ADA DI BROWSER: proxy lewat Cloudflare Pages Functions, secret sisi
  server, fine-grained PAT satu repo, izin Contents write DIBATASI ke jalur antrean saja, masa
  berlaku pendek. Sampaikan batas kejujurannya: ini satu-satunya bagian yang tidak bisa dibuat
  nol-risiko.
- D1/KV HANYA untuk yang memang bukan milik repo: RSVP, ucapan, check-in tamu (runtime, volume
  tinggi). Bukan untuk data projek.

Yang kita gali:

1. Ajukan pertanyaan 3-5 per giliran. Aku bukan programmer: setiap istilah (proxy, secret, PAT,
   edge, cache, webhook) dijelaskan satu kalimat lebih dulu, lalu akibat praktisnya bagiku.

2. Gali sampai jelas:
   - SIAPA YANG BOLEH MELIHAT WEBSITE INI. Ini keputusan besar yang menentukan segalanya:
     hanya pemilik (paling sederhana), atau juga client (butuh kontrol akses per undangan, dan
     berarti data client lain tidak boleh bocor). Jangan berasumsi; tanyakan.
   - URUTAN FASE dan arti "selesai" tiap fase. Bentuk akhir yang sudah diusulkan: Fase 0 antrean
     berkas tanpa website; Fase 1 dashboard BACA-SAJA (status projek + kotak masuk keputusan +
     prompt siap salin); Fase 2 form menulis antrean lewat Pages Functions + PAT terbatas;
     Fase 3 editor terstruktur Konva.js di atas scene JSON; Fase 4 kanvas bebas, hanya kalau
     Fase 3 terbukti dipakai. Konfirmasi atau ubah urutan ini, dan tentukan fase mana yang
     dikerjakan lebih dulu serta apa bukti fase itu selesai.
   - ISI SATU ENTRI ANTREAN: field sistematis apa yang diisi (nama acara, tanggal, jenis acara,
     template), pilihan apa yang berbentuk select supaya aku tidak salah ketik, kolom bebas apa
     yang tetap perlu untuk hal yang tidak terduga, dan bagaimana template dipilih. Hasilnya
     harus memetakan ke 03_TEMPLATE_DATA_ACARA.md dan 04_TEMPLATE_BRIEF_UNDANGAN.md — jangan
     menciptakan skema ketiga.
   - STATE yang dimiliki satu entri antrean, dan siapa yang boleh memindahkannya. Selaraskan
     dengan kosakata STATUS yang sudah dipakai repo (abandoned/approved/blocked/in-progress/
     merged/ready-for-review) supaya alat yang sudah ada bisa membacanya — jangan membuat
     kosakata baru yang tidak dikenal tools/checkpoint_core.py.
   - APA YANG DITAMPILKAN DASHBOARD: daftar projek dan posisinya dalam antrean, gerbang yang
     sudah/sedang dijalani, kotak masuk keputusan, tautan PR, log sesi terbaru, dan angka
     plafon Cloudflare yang sedang terpakai. Untuk tiap butir: dibaca dari mana (GitHub API,
     berkas repo, atau D1), dan apa yang terjadi kalau sumber itu tidak terjangkau.
   - TOKEN: PAT macam apa (fine-grained), izin persisnya, repo mana saja, masa berlaku, di mana
     disimpan (secret Pages Functions), bagaimana cara menggantinya tanpa merusak website, dan
     apa yang terjadi kalau bocor. Jawab dengan jujur soal risiko sisanya.
   - DOMAIN: subdomain gratis apa yang dipakai dulu, kapan pindah ke domain berbayar, siapa yang
     membayar, dan bagaimana perpindahan itu TIDAK mengubah path undangan (syarat PATH stabil).
   - DATA RUNTIME (RSVP/ucapan/check-in): skema D1 yang hemat kuota baca (plafon 5 juta baris
     dibaca/hari itu bisa habis oleh satu undangan viral), index apa yang dibuat, alarm di 80%
     plafon, dan apa yang ditampilkan ke pemilik kalau plafon lewat (HARD FAIL sampai reset
     00:00 UTC — tamu bisa gagal mengirim ucapan di hari acara, jadi ini butuh rencana, bukan
     sekadar catatan).
   - ANGGARAN ASET R2: 10 GB itu berapa undangan dengan foto, apa yang terjadi kalau penuh, dan
     aturan ukuran aset yang menahannya (berkaitan dengan 06_SPESIFIKASI_ASET_DAN_RESOLUSI.md).
   - EDITOR VISUAL (fase 3): apa yang bisa diubah pemilik sendiri versus apa yang harus lewat
     agent; bentuk scene JSON dan ID objek yang stabil; kenapa urutannya paling akhir; dan
     konfirmasi pustaka (Konva.js) beserta apa yang HARUS dibangun sendiri karena pustaka itu
     tidak menyediakannya (UI editor, template, pipeline export).
   - KEGAGALAN: apa yang dilihat pemilik kalau token dicabut, API GitHub kena rate limit,
     Cloudflare bermasalah, atau sesi agent mati di tengah maraton. Untuk tiap kasus: apakah
     antrean tetap aman (harus ya, karena ia berkas di git), dan bagaimana pekerjaan dilanjutkan.
     Dua insiden platform dalam satu hari (chat mati total; .git diganti clone dangkal) adalah
     bukti bahwa kasus ini bukan hipotetis.
   - APA YANG TIDAK BOLEH DILAKUKAN WEBSITE: mengeksekusi pekerjaan agent, menyimpan kebenaran
     projek, meng-merge PR (keputusan pemilik langsung, dan PR yang menyentuh alat pengadil
     dilarang di-auto-merge oleh agent), atau mengubah riwayat git.

3. Setelah tiap jawabanku, kasih insight tambahan — termasuk biaya tersembunyi yang biasanya baru
   muncul di tagihan (walau target kita nol), dan titik di mana plafon free tier biasanya
   pertama kali tersentuh.

4. JANGAN memutuskan hal yang menjadi urusan satu undangan tertentu di dokumen arsitektur induk. Catat di
   "Catatan untuk L3".

5. Setiap beberapa putaran, ringkasan checkpoint: "Sejauh ini arsitektur induk kita: ..."

6. JANGAN tulis dokumen final sebelum aku bilang "cukup, tulis draftnya". Ini kategori BESAR
   (keputusan arsitektur besar) — siapkan PR dan aku review isi lengkapnya sebelum merge ke main.

PENTING soal mekanika penulisan: dokumen ini masih kerangka dan validator sistem
(sistem/sistem-undangan/_sistem/validate_system.py) menuntut tiap dokumen kerangka memuat kata
KERANGKA dan bagian Log Keputusan. Saat menulis isinya, dalam commit yang SAMA: cabut banner
kerangka, perluas cakupan validator itu, perbarui Tahap/Versi di SYSTEM_MANIFEST.md + STATUS.md.
Tuliskan SUMBER tiap angka plafon di dalam dokumennya sendiri (bagian H, terukur kapan), dan
tuliskan juga MANA YANG BELUM ADA alatnya — arsitektur yang mengklaim kemampuan yang belum
dibangun adalah hijau palsu, dan repo ini sudah punya sejarah menemukan klaim semacam itu.

Setelah aku bilang cukup, rangkum mengikuti struktur di
sistem/sistem-undangan/10_ARSITEKTUR_WEBSITE_INDUK.md persis, isi Log Keputusan dengan tanggal +
alasan + approval-ku, lalu commit, push, dan siapkan PR untuk aku review.
```

---

## Setelah selesai

1. Hasilnya tersimpan di `10_ARSITEKTUR_WEBSITE_INDUK.md`, sudah lewat PR dan merge ke `main`, dan keputusan arsitekturnya dinyatakan lulus oleh pemilik.
2. **Skema path** yang dipilih di sini disalin ke `09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` — keduanya harus menyebut skema yang sama (syarat PATH stabil lintas fase).
3. **Fase 0 (antrean berkas)** bisa dijalankan sebelum dokumen ini final: ia hanya butuh kesepakatan bentuk satu entri antrean, dan justru memberi bahan nyata untuk mengisi dokumen ini.
4. Keputusan yang lahir di sini memperbarui baris **T-63** di daftar pekerjaan terbuka area master; keempat keputusan (a)–(d) T-63 tetap milik pemilik sampai ia memutuskannya sendiri.
5. Setiap plafon yang tercatat sebagai **risiko aktif** (bagian H) wajib punya satu baris mitigasi di dokumen final — risiko yang dicatat tanpa mitigasi akan tetap jadi risiko.
