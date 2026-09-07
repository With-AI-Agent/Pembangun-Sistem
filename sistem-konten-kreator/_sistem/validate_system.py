#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validator mandiri Sistem Konten Kreator — SELF-CONTAINED.

Pakai (dari root folder sistem, atau dari mana saja):

    python3 _sistem/validate_system.py

Sifat yang wajib dijaga (kontrak paket repo mandiri, `PAKET_REPO_MANDIRI.md`
di repo master):

* Root sistem dihitung sendiri: parent dari folder `_sistem/` tempat berkas
  ini berada. Tidak ada asumsi tentang direktori kerja pemanggil.
* Tidak tahu-menahu soal `_meta/` maupun `tools/`. Tidak mengimpor kode luar
  apa pun — hanya pustaka standar. Alasannya kausal, bukan gaya: sistem ini
  akan diunduh dan dijadikan repo tersendiri; validator yang mengimpor kode
  dari luar folder sistem akan mati begitu foldernya dibawa keluar.
* Keluaran: daftar temuan + satu baris PASS/FAIL + exit code (0 = lolos).

Yang diperiksa:
  1. berkas wajib di root sistem;
  2. dokumen instruksi `_sistem/` 00–09 + START_DI_SINI + STATUS_TEMPLATE;
  3. pegangan pengguna di `panduan/`;
  4. konsistensi arsip naskah tiap channel (`arsip-naskah/` wajib punya
     `indeks.md` + `indeks-karakter.md`; tiap naskah arsip terdaftar di indeks);
  5. tiap unit di `_produksi-aktif/*/` punya `STATUS.md` dengan field yang
     bisa di-parse (termasuk field checkpoint dengan nilai exact);
  6. `SYSTEM_MANIFEST.md` punya baris Versi.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQ_ROOT = [
    "SYSTEM_MANIFEST.md",
    "README.md",
    "PROMPT_ENTRI_UNIVERSAL.md",
    "ACCEPTANCE_TESTS.md",
    "ACCEPTANCE_TEST_LOG.md",
    "QUALITY_ASSURANCE_AND_EVOLUTION.md",
    "PROTOKOL_REVIEW_INDEPENDEN.md",
]
REQ_SISTEM_PREFIX = ["%02d" % i for i in range(0, 10)]   # 00_ .. 09_
REQ_SISTEM_EXACT = ["START_DI_SINI.md", "STATUS_TEMPLATE.md"]
REQ_PANDUAN = ["PANDUAN_PENGGUNA.md"]

SAFE_VALUE = "Tidak ada"
UNIT_STATUS_TOKENS = {
    "in-progress", "blocked", "ready-for-review", "approved", "merged", "abandoned",
}
# Field yang harus bisa dibaca mesin di tiap STATUS.md unit. Daftar statis:
# kewajiban, bukan hasil penemuan — field yang dihapus harus gagal berisik.
REQ_STATUS_FIELDS = [
    "Status",
    "Channel",
    "Model konten",
    "Tahap terakhir selesai",
    "Tahap berikutnya",
    "Output resmi",
    "Sumber eksternal dipakai",
    "Approval yang sudah diberikan",
    "Commit terakhir",
    "PR terkait",
    "Pekerjaan belum tersimpan",
    "Risiko atau blocker",
    "Waktu pembaruan",
]

ARSIP_INDEX_FILES = ["indeks.md", "indeks-karakter.md"]
ARSIP_SIDECAR_SUFFIX = ("-metadata.md", "-sumber.md")

findings = []


def add(msg):
    findings.append(msg)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def strip_fences(text):
    """Isi blok kode dikosongkan: state tidak pernah diambil dari contoh
    yang ditempel di dalam fence."""
    out, in_fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
        elif in_fence:
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def field_values(text, label):
    """Nilai field `- **Label:** nilai` (atau tanpa bold / tanpa bullet),
    line-anchored, di luar fence. Kutipan blok (`>`) tidak dihitung."""
    pattern = re.compile(
        r"^[ \t]*(?:[-*][ \t]+)?\*{0,2}\s*" + re.escape(label) +
        r"\s*[:：]\s*\*{0,2}\s*(.*?)\s*$",
        re.MULTILINE,
    )
    return [m.group(1).strip() for m in pattern.finditer(strip_fences(text))]


# --- 1. berkas wajib root sistem --------------------------------------------
for rel in REQ_ROOT:
    if not os.path.isfile(os.path.join(ROOT, rel)):
        add("berkas wajib root sistem hilang: %s" % rel)

# --- 2. dokumen instruksi _sistem/ ------------------------------------------
sd = os.path.join(ROOT, "_sistem")
have = sorted(x for x in os.listdir(sd) if x.endswith(".md")) if os.path.isdir(sd) else []
if not os.path.isdir(sd):
    add("folder _sistem/ tidak ada")
for pre in REQ_SISTEM_PREFIX:
    if not any(x.startswith(pre + "_") for x in have):
        add("dokumen instruksi hilang: _sistem/%s_*.md" % pre)
for rel in REQ_SISTEM_EXACT:
    if not os.path.isfile(os.path.join(sd, rel)):
        add("dokumen instruksi hilang: _sistem/%s" % rel)

# --- 3. pegangan pengguna ----------------------------------------------------
pd = os.path.join(ROOT, "panduan")
if not os.path.isdir(pd):
    add("folder panduan/ tidak ada (pegangan pengguna wajib)")
else:
    for rel in REQ_PANDUAN:
        if not os.path.isfile(os.path.join(pd, rel)):
            add("pegangan pengguna hilang: panduan/%s" % rel)

# --- 4. arsip naskah tiap channel -------------------------------------------
channels = sorted(
    d for d in os.listdir(ROOT)
    if d.startswith("channel-") and os.path.isdir(os.path.join(ROOT, d))
)
arsip_dirs = []
for ch in channels:
    for cur, dirs, files in os.walk(os.path.join(ROOT, ch)):
        if os.path.basename(cur) == "arsip-naskah":
            arsip_dirs.append(cur)
if channels and not arsip_dirs:
    add("ada folder channel-* tapi tidak satu pun punya arsip-naskah/ "
        "(kontrak arsip naskah + indeks karakter)")
for ad in sorted(arsip_dirs):
    rel_ad = os.path.relpath(ad, ROOT).replace(os.sep, "/")
    for idx in ARSIP_INDEX_FILES:
        if not os.path.isfile(os.path.join(ad, idx)):
            add("arsip naskah tidak konsisten: %s/%s tidak ada" % (rel_ad, idx))
    idx_path = os.path.join(ad, "indeks.md")
    if os.path.isfile(idx_path):
        idx_text = read(idx_path)
        for fn in sorted(os.listdir(ad)):
            if not fn.endswith(".md") or fn in ARSIP_INDEX_FILES:
                continue
            if fn.endswith(ARSIP_SIDECAR_SUFFIX):
                continue
            if fn not in idx_text:
                add("arsip naskah tidak konsisten: %s/%s tidak tercatat di indeks.md"
                    % (rel_ad, fn))

# --- 5. unit produksi aktif --------------------------------------------------
pa = os.path.join(ROOT, "_produksi-aktif")
units = []
if os.path.isdir(pa):
    units = sorted(d for d in os.listdir(pa) if os.path.isdir(os.path.join(pa, d)))
for unit in units:
    rel_unit = "_produksi-aktif/%s" % unit
    sp = os.path.join(pa, unit, "STATUS.md")
    if not os.path.isfile(sp):
        add("unit tanpa checkpoint: %s/STATUS.md tidak ada" % rel_unit)
        continue
    text = read(sp)
    for label in REQ_STATUS_FIELDS:
        vals = field_values(text, label)
        if not vals:
            add("%s/STATUS.md: field '%s' tidak ada atau tidak bisa di-parse"
                % (rel_unit, label))
        elif label == "Pekerjaan belum tersimpan":
            if len(vals) > 1:
                add("%s/STATUS.md: field 'Pekerjaan belum tersimpan' muncul %d kali "
                    "(bukti ganda = tidak deterministik)" % (rel_unit, len(vals)))
            else:
                value = vals[0].strip("`").strip()
                if not value:
                    add("%s/STATUS.md: field 'Pekerjaan belum tersimpan' kosong" % rel_unit)
                elif value != SAFE_VALUE and "tidak ada" in value.lower():
                    add("%s/STATUS.md: 'Pekerjaan belum tersimpan' harus exact '%s' "
                        "(case-sensitive) — ditemui %r" % (rel_unit, SAFE_VALUE, value))
        elif label == "Status":
            token = vals[0].strip().strip("*").strip("`").strip()
            if token not in UNIT_STATUS_TOKENS:
                add("%s/STATUS.md: nilai Status %r bukan salah satu dari %s"
                    % (rel_unit, token, ", ".join(sorted(UNIT_STATUS_TOKENS))))

# Template checkpoint harus memakai nilai exact, bukan petunjuk pengisian.
tp = os.path.join(sd, "STATUS_TEMPLATE.md")
if os.path.isfile(tp):
    vals = field_values(read(tp), "Pekerjaan belum tersimpan")
    if len(vals) != 1:
        add("_sistem/STATUS_TEMPLATE.md: field 'Pekerjaan belum tersimpan' harus "
            "muncul tepat sekali (ditemui %d)" % len(vals))
    elif vals[0].strip("`").strip() != SAFE_VALUE:
        add("_sistem/STATUS_TEMPLATE.md: nilai field checkpoint harus exact %r "
            "(ditemui %r)" % (SAFE_VALUE, vals[0]))

# --- 6. manifest punya baris Versi ------------------------------------------
mp = os.path.join(ROOT, "SYSTEM_MANIFEST.md")
if os.path.isfile(mp):
    if not field_values(read(mp), "Versi"):
        add("SYSTEM_MANIFEST.md: baris Versi tidak ada atau tidak bisa di-parse")

# --- keluaran ----------------------------------------------------------------
print("VALIDATOR SISTEM KONTEN KREATOR")
print("  root sistem      :", os.path.basename(ROOT) + "/")
print("  channel          :", ", ".join(channels) if channels else "TIDAK ADA")
print("  arsip naskah     :", len(arsip_dirs))
print("  unit produksi    :", ", ".join(units) if units else "TIDAK ADA")
print("  temuan           :", len(findings))
for f in findings:
    print("  - " + f)
print("HASIL: " + ("PASS" if not findings else "FAIL"))
sys.exit(0 if not findings else 1)
