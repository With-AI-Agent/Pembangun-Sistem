#!/usr/bin/env python3
"""Membuat flyer statis (SVG) dari rekaman data yang SAMA dengan undangan web.

Kenapa alat, bukan berkas gambar jadi: aturan satu-sumber (dokumen 03 bagian 1) melarang nilai
acara disalin manual ke format kedua. Flyer ini **dirender ulang** dari `data-acara.json`, jadi
kalau tanggal/jam/tempat berubah, flyer dibuat ulang — bukan diedit tangan.

Kenapa SVG: teks tetap **teks dari font** dan ornamentnya **vektor** (Langkah 0, dokumen 06
bagian 1). Tidak ada aset raster yang masuk ke unit ini, jadi tidak ada yang perlu lewat G3 di sini.

Pemakaian:
    python3 web/buat-flyer.py            # menulis flyer-portrait.svg + flyer-landscape.svg
    python3 web/buat-flyer.py --periksa  # hanya memeriksa apakah berkas yang ada masih sinkron
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

WEB = Path(__file__).resolve().parent
HARI = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
WARNA = {"latar": "#FAF7F2", "teks": "#2B2B2B", "aksen": "#B08D57"}
JUDUL = "'Playfair Display', ui-serif, Georgia, serif"
ISI = "'Montserrat', system-ui, 'Segoe UI', sans-serif"


def tanggal_panjang(iso: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    import datetime

    hari = HARI[datetime.date(y, m, d).weekday() + 1 if datetime.date(y, m, d).weekday() < 6 else 0]
    return f"{hari}, {d} {BULAN[m - 1]} {y}"


def kepala(lebar: int, tinggi: int, judul: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<!-- Flyer dibuat otomatis oleh web/buat-flyer.py dari web/data-acara.json — JANGAN diedit tangan.\n'
        f'     Unit uji coba b3 · model Modern minimalis · teks dari font, ornament vektor (Langkah 0). -->\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {lebar} {tinggi}" width="{lebar}" height="{tinggi}" role="img" aria-label="{escape(judul)}">\n'
        f'  <rect width="{lebar}" height="{tinggi}" fill="{WARNA["latar"]}"/>\n'
        f'  <rect x="14" y="14" width="{lebar - 28}" height="{tinggi - 28}" fill="none" stroke="{WARNA["aksen"]}" stroke-width="1"/>\n'
    )


def garis(cx: float, y: float, lebar: float = 90) -> str:
    return (
        f'  <g stroke="{WARNA["aksen"]}" stroke-width="1" fill="none">\n'
        f'    <line x1="{cx - lebar / 2 - 26}" y1="{y}" x2="{cx - 12}" y2="{y}"/>\n'
        f'    <line x1="{cx + 12}" y1="{y}" x2="{cx + lebar / 2 + 26}" y2="{y}"/>\n'
        f'    <path d="M{cx} {y - 5} L{cx + 6} {y} L{cx} {y + 5} L{cx - 6} {y} Z"/>\n'
        f'  </g>\n'
    )


def teks(x: float, y: float, isi: str, ukuran: float, font: str = ISI, warna: str | None = None,
         jangkar: str = "middle", spasi: float | None = None, tebal: int | None = None) -> str:
    atribut = [
        f'x="{x}"', f'y="{y}"', f'font-family="{font}"', f'font-size="{ukuran}"',
        f'fill="{warna or WARNA["teks"]}"', f'text-anchor="{jangkar}"',
    ]
    if spasi is not None:
        atribut.append(f'letter-spacing="{spasi}"')
    if tebal is not None:
        atribut.append(f'font-weight="{tebal}"')
    return f'  <text {" ".join(atribut)}>{escape(isi)}</text>\n'


def blok_acara(a: dict, x: float, y: float, ukuran: float = 15) -> str:
    baris = [
        teks(x, y, a["nama_acara"], ukuran + 3, JUDUL, WARNA["aksen"]),
        teks(x, y + ukuran + 12, tanggal_panjang(a["tanggal"]), ukuran + 3, JUDUL),
        teks(x, y + 2 * ukuran + 22, f'{a["jam_mulai"]}–{a["jam_selesai"]} {a["zona_waktu"]}', ukuran),
        teks(x, y + 3 * ukuran + 34, a["venue"], ukuran),
        teks(x, y + 4 * ukuran + 44, a["alamat"], ukuran - 2),
    ]
    return "".join(baris)


def flyer(d: dict, orientasi: str) -> str:
    L, T = (600, 900) if orientasi == "portrait" else (1000, 600)
    cx = L / 2
    nama = " & ".join(o["nama_panggilan"] for o in d["nama_mempelai"])
    nama_lengkap = [o["nama_lengkap"] for o in d["nama_mempelai"]]

    keluar = [kepala(L, T, f"Undangan pernikahan {nama} (uji coba)")]
    keluar.append(teks(cx, 66, "UNDANGAN PERNIKAHAN — UJI COBA", 11, ISI, WARNA["aksen"], spasi=2))
    keluar.append(garis(cx, 92))
    if orientasi == "portrait":
        keluar.append(teks(cx, 168, nama_lengkap[0], 26, JUDUL))
        keluar.append(teks(cx, 202, "&", 20, JUDUL, WARNA["aksen"]))
        keluar.append(teks(cx, 238, nama_lengkap[1], 26, JUDUL))
        keluar.append(garis(cx, 274))
        y = 340
        for a in d["acara"]:
            keluar.append(blok_acara(a, cx, y))
            y += 150
        keluar.append(teks(cx, T - 74, d["penutup"]["teks"][:96], 12))
        keluar.append(teks(cx, T - 40, d["penutup"]["credit"], 12, JUDUL, WARNA["aksen"], spasi=3))
    else:
        keluar.append(teks(150, 150, nama_lengkap[0], 24, JUDUL))
        keluar.append(teks(150, 182, "&", 18, JUDUL, WARNA["aksen"]))
        keluar.append(teks(150, 214, nama_lengkap[1], 24, JUDUL))
        keluar.append(garis(150, 246, 70))
        x = 420
        for a in d["acara"]:
            keluar.append(blok_acara(a, x, 140, 13))
            x = 720
        keluar.append(teks(L / 2, T - 52, d["penutup"]["credit"], 12, JUDUL, WARNA["aksen"], spasi=3))
    return "".join(keluar) + "</svg>\n"


def main() -> int:
    data = json.loads((WEB / "data-acara.json").read_text(encoding="utf-8"))
    periksa = "--periksa" in sys.argv
    keluar_beda: list[str] = []
    for orientasi in ("portrait", "landscape"):
        target = WEB / f"flyer-{orientasi}.svg"
        isi = flyer(data, orientasi)
        if periksa:
            kini = target.read_text(encoding="utf-8") if target.is_file() else ""
            if kini != isi:
                keluar_beda.append(target.name)
        else:
            target.write_text(isi, encoding="utf-8")
            print(f"ditulis: {target.name} ({len(isi)} byte)")
    if periksa:
        if keluar_beda:
            print("FLYER TIDAK SINKRON dengan data-acara.json: " + ", ".join(keluar_beda))
            return 1
        print("FLYER SINKRON: flyer-portrait.svg + flyer-landscape.svg cocok dengan data-acara.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
