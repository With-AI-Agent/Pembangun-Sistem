# Catatan Versi — Unit `rina-dimas-1226`

> Diwajibkan oleh **daftar periksa Terbit butir 10** (`09_PANDUAN_PUBLISH_DAN_SERAH_TERIMA.md` bagian 4):
> *"Simpan catatan versi (tanggal + isi perubahan singkat) di folder unit — tanpa ini, 'versi mana yang
> disetujui client' jadi tebakan."*
> **Unit uji coba b3 — bukan client.** Versi terbit dicatat satu baris per penerbitan.

| Versi | Tanggal (UTC) | Disetujui oleh | Isi perubahan | Artefak |
|---|---|---|---|---|
| **v1** | 2026-09-21 | pemilik (paket keputusan **E1–E4**, 21 Sep 2026) + pratinjau b3 | Penerbitan pertama unit uji coba: data acara fiktif, model **Modern minimalis**, format **web + flyer statis (SVG)** + **QR sebar (SVG)**, tanpa foto/musik/amplop. Semua nilai dirender dari `web/data-acara.json` | `web/index.html` · `web/flyer-portrait.svg` · `web/flyer-landscape.svg` · `web/qr-sebar.svg` |

## Aturan yang berlaku sesudah baris ini

- **Perubahan kecil** (typo, jam, tempat, foto, dress code, teks WA) → versi baru **v1.1, v1.2, …**,
  gratis, **tautan tetap sama** (slug tidak berubah — `09` bagian 3).
- **Perubahan besar** (model/warna/struktur baru) → versi baru **v2**, tercatat + persetujuan ulang.
- **Tidak ada baris versi tanpa tanggal + nama penyetuju.** Kalau pratinjau disetujui tetapi belum
  diterbitkan, ditulis di kolom Catatan sebagai *"disetujui, belum terbit"* — bukan dianggap terbit.
