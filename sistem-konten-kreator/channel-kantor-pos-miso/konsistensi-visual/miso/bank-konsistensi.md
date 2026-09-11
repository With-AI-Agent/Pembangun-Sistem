# Bank Konsistensi Visual — Miso

### Dibangun via `04_CHARACTER_BUILDER_KIT.md` — 2026-09-11_3. Elemen milik channel `channel-kantor-pos-miso` (1 channel saja — tidak lintas-channel).

**Status:** `Draft` — Reference-Ready setelah `referensi/acuan-utama.png` + `referensi/reference-sheet.png` benar-benar ada di folder ini.

## Jenis Elemen

Karakter — **Tipe A** (karakter utama channel, permanen, reusable lintas-konten). Muncul di SETIAP konten channel — permintaan eksplisit pemilik.

## Deskripsi (Prompt-Ready)

Miso, kucing jantan muda berusia 1-2 tahun dengan wajah bulat berpipi tembam, bulu krem hangat dengan loreng tabby oranye pudar di punggung, kepala, dan ekor, mata amber besar yang ekspresif, hidung merah muda gelap, **keempat kaki "berkaus kaki" putih bersih dan ujung ekor putih** (ciri khas pengenal utama), gerakan lincah tapi agak canggung — seperti kucing remaja yang baru lulus jadi petugas. Seragam kebesaran: **rompi pos biru navy gelap dengan dua kancing kuningan** dan **tas selempang kulit merah bertali melintang dada dengan gesper kuningan dan lonceng kecil** yang selalu dipakainya di luar & saat tugas. Ekspresi default: mata menyipit setengah tersenyum, kepala sedikit miring.

Poin ciri khas yang TIDAK boleh hilang di generate manapun: (1) kaus kaki putih 4 kaki + ujung ekor putih; (2) tas selempang merah + lonceng kecil; (3) rompi navy 2 kuningan; (4) loreng oranye pudar (bukan oranye terang); (5) pipi bulat.

## Kepribadian

- **Sifat inti:** teliti-dan-cinta-aturan (melipat & menghitung ulang surat tiap malam); lambat-paham-tapi-ulet (bisa mengulang pertanyaan dalam hati, tapi tidak pernah menyerah pada satu alamat); empati-tinggi (tidak bisa buru-buru pergi dari orang yang baru menerima surat penting); mudah-sepi-tapi-menyangkalnya; pemberani-kecil (berani di hal-hal kecil yang tidak dianggap siapa-siapa).
- **Motivasi:** jadi petugas pos yang bisa diandalkan — ingin dipercaya atas "satu surat", sekecil apa pun.
- **Kelemahan/manusiawi:** tidak bisa menolak permintaan; sering terlalu menyelami cerita orang lain sampai tugasnya sendiri menumpuk; takut hujan (bukan karena air — karena surat bisa basah).

## Voice Profile

- Default: **tanpa dialog verbal.** "Suara" Miso = tindakan & ekspresi: mengecap surat, memiringkan kepala, mengetukkan ekor, menutup jendela dengan dua tangan. Maksimal bunyi "nya~" pendek natural.
- Narator channel-lah yang menerjemahkan isi kepala Miso (lihat Persona & Voice di `../../channel-brief.md` bagian 3).
- **Kelonggaran terkunci:** satu kalimat verbal Miso boleh dipakai hanya bila diputuskan di Tahap 2 konsep episode, tercatat di naskah, maks 1× per episode, tidak di 10 episode pertama.
- **Yang TIDAK PERNAH dilakukan/dikatakan Miso (anti-OOC):** sarkasme & sinisme; menertawakan kegagalan orang; monolog panjang; memohon; menyerah pada surat yang tersesat; bermusuhan dengan tokoh lain lebih dari satu adegan kecil.
- Contoh gaya naskah yang SESUAI: *"Miso memiringkan kepalanya. Surat itu salah alamat — tapi entah kenapa, ia melipatnya kembali ke tempat paling aman di tasnya."* — Yang TIDAK SESUAI: *"[Miso berteriak] 'Hei! Kamu tidak bisa melakukan ini padaku!'"*

## Gaya Visual

Picture-book era keemasan: watercolor wash + gouache lembut, garis pensil grafit halus (BUKAN outline hitam tebal), grain kertas, warna sedikit luntur di tepi objek, cahaya sore/pagi keemasan yang difusi. Palet & aturan render dikunci terpisah di `../palet-gaya-catok/bank-konsistensi.md`.

## Prompt Master (Reusable)

> Copy PERSIS sebagai anchor awal, baru tambah detail unit (pose/ekspresi/environment/angle). Jangan diringkas dari ingatan sesi.

```
Miso, a young male cat, 1-2 years old, round chubby cheeks, warm cream fur
with faded soft-orange tabby stripes on back, head and tail, big expressive
amber eyes, dark pink nose, white socks on all four paws, white tail tip,
wearing a slightly oversized dark navy postman vest with two brass buttons
and a red leather shoulder satchel with crossed strap, brass buckle and a
tiny bell, playful-but-clumsy young posture, picture-book watercolor and
gouache illustration, soft graphite pencil outlines, matte paper grain,
muted warm palette, diffused golden light, gentle wholesome storybook mood
```

## Referensi

- `referensi/acuan-utama.png` — Miso berdiri default, tas terpasang, netral-default (WAJIB — sudah ada setelah Tahap 2 sesi ini)
- `referensi/reference-sheet.png` — grid turnaround (4 sudut) + ekspresi (senang, bingung, kaget, fokus, hangat)

## Log Keputusan Elemen

| Tanggal | Keputusan | Alasan |
|---|---|---|
| 2026-09-11 | Fisik final: krem-oranye soft tabby, muda-gemulai, kaus kaki 4 + ujung ekor putih, jantan | Pilihan pemilik di Discovery karakter (`krem_oranye`, `muda_gemulai`, `kaus_kaki`, `jantan`) |
| 2026-09-11 | Gender jantan tapi naskah tetap pakai "si Miso"/"dia" netral | Permintaan pemilik `jantan` — atribut gender tidak ditonjolkan di naskah |
