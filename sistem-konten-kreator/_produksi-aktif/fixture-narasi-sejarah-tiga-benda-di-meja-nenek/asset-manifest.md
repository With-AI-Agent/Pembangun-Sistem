# Asset Manifest — Tahap 5

- **Konten:** Tiga Benda di Meja Nenek (fixture)
- **Tahap:** 5 — Generate/Acquire Assets
- **Status:** asset tersimpan; **G1 Tahap 5 disetujui 2026-09-06 WIB**
- **Metode:** tujuh still frame vertikal dibuat dengan tool image generation Agent berdasarkan breakdown yang sudah dikunci. Ini bukan footage video dan bukan stok pihak ketiga.
- **Bank Konsistensi Visual:** tidak berlaku menurut Channel Brief/Model Konten Brief; `segmen-01-radio-pintu-masuk.png` dipakai sebagai reference image hanya untuk kontinuitas internal konten pada segmen 2, 4, dan 7.
- **Sumber eksternal:** tidak ada; tidak ada `SUMBER.md` dan tidak ada atribusi eksternal yang perlu dicatat.

## Inventaris

| Segmen | File | Fungsi | Metode/kontinuitas | Dimensi | Ukuran | SHA-256 |
|---|---|---|---|---:|---:|---|
| 01 | `assets/segmen-01-radio-pintu-masuk.png` | Radio tua cokelat sebagai benda pintu masuk; close-up di meja kayu. | Dibuat dari prompt b-roll tunggal; tanpa reference image. | 768×1376 | 2543960 bytes | `23943fc14116c5079f296074b1d5d82b957bae51600c1a14fdac6ae0dacb26e3` |
| 02 | `assets/segmen-02-radio-pagi.png` | Radio yang sama dalam rumah sunyi menjelang pagi. | Dibuat dengan `segmen-01-radio-pintu-masuk.png` sebagai reference image untuk kontinuitas radio. | 768×1376 | 2325562 bytes | `e7288d3bf5479a4881382c8082c29f6ce00848457f00e3fc4e07a425b645e714` |
| 03 | `assets/segmen-03-ketel-rutinitas-pagi.png` | Ketel beruap dan koridor rumah sebagai tanda rutinitas. | Dibuat dari prompt b-roll tunggal; tanpa karakter. | 768×1376 | 2766471 bytes | `3d764d288aa109e439a14390178f257a7ce0fd34363d6ec51e8e2e7964f3eb40` |
| 04 | `assets/segmen-04-radio-itu-jam.png` | Close-up dial/tombol radio yang sama untuk titik penegasan. | Dibuat dengan `segmen-01-radio-pintu-masuk.png` sebagai reference image. | 768×1376 | 2842650 bytes | `b74169d891f58b1aa24607a55fceb2dc1dec24a0dcede1acff07e454302f76f7` |
| 05 | `assets/segmen-05-ponsel-pengganti.png` | Ponsel generik tanpa logo sebagai pengganti radio. | Dibuat dari prompt b-roll tunggal; layar tanpa UI terbaca. | 768×1376 | 1998871 bytes | `e20bde37b24dd60b3040e4a08df18a4ab96bcab16e860d3f683a8861c9a6cc18` |
| 06 | `assets/segmen-06-urutan-pagi.png` | Ketel dan meja makan kosong sebagai rutinitas yang berlanjut. | Dibuat dari prompt b-roll tunggal; tanpa karakter. | 768×1376 | 2782951 bytes | `e0ef037f012402b9e87965d35c2b9bede01b04cb33f73f4e863fceaf53c0ecda` |
| 07 | `assets/segmen-07-meja-kosong-penutup.png` | Sudut meja kosong setelah radio tidak ada. | Dibuat dengan `segmen-01-radio-pintu-masuk.png` sebagai reference image untuk kontinuitas meja/ruang. | 768×1376 | 2411793 bytes | `ffaf5baed48749d937b42282098492ad8f7c456b6a2c959d9a70ef0f7483468f` |

## Pemeriksaan pra-G1

- [x] Tujuh file asset ada di `assets/` dan seluruhnya PNG vertikal `768×1376`.
- [x] Setiap file dipetakan ke satu segmen breakdown; tidak ada file tak terpakai.
- [x] Review visual awal: tidak ada wajah yang dapat dikenali, watermark, atau logo merek yang dominan; palet kayu/cokelat/krem dan cahaya hangat konsisten.
- [x] **G1 Tahap 5:** pengguna menerima seluruh asset pada 2026-09-06 WIB; marking kecil dial segmen 04 diterima apa adanya.
- [ ] Audio, footage bergerak, dan assembly belum dibuat; itu bukan klaim selesai Tahap 6.

### Catatan review

Segmen 4 mempertahankan detail dial radio yang sama, termasuk marking fisik kecil pada dial; tidak ada teks overlay atau branding besar. Pengguna menerima marking ini apa adanya sebagai accepted limitation fixture. Jangan regenerate asset atau memanggil image generation lagi pada run ini.
