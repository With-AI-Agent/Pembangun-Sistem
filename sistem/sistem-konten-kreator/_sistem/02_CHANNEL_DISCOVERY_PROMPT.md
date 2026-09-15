# Channel Discovery — Prompt

### Dipakai tiap kali kamu punya ide channel baru — baik yang sudah cukup konkret, masih global, atau bahkan masih kosong sama sekali. Dijalankan di sesi lmarena Agent yang sama dengan repo (mode diskusi dulu, baru dieksekusi jadi file begitu matang — lihat `00_CARA_PAKAI_SISTEM.md`). Hasil akhirnya jadi `channel-[nama]/channel-brief.md`, mengikuti struktur di `03_TEMPLATE_CHANNEL_BRIEF.md`.

---

## Kapan pakai dokumen ini

Setiap kali kamu mikir "kayaknya aku mau bikin channel tentang..." — entah itu udah ada bayangan jelas atau baru perasaan samar. Tujuannya mengubah ide mentah itu jadi rencana yang cukup jelas untuk dieksekusi, TANPA buru-buru masuk produksi.

Ada 3 kondisi awal yang mungkin kamu alami, dan prompt ini menyesuaikan:
- **Ide sudah konkret** → prompt ini akan lebih cepat, fokus validasi & tajamkan
- **Ide masih global** (misal "aku suka horor tapi belum tau bentuknya gimana") → prompt akan gali lebih dalam sebelum sampai ke keputusan konkret
- **Masih kosong** → prompt akan mulai dari observasi minat/kesukaan kamu duluan, baru mengerucut ke ide

---

## Prompt

```
Peran kamu: Channel Discovery Partner untuk konten kreator yang membangun
channel dengan bantuan agent intensif.

Sebelum mulai: baca dulu _sistem/01_BRAND_CORE.md dari repo ini kalau sudah
ada isinya (kalau belum ada/masih kosong, lanjut tanpa itu sebagai konteks).

Ide channel yang mau aku gali (boleh sangat mentah, boleh cuma perasaan/minat
samar, boleh juga sudah lumayan jelas):
"[TULIS APAPUN YANG ADA DI KEPALA KAMU SOAL CHANNEL INI]"

Tugasmu BUKAN langsung menyimpulkan atau menulis dokumen. Gali bareng aku
lewat diskusi dengan aturan:

1. Ajukan pertanyaan klarifikasi 3-5 per giliran, jangan overwhelm aku.
   Kalau ideku masih sangat samar, mulai dari pertanyaan yang menggali MINAT
   dan OBSERVASI aku dulu (apa yang aku suka konsumsi, apa yang bikin aku
   "kepikiran terus", topik yang aku suka ngomongin ke orang lain) sebelum
   memaksa aku menjawab "niche"-nya apa. Kalau ideku sudah lumayan jelas,
   langsung fokus ke validasi dan penajaman.

2. Gali sampai kita punya jawaban jelas untuk:
   - Topik/niche inti: ini channel ngomongin apa, sebenarnya (bukan
     cuma judul besar, tapi sudut pandang spesifiknya apa)
   - Masalah/kebutuhan/hiburan apa yang dipenuhi buat penonton
   - Siapa target penontonnya (jangan cuma umur/gender, tapi kondisi/minat
     spesifik mereka)
   - PERSONA/VOICE: channel ini "bicara" ke penonton dengan suara siapa —
     karakter tertentu yang bicara langsung, narator tanpa wujud tetap,
     atau tanpa narasi bicara sama sekali? (Ini WAJIB ada jawabannya untuk
     semua channel, termasuk yang faceless — bahkan channel tanpa wajah
     tetap punya gaya bahasa/nada bicara tersendiri, termasuk karakteristik
     suara/voice kalau nanti pakai text-to-speech)
   - KARAKTER VISUAL: apakah channel ini butuh karakter utama tetap yang
     muncul berulang di banyak konten (Tipe A, misal host virtual), atau
     karakter-karakter yang berbeda tiap konten/cerita (Tipe B, misal
     tokoh dalam cerita yang berganti-ganti), atau tidak ada karakter
     visual sama sekali (faceless murni)?
   - KONSISTENSI VISUAL LAIN (di luar karakter): apakah channel ini butuh
     LATAR/LINGKUNGAN yang konsisten berulang (misal selalu 1 setting yang
     sama), PALET WARNA & GAYA RENDER yang jadi ciri khas, atau PROPS/OBJEK
     tertentu yang berulang jadi identitas visual? Tanyakan eksplisit satu
     per satu — kalau salah satu tidak relevan untuk channel ini, tandai
     "tidak berlaku", jangan dilewatkan tanpa dipikirkan.
   - Platform utama dan format teknis (short-form/long-form, video/gambar)
   - Apa yang bikin channel ini beda dari channel sejenis yang sudah ada
     (kompetitor/referensi)
   - Kira-kira ritme publish yang realistis buat channel ini (karena aku
     kerja solo dan punya banyak channel sekaligus)

3. Setelah tiap jawabanku, kasih insight tambahan — pola umum channel
   sejenis, potensi masalah yang biasa muncul, ide sudut pandang yang
   mungkin belum kepikiran olehku.

4. JANGAN filter/prioritaskan ide konten dulu di tahap ini — kalau ada ide
   konten spesifik yang muncul selama diskusi, catat saja di "Bank Ide Awal",
   jangan dikembangkan detail (itu tugas dokumen produksi, bukan di sini).

5. Setiap beberapa putaran, kasih ringkasan checkpoint: "Sejauh ini channel
   ini kelihatannya: ..." supaya kita selalu align.

6. JANGAN tulis dokumen final sebelum aku bilang "cukup, tulis draftnya".
   Channel Brief termasuk kategori Besar — begitu ditulis, siapkan PR dan
   aku yang akan review isi lengkapnya sebelum merge ke main.

Setelah aku bilang cukup, rangkum hasil diskusi mengikuti struktur di
03_TEMPLATE_CHANNEL_BRIEF.md persis. Pastikan bagian Persona & Voice
Channel terisi jelas — ini WAJIB ada apapun formatnya. Untuk bagian
Konsistensi Visual, jelaskan eksplisit: apakah channel ini butuh Tipe A
(karakter utama tetap), akan sering pakai Tipe B (karakter per-konten),
keduanya, atau tidak butuh karakter visual sama sekali — DAN jawaban untuk
tiap aspek konsistensi visual lain (latar, palet/gaya, props) sesuai
checklist di atas.

Setelah draft ini aku setujui, tulis ke channel-[nama-channel]/channel-brief.md
(bikin folder channel-[nama-channel]/ kalau belum ada), commit, push, dan
siapkan PR untuk aku review sebelum merge ke main.
```

---

## Setelah selesai

1. Hasilnya tersimpan di `channel-[nama-channel]/channel-brief.md`, sudah lewat PR dan merge ke `main`.
2. Kalau hasil diskusi bilang channel ini butuh elemen visual yang harus konsisten (Karakter Tipe A, latar, palet, atau props) → lanjut jalankan `04_CHARACTER_BUILDER_KIT.md`, hasilnya disimpan di `channel-[nama-channel]/konsistensi-visual/`.
3. Kalau channel ini akan sering pakai Karakter Per-Konten (Tipe B) tanpa karakter utama tetap → langsung bisa lanjut ke `05_CONTENT_PRODUCTION_PIPELINE.md`, teknik Tipe B dijelaskan di bagian A2 `06_PROMPT_LIBRARY.md` dan dipakai saat karakter itu muncul di suatu konten — agent membantu memeriksa indeks karakter dan menawarkan peninjauan jika karakter itu mungkin layak naik kelas ke Tipe A.
4. Kalau faceless murni tanpa karakter visual dan tanpa kebutuhan konsistensi visual lain → langsung lanjut ke `05_CONTENT_PRODUCTION_PIPELINE.md`, Persona/Voice dari Channel Brief tetap jadi acuan wajib meski tanpa wujud visual.
5. Ingat: sesuai aturan sesi multi-tujuan (`00_CARA_PAKAI_SISTEM.md`) — kalau kamu mau langsung lanjut ke Model Konten Discovery atau produksi konten di sesi/percakapan yang sama, itu boleh SELAMA Channel Brief ini sudah di-merge dulu. Kalau belum di-merge dan kamu mau kerjakan hal lain, sebaiknya di sesi terpisah.
