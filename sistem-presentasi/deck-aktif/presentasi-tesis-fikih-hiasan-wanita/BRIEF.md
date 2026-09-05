# BRIEF — Presentasi Tesis Fikih Hiasan Wanita

> **Status:** draft Tahap 1 — menunggu konfirmasi pengguna di **G2**. Field bertanda `[REKOMENDASI]` adalah pilihan yang agent sarankan (dengan dasar); field `[DIPUTUSKAN]` sudah pasti dari pemilik tesis/pengguna. Boleh diubah; perubahan dicatat di Log Keputusan.
>
> **Sumber brief:** pesan pemilik tesis (bahasa Arab) yang sampai di chat 4 Sep 2026 + `00_RENCANA_KERANGKA.md`.
> **Bahan:** `bahan/tesis.pdf` (161 halaman, Arab). Jejak: commit GitHub `486246e`.

## Identitas deck

- **Nama deck (slug):** `presentasi-tesis-fikih-hiasan-wanita` `[REKOMENDASI, dasar: PENILAIAN AGENT]` — dipakai kata "hiasan", **bukan** "zina", karena `زينة` = hiasan/adornment; "zina" dalam bahasa Indonesia berarti hal lain (false friend). Boleh diganti.
- **Topik:** أحكام النوازل الفقهية المعاصرة المتعلقة بزينة المرأة — hukum kontemporer fikih terkait hiasan wanita, dalam empat mazhab.
- **Pemilik keputusan:** pengguna (dan pemilik tesis untuk isi).

## Tujuan & audiens `[DIPUTUSKAN dari pesan pemilik]`

- **Tujuan:** presentasi pertahanan/paparan tesis (sidang) yang memetakan isi tesis per bagian sesuai permintaan pemilik.
- **Audiens `[REKOMENDASI]`:** dosen penguji / akademisi → nada formal, istilah fikih dipertahankan dengan terjemahan singkat. Dasar: konteks "رسالة الدكتورة" (tesis doktoral) dan struktur permintaan (tujuan/masalah/metode/kesimpulan) khas sidang.

## Durasi & jumlah slide `[REKOMENDASI, dasar: konvensi sidang 10–15 mnt]`

- **Durasi:** 10–15 menit → **12–15 slide**. Pemilik meminta 12 butir; sebagian butir bisa digabung (mis. jenis+pengumpulan data) agar muat. Dasar: aturan lantai "1 slide per 1–2 menit" + daftar 12 butir pemilik.
- **Alternatif:** kalau sidang memberi waktu lebih, pisahkan butir yang digabung. Konsekuensi digabung: slide lebih padat.

## Sumber & tingkat anti-ngarang `[REKOMENDASI]`

- **Sumber:** hanya `bahan/tesis.pdf` (tingkat **`ketat-rujukan`**: setiap pernyataan wajib menunjuk halaman tesis; tidak ada riset internet untuk ISI). Dasar: pemilik memberi daftar halaman eksplisit → ini presentasi atas SATU dokumen, bukan riset baru.
- **Anti-ngarang:** `ringkas` untuk kalimat penghubung, **`ketat` untuk klaim hukum/angka** — klaim fikih harus verbatim-ish + halaman. Alasan: kesalahan menyimpulkan hukum dalam sidang = fatal.
- **Yang TIDAK dari tesis:** tidak boleh menambah dalil/hukum yang tidak ada di tesis. Kalau slide butuh konteks luar, wajib label `[BUKAN DARI SUMBER]`.

## Struktur yang diminta pemilik `[DIPUTUSKAN]`

Urutan slide mengikuti daftar pemilik (nomor = halaman cetak tesis):
1. Ringkasan (ملخص) — hal 6
2. Tujuan penelitian (أهداف) — hal 20
3. Manfaat (فوائد) — hal 21
4. Masalah (مشكلات) — [halaman dilocate saat G1]
5. Metode (منهج) — hal 23
6. Pertanyaan penelitian (أسئلة) — Bab 4
7. Alasan pengharaman menyambung rambut (العلة في تحريم وصل الشعر) — hal 66–67
8. Jenis & macam penelitian (جنس ونوع البحث) — hal 88
9. Cara pengumpulan data (طريقة جمع المعلومات) — hal 88
10. Pengolahan data (معالجة المعلومات) — [halaman dilocate saat G1]
11. Verifikasi keabsahan data (التحقق من صحة المعلومات) — hal 89
12. Penutup (خاتمة) — hal 152
13. Rekomendasi (توصيات) — hal 153

## Mode gambar `[REKOMENDASI, dasar: keputusan butir 7]`

- **Default: M0 + M1.** Mayoritas slide teks+struktur (M0) karena padat argumen fikih; M1 bila tesis punya tabel/diagram asli yang relevan. **M3 (AI) hanya** untuk slide konsep pembuka bila perlu, berlabel. **M4 (internet) TIDAK dipakai** — topik fikih sensitif akurasi & hak cipta; tidak ada kebutuhan visual eksternal.
- **Aturan G-1 & G-2 berlaku:** tidak ada teks dalam gambar; gambar hanya mengisi area.

## Format output `[DIPUTUSKAN dari keputusan butir 2]`

- `.pptx` (default, **RTL**, font Arab) + `.html` (preview/verifikasi).

## Log Keputusan

| Tanggal | Keputusan | Dasar | Oleh |
|---|---|---|---|
| 4 Sep 2026 | Brief dibuat dari pesan pemilik; struktur 13 slide | pesan pemilik | agent |
| 4 Sep 2026 | Slug pakai "hiasan" bukan "zina"; sumber tunggal tesis; M0+M1 | PENILAIAN AGENT | agent (menunggu konfirmasi pengguna) |
