# Envíos al AMBA: zonas, precios y umbrales

*Reescrito el 28/08/2026, cuando **Flexit pasó a ser la logística de Corteza**. Reemplaza toda la versión armada con las tarifas de Smart Post.*

> **Condición fiscal: Corteza es monotributista.** El IVA que paga por el flete **no se recupera**: es costo puro. Por eso todas las tarifas de acá están **con IVA al 10,5%**, que es la condición acordada con Flexit pagando en efectivo.

---

## 1. Las cuatro zonas de Flexit

**Atención: las zonas cambiaron de nombre y de contenido.** No son los cordones de Smart Post. Hay que cargarlas de cero en Tiendanube.

| Zona | Qué incluye |
|---|---|
| **Cercana** | Todos los barrios de Capital Federal |
| **Media** | Avellaneda, Hurlingham, Ituzaingó, Lanús, Lomas de Zamora, Morón, San Fernando, **San Isidro** (Beccar, Martínez, Acassuso), General San Martín, Tres de Febrero, Vicente López, La Matanza norte |
| **Lejana** | Almirante Brown, Berazategui, Esteban Echeverría, Ezeiza, Florencio Varela, José C. Paz, La Matanza sur, Malvinas Argentinas, Merlo, Moreno, Quilmes, San Miguel, **Tigre** (Nordelta) |
| **Muy lejana** | Berisso, Campana, Cañuelas, Del Viso, Derqui, Ensenada, Escobar, Garín, General Rodríguez, Guernica, Ingeniero Maschwitz, La Plata (Centro, Norte y Oeste), Luján, Marcos Paz, **Pilar**, San Vicente, Villa Rosa, Zárate |

---

## 2. Lo que te cuesta cada envío

| Zona | Sin IVA (tarifario) | **Costo real (IVA 10,5%)** |
|---|---:|---:|
| **Cercana (CABA)** | $3.942,10 | **$4.356** |
| **Media** | $5.522,10 | **$6.102** |
| **Lejana** | $7.102,10 | **$7.848** |
| **Muy lejana** | $8.287,10 | **$9.157** |

**Sigue valiendo la regla vieja: CABA es tu zona más barata y la más rentable para vender.** Y tu propia ciudad, Pilar, sigue siendo la banda más cara.

### Qué incluye la tarifa

✅ **Segunda y tercera visita incluidas en el precio.** Si el cliente no está, reintentan sin cobrarte. Con pan fresco y gente que trabaja, esto vale mucho.
✅ **Same-day**: se despacha el jueves y se entrega el jueves.
✅ **El IVA está por escrito** en el tarifario (a diferencia de Smart Post).
⚪ **Seguros opcionales** (0,5% en depósito, 0,7% en tránsito): **no tomarlos.** Sobre un pedido de $28.000 son $196 por envío para asegurar pan que, si se pierde, se repone.

### ⚠️ Lo que todavía NO está confirmado — y puede mover estos precios

Esto no es un detalle: **son las preguntas que hacen que la tarifa sea real o de folleto.** Están en `propuesta-flexit.md` con el texto listo para mandar.

1. **¿Cobran por peso real o volumétrico?** La caja de Corteza (45×35×30 cm) pesa **3 kg reales y 11,8 kg volumétricos**. Si cobran volumétrico, toda esta tabla se cae. **Es la pregunta más importante que queda.**
2. **¿Transportan panificados a temperatura ambiente?** Es lo que hizo caer a Shipnow.
3. **¿Hay volumen mínimo?** Si no lo hay, se cae la regla de los 150 anotados y el lanzamiento del 17/9 deja de depender de llenar la lista.
4. **¿Colectan en Pilar? ¿A qué hora y con qué costo?** Pilar les figura como zona Muy lejana: si cobran la colecta, puede salir caro.
5. **¿Hasta qué monto responden por un bulto perdido o dañado?** Casi todas las logísticas tienen un tope por bulto.
6. **¿La factura va a decir el total que se les paga, o solo una parte?**

---

## 3. Qué cobrarle de envío al cliente

Pago Nube se lleva su comisión de **todo** lo que cobrás, envío incluido. Si le cobrás al cliente exactamente lo que te cuesta el flete, esa comisión la ponés vos.

> **La fórmula es dividir por 0,93, no multiplicar por 1,07.** Si multiplicás, te quedás corto: la comisión también pega sobre el recargo.

### Precios de envío a cargar en Tiendanube

| Zona | Costo real | Exacto (÷0,93) | **A cobrar** |
|---|---:|---:|---:|
| **Cercana (CABA)** | $4.356 | $4.684 | **$4.700** |
| **Media** | $6.102 | $6.561 | **$6.600** |
| **Lejana** | $7.848 | $8.439 | **$8.500** |
| **Muy lejana** | $9.157 | $9.847 | **$9.900** |
| **Pilar** (reparto propio) | — | — | ver sección 5 |

Redondeados para arriba, así queda un colchoncito.

> ⚠️ **Queda una inconsistencia sin resolver:** `perfil.md` y `numeros.md` dicen que Pago Nube cobra **7%**, la versión vieja de este archivo usaba **6%**. Acá está calculado con **7%**, que es el número del modelo vigente y además el más conservador: si al final resulta ser 6%, te quedan unos $50 de más por envío y no al revés. **Chequealo en una liquidación real de Pago Nube.**

---

## 4. Los umbrales de envío sin cargo

Calculados con el **margen efectivo real del 37,9%** (45,9% de margen bruto en panificados menos el 8% de comisión y packaging).

> **Piso = costo del envío ÷ 0,379**

| Zona | Costo | Piso (ganás cero) |
|---|---:|---:|
| Cercana (CABA) | $4.356 | $11.493 |
| Media | $6.102 | $16.100 |
| Lejana | $7.848 | $20.707 |
| Muy lejana | $9.157 | $24.162 |

**Los pisos bajaron mucho respecto de la tabla vieja**, y no por Flexit: la tabla anterior estaba calculada con un margen del 24% que era una estimación desactualizada. Con el margen real de 37,9% podés ser bastante más generoso con el envío.

### Lo que te propongo ofrecer

| Zona | Qué ofrecer | Cliente paga | Te queda en el umbral |
|---|---|---:|---:|
| **Cercana (CABA)** | **Envío sin cargo desde $18.000** | $0 | $2.466 |
| **Media** | **Envío sin cargo desde $24.000** | $0 | $2.994 |
| **Lejana** | **Bonificamos $3.000 desde $28.000** | $5.500 | $7.612 |
| **Muy lejana** | **Bonificamos $3.000 desde $32.000** | $6.900 | $9.128 |
| **Pilar** (reparto propio) | **Envío sin cargo desde $18.000** | $0 | según tu costo real de reparto |

**Lo importante de este cambio: ahora podés ofrecer envío sin cargo en San Isidro, Beccar, Martínez, Acassuso y Vicente López** desde $24.000, que está por debajo de tu ticket promedio ($28.000). Antes eso era imposible. **Es la zona #1 del ranking de publicidad y ahora tiene la mejor oferta después de CABA.**

Y fijate que en las zonas con bonificación parcial ganás más que en CABA con envío gratis pleno. Ese es el punto: bonificar una parte te deja dar un beneficio real sin quedarte sin margen.

### Cuánto recargo ve el cliente

Es el número que decide si aprieta comprar o abandona el carrito:

| Zona | Envío | Sobre un pedido de $28.000 |
|---|---:|---:|
| Cercana (CABA) | $4.700 | **16,8%** |
| Media | $6.600 | 23,6% |
| Lejana | $8.500 | 30,4% |
| Muy lejana | $9.900 | **35,4%** |

**Arriba del 30% el envío espanta.** Por eso en Lejana y Muy lejana no se regala el envío: se empuja un pedido más grande.

---

## 5. Pilar: no va por Flexit

| | |
|---|---:|
| Ticket promedio en Pilar | $23.677 |
| Margen efectivo (37,9%) | **$8.974** |
| Flete de Flexit a Pilar (Muy lejana) | **−$9.157** |
| **Te queda** | **−$183** |

**Cada pedido de Pilar despachado por Flexit te daría pérdida.** Y cobrárselo al cliente tampoco funciona: $9.900 sobre un pedido de $23.677 es un **42% de recargo para que le lleven el pan a diez cuadras**. El vecino de Pilar sabe que sos de Pilar; no lo va a pagar.

> **Pilar sigue con reparto propio, y la tarea pendiente más rentable que queda es cotizar un cadete o moto local** para las ~18 entregas de los jueves. Ninguna logística del AMBA lo resuelve: para todas, Pilar es zona periférica.
>
> **Y falta el número que decide:** cuánto te cuesta hoy el reparto propio (nafta + horas + desgaste). Nunca se calculó.

**Ojo con una diferencia respecto de Smart Post:** con Smart Post existía el truco de "meter los pedidos de Pilar en los lugares ya pagados del mínimo de 30". **Con Flexit ese truco no existe** (o al menos no está confirmado que haya mínimo). Cada envío de Pilar cuesta $9.157 desde el primero.

---

## 6. Cómo comunicarlo

1. **El envío se muestra desde el principio**, nunca recién en el checkout.
2. **Mostrá siempre lo que falta:** *"Te faltan $4.200 para el envío sin cargo"*.
3. **Usá "envío sin cargo"**, no "envío gratis".
4. **Comunicá la bonificación parcial como beneficio:** *"Te bonificamos $3.000 del envío"*.
5. **Sugerí qué agregar** cuando falta poco. El tamaño de la caja no importa: mostrale lo que más margen te deje.
6. **En barrios cerrados, avisá antes de que pague** que la entrega es en la guardia — falta confirmar si Flexit entra o no.

---

## 7. Qué revisar cada mes

- ¿Cuántos pedidos por jueves?
- ¿Subió el ticket promedio?
- ¿Qué porcentaje de pedidos supera el umbral? Menos del 30% → muy alto. Más del 80% → muy bajo.
- ¿Qué porcentaje se pagó por transferencia?
- **¿Cambió el tarifario de Flexit?** Son tarifas mensuales ("vigentes septiembre") y están alineadas a los envíos Flex de ML. **Pedí el tarifario nuevo todos los meses** y recalculá esta tabla.

---

## 8. Lo que falta confirmar

1. 🔥 **Peso volumétrico** — la pregunta que define si estos precios son reales.
2. 🔥 **Panificados a temperatura ambiente** — eliminatoria.
3. **Volumen mínimo**, si lo hay.
4. **Horario y costo de la colecta en Pilar.**
5. **Tope de responsabilidad por bulto perdido o dañado.**
6. **Si integran con Tiendanube** y si la integración cotiza sola en el checkout.
7. **Si la factura cubre el total que se paga**, o solo una parte.
8. **Comisión real de Pago Nube: ¿6% o 7%?** Y si se aplica sobre producto + envío o solo sobre el producto.
9. **Costo real del reparto propio en Pilar.**
