# Cómo cargar la suscripción en Tiendanube

*Armado el 18/09/2026. Los números y la lógica salen de `suscripciones.md` sección 3 bis.*

> ⚠️ **Los nombres exactos de los botones del panel pueden variar**: Tiendanube los cambia cada tanto. Lo que importa es qué hay que lograr en cada paso, que es lo que está explicado abajo.

> 📌 **Recordá la decisión de fondo:** para los **primeros diez suscriptores conviene tomarlos por WhatsApp** con el monto cotizado, sin cargar nada. Esto es para cuando se publique en la tienda.

---

## La forma: UN producto con DOS variantes de zona

*(Corrige lo que se había dicho el 18/09 a la mañana: se habían propuesto dos productos separados.)*

**Una sola ficha, una sola foto, un solo texto, y el cliente elige su zona en un desplegable.** Menos trabajo y menos lugares donde el dato se desactualiza.

---

## Paso a paso

### 1. La categoría

Productos → Categorías → crear **Suscripciones**. Así no queda suelta entre los panes.

### 2. El producto

Productos → Agregar producto.

| Campo | Qué va |
|---|---|
| **Nombre** | `Suscripción Pack Semanal — 4 entregas` |
| **Descripción** | El texto de la sección de abajo |
| **Foto** | El collage del Pack Semanal de `textos/packs/` |
| **Categoría** | Suscripciones |

### 3. Las variantes

Buscar *"Agregar variantes"* o *"Este producto tiene variantes"*. Propiedad: **Zona de entrega**. Los nombres son los que ya usa la página de Envíos, para que el cliente los reconozca:

| Variante | Precio | **Precio promocional** |
|---|---:|---:|
| **CABA, Zona Norte y GBA cercano** | $181.200 | **$172.140** |
| **GBA norte y sur, y Zona extendida** | $201.200 | **$192.140** |

> **Cargar los dos precios, no solo el final.** El precio tachado es lo que hace visible el 5%.
>
> 📌 En la segunda variante el descuento se muestra como **4,5%** porque los $20.000 de envío no llevan descuento. Es correcto: se deja así.

### 4. El stock es el tope de trabajo

**10 unidades, no ilimitado.** Diez suscriptores son 40 envíos por mes y es hasta donde llega lo manual sin volverse un lío. Cuando se agote, se sube.

### 5. 🔴 Que Tiendanube NO calcule envío sobre este producto

Envíos → **Envío gratis** (o "Promociones de envío") → crear una regla que aplique **solo a este producto**, en **todas las zonas**, **sin monto mínimo**.

> **Es el paso que sostiene todo el armado.** El carrito mensual es de $172.140: si se deja que Tiendanube calcule, dispara el umbral de $55.000 solo y no cobra los $20.000 de las zonas lejanas. Y encima cobraría **un** envío para **cuatro** entregas.
>
> ⚠️ **Si el plan Esencial no deja elegir productos específicos** y solo ofrece "envío gratis desde $X", **este camino no sirve** y hay que resolverlo de otra forma (tomarlo por WhatsApp, o cobrar los $20.000 aparte). **Verificarlo antes de publicar.**

### 6. La prueba, antes de publicar

Cargar el producto como **no visible**, hacer un pedido de prueba a una dirección de **Escobar** eligiendo la segunda variante, y verificar:

- [ ] El total da **$192.140 clavados**
- [ ] **No aparece ninguna línea de envío** arriba de ese total
- [ ] Repetir con una dirección de **CABA** y la primera variante: **$172.140**, sin envío

Recién ahí, hacerlo visible.

---

## El texto de la descripción, listo para pegar

> **Todas las semanas el pan de la casa, y algo dulce distinto.**
>
> Recibí tu Pack Semanal todos los jueves, sin tener que acordarte de pedir.
>
> **Qué llega cada semana**
> Pan de molde integral de masa madre · Prepizzas x2 · Grisines integrales · Y algo dulce que va rotando: cookies integrales, mix de pepas o budín.
>
> Todo con harina 100% agroecológica, de panaderos artesanales que elegimos uno por uno.
>
> **Cómo funciona**
> Son 4 entregas, con un solo pago por adelantado y **5% de descuento**.
> Todos los lunes te escribimos con lo que va en la caja de esa semana, y podés cambiar algo.
>
> **Pausá cuando quieras.** Te vas de vacaciones, avisás antes del lunes y la entrega se corre al final. No se pierde.
> **Cancelá cuando quieras**, sin explicaciones.
>
> **Tu primera caja lleva algo de regalo.**
>
> **Elegí tu zona**
> Si estás en CABA, Zona Norte o GBA cercano, los envíos van sin cargo.
> Si estás en GBA norte y sur o Zona extendida, la suscripción incluye los 4 envíos de la zona.
>
> Se abona por transferencia. Escribinos y lo coordinamos.

---

## Tres cosas que conviene tener en cuenta

### 1. No se puede obligar a pagar por transferencia

**Tiendanube maneja los medios de pago para toda la tienda, no por producto.** Si alguien paga con tarjeta, $172.140 cuestan **$8.400** de comisión en vez de **$3.115**.

> **No es grave: el modelo está calculado con el 7%, que es peor que los dos.** Pero es una razón más para que los primeros se tomen por WhatsApp.

### 2. La planilla de entregas pendientes, desde el día uno

Con diez suscriptores son **diez cobros y cuarenta entregas por mes**. A la tercera semana nadie se acuerda de quién pausó.

### 3. Los $5.000 son por entrega

Si un suscriptor pausa una semana, ese mes son **$15.000**, no $20.000. Con la regla de que la entrega pausada se corre al final el mes cierra en cuatro igual, pero es el tipo de cosa que después genera un reclamo.

---

## Encargo para Claude in Chrome

*Mismo formato que `encargo-claude-chrome-tienda.md`: hacer el login a mano primero (Tiendanube manda un código por mail que el agente no puede resolver), dejar la pestaña abierta y recién ahí pegarle esto.*

> Estás en el panel de administración de Tiendanube de la tienda Corteza (cortezapan.com.ar). Necesito que crees **un producto nuevo** con dos variantes.
>
> **1. Primero creá la categoría "Suscripciones"** en Productos → Categorías, si no existe.
>
> **2. Creá el producto** en Productos → Agregar producto:
> - **Nombre exacto:** `Suscripción Pack Semanal — 4 entregas`
> - **Categoría:** Suscripciones
> - **Descripción:** pegá el texto que te paso al final, respetando las negritas y los saltos de línea.
> - **Visibilidad: NO VISIBLE.** No lo publiques. Lo va a publicar Juan después de probarlo.
>
> **3. Agregale variantes.** Propiedad: `Zona de entrega`. Dos valores, con estos precios exactos:
>
> | Valor de la variante | Precio | Precio promocional |
> |---|---|---|
> | `CABA, Zona Norte y GBA cercano` | 181200 | 172140 |
> | `GBA norte y sur, y Zona extendida` | 201200 | 192140 |
>
> **Stock: 10 unidades en cada variante.**
>
> **4. Creá la regla de envío gratis.** Andá a la sección de Envíos, buscá "Envío gratis" o "Promociones de envío", y creá una regla que aplique **únicamente al producto "Suscripción Pack Semanal — 4 entregas"**, en **todas las zonas**, **sin monto mínimo de compra**.
>
> ⚠️ **Si el panel no te deja limitar la regla a un producto específico, NO crees ninguna regla**: anotalo y avisá. Una regla por monto mínimo rompería todo el resto de la tienda.
>
> **Reglas que no podés romper:**
> - **No toques ningún otro producto**, ni precios, ni stock, ni fotos, ni las zonas de envío ya cargadas.
> - **No publiques el producto.** Tiene que quedar no visible.
> - **No inventes texto.** Pegá exactamente lo que está acá.
> - Si algo no se puede hacer como está pedido, **no improvises: anotalo y seguí**.
>
> **Al terminar, contame qué creaste, qué no pudiste y por qué**, y pasame el link de edición del producto.
>
> ---
>
> **Descripción a pegar:**
>
> *(acá va el texto de la sección "El texto de la descripción, listo para pegar")*

---

## ⚠️ Antes de publicar esto: la página de Envíos está desactualizada

`textos/pagina-envios.md` dice **"Envío sin cargo desde $40.000. En todo el AMBA, sea cual sea tu zona."**

**Ya no es cierto**: en GBA norte/sur y Zona extendida se cobran $5.000 hasta los $55.000. **Es exactamente el autogol que estaba anotado** — el cliente lee envío sin cargo y se encuentra el cargo en el checkout. **Hay que reescribirla con los tres escalones antes del lanzamiento.**
