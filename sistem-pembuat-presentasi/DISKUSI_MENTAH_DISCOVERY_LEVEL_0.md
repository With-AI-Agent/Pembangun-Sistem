# DISKUSI MENTAH — Discovery Level-0 Sistem Pembuat Presentasi

> **Status file ini:** checkpoint diskusi mentah, **bukan** `00_RENCANA_KERANGKA.md` dan **bukan** dokumen instruksi aktif. Dibuat sesuai aturan "Checkpoint diskusi ringan" di `_meta/00_CARA_KERJA_META.md` (diskusi sudah >5 giliran dan mendekati keputusan, sementara sesi lmarena bisa crash — fakta platform #3 di `_meta/PLATFORM_LMARENA.md`). Kalau sesi terputus, lanjutkan dari sini.
>
> **Dibuat:** 4 September 2026 (UTC) / 5 September 2026 (WIB) — sesi `arena/01a06d7b-pembangun-sistem`
> **Nama folder sementara:** `sistem-pembuat-presentasi/` — nama belum dikonfirmasi pengguna, boleh diganti murah selama belum ada banyak rujukan.

---

## 1. Ide mentah dari pengguna (kutipan, belum dirapikan)

- Sistem pembuat presentasi. Input bisa macam-macam: dari pengguna, atau dari riset internet oleh agent, disesuaikan keinginan pengguna.
- **Kalau pengguna mau hanya dari bahannya sendiri, agent tidak boleh mengarang.**
- Output beragam: ppt/pptx, html, dsb. **Default: ppt/pptx.**
- Ada tempat input, ada tempat output.
- Ada **mekanisme mempelajari mendalam terlebih dahulu**. Contoh: input skripsi → agent pelajari dan pahami secara mendalam **tanpa ada yang terlewat**.
- Pengguna bisa menyesuaikan isi presentasi dan tampilannya.
- Untuk visual: kalau pengguna belum punya gambaran, **agent boleh riset visual yang cocok untuk tema**, termasuk riset internet, lalu **menawarkan dulu ke pengguna**.
- Jawaban pengguna untuk bentuk/aturan/gerbang/verifikasi: **"beda-beda, tergantung keadaan dan kebutuhan"** — dan pengguna meminta agent yang mengusulkan yang terbaik, dengan izin riset internet.
- Pengguna mengaku selama ini bingung **"gimana caranya memastikan AI sudah paham keseluruhan tanpa terlewat"**.

## 2. Kesimpulan arsitektur sementara (perlu dikonfirmasi)

Karena semua aspek "tergantung keadaan", yang **dikunci bukan isinya tapi prosesnya**:

- Setiap presentasi **wajib** lewat sesi perancangan yang menghasilkan **Brief** (sumber, aturan anti-ngarang, kedalaman pemahaman, gaya visual, format output, durasi/jumlah slide).
- Bentuk dasar: **gabungan BERTINGKAT + SIKLUS**.
  - Bertingkat (lapisan atas **opsional**, dipakai ulang antar deck): Aset Gaya / Paket Ketentuan institusi.
  - Siklus (wajib, per deck): **Perancangan → Pemahaman Bahan → Outline + Rencana Visual → Produksi File → Verifikasi**.
- Yang harus konsisten: **jejak sumber** (tiap pernyataan di slide → nomor halaman / URL) dan **kontrak Brief wajib terisi sebelum produksi**.

## 3. Hasil riset (menjawab keraguan "presentasi itu kan gaya masing-masing")

**Temuan kunci: "gaya masing-masing" benar untuk ESTETIKA, tapi ada konsensus berbasis bukti untuk STRUKTUR dan BEBAN KOGNITIF.** Jadi sistem ini punya **lantai (wajib)** dan **langit-langit (bebas)**.

### Lantai — wajib, berbasis bukti (boleh di-override eksplisit + dicatat)

| Aturan | Bukti |
|---|---|
| Judul slide = **kalimat pernyataan** (assertion), bukan frasa topik | Garner & Alley (2013), *International Journal of Engineering Education* 29(6):1564-1579 — audiens assertion-evidence lebih paham & lebih ingat, signifikan secara statistik (p < .01). Sumber: https://writing.engr.psu.edu/research.html |
| Dukung judul dengan **bukti visual**, bukan dinding bullet | Struktur assertion-evidence (Michael Alley, Penn State); studi di Thai EFL juga menunjukkan hasil posttest lebih baik: https://files.eric.ed.gov/fulltext/EJ1396370.pdf |
| **Coherence**: buang materi yang tidak mendukung pesan (termasuk gambar dekoratif) | Prinsip multimedia Mayer — https://multimedia.ucsd.edu/best-practices/presentation-design.html |
| **Redundancy**: teks di slide bukan transkrip naskah bicara; naskah masuk *speaker notes* | Mayer (redundancy principle); panduan ACU: "Slides should not be a script to be read… additional content in the Notes section" — https://staff.acu.edu.au/our_university/centre-for-education-and-innovation/educational-technologies/creating-video-resources/multimedia-design-principles |
| **Segmenting**: pecah materi kompleks jadi bagian bertahap; 1 pesan per slide | Mayer (segmenting); https://www.sciencedirect.com/science/article/abs/pii/S2211368121000231 |
| **Signaling**: beri penanda bagian penting (panah/lingkaran/penekanan) | Mayer (signaling); Kosslyn (principle of salience) |
| Jumlah slide mengikuti **durasi** (~1 slide per 1–2 menit) | Sidang skripsi 10–15 menit → 10–15 slide (beberapa sumber 12–18): https://nugaskampus.com/artikel/template-ppt-sidang-dosen-fokus-ke-isi.html , https://skripsimalang.com/tips-skripsi/panduan-lengkap-isi-ppt-sidang-skripsi-yang-menarik-dan-efektif/ |
| Font minimum terbaca (aturan 10/20/30: ≤10 slide, ≤20 menit, font ≥30) | https://masoemuniversity.ac.id/artikel/panduan-menyusun-presentasi-sidang-skripsi-yang-menarik-dan-tidak-membosankan/ |

### Langit-langit — bebas / ditentukan per deck

Palet warna, font, logo, master/layout, gaya ilustrasi. Sumbernya bisa: template pengguna, gaya siap pakai dari sistem, atau hasil riset agent yang **ditawarkan sebagai pilihan** sebelum dipakai.

### Konteks sidang skripsi (untuk preset domain pertama)

- Presentasi 10–15 menit; total sidang 45–90 menit termasuk tanya jawab.
- Struktur lazim: judul → latar belakang (1-2) → rumusan masalah (1) → tujuan (1) → manfaat (1) → tinjauan pustaka (1-3) → metodologi (1-2) → hasil (2-4) → pembahasan (2-3) → kesimpulan (1) → saran (1) → terima kasih (1). Sumber: https://ftp.bills.com.au/lunar-tips/berapa-slide-ppt-skripsi-yang-ideal-1767647173 , https://www.pelajarwajo.com/2026-03-17/apa-itu-sidang-skripsi-panduan-lengkap-untuk-mahasiswa/
- Kegagalan paling umum: slide penuh teks, presenter membaca slide.
- Implikasi: ada kebutuhan **Paket Ketentuan** (kampus/perusahaan punya aturan sendiri) + **cek kepatuhan** otomatis.

## 4. Fakta teknis yang SUDAH diverifikasi di lingkungan ini (bukan asumsi)

| Hal | Hasil | Perintah/bukti |
|---|---|---|
| `python-pptx` | Tidak terpasang default, **bisa diinstall** | `pip install --target /tmp/pptxtest python-pptx` → exit 0; ikut Pillow 12.3.0 + lxml 6.1.3 |
| Bikin .pptx asli | **Bisa** | Deck uji 3 slide: judul, body 3 paragraf (level 0/1/1), tabel 3×3, gambar PNG bikinan Pillow → 32.684 bytes; dibaca ulang: `slide: 3`, `punya tabel: True`, `punya gambar: True` |
| Output HTML | Bisa | tanpa dependensi tambahan |
| Render pptx → gambar/PDF | **TIDAK BISA** | `command -v libreoffice soffice` kosong; `/usr/bin/*office*`, `/opt/libreoffice*` tidak ada; `pandoc` tidak ada |
| Install LibreOffice | **TIDAK BISA** | `sudo -n apt-get update` → `Connection failed` ke `deb.debian.org` (IP 151.101.66.132:80); `apt-cache search libreoffice` kosong. PyPI **bisa** |
| Pillow untuk preview hampiran | Tersedia (ikut python-pptx) | bisa menggambar perkiraan slide jadi PNG |
| Disk | 20G bebas | `df -h /home/user` |

**Konsekuensi desain (penting):** agent tidak akan pernah bisa "melihat" hasil render PowerPoint. Verifikasi tampilan harus: (a) struktural lewat kode, (b) preview hampiran HTML/Pillow yang bisa dibuka pengguna di browser, (c) pengguna membuka sendiri file .pptx-nya. Tidak boleh ada klaim "sudah kucek tampilannya" tanpa menyebut jalur mana yang dipakai.

### Praktik teknis python-pptx (dari riset, belum semua diuji di sini)

- Buka template dengan `Presentation('template.pptx')` → master, font, warna, logo ikut terbawa.
- Placeholder hidup di **slide layout**; slide dibuat dari layout lalu mewarisi placeholder-nya. Inspeksi `ph.placeholder_format.idx` dan `ph.name` **sebelum** menulis.
- Tulis lewat `text_frame`; untuk menjaga format asli ubah `tf.paragraphs[0].runs[0].text`, bukan timpa seluruh `text_frame.text`.
- Tabel tidak bisa ditulis lewat table placeholder — pakai `slide.shapes.add_table()`. Gambar: `slide.shapes.add_picture()`.
- Risiko yang terdokumentasi: teks pengganti yang lebih panjang **meluber**; elemen template yang tidak terpakai harus **dihapus utuh**, bukan dikosongkan teksnya; layout harus **bervariasi** (monoton = failure mode umum). Sumber: https://www.slidegenius.com/cm-faq-question/how-can-i-use-python-to-create-a-powerpoint-presentation-from-a-template , https://github.com/anthropics/skills/blob/main/skills/pptx/editing.md , https://stackoverflow.com/questions/47446367/python-pptx-slide-layout-import

## 5. Usulan agent untuk 4 hal yang pengguna serahkan ke agent (BELUM dikonfirmasi)

1. **Standar minimum:** ADA, tapi hanya untuk struktur & beban kognitif (tabel "Lantai" di atas). Estetika tetap bebas. Ketentuan institusi ditangani lewat **Paket Ketentuan** + cek kepatuhan.
2. **Gerbang approval: 3, adaptif.** G1 peta pemahaman bahan → G2 outline + rencana visual → G3 file final. G1 boleh digabung ke G2 **hanya kalau** bahan terukur pendek/sederhana (ambang diusulkan: ≤15 halaman ATAU ≤5.000 kata), dan **yang menentukan adalah angka terukur, bukan selera agent**.
3. **Mekanisme kelengkapan:** adaptif dengan pemicu keras. Bahan panjang → 5 langkah penuh (kerangka dulu → kartu per subbab → tabel cakupan → spot-check acak → approval). Bahan pendek → checklist ringan. Intinya: **"lengkap" jadi hitungan, bukan perasaan.**
4. **Verifikasi tampilan: kombinasi (a)+(b)+(c)**, dengan catatan jujur bahwa (a) dan (b) bukan render PowerPoint.

## 6. Yang masih terbuka / belum diputuskan

- [ ] Nama sistem final + nama folder.
- [ ] Konfirmasi 4 usulan di bagian 5.
- [ ] Ambang "bahan pendek vs panjang" (usulan 15 halaman / 5.000 kata) — angka final.
- [ ] Format output selain pptx: html saja, atau juga pdf/md? (pdf butuh renderer yang tidak ada di sini)
- [ ] Apakah riset internet untuk **isi** (bukan cuma visual) juga masuk lingkup versi pertama.
- [ ] Prinsip universal mana yang dipakai apa adanya vs di-override (wajib dicatat di `00_RENCANA_KERANGKA.md`).
- [ ] Batasan platform: diasumsikan **dipakai via lmarena Agent Mode** → Prinsip Checkpoint & Recovery wajib. **Belum dikonfirmasi pengguna.**

## 7. Langkah berikutnya menurut `_meta/00_CARA_KERJA_META.md`

1. Tutup pertanyaan di bagian 6 lewat diskusi.
2. Tulis `00_RENCANA_KERANGKA.md` (format sesuai `_meta/01_DISCOVERY_LEVEL_0.md`) → **kategori Besar**: wajib direview isi lengkapnya oleh pengguna sebelum merge.
3. Salin `_meta/SYSTEM_MANIFEST_TEMPLATE.md` → manifest sistem ini.
4. Tulis prompt Discovery detail untuk tiap dokumen yang butuh penggalian.
5. Update `_meta/INDEKS_SISTEM.md` + buat `_cadangan-claude/RINGKASAN_sistem-pembuat-presentasi.md`.
