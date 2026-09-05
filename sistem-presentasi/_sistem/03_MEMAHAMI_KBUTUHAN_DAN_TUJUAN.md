# 03 — Memahami Kebutuhan & Tujuan Pengguna (WAJIB di tiap deck)

> Bug deck#1: hasil "ga sesuai yang diinginkan/dibutuhkan pengguna" & "ga cocok dengan tujuan PPT". Akar: kebutuhan/tujuan tidak ditangkap eksplisit & tidak diverifikasi cocok. Dokumen ini mewajibkan penangkapan & verifikasi itu **setiap** produksi.

## A. Perkataan pemilik = spesifikasi utama
1. Simpan **verbatim** perkataan/permintaan pemilik di `PERKATAAN_PEMILIK_VERBATIM.md` — file baku deck (dirujuk dari `BRIEF.md`; update 5 Sep 2026, AP-09 audit: sebelumnya ditahan di BRIEF atau file tak baku). Jangan parafrase dulu.
2. Turunkan dari sana **daftar butir permintaan** (mis. "ringkasan h.6, tujuan h.20, …") → jadi `CHECKLIST_CAKUPAN.md`.
3. **Traceability:** tiap butir permintaan ↔ slide yang memuatnya (catat di `OUTLINE.md`). Tiap slide harus bisa ditunjuk menjawab butir mana; slide tanpa butir = pertanyaan; butir tanpa slide = cacat.

## B. Tangkap TUJUAN & konteks (isi `BRIEF.md`)
- **Tujuan pakai:** mis. "alat presentasi sidang tesis" → konsekuensi: audiens penguji, waktu terbatas, harus menonjolkan kontribusi/temuan, bahasa sesuai pemilik.
- **Audiens**, **occasion**, **durasi**, **bahasa**, **preferensi penyajian** (bullet/paragraf), **selera visual** bila disebut.
- Bila ada yang ambigu/missing → **tanya** (approval kecil), jangan asumsikan.

## C. Verifikasi cocok-tujuan (purpose-fit) di G2 & G3
Sebelum approve, jawab eksplisit:
1. Apakah urutan & penekanan slide melayani **tujuan** (mis. sidang → temuan/kontribusi dulu, metode ringkas)?
2. Apakah tiap butir pemilik terwakili (traceability lengkap)?
3. Apakah bahasa, kedalaman, dan gaya sesuai audiens & preferensi?
Jika ada "tidak", perbaiki sebelum lanjut. Catat jawaban di `STATUS.md`/`OUTLINE.md`.

## D. Paham = bisa menjelaskan kembali
Agent dianggap "paham" bila mampu menuliskan di `BRIEF.md`: (a) tujuan pakai dalam satu kalimat, (b) siapa audiens, (c) apa yang pemilik anggap penting (dari verbatim), (d) apa yang TIDAK diminta. Bila tidak bisa, jangan produksi — tanya dulu.

## Log
| Tanggal | Keputusan | Oleh |
|---|---|---|
| 2026-09-05 | Dokumen dibuat dari umpan balik deck#1 (hasil tak cocok tujuan) | agent |
