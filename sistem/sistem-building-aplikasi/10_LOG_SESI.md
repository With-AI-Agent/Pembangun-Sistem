# 10 — Log Sesi Berkelanjutan (Sistem Building Aplikasi)

> Aturan self-contained sistem ini untuk pemulihan lintas sesi (fakta platform lmarena: sesi bisa crash kapan saja). Turunan dari protokol meta — disalin, bukan dirujuk. Sistem harus tetap berfungsi penuh bila folder diunduh jadi repo standalone.

## Aturan

1. **Setiap sesi memelihara `_log-sesi/` (atau `_log-sesi/` bila 2 sesi di hari sama) — append + commit + push segera setelah tiap pertukaran yang menghasilkan informasi baru.**
2. **Header `## Keadaan Sesi` selalu segar** — di mana kita, apa yang disepakati, apa yang terbuka. Agent baru BACA header ini dulu sebelum tanya apa pun.
3. **Yang dicatat:** keputusan/koreksi/kendala/preferensi pengguna (near-verbatim), proposal penting + dasarnya, kesepakatan & penolakan + alasan, fakta terverifikasi, state kerja, pertanyaan terbuka.
4. **Yang TIDAK dicatat:** konfirmasi, basa-basi, ulang isi STATUS/LOG, dump chat.
5. **Penutupan:** di akhir sesi, ubah header `Keadaan: OPEN` → `CLOSED` (atau `OPEN — dilanjutkan di ...`) dan tambahkan entri kronologi terakhir. Jangan pernah hapus entri lama (append-only; bila butuh koreksi, tambah entri baru yang menyatakan koreksi).
6. **Pemulihan crash:** sesi baru mencari `LOG_SESI` terbaru yang `OPEN` → baca → lanjutkan tanpa menanya ulang. Backstop bila log hilang = `STATUS.md` + `PROJECT_STATE.md`.

## Format LOG_SESI (ringkas — lihat TEMPLATE di _log-sesi/ bila ada)

```markdown
# Log Sesi — YYYY-MM-DD

## Keadaan Sesi (selalu segar)
- **Keadaan:** OPEN / CLOSED
- **Scope:** fondasi Tahap X / coding Fase Y
- **Di mana kita sekarang:** ...
- **Sudah disepakati:** ...
- **Masih terbuka:** ...
- **Langkah berikutnya:** ...

## Kronologi (append, terbaru di bawah)
### YYYY-MM-DD — Peristiwa
- ...
```

## Log Keputusan

| Tanggal | Perubahan | Alasan |
|---|---|---|
| 2026-09-15 | Aturan log sesi ditanam pada run klinik pertama (kit v0.2.0) | W-02: sistem belum punya mekanisme log sesi berkelanjutan — tanpa ini sesi crash = konteks hilang permanen (fakta platform #3) |
