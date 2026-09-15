# 11 — Log Sesi Berkelanjutan (LOG_SESI)

> **Dokumen instruksi AKTIF & SELF-CONTAINED** (diturunkan dari _meta/PROTOKOL_CHECKPOINT_RECOVERY.md bagian "Log Sesi Berkelanjutan" + _meta/TEMPLATE_LOG_SESI.md, keduanya di master — provenance; format dan aturan yang dipakai ada lengkap di dokumen ini). Berlaku untuk SEMUA sesi di sistem ini, di scope mana pun (deck, level sistem, atau level repo).

## Kenapa ada aturan ini

Sesi lmarena bisa crash kapan saja (error, tidak bisa lanjut, kadang tidak bisa dibuka lagi), dan **agent sesi baru tidak punya akses ke chat sesi lama** — ingatan yang bertahan hanya file di repo. Konteks penting (keputusan, koreksi, fakta, state kerja) yang belum jadi file hilang permanen. Mekanisme lama "checkpoint kalau diskusi >5 giliran mendekati keputusan" digantikan karena berbasis ambang+judgment: sebelum ambang tercapai, tidak ada yang tercatat.

**Prinsip: pencatatan adalah mode normal, bukan mekanisme darurat.**

## Aturan

1. **Satu file per sesi:** `LOG_SESI_YYYY-MM-DD.md` (suffix `_2` kalau dua sesi sehari), di folder scope kerja:
   - kerja deck → `deck-aktif/<nama-deck>/`
   - kerja level sistem → akar folder sistem ini
   - kerja lintas-sistem/level repo → folder `_log-sesi/` di root repo (bukan di root langsung)
2. **Update + commit + push segera** setelah tiap pertukaran yang menghasilkan informasi baru — bukan mekanis tiap giliran.
3. **Header "Keadaan Sesi" di atas file selalu segar** (agent baru membaca INI dulu, bukan seluruh kronologi): di mana kita sekarang, apa yang sudah disepakati, apa yang masih terbuka, langkah berikutnya.
4. **Akhir sesi** (prompt penutup di `PANDUAN_PENGGUNA.md`): header diisi final → `CLOSED` (atau `OPEN` + "dilanjutkan di mana").
5. **Entry point sesi baru** (langkah 5 prompt pembuka): cari `LOG_SESI_*.md` terbaru; yang `OPEN` → baca, laporkan keadaan, konfirmasi ke pengguna sebelum lanjut. Jangan bertanya ulang konteks yang sudah tercatat.

## Format file

```markdown
# Log Sesi — [YYYY-MM-DD] (sesi/branch: [arena/...])

## Keadaan Sesi (selalu segar — agent baru BACA INI DULU)
- **Keadaan:** `OPEN` | `CLOSED`
- **Scope:** [deck: <path> / sistem / repo]
- **Di mana kita sekarang:** [1–3 baris]
- **Sudah disepakati:** [bullet]
- **Masih terbuka / tertunda:** [bullet]
- **Langkah berikutnya:** [1 baris]

## Kronologi (append, terbaru di bawah)
### [HH:MM] — [topik]
- **Pengguna:** [pernyataan penting — near-verbatim]
- **Agent:** [proposal/klaim penting + dasar — 1–3 baris]
- **Hasil:** [setuju / ditolak + alasan / terbuka]
```

## Filter anti-bising (WAJIB — inilah yang membuat aturan ini efisien, bukan overkill)

- **CATAT:** keputusan/koreksi/kendala/preferensi pengguna (near-verbatim, bukan parafrase bebas — prinsip 05); proposal/klaim penting agent + dasarnya; kesepakatan & penolakan + alasan; fakta/hasil verifikasi yang ditemukan sesi ini; perubahan state kerja (unit baru, tahap, blocker); pertanyaan terbuka.
- **JANGAN CATAT:** konfirmasi ("oke", "siap"), basa-basi, pengulangan isi yang sudah ada di `STATUS.md`/Log Keputusan deck (tunjuk path-nya), dump chat mentah.
- **Biaya vs manfaat:** over-recording = beberapa detik per pertukaran; under-recording = hilangnya jam konteks. Floor tetap aman: bahkan pencatatan minimum (keputusan + keadaan) sudah menyelamatkan sebagian besar nilai.

## Batas kejujuran

- Log tidak boleh digunakan untuk MENGAKU hal yang tidak terjadi (prinsip 05). Kalau sesi crash dan log kosong/tidak ada, laporkan celahnya — jangan mengarang konteks.
- Keputusan besar tetap butuh approval pengguna di tempatnya (G1/G2/G3, Log Keputusan) — log sesi bukan pengganti approval, ia hanya menjaga konteksnya tidak hilang.

## Log
| Tanggal | Keputusan | Oleh |
|---|---|---|
| 2026-09-05 | Dokumen dibuat; aturan LOG_SESI diturunkan ke sistem ini (meta v1.2.0); eksperimen live pertama: `LOG_SESI_2026-09-05.md` di root repo | agent+pengguna |
