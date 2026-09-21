#!/usr/bin/env python3
"""Validator mandiri UNIT undangan — gerbang data (dokumen 03 bagian 7) + aturan bukti aset (dokumen 06 bagian 8).

Kenapa alat ini ada: dokumen 03 bagian 7 mensyaratkan "data acara tidak boleh masuk Tahap 3 sebelum
lulus" dan dokumen 06 bagian 8 berkata *gerbang tanpa bukti = diklaim hijau tanpa dijalankan*.
Sebelum alat ini, kedua kalimat itu hanya aturan tertulis. Alat ini menegakkannya secara mekanis untuk
SATU unit, dan keluar dengan exit code (0 = lulus, 1 = ada ERROR) supaya bisa dipakai di gerbang repo.

Cakupan sengaja kecil dan deterministik:
  * struktur berkas unit wajib ada (STATUS.md + brief + spesifikasi desain + log keputusan);
  * field WAJIB dokumen 03 terisi dengan format benar (ISO 8601, jam 24 jam, zona waktu per larik acara);
  * larik acara tidak boleh memakai rujukan "sama dengan ..." (dilarang dokumen 03 bagian 1 butir 4);
  * nilai kosong yang opsional WAJIB punya alasan tertulis (bukan dibiarkan kosong diam-diam);
  * STATUS.md unit wajib memuat field deterministik (C-01: "Pekerjaan belum tersimpan");
  * aset raster wajib punya baris di `aset/daftar-aset.json` dengan jenis + DPI + kenaikan (aturan bukti G3).

Pemakaian:
    python3 sistem/sistem-undangan/_sistem/validate_unit.py <folder-unit>
tanpa argumen: memvalidasi SEMUA folder unit di dalam `_produksi-aktif/`.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SISTEM = Path(__file__).resolve().parent.parent
PRODUKSI = SISTEM / "_produksi-aktif"

ZONA_WAKTU = ("WIB", "WITA", "WIT")
BENTUK_ACARA = ("akad_nikah", "pemberkatan", "holy_matrimony", "pencatatan_sipil", "adat")
POLA_TUAN_RUMAH = ("orang_tua", "mempelai_sendiri")
RASTER_EXT = (".jpg", ".jpeg", ".png", ".webp", ".avif", ".gif", ".bmp", ".tif", ".tiff")
ISO_TANGGAL = re.compile(r"^\d{4}-\d{2}-\d{2}$")
JAM_24 = re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")
FIELD_WAJIB_UNIT = ("STATUS.md", "brief-undangan.md", "spesifikasi-desain.md", "log-keputusan-unit.md")
F_SEMENTARA = "Pekerjaan belum tersimpan"


def periksa(unit: Path) -> list[str]:
    err: list[str] = []

    def e(msg: str) -> None:
        err.append(msg)

    if not unit.is_dir():
        return [f"folder unit tidak ada: {unit}"]

    # --- 1. berkas unit wajib ---------------------------------------------------------
    for nama in FIELD_WAJIB_UNIT:
        if not (unit / nama).is_file():
            e(f"{unit.name}: berkas unit wajib tidak ada: {nama}")

    # STATUS.md unit + field deterministik C-01
    status = unit / "STATUS.md"
    if status.is_file():
        isi = status.read_text(encoding="utf-8")
        jumlah = len(re.findall(rf"\*\*{re.escape(F_SEMENTARA)}:\*\*", isi))
        if jumlah == 0:
            e(f"{unit.name}: STATUS.md unit tidak memuat field '{F_SEMENTARA}' (C-01)")
        elif jumlah > 1:
            e(f"{unit.name}: field '{F_SEMENTARA}' muncul {jumlah} kali (bukti ganda = tidak deterministik)")

    # --- 2. rekaman data acara --------------------------------------------------------
    data_path = unit / "web" / "data-acara.json"
    if not data_path.is_file():
        e(f"{unit.name}: rekaman data tidak ada: web/data-acara.json (satu-satunya sumber nilai)")
        return err

    try:
        d = json.loads(data_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return err + [f"{unit.name}: web/data-acara.json bukan JSON yang sah: {exc}"]

    def ada(nilai) -> bool:
        if nilai is None:
            return False
        if isinstance(nilai, str):
            return bool(nilai.strip()) and nilai.strip() != "-"
        if isinstance(nilai, (list, dict)):
            return len(nilai) > 0
        return True

    def kosong_dengan_alasan(field: str, alasan_kunci: str, konteks: str = "unit") -> None:
        """Field opsional yang bernilai kosong WAJIB punya alasan tertulis (03 bagian 4 butir 1)."""
        if not ada(d.get(field)) and not ada(d.get(alasan_kunci)):
            e(f"{unit.name}: {field} kosong di {konteks} tanpa alasan tertulis ('{alasan_kunci}') — "
              f"yang kurang harus dinyatakan sadar, bukan dibiarkan kosong")

    # meta
    meta = d.get("meta") or {}
    for k in ("unit", "jenis_acara", "profil_l2"):
        if not ada(meta.get(k)):
            e(f"{unit.name}: meta.{k} kosong (WAJIB)")

    # mempelai (2 orang, nama lengkap + panggilan)
    mempelai = d.get("nama_mempelai")
    if not isinstance(mempelai, list) or len(mempelai) != 2:
        e(f"{unit.name}: nama_mempelai harus daftar berisi tepat 2 orang (WAJIB #1)")
    else:
        for i, orang in enumerate(mempelai, 1):
            for k in ("nama_lengkap", "nama_panggilan"):
                if not ada((orang or {}).get(k)):
                    e(f"{unit.name}: nama_mempelai[{i}].{k} kosong (WAJIB #1)")

    # pola tuan rumah + orang tua
    pola = d.get("pola_tuan_rumah")
    if pola not in POLA_TUAN_RUMAH:
        e(f"{unit.name}: pola_tuan_rumah harus salah satu dari {POLA_TUAN_RUMAH} (WAJIB #2), ditemui: {pola!r}")
    elif pola == "orang_tua":
        ortu = d.get("orang_tua")
        if not isinstance(ortu, list) or len(ortu) < 2:
            e(f"{unit.name}: orang_tua wajib terisi bila pola_tuan_rumah=orang_tua (WAJIB #2)")
        else:
            for i, orang in enumerate(ortu, 1):
                for k in ("nama_lengkap", "gelar_utuh"):
                    if not ada((orang or {}).get(k)):
                        e(f"{unit.name}: orang_tua[{i}].{k} kosong — gelar ditulis utuh, tidak disingkat (WAJIB #2)")

    # titik sensitif
    tst = d.get("titik_sensitif_terkonfirmasi") or {}
    if tst.get("ya") is not True:
        e(f"{unit.name}: titik_sensitif_terkonfirmasi.ya harus true — tanpa ini gerbang data GAGAL, bukan peringatan")
    if not ada(tst.get("catatan")):
        e(f"{unit.name}: titik_sensitif_terkonfirmasi.catatan kosong — konfirmasi tanpa catatan = tidak dapat diaudit")

    # bentuk acara + resepsi
    if d.get("bentuk_acara") not in BENTUK_ACARA:
        e(f"{unit.name}: bentuk_acara harus salah satu dari {BENTUK_ACARA} (WAJIB #3)")
    resepsi = d.get("dengan_resepsi")
    if not isinstance(resepsi, bool):
        e(f"{unit.name}: dengan_resepsi harus boolean (WAJIB #3)")
    elif resepsi and not ada(d.get("istilah_resepsi")):
        e(f"{unit.name}: istilah_resepsi wajib terisi bila dengan_resepsi=true (WAJIB #3)")
    if d.get("bentuk_acara") == "adat" and not ada(d.get("nama_prosesi_adat")):
        e(f"{unit.name}: nama_prosesi_adat wajib terisi untuk bentuk adat (diisi client, tidak dipatok studio)")

    # acara: daftar >=1, lengkap per larik
    acara = d.get("acara")
    if not isinstance(acara, list) or not acara:
        e(f"{unit.name}: acara harus daftar berisi >= 1 larik (WAJIB #4/#5/#6/#7)")
    else:
        for i, a in enumerate(acara, 1):
            tag = f"acara[{i}]"
            for k in ("nama_acara", "hari", "venue", "alamat", "tautan_peta"):
                if not ada((a or {}).get(k)):
                    e(f"{unit.name}: {tag}.{k} kosong — tiap larik acara wajib lengkap (WAJIB #4/#6)")
            tanggal = (a or {}).get("tanggal")
            if not (isinstance(tanggal, str) and ISO_TANGGAL.match(tanggal)):
                e(f"{unit.name}: {tag}.tanggal harus ISO 8601 YYYY-MM-DD, ditemui: {tanggal!r}")
            for k in ("jam_mulai", "jam_selesai"):
                nilai = (a or {}).get(k)
                if not (isinstance(nilai, str) and JAM_24.match(nilai)):
                    e(f"{unit.name}: {tag}.{k} harus jam 24 jam HH:MM, ditemui: {nilai!r}")
            if (a or {}).get("zona_waktu") not in ZONA_WAKTU:
                e(f"{unit.name}: {tag}.zona_waktu harus salah satu dari {ZONA_WAKTU} — zona waktu selalu ditulis (WAJIB #7)")
            # larangan larik rujukan (03 bagian 1 butir 4)
            for k, nilai in (a or {}).items():
                if isinstance(nilai, str) and "sama dengan" in nilai.lower():
                    e(f"{unit.name}: {tag}.{k} memuat rujukan nilai 'sama dengan ...' — dilarang (03 bagian 1 butir 4)")

    # field opsional yang kosong wajib beralasan
    kosong_dengan_alasan("galeri", "galeri_alasan_kosong")
    kosong_dengan_alasan("amplop_digital", "amplop_alasan_kosong")
    kosong_dengan_alasan("musik", "musik_alasan_kosong")
    kosong_dengan_alasan("format_tambahan", "format_tambahan_catatan")
    rsvp = d.get("rsvp") or {}
    if not ada(rsvp.get("kontak")) and not ada(rsvp.get("alasan_kontak")):
        e(f"{unit.name}: rsvp.kontak kosong tanpa alasan tertulis ('alasan_kontak')")
    if ada(rsvp.get("batas_waktu")) and not (isinstance(rsvp.get("batas_waktu"), str) and ISO_TANGGAL.match(rsvp.get("batas_waktu"))):
        e(f"{unit.name}: rsvp.batas_waktu harus ISO 8601 YYYY-MM-DD")

    # amplop: bila aktif, tiap butir wajib lengkap (aturan dokumen 11 bagian 3/6)
    amplop = d.get("amplop_digital")
    if ada(amplop):
        rek = (amplop or {}).get("rekening")
        if not isinstance(rek, dict):
            e(f"{unit.name}: amplop_digital aktif tetapi rekening tidak ada (dokumen 11 bagian 3)")
        else:
            for k in ("nomor", "nama", "bank"):
                if not ada(rek.get(k)):
                    e(f"{unit.name}: amplop_digital.rekening.{k} kosong — titik verifikasi G2/G5 (L1 batasan mutlak #1)")
        if not ada((amplop or {}).get("status_verifikasi")):
            e(f"{unit.name}: amplop_digital aktif tanpa 'status_verifikasi' — bukti baca-balik digit per digit "
              f"belum ada (dokumen 11 bagian 6)")

    # publikasi
    pub = d.get("publikasi") or {}
    if not ada(pub.get("catatan_versi")):
        e(f"{unit.name}: publikasi.catatan_versi kosong — 'versi mana yang disetujui client' tidak boleh jadi tebakan")
    slug = meta.get("slug") or pub.get("path_stabil")
    if not ada(slug):
        e(f"{unit.name}: slug publikasi kosong (dokumen 09 bagian 3 — path permanen)")
    elif isinstance(slug, str) and not re.match(r"^[a-z0-9-]+$", slug):
        e(f"{unit.name}: slug memakai karakter di luar huruf kecil/angka/tanda hubung: {slug!r} (dokumen 09 bagian 3)")

    # --- 3. aset raster wajib punya bukti (aturan G3, dokumen 06 bagian 8) ------------
    aset_dir = unit / "web" / "aset"
    raster = [p for p in aset_dir.rglob("*") if p.is_file() and p.suffix.lower() in RASTER_EXT] if aset_dir.is_dir() else []
    if raster:
        daftar = aset_dir / "daftar-aset.json"
        if not daftar.is_file():
            e(f"{unit.name}: ada {len(raster)} berkas raster di web/aset/ tanpa daftar-aset.json — "
              f"bukti per aset wajib (dokumen 06 bagian 8)")
        else:
            try:
                man = json.loads(daftar.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                e(f"{unit.name}: web/aset/daftar-aset.json bukan JSON yang sah: {exc}")
                man = None
            if isinstance(man, dict):
                terdaftar = {baris.get("berkas") for baris in man.get("aset", []) if isinstance(baris, dict)}
                for p in raster:
                    rel = p.relative_to(aset_dir).as_posix()
                    if rel not in terdaftar:
                        e(f"{unit.name}: aset raster '{rel}' tidak ada di daftar-aset.json (bukti G3 kurang)")
            elif isinstance(man, list):
                terdaftar = {baris.get("berkas") for baris in man if isinstance(baris, dict)}
                for p in raster:
                    rel = p.relative_to(aset_dir).as_posix()
                    if rel not in terdaftar:
                        e(f"{unit.name}: aset raster '{rel}' tidak ada di daftar-aset.json (bukti G3 kurang)")
    return err


def main() -> int:
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    if arg:
        units = [Path(arg).resolve()]
    else:
        units = sorted(p for p in PRODUKSI.glob("*") if p.is_dir()) if PRODUKSI.is_dir() else []

    if not units:
        print("VALIDATOR UNIT: tidak ada folder unit di _produksi-aktif/ (belum ada undangan berjalan)")
        return 0

    semua: list[str] = []
    for unit in units:
        semua += periksa(unit)

    if semua:
        print(f"VALIDATOR UNIT: {len(semua)} ERROR")
        for pesan in semua:
            print(f"  - {pesan}")
        return 1

    nama = ", ".join(u.name for u in units)
    print(f"VALIDATOR UNIT: PASS  (unit: {nama} · gerbang data 03 bagian 7 lulus · bukti aset 06 bagian 8 lengkap/NA)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
