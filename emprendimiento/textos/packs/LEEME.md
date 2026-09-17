# Fotos de los packs

*Armadas el 17/09/2026 con las fotos que ya están cargadas en la tienda.*

**Los cinco collages están listos.** Son cuadrados de 1200×1200 (el formato de las fichas de Tiendanube), con la tipografía de la marca: **Playfair Display** para el nombre y **Jost** para el precio y el contenido.

| Archivo | Pack | |
|---|---|---|
| `pack-familiar.jpg` | Familiar · $74.600 | 6 fotos |
| `pack-semanal.jpg` | Semanal · $45.300 | 6 fotos |
| `pack-kids.jpg` | Kids · $43.000 | 4 fotos |
| `pack-antojito.jpg` | Antojito · $46.200 | 5 fotos |
| `pack-para-picar.jpg` | Para picar · $51.500 | 5 fotos |

`generar-collages.py` los rehace. Descarga las fotos de la tienda y las compone; si cambian las fotos de producto, se corre de nuevo.

> 🧅 **La prepizza sale de la SEGUNDA foto de su ficha, no de la primera** *(cambiado el 17/09)*. La primera muestra **cebolla morada** y el producto lleva **cebolla blanca**. Juan subió a la tienda una foto cenital nueva con las dos prepizzas —la de cebolla blanca adelante, la de tomate atrás— y esa es la que usan los cinco collages. El recorte se guarda como `fotos/prepizzas_cebolla_blanca.webp`.
>
> ⚠️ **La foto de la ficha sigue estando mal.** En la tienda, la imagen principal de Prepizzas x2 es la de cebolla morada: **conviene cambiar el orden de las fotos en el panel** para que la de cebolla blanca quede primera. Si no, el cliente ve un producto y recibe otro.

> ℹ️ **El de "para picar" queda menos parejo que los otros cuatro**, y es inevitable: tres de sus productos son de terceros y sus fotos son packshots de frasco sobre fondo blanco, mientras que el pan y el queso son fotos de ambiente. Se ve honesto y muestra exactamente lo que lleva, pero no tiene la cohesión de los packs 100% propios.

---

## 🔴 23 de los 39 productos están agotados, y Tiendanube los esconde

**Este es el hallazgo que salió de buscar las fotos.** La tienda tiene **39 productos publicados** (están todos en el sitemap), pero el listado de `/productos/` muestra solo **16**: Tiendanube **oculta del listado los que están sin stock**.

**Los 23 restantes existen, tienen ficha y tienen foto — pero nadie los encuentra navegando.**

### Lo que eso significa para los packs

| Producto | Estado | Dónde pega |
|---|---|---|
| **Hogaza** | agotada | 🔴 **El Pack para picar lleva DOS** |
| Aceitunas verdes | agotada | Pack para picar |
| Hummus de garbanzos | agotado | Pack para picar |
| Dulce de leche Las Quinas | agotado | Pack antojito |

**La hogaza es la que más preocupa: es un panificado propio**, no un producto de terceros. Los demás panes figuran disponibles y ella no. **Sin reponerla, el Pack para picar no se puede vender**, y es el único pack salado del lineup.

⚠️ **Y hay un efecto de vidriera más amplio:** si el 24 se lanza con 23 de 39 productos agotados, **el cliente de CABA que entra por primera vez ve una tienda de 16 productos**, no de 39. Se cruza con el problema de la página de inicio, que ya no muestra ninguno.

---

## 🧀 Dos datos del queso

1. **Es un Gouda.** El título en la tienda es *"Queso Gouda Artesanal El Capricho · 400 g"*. **El gouda es un queso semiduro de maduración**, que aguanta bastante mejor a temperatura ambiente que uno fresco. **No reemplaza preguntarle al proveedor cuántas horas**, pero baja mucho la preocupación de la cadena de frío.
2. **El slug de la URL quedó viejo:** `/productos/queso-semiduro-artesanal-el-capricho-450-g-1fb28/`. El título ya dice 400 g, la dirección todavía dice 450 g.

## Y dos productos del sitemap que la memoria no tenía

- **Laur Aceite de Oliva Extra Virgen Gran Mendoza 500ml** — no está en `tabla-margenes.md`, que solo tiene el Zuelo de 250ml.
- **Kéfir de agua** (tradicional e hibiscus) y las dos **kombuchas** ya están publicados, aunque seguían anotados como pendientes de cargar.

Todo esto refuerza lo ya anotado: **hace falta un export nuevo de Tiendanube** para rehacer la tabla de márgenes.
