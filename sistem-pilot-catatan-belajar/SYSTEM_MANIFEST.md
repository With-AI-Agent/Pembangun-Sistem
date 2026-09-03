# System Manifest — Pilot Catatan Belajar

- **Status:** `pilot-only — not released`
- **Versi:** `0.1.0-pilot`
- **Tujuan:** mengubah satu bahan belajar menjadi catatan terstruktur, pertanyaan pemahaman, dan langkah tindak lanjut tanpa kehilangan sumber atau tingkat kepastian.
- **Consumer:** pengguna pribadi dan agent.
- **Bentuk:** gabungan flat + siklus; tidak memiliki hierarki domain seperti Sistem Konten Kreator.
- **Unit kerja:** satu bahan belajar yang diproses.
- **Output utama:** satu catatan belajar yang dapat ditinjau dan ditelusuri kembali ke sumber.
- **Entry point:** `START_DI_SINI.md`
- **Instruksi workflow:** `WORKFLOW.md`
- **Template output:** `OUTPUT_TEMPLATE.md`
- **Quality protocol:** `QUALITY.md`
- **Override quality protocol:** tidak ada
- **Level audit default:** Ringan untuk catatan biasa; Mendalam jika sumber berisiko, output dipakai sebagai keputusan, atau failure berulang
- **Trigger audit:** klaim tidak terlacak, kesalahan berulang, perubahan workflow, atau permintaan pengguna

## Prinsip yang Dipakai

| Prinsip | Berlaku? | Penerapan |
|---|---|---|
| Hierarki | Tidak | Bentuk pilot tidak memiliki level turunan; jangan dipaksakan |
| Chaining | Ya | Setiap tahap mengambil output resmi tahap sebelumnya |
| Approval bertingkat | Ya | Catatan dan kesimpulan dipisahkan dari persetujuan penggunaan |
| Checkpoint & recovery | Ya | `STATUS.md` wajib diperbarui setelah setiap tahap |
| Log keputusan | Ya | Perubahan aturan dan keputusan interpretasi dicatat |
| Quality assurance & evolusi | Ya | `QUALITY.md` mengatur self-audit dan verifikasi output |

## Risiko Utama

- Agent mengubah fakta sumber menjadi kesimpulan tanpa menandai inferensi.
- Sumber tidak tercatat sehingga catatan tidak dapat diverifikasi.
- Catatan terlihat selesai padahal pertanyaan pemahaman belum diuji.
- Sesi terputus sebelum output disimpan.

## Status Pilot

- [x] Bentuk dasar ditentukan
- [x] Manifest dibuat
- [x] Workflow dibuat
- [x] Kontrak output dibuat
- [x] Quality loop dibuat
- [ ] Pilot dijalankan dengan bahan nyata
- [ ] Acceptance tests selesai
- [ ] Disetujui untuk dirilis
