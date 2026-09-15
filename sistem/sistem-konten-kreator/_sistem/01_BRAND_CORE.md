# Brand Core

### Dokumen fondasi lintas-channel. Diisi sekali di awal, direvisi kalau ada pergeseran besar. Ini BUKAN tempat menulis niche/konten spesifik satu channel — itu masuknya ke Channel Brief (dokumen 03). File ini hidup di `_sistem/01_BRAND_CORE.md` di repo, isinya langsung ditulis di file yang sama (bukan file terpisah).

---

## Kenapa dokumen ini perlu ada, padahal kamu bakal punya banyak channel yang beda-beda

Kalau tiap channel benar-benar independen tanpa benang merah, ada beberapa masalah:
- Kamu jadi nggak punya "identitas operator" yang konsisten — tiap channel kerasa dibuat orang berbeda
- Ada keputusan yang sebenarnya berlaku untuk SEMUA channel kamu (misal: nggak mau bikin konten yang menyesatkan/clickbait murni, atau standar kualitas visual minimum) — kalau nggak ditulis di satu tempat, harus diulang-ulang tiap bikin channel baru
- Agent yang bantu kamu kerja nggak akan tau batasan/nilai kamu secara umum kalau cuma dikasih tau di level channel — dan karena file ini ada permanen di repo, agent bisa baca sendiri kapan saja, tidak bergantung pada kamu mengingatkan ulang tiap sesi

Dokumen ini kecil dan jarang berubah — bukan tempat curhat panjang, cukup poin-poin yang benar-benar lintas channel.

---

## Cara Mengisi

Ini sesi **diskusi**, bukan kamu isi form sendirian — biar agent bantu gali supaya jawabannya nggak dangkal. Jalankan prompt di bawah ini langsung di sesi lmarena Agent yang sama dengan repo kamu — TIDAK perlu pindah ke platform/chat lain.

**Instruksi untuk agent:** proses ini WAJIB berupa diskusi bolak-balik dulu, BUKAN langsung ditulis ke file di percobaan pertama. Tulis ke `_sistem/01_BRAND_CORE.md` HANYA setelah pengguna eksplisit mengonfirmasi bahwa hasil diskusi sudah final dan siap ditulis. Begitu ditulis, commit, push, dan siapkan PR untuk direview (Brand Core termasuk kategori Besar — pengguna review isi lengkapnya sebelum merge ke `main`).

*(Kalimat spesifik untuk memicu mode diskusi ada di `PANDUAN_PENGGUNA.md` — dokumen ini fokus ke instruksi kerja untuk agent saja.)*

```
Peran kamu: Brand Strategy Partner untuk konten kreator.

Aku mau membangun beberapa channel konten dengan bantuan kamu secara intensif
(riset ide, naskah, visual, video, dst). Sebelum masuk ke channel spesifik,
aku mau menetapkan dulu fondasi yang berlaku di SEMUA channel aku nantinya.

Gali bareng aku lewat diskusi (3-5 pertanyaan per giliran, jangan overwhelm),
sampai kita bisa merumuskan jawaban untuk poin-poin berikut:

1. SIAPA AKU SEBAGAI OPERATOR/KREATOR (bukan channel-nya, tapi akunya)
   - Latar belakang/pengalaman yang relevan (kalau ada) — meskipun aku
     bilang konten ini terpisah dari kerjaan utamaku, mungkin ada nilai/cara
     pandang dari sana yang tetap kebawa
   - Apa yang bikin aku beda dari kreator lain yang bikin konten AI-generated
     (karena makin banyak orang pakai AI, apa yang bikin channel-channel aku
     nggak generik)

2. NILAI & BATASAN YANG BERLAKU DI SEMUA CHANNEL
   - Jenis konten/pendekatan yang TIDAK akan aku buat, apapun channelnya
     (misal: clickbait yang menyesatkan, konten yang eksploitatif, dsb)
   - Standar kualitas minimum yang aku pegang (misal: nggak asal publish
     hasil AI mentah tanpa dicek, atau sebaliknya, prioritas kecepatan
     dibanding kesempurnaan)

3. POSISI AI DALAM PROSES KERJA AKU
   - AI ini alat produksi di belakang layar, bukan niche channel (untuk saat
     ini) — apakah ini akan selalu disembunyikan dari audiens, ditampilkan
     terang-terangan, atau tergantung channel?
   - Batasan penggunaan AI yang aku pegang (misal: naskah boleh full AI tapi
     harus aku edit, atau sebaliknya)

4. GAYA KERJA AKU
   - Aku kerja solo lewat lmarena Agent yang terhubung ke repo GitHub — apakah
     ada preferensi soal ritme kerja atau kapan aku lebih suka diskusi dulu vs
     langsung eksekusi?
   - Ritme kerja yang realistis (harian/mingguan, berapa channel aktif
     bersamaan)
   - Seberapa ketat aku mau review tiap hasil kerja sebelum di-merge — apakah
     ini akan konsisten sepanjang waktu, atau bisa berubah tergantung
     seberapa besar dampak perubahannya (lihat aturan kategori Besar/Kecil di
     00_CARA_PAKAI_SISTEM.md)

Setiap beberapa putaran, kasih ringkasan checkpoint. Setelah aku bilang
"cukup, tulis draftnya", rangkum jadi dokumen final dengan struktur:

# Brand Core

## Tentang Aku Sebagai Kreator
[ringkasan poin 1]

## Nilai & Batasan Lintas Channel
[daftar eksplisit — hal yang TIDAK akan dibuat, standar kualitas minimum]

## Posisi AI dalam Proses Kerja
[bagaimana AI dipakai, terbuka/tertutup ke audiens, batasan]

## Gaya Kerja
[ritme, preferensi diskusi vs eksekusi langsung]

## Catatan Revisi
[kosong di awal — diisi tanggal + apa yang berubah, kalau dokumen ini
direvisi di masa depan]

Setelah draft ini aku setujui, tulis ke file _sistem/01_BRAND_CORE.md
(menggantikan bagian "ISI DENGAN HASIL DISKUSI" di bawah), commit, push, dan
siapkan PR untuk aku review sebelum merge ke main.
```

---

## [ISI DENGAN HASIL DISKUSI DI ATAS — kosong sampai kamu jalankan prompt-nya]

*(Setelah dokumen ini diisi dan di-merge ke `main`, dia jadi rujukan yang dibaca otomatis oleh agent setiap kali memulai Channel Discovery untuk channel baru — lihat Entry Point Universal di `00_CARA_PAKAI_SISTEM.md`. Kamu tidak perlu menempelkan isi file ini secara manual; agent membacanya langsung dari repo.)*
