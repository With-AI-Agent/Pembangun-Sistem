# Catatan Asset Tahap 5 — Pintu Kos yang Tidak Pernah Dikunci

- **Dasar:** `breakdown-output.md` b1 — **DIKUNCI (G1+G2, 2026-09-10)**. Guardrail pemilik: substitusi boleh sepanjang memenuhi deskripsi visual + larangan visual; perubahan besar = berhenti dan laporkan.
- **Jalur akuisisi:** semua asset **digenerate di dalam sesi ini** (teks→gambar, beberapa dengan referensi gambar hasil sesi yang sama). Alasan: gerbang rights-check Tahap 5 — stok/foto web tidak bisa diverifikasi status lisensinya dari sesi ini, dan karya berhak cipta pihak ketiga tidak boleh jadi asset final tanpa hak jelas. Tidak ada referensi visual dari web yang dipakai.
- **Chaining referensi (konsistensi subjek berulang — prinsip `06_PROMPT_LIBRARY.md` bagian A):** S1 = acuan pintu → dipakai sebagai referensi generate S2, S3, S4; S2 = acuan kunci+tali tembaga → referensi S5, S7. S2a, S5a, S6 tanpa referensi (subjek berdiri sendiri).
- **Ketentuan unit:** 1 potongan b-roll per segmen narasi (definisi unit Model Brief). S2 dan S5 mendapat 1 file tambahan (S2a, S5a) agar seluruh elemen visual yang disebut di kolom deskripsi segmennya tercakup.
- **Gaya seragam (semua prompt):** warm faded archival film still; palet cokelat kayu/krem/hijau tua pudar; tekstur film 16mm halus; tanpa orang/wajah, tanpa teks terbaca, tanpa logo/merek.

## Inventaris + cek checklist Tahap 5 (`05_CONTENT_PRODUCTION_PIPELINE.md`)

| File | Segmen | Prompt final (ringkas) | Referensi disertakan | Cek checklist |
|---|---|---|---|---|
| `s1-hook-pintu-sedikit-terbuka.jpg` | S1 | Close-up pintu kayu kos tua sedikit terbuka, cahaya hangat dari celah, cat krem mengelupas, fokus dangkal, film grain | — (teks saja) | ✓ — menjadi acuan pintu untuk S2/S3/S4 |
| `s2-kunci-di-tali-tembaga.jpg` | S2 | Extreme close-up kunci kuningan tua di tali tembaga pada paku, pintu cat mengelupas blur di latar, warm side light | `s1` | ✓ — menjadi acuan kunci+tali |
| `s2a-gang-menuju-pintu-senja.jpg` | S2 (tambahan cakupan (a)) | Gang sempit tua golden hour menuju satu pintu kecil di ujung, tanaman pot & pagar kayu siluet | — | ✓ — catatan: arsitektur bergaya "kota tua" generik (deskripsi segmen tidak menyebut arsitektur spesifik); tidak ada teks terbaca |
| `s3-pintu-terbuka-malam.jpg` | S3 | Pintu yang sama terbuka penuh malam hari, cahaya tungsten hangat tumpah keluar, suasana aman | `s1` | ✓ — kontinuitas pintu dengan S1 kuat (pola mengelupas & kusen sama) |
| `s4-pintu-terkunci-jendela-menyala.jpg` | S4 | Malam: pintu yang sama tertutup rapat berkait, jendela kamar kos menyala satu-satu, ketegangan tertahan, hijau tua dominan | `s1` | ✓ — **digenerate ulang 1×**: hasil pertama memuat siluet orang menonjol di jendela (berlebihan vs deskripsi "bayangan samar … tertahan"); versi final hanya bayangan sangat tipis. Sesuai checklist: hasil meleset → perbaiki prompt dulu, bukan langsung dipakai |
| `s5-kunci-tua-di-laci.jpg` | S5 | Still life: kunci yang sama kini berkarat, tergeletak sendiri di laci kayu tua terbuka, cahaya jendela | `s2` | ✓ |
| `s5a-sudut-gang-yang-berubah.jpg` | S5 (tambahan cakupan (a)) | Sudut gang tempat kos dulu berdiri, kini kosong/berubah, bekas fondasi, siang pudar | — | ✓ |
| `s6-pintu-rumah-kini-golden-hour.jpg` | S6 | Pintu rumah masa kini didorong terbuka oleh satu tangan dewasa (tanpa wajah/identitas), cahaya hangat menyambut, palet paling hangat | — | ✓ — kontak manusia hanya tangan, sesuai larangan visual |
| `s7-tali-tembaga-kosong-senja.jpg` | S7 | Tali tembaga yang sama kini kosong tanpa kunci di paku yang sama, goyang halus, cahaya senja memudar, komposisi statik | `s2` | ✓ — kontinuitas paku/tali/pintu latar dengan S2 kuat |

## Ringkasan cek checklist Tahap 5

- [x] File referensi Bank Konsistensi Visual disertakan? — **Tidak berlaku**: channel faceless, tidak ada elemen terkunci (Channel Brief bagian 4); chaining acuan antar-asset dipakai sebagai pengganti kontrol konsistensi subjek berulang (pintu, kunci, tali tembaga).
- [x] Karakter Tipe B konsisten? — **Tidak berlaku**: tidak ada karakter Tipe B di konten ini.
- [x] Sesuai Gaya Visual Channel Brief? — ✓ footage bernuansa arsip/foto benda, hangat pudar, tekstur film, palet sesuai.
- [x] Hasil meleset jauh ditangani? — ✓ S4 digenerate ulang 1× (lihat tabel); tidak ada hasil meleset yang dipakai.
- [x] Unit pertama karakter Tipe B jadi acuan? — Tidak berlaku (acuan subjek benda: S1 untuk pintu, S2 untuk kunci/tali — prinsip sama, objek beda).
- [x] Tersimpan di `_produksi-aktif/.../assets/`? — ✓ 9 file `.jpg`.

## Rights-check (bagian dari G1 Tahap 5)

- Seluruh asset digenerate agent di sesi ini; **tidak ada** karya pihak ketiga, foto berlisensi, logo, karakter milik pihak lain, atau musik yang direproduksi.
- Tidak ada referensi visual dari web yang dipakai sebagai arahan — deskripsi b-roll breakdown satu-satunya sumber prompt.
- Larangan visual terpenuhi per file: tanpa wajah dikenali (S4 hanya bayangan gorden samar; S6 hanya tangan), tanpa logo, tanpa teks terbaca.

## Gerbang

- **G1 Tahap 5 (asset diterima / ada yang perlu regenerate?):** belum — diminta ke pengguna, beserta catatan S4 (regenerate 1×) dan tambahan S2a/S5a.
