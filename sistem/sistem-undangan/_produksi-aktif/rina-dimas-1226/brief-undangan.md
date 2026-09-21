# Brief Undangan — Unit Uji Coba `rina-dimas-1226`

> Diisi mengikuti `04_TEMPLATE_BRIEF_UNDANGAN.md` (Tahap 1–2 siklus). **Uji coba b3** — "client" unit ini
> adalah **pemilik studio sendiri** (fiktif/sendiri), jadi keputusan yang biasanya datang dari client
> diambil pemilik sebagai operator, dan **setiap penyimpangan dari L1/L2 dicatat** di
> `log-keputusan-unit.md` (aturan warisan L3, `00_RENCANA_KERANGKA.md` bagian 2.2).

## Bagian A — Identitas dan Paket

| Butir | Isi |
|---|---|
| Unit | `rina-dimas-1226` (uji coba internal) |
| Jenis acara | **Pernikahan** (`02_PROFIL_JENIS_ACARA.md`, cakupan umum — G1 LULUS) |
| Bentuk acara | **Akad nikah** + resepsi (istilah resepsi terpilih: *Resepsi Pernikahan*) |
| Paket studio | Fase portofolio L1 — **bukan** client nyata, tidak ada transaksi |
| Format yang diminta | **web** (selalu) + **flyer statis** (portrait + landscape) — batas fase portofolio di `05_DISCOVERY_DESAIN_PROMPT.md` bagian 3. **Video & cetak TIDAK** dijanjikan (dokumen 07/08 ditunda) |
| Tenggat | Tidak ada tenggat client; siklus uji = satu sesi. **Lead time 3 hari kerja TIDAK diukur di sini** (tidak ada jam kerja nyata yang dijalani) — wajib diukur pada produksi nyata pertama (`05` bagian 4) |

## Bagian B — Permintaan Client

| Butir | Isi |
|---|---|
| Arah desain | **Modern minimalis** (putusan pemilik 21 Sep 2026 paket E1–E4; menu `05` bagian 2 pilihan ke-3) |
| Suasana | Tenang, bersih, banyak ruang kosong; tanpa ornamen ramai (`02` bagian 6) |
| Nada bahasa | Elegan & khidmat, bahasa Indonesia baku (L1 bagian 5) |
| Fitur yang diminta | Countdown · susunan acara · peta · form ucapan & RSVP (mode uji) · teks WA siap salin |
| Fitur yang **tidak** diminta | Musik latar · galeri foto · streaming · QR check-in · amplop digital (lihat Bagian D) |

## Bagian C — Anggaran dan Tenggat

- Anggaran: **Rp 0** (uji coba internal; produksi & bulanan jalur default memang Rp 0 — L1 bagian 6).
- Tenggat: tidak ada. **Jalur cepat** tidak diuji di sini.

## Bagian D — Batasan yang Disadari (yang kurang dinyatakan, bukan dikarang)

1. **Foto: tidak ada.** Sah per `02` bagian 6 (*"tanpa foto = sah → desain ornament-driven"*).
   Akibat: **G3 tidak teruji** pada uji coba ini (0 aset raster) — dinyatakan di `STATUS.md`.
2. **Amplop digital: tidak diaktifkan** (putusan E3). Rekening pemilik belum ada; nomor rekening nyata
   tidak ditaruh di repo. Yang diuji: bagian tidak dirender saat data kosong + jalur uji berlabel.
3. **Musik latar: tidak ada** — belum ada berkas audio dengan provenance jelas (aturan lisensi L1 bagian 10).
4. **Tanggal Hijriah: tidak diisi** — fakta yang harus benar; diisi setelah konfirmasi keluarga pada client nyata.
5. **Kontak RSVP: tidak ada** — kontak client tidak ada pada uji coba; tidak diisi nilai karangan.
6. **Titik sensitif:** `titik_sensitif_terkonfirmasi.ya = true` dengan catatan bahwa yang dikonfirmasi
   adalah **status uji coba** (data fiktif). Pada client nyata, butir ini menyangkut urutan keluarga,
   gelar, alm./wali, dan beda agama — **tidak boleh dilewati** (`02` bagian 3).

## Bagian E — Penyerahan ke Skema Data (03)

Rekaman resmi unit ini = `web/data-acara.json` (**satu-satunya sumber nilai** untuk web dan flyer).
Gerbang data (`03_TEMPLATE_DATA_ACARA.md` bagian 7) ditegakkan **alat**, bukan ingatan:

```
python3 sistem/sistem-undangan/_sistem/validate_unit.py \
  sistem/sistem-undangan/_produksi-aktif/rina-dimas-1226
```

Hasil: **rc=0 PASS** (lihat `uji-b3.md` bagian gerbang untuk keluaran apa adanya).

## Gerbang yang Dilewati

| Gerbang | Kategori | Status di unit ini |
|---|---|---|
| **G0** (Tahap 1 — brief) | Besar | **Dilewati sebagai latihan** — brief ini disetujui pemilik lewat jawaban "setuju semua (E1–E4)" + tinjauan pratinjau |
| **G1** (Tahap 2 — data) | Sedang | **LULUS secara mekanis** lewat gerbang data `validate_unit.py` rc=0 + konfirmasi titik sensitif tercatat |
| **G2** (Tahap 3 — desain & format) | Besar | **Putusan pemilik 21 Sep 2026** (E1–E4): model **Modern minimalis**, format **web + flyer** |
| **G3** (Tahap 4 — aset) | Besar | **Tidak teruji (0 aset raster)** — dinyatakan terbuka di `STATUS.md`; aturan bukti per aset diuji lewat alat |
| **G4** (Tahap 5 — rakit & pratinjau) | Sedang | **Pratinjau nyata** disajikan ke pemilik (alamat di `uji-b3.md`) |
| **G5** (Tahap 7 — serah terima) | Besar | **Latihan** — 7 butir daftar periksa dijalankan sejauh mungkin; sisa dinyatakan apa adanya |
