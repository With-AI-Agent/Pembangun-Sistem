# Tahap 4 — Breakdown Output — Surat Salah Alamat ke Rumah dengan Jendela Biru

**Channel:** Kantor Pos Miso  
**Model:** Dongeng 60-90 Detik  
**Naskah sumber:** `naskah-draft.md` — G2 naskah final disetujui 2026-09-12  
**Status:** breakdown siap direview; G1 + G2 breakdown belum

## Kontrak output

- **Unit:** 7 shot = 7 still image vertikal 9:16; target generate 768×1376 lalu di-upscale/crop di editor bila perlu.
- **Miso:** terlihat pada 7 dari 7 shot, termasuk shot 1 dan shot 7; tas merah mengikuti Miso setiap kali muncul.
- **Tipe B:** dua Tipe B: Penghuni Rumah No. 18 dan Penerima di Rumah No. 81. Deskripsi fisik yang sama diulang verbatim pada semua prompt yang menampilkan karakter terkait.
- **Gerak akhir:** Ken Burns ≤6% dan crossfade 0,4–0,6 detik dilakukan di editor eksternal; agent menyiapkan gambar diam dan arahan.
- **Teks dalam gambar:** alamat, tanggal, dan tulisan surat tidak boleh dibuat terbaca; informasi plot dibawa oleh VO.

## Anchor Prompt Master (dipakai verbatim)

Prompt final setiap shot adalah gabungan anchor yang disebut di blok shot + detail shot. Anchor lengkap yang wajib ditempel saat generate:

### Anchor Miso
```text
Miso, a young male cat, 1-2 years old, round chubby cheeks, warm cream fur
with faded soft-orange tabby stripes on back, head and tail, big expressive
amber eyes, dark pink nose, white socks on all four paws, white tail tip,
wearing a slightly oversized dark navy postman vest with two brass buttons
and a red leather shoulder satchel with crossed strap, brass buckle and a
tiny bell, playful-but-clumsy young posture, picture-book watercolor and
gouache illustration, soft graphite pencil outlines, matte paper grain,
muted warm palette, diffused golden light, gentle wholesome storybook mood
```

### Anchor Kota Kanala
```text
old fictional timeless town called Kanala, one-story terracotta brick
post office building with tall dark-wood arched windows, bottle-green
wooden door with a large brass mail slot, a freshly polished terracotta
wall clock above the door, weathered faded green vintage mailbox leaning
slightly at the front steps, narrow cobblestone lanes with soft grass
growing between stones, small shop fronts with canvas awnings and bottle
green display windows and brass lamps, low stone canal wall with still
water in the far background, old gentle rooftops with tiny antennas and a
towel hanging in a side lane, no cars, only old bicycles, picture-book
watercolor and gouache illustration, soft graphite pencil outlines, matte
paper grain, muted warm palette (cream paper, terracotta, bottle green,
brass gold, warm gray sky), diffused golden dusk light, quiet wholesome
storybook mood
```

### Anchor Props
```text
red brick-colored leather postman satchel with rounded puffed flap, single
crossed shoulder strap, small brass buckle with a tiny marble-sized brass
bell, softly worn bottom edges, slightly too big for its young owner; old
bottle-green bicycle with a wicker basket full of letters on the handlebar,
brown leather saddle and brass bell, leaning without a kickstand; vintage
brass postmark stamp with dark wooden handle; faded green vintage street
mailbox with chipped paint leaning slightly, large brass mail slot; all
items together as a character's belonging set; picture-book watercolor and
gouache illustration, soft graphite pencil outlines, matte paper grain,
muted warm palette, diffused golden light
```

### Anchor Palet & Gaya Catok
```text
picture-book watercolor and gouache illustration, soft graphite pencil
outlines, matte paper grain, colors slightly bleeding at edges, muted warm
storybook palette (paper cream #EFE3CE, terracotta #C9764F, bottle green
#3B5C4F, brass gold #C79A3B, brick red #B04A3A as accent, faded orange
#CB8B58, warm gray #A99E93, ink blue shadow #4C5D70), diffused golden
light, quiet tender storybook mood, no thick black outlines, no 3D render,
no neon, no glossy highlight, no pure black, no pure white
```

### Negative universal
```text
No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

Semua anchor di atas bersumber dari Bank Konsistensi Visual `Reference-Ready`; prompt unit di bawah menentukan urutan dan detail spesifiknya.

## Daftar shot

### Shot 1 — Miso terlihat

**Bagian naskah terkait:** “Di Kota Kanala, ada surat yang salah alamat—tetapi tidak salah menemukan seseorang.”

**Deskripsi visual:** Miso berdiri 3/4 di depan Kantor Pos Kanala pada pagi keemasan, memegang amplop terlipat; tas merah, lonceng, dan kotak pos hijau pudar terlihat.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: full-body three-quarter view of Miso standing at the Kanala post office entrance in soft golden morning light, holding one slightly folded unmarked envelope in both paws, curious head tilt, faded green mailbox on the steps, calm vertical composition, clean paper-colored space around the subject
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-eksterior-kantor-pos.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`

**Arahan VO / Ken Burns:** Pembuka pelan; zoom-in ≤6% ke amplop lalu tahan pada ekspresi Miso.

### Shot 2 — Miso terlihat

**Bagian naskah terkait:** “Pagi itu, Miso menemukan satu amplop di bawah tumpukan surat biasa.”

**Deskripsi visual:** Interior lobby; Miso membuka laci arsip rendah, amplop tua terlihat tanpa tulisan terbaca, cahaya jendela tinggi dan cap kuningan menjadi fokus sekunder.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso crouching carefully inside the Kanala post office lobby, opening a low wooden drawer beneath letter shelves, one folded unmarked envelope beneath ordinary mail, vintage brass postmark stamp on the counter, tall window light, focused gentle expression
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/reference-sheet.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-interior-lobby.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`

**Arahan VO / Ken Burns:** Pan pelan dari laci ke wajah Miso; jangan mengandalkan teks pada gambar.

### Shot 3 — Miso terlihat

**Bagian naskah terkait:** “Dengan tas merah bergoyang kecil, Miso mengayuh sepeda melewati batu-batu.”

**Deskripsi visual:** Miso mengendarai sepeda di gang menuju pintu rumah; Penghuni No. 18 membuka pintu, perempuan kecil berkardigan hijau tampak lembut.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso riding the old bottle-green bicycle slowly along a narrow cobblestone lane toward a modest house door, the same petite adult woman standing there: short black hair with one small brass hair clip, faded green cardigan, careful movement and an easy gentle smile, soft background figure, no readable house number
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/reference-sheet.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-jalan-senja.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`

**Arahan VO / Ken Burns:** Crossfade saat sepeda masuk; pan kiri ke kanan mengikuti gang.

### Shot 4 — Miso terlihat

**Bagian naskah terkait:** “Nama itu tidak tinggal di sana lagi.”

**Deskripsi visual:** Miso duduk di tepi kanal, memeriksa cap kuningan dan amplop; jendela botol hijau dan rumput di sela batu menjadi latar hening.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso sitting beside a low stone canal wall, carefully checking the brass postmark and an unmarked envelope with one paw, tail tip visible, head tilted in thoughtful confusion, bottle-green windows and soft grass between cobblestones behind him, quiet morning light, no readable writing
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/reference-sheet.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-jalan-senja.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`

**Arahan VO / Ken Burns:** Tahan 0,5 detik pada gerakan Miso memeriksa cap; zoom-out kecil membuka ruang kanal.

### Shot 5 — Miso terlihat

**Bagian naskah terkait:** “Rumah yang dicari ada di seberang kanal—rumah dengan jendela biru.”

**Deskripsi visual:** Miso dan Penghuni No. 18 menyeberangi jembatan batu; perempuan berkardigan hijau menunjuk rumah berjendela biru tertutup tanaman rambat.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso walking beside the same petite adult woman with short black hair, one brass hair clip and faded green cardigan, across a small old stone footbridge over the quiet canal; Miso holds one unmarked envelope, the woman gently points toward a modest house with a blue window partly covered by vines, no readable number
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/reference-sheet.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-jalan-senja.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`

**Arahan VO / Ken Burns:** Pan mengikuti langkah mereka; jeda sebelum frasa “jendela biru”.

### Shot 6 — Miso terlihat

**Bagian naskah terkait:** “Di depan pintu, penerima surat berdiri lama sebelum membukanya.”

**Deskripsi visual:** Di ambang rumah biru, Miso berdiri; Penghuni No. 18 menyerahkan amplop kepada Penerima No. 81, perempuan berambut kelabu dikepang dengan blus krem.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso standing quietly at the doorway of a vine-covered house with a blue window; the same petite woman with short black hair, one brass hair clip and faded green cardigan gently hands an unmarked envelope to the recipient, an adult woman with long simply braided gray hair and a cream blouse, calm hesitant face beginning to smile, warm doorway light, no readable writing
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/reference-sheet.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-eksterior-kantor-pos.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`

**Arahan VO / Ken Burns:** Crossfade saat amplop berpindah tangan; tahan pada tiga ekspresi lembut.

### Shot 7 — Miso terlihat

**Bagian naskah terkait:** “Dua orang akhirnya duduk di ambang pintu. Miso mengetukkan ekornya, lalu kembali ke sepedanya.”

**Deskripsi visual:** Miso menaiki sepeda di jalan pulang saat senja; dua siluet samar duduk hangat di rumah biru di belakang, Miso tetap foreground utama.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso riding away on the old bottle-green bicycle at quiet warm dusk, red satchel and tiny brass bell visible, looking back with a small satisfied smile; two soft indistinct adult figures sit together at the blue-window house in the distant background, gentle Kanala lane and canal, Miso clear in the foreground
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/miso/referensi/reference-sheet.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-jalan-senja.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`

**Arahan VO / Ken Burns:** Zoom-out ≤6% menuju jalan pulang; VO melambat di “sedikit lebih jauh” dan penutup.

## Checklist Tahap 4

- [x] Naskah dipecah menjadi 7 unit shot.
- [x] Miso tampil pada minimal 4 shot, termasuk shot pertama dan terakhir.
- [x] Setiap prompt merujuk anchor Bank Konsistensi Visual dan negative universal.
- [x] File referensi tercantum per shot; tidak ada kolom referensi kosong.
- [x] Deskripsi karakter Tipe B konsisten pada semua shot yang relevan.
- [x] Tidak ada sumber eksternal atau klaim faktual yang memerlukan `SUMBER.md`.
- [ ] G1 breakdown — belum.
- [ ] G2 breakdown sebagai dasar generate — belum.

**Next:** minta G1 untuk validasi struktur dan G2 untuk mengunci breakdown sebelum menghasilkan aset.
