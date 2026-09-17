# Fotos de los packs

*Armadas el 17/09/2026 con las fotos que ya están cargadas en la tienda.*

Collages cuadrados de 1200×1200 (el formato de las fichas de Tiendanube), con la tipografía de la marca: **Playfair Display** para el nombre y **Jost** para el precio y el contenido.

| Archivo | Pack | Fotos usadas |
|---|---|---|
| `pack-familiar.jpg` | Familiar · $74.600 | 6 de 6 ✅ |
| `pack-semanal.jpg` | Semanal · $45.300 | 6 de 6 ✅ |
| `pack-kids.jpg` | Kids · $43.000 | 4 de 4 ✅ |
| `pack-antojito.jpg` | Antojito · $46.200 | 4 de 5 — falta el dulce de leche |

**Falta el del Pack para picar**, y no es por la foto: **tres de sus cinco productos no están publicados en la tienda** (ver abajo).

`generar-collages.py` rehace los cuatro. Descarga las fotos de la tienda a `fotos/` y las compone. Si cambian las fotos de producto, se corre de nuevo y listo.

---

## 🔴 Lo que apareció al buscar las fotos

**La tienda tiene 16 productos publicados con foto.** Cruzándolos contra los packs:

| Producto | ¿Está en la tienda? |
|---|---|
| **Hogaza** | ❌ **No existe** — 0 menciones, y `/productos/hogaza/` da 404 |
| **Aceitunas verdes** | ❌ No publicada |
| **Hummus de garbanzo** | ❌ No publicado |
| **Dulce de leche** | ❌ No publicado |

**La hogaza es el hallazgo serio:** está en `tabla-margenes.md` y en `perfil.md` a $11.500, se le acaba de actualizar el costo a $6.700, y **el Pack para picar lleva dos**. Pero **no está publicada en la tienda**. Sin ella el pack no se puede armar ni fotografiar.

Los otros tres son productos de terceros, que ya se sabía que estaban sin stock desde el 08/09.

## 🧀 Y dos datos del queso

1. **Es un Gouda.** El título en la tienda es *"Queso Gouda Artesanal El Capricho · 400 g"*. **El gouda es un queso semiduro de maduración**, que aguanta bastante mejor a temperatura ambiente que un fresco. **No reemplaza preguntarle al proveedor cuántas horas**, pero baja mucho la preocupación de la cadena de frío.
2. **El slug de la URL quedó viejo:** `/productos/queso-semiduro-artesanal-el-capricho-450-g-1fb28/`. El título ya dice 400 g, la dirección todavía dice 450 g. No es grave, pero es lo que ve Google.
