#!/usr/bin/env python3
"""Uji T-28: apakah "LOLOS BERSYARAT" (upscale AI) layak dijanjikan di lingkungan ini?

Dibuat 17 Sep 2026 untuk MENENTUKAN dengan angka, bukan asumsi, apakah gerbang G3 jalur
"LOLOS BERSYARAT" boleh ditulis sebagai tersedia.

Dua pertanyaan yang dijawab:
  1. BISAKAH dijalankan di sini? (keterjangkauan paket + bobot model)
  2. SEBERAPA BAGUS hasilnya, dan BEDA-KAH perilakunya untuk FOTO vs GARIS HALUS/TEKS?
     (riset berkata AI upscaling "mangle text" — klaim itu DIUJI di sini, tidak dipercaya begitu saja)

Metrik: PSNR (dB) + SSIM (Gaussian 11x11, sigma 1.5, per kanal lalu rata-rata) — implementasi sendiri,
mengikuti preseden repo di DISKUSI_MENTAH bagian J.1.

Reproduksi:
    python3 -m pip install --break-system-packages numpy pillow opencv-contrib-python-headless
    # model diunduh lewat codeload.github.com (raw.githubusercontent.com DIBLOKIR di lingkungan ini)
    python3 _meta/_internal/uji/uji_upscaling.py
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import cv2
import numpy as np

MODEL_DIR = Path(os.environ.get("MODEL_DIR", "/tmp/mdl"))
SKALA = 2  # skala yang DIUJI pada 17 Sep 2026, BUKAN ambang keputusan. Gerbang G3 FINAL
           # membatasi kenaikan <= 1,5x untuk foto (00_RENCANA_KERANGKA.md 4.4/4.5 + Log
           # Keputusan); 2x justru diuji untuk mengukur batas ATASnya. Nilai dan hasil ukur
           # di berkas ini TIDAK diubah - ini artefak bukti, hanya komentarnya diluruskan
           # (temuan review independen putaran 2 PR #74).


# ---------------------------------------------------------------- metrik
def psnr(a: np.ndarray, b: np.ndarray) -> float:
    mse = float(np.mean((a.astype(np.float64) - b.astype(np.float64)) ** 2))
    if mse <= 1e-12:
        return float("inf")
    return 10.0 * np.log10(255.0**2 / mse)


def _ssimKanal(x: np.ndarray, y: np.ndarray) -> float:
    C1, C2 = (0.01 * 255) ** 2, (0.03 * 255) ** 2
    x = x.astype(np.float64)
    y = y.astype(np.float64)
    k = (11, 11)
    mu_x = cv2.GaussianBlur(x, k, 1.5)
    mu_y = cv2.GaussianBlur(y, k, 1.5)
    mu_x2, mu_y2, mu_xy = mu_x * mu_x, mu_y * mu_y, mu_x * mu_y
    s_x = cv2.GaussianBlur(x * x, k, 1.5) - mu_x2
    s_y = cv2.GaussianBlur(y * y, k, 1.5) - mu_y2
    s_xy = cv2.GaussianBlur(x * y, k, 1.5) - mu_xy
    num = (2 * mu_xy + C1) * (2 * s_xy + C2)
    den = (mu_x2 + mu_y2 + C1) * (s_x + s_y + C2)
    return float(np.mean(num / den))


def ssim(a: np.ndarray, b: np.ndarray) -> float:
    """Rata-rata 3 kanal (kalau grayscale, satu kanal)."""
    if a.ndim == 2:
        return _ssimKanal(a, b)
    return float(np.mean([_ssimKanal(a[:, :, i], b[:, :, i]) for i in range(a.shape[2])]))


# ---------------------------------------------------------------- bahan uji
def cari_foto_repo() -> Path | None:
    """Foto NYATA dari repo (bukan sintetis) — preseden J.1 memakai bahan nyata."""
    root = Path(__file__).resolve().parents[3]
    terbaik, luas = None, 0
    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue
        try:
            im = cv2.imread(str(p))
            if im is None:
                continue
            h, w = im.shape[:2]
            if w * h > luas and w >= 600 and h >= 600:
                luas, terbaik = w * h, p
        except Exception:
            continue
    return terbaik


def buat_uji_garis(w: int = 512, h: int = 512) -> np.ndarray:
    """Gambar uji GARIS HALUS + bentuk mirip teks — kategori yang riset katakan PALING BURUK
    untuk upscaling. Bukan font sungguhan (font sistem kosong di lingkungan ini), jadi yang
    diuji adalah perilaku pada GURATAN TIPIS dan tepi geometris bernada tinggi.
    """
    img = np.full((h, w, 3), 255, np.uint8)
    # guratan makin tipis: 6,4,3,2,1 piksel — yang 1-2 px adalah kasus paling merusak
    for i, tebal in enumerate((6, 4, 3, 2, 1)):
        y = 40 + i * 60
        cv2.line(img, (30, y), (w - 30, y), (20, 20, 20), tebal)
    # "huruf" tiruan dari garis tipis (meniru letterform: batang + serif)
    for k, x0 in enumerate(range(40, w - 60, 70)):
        y0, y1 = 360, 470
        cv2.line(img, (x0, y0), (x0, y1), (10, 10, 10), 2)          # batang
        cv2.line(img, (x0 - 8, y0), (x0 + 8, y0), (10, 10, 10), 2)   # serif atas
        cv2.line(img, (x0 - 8, y1), (x0 + 8, y1), (10, 10, 10), 2)   # serif bawah
        cv2.line(img, (x0, y0 + 55), (x0 + 26, y0 + 55), (10, 10, 10), 2)
    # grid halus bernada tinggi (menguji moire/aliasing)
    for x in range(0, w, 6):
        cv2.line(img, (x, 300), (x, 340), (60, 60, 60), 1)
    return img


# ---------------------------------------------------------------- metode
def muat_sr(nama_algo: str, nama_berkas: str, skala: int):
    kandidat = list(MODEL_DIR.rglob(nama_berkas))
    if not kandidat:
        return None, f"model {nama_berkas} tidak ditemukan"
    try:
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        sr.readModel(str(kandidat[0]))
        sr.setModel(nama_algo, skala)
        return sr, None
    except Exception as e:
        return None, f"gagal memuat {nama_berkas}: {str(e)[:110]}"


def jalankan(label: str, fn, low: np.ndarray, gt: np.ndarray, hasil: list):
    t0 = time.time()
    try:
        out = fn(low)
    except Exception as e:
        hasil.append((label, None, None, None, f"GAGAL: {str(e)[:90]}"))
        return
    dt = time.time() - t0
    if out.shape[:2] != gt.shape[:2]:
        out = cv2.resize(out, (gt.shape[1], gt.shape[0]), interpolation=cv2.INTER_AREA)
    hasil.append((label, psnr(out, gt), ssim(out, gt), dt, None))


# ---------------------------------------------------------------- utama
def main() -> int:
    print("=" * 84)
    print("UJI T-28 — kelayakan & mutu upscale untuk gerbang G3 jalur 'LOLOS BERSYARAT'")
    print(f"skala = {SKALA}x  ·  metrik = PSNR (dB) + SSIM  ·  model dir = {MODEL_DIR}")
    print("=" * 84)

    print("\n[1] KETERSEDIAAN komponen")
    for pkg in ("numpy", "cv2", "vtracer", "svgwrite"):
        try:
            m = __import__(pkg)
            print(f"    {pkg:<10} ADA {getattr(m, '__version__', '')}")
        except ImportError:
            print(f"    {pkg:<10} TIDAK ADA")

    sr_list = []
    for algo, berkas in (("fsrcnn", "FSRCNN_x2.pb"), ("espcn", "ESPCN_x2.pb"),
                         ("edsr", "EDSR_x2.pb"), ("lapsrn", "LapSRN_x2.pb")):
        sr, err = muat_sr(algo, berkas, SKALA)
        if sr is None:
            print(f"    {algo:<8} TIDAK BISA — {err}")
        else:
            ukuran = next(MODEL_DIR.rglob(berkas)).stat().st_size
            print(f"    {algo:<8} BISA   (model {ukuran/1024:.0f} KB)")
            sr_list.append((algo, sr))

    foto = cari_foto_repo()
    if foto is None:
        print("\nTIDAK ADA foto repo yang cukup besar untuk diuji")
        return 2
    print(f"\n[2] Bahan uji FOTO nyata: {foto.name}")
    asli = cv2.imread(str(foto))
    # ground truth = ukuran cetak; sumber = separuhnya (setara 150 DPI vs 300 DPI)
    H, W = asli.shape[:2]
    tw, th = min(W, 900), min(H, 900)
    gt_foto = cv2.resize(asli, (tw - tw % 2, th - th % 2), interpolation=cv2.INTER_AREA)
    low_foto = cv2.resize(gt_foto, (gt_foto.shape[1] // 2, gt_foto.shape[0] // 2),
                          interpolation=cv2.INTER_AREA)
    print(f"    ground truth {gt_foto.shape[1]}x{gt_foto.shape[0]} · sumber rendah "
          f"{low_foto.shape[1]}x{low_foto.shape[0]} (= simulasi 150 DPI untuk 300 DPI)")

    gt_garis = buat_uji_garis()
    low_garis = cv2.resize(gt_garis, (gt_garis.shape[1] // 2, gt_garis.shape[0] // 2),
                           interpolation=cv2.INTER_AREA)
    print(f"\n[3] Bahan uji GARIS HALUS/teks tiruan: ground truth {gt_garis.shape[1]}x"
          f"{gt_garis.shape[0]} · sumber rendah {low_garis.shape[1]}x{low_garis.shape[0]}")

    metode = [
        ("bicubic (bukan AI)", lambda im: cv2.resize(im, None, fx=SKALA, fy=SKALA,
                                                     interpolation=cv2.INTER_CUBIC)),
        ("lanczos4 (bukan AI)", lambda im: cv2.resize(im, None, fx=SKALA, fy=SKALA,
                                                      interpolation=cv2.INTER_LANCZOS4)),
    ] + [(f"{n} (AI)", lambda im, s=s: s.upsample(im)) for n, s in sr_list]

    for judul, low, gt in (("FOTO", low_foto, gt_foto),
                           ("GARIS HALUS / teks tiruan", low_garis, gt_garis)):
        print(f"\n[4] Hasil pada {judul}  —  lebih tinggi lebih baik")
        print(f"    {'metode':<24}{'PSNR dB':>10}{'SSIM':>9}{'detik':>9}   catatan")
        print("    " + "-" * 66)
        hasil: list = []
        for label, fn in metode:
            jalankan(label, fn, low, gt, hasil)
        for label, p, s, dt, err in hasil:
            if err:
                print(f"    {label:<24}{'—':>10}{'—':>9}{'—':>9}   {err}")
            else:
                print(f"    {label:<24}{p:>10.2f}{s:>9.4f}{dt:>9.2f}")

    print("\n[5] Skala penilaian (dipakai repo ini, bagian J.1 — bukan karangan baru):")
    print("    PSNR >=40 & SSIM >=0,99 = nyaris tak terbedakan")
    print("    PSNR 35-40 & SSIM 0,97-0,99 = sangat baik")
    print("    PSNR <32 = degradasi mulai terlihat")
    print("\n[6] Yang TIDAK diuji di sini (jangan disimpulkan dari angka di atas):")
    print("    - font sungguhan (font sistem kosong di lingkungan ini) — yang diuji GURATAN TIPIS,")
    print("      jadi kesimpulan untuk 'teks' berlaku untuk bentuk huruf bergaris tipis, bukan")
    print("      pengukuran pada tipografi nyata")
    print("    - CMYK/bleed/PDF-X: upscaling TIDAK menyentuhnya (riset: 'resolution only')")
    print("    - mutu cetak fisik: tidak ada printer di lingkungan ini; PSNR/SSIM adalah proksi")
    return 0


if __name__ == "__main__":
    sys.exit(main())
