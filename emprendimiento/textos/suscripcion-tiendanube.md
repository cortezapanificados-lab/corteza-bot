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
| **CABA y GBA cercano — envíos incluidos** | $181.200 | **$172.140** |
| **GBA norte y sur, y Zona extendida — incluye los 4 envíos (+$20.000)** | $201.200 | **$192.140** |

> 📌 **Los nombres largos son a propósito.** Ver la sección "Lo que Tiendanube no puede hacer", más abajo.

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
> Si estás en CABA o GBA cercano, los envíos van sin cargo.
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

## Encargo para Claude in Chrome — listo para copiar y pegar

*Formato de la casa (ver `encargo-claude-chrome-tienda.md`).*

> **Antes de arrancar, el login se hace a mano** en `tiendanube.com` (cuenta `juan_guerrini@hotmail.com`). Tiendanube manda un código de verificación por mail que el agente no puede resolver solo. Dejar la pestaña del panel abierta y recién ahí pegarle el encargo.
>
> **Son dos tandas separadas. Pasarle una, esperar a que termine, mirar el resultado, y recién ahí la segunda.** La tanda 2 toca la configuración de envíos de toda la tienda: por eso va aparte.

### TANDA 1 — Crear el producto

```
Estás en el panel de administración de Tiendanube de la tienda Corteza
(cortezapan.com.ar). Necesito que crees UN producto nuevo con dos variantes.
No toques nada más de la tienda.

PASO 1 — La categoría
Andá a Productos → Categorías. Si no existe una categoría llamada
"Suscripciones", creala. Si ya existe, no la modifiques.

PASO 2 — El producto
Andá a Productos → Agregar producto y cargá:

- Nombre exacto: Suscripción Pack Semanal — 4 entregas
- Categoría: Suscripciones
- Visibilidad: NO VISIBLE / oculto. NO lo publiques. Lo va a revisar Juan
  antes de publicarlo.
- Descripción: pegá el texto que está al final de este mensaje, entre las
  líneas de guiones. Respetá las negritas y los saltos de línea tal como
  están. Donde el texto tiene **asteriscos dobles**, eso va en negrita y los
  asteriscos NO se escriben.

PASO 3 — Las variantes
En ese mismo producto, activá las variantes (buscá "Agregar variantes" o
"Este producto tiene variantes").

Nombre de la propiedad: Zona de entrega

Dos valores, con estos datos exactos:

Valor 1: CABA y GBA cercano — envíos incluidos
  Precio: 181200
  Precio promocional (o precio de oferta): 172140
  Stock: 10

Valor 2: GBA norte y sur, y Zona extendida — incluye los 4 envíos (+$20.000)
  Precio: 201200
  Precio promocional (o precio de oferta): 192140
  Stock: 10

IMPORTANTE: cargá LOS DOS precios en cada variante, el normal y el
promocional. El precio tachado es parte del diseño, no es un error.

REGLAS QUE NO PODÉS ROMPER
- No toques ningún otro producto: ni precios, ni stock, ni costos, ni fotos,
  ni descripciones.
- No toques la configuración de envíos, ni las zonas, ni los medios de pago.
  Eso va en un encargo aparte.
- No publiques el producto. Tiene que quedar oculto.
- No inventes ni reescribas texto. Pegá exactamente lo que está acá.
- Si algo no se puede hacer como está pedido, NO improvises: anotalo y seguí
  con lo que sí se pueda.
- No le pongas foto. La carga Juan.

AL TERMINAR
Contame qué creaste, qué no pudiste hacer y por qué, y pasame el link de
edición del producto.

--------------------------------------------------
DESCRIPCIÓN A PEGAR:

**Todas las semanas el pan de la casa, y algo dulce distinto.**

Recibí tu Pack Semanal todos los jueves, sin tener que acordarte de pedir.

**Qué llega cada semana**
Pan de molde integral de masa madre · Prepizzas x2 · Grisines integrales · Y algo dulce que va rotando: cookies integrales, mix de pepas o budín.

Todo con harina 100% agroecológica, de panaderos artesanales que elegimos uno por uno.

**Cómo funciona**
Son 4 entregas, con un solo pago por adelantado y **5% de descuento**.
Todos los lunes te escribimos con lo que va en la caja de esa semana, y podés cambiar algo.

**Pausá cuando quieras.** Te vas de vacaciones, avisás antes del lunes y la entrega se corre al final. No se pierde.

**Cancelá cuando quieras**, sin explicaciones.

**Tu primera caja lleva algo de regalo.**

**Elegí tu zona**
Si estás en CABA o GBA cercano, los envíos van sin cargo.
Si estás en GBA norte y sur o Zona extendida, la suscripción incluye los 4 envíos de la zona.

Se abona por transferencia. Escribinos y lo coordinamos.
--------------------------------------------------
```

### TANDA 2 — La regla de envío

*Pasársela recién cuando la tanda 1 haya terminado bien.*

```
Seguimos en el panel de Tiendanube de Corteza. Ahora una sola tarea, y es
delicada porque toca la configuración de envíos de toda la tienda.

LO QUE NECESITO
Que el producto "Suscripción Pack Semanal — 4 entregas" NO pague envío en
ninguna zona, sin importar el monto del carrito.

CÓMO
Andá a la sección de Envíos del panel y buscá una opción llamada "Envío
gratis", "Promociones de envío" o similar. Creá una regla con estas
condiciones:

- Se aplica ÚNICAMENTE al producto "Suscripción Pack Semanal — 4 entregas"
- En TODAS las zonas de envío
- SIN monto mínimo de compra

FRENO IMPORTANTE
Si el panel NO te deja limitar la regla a un producto específico —por
ejemplo, si solo te ofrece "envío gratis a partir de $X"— entonces NO CREES
NINGUNA REGLA. Una regla por monto mínimo rompería el esquema de envíos de
toda la tienda.

En ese caso: no toques nada, sacá una captura de pantalla de las opciones
que sí te ofrece, y contame exactamente qué opciones hay disponibles.

REGLAS QUE NO PODÉS ROMPER
- No modifiques ni borres ninguna regla de envío que ya exista.
- No toques las zonas de envío ni sus precios.
- No toques ningún producto.
- Si dudás, no hagas nada y preguntá.

AL TERMINAR
Contame si pudiste crear la regla o no, y qué opciones te ofrecía el panel.
```

### Lo que queda para hacer a mano después

El agente deja el producto **oculto** a propósito. Antes de publicarlo:

1. **Subirle la foto** — el collage del Pack Semanal de `textos/packs/`.
2. **Pedido de prueba a una dirección de Escobar**, segunda variante → tiene que dar **$192.140 clavados**, sin ninguna línea de envío arriba.
3. **Otro a una dirección de CABA**, primera variante → **$172.140**.
4. Si los dos dan bien, hacerlo visible.

> 🔴 **Si la tanda 2 vuelve con que no se puede limitar por producto, no publicar nada.** Ahí el armado cambia y hay que rehacerlo.

---

## 🚫 Lo que Tiendanube no puede hacer: atar la variante a la zona

*Pregunta de Juan del 21/09/2026: ¿se puede impedir que alguien de Escobar compre la variante de CABA?*

> ### No, no se puede. Y es una limitación real de Tiendanube, no una mala configuración.

**Las variantes no saben la dirección.** El cliente elige la variante en la ficha del producto y carga la dirección después, en el checkout. Son dos momentos distintos y Tiendanube no los cruza.

**Es el precio de haber metido el envío adentro del precio** — que se hizo para esquivar un problema peor: que el carrito de $172.140 dispare el umbral de $55.000 y no cobre **nada** de envío en ninguna zona.

### Cuánto puede doler, con números

| | |
|---|---:|
| Stock topeado en | **10 suscriptores** |
| De zonas lejanas, por la mezcla esperada | ~3 |
| Si uno se equivoca, cuesta | **$20.000/mes** |
| Contra una contribución mensual de | ~$400.000 |

**Y se ve sí o sí.** La suscripción se cobra a mano por transferencia y para despachar hay que leer la dirección. No es un agujero que se escapa meses: se ve la primera semana.

### Las tres cosas que lo bajan casi a cero

1. **Nombres de variante que no dejen lugar a dudas** *(ya aplicado arriba)*. La mayoría de estos casos son confusión honesta, no viveza. **Y en la descripción va la lista de localidades, no los nombres de zona sueltos**: el que vive en Escobar tiene que poder leer "Escobar" ahí.
2. **Mirar la dirección antes de confirmar la suscripción.** Un chequeo por suscriptor, diez por mes. Es el mismo dato que hace falta para despachar, solo que mirado tres días antes.
3. **Si se equivocó, no se cancela: se le cobra la diferencia.** *"Vi que sos de Escobar, te falta el envío: son $20.000 más, o si preferís te sumo un pan de molde por semana y te queda sin cargo el envío."* **Es el mejor uso de la alternativa del pan** (`suscripciones.md` sección 3 bis): convierte un reclamo en una venta más grande.

### Lo que sí lo elimina del todo

**No venderla por la tienda.** Por WhatsApp se cotiza con la dirección sobre la mesa y el error es imposible. **Ya era la recomendación para los primeros diez; esto es un argumento más.**

### Una pista, si más adelante hace falta cerrarlo

En la **Tienda de Aplicaciones de Tiendanube**, buscar *"restricción de productos por zona"* u *"ocultar productos por ubicación"*. Hay apps de terceros que hacen esto.

⚠️ **Es una pista, no una solución verificada:** no se conoce el catálogo de apps ni cuáles andan con el plan Esencial, y varias son pagas. **Para diez suscriptores no cierra** pagar un abono mensual para tapar una exposición eventual de $20.000. Con cincuenta, vale la pena mirarlo.

---

## ⚠️ Antes de publicar esto: la página de Envíos está desactualizada

`textos/pagina-envios.md` dice **"Envío sin cargo desde $40.000. En todo el AMBA, sea cual sea tu zona."**

**Ya no es cierto**: en GBA norte/sur y Zona extendida se cobran $5.000 hasta los $55.000. **Es exactamente el autogol que estaba anotado** — el cliente lee envío sin cargo y se encuentra el cargo en el checkout. **Hay que reescribirla con los tres escalones antes del lanzamiento.**
