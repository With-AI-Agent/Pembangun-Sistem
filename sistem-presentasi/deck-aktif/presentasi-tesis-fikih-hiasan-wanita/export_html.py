# -*- coding: utf-8 -*-
"""Render preview HTML dari .pptx final (identik dengan berkas). Dir=rtl, palet A."""
from pptx import Presentation

P = "sistem-presentasi/deck-aktif/presentasi-tesis-fikih-hiasan-wanita/keluaran/presentasi-tesis-fikih-hiasan-wanita.pptx"
OUT = "sistem-presentasi/deck-aktif/presentasi-tesis-fikih-hiasan-wanita/keluaran/preview.html"

prs = Presentation(P)
GREEN="#0F3D2E"; GOLD="#C9A227"; CREAM="#F7F3E9"

def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

parts=[]
for idx,s in enumerate(prs.slides,1):
    title=""; bullets=[]; foot=""; table=None; note=""
    for sh in s.shapes:
        if sh.has_table:
            table=sh.table; continue
        if sh.has_text_frame and sh.text_frame.text.strip():
            lines=[l for l in sh.text_frame.text.splitlines() if l.strip()]
            if not lines: continue
            top_in = (sh.top or 0)/914400.0
            if top_in < 1.5:
                title=lines[0]; bullets+=lines[1:]
            elif top_in > 6.5:
                foot=lines[0]
            else:
                bullets+=lines
    try: note=s.notes_slide.notes_text_frame.text
    except Exception: note=""
    if idx==1 and not title and bullets:
        title=bullets.pop(0)
    h=f'<section class="slide"><div class="band"></div>'
    h+=f'<h2>{esc(title)}</h2><div class="rule"></div>'
    if bullets:
        h+='<ul>'+''.join(f'<li>{esc(b)}</li>' for b in bullets)+'</ul>'
    if table is not None:
        h+='<table>'
        for r in range(len(table.rows)):
            h+='<tr>'+''.join(f'<th>{esc(table.cell(r,0).text)}</th><td>{esc(table.cell(r,1).text)}</td>' if r else f'<th>{esc(table.cell(r,0).text)}</th><th>{esc(table.cell(r,1).text)}</th>')+'</tr>'
        h+='</table>'
    if note: h+=f'<p class="note">🗒 {esc(note)}</p>'
    h+=f'<div class="fbar"><span class="fnum">{idx}</span><span class="fsrc">{esc(foot)}</span></div></section>'
    parts.append(h)

css=f"""body{{margin:0;background:#2b2b2b;font-family:'Amiri','Traditional Arabic',serif}}
.slide{{position:relative;background:{CREAM};max-width:960px;margin:24px auto;padding:48px 64px 70px;direction:rtl;text-align:right;box-shadow:0 6px 24px rgba(0,0,0,.5);min-height:500px}}
.band{{position:absolute;top:0;right:0;width:14px;height:100%;background:{GREEN};box-shadow:-5px 0 0 {GOLD}}}
.fbar{{position:absolute;bottom:0;left:0;right:0;height:34px;background:{GREEN};display:flex;align-items:center;justify-content:space-between;padding:0 20px;color:{GOLD};font-size:13px}}
h2{{color:{GREEN};font-size:26px;margin:0 0 4px}}
.rule{{width:55%;height:4px;background:{GOLD};margin:0 0 20px}}
ul{{list-style:none;padding:0;margin:0}}
li{{font-size:20px;color:#1E1E1E;margin:0 0 12px;padding-right:18px;position:relative}}
li:before{{content:'◆';color:{GOLD};position:absolute;right:0;font-size:12px;top:6px}}
table{{border-collapse:collapse;width:100%;margin-top:6px}}
th,td{{border:1px solid {GOLD};padding:8px 12px;font-size:17px;text-align:right}}
th{{background:{GREEN};color:{CREAM}}}
tr:nth-child(even) td{{background:#ECE6D6}}
.note{{margin-top:18px;font-size:13px;color:#666;font-family:sans-serif;direction:rtl}}
.no{{position:absolute;bottom:10px;left:16px;color:{GOLD};font-size:12px}}
.foot{{position:absolute;bottom:10px;right:64px;color:{GOLD};font-size:13px}}
h1.head{{color:{CREAM};text-align:center;font-size:20px;padding:18px;font-family:sans-serif}}"""

html=f'<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>Preview Deck</title><style>{css}</style></head><body><h1 class="head">Preview — أحكام النوازل الفقهية المتعلقة بزينة المرأة (13 slide)</h1>'+''.join(parts)+'</body></html>'
open(OUT,"w",encoding="utf-8").write(html)
print("written", OUT, "slides:", len(parts))
