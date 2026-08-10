# Los números de Corteza

*Armado el 10/08/2026. Estructura de costos completa, punto de equilibrio y qué hace falta para llegar al margen que querés.*

> **Dos aclaraciones para leer este documento:**
> 1. Cada tabla dice con qué **margen bruto** está calculada. El 30% es solo a precios actuales: si subís precios, sube (sección 3).
> 2. De la sección 3 en adelante, todo asume el **recargo del 6,38% en el precio del envío** ya aplicado (sección 2).

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

### De dónde sale el 19,1% (y cómo lo arreglás)

Tu intuición dice: 30% de margen bruto, menos 6% de comisión, menos $1.000 de packaging (que es 3,6%) = **20,4%**. Esa cuenta está perfecta.

El 19,1% sale de un supuesto que no te había explicitado: **que Pago Nube cobra el 6% sobre todo lo que cobrás, incluido el envío.** El 6% de $34.265 son $2.056, que sobre los $28.000 de producto representan 7,3% en vez de 6%. Esos 1,3 puntos son toda la diferencia.

**Y la solución es la que propusiste vos: recargarle ese 6% al precio del envío.** Con eso el flete deja de costarte plata y el techo vuelve a los 20,4% que calculabas.

| | Techo de margen neto |
|---|---|
| Sin recargo en el envío | 19,1% |
| **Con el recargo aplicado** | **20,4%** |

> **El recargo correcto es 6,38%, no 6%** — hay que dividir por 0,94, porque la comisión también pega sobre el recargo. Los precios de envío a cargar están en `envios-amba.md`: $4.200 CABA, $6.700 Cordón 1, $8.800 Cordón 2 y 3.

**Lo que no cambia:** con margen bruto 30% el techo es 20,4% aun con el recargo, y no lo supera ningún volumen. Para pasar de ahí hay que subir precios.

### Punto de equilibrio a precios actuales

Con entregas **solo los jueves** → un viaje al proveedor por semana ($86.600/mes). Fijos base: **$148.600**. Con el recargo de envío aplicado, cada pedido deja $5.720.

| Meta | Costos fijos | Pedidos/mes para no perder | Por jueves |
|---|---|---|---|
| $0 | $148.600 | **26** | 6,0 |
| $60.000 | $208.600 | **36** | 8,4 |
| $150.000 | $298.600 | **52** | 12,1 |

---

## 3. El techo de margen neto, según el precio

**Con margen bruto 30% y el recargo de envío aplicado, el techo está en 20,4%.** Ningún volumen lo supera: los costos fijos se diluyen, pero la contribución por pedido como porcentaje de la venta no se mueve.

**Cualquier número mayor con margen bruto 30% es imposible.** Tenías razón en frenarme las dos veces.

### Pero el margen bruto no se queda en 30% si subís precios

Acá está la parte que no expliqué bien. **El proveedor te sigue cobrando lo mismo.** Si subís el precio y el costo no se mueve, todo el aumento va derecho a margen:

Con el recargo de envío ya aplicado:

| Precio | Aumento | Costo proveedor | **Margen bruto** | **Techo de margen neto** |
|---|---|---|---|---|
| $28.000 | — | $19.600 | **30,0%** | 20,4% |
| $30.800 | +10% | $19.600 | 36,4% | 27,1% |
| $32.200 | +15% | $19.600 | **39,1%** | **30,0%** ✅ |
| $33.600 | +20% | $19.600 | 41,7% | 32,7% |
| $35.000 | +25% | $19.600 | 44,0% | 35,1% |

**Con el recargo de envío y +15% de aumento, el techo llega justo al 30% que buscabas.** Las dos cosas juntas te ponen el objetivo al alcance.

**Un aumento del 15% en el precio es un aumento del 30% en tu margen bruto.** Es la palanca más poderosa que tenés, justamente porque tu costo es fijo en pesos.

---

## 4. Qué hace falta para 30% de margen neto

Con entregas solo los jueves (un viaje al proveedor por semana), Meta a $150.000 y el recargo de envío aplicado:

| Pedidos por jueves | Al mes | Aumento necesario | Ticket resultante | Margen bruto |
|---|---|---|---|---|
| 30 | 130 | **+27,8%** | $35.779 | 45,2% |
| 40 | 173 | **+24,6%** | $34.881 | 43,8% |
| 50 | 216 | **+22,7%** | $34.343 | 42,9% |
| 65 | 281 | **+20,9%** | $33.845 | 42,1% |
| 80 | 346 | **+19,8%** | $33.534 | 41,6% |

**Para 30% neto real necesitás subir entre 20% y 28%**, según el volumen. Con el recargo de envío bajó unos 2 puntos respecto del cálculo anterior.

---

## 5. Escenario recomendado: +15%

No llega al 30% neto exacto salvo con mucho volumen, pero es un aumento que el cliente absorbe y te deja el negocio muy sano. Con **margen bruto 39,1%**, entregas solo los jueves, un viaje al proveedor por semana y Meta a $150.000. Fijos: $298.600/mes.

| Pedidos por jueves | Al mes | Facturación | Neto | Margen neto |
|---|---|---|---|---|
| 30 (el mínimo) | 130 | $4.182.780 | $957.273 | **22,9%** |
| 40 | 173 | $5.577.040 | $1.375.898 | 24,7% |
| 50 | 216 | $6.971.300 | $1.794.522 | 25,7% |
| 65 | 281 | $9.062.690 | $2.422.459 | 26,7% |
| 80 | 346 | $11.154.080 | $3.050.395 | 27,3% |

### La lista de precios con +15%

*Corregida el 10/08/2026 contra los precios reales de la tienda, que eran más bajos que los que estaban anotados en la memoria.*

**Solo panificados propios.** A los productos de terceros no se les aplica (ver más abajo).

| Producto | Hoy | Con +15% |
|---|---|---|
| Pan de molde (blanco/integral/centeno) | $10.000 | **$11.500** |
| Hogaza | $10.000 | **$11.500** |
| Pan de campo (blanco/integral/centeno) | $7.500 | **$8.600** |
| Pan árabe integral x5 | $7.500 | **$8.600** |
| Prepizzas x2 | $7.000 | **$8.000** |
| Budín | $7.000 | **$8.000** |
| Cookies integrales | $6.000 | **$6.900** |
| Pepas integrales | $5.500 | **$6.300** |
| Grisines integrales | $4.000 | **$4.600** |
| Promo Lanzamiento | $25.000 | **$28.900** |

### A los productos de terceros nunca se les aplica el aumento

Es la distinción más importante de toda la política de precios. Con los panificados propios tenés poder de precio porque nadie puede comparar tu curaduría. Con una mermelada Las Quinas o un Malbec de Luigi Bosca, **el cliente googlea y compara en dos segundos.**

El relevamiento del 10/08/2026 encontró que **varios ya estaban por encima del mercado** — hasta 20% en las mermeladas y el dulce de leche. Eso no te hace ganar más: te instala fama de tienda cara y te contamina la percepción del pan, que es donde de verdad ganás.

Se bajaron seis productos a **mercado +10%**, que es un premium defendible para una tienda curada con entrega a domicilio. El detalle producto por producto está en `perfil.md`.

**Regla para el futuro: cuando subas precios, subí solo los propios. Los de terceros se revisan contra el mercado, no contra tus costos.**

**Si querés el 30% neto de una y apuntás a 50 pedidos por jueves, el aumento es +23%** (pan de molde a $12.300, promo a $34.300). Es viable, pero es un salto grande para hacer de golpe. Mi recomendación sigue siendo +15% ahora, junto con la apertura del AMBA, y revisar en tres meses con datos reales — con el recargo de envío ya aplicado, el 15% te deja muy cerca.

---

## 6. Las palancas, ordenadas por impacto

1. **Subir precios.** Como tu costo es fijo en pesos, cada punto de aumento va casi entero a margen. +15% te lleva el bruto de 30% a 39,1%.
2. ~~Consolidar los viajes al proveedor.~~ ✅ **Hecho**: al pasar a solo jueves, de $260.000 a $86.600 mensuales.
3. ✅ **Recargar el 6,38% en el precio del envío** — ya definido, te devuelve 1,3 puntos.
4. **Descuento por transferencia (~4%).** Pago Nube se lleva 6%; con transferencia te ahorrás eso y ganás 2 puntos netos. Además cobrás al instante. **Y si la comisión pega también sobre el envío, te ahorrás todavía más.**
5. **Negociar con el proveedor.** Cada punto de margen bruto vale más que cualquier otra cosa.
6. **Bajar el packaging.** $1.000 por pedido son 3,6 puntos en un pedido de $28.000.
7. **Subir el ticket.** Con flete plano por pedido, cada peso adicional en la misma caja es casi ganancia pura.

---

## 7. El dato que sigue faltando

**¿Cuántos pedidos por mes estás haciendo hoy?** Sale de las estadísticas de Tiendanube.

Es lo único que falta para reemplazar estas tablas por tu escenario real y decirte exactamente a qué distancia estás del equilibrio y de los 30 por despacho.
