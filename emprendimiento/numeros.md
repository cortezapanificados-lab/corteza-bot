# Los números de Corteza

*Modelo definido el 10/08/2026. Punto de equilibrio rehecho el 28/08/2026 con el mínimo mensual de Flexit.*

---

## 1. El modelo, en una línea

> **Ganancia por pedido = venta × (margen bruto − 8%)**

Ese 8% son las dos cargas que se llevan un porcentaje de cada venta:

| Concepto | % de la venta |
|---|---|
| Comisión Pago Nube | 7% |
| Packaging | 1% |
| **Total** | **8%** |

Y aparte, los costos fijos del mes:

| Concepto | Por mes |
|---|---|
| Claude | $35.000 |
| Tiendanube | $27.000 |
| Envío del proveedor al almacén | $20.000 |
| **Total** | **$82.000** |

*(Más la publicidad en Meta cuando arranque.)*

> ⚠️ Los $20.000 del envío del proveedor están cargados como **costo mensual**. Si en realidad son por viaje, avisame: con un viaje semanal serían $86.600 y hay que rehacer las cuentas.

---

## 2. Tu margen bruto real

Calculado con los costos exportados de Tiendanube:

| | Margen bruto | Menos el 8% | **Te queda** |
|---|---|---|---|
| **Panificados propios** | 45,9% | −8% | **37,9%** |
| Catálogo completo | 36,7% | −8% | 28,7% |
| Solo terceros | 29,1% | −8% | 21,1% |

**Como los panificados son el grueso de lo que vendés, la referencia es 37,9%.** En un pedido de $28.000 eso son **$10.612** que quedan para cubrir los fijos y ganar.

El detalle producto por producto está en `tabla-margenes.md` y en el Excel.

---

## 3. Punto de equilibrio

> ### ⚠️ Rehecho el 28/08/2026: el mínimo de Flexit cambia estos números
>
> Flexit exige **120 envíos por mes**. Los que no uses, los pagás igual. En los hechos es **un costo fijo nuevo de $726.993 mensuales** — casi nueve veces los $82.000 que tenías. La cuenta ya no es "fijos ÷ contribución": cada pedido real, además de aportar margen, **cancela un envío fantasma**.
>
> **Equilibrio = (fijos + 120 × $6.058) ÷ (contribución por pedido + $6.058)**

| Presupuesto de Meta | Costos fijos | Antes | **Ahora (con el mínimo de 120)** | Por jueves |
|---|---|---:|---:|---:|
| $0 | $82.000 | 8/mes | **49/mes** | **11,2** |
| $60.000 | $142.000 | 13/mes | **52/mes** | **12,0** |
| $150.000 | $232.000 | 22/mes | **58/mes** | **13,3** |

**Con 13 pedidos por jueves cubrís todo, incluida una campaña de $150.000 mensuales.** Sigue siendo alcanzable, pero ya no arrancás cubriendo costos con 2 pedidos por semana: **abajo de ~11 por jueves, el mes da pérdida.**

**Y el objetivo real no es el equilibrio, son los 120.** Recién ahí el flete te sale lo que dice el tarifario ($6.058 por envío en vez de $12.117 con 60 pedidos). Detalle completo en `envios-amba.md`, sección 5.

---

## 3 bis. Septiembre: el mes de un solo despacho

*Agregado el 07/09/2026, con el lanzamiento movido al **jueves 24/9**.*

Septiembre queda con **un único despacho de AMBA**. El objetivo son **30 pedidos ese día**, y **Flexit cobra solo los envíos despachados** — el mínimo de 120 se ajusta a los días de despacho del mes.

> ⚠️ **Ojo con octubre**, que es el primer mes normal: tiene **5 jueves** y ahí el mínimo sí corre completo. Son 120 envíos = **$760.740 de flete fijo** (con el tarifario del 07/09), o sea **24 pedidos por jueves solo para no pagar envíos fantasma**. El equilibrio de octubre son **50 pedidos** (11,5 por jueves).

**Con 30 pedidos a $28.000 de ticket:**

| | |
|---|---:|
| Facturación | $840.000 |
| Contribución (37,9%) | $318.360 |
| Flete (30 × $6.340) | −$190.200 |
| Costos fijos del mes | −$82.000 |
| **Resultado antes de publicidad** | **+$46.160** |

**El equilibrio de septiembre son 20 pedidos** *(recalculado el 07/09 con el envío promedio de $6.340: Flexit actualizó las tarifas 4,6%)*. Con 30 el mes cierra en positivo, aunque ajustado: el margen real de un despacho único es chico porque los $82.000 de fijos se reparten entre un solo día.

*(La cuenta es conservadora: no computa lo que se le cobra de envío a los pedidos que quedan bajo el umbral de envío sin cargo. Tampoco incluye los pedidos de Pilar, que van por reparto propio y no pagan flete.)*

**Si además corrés el test de Meta de $120.000**, septiembre da **−$73.840**. Eso está bien y es lo esperable: la publicidad del mes de lanzamiento es inversión en la lista, no gasto del despacho. Lo que hay que mirar no es ese número, es **el costo por anotado**.

> ✅ **El mínimo de 120 no corre en septiembre.** Juan lo confirmó el 07/09: al haber un solo día de envío, Flexit cobra solo los pedidos despachados. El mínimo mensual empieza a aplicar con la operación normal, desde octubre.

---

## 4. Cuánto ganás según el volumen

Ticket promedio $28.000, Meta a $150.000/mes:

| Pedidos por jueves | Al mes | Facturación | Neto | Margen neto |
|---|---|---|---|---|
| 10 | 43 | $1.212.400 | $227.500 | 18,8% |
| 20 | 87 | $2.424.800 | $686.999 | 28,3% |
| **24** | 104 | $2.909.760 | **$870.799** | **29,9%** ✅ |
| **30** (≈ el mínimo de Flexit) | 130 | $3.637.200 | **$1.146.499** | **31,5%** |
| 40 | 173 | $4.849.600 | $1.605.998 | 33,1% |
| 50 | 216 | $6.062.000 | $2.065.498 | 34,1% |
| 65 | 281 | $7.880.600 | $2.754.747 | 35,0% |
| 80 | 346 | $9.699.200 | $3.443.997 | 35,5% |

### Las dos conclusiones

**1. Llegás al 30% de margen neto con 24 pedidos por jueves.**

**2. El mínimo de Flexit son 120 por mes (~28 por jueves), y ahí ya estás en el 31,5%.** O sea que **el día que llegues al mínimo, por definición estás por encima de tu objetivo del 30%.** El mínimo no es solo una exigencia: es la garantía de que el negocio cierra.

> *Actualizado el 28/08: la tabla de arriba se calculó con el mínimo de Smart Post (30 por jueves). Con el de Flexit (120 por mes) el resultado es prácticamente el mismo, porque 120/mes ≈ 28 por jueves. Lo que cambió de verdad es el punto de equilibrio, arriba.*

**Techo de margen neto: 37,9%.** Es el máximo al que tendés con mucho volumen.

---

## 5. Qué mover ahora

El precio ya no es la palanca: con 45,9% de margen bruto en los propios, estás bien. Lo que queda:

1. **Llegar a 24 pedidos por jueves.** Es el objetivo concreto y es alcanzable.
2. **Negociar los productos de terceros que están al 24%** (mermeladas, dulce de leche, yerba, pastas Contraviento). Todos son de Las Quinas y Contraviento.
3. **Descuento por transferencia (~5%)** para esquivar el 7% de Pago Nube. Es la carga más grande de las dos y la única que se puede evitar.
4. **Empujar los productos de mejor margen**: pan de molde blanco (52,2%) y aceite Zuelo (36,4%).
5. **Subir el ticket.** Con flete plano por pedido, cada peso adicional en la misma caja es casi ganancia pura.

---

## 6. Lo que falta

**¿Cuántos pedidos por jueves estás haciendo hoy?** Es el único dato que falta para saber a qué distancia estás de los 24.
