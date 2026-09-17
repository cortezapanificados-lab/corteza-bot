from PIL import Image, ImageDraw, ImageFont
import os, unicodedata

F = "/home/user/corteza-bot/emprendimiento/textos/"
PLAYFAIR_B = F + "playfair-bold.ttf"
JOST_M     = F + "jost-medium.ttf"
JOST_L     = F + "jost-light.ttf"

S      = 1200          # lienzo cuadrado, como las fichas de Tiendanube
BANDA  = 232          # franja inferior con el nombre
GAP    = 8            # separación entre fotos
CREMA  = (245, 247, 241)
VERDE  = (79, 107, 60)
TINTA  = (25, 30, 22)
GRIS   = (108, 117, 102)

def foto(nombre):
    return Image.open("fotos/" + nombre + ".webp").convert("RGB")

def encajar(im, w, h):
    """Recorta al centro para llenar w×h sin deformar."""
    ow, oh = im.size
    esc = max(w / ow, h / oh)
    im = im.resize((max(1, round(ow * esc)), max(1, round(oh * esc))), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))

def mosaico(fotos, W, H):
    """Devuelve una lista de (foto, x, y, w, h) según cuántas haya."""
    g = GAP
    n = len(fotos)
    if n >= 6:
        gw = (W - 2 * g) // 3                      # ancho de columna
        alto_arriba = round(H * 0.62)
        alto_abajo = H - alto_arriba - g
        grande_w = 2 * gw + g
        chico_h = (alto_arriba - g) // 2
        return [
            (fotos[0], 0, 0, grande_w, alto_arriba),
            (fotos[1], grande_w + g, 0, W - grande_w - g, chico_h),
            (fotos[2], grande_w + g, chico_h + g, W - grande_w - g, alto_arriba - chico_h - g),
            (fotos[3], 0, alto_arriba + g, gw, alto_abajo),
            (fotos[4], gw + g, alto_arriba + g, gw, alto_abajo),
            (fotos[5], 2 * (gw + g), alto_arriba + g, W - 2 * (gw + g), alto_abajo),
        ]
    if n == 5:
        alto_arriba = round(H * 0.58)
        gw = (W - g) // 2
        aw = (W - 2 * g) // 3
        alto_abajo = H - alto_arriba - g
        return [
            (fotos[0], 0, 0, gw, alto_arriba),
            (fotos[1], gw + g, 0, W - gw - g, alto_arriba),
            (fotos[2], 0, alto_arriba + g, aw, alto_abajo),
            (fotos[3], aw + g, alto_arriba + g, aw, alto_abajo),
            (fotos[4], 2 * (aw + g), alto_arriba + g, W - 2 * (aw + g), alto_abajo),
        ]
    if n == 4:
        gw = (W - g) // 2
        gh = (H - g) // 2
        return [
            (fotos[0], 0, 0, gw, gh),
            (fotos[1], gw + g, 0, W - gw - g, gh),
            (fotos[2], 0, gh + g, gw, H - gh - g),
            (fotos[3], gw + g, gh + g, W - gw - g, H - gh - g),
        ]
    if n == 3:
        gw = round(W * 0.6)
        gh = (H - g) // 2
        return [
            (fotos[0], 0, 0, gw, H),
            (fotos[1], gw + g, 0, W - gw - g, gh),
            (fotos[2], gw + g, gh + g, W - gw - g, H - gh - g),
        ]
    gw = (W - g) // 2
    return [(fotos[0], 0, 0, gw, H), (fotos[1], gw + g, 0, W - gw - g, H)]

def centrar(d, txt, fuente, y, color, ancho=S):
    b = d.textbbox((0, 0), txt, font=fuente)
    d.text(((ancho - (b[2] - b[0])) / 2 - b[0], y), txt, font=fuente, fill=color)
    return b[3] - b[1]

def ajustar(d, txt, path, y, color, maxw, tam_ini):
    """Baja el cuerpo hasta que entre en maxw."""
    t = tam_ini
    while t > 12:
        f = ImageFont.truetype(path, t)
        b = d.textbbox((0, 0), txt, font=f)
        if b[2] - b[0] <= maxw:
            break
        t -= 2
    centrar(d, txt, f, y, color)
    return t

def armar(nombre, precio, contenido, archivos, salida):
    lienzo = Image.new("RGB", (S, S), CREMA)
    alto_fotos = S - BANDA
    ims = [foto(a) for a in archivos]
    for im, x, y, w, h in mosaico(ims, S, alto_fotos):
        lienzo.paste(encajar(im, w, h), (x, y))

    d = ImageDraw.Draw(lienzo)
    y0 = alto_fotos
    d.rectangle([0, y0, S, S], fill=CREMA)
    d.rectangle([0, y0, S, y0 + 3], fill=VERDE)

    ajustar(d, nombre.upper(), PLAYFAIR_B, y0 + 40, TINTA, S - 120, 62)
    f_precio = ImageFont.truetype(JOST_M, 46)
    centrar(d, precio, f_precio, y0 + 122, VERDE)
    ajustar(d, contenido, JOST_L, y0 + 184, GRIS, S - 100, 25)

    lienzo.save(salida, quality=92)
    print(f"  {salida}  ({len(archivos)} fotos)")

MOLDE_B   = "pan_de_molde_blanco"
MOLDE_I   = "pan_de_molde_integral"
CAMPO_B   = "pan_de_campo_blanco"
PREPIZZA  = "prepizzas_cebolla_blanca"   # 2a foto de la ficha: cebolla BLANCA
PEPAS     = "pepas_integrales"
COOKIES   = "cookies_integrales_con_chips_de_chocolat"
GRISINES  = "grisines_integrales"
BUDIN     = "budin"
QUESO     = "queso_gouda_artesanal_el_capricho_400_g"
HOGAZA    = "hogaza"
ACEITUNAS = "aceitunas_verdes"
HUMMUS    = "hummus"
DDL       = "dulce_de_leche"

packs = [
 ("Pack familiar", "$74.600",
  "2 panes de molde · 2 prepizzas · 2 mix pepas · 2 cookies · 2 grisines",
  [MOLDE_B, MOLDE_I, PREPIZZA, PEPAS, COOKIES, GRISINES], "pack-familiar.jpg"),
 ("Pack semanal", "$45.300",
  "Pan de molde integral · prepizzas · budín de limón · mix pepas · cookies · grisines",
  [MOLDE_I, PREPIZZA, BUDIN, PEPAS, COOKIES, GRISINES], "pack-semanal.jpg"),
 ("Pack kids", "$43.000",
  "3 cookies integrales · budín con chips · prepizzas de tomate · mix pepas",
  [COOKIES, PREPIZZA, BUDIN, PEPAS], "pack-kids.jpg"),
 ("Pack antojito", "$46.200",
  "Pan de campo blanco · dulce de leche · budín con chips · 2 cookies · mix pepas",
  [CAMPO_B, DDL, BUDIN, COOKIES, PEPAS], "pack-antojito.jpg"),
 ("Pack para picar", "$51.500",
  "2 hogazas · queso gouda El Capricho · aceitunas verdes · grisines · hummus",
  [HOGAZA, QUESO, ACEITUNAS, GRISINES, HUMMUS], "pack-para-picar.jpg"),
]
print("Generando:")
for n, p, c, a, s in packs:
    armar(n, p, c, a, s)
