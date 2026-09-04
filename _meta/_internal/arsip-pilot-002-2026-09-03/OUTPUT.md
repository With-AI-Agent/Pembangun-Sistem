# Catatan Belajar — Protokol Checkpoint & Recovery

- **Status:** `draft`
- **Catatan status:** diturunkan dari `checked` ke `draft` pada tahap Apply; pada tahap Observe (2026-09-03) konten Apply **lulus verifikasi ulang terbatas dengan catatan** dan dipakai secara nyata (lihat `Hasil Tahap Observe`). Status **`checked` final belum diberikan** — menunggu keputusan pengguna. `checked` ≠ `approved` ≠ `released`.
- **Sumber:** `../../fixtures/SUMBER_CHECKPOINT_RECOVERY.md` (snapshot beku dari `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`)
- **URL/lokasi:** repo `With-AI-Agent/Pembangun-Sistem`, commit `e7ce5e5`
- **Tanggal akses:** 2026-09-03
- **Tujuan belajar:** memahami syarat minimum sebuah checkpoint supaya sesi agent yang benar-benar terputus dapat melanjutkan tanpa menebak, dan menerapkannya pada unit pilot ini.

## Pertanyaan Awal

- Apa yang membuat sebuah checkpoint cukup untuk recovery nyata, dan bukan hanya ringkasan yang nyaman dibaca di chat?
- Kondisi apa yang membuat agent wajib berhenti dan bertanya, bukan melanjutkan?

## Ringkasan

`_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` (snapshot `../../fixtures/SUMBER_CHECKPOINT_RECOVERY.md`) adalah protokol internal yang mengatur cara menyimpan progres kerja agar sesi baru dapat melanjutkan pekerjaan tanpa mengandalkan ingatan percakapan. Isinya empat bagian utama: (1) checkpoint didefinisikan sebagai catatan persisten — bukan ringkasan chat — dengan format 12 field dan kosakata status terbatas 6 nilai [b. 12–36]; (2) enam aturan pembuatan checkpoint, dari membaca sumber resmi lebih dulu sampai kewajiban commit + push untuk output yang menjadi dependency tahap berikutnya [b. 39–46]; (3) enam langkah recovery pada sesi baru, dari membaca manifest hingga kewajiban berhenti dan bertanya saat status ambigu [b. 48–55]; dan (4) empat prinsip penanganan konflik tanpa menimpa perubahan secara diam-diam [b. 57–62]. Dua gagasan paling menentukan: syarat "aman untuk sesi berikutnya" bersifat ganda (tersimpan di path resmi **dan** tersedia di branch/remote) [b. 42, 44–45], dan menebak dilarang saat status tidak jelas [b. 55].

## Konsep Inti

_Tingkat kepastian: `fakta sumber` = tertulis eksplisit di snapshot; `inferensi` = sintesis/penarikan makna oleh agent (diberi kode S-); `terbuka` = belum dapat dipastikan dari sumber._

| Konsep | Penjelasan | Rujukan sumber | Tingkat kepastian |
|---|---|---|---|
| C1. Checkpoint = catatan persisten | Checkpoint adalah catatan persisten yang memungkinkan sesi berikutnya melanjutkan tanpa ingatan percakapan; bukan ringkasan di chat | snapshot b. 12–14 (E-D1, E-I1) | fakta sumber |
| C2. Format checkpoint 12 field | Kolom dalam template (dikoreksi di Verify: kewajiban di sumber melekat pada pembaruan file status, bukan per kolom): status, tahap terakhir, tahap berikutnya, output resmi, sumber konteks, keputusan, approval, commit, PR, pekerjaan belum tersimpan, risiko, waktu pembaruan | snapshot b. 23–36 (E-D3, E-C1) | fakta sumber |
| C3. Kosakata status terbatas | Status unit hanya boleh salah satu dari: `in-progress`, `blocked`, `ready-for-review`, `approved`, `merged`, `abandoned` | snapshot b. 23 (E-D2) | fakta sumber |
| C4. Kewajiban checkpoint | Wajib untuk setiap unit kerja/tahap besar yang menghasilkan input untuk tahap berikutnya | snapshot b. 16–18 (E-F1) | fakta sumber |
| C5. Enam aturan pembuatan checkpoint | Baca sumber resmi → simpan output ke path → perbarui status → commit + push untuk dependency → larangan klaim "aman" tanpa itu → jelaskan tindak lanjut ke pengguna | snapshot b. 39–46 (E-F2) | fakta sumber |
| C6. Enam langkah recovery sesi baru | Baca manifest → baca status unit → verifikasi output + commit → verifikasi branch + PR → jangan ulang tahap final tanpa alasan → berhenti & tanya jika ambigu | snapshot b. 48–55 (E-F3) | fakta sumber |
| C7. Empat prinsip recovery konflik | Jangan menimpa diam-diam; identifikasi yang bertabrakan; pisahkan tujuan tak berkaitan; approval ulang untuk keputusan Besar | snapshot b. 57–62 (E-F4) | fakta sumber |
| C8. Syarat ganda "aman untuk sesi berikutnya" | Output aman untuk dilanjutkan hanya jika tersimpan di path resmi **dan** tersedia di branch/remote | snapshot b. 42, 44–45 (E-I2) | fakta sumber (dirumuskan ulang) |
| S-1. [Inferensi] Aturan checkpoint adalah produsen artefak yang dikonsumsi recovery | Artefak dari aturan ①–④ (status segar, output di path, checkpoint ter-commit/push) persis menjadi bahan yang diverifikasi langkah recovery ①–④ | dirumuskan dari snapshot b. 41–44 dan b. 50–53; lanjutan X-I2 | inferensi |
| S-2. [Inferensi] "Berhenti dan bertanya" adalah titik akhir fail-closed | Seluruh langkah recovery bermuara ke satu perilaku saat bukti tidak cukup: berhenti, bukan lanjut dengan asumsi; istilah "fail-closed" adalah label agent, sumber hanya berkata "berhenti dan tanyakan pengguna; jangan menebak" | dirumuskan dari snapshot b. 55 | inferensi |

## Hubungan Antar Konsep

- Format checkpoint (C2) adalah **bentuk konkret** dari "catatan persisten" (C1): tanpa format 12 field, persistensi tidak punya bentuk yang bisa diverifikasi. _(fakta sumber: C1 b. 12–14, C2 b. 23–36 — penggabungan ini sendiri adalah sintesis, label S-3)_
- Aturan ③ "perbarui status setelah output tersimpan" (C5, b. 43) **menjaga keakuratan** C2; tanpa itu, status menjadi basi dan langkah recovery ②–③ (C6, b. 51–52) kehilangan bahan verifikasi. _(sintesis S-4, berdasar b. 43 dan 51–52)_
- Syarat ganda (C8) **menjelaskan kenapa aturan ④ dan ⑤ berpasangan**: ④ menetapkan commit + push sebagai syarat untuk output dependency, ⑤ melarang klaim "aman dilanjutkan" tanpa ketersediaan di branch/remote (b. 44–45). _(pembacaan langsung dua aturan yang saling melengkapi; perumusan "berpasangan" adalah sintesis S-5)_
- Recovery sesi baru (C6) **adalah sisi konsumsi** dari aturan checkpoint (C5): langkah ①–④ membaca dan memverifikasi artefak yang diproduksi aturan ①–④. _(sintesis S-1 pada tabel Konsep Inti)_
- Recovery konflik (C7) **aktif saat verifikasi pada langkah ③–④ (C6) menemukan perubahan yang bertabrakan**; keduanya berbagi prinsip yang sama: jangan menimpa secara diam-diam, dan jangan menebak. _(sintesis S-6, berdasar b. 50–55 dan 57–62)_
- "Berhenti dan bertanya" (langkah ⑥, b. 55) **menjadi pagar terakhir** yang menutup semua jalur recovery: apa pun yang tidak dapat dibuktikan tidak boleh dilanjutkan dengan asumsi. _(sintesis S-2 pada tabel Konsep Inti)_

## Hal yang Belum Jelas

_Disusun pada tahap Structure sesuai instruksi pengguna; difinalkan pada tahap Verify (2026-09-03). Hasil tiap butir tercantum di bawah; butir yang tetap terbuka dinyatakan terbuka, bukan ditutup-tutupi._

- **Istilah "keputusan Besar" (Q-O1, b. 62) — TERJAWAB SEBAGIAN lewat rujukan lintas dokumen meta resmi (bukan isi sumber):** sumber tidak mendefinisikannya, tetapi dokumen meta memakai istilah ini secara konsisten untuk keputusan yang sulit dibalik atau menyentuh aturan inti: `01_DISCOVERY_LEVEL_0.md` poin 4 ("beberapa keputusan besar/sulit dibalik, beberapa kecil/gampang diperbaiki"), `02_PRINSIP_UNIVERSAL.md` baris 19 ("keputusan besar dikunci sekali"), dan `ACCEPTANCE_TESTS.md` AT-05 (perubahan aturan inti wajib lewat proposal: masalah, bukti, trade-off, metrik, regression check, rollback). Catatan kejujuran: tidak ada satu definisi kanonik tunggal — jawaban ini adalah sintesis lintas dokumen dan berada di luar bahan belajar unit ini.
- **Kriteria "alasan" yang sah untuk mengulang tahap `approved`/`merged` (Q-O2, b. 54) — TETAP TERBUKA:** tidak ditemukan kriteria di sumber maupun di dokumen meta yang diperiksa (manifest, cara kerja, workflow, quality protocol, acceptance/failure tests). Ini celah nyata protokol — jangan beroperasi seolah kriterianya sudah ada.
- **Interval pengisian "Waktu pembaruan" (Q-O3, b. 36) — TETAP TERBUKA:** tidak ada aturan interval di sumber maupun dokumen terkait; konvensi per-tahap yang dipakai unit ini tetap keputusan lokal, bukan klaim sumber.
- **Ruang lingkup aturan ④ vs ⑤ (S-7, b. 44–45) — TERJAWAB SEBAGIAN lewat pembacaan ketat; tetap berlabel inferensi:** ④ mewajibkan commit + push hanya untuk output yang menjadi dependency tahap berikutnya; ⑤ bersifat umum: klaim "aman dilanjutkan" terlarang untuk setiap output yang belum tersedia di branch/remote. Konvensi unit ini sengaja menerapkan standar lebih kuat dari minimum sumber (semua checkpoint di-commit dan di-push).

## Pertanyaan Uji Pemahaman

_Dihasilkan di tahap Apply (2026-09-03). **Status bagian ini: BELUM diverifikasi** — tidak termasuk cakupan `checked` sebelumnya; wajib diverifikasi ulang sebelum status `checked` final. Jumlah dibatasi 3 pertanyaan sesuai `WORKFLOW.md` (1–3); seluruh area wajib (konsep inti, checkpoint, recovery, konflik, fakta-vs-inferensi) dipetakan eksplisit ke pertanyaan-pertanyaan ini._

### PU-1 — Syarat output "aman untuk sesi berikutnya"

- **Area yang diuji:** konsep inti (C1, C8) dan aturan checkpoint (②, ④, ⑤). Jenis isi yang diuji: **fakta sumber**.
- **Pertanyaan:** Sebuah unit baru menyelesaikan satu tahap; hasilnya sudah ditulis ke path resmi di workspace tetapi belum di-commit dan belum ter-push. Bolehkah agent menyatakan output itu "aman dilanjutkan pada sesi baru"? Sebutkan dua syarat yang harus dipenuhi beserta rujukan aturannya.
- **Tujuan:** menguji pemahaman syarat ganda (C8) dan larangan aturan ⑤.
- **Kriteria keberhasilan (semua wajib terpenuhi):** (a) menjawab "belum boleh"; (b) menyebut syarat tersimpan di path resmi — aturan ② (b. 42); (c) menyebut syarat tersedia di branch/remote lewat commit + push — aturan ④–⑤ (b. 44–45); (d) tidak menyatakan salah satu syarat saja cukup.
- **Acuan jawaban:** E-I2 / C8 (fakta sumber, dirumuskan ulang).
- **Catatan cakupan (ditambahkan pada implementasi K-P1, 2026-09-03):** dua aturan pada b. 44–45 tidak sebangun ruang lingkupnya — aturan ④ mewajibkan commit + push **hanya untuk output yang menjadi dependency tahap berikutnya**, sedangkan aturan ⑤ melarang klaim "aman dilanjutkan" **untuk setiap output** yang belum tersedia di branch/remote, terlepas dari status dependency-nya. Jawaban (a) "belum boleh" dipertahankan oleh ⑤ secara umum; pada output dependency, ④ menambah kewajiban eksplisit sebelum menyatakan tersedia. Pembedaan ruang lingkup ini sendiri tetap berlabel inferensi (S-7), tetapi dasar tekstualnya eksplisit di kedua baris.

### PU-2 — Recovery terhadap status yang tidak konsisten, lalu konflik

- **Area yang diuji:** recovery (C6), konflik (C7), titik berhenti (S-2). Jenis isi yang diuji: urutan langkah = **fakta sumber**; penerapan pada skenario = penggunaan, bukan klaim baru.
- **Pertanyaan:** Pada sesi baru, STATUS.md sebuah unit menyatakan "tahap 3 selesai, status `approved`", tetapi file output yang dirujuk tidak ada di branch. Urutkan langkah agent menurut protokol. Pada titik mana ia wajib berhenti? Jika di tengah verifikasi ia menemukan perubahan lain yang bertabrakan dengan keputusan itu, apa larangan pertamanya?
- **Tujuan:** menguji urutan recovery, kondisi wajib-berhenti, dan prinsip konflik pertama.
- **Kriteria keberhasilan (semua wajib terpenuhi):** (a) menyebut baca manifest → baca status → verifikasi output + commit → verifikasi branch + PR (b. 50–53) dalam urutan benar; (b) menyebut wajib berhenti dan bertanya saat status ambigu — dilarang menebak (b. 55); (c) menyebut prinsip konflik pertama: jangan menimpa perubahan tanpa menunjukkan konflik (b. 59). Bonus (bukan syarat lulus): menyadari bahwa mengulang tahap `approved` butuh alasan yang kriterianya masih terbuka (b. 54, terkait Q-O2).
- **Acuan jawaban:** E-F3 / C6, E-F4 / C7, S-2.

### PU-3 — Membedakan fakta sumber dan inferensi agent

- **Area yang diuji:** pembedaan fakta vs inferensi; konsep inti (X-I1, S-2). Jenis isi yang diuji: label tingkat kepastian.
- **Pertanyaan:** Klasifikasikan tiap pernyataan sebagai fakta sumber atau inferensi agent, dan berikan dasarnya: (a) "Checkpoint adalah catatan persisten agar sesi berikutnya dapat melanjutkan pekerjaan tanpa mengandalkan ingatan percakapan"; (b) "aturan ④ dan ⑤ membentuk definisi operasional siap-dijadikan-dependency"; (c) "berhenti dan bertanya adalah titik akhir fail-closed".
- **Tujuan:** menguji bahwa pembaca tidak menaikkan inferensi menjadi fakta.
- **Kriteria keberhasilan (semua wajib terpenuhi):** (a) fakta sumber — bunyi persis di b. 12–14 (E-D1); (b) inferensi (X-I1) — tidak tertulis di sumber, hanya berdasar b. 44–45; (c) inferensi (S-2) — istilah "fail-closed" tidak ada di sumber; sumber hanya berkata "berhenti dan tanyakan pengguna; jangan menebak" (b. 55).
- **Acuan jawaban:** tabel Konsep Inti dan daftar ekstraksi (label E-/X-/S-).

## Langkah Penerapan

## Langkah Penerapan

_Dihasilkan di tahap Apply (2026-09-03). **Status bagian ini: BELUM diverifikasi** — tidak termasuk cakupan `checked` sebelumnya; wajib diverifikasi ulang sebelum status `checked` final. **Semua langkah di bawah adalah REKOMENDASI PENERAPAN agent** — disintesis dari fakta sumber yang diberi rujukan, bukan perintah eksplisit dari sumber._

### LP-1 — Uji kelayakan checkpoint sebelum klaim "aman dilanjutkan"

- **Tindakan:** sebelum menyatakan sebuah output unit siap dilanjutkan sesi baru, jalankan dua cek: `git status --porcelain` menghasilkan keluaran kosong, dan `git rev-parse HEAD` sama dengan sha remote branch terkait (`git ls-remote origin <branch>`).
- **Kapan:** setiap kali sebuah tahap menghasilkan dependency untuk sesi berikutnya.
- **Bukti berhasil:** kedua cek lulus, dan hasilnya tercatat di `STATUS.md` unit (field Commit/PR terisi sha nyata + "Pekerjaan belum tersimpan: tidak ada").
- **Jenis:** rekomendasi agent; dasar sumber = syarat ganda C8 (b. 42, 44–45). Bentuk kedua cek adalah cara operasional yang dipilih agent, bukan kalimat sumber.

### LP-2 — Recovery test nyata satu kali per unit kerja

- **Tindakan:** setelah tahap dependency pertama tersimpan dan ter-push, tutup sesi secara sengaja, buka sesi baru, dan lanjutkan hanya dari manifest + `STATUS.md` + output di branch tanpa konteks percakapan; tulis laporan recovery singkat.
- **Kapan:** satu kali per unit kerja, secepatnya setelah tahap dependency pertama.
- **Bukti berhasil (diperjelas pada implementasi K-P2 opsi A, 2026-09-03):** laporan recovery memuat 4 artefak wajib: (a) tahap terakhir dan tahap berikutnya yang disebutkan persis dari `STATUS.md`; (b) daftar file output yang diverifikasi keberadaannya; (c) sha commit terakhir yang diverifikasi terhadap remote; (d) pernyataan eksplisit "tidak ada tahap yang diulang", atau daftar ambiguitas yang membuat sesi berhenti dan bertanya. Kriteria perilaku sebelumnya (tanpa menebak; berhenti-bertanya saat ambigu) tetap berlaku sebagai syarat perilaku; artefak (a)–(d) adalah bukti tercatatnya.
- **Jenis:** rekomendasi agent; dasar sumber = langkah recovery ①–⑥ (b. 50–55) ditambah pengalaman unit ini sendiri menjalankan skenario AT-04.

### LP-3 — Konvensi sementara "Waktu pembaruan" per tahap

- **Tindakan:** isi field "Waktu pembaruan" di setiap `STATUS.md` unit setiap kali satu tahap selesai. Jangan menganggap konvensi ini perintah sumber — interval tidak diatur sumber (Q-O3 masih TERBUKA dan sengaja dipertahankan). Jika interval baku ingin ditetapkan di protokol, ajukan lewat jalur proposal perubahan aturan (pola AT-05), bukan edit diam-diam.
- **Kapan:** setiap tahap selesai, sampai protokol menetapkan interval baku.
- **Bukti berhasil:** setiap perubahan tahap pada `STATUS.md` disertai nilai "Waktu pembaruan" yang berubah.
- **Jenis:** konvensi lokal unit ini (keputusan agent + pengguna); berkaitan langsung dengan ketidakpastian terbuka Q-O3.

## Hasil Tahap Capture (tahap 1 — selesai)

### Identitas sumber

| Field | Nilai | Bukti |
|---|---|---|
| Judul | Protokol Checkpoint & Recovery | judul baris 1 sumber |
| Pembuat | meta-sistem ini (dokumen `_meta/`, pemilik keputusan pengguna) | `_meta/SYSTEM_MANIFEST.md` |
| Lokasi asli | `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md` | path repo |
| Lokasi snapshot | `sistem-pilot-catatan-belajar/fixtures/SUMBER_CHECKPOINT_RECOVERY.md` | dibuat unit ini |
| sha256 sumber asli | `bb0b857a1a7d1e606476c7942c2fac9bc846f8006d05652cfaa4a390fbe2a63a` | `sha256sum` saat capture |
| Ukuran sumber | 53 baris, 1996 byte | `wc -l -c` saat capture |
| Verifikasi snapshot | baris 10+ snapshot identik byte-per-byte dengan sumber; `diff` kosong, exit 0 | `diff` saat capture |
| Tanggal akses | 2026-09-03 | sesi ini |
| Jenis sumber | dokumen internal repo, bukan sumber publik | sifat repo |

### Tujuan belajar (dirumuskan ulang dari pertanyaan awal)

Memeriksa apakah `STATUS.md` unit pilot sudah memenuhi aturan checkpoint di sumber, dengan menguji unit ini sendiri lewat pemutusan sesi nyata.

### Pertanyaan awal yang akan dijawab tahap berikutnya

1. Apa yang membuat checkpoint cukup untuk recovery nyata, bukan hanya ringkasan chat?
2. Kondisi apa yang mewajibkan agent berhenti dan bertanya?
3. Apa beda "output tersimpan" dengan "output aman untuk sesi berikutnya"?

## Hasil Tahap Extract (tahap 2 — selesai)

_Dikerjakan pada sesi recovery setelah AT-04 lulus tahap pertama (koreksi metadata snapshot di commit `a39f0a6`). Sumber: snapshot beku `../../fixtures/SUMBER_CHECKPOINT_RECOVERY.md`; semua rujukan menyebut nama bagian dan nomor baris di file snapshot tersebut (isi baris 10 ke bawah identik dengan sumber asli)._

### Definisi (fakta sumber)

| Kode | Butir | Rujukan |
|---|---|---|
| E-D1 | Checkpoint = "catatan persisten agar sesi berikutnya dapat melanjutkan pekerjaan tanpa mengandalkan ingatan percakapan"; sekaligus ditegaskan bahwa checkpoint bukan sekadar ringkasan di chat | `Tujuan`, baris 12–14 |
| E-D2 | Kosakata status unit dibatasi 6 nilai: `in-progress`, `blocked`, `ready-for-review`, `approved`, `merged`, `abandoned` | `Format checkpoint`, baris 23 |
| E-D3 | Format checkpoint = 12 field: Status; Tahap terakhir selesai; Tahap berikutnya; Output resmi; Sumber konteks yang dibaca; Keputusan baru; Approval yang sudah diberikan; Commit terakhir; PR terkait; Pekerjaan yang belum tersimpan; Risiko atau blocker; Waktu pembaruan | `Format checkpoint`, baris 23–36 |

### Fakta/aturan sumber

| Kode | Butir | Rujukan |
|---|---|---|
| E-F1 | Checkpoint wajib untuk setiap unit kerja atau tahap besar yang menghasilkan input untuk tahap berikutnya | baris 16–18 |
| E-F2 | Aturan checkpoint (6): ① baca sumber resmi sebelum membuat checkpoint; ② simpan output tahap ke path yang disebutkan, bukan hanya menampilkannya di chat; ③ perbarui status setelah output tersimpan; ④ untuk output yang menjadi dependency tahap berikutnya: commit dan push sebelum menyatakan tersedia untuk sesi baru; ⑤ dilarang menyatakan "aman dilanjutkan" jika output hanya berada di workspace dan belum tersedia di branch/remote; ⑥ setelah checkpoint, jelaskan apakah pengguna perlu review, approve, atau cukup mengetahui status | `Aturan checkpoint`, baris 39–46 |
| E-F3 | Recovery sesi baru (6 langkah): ① baca manifest sistem; ② baca status unit kerja yang aktif; ③ verifikasi file output dan commit terakhir; ④ verifikasi branch dan PR terkait; ⑤ jangan mengulang tahap berstatus `approved` atau `merged` tanpa alasan; ⑥ jika status ambigu, berhenti dan tanyakan pengguna — jangan menebak | `Recovery saat sesi baru`, baris 48–55 |
| E-F4 | Recovery saat konflik (4): ① jangan menimpa perubahan tanpa menunjukkan konflik; ② identifikasi file, branch, dan keputusan yang bertabrakan; ③ pisahkan perubahan jika dua tujuan tidak berkaitan; ④ minta approval ulang jika konflik menyentuh keputusan Besar | `Recovery saat konflik`, baris 57–62 |

### Ide inti (fakta sumber, dirumuskan ulang sebagai konsep)

| Kode | Butir | Rujukan |
|---|---|---|
| E-I1 | Landasan recovery adalah catatan persisten yang tersimpan, bukan konteks percakapan sesi sebelumnya | baris 14 |
| E-I2 | Sebuah output baru "aman untuk sesi berikutnya" hanya jika dua syarat terpenuhi sekaligus: tersimpan di path resmi (aturan ②) dan tersedia di branch/remote (aturan ④–⑤) | baris 42, 44–45 |

### Contoh yang ada di sumber

| Kode | Butir | Rujukan |
|---|---|---|
| E-C1 | Satu-satunya contoh konkret di sumber adalah blok template Markdown `Status — [Nama Unit Kerja]`; sumber tidak memuat contoh kasus naratif lain | baris 20–37 |

### Interpretasi agent — BUKAN fakta sumber

| Kode | Butir | Dasar rujukan |
|---|---|---|
| X-I1 | Aturan ④ dan ⑤ bersama-sama membentuk definisi operasional "siap dijadikan dependency": commit dan push adalah bagian dari arti "tersedia", bukan langkah tambahan opsional | baris 44–45 |
| X-I2 | Urutan langkah recovery (baca → verifikasi → lanjutkan) menanamkan prinsip mempercayai isi file yang terverifikasi, bukan asumsi urutan kejadian dari sesi lama | baris 50–55 |

### Pertanyaan terbuka (bahan tahap Verify)

| Kode | Pertanyaan | Asal |
|---|---|---|
| Q-O1 | Sumber menyebut "keputusan Besar" tanpa mendefinisikannya di dokumen ini; definisi mungkin berada di dokumen meta lain — perlu dicek, bukan diasumsikan | baris 62 |
| Q-O2 | Aturan ⑤ recovery melarang mengulang tahap `approved` "tanpa alasan", tetapi kriteria alasan yang sah tidak dirinci di sumber | baris 54 |
| Q-O3 | Sumber tidak mengatur interval pengisian "Waktu pembaruan" (per tahap atau per sesi); pemakaian per-tahap di unit ini adalah konvensi lokal, bukan klaim sumber | baris 36 |

## Hasil Tahap Verify (tahap 4 — selesai)

_Pemeriksaan independen pada 2026-09-03: setiap rujukan diuji ulang langsung terhadap baris snapshot (dibaca ulang dan dihitung ulang), bukan mengandalkan centang quality check tahap Structure. Pertanyaan terbuka ditelusuri ke dokumen meta resmi tanpa menganggap jawaban ada sebelum diverifikasi._

### Rujukan yang diperiksa

| Klaim di dokumen ini | Rujukan yang diuji | Hasil |
|---|---|---|
| Definisi checkpoint (E-D1, C1, Ringkasan) | b. 12–14 | LULUS — bunyi definisi cocok persis |
| Kewajiban checkpoint (E-F1, C4) | b. 16–18 | LULUS |
| Kosakata 6 status (E-D2, C3) | b. 23 | LULUS — 6 nilai terenumerasi persis |
| Format 12 field (E-D3, C2) | b. 23–36 | LULUS — jumlah field dihitung ulang = 12; kata "wajib" pada C2 dikoreksi (T-2) |
| Contoh template sebagai satu-satunya contoh konkret (E-C1) | b. 20–37 | LULUS |
| 6 aturan checkpoint dengan pemetaan ①–⑥ (E-F2, C5) | b. 39–46 (①=b.41 … ⑥=b.46) | LULUS |
| Aturan ② (E-I2, C8) | b. 42 | LULUS |
| Aturan ④–⑤ (E-I2, C8, X-I1, S-7) | b. 44–45 | LULUS |
| 6 langkah recovery (E-F3, C6) | b. 48–55 | LULUS |
| Larangan mengulang "tanpa alasan" (E-F3⑤, Q-O2) | b. 54 | LULUS |
| "Berhenti dan tanyakan, jangan menebak" (E-F3⑥, S-2) | b. 55 | LULUS |
| 4 prinsip konflik (E-F4, C7, Q-O1) | b. 57–62 | LULUS |
| Field "Waktu pembaruan" (E-D3, Q-O3) | b. 36 | LULUS |

### Koreksi akibat Verify (klaim yang lebih kuat dari sumber)

| Kode | Temuan | Tindakan |
|---|---|---|
| T-1 | Ringkasan menyebut "format minimum 12 field"; kata "minimum" tidak ada di sumber | Dikoreksi menjadi "format 12 field" |
| T-2 | C2 menyebut "Kolom wajib catatan"; kewajiban di sumber (b. 18) melekat pada pembaruan file status yang sesuai, bukan pada setiap kolom | Dikoreksi menjadi "Kolom dalam template" |

### Ketetapan Verify

- **Pemisahan label tidak tercampur:** seluruh `E-*` dan `C1`–`C8` adalah fakta sumber; `S-*` dan `X-I*` berlabel inferensi/sintesis; `Q-O*` berlabel pertanyaan terbuka. Tidak ditemukan fakta yang menyamar sebagai interpretasi atau sebaliknya.
- **C8 dipertahankan berlabel `fakta sumber (dirumuskan ulang)`** karena hanya konjungsi langsung dari dua aturan eksplisit (② dan ④–⑤). Opsi pelabelan paling ketat (turun ke `inferensi`) dicatat di Log Keputusan agar pengguna dapat memveto.
- **Keputusan mengisi "Hal yang Belum Jelas" pada tahap Structure dikonfirmasi tepat:** pengisian awal itu kini difinalkan di Verify persis sesuai janji penandanya, dan review pengguna atas hasil Structure telah menyetujui pendekatan tersebut. Bukan konflik; hanya penyesuaian penanda yang sudah dicatat transparan.
- **Konflik/ketidakpastian tersisa:** Q-O2 dan Q-O3 tetap terbuka (dinyatakan eksplisit); Q-O1 dan S-7 terjawab sebagian dengan catatan statusnya masing-masing. Tidak ada konflik antar-klaim yang tersisa di dokumen ini.
- **Blocker:** tidak ada.

### Keputusan status output

Status output dinaikkan dari `draft` menjadi **`checked`** sesuai kontrak tahap Verify (`WORKFLOW.md` tahap 4). Cakupan `checked`: seluruh konten hasil tahap Capture–Structure. Pertanyaan Uji Pemahaman dan Langkah Penerapan (hasil tahap Apply) belum ada dan **TIDAK termasuk** cakupan ini — keduanya wajib diperiksa lagi setelah tahap Apply. `checked` ≠ `approved` ≠ `released`: approval pengguna tetap wajib sebelum catatan dipakai sebagai rujukan tetap.

## Hasil Tahap Observe (tahap 6 — selesai)

_2026-09-03. Dua kegiatan: (A) verifikasi ulang terbatas seluruh konten Apply **sebelum status final dipertimbangkan**; (B) pemakaian nyata PU-1–PU-3 dan LP-1–LP-3 pada state pilot yang tersedia. Label: **[BUKTI]** = peristiwa/keluaran yang dapat dicek ulang; **[SIMULASI]** = jawaban uji yang disimulasikan agent; **[INTERPRETASI]** = penilaian agent, bukan bukti._

### A. Verifikasi ulang terbatas hasil Apply

| Butir | Pemeriksaan | Hasil |
|---|---|---|
| PU-1 | Acuan jawaban diuji ulang ke b. 42 (aturan ②) dan b. 44–45 (aturan ④–⑤): teks sumber cocok dengan syarat yang ditanyakan | **LULUS**, dengan catatan K-P1 (cakupan ④ khusus dependency vs ⑤ umum tidak dieksplisitkan di pertanyaan — terkait S-7) |
| PU-2 | Urutan skenario diuji ulang ke b. 50–53 (urutan benar: manifest → status → output+commit → branch+PR), b. 55 (wajib berhenti), b. 59 (larangan menimpa) | **LULUS** |
| PU-3 | Frasa opsi (a) ditemukan persis 1× di sumber (b. 14); istilah "fail-closed" dipastikan 0 temuan di snapshot; klasifikasi acuan (fakta / X-I1 / S-2) benar | **LULUS** |
| LP-1 | Label "rekomendasi agent" benar; dasar C8 cocok; kedua bukti berhasil teramati nyata (B-1) | **LULUS** |
| LP-2 | Label "rekomendasi agent" benar; dasar b. 50–55 cocok | **LULUS** dengan catatan K-P2 (sebagian kriteria bersifat kualitatif) |
| LP-3 | Label "konvensi lokal" benar; kriteria "nilai berubah setiap tahap" **tidak teramati penuh** pada pemakaian riil (B-3) | **GAGAL-TERAMATI pada kriteria utamanya** → K-P3 |
| Umum | Q-O2 dan Q-O3 masih ada dan tidak dihapus; tidak ada LP yang tampil sebagai aturan sumber | **LULUS** |

### B. Pemakaian nyata

**B-PU — Uji pemahaman dijalankan sebagai simulasi terkontrol [SIMULASI]:** PU-1 dijawab memenuhi 4/4 kriteria (belum boleh; syarat path b. 42; syarat branch/remote b. 44–45; tidak setengah-setengah); PU-2 memenuhi 3/3 kriteria plus bonus (urutan benar; berhenti-bertanya saat ambigu b. 55; larangan menimpa b. 59; menyadari area terbuka Q-O2); PU-3 memenuhi 3/3 (definisi = fakta b. 12–14; "definisi operasional" = inferensi X-I1; "fail-closed" = inferensi S-2). **[INTERPRETASI]:** kriteria dapat dinilai butir-per-butir dan jawaban dapat dipetakan ke rujukan. Keterbatasan yang dinyatakan jujur: penjawab simulasi adalah penulis catatan yang sama — kekuatan bukti terletak pada pemetaan jawaban→rujukan yang dapat dicek ulang, bukan pada kemampuan mengingat agent.

**B-1 — LP-1 dieksekusi langsung, dua kali [BUKTI]:**
- **Run 1: GAGAL pada kedua cek.** Penyebab (ditelusuri, bukan ditebak): lingkungan kerja sandbox dibangun ulang di tengah sesi ini — `.git` lokal kembali ke titik awal `ee5504e` dan tiga file tampak "modified", padahal isi working tree **terbukti identik byte-per-byte** dengan tip remote `66b787c` (blob hash ketiga file sama; `git diff 66b787c` kosong). Artinya: LP-1 menolak klaim "aman" pada state yang tidak cocok — **bekerja persis sesuai desain (fail-closed dalam arti kata sumbernya: berhenti, bukan menebak)**.
- **Rekonsiliasi [BUKTI]:** `git fetch`; verifikasi identitas isi; pointer branch dimajukan ke `66b787c` tanpa mengubah satu byte pun isi file. Tidak ada pekerjaan hilang — seluruh checkpoint selamat di remote berkat aturan ④–⑤.
- **Run 2: LULUS kedua cek** (`git status --porcelain` kosong; `git rev-parse HEAD` == `git ls-remote origin` == `66b787cf3060c2d8356cd06bc0ba6d6aa577e2a1`).
- **[INTERPRETASI]:** cek ini murah dan bernilai tinggi sebagai gerbang klaim "aman dilanjutkan"; kejadian Run 1 membuktikan nilainya pada kegagalan nyata, bukan skenario buatan.

**B-2 — LP-2 dibuktikan dua kali [BUKTI]:** (i) **terencana:** skenario AT-04 di awal sesi ini — sesi terputus pasca-Capture, sesi recovery melanjutkan dari `STATUS.md` tanpa mengulang Capture, tanpa konteks chat lama, dan berhenti melapor sebelum Extract hingga dikonfirmasi (disetujui pengguna); (ii) **tak direncanakan:** insiden rebuild lingkungan pada B-1 — lokal kehilangan 8 commit terbaru, semua pulih dari remote murni lewat verifikasi output + commit + branch (langkah ③–④, b. 52–53). **[INTERPRETASI]:** protokol teruji pada dua jenis kegagalan yang berbeda: pemutusan sesi dan kernelajaruan state lingkungan.

**B-3 — LP-3 dipakai di semua checkpoint unit ini [BUKTI]:** field "Waktu pembaruan" selalu terisi di setiap versi `STATUS.md`. **[TEMUAN]:** semua tahap unit ini terjadi pada tanggal yang sama (2026-09-03), sehingga nilainya tidak pernah berubah antar-tahap — kriteria keberhasilan LP-3 ("nilai berubah setiap perubahan tahap") **tidak dapat diverifikasi** pada pemakaian riil. **[INTERPRETASI]:** sebagai penanda hari ia berguna; sebagai penanda tahap ia lemah.

### C. Ringkasan observasi

- **Terbukti berguna [INTERPRETASI, didukung BUKTI]:** syarat ganda (PU-1/LP-1) sebagai gerbang klaim "aman"; recovery nyata (LP-2); pemisahan label fakta-inferensi (PU-3); pembatasan 1–3 pertanyaan membuat uji tetap ramping tanpa kehilangan area wajib.
- **Membingungkan/ambigu:** cakupan aturan ④ vs ⑤ di PU-1 (pembaca yang ketat bisa menjawab "tergantung dependency" — terkait S-7 yang masih berlabel inferensi); sebagian kriteria LP-2 kualitatif; granularitas tanggal pada "Waktu pembaruan".
- **Kegagalan/insiden yang tercatat:** (1) rebuild lingkungan mid-session (ditangani lewat pemulihan dari remote; tanpa kehilangan data); (2) kriteria LP-3 gagal-teramati pada pemakaian riil.

### D. Kandidat perbaikan — PROPOSAL TERBUKA, belum diterapkan

| Kode | Proposal | Status |
|---|---|---|
| K-P1 | Tambah catatan pada PU-1 yang membedakan kewajiban ④ (khusus output dependency) dari larangan klaim ⑤ (berlaku umum) | **Diimplementasikan 2026-09-03** (approval pengguna; lokal unit ini) |
| K-P2 | Perjelas bukti LP-2 dengan artefak wajib: laporan recovery harus menyebut file dan commit yang diverifikasi | **Opsi A diimplementasikan 2026-09-03** (approval pengguna); opsi B (konvensi workflow pilot) ditangguhkan |
| K-P3 | Naikkan granularitas "Waktu pembaruan" (mis. tanggal + nama tahap) — berkaitan Q-O3 yang masih TERBUKA; hanya lewat jalur proposal + approval, bukan edit diam-diam | Proposal |
| K-P4 | Catatan meta (bukan perubahan): `WORKFLOW.md` belum mendefinisikan mekanisme verifikasi-ulang pasca-Apply; jika diinginkan, ini usulan untuk meta-sistem lewat jalur proposal, bukan keputusan unit ini | Catatan untuk pengguna |

### E. Status setelah Observe

- Verifikasi ulang hasil Apply: **LULUS dengan catatan** (K-P1–K-P3; LP-3 tidak teramati penuh pada kriteria utamanya).
- Status output **tetap `draft`**: status `checked` final **tidak dinaikkan otomatis** oleh agent meski verifikasi ulang lulus — keputusan itu milik pengguna.
- Q-O2 dan Q-O3 **dipertahankan** sebagai ketidakpastian terbuka.

## Quality Check

- **Level pemeriksaan:** `Ringan` (catatan biasa, sumber internal tidak berisiko; belum ada trigger untuk level Sedang/Mendalam)

- [x] Klaim penting memiliki rujukan — diverifikasi ulang independen di tahap Verify: LULUS (13 jangkar rujukan diuji ke baris snapshot; koreksi wording T-1/T-2 diterapkan)
- [x] Fakta dan inferensi dibedakan — diverifikasi ulang di tahap Verify: LULUS; label E-/C- = fakta sumber, S-/X-I = inferensi, Q-O = terbuka; tidak ditemukan campuran
- [x] Ketidakpastian tidak disembunyikan — Q-O2 dan Q-O3 dinyatakan tetap terbuka secara eksplisit di tahap Verify, bukan ditutup-tutupi
- [x] Pertanyaan uji dapat dijawab atau diuji — **diverifikasi ulang + disimulasikan pada tahap Observe:** PU-1–PU-3 terjawab sesuai kriteria butir-per-butir; rujukan acuan diuji ulang ke snapshot (LULUS)
- [x] Langkah penerapan memiliki bukti keberhasilan — LP-1 dieksekusi nyata dua kali (gagal-dengan-benar lalu lulus), LP-2 dibuktikan dua kejadian nyata, LP-3 dipakai di semua checkpoint; **CATATAN: bukti LP-3 tidak teramati penuh pada hari yang sama → proposal K-P3**

Catatan: 6 dari 6 tahap selesai. Kelima butir quality check kini lulus pemeriksaan — butir 4–5 berdasarkan **bukti pemakaian nyata** di tahap Observe, bukan asumsi — dengan catatan LP-3 dan kandidat proposal K-P1–K-P4 tercatat terbuka. **Status output tetap `draft`**: status `checked` final TIDAK dinaikkan otomatis oleh agent dan menunggu keputusan pengguna; `checked` ≠ `approved` ≠ `released`.

## Log Keputusan

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-03 | Bahan belajar unit `pilot-002` = `_meta/PROTOKOL_CHECKPOINT_RECOVERY.md`, bukan fixture simulasi lama | Topiknya persis yang sedang diuji (recovery nyata); sumber nyata dan dapat ditelusuri, bukan bahan sintetis |
| 2026-09-03 | Sumber disalin jadi snapshot beku di `fixtures/SUMBER_CHECKPOINT_RECOVERY.md` dengan sha256 tercatat | Menjawab risiko "sumber tidak tercatat sehingga catatan tidak dapat diverifikasi"; ekstraksi tahap berikutnya menunjuk versi yang persis dibaca |
| 2026-09-03 | Unit baru `pilot-002`, `pilot-001` tidak disentuh | Menjaga contoh awal tetap utuh sebagai pembanding, sesuai instruksi pengguna |
| 2026-09-03 | Output berhenti di tahap Capture dan status tetap `draft` | Sengaja, sebagai titik putus untuk recovery test nyata (acceptance test AT-04) |
| 2026-09-03 | Butir ekstraksi digabung menjadi daftar Konsep Inti C1–C8 yang semuanya berlabel `fakta sumber`; setiap penarikan makna baru dipisah sebagai inferensi berkode `S-` | Menjaga aturan "fakta ≠ interpretasi" tetap terlihat setelah tahap penggabungan; tidak ada fakta yang diam-diam berubah jadi kesimpulan |
| 2026-09-03 | Bagian "Hal yang Belum Jelas" diisi pada tahap Structure sesuai instruksi pengguna, dengan catatan bahwa finalisasinya tetap di tahap Verify | Penanda lama ("hasil tahap Verify") berasal dari skeleton tahap Capture; instruksi pengguna untuk tahap Structure mencantumkan bagian ini, jadi diisi sekarang dengan penggantian penanda yang transparan — bukan diubah diam-diam |
| 2026-09-03 | Quality check butir 1 dan 2 dicentang di tahap Structure, status output tetap `draft` | Kedua butir kini dapat diverifikasi langsung dari tabel/rujukan; status `checked` tetap hanya boleh lewat tahap Verify sesuai WORKFLOW |
| 2026-09-03 | Koreksi T-1/T-2 di tahap Verify: kata "minimum" (Ringkasan) dihapus dan "Kolom wajib" (C2) dilunakkan menjadi "Kolom dalam template" | Verify menemukan dua klaim lebih kuat dari sumber; wajib dikoreksi sebelum status `checked` layak diberikan |
| 2026-09-03 | C8 dipertahankan berlabel `fakta sumber (dirumuskan ulang)` | Hanya konjungsi langsung dari dua aturan eksplisit (② dan ④–⑤); opsi pelabelan paling ketat (turun ke `inferensi`) dicatat di sini agar pengguna dapat memveto kapan saja |
| 2026-09-03 | Status output dinaikkan ke `checked` dengan cakupan eksplisit: hanya konten tahap Capture–Structure | Kontrak tahap Verify menghasilkan `checked` atau daftar blocker; tidak ada blocker; cakupan dibatasi karena hasil Apply belum ada — mencegah `checked` disalahartikan mencakup bagian yang belum lahir |
| 2026-09-03 | Status output diturunkan `checked` → `draft` saat konten Apply masuk | Konten Apply baru belum diverifikasi; mempertahankan `checked` akan membuat cakupannya tidak akurat. Jejak `checked` (cakupan Capture–Structure) tetap tersimpan di commit `f2aec6f`; status `checked` final menunggu verifikasi ulang hasil Apply |
| 2026-09-03 | Pertanyaan uji dibuat 3 butir (PU-1–PU-3) mencakup kelima area wajib (konsep inti, checkpoint, recovery, konflik, fakta-vs-inferensi) | `WORKFLOW.md` membatasi 1–3 pertanyaan; pemetaan area-ke-pertanyaan dicatat eksplisit agar tidak ada area yang hilang secara diam-diam |
| 2026-09-03 | Seluruh Langkah Penerapan (LP-1–LP-3) diberi label `rekomendasi agent` dengan dasar sumber per butir | Rekomendasi tidak boleh tampak sebagai perintah sumber; LP-3 mengacu ketidakpastian terbuka Q-O3 yang dipertahankan, bukan dihapus |
| 2026-09-03 | Status output **dipertahankan `draft`** walau verifikasi ulang terbatas hasil Apply lulus dengan catatan | Aturan sesi: `checked` tidak naik otomatis hanya karena konten ada; keputusan status final milik pengguna |
| 2026-09-03 | QC butir 4–5 dicentang setelah verifikasi ulang + pemakaian nyata, dengan catatan LP-3 (kriteria utamanya tidak teramati pada hari yang sama) | Centang kini berbasis bukti pemakaian (B-1, B-2, B-3), bukan asumsi; bukti dan batas validitasnya ditulis apa adanya |
| 2026-09-03 | Kandidat perbaikan K-P1–K-P4 dicatat sebagai **proposal terbuka tanpa diterapkan** | Sesuai aturan Observe: perubahan workflow/prinsip masuk jalur proposal + approval, bukan edit diam-diam |
| 2026-09-03 | K-P1 diimplementasikan (lokal unit ini): catatan cakupan ④/⑤ ditambahkan pada PU-1 | Approval pengguna atas proposal K-P1; mencegah pertanyaan menilai-salah pembaca ketat; rujukan b. 44–45 dan label inferensi S-7 dipertahankan |
| 2026-09-03 | K-P2 opsi A diimplementasikan: bukti berhasil LP-2 menjadi 4 artefak wajib; opsi B (konvensi workflow pilot) ditangguhkan | Approval pengguna; bukti recovery menjadi auditable dan selaras AT-04 |
| 2026-09-03 | Sel status pada tabel kandidat diperbarui hanya untuk K-P1/K-P2; sel K-P3/K-P4 sengaja tidak disentuh | Bookkeeping agar sesi berikutnya tidak bertindak atas info basi; status penangguhan K-P3/K-P4 dicatat di STATUS.md sesuai batasan sesi |
