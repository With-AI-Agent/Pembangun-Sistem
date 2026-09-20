# Arsitektur Website Induk

> **STATUS: KERANGKA — BELUM ADA ISI.** Dokumen ini dibuat sebagai bagian dari skeleton folder saat
> `Tahap: kerangka`, **bukan** sebagai dokumen jadi. Mengisinya adalah langkah **sesudah** rencana kerangka
> di-merge (lihat `00_RENCANA_KERANGKA.md` bagian 11).

| | |
|---|---|
| **Berkas** | `10_ARSITEKTUR_WEBSITE_INDUK.md` |
| **Lapis** | lintas semua lapis |
| **Cara diisi** | **YA — perlu prompt Discovery detail** (keputusan arsitektur besar) |
| **Sumber keputusan** | `00_RENCANA_KERANGKA.md` (rencana induk sistem ini) |

## Fungsi dokumen ini

**Website induk** yang mengelola semua undangan + datanya: **satu domain + undangan sebagai subpath**, Cloudflare Pages/Workers/D1/KV/R2 dengan **plafon free tier terukur**, dan **kebijakan domain 3 fase** (percobaan = subdomain gratis · rilis = satu domain · pengecualian = client mau domain sendiri **menanggung biayanya**).

## Catatan untuk yang mengisinya nanti

Plafon free tier sudah terukur di DISKUSI_MENTAH bagian **H** — pakai angka itu, jangan perkiraan. Kendala pengikat pemilik: **nol biaya bulanan**.

## Isi

*(kosong — belum diisi. Jangan menaruh isi di sini sebelum cara pengisiannya di atas dijalankan,
supaya tidak ada keputusan yang lahir tanpa tercatat di Log Keputusan.)*

## Log Keputusan dokumen ini

| Tanggal | Keputusan | Alasan / approval |
|---|---|---|
| — | — | — |
