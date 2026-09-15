# -*- coding: utf-8 -*-
"""Validator mandiri Sistem Presentasi (self-contained). Cek kelengkapan dokumen
sistem + kelengkapan living-docs tiap deck. Exit 0 = struktur lengkap.
Pakai: python3 _sistem/validate_system.py   (dari root folder sistem-presentasi/)

Adaptasi 7 Sep 2026 (kontrak paket repo mandiri, `PAKET_REPO_MANDIRI.md` di
repo master): daftar periksa disetarakan dengan validator sistem lain —
ditambah (a) baris Versi di SYSTEM_MANIFEST.md, (b) field checkpoint
"Pekerjaan belum tersimpan" yang bisa di-parse di tiap STATUS deck + template
T6, (c) baris HASIL: PASS/FAIL. Yang sudah benar TIDAK ditulis ulang: root
tetap dihitung sendiri, tanpa impor kode luar, jalur exit code tetap sama
(0 = lolos, 1 = ada temuan), dan baris keluaran lama dipertahankan apa adanya.
"""
import os, re, sys

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sistem-presentasi/
REQ_ROOT=["START_DI_SINI.md","SYSTEM_MANIFEST.md","00_RENCANA_KERANGKA.md","ACCEPTANCE_TESTS.md","PANDUAN_PENGGUNA.md","PROMPT_ENTRI_UNIVERSAL.md"]
REQ_SISTEM=[f"{i:02d}" for i in range(1,12)]
REQ_GEN=["G1_DISCOVERY_BRIEF.md","G2_DISCOVERY_VISUAL.md","G3_DISCOVERY_KETENTUAN.md"]
REQ_TPL=[f"T{i}_{n}.md" for i,n in [(1,"BRIEF"),(2,"PEMAHAMAN_BAHAN"),(3,"CHECKLIST_CAKUPAN"),(4,"OUTLINE"),(5,"RENCANA_VISUAL"),(6,"STATUS"),(7,"ASET_GAYA"),(8,"PAKET_KETENTUAN"),(9,"DAFTAR_GAMBAR")]]
REQ_DECK=["BRIEF.md","PEMAHAMAN_BAHAN.md","CHECKLIST_CAKUPAN.md","OUTLINE.md","RENCANA_VISUAL.md","STATUS.md","PERKATAAN_PEMILIK_VERBATIM.md","DAFTAR_GAMBAR.md"]

SAFE_VALUE="Tidak ada"
temuan=[]

def _strip_fences(text):
    out,in_fence=[],False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence=not in_fence; out.append("")
        elif in_fence: out.append("")
        else: out.append(line)
    return "\n".join(out)

def field_values(text,label):
    pat=re.compile(r"^[ \t]*(?:[-*][ \t]+)?\*{0,2}\s*"+re.escape(label)+r"\s*[:：]\s*\*{0,2}\s*(.*?)\s*$",re.MULTILINE)
    return [m.group(1).strip() for m in pat.finditer(_strip_fences(text))]

def read(p):
    with open(p,encoding="utf-8") as fh: return fh.read()

def cek_checkpoint(rel,path):
    """Field checkpoint wajib ada tepat sekali dan nilainya bisa dipercaya."""
    vals=field_values(read(path),"Pekerjaan belum tersimpan")
    if not vals:
        temuan.append(f"{rel}: field 'Pekerjaan belum tersimpan' tidak ada")
    elif len(vals)>1:
        temuan.append(f"{rel}: field 'Pekerjaan belum tersimpan' muncul {len(vals)} kali (bukti ganda = tidak deterministik)")
    else:
        v=vals[0].strip("`").strip()
        if not v:
            temuan.append(f"{rel}: field 'Pekerjaan belum tersimpan' kosong")
        elif v!=SAFE_VALUE and "tidak ada" in v.lower():
            temuan.append(f"{rel}: 'Pekerjaan belum tersimpan' harus exact '{SAFE_VALUE}' (case-sensitive) — ditemui {v!r}")

missing=[]
for f in REQ_ROOT:
    if not os.path.exists(os.path.join(ROOT,f)): missing.append(f)
sd=os.path.join(ROOT,"_sistem")
have=sorted(x for x in os.listdir(sd) if x.endswith(".md")) if os.path.isdir(sd) else []
for pre in REQ_SISTEM:
    if not any(x.startswith(pre+"_") for x in have): missing.append(f"_sistem/{pre}_*")
for f in REQ_GEN:
    if not os.path.exists(os.path.join(ROOT,"_generator",f)): missing.append(f"_generator/{f}")
for f in REQ_TPL:
    if not os.path.exists(os.path.join(ROOT,"_template",f)): missing.append(f"_template/{f}")

da=os.path.join(ROOT,"deck-aktif")
decks=sorted(os.listdir(da)) if os.path.isdir(da) else []
for d in decks:
    dp=os.path.join(da,d)
    if not os.path.isdir(dp): continue
    for f in REQ_DECK:
        if not os.path.exists(os.path.join(dp,f)): missing.append(f"deck-aktif/{d}/{f}")
    sp=os.path.join(dp,"STATUS.md")
    if os.path.isfile(sp): cek_checkpoint(f"deck-aktif/{d}/STATUS.md",sp)

# Template checkpoint: nilai harus exact, bukan petunjuk pengisian.
t6=os.path.join(ROOT,"_template","T6_STATUS.md")
if os.path.isfile(t6): cek_checkpoint("_template/T6_STATUS.md",t6)

# Manifest wajib punya baris Versi yang bisa di-parse (dipakai pembangkit paket).
mp=os.path.join(ROOT,"SYSTEM_MANIFEST.md")
if os.path.isfile(mp) and not field_values(read(mp),"Versi"):
    temuan.append("SYSTEM_MANIFEST.md: baris Versi tidak ada atau tidak bisa di-parse")

print("deck ditemukan:", decks if decks else "TIDAK ADA")
print("SAKTI/struktur lengkap?" , "YA" if not missing else "BELUM")
if missing: print("KURANG:", *missing, sep="\n  - ")
print("temuan isi:", len(temuan))
for t in temuan: print("  - " + t)
print("HASIL: " + ("PASS" if not missing and not temuan else "FAIL"))
sys.exit(0 if not missing and not temuan else 1)
