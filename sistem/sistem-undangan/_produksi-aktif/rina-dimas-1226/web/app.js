/* Undangan web — unit uji coba rina-dimas-1226
 * ATURAN SATU-SUMBER: seluruh nilai diambil dari data-acara.json. Tidak ada nilai acara yang
 * ditulis ulang di berkas ini (nama, tanggal, jam, tempat, rekening) — kalau ada, itu bug skema
 * (dokumen 03 bagian 1). Yang boleh ada di sini hanya perilaku: personalisasi tamu, hitung mundur,
 * buku tamu/RSVP (mode uji), tombol salin.
 *
 * Jalur uji (dinyatakan sadar, dipakai untuk menguji tampilan tanpa satu pun nomor nyata):
 *   ?uji=amplop   -> menyuntikkan blok amplop berlabel UJI COBA dengan nomor jelas fiktif
 *   ?tamu=Nama    -> menguji personalisasi sapaan dari parameter tautan
 */

const HARI = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];
const BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"];
const KUNCI_SIMPAN = "uji-b3:ucapan-rsvp";

let DATA = null;
const PARAM = new URLSearchParams(location.search);

/* ---------- utilitas ---------- */
const el = (tag, isi, kelas) => {
  const n = document.createElement(tag);
  if (isi !== undefined && isi !== null && isi !== "") n.textContent = isi;
  if (kelas) n.className = kelas;
  return n;
};

function tanggalPanjang(iso) {
  const [y, m, d] = iso.split("-").map(Number);
  const tanggal = new Date(Date.UTC(y, m - 1, d));
  return `${HARI[tanggal.getUTCDay()]}, ${d} ${BULAN[m - 1]} ${y}`;
}

function bagian(id) {
  const s = document.createElement("section");
  s.id = id;
  return s;
}

function garisAksen() {
  const img = document.createElement("img");
  img.src = "aset/garis-aksen.svg";
  img.alt = "";
  img.className = "garis";
  return img;
}

/* ---------- amplop: hanya bila datanya ada (11 bagian 2 butir 2) ---------- */
function amplopEfektif() {
  if (PARAM.get("uji") === "amplop") {
    return {
      uji: true,
      rekening: { nomor: "0000 0000 0000", nama: "UJI COBA — bukan rekening siapa pun", bank: "BANK UJI COBA" },
      status_verifikasi: "JALUR UJI — bukan hasil verifikasi nyata (dokumen 11 bagian 6 tidak dijalankan di sini)"
    };
  }
  return DATA.amplop_digital || null;
}

/* ---------- penyimpanan sementara (mode uji; dokumen 10 belum memutuskan penyimpanan nyata) ---------- */
function baca() {
  try { return JSON.parse(localStorage.getItem(KUNCI_SIMPAN) || "[]"); } catch { return []; }
}
function simpan(daftar) {
  try { localStorage.setItem(KUNCI_SIMPAN, JSON.stringify(daftar)); return true; } catch { return false; }
}

/* ---------- bagian-bagian halaman ---------- */
function rakitPembuka(root) {
  const s = bagian("pembuka");
  s.append(garisAksen());
  s.append(el("p", DATA.pembuka ? DATA.pembuka.teks : "", "pembuka-teks"));
  root.append(s);
}

function rakitSapaan(root) {
  const s = bagian("sapaan");
  const sapaan = DATA.sapaan_tamu || {};
  s.append(el("p", sapaan.teks || "", "sapaan"));
  const namaTamu = PARAM.get("tamu");
  if (namaTamu) {
    s.append(el("p", namaTamu, "sapaan-nama"));
    if (sapaan.personalisasi && sapaan.personalisasi.mekanisme) {
      s.append(el("p", "Nama ini dibaca dari tautan yang kamu terima.", "lebih-kecil"));
    }
  }
  root.append(s);
}

function rakitMempelai(root) {
  const s = bagian("mempelai");
  s.append(garisAksen());
  const kotak = el("div", null, "pasangan");
  const nama = DATA.nama_mempelai || [];
  nama.forEach((orang, i) => {
    const blok = el("div", null, "orang");
    blok.append(el("div", orang.nama_lengkap));
    blok.append(el("div", orang.nama_panggilan, "lebih-kecil"));
    if (i === 1) {
      const dan = el("div", "&", "dan");
      kotak.append(dan);
    }
    kotak.append(blok);
  });
  s.append(kotak);

  if (DATA.pola_tuan_rumah === "orang_tua" && Array.isArray(DATA.orang_tua)) {
    s.append(el("h3", "Tuan rumah"));
    ["mempelai_1", "mempelai_2"].forEach((pihak) => {
      const baris = DATA.orang_tua.filter((o) => o.pihak === pihak);
      if (!baris.length) return;
      const ul = el("ul", null, "daftar-ortu");
      baris.forEach((o) => ul.append(el("li", `${o.nama_lengkap}${o.gelar_utuh && o.gelar_utuh !== "— (tanpa gelar)" ? ` (${o.gelar_utuh})` : ""}`)));
      s.append(ul);
    });
  }
  if (Array.isArray(DATA.turut_mengundang) && DATA.turut_mengundang.length) {
    s.append(el("h3", "Turut mengundang"));
    const ul = el("ul", null, "daftar-mengundang");
    DATA.turut_mengundang.forEach((x) => ul.append(el("li", x)));
    s.append(ul);
  }
  root.append(s);
}

function rakitAcara(root) {
  const s = bagian("acara");
  s.append(el("h3", "Waktu & tempat"));
  (DATA.acara || []).forEach((a) => {
    const kartu = el("div", null, "kartu-acara");
    kartu.append(el("h3", a.nama_acara));
    kartu.append(el("div", tanggalPanjang(a.tanggal), "tanggal"));
    kartu.append(el("div", `${a.jam_mulai}–${a.jam_selesai} ${a.zona_waktu}`, "jam"));
    kartu.append(el("div", `${a.venue}`, "tempat"));
    kartu.append(el("div", a.alamat, "tempat"));
    if (a.tautan_peta) {
      const tautan = el("a", "Buka peta", "peta");
      tautan.href = a.tautan_peta;
      tautan.target = "_blank";
      tautan.rel = "noopener";
      kartu.append(tautan);
    }
    s.append(kartu);
  });
  root.append(s);
}

function rakitHitungMundur(root) {
  if (!DATA.countdown || !DATA.countdown.aktif) return;
  const s = bagian("hitung-mundur");
  s.append(el("h3", "Menuju hari bahagia"));
  const kotak = el("div", null, "hitung-mundur");
  const bagianWaktu = ["hari", "jam", "menit", "detik"].map((label) => {
    const wadah = el("div");
    const angka = el("span", "0", "angka");
    wadah.append(angka, el("span", label, "label"));
    kotak.append(wadah);
    return { angka, label };
  });
  s.append(kotak);
  root.append(s);

  const target = new Date(DATA.countdown.target).getTime();
  const gambar = () => {
    const sisa = Math.max(0, target - Date.now());
    const nilai = [
      Math.floor(sisa / 86400000),
      Math.floor((sisa % 86400000) / 3600000),
      Math.floor((sisa % 3600000) / 60000),
      Math.floor((sisa % 60000) / 1000)
    ];
    bagianWaktu.forEach((b, i) => { b.angka.textContent = String(nilai[i]).padStart(2, "0"); });
  };
  gambar();
  setInterval(gambar, 1000);
}

function rakitSusunan(root) {
  if (!Array.isArray(DATA.susunan_acara) || !DATA.susunan_acara.length) return;
  const s = bagian("susunan");
  s.append(el("h3", "Susunan acara"));
  const ul = el("ul", null, "daftar-susunan");
  DATA.susunan_acara.forEach((b) => {
    const li = el("li");
    li.append(el("span", b.waktu, "waktu"));
    li.append(el("span", b.kegiatan));
    ul.append(li);
  });
  s.append(ul);
  root.append(s);
}

function rakitAmplop(root) {
  const amplop = amplopEfektif();
  if (!amplop) return; // data kosong -> bagian TIDAK dirender (bukan placeholder)
  const s = bagian("amplop");
  s.append(el("h3", amplop.uji ? "Amplop Digital (JALUR UJI)" : "Amplop Digital"));
  s.append(el("p", "Bagi Bapak/Ibu/Saudara/i yang ingin memberikan tanda kasih, dapat melalui:", "kecil"));
  const rek = amplop.rekening || {};
  s.append(el("p", rek.nomor || "", "amplop-nomor"));
  s.append(el("p", rek.nama || "", "kecil"));
  s.append(el("p", rek.bank || "", "kecil"));
  if (amplop.uji) {
    s.append(el("p", amplop.status_verifikasi, "catatan-mode"));
  }
  root.append(s);
}

function rakitUcapan(root) {
  const s = bagian("ucapan");
  s.append(garisAksen());
  s.append(el("h3", "Ucapan & doa restu"));
  s.append(el("p", DATA.ucapan_doa ? DATA.ucapan_doa.teks : "", "kecil"));

  const daftar = el("ul", null, "daftar-ucapan");
  const gambarDaftar = () => {
    daftar.innerHTML = "";
    const isi = baca();
    if (!isi.length) {
      daftar.append(el("li", "Belum ada ucapan.", "lebih-kecil"));
      return;
    }
    isi.slice().reverse().forEach((u) => {
      const li = el("li");
      li.append(el("div", u.nama, "dari"));
      li.append(el("div", u.pesan));
      li.append(el("div", `${u.hadir} · ${u.kapan}`, "kapan"));
      daftar.append(li);
    });
  };

  const form = el("form");
  form.innerHTML = `
    <label for="nama">Nama</label>
    <input id="nama" name="nama" required maxlength="60" placeholder="Nama Bapak/Ibu/Saudara/i">
    <label for="hadir">Rencana kehadiran</label>
    <select id="hadir" name="hadir">
      <option>Insya Allah hadir</option>
      <option>Masih belum pasti</option>
      <option>Mohon maaf belum bisa hadir</option>
    </select>
    <label for="pesan">Ucapan &amp; doa</label>
    <textarea id="pesan" name="pesan" maxlength="300" placeholder="Tulis ucapan dan doa restu"></textarea>
    <button class="tombol" type="submit">Kirim ucapan</button>
  `;
  form.addEventListener("submit", (ev) => {
    ev.preventDefault();
    const nama = form.nama.value.trim();
    if (!nama) return;
    const isi = baca();
    isi.push({
      nama,
      hadir: form.hadir.value,
      pesan: form.pesan.value.trim(),
      kapan: new Date().toLocaleString("id-ID", { dateStyle: "medium", timeStyle: "short" })
    });
    const berhasil = simpan(isi);
    form.reset();
    gambarDaftar();
    if (!berhasil) alert("Penyimpanan sementara di perangkat ini tidak tersedia — ucapan tidak tersimpan.");
  });

  s.append(form);
  s.append(daftar);
  s.append(el("p", "MODE UJI COBA: ucapan & RSVP disimpan sementara di perangkat ini saja (localStorage) — belum ada penyimpanan nyata; keputusan tempat penyimpanan menunggu dokumen 10.", "catatan-mode"));
  root.append(s);
  gambarDaftar();
}

function rakitDresscode(root) {
  if (!DATA.dress_code) return;
  const s = bagian("dress-code");
  s.append(el("h3", "Dress code"));
  s.append(el("p", DATA.dress_code));
  root.append(s);
}

function rakitTeksWa(root) {
  const s = bagian("teks-wa");
  s.append(el("h3", "Teks undangan siap salin"));
  const tulis = () => {
    const a = (DATA.acara || [])[0] || {};
    const nama = (DATA.nama_mempelai || []).map((o) => o.nama_panggilan).join(" & ");
    const url = location.origin + location.pathname;
    return `Assalamu'alaikum Wr. Wb.\n\nDengan penuh kebahagiaan, kami mengundang Bapak/Ibu/Saudara/i untuk hadir di pernikahan ${nama}.\n\n${(a.nama_acara || "")}: ${tanggalPanjang(a.tanggal)} · ${a.jam_mulai}–${a.jam_selesai} ${a.zona_waktu}\n${a.venue}, ${a.alamat}\n\nSelengkapnya: ${url}\n\nMerupakan suatu kehormatan apabila Bapak/Ibu/Saudara/i berkenan hadir dan memberikan doa restu.`;
  };
  const kotak = el("pre", tulis(), "kotak-teks");
  kotak.style.whiteSpace = "pre-wrap";
  kotak.style.textAlign = "left";
  kotak.style.fontFamily = "var(--font-isi)";
  kotak.style.fontSize = "0.85rem";
  kotak.style.background = "rgba(176,141,87,0.08)";
  kotak.style.padding = "0.85rem";
  kotak.style.borderRadius = "0.4rem";
  const tombol = el("button", "Salin teks", "tombol");
  tombol.type = "button";
  tombol.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(kotak.textContent);
      tombol.textContent = "Tersalin";
      setTimeout(() => { tombol.textContent = "Salin teks"; }, 2000);
    } catch {
      tombol.textContent = "Salin manual saja";
    }
  });
  s.append(kotak, tombol);
  s.append(el("p", "Teks ini dihasilkan dari rekaman data (bukan diketik manual) — kalau data berubah, teks ikut berubah.", "lebih-kecil"));
  root.append(s);
}

function rakitPenutup(root) {
  const s = bagian("penutup");
  s.append(el("h2", DATA.penutup ? DATA.penutup.teks : ""));
  root.append(s);
}

/* QR untuk sebar (serah terima L1 bagian 8 item 4).
   Pustaka: vendor/qrcode-generator (MIT, provenance tercatat). QR dibuat oleh pustaka, bukan
   digambar manual (dokumen 11 bagian 5a) dan hasilnya SVG = vektor (tidak menambah aset raster). */
function rakitQr(root) {
  if (typeof qrcode !== "function") return;
  const s = bagian("qr-sebar");
  s.append(el("h3", "QR undangan"));
  try {
    const qr = qrcode(0, "M");
    qr.addData(location.href.split("#")[0]);
    qr.make();
    const wadah = el("div");
    wadah.innerHTML = qr.createSvgTag({ cellSize: 4, margin: 4, scalable: true });
    const svg = wadah.querySelector("svg");
    if (svg) {
      svg.setAttribute("width", "180");
      svg.setAttribute("height", "180");
      svg.setAttribute("role", "img");
      svg.setAttribute("aria-label", "QR tautan undangan");
      s.append(svg);
    }
    s.append(el("p", "QR ini menunjuk ke alamat halaman yang sedang dibuka. Untuk disebar, gunakan versi cetak di berkas qr-sebar.svg.", "lebih-kecil"));
  } catch (e) {
    s.append(el("p", "QR tidak bisa dibuat di peramban ini.", "lebih-kecil"));
  }
  root.append(s);
}

/* ---------- jalan ---------- */
async function mulai() {
  const root = document.getElementById("undangan");
  try {
    const resp = await fetch("data-acara.json", { cache: "no-store" });
    if (!resp.ok) throw new Error("HTTP " + resp.status);
    DATA = await resp.json();
  } catch (e) {
    root.innerHTML = "";
    const s = bagian("galat");
    s.append(el("h2", "Undangan gagal dimuat"));
    s.append(el("p", "Berkas data acara tidak terbaca oleh halaman ini.", "kecil"));
    s.append(el("p", String(e), "lebih-kecil"));
    root.append(s);
    return;
  }

  root.innerHTML = "";
  document.title = `${(DATA.nama_mempelai || []).map((o) => o.nama_panggilan).join(" & ")} — Undangan (uji coba)`;
  rakitPembuka(root);
  rakitSapaan(root);
  rakitMempelai(root);
  rakitAcara(root);
  rakitHitungMundur(root);
  rakitSusunan(root);
  rakitAmplop(root);
  rakitUcapan(root);
  rakitDresscode(root);
  rakitTeksWa(root);
  rakitQr(root);
  rakitPenutup(root);

  const credit = document.getElementById("credit");
  if (DATA.penutup && DATA.penutup.credit) credit.textContent = DATA.penutup.credit;
}

document.addEventListener("DOMContentLoaded", mulai);
