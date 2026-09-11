# Los números de Corteza

*Modelo definido el 10/08/2026. **Rehecho por completo el 11/09/2026**, dos veces: primero con los costos corregidos (packaging $500 por pedido, flete de proveedores $75.000 por mes) y después con el **ticket promedio de $40.000**, el umbral del envío sin cargo.*

---

## 1. El modelo, en una línea

> **Ganancia por pedido = venta × (margen bruto − 7%) − $500 de packaging − el flete**

> 🔄 **Rehecho el 11/09/2026 con el ticket de $40.000.** Juan definió que **el pedido promedio se modela en $40.000, que es el umbral del envío sin cargo**. Eso cambia el modelo de raíz: **si el pedido promedio llega al umbral, el flete lo paga Corteza en casi todos los pedidos.** Ya no hay dos supuestos dando vueltas — el envío es un costo de Corteza y está adentro de la cuenta.

Las cargas de un pedido de $40.000:

| Concepto | Cómo se cobra | Monto | Sobre el pedido |
|---|---|---:|---:|
| Flete al cliente (Flexit) | por pedido, según zona; bonificado desde $40.000 | $6.340 | **15,9%** |
| Comisión Pago Nube | 7% de todo lo cobrado | $2.800 | 7,0% |
| Packaging | monto fijo por pedido | $500 | 1,25% |
| **Total** | | **$9.640** | **24,1%** |

*(El flete de $6.340 es el promedio ponderado de las cuatro zonas con la mezcla esperada: 40% CABA, 30% Media, 20% Lejana, 10% Muy lejana.)*

Y los costos fijos del mes:

| Concepto | Por mes |
|---|---:|
| **Flete de los proveedores al depósito** | **$75.000** |
| Claude | $35.000 |
| Tiendanube | $27.000 |
| **Total** | **$137.000** |

---

## 2. Qué deja un pedido de $40.000

| | Monto | % del pedido |
|---|---:|---:|
| Venta | $40.000 | 100% |
| Costo de la mercadería | −$21.640 | 54,1% |
| **Margen bruto** | **$18.360** | **45,9%** |
| Comisión Pago Nube | −$2.800 | 7,0% |
| Packaging | −$500 | 1,25% |
| **Antes del flete** | **$15.060** | **37,6%** |
| Flete promedio | −$6.340 | 15,9% |
| **Queda** | **$8.720** | **21,8%** |

### Lo que deja según la zona

| Zona | Flete | Queda | Margen | Mezcla |
|---|---:|---:|---:|---:|
| **Pilar** (reparto propio) | — | **$15.060** | **37,6%** | aparte |
| Cercana (CABA) | $4.560 | $10.500 | 26,2% | 40% |
| Media | $6.385 | $8.675 | 21,7% | 30% |
| Lejana | $8.210 | $6.850 | 17,1% | 20% |
| Muy lejana | $9.580 | $5.480 | 13,7% | 10% |

> 💡 **Un pedido de CABA deja casi el doble que uno de Escobar** ($10.500 contra $5.480) por la misma venta y el mismo trabajo. **Dónde se hace la publicidad es una decisión de margen, no de marketing.** Refuerza lo que ya decía `zonas-amba-ranking.md`.

El detalle producto por producto está en `tabla-margenes.md`.

---

## 3. Los dos regímenes: la clave de todo el modelo

**Flexit cobra un mínimo de 120 envíos por mes.** Los que no se usan, se pagan igual. Eso parte el negocio en dos situaciones con matemáticas completamente distintas:

| Situación | Qué cuesta el flete del pedido siguiente | Deja un pedido de $40.000 |
|---|---|---:|
| **Abajo de 120 pedidos/mes** | **nada** — ese envío ya está pagado por el mínimo | **$15.060 · 37,6%** |
| **Arriba de 120 pedidos/mes** | $6.340, el costo real | **$8.720 · 21,8%** |

### ✅ Por qué el umbral de $40.000 es la decisión correcta hoy

Mientras el mes no llegue a 120 pedidos —o sea, todo el horizonte visible— **los envíos ya están pagados igual**. En ese régimen:

| | Deja |
|---|---:|
| Pedido de $40.000 con envío bonificado | **$15.060** |
| Pedido de $28.000 con el cliente pagando el envío | $10.392 |
| **Diferencia** | **+$4.668** |

**El umbral se paga solo.** Empujar el carrito de $28.000 a $40.000 vale $4.668 por pedido mientras el flete sea un costo hundido.

### ⚠️ Y cuándo hay que volver a mirarlo

Pasados los 120 pedidos mensuales la cuenta **se da vuelta**: cada envío bonificado pasa a costar $6.340 de verdad.

| | Deja |
|---|---:|
| Pedido de $40.000 con envío bonificado | $8.720 |
| Pedido de $28.000 con el cliente pagando el envío | $10.392 |
| **Diferencia** | **−$1.672** |

> 🔴 **Con envío sin cargo en todos los pedidos, el margen neto del negocio tiene un techo de 21,8%** — por debajo del objetivo del 30%. **Para llegar al 30% por esta vía el ticket promedio tendría que ser de $77.000.**
>
> No es un problema de hoy y no invalida el umbral: hoy el umbral es claramente lo mejor. **Pero es la conversación que hay que tener al llegar al mínimo de Flexit**, y las salidas son tres: subir el umbral, dejar de bonificar el envío en las zonas lejanas, o subir precios.

---

## 3 bis. Septiembre: el mes de un solo despacho

*Rehecho el 11/09/2026 con el ticket de $40.000. Lanzamiento el **jueves 24/9**.*

Septiembre queda con **un único despacho de AMBA** y **sin mínimo**: Flexit cobra solo los envíos despachados.

**Con 30 pedidos a $40.000:**

| | |
|---|---:|
| Facturación | $1.200.000 |
| Costo de la mercadería | −$649.200 |
| **Margen bruto (45,9%)** | **$550.800** |
| Comisión Pago Nube (7%) | −$84.000 |
| Packaging (30 × $500) | −$15.000 |
| Flete Flexit (30 × $6.340) | −$190.200 |
| Costos fijos del mes | −$137.000 |
| **Resultado antes de publicidad** | **+$124.600** |

**El equilibrio de septiembre son 16 pedidos.** El objetivo de 30 lo casi duplica.

> 💡 **Comparado con el modelo de $28.000, septiembre pasa de −$15.440 a +$124.600.** Los $12.000 más de ticket compensan de sobra el flete que ahora paga Corteza — porque en un mes sin mínimo cada pedido paga un solo flete, pero trae $4.668 más de contribución.

**Con el test de Meta de $120.000**, septiembre da **+$4.600**. Prácticamente en cero, con la lista construida: es un buen resultado para un mes de lanzamiento.

> ⚠️ **Octubre es el primer mes normal**: 5 jueves y el mínimo de 120 corriendo, o sea **$760.800 de flete fijo**. Hay que cubrir $897.800 con una contribución de $15.060 por pedido → **el equilibrio de octubre son 60 pedidos (12 por jueves)**. Y para **usar** los 120 envíos que se pagan igual hacen falta **24 por jueves**.

---

## 4. Cuánto ganás según el volumen

Ticket $40.000, envío sin cargo, Meta a $150.000/mes. Hasta 120 pedidos el flete es el mínimo obligatorio; de ahí en más, el costo real de cada envío.

| Pedidos por jueves | Al mes | Facturación | Neto | Margen neto |
|---|---|---|---|---|
| 10 | 43 | $1.720.000 | −$400.220 | −23,3% |
| 15 | 65 | $2.600.000 | −$68.900 | −2,6% |
| **20** | 87 | $3.480.000 | **$262.420** | **7,5%** |
| **24** *(usa los 120 de Flexit)* | 104 | $4.160.000 | **$518.440** | **12,5%** |
| 30 | 130 | $5.200.000 | $846.600 | 16,3% |
| 40 | 173 | $6.920.000 | $1.221.560 | 17,7% |
| 50 | 216 | $8.640.000 | $1.596.520 | 18,5% |
| 65 | 281 | $11.240.000 | $2.163.320 | 19,2% |
| 80 | 346 | $13.840.000 | $2.730.120 | 19,7% |

### Las tres conclusiones

**1. Con 20 pedidos por jueves el mes ya es rentable.** Es un objetivo mucho más cercano que los 35 que pedía el modelo de $28.000.

**2. El salto grande está entre 15 y 24 por jueves**, porque ahí se llenan los 120 envíos que se pagan igual. Cada pedido que entra en esa franja es contribución casi pura.

**3. Pasados los 120, el margen se aplana en torno al 20%** y ya no mejora con volumen. La plata sigue creciendo fuerte (de $518.440 a $2.730.120), pero el porcentaje toca su techo.

**Techo de margen neto: 21,8%** con envío sin cargo en todos los pedidos. *(Sin bonificar el envío el techo sería 38,9%. Esos 17 puntos son literalmente el precio del envío sin cargo.)*

---

## 5. Qué mover ahora

El precio ya no es la palanca: con 45,9% de margen bruto en los propios, estás bien. Lo que queda, ordenado por lo que mueve:

1. **Llegar a 24 pedidos por jueves.** No es el equilibrio (son 12), es el punto donde **usás los 120 envíos que pagás igual**. Cada pedido hasta ahí es contribución casi pura.
2. **Empujar CABA en la publicidad.** Un pedido de CABA deja $10.500 y uno de Muy lejana $5.480. Con el mismo presupuesto de Meta, la zona decide el margen.
3. **Que los combos realmente lleguen a $40.000.** Todo el modelo cuelga de eso: si el ticket real queda en $30.000, el envío bonificado se come casi todo el margen del pedido.
4. **Negociar el flete de los proveedores.** Pasó a ser el fijo más grande ($75.000/mes). Cada $10.000 que bajes valen lo mismo que un pedido más por mes, todos los meses.
5. **Descuento por transferencia (~5%)** para esquivar el 7% de Pago Nube. Sobre $40.000 la comisión son $2.800: es la carga más grande después del flete y la única que se puede evitar.
6. **Comprar el packaging por cantidad.** A $500 fijos por pedido, con 120 pedidos son $60.000 mensuales.
7. **Empujar los productos de mejor margen**: pan de molde blanco (52,2%) y aceite Zuelo (36,4%).

## 6. Lo que falta

1. **¿Cuántos pedidos por jueves estás haciendo hoy?** Para saber a qué distancia estás de los 24.
2. **¿El ticket real va a llegar a $40.000?** Es el supuesto del que cuelga todo el modelo, y hoy el ticket relevado es $23.677. **Después del primer despacho del 24/9 hay que medirlo y rehacer estas cuentas con el número real.**
3. **¿Los $75.000 de flete de proveedores son con un viaje por semana?** Si el volumen obliga a dos viajes semanales, el número se va arriba de $150.000.
4. **¿Qué porcentaje de los pedidos queda debajo del umbral?** Cada uno de esos paga su propio envío y mejora el resultado. El modelo asume cero, que es lo más conservador.
