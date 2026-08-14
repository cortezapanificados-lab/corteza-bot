from PIL import Image, ImageDraw, ImageFont
import random, os

F = "/tmp/claude-0/-home-user-corteza-bot/1de54431-12fe-52b7-96c7-204646ce999d/scratchpad/fonts/"
PF_R, PF_B = F + "playfair-regular.ttf", F + "playfair-bold.ttf"
JO_L, JO_M = F + "jost-light.ttf", F + "jost-medium.ttf"

W, H = 1080, 1920
CREAM = (246, 242, 234)
INK = (26, 26, 26)
SOFT = (120, 112, 100)
OCHRE = (176, 124, 46)


def grain(img, amount=7):
    px = img.load()
    rnd = random.Random(7)
    for y in range(0, H, 2):
        for x in range(0, W, 2):
            n = rnd.randint(-amount, amount)
            r, g, b = px[x, y]
            px[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)))
    return img


def track_width(d, text, font, tracking):
    w = 0
    for ch in text:
        w += d.textlength(ch, font=font) + tracking
    return w - tracking if text else 0


def draw_tracked(d, cx, y, text, font, tracking, fill):
    x = cx - track_width(d, text, font, tracking) / 2
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking


def centered(d, cx, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=fill)


def wheat(d, cx, cy, scale=1.0, fill=INK):
    """Espiga simple, dibujada a mano con elipses."""
    s = scale
    d.line([(cx, cy + 46 * s), (cx, cy - 40 * s)], fill=fill, width=max(1, int(3 * s)))
    for i, yy in enumerate([-34, -16, 2, 20]):
        ry = cy + yy * s
        for sign in (-1, 1):
            xa, xb = cx + sign * 4 * s, cx + sign * 26 * s
            d.ellipse(
                [min(xa, xb), ry - 13 * s, max(xa, xb), ry + 11 * s],
                outline=fill, width=max(1, int(2.5 * s)),
            )
    d.ellipse([cx - 8 * s, cy - 56 * s, cx + 8 * s, cy - 34 * s], outline=fill, width=max(1, int(2.5 * s)))


def base():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # marco finito
    d.rectangle([44, 44, W - 45, H - 45], outline=(222, 214, 200), width=2)
    return img, d


def header(d):
    draw_tracked(d, W // 2, 118, "CORTEZA", ImageFont.truetype(PF_R, 52), 16, INK)
    d.line([(W // 2 - 70, 205), (W // 2 + 70, 205)], fill=(200, 190, 174), width=2)


def footer(d, cta="ACTIVÁ TU RECORDATORIO", sub="link en la bio"):
    draw_tracked(d, W // 2, 1618, cta, ImageFont.truetype(JO_M, 40), 7, INK)
    centered(d, W // 2, 1682, sub, ImageFont.truetype(PF_R, 40), SOFT)
    # flechita
    cx, y = W // 2, 1772
    d.line([(cx, y), (cx, y + 44)], fill=OCHRE, width=3)
    d.line([(cx - 15, y + 28), (cx, y + 46)], fill=OCHRE, width=3)
    d.line([(cx + 15, y + 28), (cx, y + 46)], fill=OCHRE, width=3)


# ---------------- STORY A ----------------
img, d = base()
header(d)

draw_tracked(d, W // 2, 330, "JUEVES 17 DE SEPTIEMBRE", ImageFont.truetype(JO_M, 33), 9, OCHRE)

f_big = ImageFont.truetype(PF_B, 148)
for i, line in enumerate(["ABRIMOS", "EN TODO", "EL AMBA"]):
    centered(d, W // 2, 425 + i * 168, line, f_big, INK)

d.line([(W // 2 - 150, 960), (W // 2 + 150, 960)], fill=(200, 190, 174), width=2)

f_sub = ImageFont.truetype(JO_L, 40)
for i, line in enumerate(["Pan de masa madre y", "harinas 100% agroecológicas"]):
    centered(d, W // 2, 1010 + i * 56, line, f_sub, SOFT)

footer(d)
grain(img).save("story-amba.png")

# ---------------- STORY B ----------------
img, d = base()
header(d)

f_q = ImageFont.truetype(PF_B, 160)
centered(d, W // 2, 360, "¿SOS DE", f_q, INK)
centered(d, W // 2, 540, "CABA?", f_q, INK)

d.line([(W // 2 - 150, 790), (W // 2 + 150, 790)], fill=(200, 190, 174), width=2)

f_sub = ImageFont.truetype(JO_L, 42)
for i, line in enumerate(["En septiembre te llevamos", "el pan a tu casa."]):
    centered(d, W // 2, 845 + i * 58, line, f_sub, SOFT)

draw_tracked(d, W // 2, 1000, "JUEVES 17 DE SEPTIEMBRE", ImageFont.truetype(JO_M, 33), 9, OCHRE)
footer(d)
grain(img).save("story-caba.png")

print("ok", os.getcwd())
