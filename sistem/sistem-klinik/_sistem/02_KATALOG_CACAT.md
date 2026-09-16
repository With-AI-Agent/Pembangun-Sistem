# Katalog Cacat Sistem (Sistem Klinik)

> **Dokumen Hidup (Living Document)**
> Katalog ini adalah basis pengetahuan (knowledge base) dan panduan diagnostik utama bagi Sistem Klinik. Katalog ini digunakan saat Tahap B Diagnosis untuk memeriksa kesehatan sebuah sistem target.

## Aturan Promosi Temuan Baru
1. **Sumber Wajib (Temuan Run):** Setiap kali Sistem Klinik menyelesaikan run di repo target (rawat-jalan/rawat-inap) dan menemui cacat struktural/prosedural, temuan tersebut wajib dipanen di Tahap F.
2. **Cek Duplikat:** Cek dulu apakah cacat yang sama sudah ada di katalog ini. Hanya cacat yang **belum ada** atau varian yang benar-benar berbeda yang boleh ditambahkan.
3. **Format Terkunci:** Cacat baru harus ditulis menggunakan field yang identik dengan yang ada (ID, Nama, Gejala, Cara Periksa, Pola Perbaikan, Bukti/Risiko).
4. **Mekanisme Promosi:** Agent menyertakan cacat baru tersebut sebagai usulan (PR) ke repo meta (sistem klinik), menambahkan entri ke tabel di bawah beserta Log Keputusan perubahannya.

---

## Daftar Cacat (Katalog)

### C-01: Kebocoran Ketergantungan Eksternal (Self-Containment Broken)
- **Gejala:** Sistem atau folder kit memiliki instruksi, aturan, atau alat yang bergantung pada file di luar foldernya (misalnya merujuk file di _meta/ dengan *backtick* tanpa menyediakannya di dalam sistem itu sendiri).
- **Cara Periksa (Diagnosis):** Cari pola rujukan absolut atau *backtick* ke luar folder sistem (misal `grep "_meta/"` atau `grep "tools/"`). Jalankan skrip uji kemandirian (jika tersedia).
- **Pola Perbaikan (Resep):** Salin file/aturan eksternal yang dirujuk ke dalam folder sistem, tandai sebagai turunan berlabel versi. Ubah rujukan asli menjadi provenance historis tanpa *backtick*.
- **Bukti / Risiko:** Sistem akan rusak dan tidak bisa dioperasikan saat diunduh (extracted) sebagai repo mandiri yang terpisah dari induknya.

### C-02: Manifest Basi (Drifted State)
- **Gejala:** Field `Versi`, `Tahap`, atau `Status` di `SYSTEM_MANIFEST.md` sudah tidak sesuai dengan kondisi aktual *working tree* (misal masih "Proposed" padahal PR kerangka sudah merged, atau "Belum dibangun" padahal dokumen sudah ada).
- **Cara Periksa (Diagnosis):** Bandingkan isi `SYSTEM_MANIFEST.md` dengan daftar file aktual (`ls`) dan histori PR terakhir yang merged.
- **Pola Perbaikan (Resep):** Sinkronisasikan field manifest dengan status sebenarnya. Tambahkan cek manifest pada alur verifikasi penutup.
- **Bukti / Risiko:** Kehilangan kepercayaan terhadap manifest; agent atau sistem lain akan mengambil keputusan berdasar konteks yang salah.

### C-03: Log Sesi Menggantung (Zombie Log)
- **Gejala:** Terdapat file `LOG_SESI_*.md` yang memiliki header `- **Keadaan:** \`OPEN\``, padahal pekerjaan sudah selesai, PR terkait sudah merged, atau branch sudah tidak ada.
- **Cara Periksa (Diagnosis):** Cari teks `Keadaan: \`OPEN\`` di dalam arsip log sesi, lalu cocokkan dengan status PR/branch menggunakan `gh pr list --state all`.
- **Pola Perbaikan (Resep):** Ubah status log tersebut secara retrospektif menjadi `CLOSED` dengan menambahkan catatan penutupan di bagian akhir log (append).
- **Bukti / Risiko:** Agent baru yang memulai sesi akan bingung menentukan *entry point* atau mencoba melanjutkan konteks pekerjaan yang sebenarnya sudah usai, menyebabkan tabrakan state.

### C-04: Bukti Pengujian Volatil
- **Gejala:** Laporan penerimaan (acceptance test) atau bukti QA mengandalkan angka-angka absolut yang mudah berubah secara natural, seperti "jumlah baris (line counts)" atau "jumlah kata" dari korpus yang terus berkembang.
- **Cara Periksa (Diagnosis):** Periksa file verifikasi atau bukti di dalam sistem. Apakah ada syarat kelulusan semacam "baris > 1500" atau angka hitungan file di korpus dinamis?
- **Pola Perbaikan (Resep):** Ganti metrik volatil dengan uji keberadaan struktur (file eksis), regex pola tertentu, atau status kembalian alat (exit 0). 
- **Bukti / Risiko:** Sistem akan sering mengalami *false negative* (ujian gagal padahal sistem tidak rusak) seiring pertumbuhan konten.

### C-05: Absennya Mekanisme Fail-Closed (Checkpoint Tidak Ditegakkan)
- **Gejala:** Sistem tidak berhenti saat terjadi anomali (misalnya alat validasi menghasilkan error/merah, tapi pekerjaan terus dilanjutkan sampai tahap merge).
- **Cara Periksa (Diagnosis):** Cek panduan pengguna dan alur kerja (pipeline/actions jika ada). Apakah ada gerbang eksplisit "jika X gagal, berhenti dan jangan merge"?
- **Pola Perbaikan (Resep):** Tanamkan kebijakan *fail-closed* di dokumen alur atau panduan utama, wajibkan gerbang validasi (contoh: *exit code* wajib 0 sebelum membuat PR).
- **Bukti / Risiko:** Kerusakan data persisten atau korupsi *state* sistem yang jauh lebih sulit diperbaiki.

### C-06: Bengkak Aset di Repo Induk
- **Gejala:** Folder sistem yang diletakkan di repo meta (rawat inap) atau branch perbaikan memuat commit berisi aset raksasa (gambar, video, DB) atau riwayat yang panjang tak berujung, yang pada akhirnya ikut tersimpan ke dalam penyimpanan `.git` repo induk.
- **Cara Periksa (Diagnosis):** Sebelum rawat inap: cek ukuran folder + daftar aset berat (gambar/video/data) — bila ada dan pemilik tidak bermaksud membawanya ke repo meta, panggung suntik yang dipakai (keputusan + alasan dicatat di laporan diagnosis). Selama run suntik: cek kebijakan penyalinan/perbaikan — apakah sistem langsung mengkopi semua direktori secara membabi-buta termasuk file biner statis?
- **Pola Perbaikan (Resep):** Rawat inap: lingkup folder tamu diputuskan pemilik (butir Tahap A langkah 6); aset berat yang sengaja tidak dibawa dicatat di laporan diagnosis. Suntik: mekanisme perbaikan dibatasi pada berkas yang disentuh rencana — tidak pernah kopi buta seluruh pohon.
- **Bukti / Risiko:** Kapasitas repo bengkak secara permanen (bloat), memperlambat setiap operasi `git clone` dan `git fetch`.

### C-07: Dokumen Pengganti yang Tidak Dipensiunkan (*superseded-but-live*)
- **Gejala:** Dua dokumen **sama-sama hidup** dan memberi instruksi/angka yang bertentangan untuk hal yang sama — dokumen lama (pra-standar) tetap ada tanpa penanda apa pun, dokumen baru sudah jadi rujukan resmi. Pembaca yang kebetulan membuka yang lama mengikuti aturan usang. Tidak ada error, tidak ada test yang gagal; yang rusak adalah **keputusan** (misal "yang masuk repo hanya satu berkas" vs "copy seluruh folder"; "7 template" vs 10 template nyata; "8.1M/52 dirs" vs 26M/56 dirs nyata).
- **Cara Periksa (Diagnosis):** (1) Daftar semua `.md` di tingkat sistem (tanpa rekursi ke vendor) → tandai yang bukan dokumen aktif (arsip audit, catatan pribadi, pedoman lama). (2) Untuk tiap pasangan dokumen bertopik sama (cara pakai/template, jumlah template, ukuran folder, daftar dokumen wajib) bandingkan angka + instruksinya → selisih = temuan. (3) Periksa 12 baris pertama tiap dokumen non-aktif: wajib ada penanda arsip/digantikan + penunjuk dokumen yang berlaku. (4) Bandingkan daftar dokumen wajib di manifest dengan kenyataan di folder (jumlah + nama). (5) Jalankan validator sistem → bila tidak ada satu pun cek yang bisa menangkap (1)-(4), itu sendiri temuan (celah gerbang). (6) Tanyakan siapa yang menemukan cacat ini: bila **pemilik/pengguna**, bukan validator — gerbang terbukti tidak menangkapnya.
- **Pola Perbaikan (Resep):** (a) **Pensiunkan, jangan hapus** — sisipkan penanda di kepala berkas ("VERSI LAMA — SUDAH DIGANTIKAN, JANGAN DIIKUTI") + tabel koreksi per topik + penunjuk dokumen berlaku; isi asli di bawah penanda tidak disentuh (append-only, Kebijakan Lebur). (b) Segarkan manifest jadi satu-satunya daftar dokumen wajib yang benar (versi, jumlah template, ukuran terukur, acceptance, Log Keputusan). (c) **Tanam cek di validator**: penanda arsip wajib ada; klaim "hanya satu berkas yang masuk repo" dilarang di dokumen aktif; klaim jumlah direktori dibandingkan dengan **hitungan nyata** (bukan angka beku → tidak bisa basi); rujukan ber-backtick ke area yang tidak ikut keluar dari folder dilarang; atribut wajib template diperiksa. (d) **Buktikan dengan uji mutasi** — rusak satu per satu (hapus penanda, ubah angka, suntik klaim lama, hapus atribut template) dan pastikan validator GAGAL; gerbang yang hijau tanpa uji mutasi bisa jadi hijau karena tidak memeriksa apa pun (pola F-8). (e) Tambah acceptance test "copy folder → repo standalone" sebagai **bukti perilaku**, bukan hanya bukti baca dokumen.
- **Bukti / Risiko:** Run klinik ke-2 pada Sistem Building Aplikasi (2026-09-16) menemukan 11 Critical + 9 Minor; **9 di antaranya satu keluarga ini**: `PANDUAN_PEMAKAIAN.md` (158 baris, pra-standar) hidup tanpa penanda dan bertentangan dengan `PANDUAN_PENGGUNA.md`; `SYSTEM_MANIFEST.md` (dokumen wajib) menyebut "7 template" padahal ada 10 dan "8.1M/52 dirs" padahal nyata 26M/56 dirs/1.802 berkas; skills/README.md kontradiktif **di dalam dirinya sendiri** (header vs § Registrasi, "hemat 85%" tanpa pembanding, ukuran per-skill basi, folder `banner` yang tidak ada, 224K vs 16K nyata, 18 vs 17 sub-skill); ringkasan cadangan basi total; `STATUS.md` bernarasi run "sedang berjalan" + "Merge PR (G-Final)" padahal auto-merge ditolak; _sistem/templates/ROADMAP.md mencontohkan bentuk task singkat yang justru dilarang AGENT_SYSTEM.md. **Dampak nyata: pemilik ragu memakai sistemnya sendiri dan hampir mengikuti pedoman usang** — temuan awal datang dari pemilik, bukan dari validator. Risiko bila dibiarkan: agent di repo baru kehilangan 10 template + `skills/` + `PROFIL_PENGGUNA.md` (pedoman usang menyuruh copy 1 berkas) → Fondasi pincang; angka yang berbeda antar dokumen mengikis kepercayaan pemilik pada seluruh repo. **Celah kit:** Kebijakan Lebur melarang overwrite/hapus tanpa izin (benar) tetapi tidak ada butir yang mewajibkan dokumen yang digantikan diberi penanda arsip — usulan: penanda arsip + "satu sumber angka terukur" masuk Kontrak Tanaman/planting checklist dan ke validator target.

---

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-13 | Seed awal katalog dibuat (C-01 sampai C-06) | Menyediakan tolok ukur awal bagi agent klinik untuk melakukan diagnosis sistem target (Langkah 3 rencana kerangka). |
| 2026-09-16 | **C-07 (*superseded-but-live*) ditambahkan** sebagai PANEN Tahap F run klinik ke-2 pada Sistem Building Aplikasi: 9 dari 20 temuan run itu satu keluarga (pedoman usang hidup tanpa penanda, manifest 7 vs 10 template + 8.1M/52 dirs, skills/README.md kontradiktif di dalam dirinya, ringkasan cadangan basi, STATUS narasi run lewat, template ROADMAP mencontohkan bentuk yang dilarang) | Perawatan sistem adalah run klinik; butir di luar C-01…C-06 dipromosikan lewat Aturan Promosi butir 4 (katalog + laporan ke pemilik). Resepnya mencakup penanda arsip append-only, penyegaran manifest, 5 cek validator baru, dan **uji mutasi 5/5** sebagai bukti gerbang benar-benar menyala. Celah kit yang ketahuan: Kebijakan Lebur melindungi dari overwrite/hapus tetapi tidak mewajibkan penanda arsip pada dokumen yang digantikan — usulan masuk Kontrak Tanaman/planting checklist |
| 2026-09-14 UTC / 15 Sep WIB | C-06 diberi redaksi ulang: "Penyumbatan Bengkel / Bengkak Aset" → "Bengkak Aset di Repo Induk"; aturan promosi butir 1 disinkron ke dua panggung baru | K-11 menghapus panggung bengkel; polanya (bengkak aset di repo induk) tetap valid dan kini diikat ke kedua panggung yang ada (folder rawat inap yang diletakkan di meta + run suntik yang melakukan kopi buta) |
