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

## 3 bis. Octubre: el mes del lanzamiento

*El lanzamiento pasó a octubre el 15/09/2026. **Esta sección reemplaza al escenario de septiembre**, que ya no corre.*

> ## 🔴 La pregunta más cara que hay abierta hoy
>
> **¿Cómo cobra Flexit el mínimo de 120 envíos en un mes en el que se arranca a mitad de camino?**
>
> En septiembre Juan confirmó que, con **un solo día de despacho**, Flexit cobraba solo lo despachado. **Octubre no es ese caso**: si se lanza el 8 o el 15 hay tres o cuatro despachos, o sea un mes casi normal. Hay tres respuestas posibles y la diferencia entre ellas es enorme:
>
> *(Lanzando el 8/10, con 4 despachos)*
>
> | Cómo cobre Flexit | Flete fijo del mes | **Equilibrio** | Por despacho |
> |---|---:|---:|---:|
> | Solo lo despachado *(como septiembre)* | variable | **16 pedidos** | 3,9 |
> | Prorrateado por días de despacho (96 envíos) | $608.640 | **50 pedidos** | 12,4 |
> | Los 120 completos | $760.800 | **60 pedidos** | 14,9 |
>
> **Entre la primera y la segunda hay 34 pedidos de diferencia.** No se puede fijar fecha de lanzamiento sin esa respuesta: es una llamada.

### El equilibrio según en qué jueves se lance

Octubre tiene **cinco jueves: 1, 8, 15, 22 y 29.** Asumiendo el caso del medio (mínimo prorrateado por días de despacho):

| Lanzás el | Despachos | Mínimo prorrateado | Flete fijo | Equilibrio | **Por despacho** |
|---|---:|---:|---:|---:|---:|
| 1/10 | 5 | 120 | $760.800 | 60 | **11,9** |
| 8/10 | 4 | 96 | $608.640 | 50 | **12,4** |
| **15/10** | **3** | **72** | **$456.480** | **39** | **13,1** |
| 22/10 | 2 | 48 | $304.320 | 29 | **14,7** |
| 29/10 | 1 | 24 | $152.160 | 19 | **19,2** |

> 💡 **El dato que más ordena: el equilibrio por despacho es casi plano, entre 12 y 15 pedidos, elijas el jueves que elijas.** El mínimo se prorratea junto con los despachos, así que lanzar antes o después casi no cambia cuántos pedidos hace falta por jueves. **Lo que sí cambia es la exposición total**: $760.800 de flete comprometido si se lanza el 1, contra $152.160 si se lanza el 29.

### Lo que cambia de fondo respecto del plan de septiembre

**En septiembre el riesgo estaba en un solo día. En octubre está en el segundo, el tercero y el cuarto.**

El plan de septiembre era un despacho único de 30 pedidos, y la lista de espera lo resolvía sola: de una lista compra el 15-25% en el primer aviso, y eso alcanzaba. **Con tres o cuatro despachos, la lista llena el primero y los siguientes necesitan demanda nueva.**

Es exactamente lo que ya advertía `campana-meta.md`: *"la publicidad de esta fase importa más en las semanas 2, 3 y 4 que en la 1; la primera semana la resuelve la lista, el riesgo real es caerse en los despachos siguientes."* **Ese riesgo pasó de ser teórico a ser el principal.**

### Lo que se gana con la postergación

1. **El test de Meta ahora sí tiene su ventana.** Necesita ~50 conversiones semanales por conjunto para salir de la fase de aprendizaje; con 9 días no llegaba, con cuatro semanas sí.
2. **Los influencers llegan a publicar antes del cierre.** Es el canal más barato (CAC de $4.500 a $13.500 por canje) y se había caído del calendario.
3. **La tienda se puede arreglar de verdad** — el inicio sin productos, el SEO, los sellos, las fotos.
4. **Hay un segundo par de manos.** Con Alva incorporado, las doce tareas que estaban trabadas por falta de tiempo dejan de estarlo.

### Lo que se pierde

**Septiembre iba a cerrar en +$124.600 con 30 pedidos y sin mínimo corriendo.** Ese mes "barato" —un despacho, cero envíos fantasma— no se repite: cualquier mes normal ya entra con el mínimo encima. Es el costo real de la postergación, y es el precio de llegar con la tienda y la publicidad listas en vez de a medias.

### La recomendación

> **Jueves 15 de octubre**, si Flexit confirma que el mínimo se prorratea.
>
> Cuatro semanas de preparación —suficiente para que Meta aprenda y los influencers publiquen—, **tres despachos para construir ritmo** en vez de jugarse todo a un día, y **$456.480 de flete comprometido en vez de $760.800**. El equilibrio son 39 pedidos, 13 por jueves.
>
> **Si Flexit responde que cobra los 120 completos igual, la fecha correcta pasa a ser el 29/10**: un solo despacho, mínimo de 24, equilibrio de 19 pedidos. Es reproducir el plan de septiembre un mes más tarde.

---

## 3 ter. Los dos extremos: el mejor y el peor pedido de $40.000

*Calculado el 11/09/2026, a pedido de Juan.*

**El ticket no dice nada por sí solo.** Dos pedidos de $40.000 pueden dejar $12.884 o **hacerte perder plata**, según qué lleven y adónde vayan.

### 🔴 El peor caso: zona Muy lejana con los productos de menor margen

| | |
|---|---:|
| 2 × Pasta de tomates secos Contraviento | $21.000 |
| 3 × Yerba orgánica Roapipó suave | $19.500 |
| **Total del pedido** | **$40.500** |

| | Monto | |
|---|---:|---:|
| Costo de la mercadería | −$28.620 | |
| **Margen bruto** | **$11.880** | 29,3% |
| Comisión Pago Nube (7%) | −$2.835 | |
| Packaging | −$500 | |
| Flete Muy lejana | −$9.580 | |
| **Resultado** | **−$1.035** | **−2,6%** |

**Ese pedido da pérdida.** Para empatar tendría que ser de **$45.200** con esa misma mezcla de productos.

### 🟢 El mejor caso: CABA con los panificados de mayor margen

| | |
|---|---:|
| 3 × Pan de molde blanco | $34.500 |
| 1 × Pepas integrales | $6.300 |
| **Total del pedido** | **$40.800** |

| | Monto | |
|---|---:|---:|
| Costo de la mercadería | −$20.000 | |
| **Margen bruto** | **$20.800** | 51,0% |
| Comisión Pago Nube (7%) | −$2.856 | |
| Packaging | −$500 | |
| Flete Cercana (CABA) | −$4.560 | |
| **Resultado** | **+$12.884** | **+31,6%** |

**Con 11 pedidos así al mes ya cubrís los $137.000 de costos fijos.** Con pedidos como el caso A no los cubrís nunca.

> **Entre los dos extremos hay $13.919 de diferencia, con la misma venta y el mismo trabajo.**

---

### 🧭 La regla que sale de acá: el margen bruto mínimo por zona

En un pedido de $40.000 con envío sin cargo, el margen bruto tiene que alcanzar para cubrir la comisión, el packaging y el flete de la zona:

| Zona | Flete | Hay que cubrir | **Margen bruto mínimo** |
|---|---:|---:|---:|
| **Pilar** (reparto propio) | — | $3.300 | **8,3%** |
| Cercana (CABA) | $4.560 | $7.860 | **19,7%** |
| Media | $6.385 | $9.685 | **24,2%** |
| Lejana | $8.210 | $11.510 | **28,8%** |
| **Muy lejana** | $9.580 | $12.880 | **32,2%** |

**Para comparar:** los panificados propios van de 43,5% a 52,2% — **pasan en todas las zonas con holgura.** El almacén de terceros va de 29,2% a 36,4%:

- En **CABA y Media** pasan todos, cómodos.
- En **Lejana** pasan todos, pero al filo: un pedido de $40.000 de pura yerba deja **$170**.
- En **Muy lejana** **solo pasan dos de los veinte**: el aceite Zuelo (36,4%) y las aceitunas negras (32,9%). **Los otros dieciocho dan pérdida si el pedido es solo de almacén.**

> ### ⚠️ Lo que hay que vigilar
>
> **El riesgo no es teórico**: un cliente de Escobar o La Plata que arma $40.000 de mermeladas, dips y yerba es un pedido perfectamente normal, y te hace perder plata.
>
> **No hace falta bloquearlo ni complicar la tienda.** Lo que hace falta es **mirarlo después del primer despacho**: si aparecen pedidos de almacén puro en zonas lejanas, las salidas son subir el umbral para esas dos zonas, o pedir un mínimo de panificados en el carrito. **Mientras el pan sea el grueso del pedido, el problema no existe** — y el pan es lo que la gente viene a comprar.

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
