# Model Konten Brief — [NAMA MODEL KONTEN] (Channel: [NAMA CHANNEL])

### Dokumen "hidup" milik SATU model konten dalam SATU channel. Hasil dari `07_MODEL_KONTEN_DISCOVERY_PROMPT.md` ditulis mengikuti struktur ini, disimpan sebagai `channel-[nama-channel]/model-konten/[nama-model]/brief.md` — folder ini juga bisa berisi `assets/` untuk reference visual khusus model konten ini (kalau perlu, opsional). **Dibaca BERSAMAAN dengan Channel Brief channel-nya** (otomatis lewat Entry Point Universal) setiap kali produksi konten dari model ini — dokumen ini TIDAK mengulang isi Channel Brief, hanya menambahkan yang spesifik/beda di level ini.

---

## Status: `Draft` → `Reviewed` → `Approved` → `Merged` → `Operational`

- [ ] **Draft** — masih digali, isi bisa berubah kapan saja
- [ ] **Reviewed** — sudah dibaca lengkap oleh pengguna, koreksi sudah masuk (belum tentu final)
- [ ] **Approved** — isi dikunci lewat gerbang **G2**, tapi masih di branch/PR
- [ ] **Merged** — PR sudah lewat gerbang **G3** dan masuk ke `main`
- [ ] **Operational** — sudah `Merged` DAN semua dependency wajibnya benar-benar ada (lihat Checklist Kelengkapan di bawah). Hanya status ini yang boleh dipakai untuk mulai produksi.

*(Kenapa dipisah begini: "sudah disetujui" dan "sudah masuk `main`" itu dua hal berbeda — brief bisa disetujui isinya tapi belum di-merge, atau sudah di-merge tapi asset referensi wajibnya belum ada. Kalau keduanya dicampur jadi satu kata "Terkunci", produksi bisa mulai di atas dependency yang sebenarnya belum lengkap. Definisi gerbang G2/G3 ada di `00_CARA_PAKAI_SISTEM.md`.)*

*(Model Konten Brief termasuk kategori Besar — WAJIB direview isi lengkapnya sebelum merge.)*

**Checklist Kelengkapan — syarat naik ke `Operational`:**

- [ ] Semua bagian wajib di bawah terisi (tidak ada placeholder `[...]` tersisa)
- [ ] Bentuk detail tiap tahap pipeline untuk model ini sudah ditetapkan (unit kerjanya apa: shot/panel/section/track/lainnya)
- [ ] Override terhadap Channel Brief (kalau ada) sudah dinyatakan eksplisit
- [ ] Gerbang tambahan (kalau model ini menambah G2) sudah dicatat — ingat, G2/G3 bawaan tidak boleh dihapus
- [ ] Channel Brief induknya sudah berstatus `Operational`
- [ ] Sudah `Merged` ke `main`

*(Agent WAJIB menolak menetapkan status `Operational` selama masih ada kotak yang belum tercentang.)*

**Versi:** `[nomor]` — **Terakhir diperbarui:** `[tanggal]`

## Mewarisi dari: `channel-[nama-channel]/channel-brief.md`

*(Semua yang sudah dikunci di sana — Persona & Voice, Konsistensi Visual — otomatis berlaku di sini kecuali dinyatakan override eksplisit di bawah.)*

---

## 1. Identitas Model Konten

- **Nama model konten:**
- **Definisi singkat (beda dari model konten lain di channel yang sama, kalau ada):**

## 2. Format Teknis Spesifik

- **Durasi/panjang pasti:**
- **Struktur konten khas format ini** (hook-beat-twist-CTA, atau pola lain spesifik):
- **Platform paling cocok untuk format ini:**

## 3. Gaya Visual Spesifik

*(Hanya isi yang BEDA/lebih detail dari Gaya Visual Channel — jangan diulang kalau sama persis, cukup tulis "sama seperti Channel Brief")*

- **Pendekatan visual:** (animasi/gambar statis/video real/motion graphic/dst)
- **Kalau ada elemen Konsistensi Visual dari channel (karakter Tipe A, latar, dst) — cara tampil di format ini:** (sama seperti biasanya / perlu penyesuaian, jelaskan — kalau perlu penyesuaian, file referensi tambahan disimpan di `assets/` folder model konten ini, bukan mengubah Bank Konsistensi Visual aslinya)

## 4. Alur Kerja Produksi

*(WAJIB pilih salah satu mode di bawah — jangan campur keduanya untuk 1 model konten yang sama.)*

**Mode:** [ ] Ikuti Kerangka Standar (dengan override ringan)  /  [ ] Alur Kerja Kustom

### Kalau Mode = Ikuti Kerangka Standar

*(Isi bagian ini, kosongkan bagian "Alur Kerja Kustom" di bawah)*

- **Override Persona/Voice (kalau ada penyesuaian tone khusus format ini):**
- **Bentuk konkret Tahap Breakdown untuk format ini** (WAJIB diisi — misal "shot" untuk video, "section" untuk infografis, "panel" untuk komik, atau bentuk lain sesuai format ini):
- **Override Ringan per Tahap** — tahap mana dari `05_CONTENT_PRODUCTION_PIPELINE.md` yang berbeda DETAIL TEKNISNYA untuk format ini (biasanya cukup Tahap 4-5, isi "tidak ada override" untuk tahap yang sama persis dengan default):
  - Tahap 1 (Ideation):
  - Tahap 2 (Konsep & Angle):
  - Tahap 3 (Naskah/Script):
  - Tahap 4 (Breakdown Visual):
  - Tahap 5 (Generate Asset):
  - Tahap 6 (Assembly & Publish Prep):

### Kalau Mode = Alur Kerja Kustom

*(Isi bagian ini, kosongkan bagian "Override Ringan" di atas. Gunakan kalau struktur alur kerja model konten ini beda dari akar — misal ada tahap ekstraksi dari sumber eksternal, atau alur 1-sumber-jadi-banyak-konten. Hasil dari MODE ALUR KERJA KUSTOM di `07_MODEL_KONTEN_DISCOVERY_PROMPT.md`.)*

- **Kenapa model konten ini butuh alur kustom (beda dari kerangka standar):**

- **Tahapan alur kerja (isi selengkap dan sekonkret mungkin, boleh berapapun jumlah tahapnya):**

| No | Nama Tahap | Input | Proses/Tools | Output |
|---|---|---|---|---|
| | | | | |

- **Titik pertemuan dengan kerangka standar:** (di tahap keberapa alur kustom ini "bertemu kembali" dengan alur standar — biasanya begitu 1 ide/bahan konkret sudah didapat, dari situ lanjut mengikuti Tahap Naskah → Breakdown Visual → dst di `05_CONTENT_PRODUCTION_PIPELINE.md` seperti biasa)

- **Catatan tools yang belum pasti** (kalau ada tahap yang tools/caranya belum ditentukan dan akan dieksplorasi saat eksekusi nyata — wajar untuk dicatat sebagai "belum ditentukan" daripada dipaksa diisi sekarang):

## 5. Contoh Konkret

*(1 contoh konten dari format ini, ditulis singkat, sebagai validasi bahwa definisi di atas sudah cukup jelas untuk dieksekusi ulang)*

## 6. Log Keputusan Model Konten

*(Sama seperti Log Keputusan di Channel Brief, tapi khusus perubahan di level model konten ini. Tabel ini tetap dipertahankan meskipun ada git history — beda level detail.)*

| Tanggal | Keputusan | Alasan |
|---|---|---|
| | | |
