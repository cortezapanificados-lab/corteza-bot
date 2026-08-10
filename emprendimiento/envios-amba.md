# Envíos al AMBA y mínimos de compra

*Armado el 10/08/2026. Cómo definir a partir de qué monto Corteza regala el envío, sin regalar la ganancia.*

---

## 1. Primero, la idea de fondo

El envío gratis es la herramienta de venta más poderosa que tiene una tienda online. **El costo de envío es la principal razón por la que la gente arma el carrito y después no compra.** Así que el mínimo de compra no es un gasto: es lo que te empuja el ticket para arriba.

Pero tiene una trampa: si el mínimo está mal puesto, o regalás plata que ibas a ganar igual, o ponés una zanahoria tan lejos que nadie la intenta.

El número correcto vive entre dos límites. Hay que calcular los dos.

---

## 2. El dato que falta y sin el cual esto no se puede cerrar

**Tu margen bruto.** Es el único número que no tengo y del que depende todo.

Como Corteza compra a proveedores y revende, se calcula así:

> **Margen = (lo que cobrás − lo que te costó) ÷ lo que cobrás**

Ejemplo con un pan de campo a $8.500:
- Si te lo deja el proveedor a $5.500 → ganás $3.000 → margen = 3.000 ÷ 8.500 = **35%**
- Si te lo deja a $6.500 → ganás $2.000 → margen = 2.000 ÷ 8.500 = **24%**

Sacá el margen de tus 5 o 6 productos más vendidos y promedialo. Con ese número entrás a las tablas de abajo. Mientras tanto, en los ejemplos uso **35%**, que es un supuesto razonable para reventa — pero es un supuesto, hay que reemplazarlo por el tuyo.

---

## 3. El piso: abajo de acá perdés plata

Cuando regalás el envío, ese costo sale de tu ganancia. Entonces el pedido tiene que ser lo bastante grande como para que la ganancia alcance a pagar el envío.

> **Piso = costo del envío ÷ tu margen**

Con margen 35% y un envío de $8.000: $8.000 ÷ 0,35 = **$22.900**.

Eso significa que en un pedido de $22.900 con envío bonificado, **ganás exactamente cero.** Toda tu ganancia se fue en el flete. Por eso el piso no es el umbral: es el punto donde empezás a no perder.

**Al piso sumale un 40%** para que el pedido te deje ganancia de verdad.

### Tabla del piso (dónde ganás cero)

| Costo del envío | Margen 25% | Margen 30% | Margen 35% | Margen 40% |
|---|---|---|---|---|
| $5.000 | $20.000 | $16.700 | $14.300 | $12.500 |
| $7.000 | $28.000 | $23.300 | $20.000 | $17.500 |
| $9.000 | $36.000 | $30.000 | $25.700 | $22.500 |
| $11.000 | $44.000 | $36.700 | $31.400 | $27.500 |
| $13.000 | $52.000 | $43.300 | $37.100 | $32.500 |

Buscá tu margen en la columna y el costo de envío en la fila. Ese es tu piso. **Nunca pongas el umbral por debajo de ese número.**

---

## 4. El techo: arriba de acá nadie llega

Acá entra el comportamiento del cliente, no la contabilidad.

La regla que funciona en ecommerce es que **el umbral tiene que estar entre un 20% y un 40% por encima de tu ticket promedio.** Ni más ni menos, y por razones distintas:

- **Si lo ponés igual o abajo del ticket promedio**: regalás envíos que la gente iba a pagar igual. Plata tirada.
- **Si lo ponés muy arriba**: el cliente hace la cuenta, ve que le falta un montón, se resigna y compra lo mínimo pagando el envío. La zanahoria dejó de funcionar.
- **Si lo ponés un poco arriba**: el cliente piensa "me faltan $6.000, agrego una mermelada y me ahorro el envío". **Ese es el efecto que buscás.** Y encima te comprás un cliente que probó un producto nuevo.

> **Techo = tu ticket promedio × 1,4**

Fijate el ticket promedio real en las estadísticas de Tiendanube. Por lo que muestra la tienda, deberías estar en el orden de los $25.000–$30.000, pero confirmalo con el dato real.

---

## 5. Qué hacer cuando el piso queda más arriba que el techo

Esto te va a pasar en las zonas más lejanas y es la parte importante de todo este documento.

Si en una zona el envío te sale $13.000 y tu margen es 30%, el piso es $43.300. Pero si tu ticket promedio es $28.000, el techo es $39.000. **El piso quedó arriba del techo: no hay ningún número que funcione.**

Eso no es un problema de cálculo. Es el sistema avisándote algo real: **en esa zona no podés regalar el envío.** Tenés tres salidas:

1. **No ofrecer envío gratis ahí.** El comprador paga el flete completo, y listo. Es una opción totalmente válida y honesta.
2. **Bonificar una parte, no todo.** "A partir de $32.000 te bonificamos $6.000 del envío." Suena bien, empuja el ticket igual, y vos absorbés solo lo que te cierra.
3. **Revisar el precio en esa zona.** Es lo que hacen casi todas las tiendas: los precios contemplan el flete. No lo recomiendo por ahora, complica todo.

**Mi recomendación: la opción 2.** Bonificación parcial en las zonas lejanas, envío gratis pleno en las cercanas.

---

## 6. La estructura que te propongo

Tres bandas. Tiendanube te deja configurar zonas de envío con un mínimo distinto para cada una, así que esto es armable sin complicación.

Los costos de envío de abajo son **placeholders**: reemplazalos por la tarifa real de tu empresa de logística por zona. Los umbrales están calculados con margen 35%.

| Banda | Zonas | Costo envío (a confirmar) | Umbral envío gratis |
|---|---|---|---|
| **1 — Pilar** | Pilar y alrededores | $5.000 | **$25.000** (se mantiene) |
| **2 — AMBA cercano** | Escobar, Tigre, San Fernando, San Isidro, Vicente López, San Miguel, José C. Paz, Malvinas Argentinas, Moreno, Gral. Rodríguez | ~$8.000 | **$32.000** |
| **3 — CABA y resto del AMBA** | CABA, Oeste y Sur | ~$11.000–13.000 | **Bonificación parcial**: desde $35.000 se bonifican $6.000 del envío |

El umbral de Pilar de $25.000 que ya tenés está bien puesto — no lo toques. Con margen 35% el piso ahí es $14.300, así que te queda ganancia cómoda.

---

## 7. Cómo comunicarlo (esto importa tanto como el número)

**1. El envío se muestra desde el principio, nunca recién en el checkout.** La sorpresa de flete al final es lo que más carritos mata. Poné un calculador de envío en la página del producto.

**2. Mostrá siempre lo que falta.** Tiendanube tiene una barrita para esto y es de lo que más convierte:

> 🚚 *Te faltan $4.200 para el envío sin cargo*

**3. Usá "envío sin cargo", no "envío gratis".** Suena menos a promoción barata y más acorde a tu marca.

**4. Cuando falta poco, sugerí qué agregar.** Si al cliente le faltan $5.000, mostrale productos de ese precio: la yerba a $6.600, el hummus a $5.200, un té a $5.200. Le resolvés la decisión.

**5. Nunca hagas descuento en vez de envío.** "Envío sin cargo" convierte muchísimo más que "$8.000 de descuento", aunque sea la misma plata para vos. La gente odia pagar el flete de una manera que no odia pagar el producto.

---

## 8. Qué revisar a los 30 días de lanzar

- **¿Subió el ticket promedio?** Es lo que tiene que pasar. Si no se movió, el umbral está mal puesto.
- **¿Qué porcentaje de pedidos llega al umbral?** Si es menos del 30%, está muy alto. Si es más del 80%, está muy bajo y estás regalando plata.
- **¿De qué zonas te compran?** Si una banda no vende nada, revisá si el problema es el flete.
- **¿Cuánto te está costando en total la bonificación de envíos?** Que sea un número que mires todos los meses, no una sorpresa.

---

## 9. Pendiente para cerrar esto

Con estos dos datos te dejo la tabla final con los números definitivos:

1. **Tu margen bruto promedio** (sección 2).
2. **La tarifa real de tu empresa de logística por zona.**

Y un tercero que ayuda: **el ticket promedio actual**, que sale de las estadísticas de Tiendanube.
