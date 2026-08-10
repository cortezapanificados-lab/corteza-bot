# Los números de Corteza

*Armado el 10/08/2026. Estructura de costos completa, punto de equilibrio y qué hace falta para llegar al margen que querés.*

> **Nota importante sobre este documento:** cada tabla aclara con qué **margen bruto** está calculada. Es fundamental, porque el margen bruto **no es siempre 30%** — ver la sección 3.

---

## 1. Todos tus costos

### Por pedido (variables)

| Concepto | Cuánto |
|---|---|
| Costo del producto (proveedor) | 70% del precio actual → **margen bruto 30%** |
| Comisión Pago Nube | **6%** |
| Packaging | **$1.000** (2 bolsas de $350 + $300) |
| Envío | $3.919 CABA / $6.265 Cordón 1 / $8.196 Cordón 2 y 3 |

### Fijos mensuales

| Concepto | Por mes |
|---|---|
| Tiendanube | $27.000 |
| Claude | $35.000 |
| Flete del proveedor a tu depósito | **$20.000 por viaje** |
| Publicidad en Meta | a definir |

**El flete del proveedor es el costo fijo más grande y depende de cuántos viajes hagas:**

| Frecuencia | Viajes/mes | Costo mensual |
|---|---|---|
| 3 por semana (martes + jueves + viernes) | 13 | $260.000 |
| 2 por semana | 8,7 | $173.300 |
| **1 por semana — solo jueves** ✅ | **4,3** | **$86.600** |

✅ **Ya está resuelto: al pasar a entregar solo los jueves, este costo bajó a $86.600 mensuales.** Comparado con tres viajes semanales, son **$173.400 por mes de ahorro** — más que Tiendanube y Claude juntos, y el equivalente a 32 pedidos. Fue la mejor decisión de toda la sesión.

**Costos fijos totales: $148.600/mes** (Tiendanube + Claude + viajes), antes de publicidad.

---

## 2. La cuenta abierta, peso por peso

Pedido de $28.000 en productos, Cordón 1, el cliente paga el envío:

| Concepto | Monto |
|---|---|
| **ENTRA** (el cliente paga producto + envío) | **+$34.265** |
| − Proveedor | −$19.600 |
| − Comisión Pago Nube (6% de $34.265) | −$2.056 |
| − Packaging | −$1.000 |
| − Smart Post | −$6.265 |
| **= TE QUEDA** | **$5.344** |

Esos $5.344 son el **19,1% de los $28.000** de producto.

### De dónde sale el 19,1% (y por qué no da 20,4%)

Tu intuición dice: 30% de margen bruto, menos 6% de comisión, menos $1.000 de packaging (que es 3,6%) = **20,4%**. Y está perfecta esa cuenta.

Mi 19,1% sale de un supuesto que hice y no te dije: **que Pago Nube te cobra el 6% sobre todo lo que cobrás, incluido el envío.** El 6% de $34.265 son $2.056, que sobre los $28.000 de producto representan 7,3% en vez de 6%. Esos 1,3 puntos son toda la diferencia.

| | Techo de margen neto |
|---|---|
| Si la comisión pega sobre producto + envío | **19,1%** |
| Si la comisión pega solo sobre el producto | **20,4%** |

> 🔍 **Hay que confirmarlo en el panel de Pago Nube.** Los procesadores de pago normalmente cobran sobre el total de la transacción, por eso lo asumí así, pero es un dato verificable y vale la pena mirarlo. En el resto del documento uso el escenario conservador (19,1%).

**Lo que no cambia con ninguna de las dos hipótesis:** con margen bruto 30% tu techo de margen neto está entre 19% y 20%, y no lo supera ningún volumen. Para pasar de ahí hay que subir precios.

### Punto de equilibrio a precios actuales

Con entregas **solo los jueves** → un viaje al proveedor por semana ($86.600/mes). Fijos base: **$148.600**.

| Meta | Costos fijos | Pedidos/mes para no perder | Por jueves |
|---|---|---|---|
| $0 | $148.600 | **28** | 6,4 |
| $60.000 | $208.600 | **39** | 9,0 |
| $150.000 | $298.600 | **56** | 12,9 |

---

## 3. El techo de margen neto, según el precio

**Con margen bruto 30% el techo está en 19,1%.** Ningún volumen lo supera: los costos fijos se diluyen, pero la contribución por pedido como porcentaje de la venta no se mueve.

**Cualquier número mayor con margen bruto 30% es imposible.** Tenías razón en frenarme las dos veces.

### Pero el margen bruto no se queda en 30% si subís precios

Acá está la parte que no expliqué bien. **El proveedor te sigue cobrando lo mismo.** Si subís el precio y el costo no se mueve, todo el aumento va derecho a margen:

| Precio | Aumento | Costo proveedor | **Margen bruto** | Techo neto (hip. A) | Techo neto (hip. B) |
|---|---|---|---|---|---|
| $28.000 | — | $19.600 | **30,0%** | 19,1% | 20,4% |
| $30.800 | +10% | $19.600 | 36,4% | 25,9% | 27,1% |
| $32.200 | +15% | $19.600 | **39,1%** | 28,9% | 30,0% |
| $33.600 | +20% | $19.600 | 41,7% | 31,6% | 32,7% |
| $35.000 | +25% | $19.600 | 44,0% | 34,1% | 35,1% |

Las tablas donde aparecía 24,6% eran las del escenario **+15%**, donde el margen bruto ya no es 30% sino 39,1%. El número estaba bien pero yo lo presenté sin aclarar eso, y leído junto a todo lo que veníamos hablando de "30% de margen" no cerraba. Mal ahí.

**Dato lindo:** si Pago Nube resulta cobrar solo sobre el producto (hipótesis B), **con +15% llegás justo al 30% de techo.**

**Un aumento del 15% en el precio es un aumento del 30% en tu margen bruto.** Es la palanca más poderosa que tenés, justamente porque tu costo es fijo en pesos.

---

## 4. Qué hace falta para 30% de margen neto

Con entregas solo los jueves (un viaje al proveedor por semana) y Meta a $150.000, escenario conservador (hipótesis A):

| Pedidos por jueves | Al mes | Aumento necesario | Ticket resultante | Margen bruto |
|---|---|---|---|---|
| 30 | 130 | **+29,9%** | $36.367 | 46,1% |
| 40 | 173 | **+26,7%** | $35.469 | 44,7% |
| 50 | 216 | **+24,7%** | $34.930 | 43,9% |
| 65 | 281 | **+23,0%** | $34.433 | 43,1% |
| 80 | 346 | **+21,9%** | $34.122 | 42,6% |

**Para 30% neto necesitás subir entre 22% y 30%**, según cuánto volumen tengas. Si la comisión resulta ser solo sobre el producto, restale unos 2 puntos a cada fila.

---

## 5. Escenario recomendado: +15%

No llega al 30% neto (o lo roza justo, si la comisión es solo sobre el producto), pero es un aumento que el cliente absorbe y te deja el negocio muy sano. Con **margen bruto 39,1%**, entregas solo los jueves, un viaje al proveedor por semana y Meta a $150.000. Fijos: $298.600/mes.

| Pedidos por despacho | Al mes | Facturación | Neto | Margen neto |
|---|---|---|---|---|
| 30 (el mínimo) | 130 | $4.182.780 | $908.444 | **21,7%** |
| 40 | 173 | $5.577.040 | $1.310.792 | 23,5% |
| 50 | 216 | $6.971.300 | $1.713.140 | 24,6% |
| 65 | 281 | $9.062.690 | $2.316.662 | 25,6% |
| 80 | 346 | $11.154.080 | $2.920.183 | 26,2% |

### La lista de precios con +15%

| Producto | Hoy | Con +15% |
|---|---|---|
| Pan de molde (blanco/integral/centeno) | $10.000 | **$11.500** |
| Pan de campo (blanco/integral/centeno) | $8.500 | **$9.800** |
| Pan árabe integral x5 | $8.500 | **$9.800** |
| Prepizzas x2 | $8.500 | **$9.800** |
| Grisines integrales | $5.000 | **$5.800** |
| Budín | $9.000 | **$10.400** |
| Pepas integrales | $7.000 | **$8.000** |
| Cookies integrales | $7.000 | **$8.000** |
| Promo Lanzamiento | $27.900 | **$32.100** |

**Si querés el 30% neto de una, el aumento es +25%** (pan de molde a $12.500, promo a $34.900). Es viable, pero es un salto grande para hacer de golpe. Mi recomendación sigue siendo +15% ahora, junto con la apertura del AMBA, y revisar en tres meses con datos reales.

---

## 6. Las palancas, ordenadas por impacto

1. **Subir precios.** Como tu costo es fijo en pesos, cada punto de aumento va casi entero a margen. +15% te lleva el bruto de 30% a 39,1%.
2. ~~Consolidar los viajes al proveedor.~~ ✅ **Hecho**: al pasar a solo jueves, de $260.000 a $86.600 mensuales.
3. **Descuento por transferencia (~4%).** Pago Nube se lleva 6%; con transferencia te ahorrás eso y ganás 2 puntos netos. Además cobrás al instante. **Y si la comisión pega también sobre el envío, te ahorrás todavía más.**
4. **Negociar con el proveedor.** Cada punto de margen bruto vale más que cualquier otra cosa.
5. **Bajar el packaging.** $1.000 por pedido son 3,6 puntos en un pedido de $28.000.
6. **Subir el ticket.** Con flete plano por pedido, cada peso adicional en la misma caja es casi ganancia pura.

---

## 7. El dato que sigue faltando

**¿Cuántos pedidos por mes estás haciendo hoy?** Sale de las estadísticas de Tiendanube.

Es lo único que falta para reemplazar estas tablas por tu escenario real y decirte exactamente a qué distancia estás del equilibrio y de los 30 por despacho.
