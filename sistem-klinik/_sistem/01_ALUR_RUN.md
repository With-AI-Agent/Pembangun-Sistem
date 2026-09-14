# 01 — Alur Run (Siklus Kunjungan Klinik)

> Aturan inti Sistem Klinik: SATU RUN = SATU KUNJUNGAN ke SATU sistem target, dengan tahapan yang sama setiap kali, dua gerbang Besar yang tidak bisa ditawar, dan dua panggung (suntik = default, bengkel = pengecualian) yang menghasilkan artefak identik.
> Sumber keputusan: 00_RENCANA_KERANGKA.md di folder ini (di-merge via PR #43, commit `a4331f8`, 13 Sep 2026) + Discovery Level-0 11 Sep 2026 + koreksi pemilik K-9/K-10 13 Sep 2026. Provenance prinsip: dokumen-dokumen meta di folder induk repo ini — aturan yang benar-benar dipakai saat run adalah SELURUHNYA di dokumen ini dan turunannya di kit (folder sistem harus tetap berfungsi penuh saat dibawa keluar).
> **Status berlaku:** dokumen ini menstandarkan desain run. RUN NYATA baru sah setelah kit pertama dirakit (06_RITME_KIT) dan Tahap di manifest naik ke `siap-pakai`. Fail-closed: bila kit tidak ada, tidak ada run — lapor, jangan improvisasi.

---

## Daftar Isi

1. [Aturan Dasar Run](#1-aturan-dasar-run)
2. [Peta Siklus](#2-peta-siklus)
3. [Tahap A — Pendaftaran](#3-tahap-a--pendaftaran)
4. [Tahap B — Diagnosis](#4-tahap-b--diagnosis)
5. [G-Rencana (Gerbang 1)](#5-g-rencana-gerbang-1)
6. [Tahap C — Tindakan](#6-tahap-c--tindakan)
7. [Tahap D — Verifikasi](#7-tahap-d--verifikasi)
8. [Tahap E — Catatan](#8-tahap-e--catatan)
9. [Tahap F — Panen](#9-tahap-f--panen)
10. [G-Final (Gerbang 2)](#10-g-final-gerbang-2)
11. [Peleburan & Penyerahan](#11-peleburan--penyerahan)
12. [Adaptasi Dua Panggung](#12-adaptasi-dua-panggung)
13. [Aturan Berhenti Fail-Closed](#13-aturan-berhenti-fail-closed)
14. [Batasan Platform](#14-batasan-platform)
15. [Definisi Selesai 1 Run](#15-definisi-selesai-1-run)
16. [Log Keputusan](#16-log-keputusan)

---

## 1. Aturan Dasar Run

- **1.1 Sasaran run adalah KEADAAN, bukan umur (K-7).** Target boleh: (a) lama pra-meta yang belum pernah dirawat, (b) lama yang sudah jadi tapi belum dipakai, (c) baru pasca-meta yang mau ditingkatkan/diksa ulang. Sistem yang lahir lengkap tidak "tanam dua kali" — dia dapat jalur kontrol + upgrade yang sama; idempotensi (butir 1.3) yang menanganinya.
- **1.2 Dua panggung, satu siklus.**

  | Panggung | Di mana agent kerja | Kapan dipilih | Jejak di repo meta |
  |---|---|---|---|
  | **Rawat jalan (suntik) — DEFAULT** | repo TARGET | hampir selalu | NOL byte — kit tidak pernah di-commit ke mana pun; histori hidup di git & PR target |
  | **Rawat inap (bengkel) — PENGECUALIAN** | repo META, target menginap | rombakan struktural berat yang butuh alat/arsip meta, atau target sedang kecil | salinan tamu hidup HANYA di branch kerja; PR hanya mengangkut laporan |

  Suntik adalah default karena tidak menaruh apa pun di repo meta. Bengkel pengecualian ber-kuota: branch yang di-push tetap menempati store repo selama branch/PR hidup (K-9) — makanya salinannya seadanya, aset tidak ikut, dan branch dihapus setelah pemulangan.
- **1.3 Idempoten dan anti-kit-usang.** Run SELALU dibuka dengan membaca REKAM-KLINIK target (atau padanannya — butir 4.2) SEBELUM audit apa pun: yang sudah terpasang diverifikasi, bukan ditanam dua kali; yang pernah DITOLAK pemilik tidak ditawari ulang tanpa alasan baru; bila cap versi di rekam lebih tua dari versi kit saat ini, tawaran "naik ke vX" WAJIB masuk rencana (pemilik boleh menolak; penolakan dicatat). Sebaliknya — bila versi kit yang dibawa LEBIH TUA dari cap di rekam (kit usang; rekam direkam kit lebih baru), BERHENTI fail-closed: dilarang merawat dengan kit yang lebih tua dari yang pernah merawat target; wajib sinkron/naikkan kit lebih dulu (06_RITME_KIT §2) sebelum Tahap B dilanjutkan, dan kejadian itu dicatat di rekam.
- **1.4 Katalog Cacat = satu-satunya tolok ukur.** Diagnosis tidak menebak dari feeling: setiap butir katalog diperiksa satu per satu dengan cara periksa yang tertulis di katalog itu (02_KATALOG_CACAT). Temuan yang tidak ada di katalog tetap sah — dia jadi kandidat panen (Tahap F) dan, setelah disetujui, butir katalog baru.
- **1.5 Tidak ada mode "agent percaya diri lanjut".** Dua gerbang (G-Rencana, G-Final) + per-item untuk overwrite dan install kapabilitas; semuanya dijawab pemilik. Kecil yang boleh jalan tanpa jeda dibatasi eksplisit di butir 6.4.
- **1.6 Format rekam dua panggung identik.** Laporan diagnosis, rencana, catatan tindakan, dan verifikasi memakai format yang sama apa pun panggungnya — supaya hasil bengkel dievaluasi dengan mata yang sama dengan hasil suntik.
- **1.7 Satu run, satu target.** Tidak ada kerja multi-repo paralel di satu run. Target kedua = run kedua.

## 2. Peta Siklus

```
A  PENDAFTARAN        identitas + keadaan target; baca REKAM-KLINIK dulu
B  DIAGNOSIS          audit terhadap katalog cacat + kontrak tanaman; read-only
   ── G-RENCANA (Besar — pemilik; borongan bernomor K-10) ──
C  TINDAKAN           eksekusi rencana per item, metode Kebijakan Lebur
D  VERIFIKASI         per item + alat portabel kit + konsistensi rujukan target
E  CATATAN            REKAM-KLINIK ditulis ke target + cap versi kit (draft final)
F  PANEN              cacat baru / celah aturan / ide kit → usulan balik ke meta
   ── G-FINAL (Besar — pemilik: isi perubahan + verifikasi + panen + izin peleburan) ──
   PELEBURAN &        kit hilang dari target; PR target tanpa auto-merge
   PENYERAHAN         (bengkel: pulangkan + PR meta di-close/merge laporan + hapus branch)
```

**Urutan E–F–G-Final–Peleburan (rekonsiliasi yang dilaporkan):** tabel Titik Penguncian rencana dan jangkar konsistensi #5 menyatakan eksplisit G-Final berada **sebelum peleburan kit + PR**; diagram ringkas di rencana menaruh peleburan lebih awal. Aturan gerbang eksplisit yang menang: rekam klinik (E) dan usulan panen (F) harus SUDAH ADA saat pemilik menilai G-Final, dan kit baru hilang SETELAH disetujui — supaya koreksi G-Final masih bisa dieksekusi tanpa merakit ulang. Catat di Log Keputusan butir 16.

## 3. Tahap A — Pendaftaran

Tujuan: tahu DI MANA dan KADALUARSA target, sebelum memeriksa apa pun. Read-only total.

1. **Identitas target:** nama, lokasi repo, platform utama pemakaiannya (lmarena / Claude Code / Antigravity / lain — dari manifest atau pemakaian nyata), punya tidaknya git remote dan akses `gh`.
2. **Keadaan pemakaian:** dipakai aktif / sudah jadi tapi belum dipakai / dalam pembangunan (K-7: ketiganya sah sebagai target).
3. **Baca REKAM-KLINIK (idempotensi):** versi kit terakhir yang pernah merawat, tanggal run, item yang pernah DITOLAK pemilik + alasannya, rollback yang pernah terjadi. Bila target belum pernah dirawat → rekam belum ada; catat "kunjungan pertama".
4. **Cap vs versi kit:** bila cap di rekam < versi kit saat ini → tandai "tawaran naik versi" sebagai item wajib rencana (butir 1.3). Bila cap di rekam > versi kit yang dibawa (kit usang) → berhenti fail-closed (butir 1.3): wajib sinkron kit dulu, Tahap B tidak dilanjutkan dengan kit lebih tua dari yang pernah merawat.
5. **Konvensi target:** bahasa dokumen, gaya penamaan berkas, struktur folder, ada-tidaknya padanan lokal untuk rekam/log/status — ini yang menentukan bentuk artefak tanaman (Kebijakan Lebur: konvensi target menang).
6. (Bengkel saja) **Estimasi ukuran + daftar exclude:** aset besar (gambar/video/data) TIDAK ikut menginap; daftarnya ditulis di laporan diagnosis (K-9).

Hasil tahap: blok "Keadaan Target" di laporan diagnosis (format 4.5).

## 4. Tahap B — Diagnosis

Audit menyeluruh, READ-ONLY: tidak satu byte pun ditulis ke target sebelum G-Rencana lolos. Catatan kerja tinggal di folder kit/workspace.

### 4.1 Empat pemeriksaan wajib

1. **Katalog cacat, butir demi butir** — setiap butir katalog: jalankan cara periksa yang tertulis di situ → status ADA/TIDAK di target ini + bukti konkret (berkas + baris/kondisi). Temuan di luar katalog dicatat sebagai "kandidat butir baru".
2. **Kontrak tanaman (04_KONTRAK_TANAMAN)** — untuk tiap butir syarat "sistem terawat": apakah target sudah punya padanannya? Yang sudah ada → rencananya EXTEND, bukan dokumen kembar; yang belum → kandidat tanam.
3. **Fungsi kurang optimal** — mekanisme ada tapi bekerja buruk (panduan usang, prompt di bawah standar, proses yang selalu macet). Sumber sinyal: keluhan pemilik saat pendaftaran, rekam klinik sebelumnya, pengamatan langsung.
4. **Peluang kapabilitas** — kebutuhan yang seharusnya dilayani plugin/skill/alat (riset internet, prosedur lengkap di 05_TAWARAN_KAPABILITAS). Di tahap diagnosis cukup arah kebutuhannya; tawaran lengkap disusun untuk borongan.

### 4.2 Rekam klinik sebagai dasar

Bila REKAM-KLINIK ada tapi formatnya bukan bawaan kit (target lama dengan konvensi sendiri): baca sebagai padanan sah, dan catat padanannya di laporan — jangan paksa format kit ke target yang sudah punya cara (konvensi target menang; Kebijakan Lebur 03).

### 4.3 Bila target "sehat"

Run kontrol yang hasilnya "semua butir lolos, tidak ada yang perlu diubah" adalah hasil sah: rencana berisi verifikasi + tawaran naik-versi bila cap tua + panen. Tidak ada kewajiban memaksakan perubahan.

### 4.4 Aturan berhenti di diagnosis

Bila pemeriksaan tidak bisa dilakukan (target tidak bisa dibaca, kit rusak, rekam kontradiktif dengan kenyataan) → BERHENTI, laporkan (bagian 13). Jangan diagnosis separuh lalu lanjut.

### 4.5 Format LAPORAN DIAGNOSIS

```markdown
# LAPORAN DIAGNOSIS — <nama target> (run <tanggal>, kit v<versi>, panggung <suntik/bengkel>)

## 1. Keadaan Target (hasil Tahap A)
[identitas, keadaan pemakaian, konvensi, (bengkel) ukuran + daftar exclude]

## 2. Bacaan REKAM-KLINIK
[run terakhir, versi, item ditolak + alasan, rollback; atau "kunjungan pertama"]

## 3. Temuan Katalog Cacat
| ID katalog | Gejala di target | Bukti (berkas/kondisi) | Risiko | Status |

## 4. Kepatuhan Kontrak Tanaman
| Butir | Padanan di target | Kondisi | Disposisi usulan (extend/tanam baru/cukup) |

## 5. Fungsi Kurang Optimal
[daftar + dampaknya]

## 6. Peluang Kapabilitas (arah — tawaran lengkap di borongan)
[kebutuhan → arah solusi]

## 7. (Bengkel) Exclude & Estimasi Ukuran
[daftar aset yang tidak menginap + alasan]

## 8. Tidak Bisa Diverifikasi
[apa yang tidak terperiksa dan kenapa — WAJIB diisi "tidak ada" bila lengkap]
```

### 4.6 Format RENCANA PERUBAHAN

```markdown
# RENCANA PERUBAHAN — <nama target> (mengacu laporan diagnosis di atas)

## Daftar item (borongan bernomor — K-10)
| # | Jenis | Lokasi di target | Ringkasan | Kategori | Risiko bila jalan | Alternatif lokal | Status keputusan |

Jenis: tanam-baru / extend / upgrade / naik-versi / hapus (hapus & overwrite = Besar, selalu per-item).
Kategori: Besar (G-Rencana + per-item bila ditunda ke borongan eksekusi) / Kecil (jalan + lapor).

## Slot usulan pemilik
"Ada yang kamu mau tapi belum ada di daftar?" — dijawab sebelum eksekusi.

## Tidak akan dilakukan
[item dari rekam klinik yang dulu DITOLAK — muncul lagi hanya bila ada alasan baru, dinyatakan eksplisit]
```

## 5. G-Rencana (Gerbang 1)

- **Apa yang dikunci:** laporan diagnosis + rencana perubahan LENGKAP. Tidak ada penulisan ke target sebelum pemilik menyetujui rencananya — apa pun panggungnya.
- **Bentuk tanya = borongan bernomor (K-10):** seluruh item Besar ditanyakan sekaligus dalam daftar bernomor lengkap — rencana besar dibagi beberapa pesan berturut (maks ±5 butir per pesan) tapi tetap SATU rangkaian yang selesai SEBELUM eksekusi; tidak ada mode "jalan sedikit, tanya lagi". Tiap item memuat fungsi/tujuan/alasan; tiap tawaran kapabilitas wajib memuat tujuh komponen: APA → fungsi/tujuan → mengapa target INI butuh → cara pasang → risiko bila pasang → alternatif lokal → konsekuensi bila tidak. Setiap borongan ditutup slot usulan pemilik.
- **Jawaban dicatat persis** (terima/tolak/tunda + usulan pemilik) → masuk REKAM-KLINIK; penolakan tidak ditawari ulang tanpa alasan baru.
- **Hasil gerbang:** rencana disetujui utuh / disetujui dengan koreksi (dieksekusi dulu, tidak perlu gerbang ulang bila koreksinya mengecilkan ruang kerja) / ditolak (run selesai tanpa tindakan; hasil diagnosis tetap dicatat sebagai usulan panen bila ada).
- Fail-closed: jawaban ambigu → tanya satu kali klarifikasi dalam borongan yang sama; tidak boleh ditafsir sendiri.

## 6. Tahap C — Tindakan

1. **Eksekusi rencana per item, urut nomor.** Satu item tuntas (ditulis + tercatat) baru item berikut — kesalahan kecil tidak sempat menular.
2. **Metode tanam mengikuti Kebijakan Lebur (03_KEBIJAKAN_LEBUR):** cek padanan → extend dulu, baru create; overwrite/hapus hanya item yang sudah diizinkan eksplisit; artefak ikut konvensi target; istilah klinik tidak menular.
3. **Item Besar yang diperiksa di G-Rencana tidak ditanya ulang** di tengah C. Item BARU yang muncul di luar rencana → BERHENTI sebentar, diborong ulang (daftar bernomor susulan, format K-10 sama), lanjut sekali jalan setelah terjawab.
4. **Kecil boleh jalan tanpa jeda (6.4):** tanam file baru non-destruktif yang sudah ada di rencana, tulis log, isi STATUS, verifikasi read-only — jalan + lapor di G-Final.
5. **Catatan tindakan:** tiap item dicatat (apa, di mana, metode, hasil) — bahan verifikasi (D) dan isi rekam klinik (E).
6. **Kit tidak pernah masuk git target.** Selama run: folder kit di `.gitignore` kerja (bila target pakai git) atau di luar pohon yang di-commit; diverifikasi ulang di peleburan.
7. **Log run berkelanjutan:** selama run, agent memelihara LOG_SESI run (bentuk: TEMPLATE-LOG-SESI-TARGET dari kit; lokasi & bahasa ikut konvensi target / branch kerja runtime). Ini syarat pemulihan bila sesi crash di tengah C — bukan birokrasi (bagian 14).

## 7. Tahap D — Verifikasi

1. **Per item:** setiap item rencana dicek ulang terhadap ringkasannya sendiri — ada di lokasi yang dijanjikan, isinya seperti yang disetujui, metodenya sesuai (extend tidak jadi kembaran; overwrite hanya yang diizinkan).
2. **Alat portabel kit** (di `kit/alat/`, stdlib-only, tidak tahu bentuk repo): cek field STATUS deterministik (`**Pekerjaan belum tersimpan:** Tidak ada` tepat satu kali, `Waktu pembaruan` berformat `YYYY-MM-DD — <peristiwa>`), cek rujukan internal target, cek format rekam. Hasil ditempel mentah ke laporan verifikasi — tanpa diringkas jadi klaim.
3. **Konsistensi rujukan internal target:** dokumen yang disentuh tidak boleh meninggalkan rujukan usang (nama berkas/istilah yang berubah ikut diperbarui di tempat yang merujuknya).
4. **Uji idempotensi mental:** "bila kit ini dijalankan LAGI besok, item mana yang akan terbaca sudah-terpasang?" — jawabannya harus: semua item run ini. Yang tidak, berarti ada yang ditanam tidak tercatat → kembali ke C untuk item itu.
5. **Gagal verifikasi:** perbaiki dalam lingkup item itu + catat; gagal berulang → naikkan ke pemilik (bagian 13), jangan paksa lolos.

## 8. Tahap E — Catatan

REKAM-KLINIK final ditulis KE TARGET (TEMPLATE-REKAM-KLINIK dari kit; nama berkas ikut konvensi target bila target punya padanan):

- tanggal run, panggung, **cap versi kit** (yang dipakai run ini), pelaksana;
- temuan (ringkas) + daftar item perubahan + status keputusan per item;
- **yang DITOLAK pemilik + alasannya** (bahan anti-tawar-ulang run berikutnya);
- rollback yang berlaku (mekanisme apa dinonaktifkan via commit/PR apa);
- pelengkapnya: STATUS unit target diperbarui dengan field deterministik, log run ditutup rapi.

Rekam ini adalah memori jangka panjang target — run berikutnya membacanya PERTAMA (butir 1.3). Draft rekam + laporan verifikasi + usulan panen diserahkan bersamaan ke G-Final.

## 9. Tahap F — Panen

Panen wajib di SETIAP run — ini mekanisme evolusi kit (K-8), bukan niat.

- **Yang dipanen:** cacat baru yang belum ada di katalog (diberi nama + gejala + cara periksa + pola perbaikan + risiko), celah aturan kit yang ketahuan saat run, ide perbaikan kit/alur, kemampuan bengkel yang terbukti perlu dipromosikan portabel masuk kit.
- **Nihil panen adalah nilai sah** — asal DITULIS eksplisit: "nihil, karena <alasan>". Diam tanpa laporan tidak sah.
- Panen TIDAK mengangkut konten target — yang mengalir balik ke meta hanya temuan dan usulan, netral-domain (nama target boleh disebut sebagai sumber di laporan, isi privat target tidak ikut).
- Keputusan atas panen ikut G-Final (satu gerbang, dua objek keputusan).

## 10. G-Final (Gerbang 2)

- **Apa yang dikunci:** (1) isi perubahan selesai + hasil verifikasi per item + keluaran mentah alat portabel; (2) REKAM-KLINIK draft + cap versi; (3) usulan panen; (4) izin peleburan & penyerahan.
- **Bentuk:** satu penyerahan berpagar (laporan + bukti) — pemilik review isi lengkap. Sisa keputusan Besar yang belum terjawab (harusnya tidak ada — semua diborong sejak G-Rencana) ditutup DI SINI dalam satu borongan terakhir.
- **Hasil gerbang:** lanjut peleburan + penyerahan sesuai keputusan; atau koreksi → kembali ke tahap terkait dengan catatan; atau henti-run (hasil yang sudah ada tetap dicatat di rekam sebagai run setengah/tunda — jujur, bukan gagal sembunyi).
- Fail-closed: tanpa persetujuan G-Final, tidak ada peleburan, tidak ada PR.

## 11. Peleburan & Penyerahan

### 11.1 Suntik (rawat jalan)

1. Peleburan kit: folder kit hilang dari workspace target; `.gitignore` kerja dibersihkan dari entri run; TIDAK ada sisa berkas kit di pohon git target (dicek `git status` bersih dari kit).
2. PR dibuka di repo target: memuat perubahan tertanam + rekam klinik + STATUS; deskripsi lengkap (apa, gerbang yang sudah dilewati, item ditolak); **TANPA auto-merge — merge = keputusan pemilik penuh.**
3. Panen yang disetujui → PR terpisah ke sistem-klinik di repo meta (ke katalog/kit sesuai jenisnya) — bisa jalan di sesi meta sendiri; catat tautannya di rekam run.
4. Checklist akhir = bagian 15.

### 11.2 Bengkel (rawat inap)

1. **Pemulangan hasil:** patch/download-workspace diserahkan ke pemilik untuk diterapkan ke repo target asli (bengkel TIDAK pernah push ke repo target langsung dari meta).
2. **PR meta di-close** setelah pemulangan — KECUALI ada bagian yang memang jadi milik meta (laporan ke `_arsir-run/`, temuan untuk katalog): PR itu hanya berisi berkas laporan, boleh di-merge pemilik.
3. **Hygiene pasca-pemulangan (K-9):** salinan tamu dihapus dari `_bengkel/<nama>/`; branch kerja DIHAPUS — keputusan sadar pemilik, dicatat, bukan diam-diam; PR tetap tinggal sebagai catatan permanen run.
4. Kebijakan Lebur berlaku penuh di bengkel: apa pun yang ditanam ke tamu ikut konvensi tamu; overwrite tetap per-item.
5. Branch yatim (sesi mati sebelum pemulangan): dilaporkan, TIDAK dihapus diam-diam.

## 12. Adaptasi Dua Panggung

| Aspek | Suntik (default) | Bengkel (pengecualian) |
|---|---|---|
| Lokasi kerja | repo target, workspace sendiri | repo meta, `_bengkel/<nama>/` — hidup hanya di branch kerja |
| Akses alat berat meta | tidak ada — hanya alat portabel kit | penuh (tools & arsip meta boleh dipakai ke salinan tamu) |
| Yang masuk git | perubahan tertanam + rekam klinik → PR target | HANYA berkas laporan → PR meta (close/merge-laporan); salinan tamu TIDAK pernah ke main |
| Merge/di-discharge | pemilik merge PR target | pemilik close PR meta setelah pemulangan (+ hapus branch, keputusan sadar) |
| Pemulangan hasil | langsung di tempat (repo target) | patch / download-workspace → diterapkan pemilik ke repo target |
| Kapan dipilih | hampir selalu | rombakan berat butuh alat meta; atau target kecil; kuota-bijaksana (K-9) |
| Format artefak | identik dua panggung (butir 1.6) | identik dua panggung (butir 1.6) |

Tahap A–F sama persis di kedua panggung; yang berbeda hanya mekanisme penempatan kerja dan penyerahan di atas.

## 13. Aturan Berhenti Fail-Closed

Semua kegagalan arahnya AMAN: tidak ada tanam setengah jadi, tidak ada overwrite tanpa izin, kit tidak tertinggal di git target, tidak ada klaim selesai palsu. **BERHENTI + LAPORKAN pemilik (jangan improvisasi) bila:**

1. Dokumen aturan / bagian kit yang dibutuhkan tidak ada, rusak, atau bertentangan dengan dokumen lain → lapor kontradiksinya; dokumen aktif + keputusan terbaru yang disetujui menang; konflik tetap dilaporkan.
2. REKAM-KLINIK (atau padanan) menunjukkan run lain masih berjalan / keadaan setengah jadi yang tidak bisa dipastikan → jangan mulai item baru; tawarkan run pemeriksaan-pemulihan.
3. Gerbang tidak terjawab atau jawabannya ambigu → satu klarifikasi dalam borongan yang sama; tidak terjawab juga → run berhenti di gerbang itu (boleh dilanjutkan sesi lain dari log).
4. Verifikasi gagal berulang pada item yang sama → naikkan dengan bukti, jangan paksa lolos, jangan perbaiki di luar lingkup item.
5. Target tidak bisa dibaca/ditulis dengan aman (akses hilang, repo rusak) → henti; tidak ada perbaikan spontan di luar rencana.
6. PR run sudah merged/closed dan masih ada kerja tersisa → sesi ini tidak bisa push lagi (fakta platform 14.2): kerja berlanjut di SESI BARU dari main; jangan buat file baru yang berharap bisa di-push.
7. Permintaan pemilik di luar rencana yang sudah disetujui → diborong ulang (K-10) SEBELUM dieksekusi, kecuali eksplisit darurat dan non-destruktif.

Laporan berhenti selalu memuat: di tahap apa, apa yang sudah aman (ter-commit/ter-push), apa yang tidak, dan opsi lanjutan — supaya sesi baru bisa memulihkan tanpa menanya ulang.

## 14. Batasan Platform

- **Dipakai via lmarena?** Ya — lingkungan utama target. Runtime lain (Claude Code / Antigravity, jarang): aturan di dokumen ini netral-platform; bagian lmarena di bawah menjadi aktif-opsional sesuai environment target.

**Tiga fakta platform (kausal — "tidak bisa", bukan "jangan"):**

1. **Branch kerja otomatis.** Sesi di repo target (maupun meta) bekerja di branch `arena/...` yang dibuat otomatis — `main` tidak tersentuh sampai merge. Run selalu memverifikasi branch aktif di awal, tidak pernah mengasumsikan `main`.
2. **Push dicabut setelah merge/close.** Setelah PR di-merge atau di-close, sesi TIDAK BISA push lagi. Konsekuensi run: SEMUA commit + rekam + PR harus selesai SEBELUM pemilik me-merge; hasil bengkel dipulangkan sebelum PR di-close; setelah merge, kerja lanjutan = sesi baru dari main (file pasca-merge terjebak di sesi — workaround satu-satunya: download workspace).
3. **Sesi bisa crash kapan saja.** Karena itu log run berkelanjutan (6.7) + REKAM-KLINIK (E) + STATUS deterministik bukan pelengkap — mereka adalah mekanisme pemulihan yang menjadikan run bisa dilanjutkan sesi lain tanpa menanya ulang. Mekanisme inilah barang tanam utama klinik ke target (Kontrak Tanaman); sistem klinik menerapkannya pada dirinya sendiri lebih dulu.

**Implikasi khusus bengkel:** salinan tamu hanya ada di branch (fakta 1); PR meta di-close pasca-pemulangan sebelum akses push hilang (fakta 2); log run di meta mengikuti aturan 10_LOG_SESI.md folder ini (fakta 3).

## 15. Definisi Selesai 1 Run

Satu run dianggap SELESAI hanya bila SEMUA lolos:

- [ ] Semua item rencana yang disetujui terpasang dan terverifikasi (keluaran verifikasi tercatat, bukan klaim);
- [ ] REKAM-KLINIK tertulis di target dengan cap versi kit + daftar keputusan (termasuk yang ditolak);
- [ ] Folder kit hilang dari git target (suntik) — atau salinan tamu dihapus + branch dihapus pasca-pemulangan (bengkel);
- [ ] PR target terbuka TANPA auto-merge (suntik) — atau patch diserahkan + PR meta di-close/merge-laporan (bengkel);
- [ ] Panen dilaporkan (termasuk "nihil, karena …");
- [ ] Merge/discharge dilakukan pemilik — tanpa kecuali.

Tidak ada status "selesai" sebelum checklist ini lolos. Run yang berhenti di tengah (crash/gerbang) berstatus jujur di log + rekam: "berhenti di <tahap>, dilanjutkan <di mana>".

## 16. Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-13 | Dokumen ditulis (tahap kerangka→isi; urutan Langkah 1 rencana) | Ditetapkan 00_RENCANA_KERANGKA.md "Langkah setelah rencana merge"; prinsip sudah diputuskan di Discovery Level-0 (K-1…K-10) — dokumen [ATURAN], bukan [GENERATOR] |
| 2026-09-13 | Urutan kanonik: E Catatan → F Panen → G-Final → peleburan+PR (diagram rencana tidak diikuti mentah) | Titik Penguncian rencana + jangkar konsistensi #5 eksplisit "G-Final sebelum peleburan kit + PR" (2 pernyataan vs 1 diagram ringkas); menegakkan gerbang lebih aman: koreksi G-Final masih bisa dieksekusi karena kit belum lebur; rekonsiliasi dilaporkan, bukan diam-diam |
| 2026-09-13 | G-Rencana = satu rangkaian borongan bernomor K-10 yang selesai sebelum eksekusi; item baru di C diborong susulan sekali jalan | Sintesis K-3 (dua gerbang + per-item) dan K-10 (anti bertele-tele, anti 10-sekaligus): borongan bergelombang ≤±5 butir, tanpa cicil-tanya di tengah run |
| 2026-09-14 | Butir 1.3 + Tahap A langkah 4 dilengkapi arah sebaliknya: kit yang dibawa LEBIH TUA dari cap rekam → berhenti fail-closed, wajib sinkron kit dulu | Hasil pre-audit acceptance AT-KL-02 (Langkah 7): aturan lama hanya mengatur cap < kit (naik versi); arah kit < cap belum tertulis — tanpa kalimat ini agent bisa menurunkan versi perawatan target tanpa aturan yang melarang |
| 2026-09-14 | Koreksi pasca-review putaran 1 PR #51: kalimat anti-kit-usang KINI BENAR-BENAR ada di §1.3 (edit pertama 14 Sep hilang karena kesalahan proses — dua edit paralel ke berkas ini, tulisan kedua menimpa yang pertama; terdeteksi reviewer lewat byte-diff); seluruh enam stamp `kit/aturan/*` disinkron `versi-kit 0.1.2` | Review independen putaran 1 MERAH (temuan F-1 klaim≠artefak, F-3 stamp basi); diterima pemilik + dijalankan penulis; verifikasi pakai token tak ambigu + daftar hunk, bukan token yang muncul di teks lama |
