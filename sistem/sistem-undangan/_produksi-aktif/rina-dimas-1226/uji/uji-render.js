#!/usr/bin/env node
/* Uji render undangan (b3) — memuat halaman di DOM nyata (jsdom), menjalankan app.js,
 * lalu memeriksa bahwa nilai dari data-acara.json BENAR-BENAR muncul di halaman.
 *
 * Alat ini dijalankan dari /tmp (jsdom tidak di-vendor ke repo sistem).
 * Pemakaian (dari akar repo):
 *     npm i --prefix /tmp jsdom
 *     node sistem/sistem-undangan/_produksi-aktif/rina-dimas-1226/uji/uji-render.js \
 *          sistem/sistem-undangan/_produksi-aktif/rina-dimas-1226/web
 * Keluar 0 = semua pemeriksaan lulus; 1 = ada yang gagal (dicetak apa adanya).
 */
const fs = require("fs");
const path = require("path");
/* jsdom TIDAK di-vendor ke repo (alat uji lokal, bukan bagian sistem). Pasang sekali:
 *     npm i --prefix /tmp jsdom
 * Alat mencari jsdom di dua tempat: pustaka lokal, lalu /tmp/node_modules. */
function muatJsdom() {
  for (const jalur of ["jsdom", "/tmp/node_modules/jsdom"]) {
    try { return require(jalur); } catch (e) { /* coba jalur berikutnya */ }
  }
  console.error("jsdom tidak ditemukan. Jalankan lebih dulu:  npm i --prefix /tmp jsdom");
  process.exit(2);
}
const { JSDOM, VirtualConsole } = muatJsdom();

const WEB = path.resolve(process.argv[2] || ".");
const data = JSON.parse(fs.readFileSync(path.join(WEB, "data-acara.json"), "utf8"));
const html = fs.readFileSync(path.join(WEB, "index.html"), "utf8");
const appjs = fs.readFileSync(path.join(WEB, "app.js"), "utf8");
const qrjs = fs.readFileSync(path.join(WEB, "vendor", "qrcode-generator", "qrcode.js"), "utf8");

const lulus = [];
const gagal = [];

function periksa(nama, syarat, bukti) {
  if (syarat) lulus.push(nama);
  else gagal.push(`${nama} — bukti: ${bukti}`);
}

async function render(query) {
  const vc = new VirtualConsole();
  vc.on("jsdomError", () => {});
  const dom = new JSDOM(html, { url: `https://lee-studio.pages.dev/rina-dimas-1226/${query}`, runScripts: "outside-only", virtualConsole: vc });
  const w = dom.window;
  w.fetch = async () => ({ ok: true, status: 200, json: async () => data });
  w.eval(qrjs);
  w.eval(appjs);
  w.document.dispatchEvent(new w.Event("DOMContentLoaded"));
  await new Promise((r) => setTimeout(r, 150));
  return dom;
}

(async () => {
  // ---------- 1. halaman normal ----------
  const dom = await render("");
  const d = dom.window.document;
  const teks = d.body.textContent;

  periksa("judul halaman berisi kedua nama panggilan", /Rina & Dimas/.test(d.title), d.title);
  periksa("nama lengkap mempelai 1 tampil", teks.includes(data.nama_mempelai[0].nama_lengkap), "tidak ditemukan");
  periksa("nama lengkap mempelai 2 tampil", teks.includes(data.nama_mempelai[1].nama_lengkap), "tidak ditemukan");
  periksa("nama orang tua (4) tampil", data.orang_tua.every((o) => teks.includes(o.nama_lengkap)), "ada yang hilang");
  periksa("turut mengundang tampil", data.turut_mengundang.every((x) => teks.includes(x)), "ada yang hilang");

  const hariID = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];
  const bulanID = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"];
  for (const a of data.acara) {
    const [y, m, day] = a.tanggal.split("-").map(Number);
    const namaHari = hariID[new Date(Date.UTC(y, m - 1, day)).getUTCDay()];
    const panjang = `${namaHari}, ${day} ${bulanID[m - 1]} ${y}`;
    periksa(`acara "${a.nama_acara}": tanggal panjang tampil (${panjang})`, teks.includes(panjang), "tidak ditemukan");
    periksa(`acara "${a.nama_acara}": jam + zona waktu tampil`, teks.includes(`${a.jam_mulai}–${a.jam_selesai} ${a.zona_waktu}`), "tidak ditemukan");
    periksa(`acara "${a.nama_acara}": venue + alamat tampil`, teks.includes(a.venue) && teks.includes(a.alamat), "tidak ditemukan");
    const tautan = d.querySelector(`a.peta[href="${a.tautan_peta}"]`);
    periksa(`acara "${a.nama_acara}": tautan peta ada`, !!tautan, "tidak ada <a class=peta>");
  }

  periksa("susunan acara tampil lengkap", data.susunan_acara.every((b) => teks.includes(b.kegiatan) && teks.includes(b.waktu)), "ada yang hilang");
  periksa("dress code tampil", teks.includes(data.dress_code), "tidak ditemukan");
  periksa("pembuka tampil", teks.includes(data.pembuka.teks), "tidak ditemukan");
  periksa("credit Lee-Studio tampil di kaki halaman", d.querySelector("#credit").textContent.trim() === "Lee-Studio", d.querySelector("#credit").textContent);
  periksa("sapaan baku L1 tampil", teks.includes(data.sapaan_tamu.teks), "tidak ditemukan");
  periksa("hitung mundur tampil (4 satuan)", d.querySelectorAll(".hitung-mundur .angka").length === 4, String(d.querySelectorAll(".hitung-mundur .angka").length));
  periksa("bagian ucapan & RSVP ada", !!d.querySelector("#ucapan form"), "form tidak ada");
  periksa("mode uji ucapan dinyatakan di layar", /MODE UJI COBA/.test(teks), "catatan mode tidak tampil");
  periksa("teks WA memuat tautan halaman", d.querySelector("#teks-wa pre").textContent.includes("https://lee-studio.pages.dev/rina-dimas-1226/"), "tautan tidak ada di teks");
  periksa("QR sebar dirender sebagai SVG (vektor)", !!d.querySelector("#qr-sebar svg"), "tidak ada svg QR");
  periksa("pita 'MODE UJI COBA' tampil di atas", /MODE UJI COBA b3/.test(teks), "tidak ada");
  periksa("amplop TIDAK dirender saat data kosong (aturan 11 bagian 2 butir 2)", d.querySelector("#amplop") === null, "bagian amplop muncul padahal data kosong");
  periksa("tidak ada elemen audio (tanpa musik, tanpa autoplay)", d.querySelectorAll("audio").length === 0, "ada elemen audio");

  // ---------- 2. jalur uji amplop ----------
  const dom2 = await render("?uji=amplop");
  const d2 = dom2.window.document;
  const amplop = d2.querySelector("#amplop");
  periksa("jalur uji ?uji=amplop: bagian amplop muncul", !!amplop, "tidak muncul");
  periksa("jalur uji: nomor jelas fiktif tampil", amplop && amplop.textContent.includes("0000 0000 0000"), amplop ? amplop.textContent.slice(0, 80) : "-");
  periksa("jalur uji: berlabel UJI COBA (tidak menyamar sebagai verifikasi nyata)", amplop && /JALUR UJI/.test(amplop.textContent), "label tidak ada");

  // ---------- 3. personalisasi tamu dari tautan ----------
  const dom3 = await render("?tamu=Bapak%20Uji%20Coba");
  const d3 = dom3.window.document;
  periksa("?tamu=Nama: nama tamu tampil dari parameter tautan", d3.querySelector(".sapaan-nama") && d3.querySelector(".sapaan-nama").textContent === "Bapak Uji Coba", d3.querySelector(".sapaan-nama") ? d3.querySelector(".sapaan-nama").textContent : "tidak ada");

  // ---------- hasil ----------
  console.log(`UJI RENDER UNDANGAN (b3) — ${lulus.length} lulus, ${gagal.length} gagal`);
  lulus.forEach((n) => console.log(`  LULUS  ${n}`));
  gagal.forEach((n) => console.log(`  GAGAL  ${n}`));
  process.exit(gagal.length ? 1 : 0);
})();
