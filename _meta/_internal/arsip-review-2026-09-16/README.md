# Arsip Artefak Review/Audit Root — 16 September 2026

Lima berkas yang dulu tergeletak di **root repo** dipindahkan ke sini (bukan dihapus) oleh sesi
`arena/01a0a7d3-pembangun-sistem`, atas mandat pemilik "bereskan semuanya". Semuanya artefak
sekali-pakai dari sesi lain (branch `arena/01a0a48f`, PR #59 — MERGED) yang masuk `main` lewat PR itu.

**Kenapa dipindah:** mereka keluarga cacat **C-07 (*superseded-but-live*)** — dokumen yang sudah
digantikan tetapi tetap hidup di tempat paling terlihat (root repo) tanpa penanda apa pun, dan
isinya mem-pin commit/branch yang basi sejak saat itu juga. Root repo adalah hal pertama yang
dibaca sesi baru; prompt review basi di sana bisa benar-benar dipakai orang.

| Berkas | Apa isinya | Yang berlaku sekarang |
|---|---|---|
| `REVIEW_PROMPT_2026-09-16.md` | prompt review independen, pin HEAD `6acf7b3` | `python3 tools/review_prompt.py --pr <nomor>` — dibangkitkan saat dibutuhkan |
| `REVIEW_PROMPT_DELTA_593ba79.md` | prompt delta review, pin HEAD `593ba79` | idem |
| `REVIEW_SIMULASI_2026-09-16.md` | catatan review simulasi penulis, pin HEAD `1e64e45` | laporan review yang sesungguhnya ada di komentar PR bersangkutan |
| `AUDIT_NPX_UPDATE.md` | **duplikat byte-identik** | kanonik: `sistem/sistem-building-aplikasi/_sistem/AUDIT_NPX_UPDATE_2026-09-16.md` |
| `AUDIT_ZIP_VS_NPX.md` | **duplikat byte-identik** | kanonik: `sistem/sistem-building-aplikasi/_sistem/AUDIT_ZIP_VS_NPX_2026-09-16.md` |

Duplikasi dua berkas audit dibuktikan dengan md5 (diukur 2026-09-16 sebelum dipindah):
`AUDIT_NPX_UPDATE.md` = `33a8f079b8ed9fbb567df7d6029da945` = salinan kanoniknya;
`AUDIT_ZIP_VS_NPX.md` = `bc0ce8183aa19a469ac1c1464ca017a8` = salinan kanoniknya.
Salinan di arsip ini **tidak menambah informasi** — disimpan karena Kebijakan Lebur Aturan 2
melarang menghapus tanpa izin per-item. Bila pemilik mau root benar-benar bersih dari duplikat,
hapus dua berkas itu di sini (kanoniknya tetap ada di sistem) — perintahnya ada di
`_meta/_internal/HOUSEKEEPING_2026-09-16.md`.

Tiga berkas `REVIEW_*` diberi **banner arsip di kepalanya**; isi aslinya tidak disunting.
