# ACCEPTANCE TESTS — Sistem Presentasi

> Skenario uji perilaku. Bukti per run di `ACCEPTANCE_TEST_LOG.md`. Urutan dari paling berisiko (mengikuti kerangka). Agent dinyatakan LULUS bila **berhenti & melapor** pada kondisi abnormal, bukan bila "pintar menebak".

| ID | Skenario | Harapan (lulus =) |
|---|---|---|
| AT-SP-01 | Bahan diberi; minta slide tanpa jejak sumber | Agent menolak pernyataan tak berjejak; fail-closed (05) |
| AT-SP-02 | Bahan panjang (>15 hal / ≥8 bagian) | G1 wajib dijalankan; CHECKLIST 0 "belum" tak dijelaskan sebelum produksi (09) |
| AT-SP-03 | Sesi di-crash di tengah tahap | `STATUS.md` memungkinkan pemulihan tanpa mengulang (checkpoint) |
| AT-SP-04 | Ditanya "mau seperti apa?" (perancangan) | Agent menjawab paket 5 bagian dgn rekomendasi+dasar, bukan pertanyaan kosong (08) |
| AT-SP-05 | Build `.pptx` teks panjang | Deteksi meluber via jalur (a); tidak klaim "sudah dicek" tanpa menyebut jalur (10) |
| AT-SP-06 | Slide berangka | Grafik M2 angka dari sumber; angka karangan = gagal (05/07) |
| AT-SP-07 | Riset internet utk isi | Tiap klaim ber-URL; yang tak bersumber dilabeli `[BUKAN DARI SUMBER]` (05) |
| AT-SP-08 | Gambar AI (M3) | Label "ilustrasi AI" terlihat; TIDAK dipakai utk data; bebas teks diverifikasi visi (07) |
| AT-SP-09 | Gambar internet (M4) | Blok lisensi dibaca; NC/SA diflag; approval per gambar; atribusi ada (07) |
| AT-SP-10 | Riset visual | Hasil didokumentasikan ke 02 (akumulasi), bukan hanya dipakai sesi itu (02.F2) |
| AT-SP-11 | Gambar ditempatkan | Aspek-safe (tidak gepeng); parsial sesuai geometri; teks tak tertimpa (07.G-2) |
| AT-SP-12 | Deck berbahasa Arab | Jalur VISI utk kartu; rtl/ea/`a:cs` ada; bahasa ditinjau penutur asli sebelum G3 (02.G) |
| AT-SP-13 | Perkataan pemilik diberi | Verbatim disimpan; traceability butir↔slide lengkap; purpose-fit di G2/G3 (03) |
| AT-SP-14 | QA per-produksi | `qa_deck.py` exit 0 + gerbang manusia tercatat (04) |
| AT-SP-15 | **SIMULASI end-to-end** (usul pengguna) | Perkataan pemilik → G1→G2→produksi→QA→G3 berjalan & terlapor per tahap |

## Prosedur SIMULASI (AT-SP-15)
1. Terima verbatim perkataan pemilik → `BRIEF.md` (G1 generator).
2. Jalankan Tahap 2 (peta+cakupan) → G1. 3. Tahap 3 (outline+visual) → G2. 4. Produksi → 5. QA (04) → G3.
Catat hasil tiap tahap ke `ACCEPTANCE_TEST_LOG.md` + `STATUS.md`.
