#!/usr/bin/env node
/* Menghasilkan `qr-sebar.svg` — QR **vektor** untuk disebar (serah terima L1 bagian 8 item 4).
 *
 * Aturan yang dipatuhi:
 *  - QR dibuat oleh pustaka (web/vendor/qrcode-generator, MIT) — TIDAK digambar ulang manual,
 *    karena kode QR yang salah gambar = tamu tidak bisa membuka undangan (dokumen 11 bagian 5a).
 *  - QR **tidak** diperbesar dari berkas raster: SVG = vektor, jadi tidak ada aset raster di unit ini
 *    (Langkah 0 dokumen 06 bagian 1, dan G3 tidak dilewati).
 *  - Alamat yang di-QR-kan dibaca dari `data-acara.json` (publikasi) — bukan diketik di skrip ini
 *    (aturan satu-sumber dokumen 03 bagian 1).
 *
 * Pemakaian:  node web/buat-qr.js [alamat]
 *             node web/buat-qr.js --periksa
 */
const fs = require("fs");
const path = require("path");
const qrcode = require(path.join(__dirname, "vendor", "qrcode-generator", "qrcode.js"));

const WEB = __dirname;
const data = JSON.parse(fs.readFileSync(path.join(WEB, "data-acara.json"), "utf8"));
const alamatDefault = (data.publikasi && data.publikasi.url_pratinjau_b3) || "";
const alamatFase1 = (data.publikasi && data.publikasi.url_rencana_fase_1) || "";

const arg = process.argv[2];
const periksa = arg === "--periksa";
const alamat = !arg || arg === "--periksa"
  ? `https://${alamatFase1.replace(/^https?:\/\//, "")}`
  : arg;

const qr = qrcode(0, "M");
qr.addData(alamat);
qr.make();
const svg = qr.createSvgTag({ cellSize: 4, margin: 4, scalable: true });

const target = path.join(WEB, "qr-sebar.svg");
const kepala = `<?xml version="1.0" encoding="UTF-8"?>\n<!-- Dibuat otomatis oleh web/buat-qr.js — JANGAN diedit tangan.\n     Alamat: ${alamat}\n     Pustaka: qrcode-generator (MIT) — provenance di vendor/qrcode-generator/PROVENANCE.md -->\n`;

if (periksa) {
  const kini = fs.existsSync(target) ? fs.readFileSync(target, "utf8") : "";
  if (kini !== kepala + svg) {
    console.log("QR TIDAK SINKRON dengan data-acara.json / pustaka");
    process.exit(1);
  }
  console.log("QR SINKRON: qr-sebar.svg cocok dengan alamat di data-acara.json");
  process.exit(0);
}

fs.writeFileSync(target, kepala + svg, "utf8");
console.log(`ditulis: qr-sebar.svg (${(kepala + svg).length} byte) · alamat: ${alamat}`);
