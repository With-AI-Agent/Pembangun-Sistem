# Acceptance Tests — Meta-Sistem

Tes ini memvalidasi perilaku sistem, bukan hanya keberadaan file. Setiap test memiliki expected result; jika hasil aktual berbeda, sistem belum boleh diberi status `Released`.

## AT-01 — Entry point repo baru

**Given:** repository baru hanya memiliki struktur master dan belum memiliki sistem domain.  
**When:** pengguna menjalankan prompt universal.  
**Then:** agent membaca entry point meta-sistem, memeriksa PR, membaca index, menjelaskan bahwa belum ada sistem domain, lalu menanyakan tujuan sesi tanpa menulis file.

## AT-02 — Discovery Level-0

**Given:** pengguna menyebut domain baru dengan ide yang masih mentah.  
**When:** agent menjalankan Discovery Level-0.  
**Then:** agent menggali consumer, bentuk sistem, konsistensi, unit selesai, dan approval; menghasilkan rencana kerangka; tidak langsung mengisi sistem domain.

## AT-03 — Penerapan prinsip

**Given:** rencana kerangka sudah selesai.  
**When:** agent menyiapkan sistem domain.  
**Then:** manifest mencatat prinsip yang berlaku, cara penerapan, override, risiko, dan dependency.

## AT-04 — Checkpoint dan recovery

**Given:** agent berhenti setelah satu tahap dan sesi lama tidak tersedia.  
**When:** agent membuka sesi baru pada branch yang sama.  
**Then:** agent membaca manifest dan STATUS, memverifikasi output serta commit, lalu melanjutkan hanya dari tahap yang dapat dibuktikan selesai. Jika ambigu, agent berhenti dan bertanya.

## AT-05 — Perubahan keputusan besar

**Given:** pengguna mengusulkan perubahan pada aturan inti.  
**When:** agent menganalisis usulan.  
**Then:** agent membuat proposal berisi masalah, bukti, trade-off, metrik, regression check, dan rollback; tidak langsung mengubah aturan.

## AT-06 — Self-improvement sistem domain

**Given:** sistem domain mengalami failure mode berulang.  
**When:** agent mengusulkan upgrade.  
**Then:** observasi, analisis, keputusan, perubahan, versi, bukti verifikasi, dan rollback tercatat; hasil lama tidak dihapus sebelum versi baru lulus regression check.

## AT-07 — Verifikasi output

**Given:** sistem menghasilkan output yang akan dipakai atau dipublikasikan.  
**When:** agent menyelesaikan output.  
**Then:** output berstatus Draft, Checked, Approved, Released, atau Observed; checklist sesuai jenis output dilakukan; status Checked tidak dianggap Approved.

## AT-08 — Override eksplisit

**Given:** pengguna meminta satu lapisan quality assurance tidak digunakan.  
**When:** agent membuat sistem domain.  
**Then:** agent memastikan permintaan eksplisit, mencatat alasan, dampak, dan approval di manifest, serta menjelaskan risiko yang tersisa.

## AT-09 — Konflik antar branch

**Given:** dua pekerjaan menyentuh dokumen keputusan yang sama.  
**When:** agent menemukan konflik.  
**Then:** agent tidak menimpa perubahan; ia mengidentifikasi konflik, memisahkan tujuan, dan meminta approval ulang jika keputusan Besar terdampak.

## AT-10 — Pembuatan template

**Given:** master blueprint dan pilot sudah lulus.  
**When:** template bersih dibuat.  
**Then:** template tidak membawa data pribadi, output produksi, audit internal, atau keputusan domain contoh; entry point dan kontrak minimum tetap tersedia.

## AT-11 — Regression setelah upgrade

**Given:** aturan universal atau template diubah.  
**When:** perubahan masuk tahap verifikasi.  
**Then:** contoh sistem lama, cross-reference, manifest, template, ringkasan, dan skenario failure yang relevan diuji ulang.

## AT-12 — Batas audit

**Given:** tidak ada bukti masalah dan tidak ada perubahan besar.  
**When:** sistem beroperasi normal.  
**Then:** tidak ada audit mendalam tanpa trigger; pemeriksaan ringan tetap berjalan sesuai kontrak output.

## AT-13 — Recovery konteks dari log sesi pasca crash

**Given:** sebuah sesi memelihara `LOG_SESI_YYYY-MM-DD.md` (header "Keadaan Sesi" + kronologi) yang berkeadaan `OPEN`, lalu sesi itu crash tanpa penutupan yang benar; tidak ada commit baru setelah update log terakhir.  
**When:** pengguna membuka sesi baru dan menjalankan prompt pembuka universal.  
**Then:** agent menemukan log terbaru, membacanya, dan **melaporkan keadaan sesi sebelumnya** (apa yang disepakati, apa yang terbuka, langkah berikutnya) sebelum bertanya tujuan sesi — tanpa meminta pengguna menjelaskan ulang konteks yang sudah tercatat; jika ada keputusan yang belum tercatat di log, agent menyebutkannya sebagai celah, bukan menebaknya.
