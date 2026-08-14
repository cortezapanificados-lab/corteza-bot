"""
Corteza — genera la placa de historia para la captura de lista (1080x1920).

Uso:  python3 generar-placas.py
Sale: story-amba.png

Para hacer versiones por zona (anuncios de Nordelta, San Isidro, etc.),
cambiá HEADLINE por ejemplo a ["ABRIMOS", "EN", "NORDELTA"].

Fuentes: Playfair Display y Jost (los .ttf están en esta misma carpeta).
Logo: logo-corteza.png, bajado de la tienda.
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PF_B = os.path.join(HERE, "playfair-bold.ttf")
JO_L = os.path.join(HERE, "jost-light.ttf")
JO_M = os.path.join(HERE, "jost-medium.ttf")
LOGO = os.path.join(HERE, "logo-corteza.png")

W, H = 1080, 1920
CREAM = (246, 242, 234)
INK = (26, 26, 26)
SOFT = (120, 112, 100)
OCHRE = (176, 124, 46)
RULE = (200, 190, 174)

EYEBROW = "JUEVES 17 DE SEPTIEMBRE"
HEADLINE = ["ABRIMOS", "EN TODO", "EL AMBA"]
SUBTITLE = ["Pan de masa madre y", "harinas 100% agroecológicas"]
CTA = "ACTIVÁ TU RECORDATORIO"
CTA_SUB = "link en la bio"


def logo_tintado(ancho_objetivo):
    """Aísla las letras del logo, las vuelve transparentes alrededor y las tiñe de INK."""
    src = Image.open(LOGO).convert("RGBA")
    alpha = src.getchannel("A")
    if alpha.getextrema()[0] == 255:
        # el PNG no trae transparencia: es negro sobre blanco, así que la
        # máscara sale de la luminancia (negro = opaco, blanco = transparente)
        alpha = ImageOps.invert(ImageOps.grayscale(src.convert("RGB")))
    logo = Image.new("RGBA", src.size, INK + (0,))
    logo.putalpha(alpha)
    logo = logo.crop(alpha.getbbox())
    w, h = logo.size
    return logo.resize((ancho_objetivo, round(h * ancho_objetivo / w)), Image.LANCZOS)


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
    return sum(d.textlength(c, font=font) + tracking for c in text) - tracking if text else 0


def draw_tracked(d, cx, y, text, font, tracking, fill):
    x = cx - track_width(d, text, font, tracking) / 2
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + tracking


def centered(d, cx, y, text, font, fill):
    d.text((cx - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill)


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)
d.rectangle([44, 44, W - 45, H - 45], outline=(222, 214, 200), width=2)

# Logo real, centrado arriba
logo = logo_tintado(560)
img.paste(logo, ((W - logo.width) // 2, 130), logo)
d.line([(W // 2 - 70, 130 + logo.height + 56), (W // 2 + 70, 130 + logo.height + 56)], fill=RULE, width=2)

draw_tracked(d, W // 2, 372, EYEBROW, ImageFont.truetype(JO_M, 33), 9, OCHRE)

f_big = ImageFont.truetype(PF_B, 148)
for i, line in enumerate(HEADLINE):
    centered(d, W // 2, 462 + i * 168, line, f_big, INK)

d.line([(W // 2 - 150, 997), (W // 2 + 150, 997)], fill=RULE, width=2)

f_sub = ImageFont.truetype(JO_L, 40)
for i, line in enumerate(SUBTITLE):
    centered(d, W // 2, 1047 + i * 56, line, f_sub, SOFT)

# (el hueco de acá abajo queda libre a propósito, para el sticker de encuesta)

draw_tracked(d, W // 2, 1618, CTA, ImageFont.truetype(JO_M, 40), 7, INK)
centered(d, W // 2, 1682, CTA_SUB, ImageFont.truetype(JO_L, 40), SOFT)
cx, y = W // 2, 1772
d.line([(cx, y), (cx, y + 44)], fill=OCHRE, width=3)
d.line([(cx - 15, y + 28), (cx, y + 46)], fill=OCHRE, width=3)
d.line([(cx + 15, y + 28), (cx, y + 46)], fill=OCHRE, width=3)

grain(img).save(os.path.join(HERE, "story-amba.png"))
print("listo: story-amba.png")
