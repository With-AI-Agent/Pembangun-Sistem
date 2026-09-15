# -*- coding: utf-8 -*-
"""Build .pptx RTL (Arab) untuk deck tesis fikih hiasan wanita.
Sumber konten: PEMAHAMAN_BAHAN.md + OUTLINE.md (semua berjejak halaman).
Menjalankan aturan lantai: judul assertion, naskah->notes, jejak sumber, RTL, font>=20.
"""
from pptx import Presentation
from pptx.util import Pt, Inches
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

GREEN = RGBColor(0x0F, 0x3D, 0x2E)
GOLD  = RGBColor(0xC9, 0xA2, 0x27)
CREAM = RGBColor(0xF7, 0xF3, 0xE9)
INK   = RGBColor(0x1E, 0x1E, 0x1E)
FONT  = "Amiri"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

def rtl_run(run, size, bold, color):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    for tag in ("a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is None:
            el = rPr.makeelement(qn(tag), {})
            rPr.append(el)
        el.set("typeface", FONT)

def rtl_para(p, size, bold, color, space_after=8):
    p.alignment = PP_ALIGN.RIGHT
    pPr = p._p.get_or_add_pPr()
    pPr.set("rtl", "1")
    p.space_after = Pt(space_after)
    rtl_run(p.runs[0], size, bold, color) if p.runs else None

def set_bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = CREAM

def add_box(slide, left, top, width, height):
    return slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))

def new_slide():
    s = prs.slides.add_slide(BLANK)
    set_bg(s)
    # pita identitas vertikal di kanan (RTL)
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(13.333-0.28), 0, Inches(0.28), Inches(7.5))
    band.fill.solid(); band.fill.fore_color.rgb = GREEN
    band.line.fill.background()
    return s

def title(slide, text):
    tb = add_box(slide, 0.6, 0.35, 12.1, 1.0)
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = text
    rtl_para(p, 30, True, GREEN, space_after=4)
    # garis emas bawah judul
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(13.333-0.28-6.2), Inches(1.32), Inches(6.2), Inches(0.05))
    line.fill.solid(); line.fill.fore_color.rgb = GOLD
    line.line.fill.background()

def bullets(slide, items, size=22):
    tb = add_box(slide, 0.8, 1.7, 11.7, 5.0)
    tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = item
        rtl_para(p, size, False, INK, space_after=10)

def footnote(slide, text):
    tb = add_box(slide, 0.5, 7.0, 5.0, 0.4)
    tf = tb.text_frame
    p = tf.paragraphs[0]; p.text = text
    p.alignment = PP_ALIGN.LEFT
    p.runs[0].font.size = Pt(12); p.runs[0].font.color.rgb = GOLD

def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text

def table_slide(slide, rows):
    tbl_shape = slide.shapes.add_table(len(rows), 2, Inches(1.2), Inches(1.8), Inches(10.9), Inches(4.6))
    t = tbl_shape.table
    t.columns[0].width = Inches(3.2); t.columns[1].width = Inches(7.7)
    for r, (c0, c1) in enumerate(rows):
        for c, val in ((0, c0), (1, c1)):
            cell = t.cell(r, c)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.RIGHT
            pPr = p._p.get_or_add_pPr(); pPr.set("rtl", "1")
            run = p.runs[0]
            run.font.name = FONT
            run.font.size = Pt(18 if r else 20)
            run.font.bold = (r == 0)
            for tag in ("a:ea", "a:cs"):
                rPr = run._r.get_or_add_rPr()
                el = rPr.find(qn(tag)) or rPr.makeelement(qn(tag), {})
                if el not in rPr: rPr.append(el)
                el.set("typeface", FONT)
            if r == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = GREEN
                run.font.color.rgb = CREAM
            elif r % 2 == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0xEC,0xE6,0xD6)
            else:
                cell.fill.solid(); cell.fill.fore_color.rgb = CREAM
    return t

# ===== SLIDE 1: JUDUL =====
s = new_slide()
tb = add_box(s, 0.6, 2.2, 12.1, 2.2)
tf = tb.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]; p.text = "أحكام النوازل الفقهية المعاصرة المتعلقة بزينة المرأة في المذاهب الأربعة"
rtl_para(p, 36, True, GREEN, space_after=16)
p2 = tf.add_paragraph(); p2.text = "إعداد: الشيخ علي بلعيدي"
rtl_para(p2, 24, False, INK)
footnote(s, "ص٦ (موضوع من الملخص) · اسم المشرف/الجامعة: diisi pengguna")
notes(s, "Slide pembuka. Nama pembimbing/universitas TIDAK ada di bahan -> dikosongkan, jangan dikarang. Topik dari ملخص hal 6; nama dari nama berkas.")

# ===== SLIDE 2: RINGKASAN =====
s = new_slide(); title(s, "البحث يبيّن أحكام زينة المرأة المعاصرة في المذاهب الأربعة بمنهج وصفي مقارن")
bullets(s, [
 "الموضوعات: التشقير، الأظافر، الحواجب، العدسات، النمص، الوشم، الوصل، العمليات الجراحية",
 "المنهج: وصفي مقارن، استقرائي، استنباطي",
 "الأصل: التحريم عند تغيير خلق الله أو التدليس أو الضرر",
])
footnote(s, "ص٦"); notes(s, "Ringkasan (hal 6): penelitian memaparkan hukum kontemporer hiasan wanita dalam 4 mazhab.")

# ===== SLIDE 3: TUJUAN =====
s = new_slide(); title(s, "أربعة أهداف: من حكم الأدوات والعمليات والبيع إلى أثر الزينة على النكاح")
bullets(s, [
 "بيان حكم أدوات التجميل المعاصرة للمرأة في المذاهب الأربعة",
 "معرفة حكم عمليات التجميل في المذاهب الأربعة المعتمدة",
 "معرفة حكم بيع أدوات التجميل للمرأة في المذاهب الأربعة",
 "بيان الأثر المترتب على الزينة في عقد النكاح",
])
footnote(s, "ص٢١"); notes(s, "Tujuan (hal 21): 4 poin.")

# ===== SLIDE 4: MANFAAT =====
s = new_slide(); title(s, "الفوائد توازي الأهداف: معرفة الحكم وبيان النوازل وإدراك الأثر")
bullets(s, [
 "معرفة أحكام الزينة المعاصرة في المذاهب الأربعة",
 "بيان أحكام النوازل المتعلقة بزينة المرأة",
 "معرفة حكم عمليات التجميل للمرأة",
 "معرفة حكم بيع أدوات التجميل الممنوعة",
 "إدراك أثر الزينة على عقد النكاح",
])
footnote(s, "ص٢١"); notes(s, "Manfaat (hal 21): 5 poin.")

# ===== SLIDE 5: MASALAH =====
s = new_slide(); title(s, "خمس مشكلات: نوازل لم تُفصَّل، صعوبة الحصر، اختلاف الأزمنة، واردات الغرب، اختلاف التكييف")
bullets(s, [
 "النوازل معاصرة لم يفصّلها الفقهاء قديمًا",
 "كثرة وسائل الزينة واختلاط العادات يصعّب الحصر",
 "اختلاف الأزمنة يستدعي نظر القواعد والضوابط",
 "ورود أدوات من الغرب دون نظر شرعي",
 "اختلاف التكييف الفقهي لوسائل الزينة",
])
footnote(s, "ص٢١"); notes(s, "Masalah (hal 21): 5 poin.")

# ===== SLIDE 6: METODE =====
s = new_slide(); title(s, "ثلاثة مناهج متكاملة: وصفي مقارن، استقرائي، استنباطي")
bullets(s, [
 "وصفي مقارن: تتبّع أقوال المذاهب من كتبها المعتمدة ومقارنتها",
 "استقرائي: استقراء النوازل والدراسات المعاصرة",
 "استنباطي: استنباط الأحكام من النصوص والقواعد",
])
footnote(s, "ص٢٣"); notes(s, "Metode (hal 23): 3 pendekatan.")

# ===== SLIDE 7: PERTANYAAN =====
s = new_slide(); title(s, "الأسئلة توازي الأهداف ويُجاب عنها في الباب الرابع")
bullets(s, [
 "السؤال الأول: ما حكم استعمال أدوات التجميل المعاصرة للمرأة في المذاهب الأربعة؟",
 "الأسئلة ٢–٤ توازي الأهداف: العمليات، البيع، أثر الزينة على النكاح",
 "الإجابات مفصّلة في الباب الرابع",
])
footnote(s, "ص٩٠"); notes(s, "Pertanyaan (hal 90 + rekonstruksi dari tujuan hal 21). Q2-4 direkonstruksi dari 4 tujuan; tandai demikian.")

# ===== SLIDE 8: OLEH (tabel) =====
s = new_slide(); title(s, "اتفقوا على الجواز بغير شعر الآدمي، واختلفوا في العلة — والراجح التدليس")
table_slide(s, [
 ("المذهب", "العلة في تحريم وصل الشعر"),
 ("الحنفية", "كرامة الإنسان وتحريم الابتذال بأجزاء الآدمي"),
 ("المالكية", "مركّبة: تغيير خلق الله + التدليس (غير مقيد)"),
 ("الشافعية", "مركّبة: كرامة الإنسان + تحريم استعمال النجس"),
 ("الحنابلة", "التدليس والغش"),
 ("الراجح", "الزور والتدليس (حديث المرأة التي وصلت شعرها)"),
])
footnote(s, "ص٦٦–٦٧"); notes(s, "العلة (hal 66-67). Konsensus: boleh menyambung dengan bukan rambut manusia. Kesimpulan penulis: yang rajih = الزور/التدليس.")

# ===== SLIDE 9: JENIS =====
s = new_slide(); title(s, "البحث فقهي مقارن، يستقرئ النوازل ويستنبط أحكامها")
bullets(s, [
 "جنس البحث: فقهي مقارن بين المذاهب الأربعة",
 "نوعه: استقراء النوازل ثم استنباط الحكم من النصوص والقواعد",
])
footnote(s, "ص٨٨"); notes(s, "Jenis & macam (hal 88, Bab3 Far'1).")

# ===== SLIDE 10: PENGUMPULAN =====
s = new_slide(); title(s, "تتبّع أقوال المذاهب وجمع النوازل ثم الترتيب والمقارنة")
bullets(s, [
 "تتبّع أقوال المذاهب في كتب الفقه المعتمدة",
 "جمع النوازل والدراسات المعاصرة",
 "ترتيب المعلومات ومقارنتها",
])
footnote(s, "ص٨٩"); notes(s, "Pengumpulan data (hal 89, Far'2).")

# ===== SLIDE 11: PENGOLAHAN+VERIFIKASI =====
s = new_slide(); title(s, "المقارنة والاستدلال ثم التطبيق، مع التحقق بعرض المعلومة على عدة مصادر")
bullets(s, [
 "مقارنة أقوال الفقهاء وذكر أدلتهم",
 "تطبيق النصوص المعتمدة على النوازل المعاصرة",
 "التحقق بعرض المعلومة على عدة مصادر حتى يتفق المعنى",
])
footnote(s, "ص٨٩"); notes(s, "Pengolahan + verifikasi (hal 89, Far'3+4).")

# ===== SLIDE 12: PENUTUP =====
s = new_slide(); title(s, "الحمد لله؛ البحث جهد بشري يقبل الخطأ، وسُئل الله القبول والنفع")
bullets(s, [
 "الحمد لله على إتمام البحث",
 "البحث جهد بشري يقبل الخطأ والصواب",
 "سؤال الله القبول والنفع به",
])
footnote(s, "ص١٥١"); notes(s, "خاتمة (hal 151) = doa penutup; ringkasan temuan substantif ada di S2.")

# ===== SLIDE 13: REKOMENDASI =====
s = new_slide(); title(s, "ثلاث وصايا: للعلماء بالبحث الدقيق، للمرأة بالحذر، للمجامع بمتابعة الجديد")
bullets(s, [
 "للعلماء وطلاب العلم: دقة البحث وإظهار أحكام النوازل للمجتمع",
 "للمرأة المسلمة: الحذر من الزينة المحرمة والاكتفاء بالحلال عن علم",
 "للمجامع الفقهية: متابعة المستجدات في زينة المرأة وبيان أحكامها",
])
footnote(s, "ص١٥٢"); notes(s, "توصيات (hal 152): 3 poin.")

OUT = "sistem-presentasi/deck-aktif/presentasi-tesis-fikih-hiasan-wanita/keluaran/presentasi-tesis-fikih-hiasan-wanita.pptx"
prs.save(OUT)
print("saved", OUT, "slides:", len(prs.slides._sldIdLst))
