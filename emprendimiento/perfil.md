# Perfil de Corteza

*Última actualización: 28/08/2026 (Flexit pasa a ser la logística del AMBA; condición fiscal)*

**Quien lleva Corteza: Juan (varón — hablarle en masculino).**

Corteza es una marca de panificados artesanales de Pilar, Buenos Aires, Argentina. **Modelo de negocio: curaduría/reventa** — los panificados los elaboran distintos proveedores artesanales (masa madre, harinas 100% agroecológicas) y Corteza los selecciona y los vende bajo su marca. La tienda también vende productos orgánicos y artesanales de otras marcas (almacén, vinoteca, dips y té).

**El negocio es 100% online.** No hay local a la calle. La dirección de Pilar es administrativa; si hace falta stockear algo, se stockea en la casa particular.

**Condición fiscal: Corteza es monotributista** (Juan Martín Guerrini). El IVA que paga por sus costos **no se recupera**: es costo puro, no crédito fiscal. ⚠️ **Al volumen proyectado del AMBA (~$3,6 millones mensuales con 30 pedidos por jueves) puede quedar fuera del monotributo. Hay que consultarlo con el contador antes del lanzamiento**, porque si pasa a responsable inscripto cambian el IVA del flete y toda la estructura de costos.

**Logística del AMBA: FLEXIT** (decidido el 28/08/2026, reemplaza a Smart Post, que dejó de responder). Logística tercerizada, same-day, con cuatro zonas. El costo de envío depende de la zona del comprador y **lo paga el comprador**, salvo que supere un mínimo de compra (ver `envios-amba.md`).

**Tarifas Flexit** (tarifario de septiembre 2026, **con IVA al 10,5%** — la condición acordada pagando en efectivo):

| Zona | Qué incluye | Costo | **Se le cobra al cliente** |
|---|---|---:|---:|
| **Cercana** | Todo CABA | $4.356 | **$4.700** |
| **Media** | San Isidro (Beccar, Martínez, Acassuso), Vicente López, San Fernando, Gral. San Martín, Tres de Febrero, Morón, Hurlingham, Ituzaingó, Avellaneda, Lanús, Lomas de Zamora, La Matanza norte | $6.102 | **$6.600** |
| **Lejana** | Tigre (Nordelta), San Miguel, José C. Paz, Malvinas Argentinas, Moreno, Merlo, La Matanza sur, Quilmes, Berazategui, Florencio Varela, Alte. Brown, E. Echeverría, Ezeiza | $7.848 | **$8.500** |
| **Muy lejana** | **Pilar**, Escobar, Del Viso, Derqui, Garín, Villa Rosa, Ing. Maschwitz, Gral. Rodríguez, Luján, Campana, Zárate, Marcos Paz, Cañuelas, San Vicente, Guernica, La Plata, Berisso, Ensenada | $9.157 | **$9.900** |

**Pilar está en la zona más cara**, igual que con Smart Post. Por eso las entregas de Pilar se siguen haciendo con **reparto propio**: por Flexit cada pedido de Pilar daría pérdida. **CABA es la zona más barata y la más rentable para vender.**

Lo que incluye Flexit: **segunda y tercera visita sin costo adicional**, same-day, IVA aclarado por escrito y cobertura más amplia que Smart Post (suma Campana, Zárate, Luján y La Plata). Los seguros (0,5% depósito / 0,7% tránsito) son opcionales y **no se toman**.

**Condiciones acordadas con Flexit (28/08/2026):**
- **Mínimo de 120 envíos por mes**, no 30 por despacho. Se cuenta sobre el mes entero, así que un jueves flojo se compensa con uno bueno. **Es la condición que Smart Post nunca quiso dar.**
- **Pago del total en efectivo, una vez por mes** (~$727.000 mensuales en el piso de 120 envíos).
- **Flexit sabe que Corteza manda panificados a temperatura ambiente**, sin cadena de frío.

**Packaging: cada pedido va en 2 bolsas camiseta de ~2 kg cada una** (unos 4 kg por pedido).

🔥 **La pregunta abierta más cara: ¿Flexit cobra por envío o por bulto?** Como cada pedido son dos bolsas, si cobran por bulto el flete se duplica y **el AMBA deja de cerrar en todas las zonas salvo CABA**. Si la respuesta es "por bulto", la solución es consolidar las dos bolsas en un solo bulto cerrado — algo que conviene hacer igual, porque una bolsa camiseta no protege el pan en una camioneta compartida ni representa a la marca. Ver `envios-amba.md`.

⚠️ **También falta confirmar**: cómo se cuenta el primer mes del mínimo (arrancando el 17/9 hay solo dos despachos en septiembre), si hay tope máximo, el horario y costo de la colecta en Pilar y el tope de responsabilidad por bulto.

**Las tarifas son mensuales** y están alineadas a los envíos Flex de MercadoLibre: hay que pedir el tarifario nuevo todos los meses.

## Estructura de costos

**Por pedido:**
- **Margen bruto real (calculado con los costos exportados de Tiendanube el 10/08/2026):**
  - Panificados propios: **45,9%** ponderado
  - Productos de terceros: **29,0%** ponderado
  - Catálogo completo: **36,9%**
  - *(El "30%" que se venía usando era una estimación y quedó desactualizado. El margen real es bastante mejor.)*
- **Comisión Pago Nube: 7%** de la venta.
- **Packaging: 1%** de la venta.
- **Envío**: según zona (arriba), a cargo del comprador. El precio que se le cobra lleva recargo para cubrir la comisión de Pago Nube (se divide por 0,93): **$4.700 Cercana, $6.600 Media, $8.500 Lejana, $9.900 Muy lejana**.

> **El modelo, en una línea: ganancia por pedido = venta × (margen bruto − 8%).**

**Fijos mensuales:**
- Claude: $35.000
- Tiendanube: $27.000
- Envío del proveedor al almacén: $20.000
- Publicidad en Meta: a definir (ver `campana-meta.md`)

**Total fijos: $82.000/mes** antes de publicidad.

**Techo de margen neto: 37,9%** (45,9% de margen bruto en propios menos el 8% de cargas). **Ya supera el objetivo del 30%.**

**Punto de equilibrio:** 8 pedidos/mes sin publicidad, 22 con Meta a $150.000 (5 por jueves).

**Se llega al 30% de margen neto con 24 pedidos por jueves.** Y el mínimo de 30 que exige Smart Post ya deja 31,5%: cuando se pueda despachar con ellos, el objetivo está cumplido por definición. Análisis completo en `numeros.md`.

El lanzamiento está esperando una **mudanza personal** de quien lleva el emprendimiento (no se muda el negocio; es un tema de espacio para stockear). Es un asunto privado: **no se usa como material de comunicación.**

Cuando se lance, se abre **todo el AMBA de una vez**, no por zonas: como la logística es tercerizada y cada pedido se cobra por separado, no hay ninguna ventaja en abrir de a poco.

- Tienda online: www.cortezapan.com.ar (plataforma Tiendanube)
- Email: corteza.panificados@gmail.com
- Teléfono: 11 5415-3989
- Dirección: C. 9 1761, B1629 Pilar, Provincia de Buenos Aires

## Panificados propios

*Precios relevados directamente de la tienda el 10/08/2026. La columna "nuevo" es el aumento del 15% decidido ese día (ver `numeros.md`). Costos y márgenes por producto en `tabla-margenes.md`.*

| Producto | Precio anterior | **Precio nuevo (+15%)** | Notas |
|---|---|---|---|
| Pan de molde blanco | $10.000 | **$11.500** | masa madre; 850g |
| Pan de molde integral | $10.000 | **$11.500** | masa madre; 850g |
| Pan de molde de centeno | $10.000 | **$11.500** | masa madre; 850g |
| Hogaza | $10.000 | **$11.500** | masa madre; dos variantes |
| Pan de campo blanco | $7.500 | **$8.600** | masa madre; 500g |
| Pan de campo integral | $7.500 | **$8.600** | masa madre; 500g |
| Pan de campo de centeno | $7.500 | **$8.600** | masa madre; 500g |
| Pan árabe integral x5 | $7.500 | **$8.600** | masa madre |
| Prepizzas x2 | $7.000 | **$8.000** | masa madre; blancas. Variantes por cobertura: salsa de tomate / cebolla / 1 y 1. Si alguna vez se venden integrales, ese costo sube a $5.000 |
| Budín | $7.000 | **$8.000** | por ahora solo blancos |
| Cookies integrales con chips de chocolate y nuez | $6.000 | **$6.900** | veganas; 200g |
| Pepas integrales | $5.500 | **$6.300** | veganas; batata y membrillo; 200g |
| Grisines integrales | $4.000 | **$4.600** | 200g |

Todos con harinas 100% agroecológicas. Los panes (molde, campo, árabe, prepizzas) son de masa madre; grisines, budines, pepas y cookies no.

Algunos panes se ofrecen enteros o rebanados.

### Promo Lanzamiento — $25.000 → **$28.900**

Incluye: 1 pan de molde blanco rebanado, 1 paquete de pepas integrales (batata y membrillo), 1 budín con chips de chocolate y 1 paquete de grisines integrales.

Comprando suelto a los precios nuevos serían $30.400, así que la promo mantiene el mismo descuento relativo que tenía (~5%).

## Productos de terceros

**Al 10/08/2026 están todos SIN STOCK en la tienda.** Las aceitunas negras y verdes San Nicolás ya no figuran en el catálogo.

**Criterio de precio:** acá no hay poder de precio, porque son marcas que el cliente puede comparar en dos segundos. El precio lo fija el mercado, no los costos de Corteza. **Nunca aplicarles los aumentos que se le apliquen a los panificados propios.** El objetivo es quedar en torno a **mercado +10%**, que es un premium defendible para una tienda curada con entrega a domicilio.

### Almacén orgánico

| Producto | Precio anterior | **Nuevo** | Mercado (relevado 10/08/2026) |
|---|---|---|---|
| Mermelada de frutos rojos Las Quinas 450g | $9.400 | **$8.700** | ~$7.890 (estaba 19% arriba) |
| Mermelada de frutilla Las Quinas 450g | $9.400 | **$8.700** | ~$7.890 |
| Dulce de leche Las Quinas | $9.400 | **$8.600** | ~$7.800 (estaba 20% arriba) |
| Yerba orgánica Roapipó suave 500g | $6.600 | **$6.100** | $4.458–$6.899 (estaba en el techo) |
| Miel líquida orgánica Las Quinas 500g | $9.400 | sin cambio | sin datos |
| Miel cremosa Las Quinas 500g | $8.200 | sin cambio | sin datos |
| Hummus de garbanzos Pampa Gourmet 180g | $5.200 | sin cambio | sin datos |
| Pickles orgánicos San Nicolás 250g | $6.200 | sin cambio | sin datos |
| Aceite de oliva Zuelo orgánico 250ml | $11.000 | sin cambio | $10.279–$12.155 ✅ en mercado |

### Dips y condimentos

| Producto | Precio anterior | **Nuevo** | Mercado |
|---|---|---|---|
| Pasta de tomates secos Contraviento 180g | $10.600 | **$9.800** | sin dato directo; se bajó en proporción |
| Pasta de aceitunas verdes Contraviento 170g | $9.700 | **$8.900** | $6.069–$9.592 (estaba arriba del rango) |
| Mostaza Dijón Arytza 360g | $7.600 | sin cambio | sin datos |

## Té (Intizen, cajas x15 saquitos)

| Producto | Precio |
|---|---|
| Dulce Manzanilla | $5.200 |
| Verde Chai | $5.200 |
| Chaman Chai | $5.200 |

## Vinoteca orgánica

Los vinos son lo más comparable de todo el catálogo: **no tocarlos sin chequear el mercado primero.**

| Producto | Precio | Mercado |
|---|---|---|
| Animal Extra Brut orgánico 375ml | $8.000 | sin datos |
| La Linda Malbec orgánico 750ml | $18.500 | la versión no orgánica ronda $13.650; conviene chequear la orgánica |
| Ruca Malen Cap 2 Chardonnay orgánico 750ml | $16.500 | $16.920–$18.800 ✅ apenas por debajo |

## Logística

- Zona de entrega: hoy únicamente Pilar; al lanzar, todo el AMBA vía **Flexit**. Pilar queda siempre con reparto propio.
- Día de entrega: **jueves** (único día, para Pilar y para todo el AMBA).
- **Cierre de pedidos: lunes 14:00** (ya actualizado en la tienda). El pedido a los proveedores sale el lunes a la tarde y la mercadería llega el miércoles.
- Horario: de 9 a 17 hs aprox.
- **Cierre de pedidos** (pan de masa madre, vigente desde el 24/07/2026): pedidos hasta el **sábado** se entregan el **martes**; pedidos hasta el **martes** se entregan el **viernes**. El pan llega el mismo día de entrega.
- Sin pedido mínimo
- Envío bonificado según zona (ver `envios-amba.md`): **CABA y Pilar sin cargo desde $18.000; Media sin cargo desde $24.000; Lejana bonificación de $3.000 desde $28.000; Muy lejana bonificación de $3.000 desde $32.000**

## Marca (INPI)

- Solicitud de registro de "CORTEZA" (denominativa): **acta 4.729.366, clase 35** (venta minorista de alimentos, tienda online, marketing y afines), presentada el 10/06/2026 a nombre de Juan Martín Guerrini.
- Estado al 24/07/2026: **con oposición** de Néstor Mario Valente ("Corteza Naturalmente Genuinos", rubro ropa/bolsos). Vista notificada el 22/07/2026, **vence el 22/10/2026**. Ver bitácora y pendientes.

## Medios de pago

Transferencia bancaria, efectivo, tarjeta de crédito y débito. (El pie de la tienda dice "tarjetas de crédito o efectivo".)
