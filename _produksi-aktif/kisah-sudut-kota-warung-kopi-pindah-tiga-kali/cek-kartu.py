#!/usr/bin/env python3
"""Cek kepatuhan naskah-draft.md terhadap batas Model Konten Brief 'Kartu Teks 8-10'.

Dipakai di Tahap 3 (sebelum minta G2) dan Tahap 4. Angka dilaporkan dari
perhitungan berkas, bukan dihitung tangan.

Batas (model-konten/kartu-teks-8-10/brief.md bagian 2):
  - jumlah kartu        : 8-10
  - kata per kartu      : 18-28
  - kartu 1 (hook)      : <= 15 kata
  - total kata          : 160-250
"""
import os
import re
import sys

BATAS = dict(kartu_min=8, kartu_max=10, kata_min=18, kata_max=28, hook_max=15,
             total_min=160, total_max=250)


def baca(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def hitung_kata(teks):
    """Hitung kata: pecah pada whitespace, buang tanda baca di tepi token."""
    token = [t for t in re.split(r"\s+", teks.strip()) if t]
    bersih = [re.sub(r"^[^\w]+|[^\w]+$", "", t, flags=re.UNICODE) for t in token]
    return [t for t in bersih if t]


def ekstrak_kartu(teks):
    """Ambil isi tiap '## Kartu N — ...' dari baris kutipan (>) yang mengikutinya."""
    kartu = []
    pola = re.compile(r"^## Kartu (\d+)\s*[—-]\s*(.+?)\s*$")
    baris = teks.splitlines()
    i = 0
    while i < len(baris):
        m = pola.match(baris[i])
        if not m:
            i += 1
            continue
        nomor, judul = int(m.group(1)), m.group(2)
        isi = []
        i += 1
        while i < len(baris) and not baris[i].startswith("## "):
            if baris[i].startswith("> "):
                isi.append(baris[i][2:].strip())
            elif baris[i].strip() == ">":
                isi.append("")
            i += 1
        kartu.append((nomor, judul, " ".join(x for x in isi if x)))
    return kartu


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "naskah-draft.md")
    if not os.path.isfile(path):
        print("GAGAL: naskah-draft.md tidak ditemukan di", folder)
        return 1

    kartu = ekstrak_kartu(baca(path))
    if not kartu:
        print("GAGAL: tidak ada '## Kartu N' dengan isi kutipan yang terbaca")
        return 1

    gagal = []
    print("CEK NASKAH — model Kartu Teks 8-10")
    print("  berkas           :", os.path.relpath(path))
    print("  jumlah kartu     : %d (batas %d-%d)"
          % (len(kartu), BATAS["kartu_min"], BATAS["kartu_max"]))
    if not (BATAS["kartu_min"] <= len(kartu) <= BATAS["kartu_max"]):
        gagal.append("jumlah kartu %d di luar %d-%d"
                     % (len(kartu), BATAS["kartu_min"], BATAS["kartu_max"]))

    total = 0
    for nomor, judul, isi in kartu:
        n = len(hitung_kata(isi))
        total += n
        if nomor == 1:
            ok = n <= BATAS["hook_max"]
            batas_txt = "<= %d (hook)" % BATAS["hook_max"]
            if not ok:
                gagal.append("kartu 1 = %d kata, melebihi %d" % (n, BATAS["hook_max"]))
        else:
            ok = BATAS["kata_min"] <= n <= BATAS["kata_max"]
            batas_txt = "%d-%d" % (BATAS["kata_min"], BATAS["kata_max"])
            if not ok:
                gagal.append("kartu %d = %d kata, di luar %d-%d"
                             % (nomor, n, BATAS["kata_min"], BATAS["kata_max"]))
        print("  kartu %d (%s) : %2d kata  [%s]  %s"
              % (nomor, judul, n, batas_txt, "OK" if ok else "MELESET"))

    ok_total = BATAS["total_min"] <= total <= BATAS["total_max"]
    print("  total kata       : %d (batas %d-%d)  %s"
          % (total, BATAS["total_min"], BATAS["total_max"], "OK" if ok_total else "MELESET"))
    if not ok_total:
        gagal.append("total %d kata di luar %d-%d"
                     % (total, BATAS["total_min"], BATAS["total_max"]))

    # perkiraan waktu baca: 150 kata/menit (kecepatan baca santai)
    detik = total / 150.0 * 60
    print("  waktu baca       : ~%.0f detik pada 150 kata/menit" % detik)

    if gagal:
        print("HASIL: FAIL")
        for g in gagal:
            print("  -", g)
        return 1
    print("HASIL: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
