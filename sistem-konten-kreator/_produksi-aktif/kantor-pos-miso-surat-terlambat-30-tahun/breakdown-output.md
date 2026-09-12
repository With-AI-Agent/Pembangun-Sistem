# Tahap 4 — Breakdown Output — Surat yang Terlambat Tiga Puluh Tahun

**Channel:** Kantor Pos Miso  
**Model:** Dongeng 60-90 Detik  
**Naskah sumber:** `naskah-draft.md` — G2 naskah final disetujui 2026-09-12  
**Status:** breakdown siap direview; G1 + G2 breakdown belum

## Kontrak output

- **Unit:** 7 shot = 7 still image vertikal 9:16; target generate 768×1376 lalu di-upscale/crop di editor bila perlu.
- **Miso:** terlihat pada 6 dari 7 shot, termasuk shot 1 dan shot 7; tas merah mengikuti Miso setiap kali muncul.
- **Tipe B:** satu Tipe B: Pemilik Toko Roti. Deskripsi fisik yang sama diulang verbatim pada semua prompt yang menampilkan karakter terkait.
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

**Bagian naskah terkait:** “Di Kota Kanala, ada surat yang datang setelah penunggunya berhenti menghitung hari.”

**Deskripsi visual:** Miso membuka laci arsip rendah di lobby kantor pos; cahaya pagi dari jendela tinggi menerangi rak kayu.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso crouching inside the Kanala post office lobby, opening a low wooden archive drawer beneath old letter shelves, soft morning light from a tall arched window, curious focused expression, red satchel across his body, quiet dusty paper atmosphere
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

**Arahan VO / Ken Burns:** Pan dari cahaya jendela ke laci; jeda setelah “berhenti menghitung hari”.

### Shot 2 — Miso terlihat

**Bagian naskah terkait:** “Di balik laci arsip, di bawah buku catatan tua, terselip amplop dengan tanggal tiga puluh tahun lalu.”

**Deskripsi visual:** Close-up Miso dan amplop tua tanpa tulisan terbaca; satu kaki berkaus kaki putih menyentuh debu, cap kuningan dan kotak kayu mengisi frame.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: close view of Miso carefully brushing dust from one old unmarked envelope hidden beneath a wooden archive box, one white-socked paw and white tail tip visible, brass postmark stamp nearby, soft paper fibers and warm muted light, no readable date or writing
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

**Arahan VO / Ken Burns:** Zoom-in sangat kecil pada tekstur kertas; tulisan tidak dibuat terbaca.

### Shot 3 — Miso terlihat

**Bagian naskah terkait:** “Miso memasukkan surat itu ke tas merahnya dan mengayuh menuju ujung gang.”

**Deskripsi visual:** Miso bersepeda melewati gang menuju toko roti kecil di ujung jalan; keranjang penuh surat, tas merah, kanal, dan lampu kuningan terlihat.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso riding the old bottle-green bicycle through a narrow Kanala cobblestone lane toward a small warm bakery at the far end, wicker basket with letters, oversized red satchel and tiny bell visible, quiet morning, bottle-green shop fronts and terracotta walls, no readable shop sign
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

**Arahan VO / Ken Burns:** Pan searah laju sepeda; crossfade saat toko roti memenuhi frame.

### Shot 4 — Miso terlihat

**Bagian naskah terkait:** “Rumah yang tertulis di sana sudah berubah menjadi toko roti.”

**Deskripsi visual:** Miso di pintu toko roti; Pemilik Toko Roti, perempuan rambut cokelat dikepang longgar dengan celemek krem bertabur tepung, menerima amplop dengan ragu.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso standing at the entrance of a small timeless Kanala bakery, holding one old unmarked envelope toward the same adult woman with loosely braided dark brown hair, cream apron dusted with flour, nimble hands and a smile beginning only after recognition, warm bread shelves, terracotta doorway, no readable sign
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

**Arahan VO / Ken Burns:** Tahan pada perpindahan amplop; jeda sebelum “tiga puluh tahun”.

### Shot 5 — Miso tidak terlihat

**Bagian naskah terkait:** “Ia memeriksa tanggalnya, lalu membuka lipatan surat.”

**Deskripsi visual:** Close-up tangan Pemilik Toko Roti di meja kayu, surat tua terbuka di samping roti kecil dan buku resep; Miso tidak terlihat agar ritme visual bernafas.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
SHOT DETAIL: close-up of the same adult bakery owner with loosely braided dark brown hair and cream flour-dusted apron, careful hands opening an old unmarked envelope beside a small fresh loaf and a worn recipe book on a wooden counter, warm window light, tender still-life, no readable writing, no modern objects
ANCHOR KOTA KANALA (verbatim, from Bank Konsistensi Visual)
ANCHOR PROPS KANTOR POS MISO (verbatim, from Bank Konsistensi Visual)
ANCHOR PALET & GAYA CATOK (verbatim, from Bank Konsistensi Visual)
NEGATIVE: No legible words, numbers, logos, or real-world brand marks; no modern
vehicles, no horror, no violence, no extra clothing on Miso, no hat, no
thick black outlines, no 3D render, no neon, no glossy digital finish.
```

**File referensi yang wajib disertakan:**
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/kota-kanala/referensi/sudut-interior-lobby.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/props-kantor-pos-miso/referensi/acuan-utama.png`
- `sistem-konten-kreator/channel-kantor-pos-miso/konsistensi-visual/palet-gaya-catok/referensi/style-sheet.png`

**Arahan VO / Ken Burns:** Ken Burns pelan dari roti ke tangan; jeda saat isi surat mulai dibaca.

### Shot 6 — Miso terlihat

**Bagian naskah terkait:** “Pemilik toko roti membaca dekat jendela. Ia tertawa pelan, lalu memberikan Miso roti kecil.”

**Deskripsi visual:** Miso duduk dekat jendela; pemilik yang sama menyimpan surat di buku resep dan menyerahkan roti kecil, cahaya sore hangat, tas merah tetap terpasang.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso sitting politely beside a warm bakery window, the same adult woman with loosely braided dark brown hair and cream flour-dusted apron placing an old unmarked letter into a worn recipe book and offering Miso one small fresh loaf, Miso amber eyes warm and surprised, red satchel and tiny bell visible, gentle afternoon light, no readable writing
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

**Arahan VO / Ken Burns:** Zoom-in ≤6% ke roti kecil lalu ekspresi Miso; VO tetap datar-hangat.

### Shot 7 — Miso terlihat

**Bagian naskah terkait:** “Tidak semua surat tiba tepat waktu. Besok masih ada pos.”

**Deskripsi visual:** Miso mengayuh pulang menuju Kantor Pos Kanala saat senja; roti kecil aman di keranjang, lampu kantor dan kotak pos hijau pudar terlihat, Miso foreground utama.

**Prompt generate final (768×1376, vertikal 9:16):**

```text
ANCHOR MISO (verbatim, from Bank Konsistensi Visual)
SHOT DETAIL: Miso riding home toward the Kanala post office at quiet warm dusk, one small loaf safely in the wicker bicycle basket beside letters, red satchel and tiny brass bell visible, old terracotta post office and faded green mailbox glowing softly in the background, Miso clear in foreground with peaceful tired smile, no readable text
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

**Arahan VO / Ken Burns:** Zoom-out ≤6% saat Miso mendekati kantor; penutup melambat pada “Besok masih ada pos”.

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
