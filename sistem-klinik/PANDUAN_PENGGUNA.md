---
agent_instruction: IGNORE for execution — USER GUIDE ONLY
user_guide_only: true
folder: sistem-klinik/
purpose: Pegangan pengguna Sistem Klinik — dokumen ini untuk manusia/pengguna, bukan instruksi eksekusi agent; agent membacanya hanya jika diminta eksplisit oleh pengguna. Prompt eksekusi lintas-sesi tetap sah ditempel dari bagian 2–3 (sumber: PROMPT_ENTRI_UNIVERSAL.md).
---

# Panduan Pengguna — Sistem Klinik

> Pegangan pengguna sistem ini (W-01). Struktur mengikuti template pegangan meta (provenance: PANDUAN_PENGGUNA_TEMPLATE.md di _meta — aturan yang benar-benar dipakai sudah disalin/diturunkan ke file ini). Saat sistem masih tahap kerangka, bagian 4–7 sengaja ringkas dan diperluas saat dokumen _sistem/ jadi; bagian 2–3 final sejak hari pertama karena bagian itu yang membuat sistem bisa dipakai lintas sesi.

## 1. Pembuka

Semua sesi di sistem ini dimulai dengan SATU prompt (bagian 2) dan diakhiri dengan satu prompt (bagian 3) — tidak perlu menempel konteks manual. Isi bagian 2 dan 3 di bawah adalah salinan IDENTIK dari `PROMPT_ENTRI_UNIVERSAL.md` (dua file, satu sumber — kalau mengubah salah satunya, sinkronkan keduanya; selisih diam-diam adalah temuan audit di preseden M-15).

## 2. Prompt Pembuka Universal

```
Kamu adalah agent yang terhubung ke repo meta ini, dan sesi ini bekerja pada Sistem Klinik (folder sistem-klinik/).
Sebelum melakukan apa pun:

1. Jalankan Entry Point tingkat repo yang WAJIB (aturannya tertulis di file 00_CARA_KERJA_META.md di folder _meta — baca itu): laporan awal mengikuti SESSION_REPORT_TEMPLATE, cek PR menggantung lewat gh pr list --state all, cek INDEKS_SISTEM, dan cari LOG_SESI terbaru di _log-sesi/ — kalau ada yang OPEN, BACA dulu dan laporkan; jangan tanya ulang konteks yang sudah tercatat
2. Baca `STATUS.md`, `SYSTEM_MANIFEST.md`, dan `00_RENCANA_KERANGKA.md` di folder sistem-klinik/ sebagai peta sistem ini. Bila START_DI_SINI.md sudah ada di folder itu, baca itu juga; bila belum (tahap kerangka), laporkan sebagai bagian yang menyusul — bukan blocker
3. Tanyakan: "Apa tujuan sesi ini?" — kandidat: membangun dokumen sistem klinik yang dijadwalkan di rencana kerangka; menjalankan run bengkel (target menginap di _bengkel/); memperbaiki/menambah katalog cacat hasil temuan run; atau lain-lain
4. Baca sendiri konteks wajib sesuai tujuan — jangan baca seluruh isi repo. JANGAN menyentuh isi sistem lain (folder _produksi-aktif/, folder sistem lain, repo target manapun) kecuali tujuan sesi ini eksplisit memintanya
5. Jangan mulai eksekusi/menulis file apa pun sebelum aku konfirmasi tujuan sesi ini jelas

Sepanjang sesi: pelihara LOG_SESI di _log-sesi/ (aturannya ada di `10_LOG_SESI.md`), commit+push tiap pertukaran yang menghasilkan informasi baru, tanya di tiap gerbang approval, akhiri dengan PR tanpa auto-merge.
```

## 3. Prompt Penutup Sesi

```
Tutup sesi ini:
1. Perbarui `STATUS.md` di sistem-klinik/ — field deterministik wajib benar: Pekerjaan belum tersimpan = "Tidak ada" hanya bila working tree memang bersih dan seluruh commit ter-push
2. Perbarui header LOG_SESI sesi ini: CLOSED (atau OPEN + "dilanjutkan di mana" bila disengaja)
3. Perbarui tanggal "terakhir disentuh" dan status sistem ini di _meta/INDEKS_SISTEM.md — pencatatan manual, TIDAK mengandalkan git history
4. Kalau kerja berlanjut lintas sesi: tinggalkan handoff di log sesi + STATUS supaya sesi baru melanjutkan tanpa ditanya ulang dari nol
5. Commit + push semua yang bermakna; buka PR dengan deskripsi lengkap (apa yang dikerjakan, gerbang yang diberikan/ditunda, nomor PR dicatat di commit terakhir). SEBELUM merge/close apa pun: pastikan semua sudah ter-push — setelah itu sesi ini TIDAK BISA push lagi (fakta platform); kerja lanjutan dari sesi baru yang dibuka dari main
6. Jalankan pembangkit prompt review repo induk (tools/review_prompt.py --pr <nomor>) dan tempel keluarannya sebagai SATU BLOK BERPAGAR di badan pesan chat TERAKHIR sesi — tanpa blok itu, penutupan dianggap belum dikerjakan dan PR belum boleh dinilai
7. Jangan pernah auto-merge — merge selalu keputusanku
```

## 4. Apa sistem ini, dengan kata awam (istilah awam)

Klinik Sistem = tempat perawatan untuk sistem-sistemMU yang hidup di repo terpisah — mau dia lahir sebelum meta ini matang (banyak cacat warisan) atau sesudahnya (pingin ditingkatkan/diksa ulang): yang dinilai keadaannya, bukan umurnya. Ada dua cara datang:
- **Rawat jalan (suntikan)** — kamu salin folder kit/ dari sini ke repo target (di workspace, bukan ke git), kirim satu prompt dari kit itu, dan agent di sana mengaudit + menanam yang hilang + meleburkan dirinya. Targetmu terlihat normal saja, cuma lebih sehat. Ini mode default.
- **Rawat inap (bengkel)** — copy sistem target "menginap" sementara di sistem-klinik/_bengkel/ (hanya di branch kerja, tidak pernah masuk main), untuk rombakan besar yang butuh alat-alat meta. Selesai, dia pulang; PR-nya tinggal jadi catatan. Salinannya seadanya — hanya yang dibedah menginap, aset besar tidak ikut; branch-nya dihapus setelah pemulangan (hygiene anti-bengkak, K-9).

Kapan-kapan mau kontrol ulang: salin kit/ terbaru, jalankan lagi — kit membaca rekam klinik dulu, jadi tidak menanam dua hal yang sama dua kali; sistem yang sudah sehat cuma kena jalur "kontrol + upgrade".
Dan klinik ini sendiri hidup: setiap run berakhir dengan TAHAP PANEN — cacat baru & ide perbaikan yang ditemukan di targetmu dilaporkan balik, dan kalau kamu setujui, masuk ke kit versi berikutnya.

| Situasi | Yang terjadi |
|---|---|
| Kamu mau run ke sistem target | Agent MUST mulai dari diagnosis + rencana (G-Rencana); tidak ada sentuhan sebelum kamu setuju rencananya |
| Agent mau menimpa/menghapus file target | WAJIB izin per-item; diam-diam overwrite tidak sah |
| Agent menemukan alat/skill yang mungkin berguna (UI, PPT, OCR, dll.) | DIA MENAWARKAN + hasil risetnya; kamu boleh bilang tidak; penolakan dicatat, tidak ditawari ulang tanpa alasan baru |
| Agent butuh keputusan kamu (banyak persetujuan per-item) | TANYANYA DIBORONG, bukan dicicil (K-10): daftar bernomor maks ±5 per pesan, tiap tawaran skill/plugin dijelaskan fungsi/tujuan/alasan + risiko + alternatif, dan SELALU ada slot terakhir "mau mengusulkan yang belum ada di daftar?" — kamu jawab sekali, agent kerjakan sekali sampai checkpoint berikutnya |
| Run selesai | Rekam klinik ditulis + cap versi kit; folder kit hilang dari git target; PR terbuka TANPA auto-merge; merge = kamu |
| Sesi crash | Sesi baru cari LOG_SESI terbaru → lanjut; itulah kenapa commit tiap tahap itu fisik, bukan birokrasi |


## 5. Kalimat pembuka untuk berbagai situasi

- Mau menjalankan run ke sistem target: "Jalankan run klinik suntikan untuk <repo target>."
- Mau run bengkel: "Ambil sistem <nama> dari <lokasi>, jalankan rawat inap di _bengkel/."
- Mau sekadar menambah temuan ke katalog cacat: "Catat temuan ini untuk Katalog Cacat: ..."
- Mau status saja: "Laporkan status sistem klinik, jangan kerjakan apa pun."

## 6. Cara review & merge

Sama seperti repo induk: buka PR → review isi (kamu pemilik keputusan) → merge sendiri → sesi lama tidak bisa push lagi setelah itu (fakta platform — buka sesi baru dari main untuk lanjut). Jangan minta agent auto-merge.

## 7. Kebiasaan yang perlu dijaga — dan status sistem

| Situasi | Yang terjadi |
|---|---|
| Kamu mau run ke sistem target | Agent MUST mulai dari diagnosis + rencana (G-Rencana); tidak ada sentuhan sebelum kamu setuju rencananya |
| Agent mau menimpa/menghapus file target | WAJIB izin per-item; diam-diam overwrite tidak sah |
| Agent menemukan alat/skill yang mungkin berguna (UI, PPT, OCR, dll.) | DIA MENAWARKAN + hasil risetnya; kamu boleh bilang tidak; penolakan dicatat, tidak ditawari ulang tanpa alasan baru |
| Run selesai | Rekam klinik ditulis + cap versi kit; folder kit hilang dari git target; PR terbuka TANPA auto-merge; merge = kamu |
| Sesi crash | Sesi baru cari LOG_SESI terbaru → lanjut; itulah kenapa commit tiap tahap itu fisik, bukan birokrasi |

Tahap pembangunan dibaca di `STATUS.md` dan `SYSTEM_MANIFEST.md` folder ini. Rencana keseluruhan + keputusan yang sudah kamu ambil (11 Sep 2026) ada di `00_RENCANA_KERANGKA.md`.
