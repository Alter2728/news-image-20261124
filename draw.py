#!/usr/bin/env python3
"""Render the front page for Tuesday 24 November 2026 as a 1024x1024 PNG.

One lead story plus five smaller stories, all drawn with flat vector-style
shapes (no photos, no downloaded art). Deterministic: fixed layout, fixed
fonts, no timestamps, no randomness.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
PAPER = (247, 243, 232)
INK = (24, 24, 28)
RED = (178, 34, 28)
NAVY = (28, 52, 92)
TEAL = (18, 110, 105)
GOLD = (198, 142, 28)
GREY = (92, 88, 80)
RULE = (150, 142, 124)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF = lambda s: font("DejaVuSerif.ttf", s)
SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, fill=INK):
    """Draw wrapped paragraph, return y below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def hrule(draw, x0, x1, y, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- pictures
def pic_pills(draw, x, y, w, h):
    """Lead illustration: a medicine bottle, capsules and a $41bn coin stack."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 236, 240), outline=NAVY, width=3)
    draw.text((x + w - 14, y + 8), "$41bn", font=SERIF_B(30), fill=RED, anchor="ra")
    # coin stack on the right
    for i, yy in enumerate(range(y + h - 46, y + h - 46 - 4 * 16, -16)):
        draw.ellipse([x + w - 108, yy, x + w - 38, yy + 26], fill=GOLD,
                     outline=(140, 96, 10), width=2)
        draw.text((x + w - 86, yy + 3), "$", font=SANS_B(16), fill=(140, 96, 10))
    # bottle
    bx, by, bw, bh = x + 52, y + 62, 130, 114
    draw.rectangle([bx + 38, by - 26, bx + bw - 38, by + 6], fill=RED)          # cap
    draw.rectangle([bx, by, bx + bw, by + bh], fill=(255, 255, 255),
                   outline=NAVY, width=3)
    draw.rectangle([bx + 8, by + 46, bx + bw - 8, by + bh - 8], fill=(240, 244, 246),
                   outline=NAVY, width=1)
    draw.text((bx + 8, by + 66), "INSMED", font=SANS_B(22), fill=NAVY)
    # capsules
    draw.rounded_rectangle([x + 200, y + 60, x + 262, y + 88], radius=14,
                           fill=RED, outline=INK, width=2)
    draw.rounded_rectangle([x + 200, y + 60, x + 231, y + 88], radius=14,
                           fill=(255, 255, 255))
    draw.rounded_rectangle([x + 216, y + 100, x + 278, y + 128], radius=14,
                           fill=TEAL, outline=INK, width=2)
    draw.rounded_rectangle([x + 216, y + 100, x + 247, y + 128], radius=14,
                           fill=(255, 255, 255))


def pic_gaza(draw, x, y, w, h):
    """City skyline under smoke."""
    draw.rectangle([x, y, x + w, y + h], fill=(232, 214, 196), outline=INK, width=2)
    draw.rectangle([x, y, x + w, y + 34], fill=(214, 132, 84))
    draw.ellipse([x + w - 46, y + 6, x + w - 14, y + 38], fill=(255, 214, 120))
    # buildings
    for bx, bw, bh in [(x + 12, 52, 62), (x + 70, 44, 84), (x + 120, 58, 56),
                       (x + 184, 48, 76), (x + 238, 56, 66)]:
        draw.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(96, 84, 76),
                       outline=INK, width=1)
        for wy in range(y + h - bh + 8, y + h - 6, 14):
            draw.rectangle([bx + 8, wy, bx + 18, wy + 8], fill=(255, 214, 120))
    # cracked building + smoke
    draw.polygon([(x + 120, y + h - 56), (x + 148, y + h - 88), (x + 178, y + h - 56)],
                 fill=(70, 60, 54))
    for sx, sy, r in [(x + 150, y + 44, 12), (x + 168, y + 32, 16), (x + 190, y + 46, 11)]:
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(120, 116, 110))


def pic_ukraine(draw, x, y, w, h):
    """Damaged apartment block with a rescue cross."""
    draw.rectangle([x, y, x + w, y + h], fill=(214, 226, 238), outline=INK, width=2)
    draw.rectangle([x + 30, y + 18, x + 190, y + h - 8], fill=(178, 178, 168),
                   outline=INK, width=2)
    for row in range(3):
        for col in range(4):
            wx = x + 44 + col * 38
            wy = y + 28 + row * 26
            draw.rectangle([wx, wy, wx + 24, wy + 16], fill=(255, 214, 120),
                           outline=INK, width=1)
    # blast hole
    draw.polygon([(x + 100, y + 34), (x + 130, y + 52), (x + 118, y + 80),
                  (x + 88, y + 70)], fill=(40, 36, 32))
    draw.polygon([(x + 100, y + 34), (x + 130, y + 52), (x + 118, y + 80)],
                 fill=(226, 90, 40))
    # rubble
    for rx, rw in [(x + 30, 26), (x + 62, 18), (x + 88, 30), (x + 124, 20)]:
        draw.rectangle([rx, y + h - 22, rx + rw, y + h - 8], fill=(120, 112, 102))
    # medical cross badge
    draw.ellipse([x + w - 58, y + h - 58, x + w - 6, y + h - 6], fill=(255, 255, 255),
                 outline=RED, width=3)
    draw.rectangle([x + w - 40, y + h - 50, x + w - 24, y + h - 14], fill=RED)
    draw.rectangle([x + w - 49, y + h - 41, x + w - 15, y + h - 25], fill=RED)


def pic_climate(draw, x, y, w, h):
    """A globe warming under a hot sun, with a broken pact ribbon."""
    draw.rectangle([x, y, x + w, y + h], fill=(214, 232, 222), outline=INK, width=2)
    cx, cy, r = x + w // 2, y + h // 2 + 2, 38
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(64, 140, 190),
                 outline=NAVY, width=2)
    draw.ellipse([cx - 26, cy - 22, cx - 2, cy - 2], fill=(60, 160, 90))
    draw.ellipse([cx + 4, cy + 8, cx + 26, cy + 28], fill=(60, 160, 90))
    # sun
    sx, sy = x + w - 44, y + 26
    draw.ellipse([sx - 16, sy - 16, sx + 16, sy + 16], fill=(255, 190, 60),
                 outline=(200, 120, 20), width=2)
    for i in range(8):
        import math
        a = i * math.pi / 4
        draw.line([(sx + int(20 * math.cos(a)), sy + int(20 * math.sin(a))),
                   (sx + int(30 * math.cos(a)), sy + int(30 * math.sin(a)))],
                  fill=(200, 120, 20), width=3)
    # thermometer
    draw.rectangle([x + 18, y + 12, x + 34, y + 48], fill=(255, 255, 255),
                   outline=INK, width=2)
    draw.ellipse([x + 12, y + 44, x + 40, y + 68], fill=RED, outline=INK, width=2)
    draw.rectangle([x + 22, y + 24, x + 30, y + 48], fill=RED)
    # "NO DEAL" ribbon
    draw.rectangle([x + 8, y + h - 30, x + w - 8, y + h - 8], fill=RED)
    draw.text((x + w // 2, y + h - 28), "NO DEAL", font=SANS_B(15), fill=(255, 255, 255),
              anchor="ma")


def pic_ebola(draw, x, y, w, h):
    """Clinic tent, medical cross and a spiked virus."""
    draw.rectangle([x, y, x + w, y + h], fill=(226, 232, 214), outline=INK, width=2)
    # tent
    draw.polygon([(x + 20, y + h - 10), (x + 110, y + 26), (x + 200, y + h - 10)],
                 fill=(240, 240, 230), outline=INK, width=2)
    draw.polygon([(x + 96, y + h - 10), (x + 110, y + 52), (x + 124, y + h - 10)],
                 fill=(60, 60, 58))
    # cross on tent
    draw.rectangle([x + 102, y + 62, x + 118, y + 92], fill=RED)
    draw.rectangle([x + 90, y + 72, x + 130, y + 84], fill=RED)
    # virus
    vx, vy = x + w - 52, y + 34
    for i in range(10):
        import math
        a = i * math.pi / 5
        draw.line([(vx + int(14 * math.cos(a)), vy + int(14 * math.sin(a))),
                   (vx + int(24 * math.cos(a)), vy + int(24 * math.sin(a)))],
                  fill=TEAL, width=3)
        draw.ellipse([vx + int(24 * math.cos(a)) - 3, vy + int(24 * math.sin(a)) - 3,
                      vx + int(24 * math.cos(a)) + 3, vy + int(24 * math.sin(a)) + 3],
                     fill=TEAL)
    draw.ellipse([vx - 14, vy - 14, vx + 14, vy + 14], fill=TEAL, outline=NAVY, width=2)


def pic_quasar(draw, x, y, w, h):
    """Black hole with a glowing disc, ringed by stars."""
    draw.rectangle([x, y, x + w, y + h], fill=(18, 22, 44), outline=INK, width=2)
    # stars
    for sx, sy, r in [(x + 20, y + 18, 2), (x + 60, y + 44, 1), (x + 250, y + 22, 2),
                      (x + 280, y + 60, 1), (x + 40, y + 92, 1), (x + 268, y + 96, 2),
                      (x + 150, y + 14, 1), (x + 200, y + 100, 1)]:
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 255, 255))
    cx, cy = x + w // 2, y + h // 2
    # accretion disc
    draw.ellipse([cx - 92, cy - 26, cx + 92, cy + 26], fill=(255, 170, 60))
    draw.ellipse([cx - 70, cy - 16, cx + 70, cy + 16], fill=(255, 220, 130))
    # black hole
    draw.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], fill=(0, 0, 0),
                 outline=(255, 200, 90), width=3)
    # jets
    draw.polygon([(cx - 6, cy - 34), (cx + 6, cy - 34), (cx, cy - 58)], fill=(180, 220, 255))
    draw.polygon([(cx - 6, cy + 34), (cx + 6, cy + 34), (cx, cy + 58)], fill=(180, 220, 255))


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # margin

    # ---- masthead
    d.text((W // 2, 18), "THE DAILY GLOBE", font=SERIF_B(62), fill=INK, anchor="ma")
    hrule(d, M, W - M, 96, width=3)
    d.text((M, 106), "EST. 2026", font=SANS_B(15), fill=GREY)
    d.text((W // 2, 104), "TUESDAY 24 NOVEMBER 2026", font=SANS_B(30), fill=RED,
           anchor="ma")
    d.text((W - M, 106), "ONE DAY \u2022 ONE PAGE", font=SANS_B(15), fill=GREY, anchor="ra")
    hrule(d, M, W - M, 146, width=3)
    d.text((W // 2, 152), "SIX STORIES THAT DEFINED THE DAY \u2014 WORLD NEWS, TUESDAY 24 NOVEMBER 2026",
           font=SANS_B(14), fill=GREY, anchor="ma")

    # ---- lead story
    ly = 184
    d.text((M, ly), "BUSINESS  \u2022  LEAD STORY", font=SANS_B(16), fill=RED)
    head = ["Sanofi buys Insmed", "in a $41bn deal"]
    hy = ly + 26
    for line in head:
        d.text((M, hy), line, font=SERIF_B(46), fill=INK)
        hy += 54
    pic_pills(d, M, hy + 6, 400, 190)
    tx = M + 424
    ty = hy + 10
    ty = para(d, tx, ty,
              "France\u2019s Sanofi agreed on Tuesday to buy US drugmaker "
              "Insmed for $41bn in cash \u2014 $175 a share \u2014 the year\u2019s "
              "biggest pharma deal.",
              SANS(20), 548, 27)
    ty += 8
    ty = para(d, tx, ty,
              "The prize: two respiratory drugs, Brinsupri and Arikayce. "
              "The deal is expected to close in the first half of 2027.",
              SANS(20), 548, 27)
    hrule(d, M, W - M, 512, width=2)

    # ---- small stories, row 1: three cards
    cards1 = [
        ("GAZA", "Gaza strikes kill six, incl. Hamas security chief",
         "Israeli airstrikes killed at least six people in Gaza, medics "
         "said, including Naeem Abu Nahel, head of Hamas\u2019s internal "
         "security.",
         pic_gaza),
        ("UKRAINE", "Zaporizhzhia strike kills two, wounds 40",
         "An overnight Russian attack hit an apartment block in "
         "Zaporizhzhia, killing two and wounding 40, including four "
         "children.",
         pic_ukraine),
        ("CLIMATE", "COP31 ends without a deal",
         "Nearly 200 nations left the Antalya summit with no deal after "
         "the EU rejected a text that never named fossil fuels.",
         pic_climate),
    ]
    cw, gap = 312, 16
    cy = 524
    for i, (kick, head, body, pic) in enumerate(cards1):
        x = M + i * (cw + gap)
        pic(d, x, cy, cw, 100)
        yy = cy + 110
        d.text((x, yy), kick, font=SANS_B(14), fill=RED)
        yy += 20
        yy = para(d, x, yy, head, SERIF_B(20), cw, 24)
        yy += 4
        para(d, x, yy, body, SANS(14), cw, 18)

    # ---- small stories, row 2: two wide cards
    hrule(d, M, W - M, 772, width=1, fill=RULE)
    cards2 = [
        ("HEALTH \u2022 DR CONGO", "Fighting in Congo traps Ebola teams",
         "Heavy fighting near a hospital in Ituri province forced Ebola "
         "response teams to take cover for more than 24 hours, the WHO said.",
         pic_ebola),
        ("SPACE", "Euclid spots the most distant quasar yet",
         "ESA\u2019s Euclid telescope found quasar J1504+6252, nicknamed "
         "D\u00fan Aonghasa \u2014 a black hole of about 360 million suns, "
         "seen 630 million years after the Big Bang.",
         pic_quasar),
    ]
    cw2 = 480
    cy2 = 788
    for i, (kick, head, body, pic) in enumerate(cards2):
        x = M + i * (cw2 + gap)
        pic(d, x, cy2, 168, 168)
        tx = x + 182
        d.text((tx, cy2), kick, font=SANS_B(14), fill=RED)
        yy = para(d, tx, cy2 + 22, head, SERIF_B(22), cw2 - 182, 26)
        yy += 6
        para(d, tx, yy, body, SANS(15), cw2 - 182, 20)

    # ---- footer
    hrule(d, M, W - M, 972, width=2)
    d.text((W // 2, 982),
           "Sources: Sanofi \u2022 Reuters \u2022 ESA \u2022 WHO \u2022 UN News  \u2014  "
           "All six stories from Tuesday 24 November 2026",
           font=SANS(14), fill=GREY, anchor="ma")

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
