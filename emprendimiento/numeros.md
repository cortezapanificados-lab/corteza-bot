# Los números de Corteza

*Modelo definido el 10/08/2026. **Rehecho por completo el 11/09/2026** con los dos costos corregidos por Juan: packaging $500 por pedido y flete de proveedores $75.000 por mes.*

---

## 1. El modelo, en una línea

> **Ganancia por pedido = venta × (margen bruto − 7%) − $500**

> 🔄 **Corregido el 11/09/2026.** Juan pasó los dos costos reales y ninguno estaba bien cargado:
> **el packaging son $500 fijos por pedido** (venía como 1% de la venta) y **el flete de los proveedores al depósito son $75.000 por mes** (venía como $20.000). Todas las cuentas de abajo están rehechas con eso.

Las cargas por pedido:

| Concepto | Cómo se cobra | En un ticket de $28.000 |
|---|---|---:|
| Comisión Pago Nube | 7% de todo lo cobrado, envío incluido | $1.960 |
| Packaging | **monto fijo por pedido**, no porcentaje | $500 |
| **Total** | | **$2.460 (8,8%)** |

> ⚠️ **El packaging es fijo, y eso cambia cómo se lee.** En un pedido de $28.000 pesa 1,8%; en uno de $10.000 pesa 5%. **Los pedidos chicos son proporcionalmente más caros de empacar** — un argumento más a favor de los combos y del umbral de $40.000.

Y aparte, los costos fijos del mes:

| Concepto | Por mes |
|---|---:|
| **Flete de los proveedores al depósito** | **$75.000** |
| Claude | $35.000 |
| Tiendanube | $27.000 |
| **Total** | **$137.000** |

*(Más la publicidad en Meta cuando arranque.)*

> 💡 **El flete de proveedores es ahora el costo fijo más grande del negocio: más que Claude y Tiendanube juntos.** Son $55.000 mensuales más de lo que estaba anotado. La buena noticia es que **es fijo**: no crece con las ventas, así que se diluye con volumen. Repartido entre 30 pedidos son $2.500 por pedido; entre 120, $625.

---

## 2. Tu margen bruto real

Calculado con los costos exportados de Tiendanube:

| | Margen bruto | Menos comisión 7% | Menos $500 de packaging | **Te queda** |
|---|---|---|---|---|
| **Panificados propios** | 45,9% | 38,9% | −1,8% | **37,1%** |
| Catálogo completo | 36,7% | 29,7% | −1,8% | 27,9% |
| Solo terceros | 29,1% | 22,1% | −1,8% | 20,3% |

*(La columna del packaging asume el ticket de $28.000. En pedidos más chicos pesa más.)*

**Como los panificados son el grueso de lo que vendés, la referencia es 37,1%.** En un pedido de $28.000 eso son **$10.392** que quedan para cubrir los fijos y ganar. *(Antes de la corrección del 11/09 esta cifra era $10.612: la diferencia por pedido es chica, lo que pega fuerte son los $55.000 mensuales del flete.)*

El detalle producto por producto está en `tabla-margenes.md` y en el Excel.

---

## 3. Punto de equilibrio

> ⚠️ **Antes de leer los números: hay dos supuestos distintos de envío dando vueltas en esta memoria y conviene elegir uno.**
>
> La tabla A de abajo asume que **el envío lo paga el cliente** (que es la regla general). La tabla B y el escenario de septiembre asumen que **lo paga Corteza**, que es lo que pasa arriba de $40.000 y en Pilar. **Con el umbral de envío sin cargo en $40.000 y los combos armados justamente para llegar ahí, la verdad va a estar en el medio.** Falta definir qué porcentaje de los pedidos va a superar el umbral: es el dato que cierra el modelo.

### A. Si el envío lo paga el cliente

Equilibrio = fijos ÷ $10.392 de contribución.

| Presupuesto de Meta | Costos fijos | **Equilibrio** | Por jueves |
|---|---:|---:|---:|
| $0 | $137.000 | **14/mes** | **3,2** |
| $60.000 | $197.000 | **19/mes** | **4,4** |
| $150.000 | $287.000 | **28/mes** | **6,5** |

*(Antes de la corrección del 11/09 eran 8, 13 y 22.)*

### B. Con el mínimo de 120 envíos de Flexit corriendo

Flexit exige **120 envíos por mes** en un mes de operación normal. Los que no uses, los pagás igual: son **$760.800 de flete fijo** con el tarifario del 07/09. La cuenta ya no es "fijos ÷ contribución": cada pedido real, además de aportar margen, **cancela un envío fantasma**.

> **Equilibrio = (fijos + 120 × $6.340) ÷ $10.392**

| Presupuesto de Meta | A cubrir | **Equilibrio** | Por jueves (mes de 5) |
|---|---:|---:|---:|
| $0 | $897.800 | **87/mes** | **17,4** |
| $60.000 | $957.800 | **93/mes** | **18,5** |
| $150.000 | $1.047.800 | **101/mes** | **20,2** |

> ⚠️ **Estos números no coinciden con los que estaban anotados el 28/08 (49, 52 y 58 por mes) y la diferencia no es solo por los costos corregidos.** Rehaciendo la cuenta con la fórmula que la propia memoria enunciaba, y aun con los fijos viejos de $82.000, daba 76 pedidos, no 49. **La tabla de agosto tenía un error de cálculo.** La de acá arriba es la buena.

**El objetivo real no es el equilibrio, son los 120.** Recién ahí el flete te sale lo que dice el tarifario ($6.340 por envío en vez del doble con 60 pedidos). Detalle completo en `envios-amba.md`, sección 5.

---

## 3 bis. Septiembre: el mes de un solo despacho

*Agregado el 07/09/2026, rehecho el 11/09/2026 con los costos corregidos. Lanzamiento el **jueves 24/9**.*

Septiembre queda con **un único despacho de AMBA**. El objetivo son **30 pedidos ese día**, y **Flexit cobra solo los envíos despachados** — el mínimo de 120 se ajusta a los días de despacho del mes.

**Con 30 pedidos a $28.000 de ticket:**

| | |
|---|---:|
| Facturación | $840.000 |
| Costo de la mercadería | −$454.440 |
| **Margen bruto (45,9%)** | **$385.560** |
| Comisión Pago Nube (7%) | −$58.800 |
| Packaging (30 × $500) | −$15.000 |
| Flete Flexit (30 × $6.340) | −$190.200 |
| Costos fijos del mes | −$137.000 |
| **Resultado antes de publicidad** | **−$15.440** |

> ⚠️ **Septiembre pasa de +$46.160 a −$15.440.** No cambió nada del producto: los márgenes de la mercadería están igual de bien. Lo que cambió son los $55.000 extra de flete de proveedores. **Un mes con un solo día de despacho tiene que bancar los fijos completos con 30 pedidos, y no le alcanza por poco.**

**El equilibrio de septiembre son 34 pedidos** (antes 21). Son 4 pedidos más que el objetivo: **la pérdida se da vuelta con muy poco.**

*(La cuenta es conservadora: no computa lo que se le cobra de envío a los pedidos que quedan bajo el umbral de $40.000. Tampoco incluye los pedidos de Pilar, que van por reparto propio y no pagan flete. Con esos dos ajustes el mes probablemente cierre en cero o levemente positivo.)*

> ⚠️ **Ojo con octubre**, que es el primer mes normal: tiene **5 jueves** y ahí el mínimo de 120 corre completo — **$760.800 de flete fijo**, o sea **24 pedidos por jueves solo para no pagar envíos fantasma**. El equilibrio de octubre son **87 pedidos** (17,4 por jueves).

**Si además corrés el test de Meta de $120.000**, septiembre da **−$135.440**. Eso está bien y es lo esperable: la publicidad del mes de lanzamiento es inversión en la lista, no gasto del despacho. Lo que hay que mirar no es ese número, es **el costo por anotado**.

> ✅ **El mínimo de 120 no corre en septiembre.** Juan lo confirmó el 07/09: al haber un solo día de envío, Flexit cobra solo los pedidos despachados. El mínimo empieza a aplicar con la operación normal, desde octubre.

---

## 4. Cuánto ganás según el volumen

Ticket promedio $28.000, Meta a $150.000/mes, **asumiendo que el envío lo paga el cliente** (supuesto A de la sección 3):

| Pedidos por jueves | Al mes | Facturación | Neto | Margen neto |
|---|---|---|---|---|
| 10 | 43 | $1.204.000 | $159.856 | 13,3% |
| 20 | 87 | $2.436.000 | $617.104 | 25,3% |
| 24 | 104 | $2.912.000 | $793.768 | 27,3% |
| **30** | 130 | $3.640.000 | **$1.063.960** | **29,2%** |
| **35** | 152 | $4.256.000 | **$1.292.584** | **30,4%** ✅ |
| 40 | 173 | $4.844.000 | $1.510.816 | 31,2% |
| 50 | 216 | $6.048.000 | $1.957.672 | 32,4% |
| 65 | 281 | $7.868.000 | $2.633.152 | 33,5% |
| 80 | 346 | $9.688.000 | $3.308.632 | 34,2% |

### Las dos conclusiones

**1. El 30% de margen neto llega cerca de los 35 pedidos por jueves**, no de los 24 que decía la tabla vieja. Los $55.000 extra de flete de proveedores corrieron la meta unos 11 pedidos por jueves.

**2. El mínimo de Flexit (120 por mes, ~28 por jueves) ya no alcanza por sí solo para el 30%**, aunque queda cerca: a 30 por jueves el negocio rinde 29,2%. **El mínimo dejó de ser la garantía de que el negocio cierra y pasó a ser el piso desde el cual empieza a rendir.**

**Techo de margen neto: 38,9%** (45,9% de margen bruto menos el 7% de comisión). Es el máximo al que tendés con mucho volumen, cuando el packaging y los fijos se vuelven insignificantes.

---

## 5. Qué mover ahora

El precio ya no es la palanca: con 45,9% de margen bruto en los propios, estás bien. Lo que queda:

1. **Llegar a 35 pedidos por jueves.** Es el nuevo objetivo para el 30% neto. A 30 por jueves ya estás en 29,2%, así que no está lejos.
2. **Negociar el flete de los proveedores.** Pasó a ser el fijo más grande del negocio ($75.000/mes). Cada $10.000 que bajes valen lo mismo que un pedido más por mes, todos los meses.
3. **Descuento por transferencia (~5%)** para esquivar el 7% de Pago Nube. Es la carga más grande y la única que se puede evitar.
4. **Comprar el packaging por cantidad.** A $500 fijos por pedido, con 120 pedidos son $60.000 mensuales — casi lo mismo que el flete de proveedores.
5. **Empujar los productos de mejor margen**: pan de molde blanco (52,2%) y aceite Zuelo (36,4%).
6. **Subir el ticket.** Con flete plano por pedido, cada peso adicional en la misma caja es casi ganancia pura. Y como el packaging también es fijo por pedido, un ticket más alto lo diluye dos veces.

---

## 6. Lo que falta

1. **¿Cuántos pedidos por jueves estás haciendo hoy?** Para saber a qué distancia estás de los 35.
2. **¿Qué porcentaje de los pedidos va a superar los $40.000?** Es lo que define si el envío lo paga el cliente o Corteza, y es la diferencia entre las dos tablas de equilibrio de la sección 3. Sin ese dato el modelo tiene dos respuestas.
3. **¿Los $75.000 de flete de proveedores son con un viaje por semana?** Si el volumen obliga a dos viajes semanales, el número se va arriba de $150.000 y hay que rehacer todo de nuevo.
