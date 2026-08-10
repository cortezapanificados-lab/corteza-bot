# Bitácora

Registro con fecha de decisiones, avances y charlas importantes. Las entradas más nuevas van arriba.

## 10/08/2026 — Corrección de costos y aclaración sobre el margen bruto

Se corrigieron dos costos que estaban mal cargados: **la comisión de Pago Nube es 6%** (no 5,73%) y **el viaje del proveedor cuesta $20.000** (no $15.000). Se rehicieron todos los cálculos.

Además quedó aclarado un punto que se estaba presentando mal y generaba confusión legítima:

- **A precios actuales, con margen bruto 30%, el techo de margen neto es 19,1%.** Ningún volumen lo supera. Cualquier número mayor con margen bruto 30% es imposible.
- **Pero el margen bruto no se queda en 30% si se suben los precios.** El proveedor cobra lo mismo en pesos, así que el aumento va casi entero a margen: con +15% el bruto pasa a 39,1% y el techo neto a 28,9%.

Las tablas que mostraban 24,6% correspondían al escenario +15% y no al de precios actuales. De ahora en más **cada tabla aclara con qué margen bruto está calculada.**

**Hallazgo nuevo e importante: el flete del proveedor es el costo fijo más grande.** A $20.000 el viaje: 3 viajes semanales son $260.000/mes, 1 semanal son $86.600. **Consolidar todo en un solo día ahorra hasta $173.400 mensuales**, más que Tiendanube y Claude juntos. Es el argumento más fuerte para unificar también las entregas de Pilar en el mismo día del AMBA.

Números actualizados: punto de equilibrio a precios actuales con 1 viaje semanal y Meta a $150.000 es de **56 pedidos/mes**. Con el aumento del 15% y 30 pedidos por despacho, el neto es **$908.444 mensuales (21,7%)**. Para llegar a 30% neto real hace falta un aumento de entre 22% y 30% según el volumen.

## 10/08/2026 — Decidido: un solo día de AMBA por semana

Confirmado que el mínimo de Smart Post es **30 envíos por despacho**. Se decidió entregar en todo el AMBA **una vez por semana**, y los números lo respaldan con claridad:

- Con 60 pedidos semanales, hacerlo en uno o dos días da exactamente el mismo neto ($2.109.069/mes). Partirlo no ahorra nada.
- Con 35 pedidos semanales, un día deja **$1.091.957** y dos días solo **$413.771**, porque con 17 por despacho se pagan 25 envíos fantasma por semana.

**Regla fijada: un solo día hasta sostener más de 60 pedidos semanales de forma estable.** Como no hay tope máximo, un día aguanta 30, 60 o 120 pedidos sin costo extra; partirlo solo agrega el riesgo de no llegar al mínimo.

Cumplir el mínimo de 30 ya deja **21,2% de margen neto** (con el aumento del 15% aplicado). De ahí para arriba mejora rápido: 50 por despacho dan 24,4%, y 80 dan 26,2%.

**Semana operativa propuesta:** cierre de pedidos martes 22:00, compra al proveedor y recepción el miércoles, armado y colecta el jueves antes de las 13:00, entrega el jueves en todo el AMBA. Se eligió jueves porque cubre el fin de semana y deja el viernes como día de recuperación. Detectado un punto operativo exigente: el PDF indica colecta hasta las 13:00 en zonas lejanas y Pilar es Cordón 3, así que hay que empacar buena parte el miércoles.

**Riesgo identificado para después del lanzamiento:** la lista de espera garantiza un primer despacho grande, pero los despachos 2, 3 y 4 son el peligro real — se agota el envión y se cae abajo de 30. Dos defensas: **escalonar las invitaciones de la lista por tandas semanales** y **montar una suscripción semanal con 8% de descuento**. Con 18 suscriptores se arranca cada semana con más de la mitad del mínimo asegurado. El descuento cuesta ~$190.000 mensuales de margen, bastante menos que una sola semana sin llegar a 30 (que deja el neto en $346.043 contra $888.535).

Archivo nuevo: `lanzamiento-amba.md`.

## 10/08/2026 — Modelo económico completo, mapa de zonas y campaña de Meta

Sesión larga de números. Tres hallazgos que cambian la estrategia.

**1. Las zonas de Smart Post se miden desde CABA, no desde Pilar.** Confirmado revisando el mapa del PDF: misma zona = CABA ($3.919), cercana = Cordón 1 ($6.265), lejana = Cordón 2 ($8.196), periféricas = Cordón 3 ($8.196). Como las dos últimas cuestan igual, hay tres precios y no cuatro.

**Pilar está en el Cordón 3**, la banda más cara. O sea que la ciudad propia es la más cara de servir y **CABA, donde hoy no se vende, es la más barata y la más rentable.** Da vuelta la estrategia geográfica: la expansión rentable es hacia la Capital, no hacia los partidos vecinos (Escobar es Cordón 3, Tigre es Cordón 2). Las entregas de Pilar se siguen haciendo con reparto propio.

**2. Costos fijos mensuales**: Tiendanube $27.000 + Claude $35.000 + $15.000 por viaje del proveedor (se asumen 8 al mes) = **$182.000** antes de publicidad. Punto de equilibrio: 33 pedidos/mes sin publicidad, 61 con Meta a $150.000.

**3. Sobre el objetivo de 30% de margen neto**: hay un límite matemático que conviene tener claro. **Con los precios actuales el neto no puede superar el 19,4%, ni con volumen infinito**, porque de cada $28.000 facturados quedan $5.437 después de producto, comisión y packaging. Para llegar a 30% hay que subir precios sí o sí. Un 30% neto real exige entre +26% y +63% de aumento según el volumen.

**Recomendación: +15% ahora** (techo de 29,2%, lista de precios completa en `numeros.md`) y perseguir volumen, con un segundo ajuste más adelante. Subir 35% de golpe con el volumen actual probablemente espante más clientes de los que compense.

**Condiciones finales de Smart Post**: sin IVA, **sin costo de colecta**, tarifa plana por tamaño y **mínimo de 30 envíos por despacho, sin tope máximo**. Ese mínimo ordena todo el lanzamiento: con un día de AMBA por semana son ~130 pedidos mensuales, muy por encima del equilibrio — o sea que si se cumple el mínimo, el negocio cierra con holgura (~21% neto con el aumento). El desafío no es la rentabilidad, es juntar los 30 pedidos del primer día. Y como no hay tope máximo, cada pedido extra del mismo día es contribución casi pura.

**Se armó `campana-meta.md`** con el plan de publicidad en tres fases: Fase 0 ($60.000/mes) para juntar 150 anotados antes de abrir —que es lo que hace falta para llegar a los 30 pedidos—, Fase 1 ($150.000/mes) para el lanzamiento, y Fase 2 escalando 30% por semana mientras el costo por cliente se mantenga debajo de $15.000. La plata va a CABA y Cordón 1, en ese orden.

Archivos nuevos: `numeros.md` y `campana-meta.md`. Se reordenó `pendientes.md` por prioridad.

Falta un solo dato para cerrar todo: **cuántos pedidos por mes se están haciendo hoy.**

## 10/08/2026 — La cuenta completa: packaging y comisión cambian el panorama

Se sumaron los dos costos que faltaban: **packaging $1.000 por pedido** (2 bolsas de $350 + $300 de changüí) y **comisión de Pago Nube del 5,73%**.

La ecuación por pedido queda: **ganancia = (pedido × 24,27%) − $1.000 − envío**, donde el 24,27% sale de restarle la comisión al margen bruto del 30%.

**Los pisos suben muchísimo**: misma zona $20.268, cercana $29.934, lejana $37.890. El umbral de $30.000 que se había sugerido para zona cercana resulta ser exactamente el punto de ganancia cero — ese pedido dejaba $16.

Conclusión de fondo: **con margen 30% el envío sin cargo pleno solo cierra en misma zona.** Para las otras bandas los umbrales necesarios ($42.000 y $53.000) quedan fuera del alcance del cliente. La solución es **bonificación parcial**: un monto fijo de descuento sobre el envío y el cliente paga la diferencia. Curiosamente deja más ganancia que el envío gratis pleno.

Estructura definida: misma zona envío sin cargo desde $28.000; cercana bonificación de $3.000 desde $32.000; lejana bonificación de $3.000 desde $35.000.

También se anotó que el umbral actual de Pilar ($25.000) deja apenas $1.149 por pedido, y conviene subirlo a $28.000.

**Cuatro palancas para mejorar el margen**, ordenadas por facilidad: (1) empujar transferencia bancaria con un descuento del 4% para esquivar el 5,73% de Pago Nube —la más fácil y de mejor retorno—, (2) bajar el costo de packaging comprando por cantidad, (3) renegociar con proveedores, (4) subir el ticket, que con flete plano es casi ganancia pura.

Sigue faltando el costo de la colecta: si existe, todos los pisos suben otra vez.

## 10/08/2026 — Condiciones de Smart Post: tarifa plana y margen 30%

Tres datos que llegaron después del PDF y que cambian las conclusiones:

1. **Smart Post no cobra IVA** (acordado por fuera del PDF, que dice lo contrario). Se usan las tarifas netas: $3.919 / $6.265 / $8.196. Queda pendiente pedirlo por escrito.
2. **La tarifa es plana por envío, sin importar el tamaño**, porque la camioneta del día es exclusiva para Corteza.
3. **Margen bruto: 30%** por producto, sin contar logística.

**Cae todo el análisis de peso volumétrico** de la entrada anterior: con tarifa plana no existe el problema de los 20.000 cm³. Y la conclusión se da vuelta: como el flete cuesta lo mismo con un pan que con veinte, **ahora conviene la caja más grande posible**. Cada producto extra es margen sin costo logístico adicional. Eso habilita formatos grandes (packs, caja del mes) y saca al vino de la lista de problemas.

**El riesgo nuevo, y es más serio que el anterior:** si la camioneta es exclusiva, alguien la paga. Es muy poco probable que Smart Post la mande por 5 paquetes. Casi seguro hay un mínimo de envíos o un cargo mínimo por día. **Es la pregunta prioritaria a hacerles**, porque si existe ese mínimo, el AMBA tiene una escala mínima de lanzamiento: la lista de espera pasa de útil a imprescindible, y conviene arrancar con un solo día de AMBA por semana para concentrar volumen, sumando el segundo cuando crezca.

Umbrales recalculados con margen 30% y tarifas sin IVA: Pilar $20.000 (se puede bajar desde los $25.000 actuales), zona cercana $30.000, zona lejana bonificación parcial de $5.000 desde $32.000.

Se dejó anotada una advertencia: el 30% no contempla comisiones de cobro con tarjeta, embalaje ni roturas. Si eso se lleva 5 o 6 puntos, el margen efectivo es ~24% y los pisos suben bastante.

## 10/08/2026 — Tarifas de Smart Post: el problema del volumen (SUPERADO, ver entrada de arriba)

Se recibió el PDF de tarifas de **Smart Post**, la logística con la que se va a hacer el AMBA. Tarifa tamaño chico (hasta 5 kg) sin IVA: misma zona $3.919, cercana $6.265, lejana y periféricas $8.196. Con IVA: $4.742 / $7.581 / $9.917.

**El hallazgo más importante no es el precio, es cómo miden el tamaño.** Cobran por el mayor entre el peso real y el peso volumétrico, y el volumétrico se calcula `(alto × largo × ancho) / 4000`. Como el pan es liviano pero voluminoso, una caja de 45×35×30 cm pesa 3 kg en la balanza pero se cobra como 11,8 kg. **El límite para quedarse en tarifa chica es 20.000 cm³.**

Esto genera una tensión de fondo con los mínimos de compra: el umbral empuja al cliente a comprar más, pero cuanto más compra, más grande la caja y más caro el flete — justo cuando se lo estás bonificando. La salida es diseñar los combos mirando el volumen, no solo el precio: los productos de almacén (aceite, mermeladas, té) suben el ticket sin agrandar la caja, el pan la agranda muchísimo. El vino además pesa y es frágil.

Otros dos puntos de la letra chica: **la colecta se paga aparte** (se reparte entre los pedidos del día, así que conviene concentrar despachos) y **los aumentos siguen a los de MercadoLibre**, o sea que los umbrales hay que revisarlos cada 3 meses.

Umbrales sugeridos con margen 35%: Pilar $25.000 (el actual, se mantiene), zona cercana $32.000, zona lejana bonificación parcial de $6.000 desde $35.000 en vez de envío gratis pleno (el piso queda arriba de lo que el cliente está dispuesto a gastar).

Sigue faltando el **margen bruto** para cerrar los números, más el costo de la colecta, las tarifas de tamaño mediano y grande, y confirmar qué partidos entran en cada banda saliendo de Pilar.

## 10/08/2026 — Modelo real del AMBA: logística tercerizada y mínimos de compra

Se corrigieron dos supuestos equivocados de la charla anterior:

1. **La mudanza es personal, no del negocio.** Corteza es 100% online, sin local. Si hace falta stockear, se stockea en la casa particular. Es un tema privado: **no se usa como material de comunicación.** Se sacó de la campaña la idea de contar la mudanza como historia.
2. **Se abre todo el AMBA de una vez, no por zonas.** La logística es tercerizada, cada envío se cobra por separado según la zona del comprador y lo paga el comprador. Como no hay rutas propias que justificar, abrir de a poco solo frenaría ventas. Se eliminó de la campaña el mecanismo de apertura por umbral de 15 anotados.

Se armó `envios-amba.md` con el criterio para definir los mínimos de compra con envío bonificado. **La cuenta central: piso = costo del envío ÷ margen bruto** (el punto donde toda la ganancia se va en el flete). Sobre eso, dos límites: el piso por rentabilidad y un techo por conducta del cliente (ticket promedio × 1,4). Cuando el piso supera al techo —típico en zonas lejanas— la salida recomendada es **bonificación parcial del envío** en vez de envío gratis pleno.

Estructura propuesta: tres bandas (Pilar / AMBA cercano / CABA y resto), con el umbral de Pilar de $25.000 sin cambios porque ya está bien calibrado.

Falta para cerrarlo: el **margen bruto promedio**, las **tarifas reales de la empresa de logística por zona** y el **ticket promedio** de Tiendanube.

## 10/08/2026 — Corrección: el AMBA está frenado por una fecha, no por capacidad

Se aclaró un dato que cambia la estrategia: **Corteza sí puede entregar en el resto del AMBA.** No es una limitación operativa ni de proveedores. Hoy se entrega solo en Pilar porque se está esperando una mudanza para largar la expansión.

Consecuencia para el marketing: el interés de fuera de Pilar deja de ser "plata tirada" y pasa a ser un activo. Se agregó a la campaña la sección **3 bis — Lista de espera del AMBA**, con la idea de capturar desde ya a toda la gente de otras zonas (mail + **zona**, que es el dato que importa) para llegar al día de la mudanza con demanda armada en lugar de arrancar de cero.

Se sumó también el mecanismo de **apertura por zona con umbral** ("cuando lleguemos a 15 anotados en tu zona, abrimos"), que hace que la gente recomiende para destrabar su barrio, garantiza que el primer viaje a cada zona sea rentable y genera una novedad publicable por cada apertura.

Regla que quedó fijada: **prometer el aviso, nunca la fecha.**

Pendiente por definir: fecha estimada de la mudanza y a qué zona, porque eso determina qué parte del AMBA conviene abrir primero.

## 10/08/2026 — Campaña de marketing "El martes hay pan"

Se armó una campaña completa de 4 semanas, guardada en `textos/campana-agosto-2026.md`: diagnóstico, concepto, 5 canales ordenados por retorno, plan semana por semana, textos listos para copiar y pegar, y qué medir.

Tres definiciones estratégicas que conviene no perder de vista:

1. **La restricción geográfica manda.** Como hoy solo se entrega en Pilar, toda la campaña es hiperlocal. Publicitar fuera de Pilar es plata tirada.
2. **El objetivo es la recurrencia, no la captación.** El pan es consumo semanal y se está vendiendo como compra única. El número clave a seguir es cuántos clientes compran 2 o más veces por mes.
3. **La competencia es la comodidad, no otra panadería.** El cliente elige entre pedir a Corteza o agarrar pan en el súper. La campaña vende no tener que pensar en el pan.

El concepto da vuelta la limitación de entregar solo martes y viernes y la convierte en un ritual de marca. Se priorizó la lista de difusión de WhatsApp como canal principal por ser gratis y el de mayor retorno. Se sumaron dos mecánicas de crecimiento: el "pedido de barrio" (5 pedidos juntos en un barrio cerrado = envío gratis para todos, que además abarata la logística) y el combo "Plan Semana" por encima de los $25.000.

También se charló sobre si conviene usar Claude o Gemini para esto. Conclusión: se complementan. Claude para estrategia, textos, números y memoria del negocio; Gemini o Canva para generar imágenes y videos; y las fotos reales del pan sacadas con el celular por encima de todo, porque en comida rinden más que cualquier imagen generada.

Pendientes cargados en `pendientes.md`. La primera tarea es armar la lista de WhatsApp.

## 22/07/2026 — "Sobre Corteza" terminada: título con formato aplicado

Verificado en la página: el título del texto ya tiene formato de encabezado y la descripción que Google muestra de la página ahora arranca con "Elegimos el mejor pan artesanal...". Tema cerrado; quedan como opcionales las negritas en frases clave.

## 22/07/2026 — Página "Sobre Corteza" renovada y publicada

Ya está online: la placa corregida subida a Tiendanube y el texto de la Opción A cargado como texto real debajo (verificado en la página). Se decidió mantener el texto fuera de la imagen (por posicionamiento en Google, legibilidad en celulares y facilidad de actualización cuando se lance AMBA). Queda pendiente darle formato al texto (título + negritas) desde el editor de Tiendanube.

## 22/07/2026 — Placa de "Sobre Corteza" corregida digitalmente

Se editó la placa de la página "Sobre nosotros" directamente sobre la imagen (sin Canva): "elaboramos" → "seleccionamos" y el sello "100% DE MASA MADRE" → "PANES 100% / MASA MADRE". Quedó guardada en `textos/placa-sobre-corteza-corregida.png` (2000x2000), lista para subir a Tiendanube. Pendiente: replicar los cambios en el Canva original.

## 22/07/2026 — Se aclaró el modelo de negocio: curaduría, no producción propia

Dato clave: Corteza no fabrica los panificados — los elaboran distintos proveedores artesanales y Corteza los selecciona y revende bajo su marca. Además, hay planes de expandir la entrega de Pilar a todo el AMBA "en cualquier momento". Se actualizó el perfil y se reescribió el borrador de "Sobre Corteza" (v2) para que el texto sea honesto con este modelo: la curaduría como diferencial.

## 22/07/2026 — Precios confirmados y borrador de "Sobre Corteza"

Se confirmó: pepas integrales a $7.000 (ya actualizado en la web) y budines por ahora solo blancos. Se escribió un borrador con dos opciones de texto para la página "Sobre Corteza" de la tienda, en `textos/sobre-corteza.md`, con huecos para completar con la historia personal.

## 22/07/2026 — Relevamiento completo de la tienda online

Se recorrió www.cortezapan.com.ar y se actualizó el perfil con el catálogo completo: además de los panificados propios, la tienda vende almacén orgánico (mermeladas, dulce de leche, miel, yerba, aceitunas, aceite de oliva), dips, té Intizen y vinoteca orgánica. Hay una Promo Lanzamiento a $27.900. Se detectaron diferencias a confirmar (precio de pepas, budines) que quedaron anotadas en pendientes. Datos de contacto agregados al perfil: tel 11 5415-3989, dirección C. 9 1761, Pilar.

## 22/07/2026 — Se armó la memoria del emprendimiento

Se creó la carpeta `emprendimiento/` en este repositorio para que Claude tenga contexto de Corteza en cada sesión (desde la PC o el celular). Se cargó el perfil del negocio con productos, precios y logística (tomados del bot de WhatsApp). Se decidió por ahora no seguir desarrollando el bot de WhatsApp; el foco es usar a Claude como asistente del emprendimiento.
