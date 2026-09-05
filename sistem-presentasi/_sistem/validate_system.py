# -*- coding: utf-8 -*-
"""Validator mandiri Sistem Presentasi (self-contained). Cek kelengkapan dokumen
sistem + kelengkapan living-docs tiap deck. Exit 0 = struktur lengkap.
Pakai: python3 _sistem/validate_system.py   (dari root folder sistem-presentasi/)"""
import os, sys

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sistem-presentasi/
REQ_ROOT=["START_DI_SINI.md","SYSTEM_MANIFEST.md","00_RENCANA_KERANGKA.md","ACCEPTANCE_TESTS.md","PANDUAN_PENGGUNA.md","PROMPT_ENTRI_UNIVERSAL.md"]
REQ_SISTEM=[f"{i:02d}" for i in range(1,12)]
REQ_GEN=["G1_DISCOVERY_BRIEF.md","G2_DISCOVERY_VISUAL.md","G3_DISCOVERY_KETENTUAN.md"]
REQ_TPL=[f"T{i}_{n}.md" for i,n in [(1,"BRIEF"),(2,"PEMAHAMAN_BAHAN"),(3,"CHECKLIST_CAKUPAN"),(4,"OUTLINE"),(5,"RENCANA_VISUAL"),(6,"STATUS"),(7,"ASET_GAYA"),(8,"PAKET_KETENTUAN"),(9,"DAFTAR_GAMBAR")]]
REQ_DECK=["BRIEF.md","PEMAHAMAN_BAHAN.md","CHECKLIST_CAKUPAN.md","OUTLINE.md","RENCANA_VISUAL.md","STATUS.md","PERKATAAN_PEMILIK_VERBATIM.md","DAFTAR_GAMBAR.md"]

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

print("deck ditemukan:", decks if decks else "TIDAK ADA")
print("SAKTI/struktur lengkap?" , "YA" if not missing else "BELUM")
if missing: print("KURANG:", *missing, sep="\n  - ")
sys.exit(0 if not missing else 1)
