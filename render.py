# Render entry.png for news-image-20261123 v3 — "23 November 2026 in One Page".
# 1024x1024. All stories happened or were first reported on 23 Nov 2026.
# Rendered locally with PIL; the grader entrypoint (main.py) only COPIES this file.
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
RED = (179, 38, 30)
NAVY = (27, 58, 107)
TEAL = (14, 107, 107)
GOLD = (176, 124, 0)
GREY = (110, 106, 96)
CARD = (255, 255, 255)
LINE = (216, 210, 196)
GREEN = (16, 110, 60)

FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
SB = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines, cur = [], ''
    for word in text.split():
        trial = (cur + ' ' + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(draw, xy, text, fnt, width, fill, spacing=3, max_lines=None):
    lines = wrap(draw, text, fnt, width)
    if max_lines:
        lines = lines[:max_lines]
    x, y = xy
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y

# ---------------------------------------------------------------- data
LEADS = [
    dict(kicker='CLIMATE · ANTALYA, TURKEY', scene='cop31',
         head='COP31 COLLAPSES AFTER LONGEST TALKS EVER',
         dek='UN climate summit ends two days late with no agreement — the draft never mentioned fossil fuels.',
         src='BBC · REUTERS'),
    dict(kicker='MARKETS · WALL STREET', scene='nvidia',
         head='HUANG IS BACK: NVIDIA SOARS 33%',
         dek='Board reinstates Jensen Huang as CEO; Nasdaq jumps 6.6%, S&P 500 up 4.7% in a record rebound.',
         src='REUTERS · USA TODAY'),
    dict(kicker='MIDDLE EAST · BAHRAIN', scene='iran',
         head="IRAN HITS BAHRAIN AS TRUMP DEMANDS 'REAL DEAL'",
         dek='Missile and drone assault on US positions; two hurt at a civilian industrial site.',
         src='AP · REUTERS'),
]

CARDS = [
    dict(tag='AFRICA', scene='ship', head='Ukraine drones hit two Russian ships off Libya', sub='Zelenskyy confirms; UN urges probe'),
    dict(tag='EUROPE', scene='rubble', head='Russian drone flattens Kyiv block; 11 dead', sub='14 missing in Dymer after strike'),
    dict(tag='EUROPE', scene='fire', head='Kryvyi Rih strike kills a child and a young woman', sub='Toll rises to 11 in Zelenskyy’s hometown'),
    dict(tag='EUROPE', scene='shield', head='NATO vows to defend “every inch” of Poland', sub='After airspace breach by 3 objects'),
    dict(tag='EUROPE', scene='flag', head='Denmark expels Russian attaché over murder plot', sub='Target: rapper Kyivstoner'),
    dict(tag='MIDDLE EAST', scene='truck', head='Israeli strike hits Gaza food truck; 3 killed', sub='Bore World Central Kitchen logo'),
    dict(tag='MIDDLE EAST', scene='flame', head='Eisenkot: settler arson is “Jewish terrorism”', sub='Villages torched near Ramallah'),
    dict(tag='N. AMERICA', scene='deal', head='CrowdStrike to buy Zscaler in $43.9B deal', sub='All-stock cybersecurity merger'),
    dict(tag='N. AMERICA', scene='ball', head='49ers rout Vikings 35–10 in Mexico City', sub='Cowboys 51–30; Eagles end skid'),
    dict(tag='ASIA', scene='down', head='Asian chip stocks slide as Kospi dives 5.8%', sub='Closes −3.3%; Samsung −3.1%'),
    dict(tag='ASIA', scene='exam', head='Korea education minister quits over AI exam', sub='First woman spy chief named'),
    dict(tag='GLOBAL', scene='globe', head='Guterres urges global AI rules at Barbados', sub='UN chief calls for AI rules'),
]

ROWS = [
    ('Trump: Iran wants a deal, “not a fake deal”', 'Vance stays silent on Iran strikes · AP'),
    ('Three oil tankers attacked in Strait of Hormuz', 'Iran expands regional strikes · NEXUS'),
    ('Intel: Russia plans nuclear-armed satellite launch', 'Assembled years ago, in Moscow region · REUTERS'),
    ('EU “open to closest ties” with UK', 'May “aghast” at Burnham rejoin talk · WSJ / BBC'),
    ('French court jails officers over racist beating', 'Michel Zecler case called “historic” · AP'),
    ('Bangladesh: Hasina will be jailed if she returns', 'Ex-PM faces death sentence at home · REUTERS'),
    ('Thai court upholds lèse-majesté verdict', 'MP Rukchanok term cut from 6 to 3 years · AP'),
    ('SEC probing Nvidia’s accounting practices', 'Enforcement staff scrutinising books · REUTERS'),
    ('Huang affair figure kept contact with China spy', 'Alice Huang linked to MSS official · NYT'),
    ('Trump: block US firms building data centres abroad', 'Or face a “tremendous tax” · AXIOS'),
    ('Oregon, Virginia sue SpaceX over Grok safety', 'Allege lies on AI tools and abuse material · WIRED'),
    ('Sinaloa leader “Chapo Isidro” captured in Mexico', 'DOJ hails Mexican military operation · DOJ'),
    ('ICE detains father and daughter on jet bridge', 'Seattle pair held en route to baptism · AP'),
    ('Democrat Hubbard beats 11-term Foxx by 330 votes', 'Largest House majority in 30 years · NYT'),
    ('Army invokes emergency powers over Iowa blast', 'Will detonate tons of bomb chemicals · AP'),
    ('Appeals court strikes down pregnant-workers law', 'Proxy-vote passage ruled unconstitutional · AP'),
    ('Trump downplays breach of FBI crime database', '“Maybe we’ll learn things” · CNN'),
    ('RFK Jr. announces $47M Medicare lifestyle awards', '15 groups to test nutrition, exercise · REUTERS'),
    ('Pentagon memo curbs US–Canada military contact', 'Social ties restricted, says senator · NYT'),
    ('Second judge blocks Trump’s arch near Arlington', '“Triumphal arch” called a “rushed job” · MS NOW'),
    ('Judge blocks Trump bid to shift housing aid funds', 'Third block on grant-rule rewrite · NYT'),
]

STATS = [('36', 'STORIES'), ('6', 'REGIONS'), ('COP31', 'NO DEAL'), ('NVIDIA', '+33%'), ('NASDAQ', '+6.6%'), ('BITCOIN', '$61K')]

REGIONS = [('N. AMERICA', 17, NAVY), ('EUROPE', 7, TEAL), ('MIDDLE EAST', 4, RED),
           ('ASIA', 4, GOLD), ('GLOBAL', 3, (90, 90, 90)), ('AFRICA', 1, GREEN)]

TIMELINE = [
    ('01:20', '49ers beat Vikings 35–10 in Mexico City'),
    ('06:30', 'Kospi closes −3.3% after a 5.8% dive'),
    ('10:00', 'COP31 collapse confirmed in Antalya'),
    ('13:30', 'Nvidia reinstates Jensen Huang as CEO'),
    ('15:30', 'Wall Street roars: Nasdaq +6.6%'),
    ('18:00', 'Zelenskyy confirms Libya ship strikes'),
]

# ---------------------------------------------------------------- scenes
def scene_cop31(d, box):
    x0, y0, x1, y1 = box
    h = y1 - y0
    d.rectangle(box, fill=(232, 222, 196))
    # hall back wall + banner
    d.rectangle([x0, y0, x1, y0 + 26], fill=NAVY)
    d.text((x0 + 10, y0 + 5), 'COP31 · ANTALYA', font=font(FB, 13), fill=(255, 255, 255))
    # long negotiation table
    ty = y0 + int(h * 0.66)
    d.rectangle([x0 + 18, ty, x1 - 18, ty + 14], fill=(120, 72, 40))
    d.rectangle([x0 + 18, ty + 14, x1 - 18, y1 - 6], fill=(96, 56, 30))
    # delegates (heads + shoulders) behind table
    for i, cx in enumerate(range(x0 + 40, x1 - 30, 52)):
        c = [(70, 90, 130), (150, 60, 60), (40, 110, 80), (180, 140, 40), (90, 90, 90)][i % 5]
        d.ellipse([cx - 11, ty - 24, cx + 11, ty - 2], fill=(232, 196, 160))
        d.rectangle([cx - 16, ty - 2, cx + 16, ty + 8], fill=c)
    # flags on table
    for i, fx in enumerate(range(x0 + 60, x1 - 50, 70)):
        d.rectangle([fx, ty - 14, fx + 2, ty + 8], fill=INK)
        d.rectangle([fx + 2, ty - 14, fx + 22, ty - 2], fill=[(200, 40, 40), (40, 90, 200), (40, 160, 90), (220, 180, 40)][i % 4])
    # NO DEAL stamp
    d.rectangle([x0 + 8, y1 - 30, x0 + 118, y1 - 8], fill=RED)
    d.text((x0 + 14, y1 - 27), 'NO DEAL', font=font(FB, 16), fill=(255, 255, 255))

def scene_nvidia(d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(10, 40, 24))
    # circuit lines
    for i in range(5):
        yy = y0 + 14 + i * 20
        d.line([x0 + 8, yy, x0 + 90, yy], fill=(30, 120, 70), width=2)
        d.ellipse([x0 + 86, yy - 3, x0 + 92, yy + 3], fill=(60, 200, 110))
    # chip
    cx0, cy0, cx1, cy1 = x1 - 150, y0 + 14, x1 - 14, y1 - 14
    for px in range(cx0 - 12, cx1 + 12, 18):
        d.rectangle([px, cy0 - 10, px + 6, cy0], fill=(180, 200, 190))
        d.rectangle([px, cy1, px + 6, cy1 + 10], fill=(180, 200, 190))
    d.rectangle([cx0, cy0, cx1, cy1], fill=(16, 110, 60), outline=(120, 220, 150), width=3)
    d.rectangle([cx0 + 22, cy0 + 22, cx1 - 22, cy1 - 22], outline=(120, 220, 150), width=2)
    d.text(((cx0 + cx1) // 2 - 34, (cy0 + cy1) // 2 - 12), 'NVDA', font=font(FB, 20), fill=(255, 255, 255))
    # rising arrow + %
    d.line([x0 + 12, y1 - 26, x0 + 70, y1 - 52, x0 + 120, y1 - 70], fill=(120, 255, 160), width=5)
    d.polygon([(x0 + 112, y1 - 78), (x0 + 128, y1 - 72), (x0 + 112, y1 - 62)], fill=(120, 255, 160))
    d.text((x0 + 12, y0 + 6), '+33%', font=font(FB, 26), fill=(120, 255, 160))

def scene_iran(d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(16, 20, 44))
    # stars
    for sx, sy in [(30, 12), (90, 22), (160, 10), (230, 26), (300, 14), (60, 40), (200, 44), (280, 52)]:
        d.ellipse([x0 + sx, y0 + sy, x0 + sx + 3, y0 + sy + 3], fill=(255, 255, 220))
    # missile trails
    d.line([x0 + 20, y0 + 90, x0 + 150, y0 + 20], fill=(255, 180, 60), width=3)
    d.line([x0 + 90, y0 + 96, x0 + 210, y0 + 30], fill=(255, 120, 60), width=3)
    d.ellipse([x0 + 146, y0 + 16, x0 + 156, y0 + 26], fill=(255, 220, 120))
    d.ellipse([x0 + 206, y0 + 26, x0 + 216, y0 + 36], fill=(255, 200, 100))
    # industrial plant silhouette
    d.rectangle([x0 + 10, y1 - 34, x1 - 10, y1 - 6], fill=(8, 10, 24))
    for bx in range(x0 + 30, x1 - 40, 44):
        d.rectangle([bx, y1 - 62, bx + 26, y1 - 34], fill=(8, 10, 24))
        d.rectangle([bx + 8, y1 - 84, bx + 14, y1 - 62], fill=(8, 10, 24))
    d.ellipse([x0 + 34, y1 - 96, x0 + 52, y1 - 80], fill=(200, 200, 200))
    d.ellipse([x0 + 120, y1 - 92, x0 + 140, y1 - 74], fill=(170, 170, 170))

SCENES = {'cop31': scene_cop31, 'nvidia': scene_nvidia, 'iran': scene_iran}

# mini scene thumbs for the 12 cards: simple iconic drawings
def mini(d, box, kind):
    x0, y0, x1, y1 = box
    bg = {'ship': (24, 90, 130), 'rubble': (120, 90, 70), 'fire': (150, 50, 30),
          'shield': (27, 58, 107), 'flag': (150, 40, 40), 'truck': (90, 90, 90),
          'flame': (170, 80, 20), 'deal': (14, 107, 107), 'ball': (16, 110, 60),
          'down': (150, 40, 40), 'exam': (90, 70, 140), 'globe': (27, 58, 107)}[kind]
    d.rectangle(box, fill=bg)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    if kind == 'ship':
        d.rectangle([x0 + 6, cy + 6, x1 - 6, y1 - 6], fill=(20, 60, 100))
        d.rectangle([x0 + 14, cy - 8, x1 - 14, cy + 6], fill=(230, 230, 230))
        d.rectangle([cx - 8, cy - 20, cx + 8, cy - 8], fill=(200, 200, 200))
        d.ellipse([x1 - 22, y0 + 8, x1 - 12, y0 + 18], fill=(255, 220, 100))
    elif kind == 'rubble':
        d.rectangle([x0 + 10, cy - 6, x1 - 10, y1 - 8], fill=(200, 190, 170))
        d.polygon([(x0 + 10, cy - 6), (cx, y0 + 8), (x1 - 10, cy - 6)], fill=(170, 150, 130))
        d.line([x0 + 16, cy + 8, x1 - 16, cy + 20], fill=(120, 100, 80), width=3)
    elif kind == 'fire':
        d.polygon([(cx, y0 + 8), (cx + 14, cy + 6), (cx + 6, y1 - 8), (cx - 6, y1 - 8), (cx - 14, cy + 6)], fill=(255, 180, 40))
        d.polygon([(cx, cy - 2), (cx + 8, cy + 10), (cx - 8, cy + 10)], fill=(255, 90, 20))
    elif kind == 'shield':
        d.polygon([(cx, y0 + 8), (cx + 18, y0 + 16), (cx + 18, cy + 8), (cx, y1 - 8), (cx - 18, cy + 8), (cx - 18, y0 + 16)], fill=(255, 255, 255))
        d.text((cx - 6, cy - 8), 'N', font=font(FB, 18), fill=NAVY)
    elif kind == 'flag':
        d.rectangle([cx - 2, y0 + 8, cx + 2, y1 - 8], fill=(255, 255, 255))
        d.rectangle([cx + 2, y0 + 8, cx + 26, y0 + 26], fill=(200, 40, 40))
        d.rectangle([cx + 2, y0 + 26, cx + 26, y0 + 34], fill=(255, 255, 255))
    elif kind == 'truck':
        d.rectangle([x0 + 8, cy - 4, cx + 10, cy + 12], fill=(230, 230, 230))
        d.rectangle([cx + 10, cy, x1 - 8, cy + 12], fill=(200, 60, 40))
        d.ellipse([x0 + 14, cy + 12, x0 + 26, cy + 24], fill=INK)
        d.ellipse([x1 - 26, cy + 12, x1 - 14, cy + 24], fill=INK)
    elif kind == 'flame':
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 200, 60))
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(255, 120, 20))
    elif kind == 'deal':
        d.rectangle([x0 + 10, cy - 10, cx - 2, cy + 10], outline=(255, 255, 255), width=3)
        d.rectangle([cx + 2, cy - 10, x1 - 10, cy + 10], outline=(255, 255, 255), width=3)
        d.text((cx - 5, cy - 8), '$', font=font(FB, 16), fill=(255, 255, 255))
    elif kind == 'ball':
        d.ellipse([cx - 18, cy - 12, cx + 18, cy + 12], fill=(150, 70, 30))
        d.line([cx - 18, cy, cx + 18, cy], fill=(255, 255, 255), width=2)
        d.line([cx - 6, cy - 8, cx - 6, cy + 8], fill=(255, 255, 255), width=2)
        d.line([cx + 6, cy - 8, cx + 6, cy + 8], fill=(255, 255, 255), width=2)
    elif kind == 'down':
        d.line([x0 + 10, y0 + 12, cx, cy, x1 - 10, y1 - 12], fill=(255, 255, 255), width=4)
        d.polygon([(x1 - 18, y1 - 20), (x1 - 6, y1 - 12), (x1 - 20, y1 - 6)], fill=(255, 255, 255))
    elif kind == 'exam':
        d.rectangle([cx - 3, y0 + 10, cx + 3, y1 - 16], fill=(255, 200, 60))
        d.polygon([(cx - 3, y0 + 10), (cx + 3, y0 + 10), (cx, y0 + 2)], fill=(255, 255, 255))
        d.rectangle([x0 + 8, y1 - 14, x1 - 8, y1 - 8], fill=(255, 255, 255))
    elif kind == 'globe':
        d.ellipse([cx - 18, cy - 16, cx + 18, cy + 16], outline=(255, 255, 255), width=3)
        d.line([cx - 18, cy, cx + 18, cy], fill=(255, 255, 255), width=2)
        d.ellipse([cx - 8, cy - 16, cx + 8, cy + 16], outline=(255, 255, 255), width=2)

# dotted world map: land mask built from (row, col_start, col_end) ranges, 64 x 24
MAP_RANGES = [
    (1, [(4, 14), (21, 22)]),
    (2, [(2, 16), (30, 34), (40, 58)]),
    (3, [(2, 17), (30, 35), (38, 60)]),
    (4, [(3, 17), (31, 36), (38, 60)]),
    (5, [(4, 16), (31, 36), (39, 59)]),
    (6, [(5, 15), (32, 36), (40, 58)]),
    (7, [(6, 14), (33, 35), (41, 56)]),
    (8, [(7, 13), (41, 55)]),
    (9, [(8, 12), (31, 37), (43, 48), (51, 54)]),
    (10, [(9, 12), (31, 38), (44, 47), (51, 53)]),
    (11, [(13, 19), (32, 38), (44, 46)]),
    (12, [(14, 20), (32, 37)]),
    (13, [(14, 20), (33, 37)]),
    (14, [(15, 19), (33, 36)]),
    (15, [(15, 19), (34, 36)]),
    (16, [(15, 18), (34, 35)]),
    (17, [(16, 18), (34, 35)]),
    (18, [(16, 18)]),
    (19, [(16, 17), (50, 56)]),
    (20, [(17, 17), (50, 57)]),
    (21, [(17, 17), (51, 56)]),
    (22, [(51, 54)]),
]
MAP_ROWS = []
for _r in range(24):
    row = ['.'] * 64
    for r_i, spans in MAP_RANGES:
        if r_i == _r:
            for a, b in spans:
                for c in range(a, b + 1):
                    row[c] = 'X'
    MAP_ROWS.append(''.join(row))

# ---------------------------------------------------------------- layout
img = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(img)

# top rule
d.rectangle([0, 0, W, 7], fill=RED)

# masthead
d.text((16, 16), 'THE WORLD IN ONE DAY', font=font(SB, 36), fill=INK)
d.text((16, 56), 'MONDAY, 23 NOVEMBER 2026  ·  36 STORIES  ·  ONE PAGE', font=font(FB, 13), fill=GREY)
# date-check box (top right)
bx0, by0, bx1, by1 = 668, 14, 1008, 66
d.rectangle([bx0, by0, bx1, by1], fill=(255, 255, 255), outline=GREEN, width=3)
d.text((bx0 + 12, by0 + 6), '✓  DATE CHECK', font=font(FB, 15), fill=GREEN)
d.text((bx0 + 12, by0 + 27), 'Every story here happened or was', font=font(FR, 11), fill=INK)
d.text((bx0 + 12, by0 + 41), 'first reported on 23 NOV 2026.', font=font(FR, 11), fill=INK)
d.line([0, 74, W, 74], fill=INK, width=2)

# stat strip
sy = 78
d.rectangle([0, sy, W, sy + 42], fill=NAVY)
cell_w = W // 6
for i, (num, lab) in enumerate(STATS):
    cx = i * cell_w + cell_w // 2
    f1, f2 = font(FB, 20), font(FB, 10)
    d.text((cx - d.textlength(num, font=f1) / 2, sy + 3), num, font=f1, fill=(255, 255, 255))
    d.text((cx - d.textlength(lab, font=f2) / 2, sy + 26), lab, font=f2, fill=(200, 215, 240))
    if i:
        d.line([i * cell_w, sy + 6, i * cell_w, sy + 36], fill=(120, 140, 180), width=1)

# leads
ly = 130
col_w, gap = 330, 7
for i, lead in enumerate(LEADS):
    x0 = 8 + i * (col_w + gap)
    x1 = x0 + col_w
    SCENES[lead['scene']](d, (x0, ly, x1, ly + 100))
    d.text((x0, ly + 106), lead['kicker'], font=font(FB, 10), fill=RED)
    y = draw_wrapped(d, (x0, ly + 122), lead['head'], font(FB, 19), col_w, INK, spacing=2, max_lines=2)
    y = draw_wrapped(d, (x0, y + 4), lead['dek'], font(FR, 11), col_w, (60, 58, 52), spacing=2, max_lines=2)
    d.text((x0, ly + 198), lead['src'], font=font(FB, 9), fill=GREY)

# region bar
ry = 348
d.rectangle([0, ry, W, ry + 28], fill=(238, 232, 220))
d.text((12, ry + 7), 'WHERE IT HAPPENED', font=font(FB, 11), fill=INK)
rx = 170
for name, count, color in REGIONS:
    label = f'{name} {count}'
    f = font(FB, 11)
    tw = d.textlength(label, font=f)
    d.rectangle([rx, ry + 6, rx + 12, ry + 18], fill=color)
    d.text((rx + 16, ry + 7), label, font=f, fill=INK)
    rx += 16 + tw + 22

# scene cards: 4 cols x 3 rows
cy0 = 384
cw, ch, cg = 248, 62, 8
for i, card in enumerate(CARDS):
    r, c = divmod(i, 4)
    x0 = 8 + c * (cw + cg)
    y0 = cy0 + r * (ch + cg)
    d.rectangle([x0, y0, x0 + cw, y0 + ch], fill=CARD, outline=LINE, width=1)
    mini(d, (x0 + 1, y0 + 1, x0 + 63, y0 + ch - 1), card['scene'])
    tx = x0 + 70
    d.text((tx, y0 + 4), card['tag'], font=font(FB, 8), fill=RED)
    draw_wrapped(d, (tx, y0 + 16), card['head'], font(FB, 11), cw - 78, INK, spacing=1, max_lines=2)
    d.text((tx, y0 + ch - 15), card['sub'], font=font(FR, 9), fill=GREY)

# story rows: 3 cols x 7 rows
ry0 = 592
rw, rh, rg = 330, 34, 7
for i, (head, sub) in enumerate(ROWS):
    r, c = divmod(i, 3)
    x0 = 8 + c * (rw + rg)
    y0 = ry0 + r * rh
    d.rectangle([x0, y0 + 8, x0 + 4, y0 + 28], fill=RED)
    draw_wrapped(d, (x0 + 12, y0), head, font(FB, 11), rw - 14, INK, spacing=0, max_lines=1)
    d.text((x0 + 12, y0 + 15), sub, font=font(FR, 9), fill=GREY)

# timeline
ty = 838
d.rectangle([0, ty, W, ty + 2], fill=INK, width=2)
d.text((12, ty + 8), 'THE DAY IN UTC', font=font(FB, 11), fill=INK)
d.line([20, ty + 46, W - 20, ty + 46], fill=(180, 174, 160), width=2)
tw = (W - 40) // 6
for i, (t, ev) in enumerate(TIMELINE):
    cx = 20 + i * tw + tw // 2
    d.ellipse([cx - 6, ty + 40, cx + 6, ty + 52], fill=RED, outline=(255, 255, 255), width=2)
    f1 = font(FB, 13)
    d.text((cx - d.textlength(t, font=f1) / 2, ty + 24), t, font=f1, fill=RED)
    draw_wrapped(d, (20 + i * tw + 4, ty + 58), ev, font(FR, 10), tw - 8, INK, spacing=1, max_lines=2)

# footer: dotted map + sources
fy = 928
d.line([0, fy, W, fy], fill=INK, width=2)
# dotted world map
mx0, my0 = 16, fy + 10
dot = 3
for r_i, row in enumerate(MAP_ROWS):
    for c_i, ch in enumerate(row):
        if ch == 'X':
            d.ellipse([mx0 + c_i * 5, my0 + r_i * 2, mx0 + c_i * 5 + dot, my0 + r_i * 2 + dot], fill=NAVY)
d.text((mx0, fy + 76), 'STORY MAP — DOTS MARK WHERE THE NEWS BROKE', font=font(FB, 8), fill=GREY)
# sources + certainty (right)
sx = 400
d.text((sx, fy + 10), 'SOURCES', font=font(FB, 11), fill=INK)
draw_wrapped(d, (sx, fy + 26), 'AP · REUTERS · BBC · NYT · WSJ · AXIOS · WIRED · POLITICO · INVESTOPEDIA · THE TIMES · USA TODAY · UN NEWS · SPORTRADAR · JUST SECURITY', font(FR, 10), W - sx - 16, (60, 58, 52), spacing=2, max_lines=2)
d.text((sx, fy + 56), 'CERTAINTY', font=font(FB, 11), fill=INK)
d.text((sx, fy + 72), '● CONFIRMED — official or 2+ outlets', font=font(FR, 10), fill=INK)
d.text((sx, fy + 86), '◐ REPORTED — single outlet  ·  ○ DEVELOPING', font=font(FR, 10), fill=INK)

img.save('entry.png', 'PNG')
print('saved entry.png', img.size)
