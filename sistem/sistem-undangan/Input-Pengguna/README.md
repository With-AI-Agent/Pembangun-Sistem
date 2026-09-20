# Input-Pengguna — tempat pemilik menaruh bahan miliknya sendiri

> **STATUS: KERANGKA — BELUM ADA ISI.** Dokumen ini dibuat sebagai bagian dari skeleton folder saat
> `Tahap: kerangka`, **bukan** sebagai dokumen jadi. Mengisinya adalah langkah **sesudah** rencana kerangka
> di-merge (lihat `00_RENCANA_KERANGKA.md` bagian 11).

Folder ini ada karena permintaan pemilik: **mekanisme input milik pemilik** — font, template, contoh
undangan yang disukai, dan referensi visual. Bahan di sini **diperlakukan sebagai masukan**, bukan
diabaikan, dan **tidak boleh ditimpa** oleh pilihan default agent.

## Struktur yang direncanakan

| Subfolder | Untuk apa |
|---|---|
| `font/` | berkas font milik/dipilih pemilik (catat **lisensinya** — tidak semua font boleh dipakai komersial) |
| `template/` | template atau kerangka layout yang ingin dipakai ulang |
| `contoh/` | contoh undangan jadi yang disukai pemilik |
| `referensi/` | gambar/moodboard/palet warna sebagai arah desain |

## Aturan yang sudah mengikat

1. **Aset besar TIDAK masuk repo** — yang masuk **resep + sumber kecil** saja (keputusan review #6,
   disetujui pemilik 17 Sep 2026). Plafon artefak sesi ±128 MB / 10.000 berkas; melanggarnya membuat
   pekerjaan **tidak bisa di-commit**.
2. **Setiap bahan wajib dicatat provenance-nya** (dari mana, lisensi apa, tanggal) — tanpa itu bahan
   tidak boleh dipakai untuk client.
3. Bahan di sini **masuk lewat gerbang G3** sama seperti aset lain: teks tetap harus dari font,
   ornament/logo tetap harus vektor, dan **hanya foto** yang boleh raster
   (`00_RENCANA_KERANGKA.md` bagian 4.3).
