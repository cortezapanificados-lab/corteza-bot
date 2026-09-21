# Suscripciones

*Diseño definido el 17/09/2026.*

> ## 🎯 La recomendación: **arrancar con UN solo pack suscribible — el Pack Semanal** — con parte fija y parte que rota.

---

## 1. Por qué uno solo, y por qué ése

**Los cinco packs no son igual de suscribibles. La mayoría no lo es.** Esto es lo que recibiría el cliente **al mes** si se suscribe a cada uno:

| Pack | Lo que llega al mes | ¿Aguanta semanal? |
|---|---|---|
| **Semanal** | 4 prepizzas · 4 molde integral · 4 grisines · 4 budines · 4 pepas · 4 cookies | ✅ **Sí** |
| Familiar | 4+4 panes de molde · 8 prepizzas · 8 grisines · **8 pepas · 8 cookies** | ⚠️ 16 paquetes de galletitas al mes |
| Kids | 4 prepizzas · **12 cookies** · 4 budines · 4 pepas | ❌ 12 cookies al mes |
| Antojito | 4 panes de campo · **4 dulces de leche** · 4 budines · 8 cookies · 4 pepas | ❌ ¿un dulce de leche por semana? |
| Para picar | 8 hogazas · **4 quesos · 4 hummus · 4 aceitunas** | ❌ y encima el riesgo de frío se repite todas las semanas |

> **La fatiga es lo que mata las suscripciones de comida**, y se nota apenas se multiplica por cuatro. **El único pack cuyo contenido es genuinamente de consumo semanal es el Semanal** — el nombre ya lo decía.

**Las otras cuatro razones para arrancar con uno:**

1. **Se comunica en una frase.** *"Suscribite al Pack Semanal y te llega todos los jueves con 5% de descuento."* Cinco planes con elección es parálisis de decisión, justo en el momento en que el cliente no te conoce.
2. **$181.200 al mes es un ticket creíble** para una casa. El Familiar como suscripción son **$298.400 mensuales**: es mucha plata para pan, y ya estaba anotado que el plan caro sirve de ancla, no de producto.
3. **Menos carga el jueves a la mañana**, que es el cuello de botella de toda la operación.
4. **Con un solo plan se aprende.** Si lanzás cinco y funciona uno, no vas a saber si fue por el pack, por el precio o por el cliente.

---

## 2. La vuelta de tuerca que resuelve la fatiga: parte fija + parte que rota

> ### El pan es siempre el mismo. Lo dulce cambia cada semana.

| | Qué va |
|---|---|
| **Fijo, todas las semanas** | Pan de molde integral · prepizzas x2 · grisines |
| **Rota** | Una cosa dulce: cookies / mix pepas / budín |

**Rotar no cuesta margen:** cookies 44,9%, pepas 44,4%, budín 43,8% — están los tres en la misma banda.

Y resuelve dos cosas de un saque:

1. **Mata la fatiga.** El cliente no recibe lo mismo cuatro veces al mes.
2. **Te da aire cuando un proveedor no llegó con algo.** Es la ventaja que ya estaba anotada: *"armás con lo que mejor margen tiene y con lo que el productor realmente consiguió. Nunca quedás vendiendo algo que no tenés."*

**Y se comunica como beneficio, no como limitación:** *"Todas las semanas el pan de la casa, y algo dulce distinto."*

---

## 3. Los números

| | |
|---|---:|
| Precio semanal | $45.300 |
| **Al mes (4 entregas)** | **$181.200** |
| Con 5% de descuento | $172.140 |
| Margen bruto del pack | 45,3% |
| **Deja por mes, por suscriptor, en CABA** | **$40.650** |
| El 5% cuesta, por suscriptor por mes | $8.426 |

**El descuento se paga tres veces.** Asegura 4 envíos del mínimo de Flexit, que valen **$25.360** si quedan sin usar, contra los $8.426 que cuesta.

| Suscriptores | Envíos/mes | Del mínimo de 120 | Facturación asegurada |
|---:|---:|---:|---:|
| 10 | 40 | 33% | $430.350 |
| 20 | 80 | 67% | $860.700 |
| **30** | **120** | **100%** | **$1.291.050** |

**Treinta suscriptores cubren el mínimo entero de Flexit sin vender nada más.**

---

## 3 bis. 📦 El envío en las zonas lejanas *(definido el 18/09/2026)*

> ### El Pack Semanal son $45.300 por entrega, o sea **por debajo del umbral de $55.000**. En Lejana y Muy lejana el suscriptor paga los $5.000 de envío, como cualquier otro pedido.
>
> *(Decidido por Juan el 18/09, junto con el umbral de $55.000 — `envios-amba.md` sección 3 quater.)*

**El 5% de descuento es sobre el producto, no sobre el envío.**

### 🔴 La trampa que hay que esquivar al cargarlo

La suscripción se cobra **un mes por adelantado en una sola transferencia**, así que **el carrito dice $172.140, no $45.300**. Y Tiendanube calcula el envío sobre el total del carrito.

> **Con la regla de "sin cargo desde $55.000", ese carrito la dispara solo y no cobra ni un peso de envío.** Y encima **ese carrito es un pedido pero son cuatro entregas**: cuatro envíos de Flexit, una sola línea de envío.
>
> **La regla del umbral lee el carrito; la suscripción lee la semana. Nunca van a coincidir.**

**La salida: el envío va adentro del precio y Tiendanube no calcula nada.** Dos productos distintos, los dos con envío sin cargo en la ficha:

**Un solo producto con dos variantes de zona** *(corregido el 18/09: primero se habían propuesto dos productos separados; con variantes es una sola ficha, una sola foto y un solo texto)*:

| Variante — *Zona de entrega* | Precio | **Promocional** | Qué incluye |
|---|---:|---:|---|
| **CABA y GBA cercano** | $181.200 | **$172.140** | 4 entregas, envíos sin cargo |
| **GBA lejano y GBA muy lejano** | $201.200 | **$192.140** | 4 entregas + **los 4 envíos de $5.000** |

> 🔧 **El paso a paso completo del panel, el texto de la ficha y el encargo para Claude in Chrome están en `textos/suscripcion-tiendanube.md`.**
>
> ⚠️ **El paso que sostiene todo:** una regla de **envío gratis limitada a ese producto**, en todas las zonas, sin monto mínimo. **Hay que confirmar que el plan Esencial deja limitarla por producto**; si solo permite "desde $X", este camino no sirve.
>
> 💳 **Y no se puede obligar a pagar por transferencia:** Tiendanube maneja los medios de pago para toda la tienda. Con tarjeta, $172.140 cuestan $8.400 de comisión en vez de $3.115. **No es grave —el modelo usa el 7%, que es peor que los dos—** pero es otra razón para tomar los primeros por WhatsApp.

- ⚠️ **Confirmar la dirección antes de aceptar la transferencia.** Nada impide que alguien de Escobar elija la versión de CABA y se ahorre $20.000.
- 💡 **Para los primeros diez, ni ponerlo en la tienda:** tomarlos por WhatsApp con el monto cotizado. Es más simple que configurar dos productos para algo que todavía se está probando.
- 📌 **Los $5.000 son por entrega, no por mes.** Si alguien pausa una semana, ese mes son **$15.000**. Con la regla de que la entrega pausada se corre al final el mes cierra en cuatro igual, pero conviene tenerlo anotado.

### Los números por zona

*Pack $45.300 · costo $24.800 · 4 entregas · 5% sobre el producto · cobro al 7% (hipótesis conservadora) · packaging $500 por entrega.*

| Zona | Paga por mes | **Deja por mes** |
|---|---:|---:|
| **CABA** | $172.140 | **$40.652** |
| **Media** | $172.140 | **$33.352** |
| **Lejana** | **$192.140** | **$44.652** |
| **Muy lejana** | **$192.140** | **$39.172** |

> 🔄 **Con los $5.000, Lejana pasa a ser la zona que más deja**, y Muy lejana queda a $1.500 de CABA. No es que convenga vender ahí: es que el cliente pone $20.000 del flete. **Y confirma que cobrar los $5.000 es lo que hace que la suscripción cierre en las zonas caras**: sin eso, Muy lejana caía a $19.172 al mes.

💡 **Y está calculado con el 7% de costo de cobrar, que es la hipótesis conservadora.** Como la suscripción se cobra por transferencia (1,81%), en la práctica quedan unos **$9.900 más por mes por cada suscriptor de zona lejana**.

### 🤔 La alternativa: subir el pack arriba del umbral en vez de cobrar el envío

Con un **pan de molde blanco** ($11.500) el Pack Semanal queda en **$56.800** y pasa los $55.000:

| | Cobrándole el envío | **Sumando un pan de molde** |
|---|---:|---:|
| Paga por mes | $192.140 | $215.840 |
| Recibe de más | — | **4 panes de molde blanco** ($46.000 de lista) |
| Deja en Lejana | $44.652 | $44.692 |
| **Deja en Muy lejana** | **$39.172** | **$39.212** |

> **Para Corteza es exactamente lo mismo: $40 al mes de diferencia.** El pan de molde blanco es el producto de mejor margen del catálogo (52,2%) y compensa al peso lo que se resigna de envío.

**Es neutro en plata, así que se decide por otra cosa.** A favor: nadie quiere pagar envío, y "te llevás un pan más y no pagás envío" vende mucho mejor que $20.000 de flete. En contra: son **dos panes por semana** —el pack ya trae un molde integral— y la fatiga es justamente lo que mata las suscripciones de comida.

> **Recomendación: la regla es cobrar los $5.000. El pan extra se ofrece como opción** cuando el cliente de zona lejana pregunte por el envío, no como default.

---

## 4. Las cuatro reglas que hacen que la gente se suscriba

1. **Se puede pausar.** Sin esto no se suscribe nadie: la gente se va de vacaciones. *"Pausá cuando quieras, avisando antes del lunes."* La entrega pausada se corre al final, no se pierde.
2. **Se puede cancelar sin explicaciones.** Cuanto más fácil salir, más fácil entrar.
3. **Se avisa cada semana antes del cierre** con lo que va en la caja, y se puede cambiar algo.
4. **La primera entrega lleva algo de regalo.** Cuesta poco y es lo que el suscriptor cuenta.

---

## 5. Cuándo abrir la elección

**No al lanzamiento. Cuando haya unos diez suscriptores y el mecanismo esté probado.**

Ahí sí conviene sumar un segundo plan, y el candidato natural es el **Familiar** para las casas que consumen de verdad. **Dejar elegir entre los cinco no se recomienda nunca**: tres de ellos no funcionan como entrega semanal.

⚠️ **El Pack para picar no se ofrece como suscripción** mientras no esté resuelta la cadena de frío. En una entrega semanal, ese riesgo se repite todas las semanas.

---

## 6. ✅ RESUELTO: sí, Tiendanube cobra automático — pero conviene no usarlo todavía

*Averiguado el 17/09/2026 en la documentación oficial de Tiendanube.*

**La función existe, es nativa y es gratis.** Genera los pedidos sola según la frecuencia, cobra sola y manda mail de confirmación al cliente. La frecuencia mínima es de 5 días, así que **semanal funciona**.

### Las dos condiciones que la vuelven cara

| | |
|---|---|
| **Pide plan Impulso como mínimo** | ✅ **Confirmado el 17/09: Corteza tiene el plan Esencial** ($26.999). Impulso son **$78.999**. → **+$52.000 por mes** |
| **Solo tarjeta de crédito vía Pago Nube** | **No admite transferencia.** Y la tarjeta es el medio caro: 4,88% contra 1,81% |

### La cuenta que decide

**Cobrar a mano por transferencia ahorra $5.285 por suscriptor por mes** contra la tarjeta que obliga la suscripción nativa:

| Suscriptores | Ahorro por cobrar por transferencia | Costo del upgrade | Conviene |
|---:|---:|---:|---|
| 5 | $26.423 | $52.000 | nativo |
| **10** | **$52.847** | $52.000 | **manual** |
| 20 | $105.694 | $52.000 | manual |
| 30 | $158.541 | $52.000 | manual |

> **Con diez suscriptores, cobrar a mano por transferencia ya ahorra más de lo que cuesta el plan entero.** Y sigue ganando a medida que crece.

### Y lo manual además es mejor producto

Las tres limitaciones de la suscripción nativa chocan de frente con las reglas del punto 4:

| Regla que hace que la gente se suscriba | La suscripción nativa |
|---|---|
| **Se puede pausar** | ❌ **Máximo 2 saltos consecutivos.** Tres semanas de vacaciones la rompen |
| **Se puede cancelar sin explicaciones** | ❌ **El cliente no puede cancelar ni editar solo.** Todo lo hace el administrador |
| Se puede cambiar algo de la caja | ❌ No hay sustitución automática: si falta stock, **saltea el ciclo** |

**Cobrando a mano las tres se cumplen sin esfuerzo:** se pausa lo que el cliente quiera, se cancela por WhatsApp, y la caja se arma con lo que el productor haya conseguido.

### 📌 La decisión

> **Arrancar a mano: el Pack Semanal se vende como producto normal, con las 4 entregas del mes pagadas por adelantado por transferencia.**
>
> **Una sola transferencia por suscriptor por mes** ($172.140 con el 5% aplicado), no cuatro. Eso es lo que hace manejable lo manual: con 30 suscriptores son 30 cobros mensuales, no 120 semanales.
>
> **Revisar el upgrade a Impulso cuando la administración duela** — en la práctica, pasados los 15 o 20 suscriptores. **El límite no es la plata, es la paciencia.**

### Y tampoco conviene pasar a Impulso por la comisión de plataforma

El Esencial cobra **1% sobre cada venta**; el Impulso, 0,7%. **Ese 0,3% de ahorro empata con los $52.000 del upgrade recién con $17,3 millones de facturación mensual** — muy por encima de los $5,4 millones que da el mínimo de 120 pedidos. **Con el volumen proyectado, el upgrade no se justifica por ningún lado.**

### Otras limitaciones, para cuando se migre

- Solo **un producto de suscripción por carrito** (se pueden sumar productos sueltos).
- **No se puede elegir el día de facturación** ni crear reglas de envío propias.
- **Si se borra un producto, se cancelan todas sus suscripciones** automáticamente.
- **Las suscripciones canceladas no se reactivan.**
- No se pueden editar los planes con libertad si hay suscriptores activos.

**El número a seguir:** cuántos de los primeros compradores se suscriben.

---

# (histórico) El modelo anterior: pack mensual de entregas de $40.000

*Rehecho el 10/09/2026, reemplazado el 15/09. Se conserva porque el razonamiento de fondo —toda entrega vale $40.000; lo que el cliente elige es cada cuánto la recibe— sigue siendo el que ordena todo, y porque las cuentas por zona siguen valiendo.*

*Rehecho el 10/09/2026 con el modelo correcto: **la suscripción es un pack mensual de entregas de $40.000**, no entregas chicas.*

> ⚠️ **El error que se corrigió, para no repetirlo:** la primera versión modelaba entregas de $25.000–$30.000, o sea **por debajo del umbral de envío sin cargo**. Eso inventaba un problema que este modelo no tiene. **Si cada entrega vale $40.000, el envío sin cargo ya le corresponde al suscriptor como a cualquier cliente. El beneficio de suscribirse es el descuento, y nada más.**

---

## 1. La regla que ordena todo

> ### Toda entrega vale $40.000. Lo que el cliente elige es cada cuánto la recibe.

Así **cada entrega supera el umbral sola** y el envío sin cargo se aplica sin reglas especiales, sin excepciones y sin explicaciones. **Para que el plan sea más barato se baja la frecuencia, nunca el monto por entrega.**

| Plan | Entregas | Lista | **Paga (−6%)** |
|---|---:|---:|---:|
| **Plan Semana** | 4 por mes | $160.000 | **$150.000** |
| **Plan Quincenal** | 2 por mes | $80.000 | **$75.000** |

---

## 2. Lo que deja el Plan Semana

| Zona | Te queda por mes | Margen | Si compraran lo mismo suelto |
|---|---:|---:|---:|
| CABA | **+$30.700** | 20,5% | +$40.000 |
| Zona Media | **+$23.400** | 15,6% | +$32.700 |
| Lejana | **+$16.100** | 10,7% | +$25.400 |
| Muy lejana | **+$10.620** | 7,1% | +$19.920 |

**El descuento cuesta $9.300 por suscriptor por mes**, igual en todas las zonas.

*(Plan Quincenal: la mitad exacta — +$15.350 / +$11.700 / +$8.050 / +$5.310.)*

---

## 3. 🔑 El descuento se paga solo si cobrás por transferencia

**Este es el punto más importante del documento.**

La comisión de Pago Nube sobre $150.000 son **$10.500**. El descuento del 6% cuesta **$9.300**. **Si el suscriptor paga por transferencia, la comisión que te ahorrás financia el descuento entero y sobra.**

| Zona | Suelto, sin descuento, con tarjeta | **Plan $150.000 por transferencia** |
|---|---:|---:|
| CABA | +$40.000 | **+$41.200** |
| Zona Media | +$32.700 | **+$33.900** |
| Lejana | +$25.400 | **+$26.600** |
| Muy lejana | +$19.920 | **+$21.120** |

> **Cobrado por transferencia, el plan te deja MÁS que vender lo mismo suelto — y encima te garantiza los cuatro envíos.**

**Por eso el plan se ofrece así: *"6% de descuento pagando por transferencia."*** No es una condición incómoda: en un pago de $150.000 la transferencia es lo natural, y de paso resuelve la palanca de margen que ya estaba anotada en `numeros.md` (esquivar el 7% de Pago Nube es la carga más grande y la única evitable).

---

## 4. Qué compra el descuento, además

**Cuatro envíos garantizados por mes.** Con el mínimo de 120 envíos de Flexit, un envío que queda sin usar cuesta **$6.340**. Cuatro envíos que de otro modo quedarían vacíos son **$25.360** que no se tiran — contra $9.300 que cuesta el descuento.

⚠️ **Y la contracara, para tenerla anotada: cuando superes los 120 envíos mensuales, ese argumento se cae.** Ahí el descuento pasa a ser costo puro y hay que revisar si el 6% sigue teniendo sentido.

---

## 5. Cuántos suscriptores hacen falta

| | |
|---|---:|
| **Plan Semana** para llenar los 120 envíos | **30 suscriptores** |
| Plan Quincenal para lo mismo | 60 |

**Treinta personas con Plan Semana son $4.500.000 de facturación mensual asegurada** y el mínimo de Flexit cubierto sin vender nada más.

---

## 6. Dos advertencias sobre el precio

**$150.000 por mes es mucha plata para pan.** Es un plan para una casa que consume de verdad, no para el cliente promedio: hoy el ticket es $23.677. **Por eso el Plan Quincenal a $75.000 no es opcional — es el que va a vender.** El Semana es el plan aspiracional que hace que el Quincenal parezca razonable.

**Y en Muy lejana el Plan Semana deja 7,1%.** Es delgado. No es para no venderlo, pero **no es una zona para empujar el plan con publicidad**.

---

## 7. Las dos modalidades de contenido

### A — La caja de Corteza *(la armás vos)*
Vos decidís qué va cada semana. **La ventaja es tuya:** armás con lo que mejor margen tiene y con lo que el productor realmente consiguió. Nunca quedás vendiendo algo que no tenés.

### B — Armá tu semana *(elige el cliente)*
El cliente define su lista fija. Convierte mejor con quien ya sabe lo que le gusta.

⚠️ **Limitala a panificados propios.** Los productos de terceros están sin stock la mayor parte del tiempo, y en una suscripción cada faltante es un mail de disculpas *todas las semanas*.

---

## 8. Cómo arrancar sin complicarse

⚠️ **No se sabe todavía si Tiendanube puede cobrar automáticamente todos los meses**, o si hace falta una app del panel. **Hay que averiguarlo, y no prometer suscripción automática hasta confirmarlo.**

**Mientras tanto: vender el plan como un producto normal, pagado una vez.** El cliente compra "Plan Semana — 4 entregas" a $150.000, y vos llevás en una planilla quién tiene entregas pendientes.

Cero fricción técnica, **cobrás el mes por adelantado**, y probás si el plan interesa antes de instalar y configurar nada.

---

## 9. Las cuatro reglas que hacen que la gente se suscriba

1. **Se puede pausar.** Sin esto no se suscribe nadie: la gente se va de vacaciones. *"Pausá cuando quieras, avisando antes del lunes."* La entrega pausada se corre al final, no se pierde.
2. **Se puede cancelar sin explicaciones.** Cuanto más fácil salir, más fácil entrar.
3. **Se avisa cada semana antes del cierre**, con lo que va en la caja, y se puede cambiar algo.
4. **La primera caja lleva algo de regalo.** Cuesta poco y es lo que el suscriptor cuenta.

---

## 10. El número a seguir

**Cuántos de los primeros 30 compradores del 24/9 se suscriben.** Si son diez con Plan Semana, octubre arranca con **40 envíos garantizados de 120** y $1.500.000 de facturación asegurada, sin vender nada nuevo.
