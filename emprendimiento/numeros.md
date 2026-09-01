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
