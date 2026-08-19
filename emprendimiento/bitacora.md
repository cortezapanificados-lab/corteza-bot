# Bitácora

Registro con fecha de decisiones, avances y charlas importantes. Las entradas más nuevas van arriba.

## 19/08/2026 — Avanza la tienda; Smart Post frenado por un comercial que no contesta

**Lo que hizo Juan.** Mandó los pedidos de reseña y **ya tiene un par de respuestas**. Creó la página **"Ustedes"** en Tiendanube, rehízo **"Sobre Corteza"** (no lo convencía cómo había quedado) y cambió las fotos de la **página de inicio** que no le gustaban.

**Smart Post: se pidió el mínimo mensual y el comercial desapareció.** El pedido concreto fue pasar del mínimo de **30 envíos por despacho** a **120 por mes**, que es la misma cantidad pero permite compensar una semana floja con otra fuerte. Como el comercial dejó de responder, Juan **escaló a soporte pidiendo que le cambien de comercial**; quedaron en avisarle.

**Qué se ordenó de eso.** Se separó lo que es plata de lo que es bloqueo:

- El **mínimo mensual vale $133.246 solo en octubre**, pero **si dicen que no, el plan sigue igual**. Es una mejora, no un requisito.
- De las tres preguntas de zona que seguían abiertas, **ninguna frena el test de Meta de la semana del 24**. El conjunto A (San Isidro–Martínez–Acassuso–Beccar) se lanza igual: aunque Beccar y Acassuso fueran Cordón 2, seguiría siendo la mejor zona del ranking. La única con consecuencia real es **Nordelta**: si es Cordón 3, el recargo del 36,7% se va más arriba. **Si el 24/8 sigue sin respuesta, se arranca con los conjuntos A y B y Nordelta espera.**
- Lo de los **barrios cerrados** es operativo: hace falta antes del **17/9**, no antes de anunciar.
- Se le puso fecha al escalamiento: **si el viernes 21/8 no hay comercial nuevo, escribirle a soporte por mail** —que quede por escrito— y pedir ahí mismo las respuestas, sin esperar a que asignen a alguien. Junto con eso conviene sacar de una vez las dos confirmaciones que ya estaban pendientes: **que no cobran IVA** y el **horario de colecta** en Pilar.

**Reseñas: faltan dos.** La regla sigue siendo **no publicar "Ustedes" con menos de 4**. El orden para conseguirlas: un único recordatorio a los que no contestaron (a los 4 o 5 días del primer mensaje, y no se insiste más) y, si no alcanza, abrir el pedido a los 10 clientes de un solo pedido. La red de seguridad ya está decidida desde el 18/08: si el 31/8 faltan reseñas escritas, la página se publica **apoyada en la destacada "Ustedes" de Instagram**, que es prueba social que ya existe y no depende de que conteste nadie.

**Lo que sigue faltando de la semana 2** y no se puede correr: la app **"Opiniones de productos"** en las fichas —que es donde se decide la compra—, las **zonas de envío** cargadas en Tiendanube y los **15 micro-influencers**, que no pueden pasar de la semana del 24 porque tienen que publicar la semana del 14/9.

## 18/08/2026 — Memoria consolidada: el trabajo estaba disperso en 5 ramas

**Qué pasó.** Esta sesión arrancó leyendo la memoria del 22/07 y dio por perdido casi un mes de trabajo. No se había perdido nada: cada conversación se abre en una rama de git nueva creada desde `main`, guarda ahí, y nunca vuelve a `main`. Como `main` quedó congelado el 22/07, cada sesión nueva arrancaba ciega a las anteriores.

**Se consolidó todo en una sola línea**, uniendo cuatro ramas:

- `corteza-marketing-campaign` (8–14/08, 41 commits): todo el plan de lanzamiento, campaña de Meta, costos, márgenes, suscripciones, zonas del AMBA, formulario de captura y placas.
- `riot-discord-autostart` (24/07): campaña AMBA, perfil de Google (`google-business.md`), cierres de pedidos.
- `denuncia-persecucion-vehicular` (24/07): la oposición a la marca en el INPI (`marca-inpi.md`).
- `tiendanube-product-costs` (23/07): costos y márgenes por producto.

Los nombres de las ramas no tienen relación con el contenido: se generan solos.

**Cómo se resolvieron los choques:** en `perfil.md` se conservaron los precios de agosto (los relevados el 10/08, que corrigieron los de julio) sumándoles los detalles que julio tenía y agosto había perdido (gramajes, "veganas", variantes de prepizza). La tabla de costos de julio se descartó por redundante: los mismos costos ya están en `tabla-margenes.md`, recalculados. En `bitacora.md` se intercalaron las 39 entradas por fecha. En `pendientes.md` se recuperaron tres tareas vivas que agosto no tenía: el perfil de Google, la inconsistencia de medios de pago y el % de recompra; y se agregó el INPI en Prioridad 1. Se descartaron por superadas las de logística del AMBA (ya resuelta con Smart Post) y los cierres sábado/martes (reemplazados por el jueves único).

**Se verificó que el recordatorio del INPI del 22/10/2026 sigue activo.**

**Para que no se repita**, se agregaron dos reglas al `CLAUDE.md`: revisar las otras ramas antes de dar algo por perdido y no reescribir nunca la memoria asumiendo que está vacía; y dejar el trabajo en `main` al terminar.

**Mensajes de reseña reescritos y página "Ustedes".** Juan reescribió el mensaje: sin presentación (los clientes ya lo conocen), más corto, y preguntando algo concreto —"qué te parecen nuestros panificados"— en vez de un "qué te pareció" demasiado abierto. Se le limpió la última frase para que el permiso quedara adelante y claro. El permiso ahora va pedido en el propio mensaje: al elegir cómo quiere figurar, el cliente ya lo está dando (Ley 25.326). Se sacó el pedido de foto del primer mensaje para no pedir dos cosas juntas. Además, la página de reseñas pasa a llamarse **"Ustedes"** (mejor que "Clientes" y hace juego con la destacada de Instagram) y va a incluir un **link a la destacada "Ustedes"** con las historias que subieron los propios clientes: es prueba social que ya existe, no se puede falsificar y sirve de respaldo si el 31/8 no hay 4 reseñas escritas.

**Consultas de Juan en esta sesión**, respondidas con el plan real a la vista:

- **¿Se puede aplazar la semana entera sin mover el 17/9?** No del todo. Dos cosas siguen siendo de esta semana: los 11 pedidos de reseña (las respuestas tardan y la sección tiene que estar publicada antes del 31/8) e insistirle a Smart Post. El resto de la semana 2 se corre, con la advertencia de que los 15 micro-influencers no pueden pasar de la semana del 24, porque la semana 3 ya carga el test de Meta.
- **¿Conviene vender ya con entrega el 17 en vez del formulario?** No reemplazarlo. "Dejá tu contacto" convierte mucho más que "pagá hoy, recibí en 30 días", y la lista es la que después convierte con el aviso del 9/9 y el cierre del 14/9. Además, vender ya elimina la salida de emergencia de correr el lanzamiento al 24/9 si no se llega a los 100 anotados. Sí conviene sumar la preventa **como extra desde el 1/9**, cuando se sepa si se llega.
- **¿Avisar en Pilar que desde el 17 habrá costo de envío?** No. Contradice la decisión ya tomada de no abrir todavía el tema del envío con los clientes de Pilar, y caería en la misma semana en que se les pide una reseña. Además todavía no está calculado cuánto cuesta el reparto propio en Pilar, así que no hay con qué decidir. El tema se retoma después del 31/8.

## 14/08/2026 — Captura en marcha: form, barra, píxel, posteo e historia

Se ejecutó casi toda la semana 1 del plan de lanzamiento en un día. Quedó publicado: el **Google Form** de captura, la **barra de anuncio** en Tiendanube ("ESTAMOS POR ABRIR EN TODO AMBA — ANOTATE"), el **píxel de Meta**, el **posteo del feed** y la **primera historia**. El mensaje de ausencia automático de WhatsApp se descartó —las consultas las contesta ella—, y quedan las respuestas rápidas `/caba`, `/cierre` y `/envio`, que son atajos y no automatismos.

**Decisiones de forma:** el formulario quedó en tres campos (nombre, WhatsApp o mail, zona) y el CTA pasó a ser **"activá tu recordatorio"** en vez de "anotate en la lista" —idea de la dueña, y es mejor: invierte quién le hace el favor a quién—. La condición fue alinear título, descripción y confirmación del formulario para que la promesa sea la misma de punta a punta. La bio quedó minimalista, como estaba: "100% agroecológico / Envíos a todo AMBA desde el 17 de septiembre / 👇 Activá tu recordatorio".

**Las placas** se generan con `textos/generar-placas.py`, usando el **logo real** bajado de la tienda (se le aísla el canal alfa para teñirlo) más Playfair Display y Jost. Quedó una sola placa de historia —CABA está adentro del AMBA, así que la versión "¿Sos de CABA?" era redundante y dejaba afuera a Nordelta y San Isidro— y una tapa para la destacada.

**Foto del feed:** se eligió la hogaza cortada al medio, recortada a 4:5, sin texto encima. Es la única de las tres que muestra la miga, que es la prueba visual de la fermentación larga. La estantería de la panadería queda de segunda en el carrusel: no genera deseo pero sí confianza, y además da para un posteo propio de curaduría ("nosotros no horneamos, elegimos").

**Se desbloquearon las reseñas.** Estaban pospuestas porque no se quería abrir todavía el tema del envío con los clientes de Pilar, pero los textos de `mensajes-resenas.md` **no mencionan el envío ni los precios**: son solo el pedido de opinión. Se decidió mandarlos ya a los 11 clientes de dos pedidos o más, porque las reseñas tienen que estar publicadas antes del 31/8, cuando empiece a llegar tráfico pago de CABA. Plan completo en `textos/seccion-resenas.md`, con el mínimo de 4 reseñas para publicar y la regla de no poner solo cinco estrellas.

**Fichas nuevas escritas:** kéfir de agua (tradicional e hibiscus) y las dos líneas de Booch Kombucha, la clásica y la funcional. En la funcional se decidió **vender el momento del día en vez del efecto** ("es la de la mañana") y no repetir "foco", "energía" y "calma": el Código Alimentario es estricto con las propiedades atribuidas a alimentos y los hongos adaptógenos son el rubro más mirado. Falta el costo de cada producto para calcular márgenes.

Además se limpió `pendientes.md`, que tenía el píxel repetido tres veces y varias tareas duplicadas. Ahora está ordenado por semana del plan.

## 13/08/2026 — Ranking de zonas del AMBA para los anuncios localizados

Idea de la dueña: hacer un anuncio por zona con el nombre del lugar en el titular ("El jueves 17 lanzamos en Nordelta"). La idea es buena —nombrar el barrio baja el costo del clic— pero tiene un límite duro: **Meta necesita unas 50 conversiones semanales por conjunto para salir de la fase de aprendizaje**, y con $500.000 en 4 semanas alcanza para unos 50 anotados semanales en total. **Máximo 3 zonas simultáneas**; con 8 el presupuesto se pulveriza. Se investigó y se armó `zonas-amba-ranking.md`.

**El hallazgo principal: San Isidro, Martínez, Acassuso y Beccar son Cordón 1 ($6.265) y Nordelta es Cordón 2 ($8.196).** Mismo perfil socioeconómico o mejor, $1.931 menos por pedido — sobre 40 pedidos semanales son $334.000 mensuales, más de la mitad del presupuesto de publicidad. El corredor San Isidro pasa a ser la zona #1 del ranking, por encima de CABA y de Nordelta.

**El otro concepto que ordenó el análisis:** con el recargo del 6,38%, si el cliente paga su envío la zona no le cuesta plata a Corteza — Nordelta deja lo mismo que Palermo. Lo que cambia por zona es **cuánta gente abandona el carrito al ver el envío**: $4.200 en CABA es el 17,5% de un pedido de $24.000, pero $8.800 en Nordelta es el 36,7%. De ahí las dos reglas: en CABA se regala el envío, en Cordón 2 y 3 no se regala, se empuja el pedido grande con bonificación parcial.

Nordelta queda tercero pero es estratégico: 45.000-50.000 habitantes en 23-26 barrios dentro de un polígono chico (se targetea con un pin y 3 km de radio, lo más barato y preciso del AMBA) y es **Pilar del Lago a diez veces la escala**, o sea la única fórmula que ya le funcionó. Hay competencia (Craft Vegan Bakery en Nordelta, El Massa en Tigre) pero ninguno con el ángulo de harinas agroecológicas más curaduría.

Se anotó también una palanca para más adelante: **un punto de retiro adentro de cada country** baja diez envíos a uno, pero recién sirve pasados los 30 pedidos estables por despacho — antes de eso consolidar te aleja del mínimo y pagás envíos fantasma igual.

## 13/08/2026 — Captura de lista de espera: textos listos y método definido

Se resolvió cómo capturar el campo **zona**, que el newsletter nativo de Tiendanube no soporta. Método elegido: **barra de anuncio en Tiendanube que linkea a un Google Form**. Se descartó el formulario embebido con código (requiere tocar la plantilla) y el newsletter nativo solo (un mail sin zona no sirve: CABA se comunica distinto que zona norte, porque en CABA el envío se puede regalar y en Pilar no).

**El formulario quedó en 3 preguntas: nombre, WhatsApp o mail (a elección) y zona** (desplegable CABA / Zona Norte / Zona Oeste / Zona Sur). Decisión de la dueña: cuantos menos campos, más gente se anota. Se descartó pedir barrio o localidad —el dato para saber el cordón llega igual con la primera compra— y se sacó "Zona Este", que en el AMBA no existe.

El campo de contacto acepta las dos cosas para no perder a quien no le da el teléfono a una marca desconocida. El costo es de trabajo, no de plata: quedan mezclados en una columna y se separan con `=SI(ESNUMERO(HALLAR("@";C2));"Mail";"WhatsApp")`. Los mails se mandan con CCO desde Gmail (límite 500 por día, alcanza de sobra).

**El riesgo que trae usar WhatsApp, y cómo se tapa:** las listas de difusión **solo entregan a quien tenga el número agendado**. Un anotado que no guarde el contacto nunca recibe el aviso del 9/9 y no queda registro. Por eso la pantalla de confirmación del formulario pide guardar el número y ofrece un botón de wa.me para que escriban primero, y una semana antes del lanzamiento hay que mandar un mensaje de prueba a la difusión y escribirle uno por uno a los que no reciben.

Quedó armado `textos/captura-lista-caba.md` con todo listo para copiar y pegar: el paso a paso del Google Form, tres variantes de la barra de Tiendanube, el posteo fijo de Instagram con la bio y la historia con encuesta, el mensaje de ausencia y la respuesta rápida `/caba` de WhatsApp Business, y los dos mensajes de conversión de la lista (aviso del miércoles 9/9 y cierre del lunes 14/9).

**Recalculado el ritmo:** quedan 4 semanas y media hasta el 14/9, así que el objetivo pasa de 27 a **33 anotados por semana**. Se agregó la tabla de control semanal (33 / 66 / 100 / 133 / 150) y el segundo indicador a vigilar: **el mix por zona**, porque si más de la mitad no son de CABA el mensaje está apuntando mal.

## 10/08/2026 — PLAN DE LANZAMIENTO DEFINITIVO: jueves 17 de septiembre

Fecha tope puesta por la dueña: arrancar los repartos a otras zonas como máximo el 17/9. **Resultó ser también la mejor opción financiera.**

Septiembre tiene 4 jueves (3, 10, 17, 24). Lanzando el 17 quedan **solo 2 despachos**, y como en la rampa sobran despachos y faltan pedidos, eso concentra el volumen: **32 pedidos por despacho, cero envíos fantasma.** Contra $195.950 de fantasmas lanzando el 3 y $78.380 lanzando el 10.

**El número que define el lanzamiento: 150 anotados en la lista de espera.** Con 2 despachos hacen falta 60 pedidos en septiembre para superar el mínimo de 30 en ambos. Con 150 anotados al 20% de conversión más los clientes nuevos del mes se llega a 64. Hay **5 semanas y media** para juntarlos: 27 por semana.

**Modelo financiero septiembre-diciembre** (40 clientes nuevos/mes, recompra 70%):

| Mes | Despachos | Pedidos | Fantasmas | Operativo | Resultado | Acumulado |
|---|---:|---:|---:|---:|---:|---:|
| Sep | 2 | 64 | $0 | $508.036 | +$8.036 | $8.036 |
| Oct | 5 | 116 | $133.246 | $854.194 | +$217.434 | $225.470 |
| Nov | 4 | 149 | $0 | $1.291.677 | +$654.917 | $880.387 |
| Dic | 5 | 172 | $0 | $1.503.721 | +$866.961 | **$1.747.348** |

**Septiembre cierra positivo aun metiendo los $500.000 de publicidad: la inversión se recupera en el primer mes.**

**Octubre es el único mes con desperdicio** ($133.246) por tener 5 jueves, que reparten los 116 pedidos en 23,2 por despacho. Se elimina con el mínimo mensual de Smart Post o llegando a octubre con más clientes.

**Regla que no se negocia: no lanzar el 17 con menos de 100 anotados.** Si al 10/9 no se llegó, correr el lanzamiento al 24/9 (un solo despacho, cero fantasmas) antes que lanzar flojo.

Plan completo semana por semana en `plan-lanzamiento.md`, que reemplaza a `plan-agosto.md` como documento operativo.

## 10/08/2026 — Fecha de lanzamiento: jueves 10 de septiembre (SUPERADO, ver arriba)

Septiembre 2026 tiene **4 jueves: 3, 10, 17 y 24** (ningún mes puede tener 3). Como durante la rampa sobran despachos y faltan pedidos, **cuantos menos despachos haya en el mes, menos envíos fantasma se pagan:**

| Lanzando el | Despachos | Por despacho | Fantasmas | Resultado mes 1 |
|---|---:|---:|---:|---:|
| jueves 3 | 4 | 17,5 | $195.950 | −$132.598 |
| **jueves 10** | **3** | **23,3** | **$78.380** | **−$15.028** |
| jueves 17 | 2 | 35,0 | $0 | +$63.352 |

**Se define lanzar el jueves 10 de septiembre:** ahorra $117.570 contra el 3, da una semana más de preparación y deja el mes 1 casi en cero. Lanzar el 17 sería mejor en plata pero retrasa toda la rampa.

Calendario: cierre del primer pedido el **lunes 7/9 a las 14:00**, recepción el miércoles 9, **primer despacho el jueves 10**, después 17 y 24.

**Detectado: octubre tiene 5 jueves** (1, 8, 15, 22, 29), y ese jueves de más reparte los pedidos más finito: $133.246 de fantasmas contra los $54.474 que daría con 4 despachos. Es un argumento más para negociar el mínimo mensual con Smart Post — **con mínimo mensual deja de importar cuántos jueves tenga el mes.**

## 10/08/2026 — Presupuesto del mes 1: $500.000 y el peso de la lista de espera

**Definido: $500.000 de bolsillo para publicidad del mes 1.** Reparto: $135.000 en 10 influencers por canje, $120.000 en Meta las primeras dos semanas para aprender el CAC y $245.000 para escalar si cierra. Escenario base: 43 clientes nuevos (hacen falta 40).

**Corrección al modelo tras una observación válida:** los códigos de descuento y el envío regalado de la primera compra son un costo y no estaban contados. **Van dentro del CAC, no aparte:** CAC real = lo pagado en Meta + $3.919 de envío. Para un CAC total objetivo de $15.000, el techo de pago en Meta es $11.081.

**Se descarta la regla abierta de "envío gratis en la primera compra"** porque es gameable con otro mail. En su lugar, **códigos por canal con usos limitados**, que además permiten medir el CAC por canal.

**Umbral de envío definido en $35.000** (1,3 veces el ticket promedio de $27.038, que es la colocación estándar). Con $25.000 se regalaban 86 envíos mensuales y se comía el 72% del presupuesto de publicidad. No hay datos duros del mercado argentino sobre tolerancia al costo de envío: se define por regla de colocación y **se mide en el test de Meta**.

**Dos hallazgos operativos del mes 1:**

1. **Despacho SEMANAL desde el día 1 — decidido.** Se evaluó arrancar quincenal para esquivar el mínimo de 30 y **se descartó por marca**: el concepto es "el jueves hay pan" y arrancar cada 15 días para después cambiar rompe el ritual. Tiene un costo de **$289.222 en envíos fantasma durante la rampa** ($234.748 el mes 1, $54.474 el mes 2, cero desde el mes 3), y el mes 1 cierra en **−$171.396** con una inversión total de arranque de $734.748.

   **Antes de dar ese costo por hecho: negociar con Smart Post un mínimo MENSUAL en vez de por despacho** ("con cuatro despachos te garantizo 120 envíos, pero repartidos desigual mientras arranco"). Es mucho más aceptable para ellos porque reciben el mismo volumen total, y si lo dan los $289.222 desaparecen. Es la gestión más rentable del mes.

2. **La lista de espera decide el resultado del mes 1.** Sin lista: 40 pedidos, 18,4 por despacho, $98.367 de envíos fantasma, resultado **−$311.594**. Con una lista de 150 que convierta 20%: 70 pedidos, 32,3 por despacho, sin fantasmas, resultado **+$63.352**. **Son $375.000 de diferencia**, porque la lista suma pedidos y además hace superar el mínimo desde el día uno.

**Juntar 150 anotados antes de lanzar dejó de ser recomendable y pasó a ser la condición del lanzamiento.**

## 10/08/2026 — Plan de agosto: el orden de las tareas y el diseño de la suscripción

Ante la sensación de que era mucho junto (combo barato + suscripción + influencers + Meta + reseñas), se ordenó todo con un principio: **primero la casa, después las visitas.** Los influencers y Meta solo mandan gente a la tienda; si la tienda no está lista, se quema el tráfico y la plata.

**Secuencia definida — una tarea por semana:**

| Semana | Tarea |
|---|---|
| 1 | Los 21 mensajes a clientes |
| 1-2 | Caja de presentación + suscripción + reseñas + píxel |
| 2-3 | Contactar 15 influencers, cerrar 10 |
| 4 | Test de Meta de $30.000 |
| Septiembre | Lanzar |

**El mensaje de la semana 1 hace tres trabajos a la vez:** reactiva a los 15 dormidos, pide permiso para la lista de difusión y pide la reseña para la sección nueva de la web.

**Hallazgo importante en el diseño de la suscripción: el flete se paga 4,33 veces al mes.** En CABA son $16.969 mensuales de envío por suscriptor, o sea que hacen falta $39.463 de venta mensual solo para cubrirlo. **Una suscripción chica con envío incluido no cierra** (un pan por semana deja 16%).

Planes definidos: **Casa quincenal $48.100** (25% de contribución), **Semana $96.200** (25%) y **Familia $168.400** (33%). Se arranca con los dos primeros. **No se ofrece plan semanal chico.**

**Un suscriptor del Plan Semana vale 2,2 veces un cliente suelto** ($24.421 contra $11.276 de contribución mensual), y además no hay que reconquistarlo cada mes.

**Sobre la sección de reseñas** (idea propia, muy buena para CABA donde nadie conoce la marca): solo reseñas reales, **no poner solo cinco estrellas** —un 4,8 con alguna de cuatro es más creíble que un 5,0 perfecto— y que digan el barrio. Pedir foto de la mesa servida: vale por cinco reseñas sin foto.

Detalle en `plan-agosto.md`.

## 10/08/2026 — Reestructuración de septiembre: fuera el reparto propio, foco en CABA

**Decisión tomada:** a partir de septiembre se termina el reparto propio en Pilar. Todo pasa por Smart Post y el foco de captación se traslada a **CABA**. Objetivo: **40 pedidos por semana.**

Se planteó el riesgo de que los 21 clientes de Pilar pasen de envío gratis a pagar $8.800 y que varios no vuelvan. La decisión se reafirmó: **la base de Pilar deja de ser el negocio y pasa a ser un extra.** Queda asumido como costo de la reestructuración.

**El razonamiento de CABA es correcto y hay una tercera ventaja además de las dos previstas** (más poder adquisitivo, envío más barato): con envío a $3.919 el piso para regalar el envío es de $9.114, contra $19.060 en Pilar. **CABA es la única zona donde se puede ofrecer envío sin cargo**, que es el argumento que más convierte en ecommerce. Umbral recomendado: $15.000.

**La matemática del objetivo:** 173 pedidos/mes requieren ~102 clientes activos. Con recompra del 70% eso son 31 clientes nuevos por mes en régimen, y con 40 nuevos mensuales se llega al objetivo en 4 meses. El CAC tiene que quedar por debajo de $15.000 (ideal $10.000–12.000) para entrar en el presupuesto de $470.520 mensuales que deja el 30% de margen.

**Advertencia estratégica registrada:** en CABA la masa madre no diferencia — hay decenas de panaderías excelentes. **El diferencial real es "harinas 100% agroecológicas"**, y ese tiene que ser el titular de toda la comunicación, no la masa madre.

**Canal identificado como el de mejor retorno: micro-influencers de alimentación consciente por canje.** Una caja de $25.000 cuesta $13.500 reales; si trae 3 clientes el CAC es $4.500, tres veces mejor que Meta. Plan: contactar 15, cerrar 10.

Otras definiciones: concentrar Meta en 4 barrios (Palermo, Villa Crespo, Colegiales, Belgrano) en vez de toda CABA; crear una **caja de presentación de ~$16.100 con envío sin cargo** porque la Promo de $28.900 es mucho para un primer pedido de una marca desconocida; y **la suscripción pasa a ser la pieza central**, porque reemplaza al boca a boca del country que sostenía la recompra en Pilar.

**Costo de arranque a presupuestar:** el mes 1 da ~15,7 pedidos por jueves contra el mínimo de 30 de Smart Post, o sea unos $240.000 de envíos fantasma el primer mes y $56.000 el segundo. Se puede achicar despachando cada 15 días al arranque.

Plan completo en `estrategia-caba.md`.

## 10/08/2026 — Diagnóstico de ventas: el negocio se está achicando

Se analizó el export de ventas (44 pedidos pagados, 28/05 al 10/08). **Es el hallazgo más importante de toda la sesión y cambia el orden de prioridades.**

**Los pedidos cayeron 67% de junio a julio:** 27 → 9, y agosto va peor. Promedio del período: 4,2 pedidos por semana.

**La causa está identificada: se cortó la entrada de clientes nuevos.** En junio entraron 13 clientes nuevos; en julio, uno solo; en agosto, ninguno. Los clientes existentes siguieron comprando más o menos igual — lo que se apagó fue la adquisición.

**La recompra tampoco alcanza:** 43% de mayo a junio, 38% de junio a julio, 14% de julio a agosto. Para un consumo semanal como el pan debería estar arriba del 60%. Con 40% de recompra y cero clientes nuevos, el negocio se achica 60% por mes, que es exactamente lo que muestran los números.

**Resultado por mes:** junio +$158.366, **julio +$5.827** (prácticamente cero).

**Correcciones al modelo con datos reales:**
- Ticket promedio: **$23.677** (se venía usando $28.000).
- Costo de cobro real: **2,97%**, no 7%. El 18% de las ventas es en efectivo y el 55% por transferencia.
- Contribución real: **42,2%** de la venta, mejor que el 37,9% modelado.
- Medios de pago: 54,5% transferencia, 27,3% tarjeta, 18,2% efectivo. **Ya está el 72,7% en medios baratos**, así que subir el descuento por transferencia tiene poco para ganar.
- El descuento del 2% arrancó el 14/07 y solo se aplicó en 5 de 24 transferencias: es muy nuevo para evaluarlo.

**El activo escondido: 55% de los pedidos vienen del country Pilar del Lago** ($605.670 de $1.041.785). Es riesgo de concentración y a la vez una fórmula probada — lo más barato y probable es replicarla en otros countries de la zona.

**Nuevo orden de prioridades:** (1) recuperar la entrada de clientes nuevos, (2) atacar la recompra con la lista de WhatsApp y la suscripción, (3) replicar Pilar del Lago en otros countries, (4) recién después optimizar márgenes — el margen ya está sano.

**Para el AMBA:** con 4,2 pedidos semanales y un mínimo de 30 por despacho, hoy se está a 1/7 del volumen necesario. Primero hay que arreglar el motor de clientes en Pilar.

Detalle completo en `diagnostico-ventas.md`.

## 10/08/2026 — Modelo de costos definitivo

Queda fijado el modelo, más simple que todo lo que se venía usando:

> **Ganancia por pedido = venta × (margen bruto − 8%)**

Ese 8% son **7% de comisión de Pago Nube + 1% de packaging**. El packaging pasa de estar cargado como monto fijo ($1.000) a porcentaje (1%), que es lo que corresponde según el cálculo real.

**Costos fijos: $82.000/mes** — Claude $35.000 + Tiendanube $27.000 + envío del proveedor al almacén $20.000. *(Este último queda cargado como mensual; si fueran $20.000 por viaje habría que rehacer las cuentas.)*

Con margen bruto de 45,9% en panificados propios, **queda 37,9% de la venta** para cubrir fijos y ganar. En un pedido de $28.000 son $10.612.

**Los números que importan:**

- **Punto de equilibrio: 8 pedidos/mes sin publicidad, 22 con Meta a $150.000** (5 por jueves).
- **Se llega al 30% de margen neto con 24 pedidos por jueves.**
- **El mínimo de 30 que exige Smart Post ya deja 31,5%.** El mínimo dejó de ser un problema y pasó a ser la garantía de que el negocio cierra: el día que se pueda despachar con ellos, el objetivo de rentabilidad está cumplido por definición.
- Techo de margen neto: 37,9%.

La palanca ya no es el precio ni el margen: es llegar a 24 pedidos por jueves.

## 10/08/2026 — Los costos reales cambian todo el panorama (para bien)

Se cargó el export de productos de Tiendanube con **los costos reales de cada producto**. Es el dato que faltaba desde el arranque y corrige toda la modelización previa.

**El margen bruto real de los panificados propios es 45,9%**, no 30% como se venía asumiendo. El de terceros es 29,0% y el del catálogo completo, 36,9%. Todos los cálculos anteriores eran demasiado pesimistas.

Consecuencias:

- **El techo de margen neto es 36,3%**, no 20,4%. **Ya está por encima del objetivo del 30% sin necesidad de más aumentos de precio.**
- **El punto de equilibrio es mucho más bajo:** 15 pedidos/mes sin publicidad y 29 con Meta a $150.000 (7 por jueves), contra los 52 que se calculaban antes.
- **Se llega al 30% de margen neto real con 39 pedidos por jueves.** Esa pasa a ser la meta concreta del negocio.
- Cumplir el mínimo de Smart Post (30 por jueves) ya deja **$1.022.743 mensuales al 28,1%**.

**El mejor producto es el pan de molde blanco: 52,2% de margen.** Conviene empujarlo en toda la comunicación. En terceros, el mejor es el aceite Zuelo (36,4%).

**Sobre los productos de terceros:** las bajadas de precio recomendadas más temprano se hicieron sin los costos a la vista y llevaron cinco productos de ~30% a ~24% de margen (mermeladas, dulce de leche, yerba y las dos pastas Contraviento). La bajada se sostiene, pero con otro fundamento: **en estos productos el costo de compra es demasiado alto para competir por precio** — la mermelada cuesta $6.600 y en el mercado se vende a ~$7.890, o sea 16% de margen si se igualara. Su función no es dejar ganancia por unidad sino **subir el valor del pedido**, y como el flete es plano, cada producto extra suma contribución sin costo logístico adicional. Son armadores de carrito, no centros de ganancia.

Aun así, 24% es finito: quedó anotado **negociar con Las Quinas y Contraviento** aprovechando el volumen del AMBA, buscar proveedores alternativos o discontinuarlos.

**La palanca ya no es el precio: es el volumen.** El objetivo pasa a ser llegar a 39 pedidos por jueves.

## 10/08/2026 — Relevamiento de precios reales y nueva política de precios

Se relevó la tienda directamente y aparecieron **diferencias con los precios que estaban anotados en la memoria**: los reales eran más bajos. Pan de campo $7.500 (no $8.500), prepizzas $7.000 (no $8.500), grisines $4.000 (no $5.000), budín $7.000 (no $9.000), pepas $5.500 (no $7.000), cookies $6.000 (no $7.000) y Promo Lanzamiento $25.000 (no $27.900). También apareció una **Hogaza a $10.000** que no estaba registrada, y ya no figuran las aceitunas San Nicolás.

**Queda establecida la política de precios en dos velocidades:**

**1. Panificados propios → +15%.** Es donde hay poder de precio real, porque nadie puede comparar la curaduría de Corteza. Pan de molde y hogaza $11.500, pan de campo y árabe $8.600, prepizzas y budín $8.000, cookies $6.900, pepas $6.300, grisines $4.600, Promo $28.900 (mantiene el mismo descuento relativo).

**2. Productos de terceros → nunca se les aplica el aumento.** Son marcas que el cliente compara en dos segundos, así que el precio lo fija el mercado y no los costos de Corteza.

El relevamiento contra el mercado encontró que **varios estaban por encima**: mermeladas Las Quinas 19% arriba ($9.400 vs ~$7.890), dulce de leche 20% arriba ($9.400 vs ~$7.800), yerba Roapipó en el techo del rango ($6.600 vs $4.458–$6.899) y pasta de aceitunas Contraviento arriba del rango ($9.700 vs $6.069–$9.592). En cambio el aceite Zuelo ($11.000 vs $10.279–$12.155) y el Ruca Malen Chardonnay ($16.500 vs $16.920–$18.800) están bien.

Se bajaron seis productos a **mercado +10%**, que es un premium defendible para una tienda curada con envío a domicilio: mermeladas a $8.700, dulce de leche a $8.600, tomates secos a $9.800, pasta de aceitunas a $8.900 y yerba a $6.100. Estar 20% arriba en un producto comparable no hace ganar más: instala fama de tienda cara y contamina la percepción del pan, que es donde está la ganancia real.

Nota: todos los productos de terceros estaban **sin stock** al momento del relevamiento.

**Regla para el futuro: cuando se suban precios, se suben solo los propios. Los de terceros se revisan contra el mercado, no contra los costos.**

## 10/08/2026 — Se corrige el plan de publicidad: no gastar hasta que la fecha esté cerca

Se revisó la recomendación de arrancar ya con $60.000 mensuales en Meta para juntar la lista de espera. **Es un error si la fecha de lanzamiento está lejos**: las listas se enfrían y alguien que se anota seis meses antes llega tibio al primer aviso. Se estaría pagando por contactos que se degradan.

**Plan corregido:**

| Cuándo | Qué | Costo |
|---|---|---|
| Desde hoy | Captura orgánica (cartel en la tienda, posteo fijo, respuesta automática de WhatsApp) + instalar el píxel | $0 |
| 6-8 semanas antes de abrir | Empujón pago para completar los 150 anotados | $60.000-150.000/mes |

La captura gratuita sí arranca ya, porque no es publicidad sino tapar un agujero que hoy pierde contactos todos los días — y son los mejores contactos posibles, gente que buscó activamente. El píxel también, porque necesita tiempo para juntar datos.

Se sumó la idea de un **test de calibración de $30.000 por dos semanas** para averiguar cuánto cuesta conseguir un anotado. Ese número define con cuánta anticipación hay que prender la publicidad.

**Dato bloqueante para planificar: la fecha estimada de lanzamiento del AMBA.**

## 10/08/2026 — Cierre de pedidos los lunes 14:00 (ya cargado en la tienda)

Queda definido el calendario semanal definitivo: **entrega los jueves, cierre de pedidos el lunes a las 14:00.** Ya está actualizado en la tienda. El pedido a los proveedores sale el lunes a la tarde y la mercadería llega el miércoles, así que hay margen cómodo de preparación.

Tres consecuencias que cambian el marketing:

1. **La ventana de venta es el fin de semana.** Entre el viernes y el lunes al mediodía se juega la semana entera. Se reordenó toda la cadencia: los mensajes de WhatsApp pasan a **domingo** ("mañana a las 14 cerramos") y **lunes temprano** ("hoy a las 14 cierra"); los posteos de Instagram a viernes/sábado, domingo y jueves.

2. **Se agregó programación horaria a la campaña de Meta.** Como quien ve un anuncio el martes tiene que esperar 9 días para recibir, se recomienda concentrar el presupuesto: ~70% de viernes a domingo, ~20% el lunes hasta las 14, ~10% el resto. Mismo presupuesto, más pedidos.

3. **La suscripción semanal pasa a ser la columna vertebral.** Un cierre el lunes al mediodía, en horario laboral, es muy fácil de olvidar. La suscripción le saca ese problema al cliente y le asegura el pedido a Corteza. Dejó de ser una buena idea para convertirse en la defensa principal del modelo.

Se detectó también un punto a cuidar: **quien llega tarde espera 10 días.** Conviene que la tienda muestre bien claro "tu pedido llega el jueves X" y usar esa espera para ofrecer la suscripción.

También se recalcularon todas las tablas con el recargo del envío aplicado. Con el aumento del 15% y 30 pedidos por jueves, el neto queda en **$957.273 mensuales (22,9%)**.

## 10/08/2026 — Se pasa a entregar solo los jueves + se abre la cuenta del margen

**Decisión tomada: se entrega un solo día, los jueves**, tanto Pilar como todo el AMBA. Cierre de pedidos el martes 22:00. Eso deja **un solo viaje al proveedor por semana ($86.600/mes contra $260.000 de tres viajes)** y los costos fijos totales en **$148.600/mes** antes de publicidad.

Se actualizaron todos los textos de la campaña, el perfil y "Sobre Corteza" al nuevo día. El concepto pasa a llamarse **"El jueves hay pan"**, y el cierre del martes a las 22 se convierte en el motor de urgencia semanal: da un motivo legítimo para escribirle a la lista dos veces por semana.

**Sobre el techo de margen neto del 19,1%:** se revisó la cuenta peso por peso. La diferencia con la intuición (30% bruto − 6% comisión − 3,6% packaging = 20,4%) sale de un supuesto que no se había explicitado: que **Pago Nube cobra el 6% sobre el total cobrado, incluido el envío**. El 6% de $34.265 son $2.056, que sobre los $28.000 de producto representan 7,3% en vez de 6%. Esos 1,3 puntos son toda la diferencia.

| | Techo de margen neto (margen bruto 30%) |
|---|---|
| Comisión sobre producto + envío | 19,1% |
| Comisión solo sobre el producto | 20,4% |

**Queda para confirmar en el panel de Pago Nube.** Se usa el escenario conservador (19,1%) en todos los documentos. Dato interesante: si la comisión fuera solo sobre el producto, con +15% se llegaría justo al 30% de techo.

Lo que no cambia con ninguna hipótesis: con margen bruto 30% el techo está entre 19% y 20%, y no lo supera ningún volumen.

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

## 24/07/2026 — Oposición a la marca CORTEZA en el INPI: investigada por consulta pública

Dato nuevo: la marca **CORTEZA** se pidió en el INPI el 10/06/2026 (acta **4.729.366**, denominativa, **clase 35** — servicios de venta minorista de alimentos, tienda online, marketing, etc.), a nombre de Juan Martín Guerrini. Se publicó en el Boletín 11.061 el 17/06/2026 y el 06/07/2026 **Néstor Mario Valente** (Rosario) presentó oposición vía apoderado (agente 1009, oposición Nº 772.685), argumentando confundibilidad con su marca **"CORTEZA NATURALMENTE GENUINOS"** (acta 4.229.688, clase 35, mixta) — que en realidad está limitada a venta de **ropa, bolsos, carteras y calzado**, nada que ver con alimentos.

La vista de la oposición se notificó el **22/07/2026** y vence el **22/10/2026**: antes de esa fecha hay que negociar el levantamiento o contestar la vista. Lectura preliminar: la oposición parece defendible — los rubros no se superponen (panificados vs. marroquinería), la marca del oponente tiene aditamentos ("Naturalmente Genuinos") y ya coexisten muchas marcas "Corteza" en clase 35 (ej. "Corteza Mall", concedida en 2026). La moneda de negociación obvia: limitar la clase 35 de Corteza excluyendo ropa/calzado/bolsos/carteras. Todo salió de la consulta pública del INPI, sin necesidad de usuario ni clave.

## 24/07/2026 — Diagnóstico de optimización del negocio

Se analizó el negocio completo y se priorizaron 4 frentes: (1) conocer los márgenes por producto — planilla pendiente de que el dueño pase los costos; (2) suscripción semanal de pan, que encaja con el modelo de pedidos anticipados; (3) combos para subir el ticket (Desayuno, Picada, Merienda); (4) medir y trabajar la recompra. Ideas cargadas en ideas.md y datos a conseguir en pendientes (costos por proveedor, costo de reparto, ticket promedio, más vendidos, % de recompra). También se detectó la inconsistencia de medios de pago en el pie de la tienda.

## 24/07/2026 — Decisión: nuevos cierres de pedidos (sábado y martes)

Se adoptó el esquema nuevo: pedidos hasta el sábado → entrega el martes; pedidos hasta el martes → entrega el viernes. Motivo: un día más de margen para trabajar más relajado, pensando también en el volumen que traerá AMBA. Se actualizó el perfil y la descripción preparada para Google. Se prepararon los textos para publicar los cierres en la tienda ("Sobre Corteza" + barra de anuncio); queda pendiente que el dueño los pegue en Tiendanube.

## 24/07/2026 — Se documentó el cierre de pedidos del pan de masa madre

Esquema actual: pedidos hasta el domingo → entrega el martes; pedidos hasta el miércoles → entrega el viernes (el pan llega el día de entrega). En evaluación: adelantar los cierres a sábado y martes respectivamente, para trabajar más relajado. Se actualizó la logística en el perfil.

## 24/07/2026 — Plan de campaña de marketing para el lanzamiento AMBA

Se armó el plan completo de la campaña de lanzamiento en AMBA con foco en costo mínimo: quedó guardado en `emprendimiento/campania-amba.md`. Estructura: Fase 0 (prerrequisitos: logística, tienda, fotos, Google), Fase 1 (pre-lanzamiento: expectativa + lista de espera con 10% off + activar clientes de Pilar), Fase 2 (lanzamiento: Promo Lanzamiento como oferta estrella, sorteo, canjes con micro-cuentas, grupos de barrio), Fase 3 (sostener: referidos, rutina de contenido, difusión por WhatsApp, reseñas). Incluye presupuesto, métricas simples y textos listos para usar. Regla acordada: no pagar publicidad hasta que lo orgánico funcione. Se agregaron los prerrequisitos a pendientes.

## 23/07/2026 — Costos completos en Tiendanube (los 13 productos + Hogaza)

Se terminó la carga: prepizzas a $4.500 las tres variantes (Juan confirmó que son de masa blanca) y Hogaza a $6.400 (producto nuevo, se vende a $10.500 — margen 39%). Todo verificado releyendo los valores guardados en el panel. El perfil quedó actualizado con la tabla de costos definitiva.

## 23/07/2026 — Costos cargados en Tiendanube (12 de 13 productos)

Claude entró al panel de Tiendanube (cuenta juan_guerrini@hotmail.com, con código de verificación por mail) y cargó el campo "Costo" en todos los panificados propios: molde blanco/integral/centeno, campo blanco/integral/centeno, pan árabe, grisines, budín, pepas y cookies. El margen que calcula Tiendanube coincide con el del perfil (35% a 50%). Quedaron pendientes las PREPIZZAS X2: en la tienda las variantes son por cobertura (Salsa de tomate / Cebolla / 1 y 1), no por masa blanca/integral, así que hay que definir qué costo va. También apareció un producto nuevo "Hogaza" sin costo en la lista. Dato: las pepas tienen 3 variantes y el budín 2 en la tienda.

## 23/07/2026 — Costos de los panificados registrados

Se pasaron los costos de los 13 panificados propios (lo que se le paga al proveedor) y quedaron guardados en el perfil junto con el margen de cada producto. Los márgenes van del 35% (molde de centeno) al 50% (grisines, budín, pepas). Dato nuevo: hay prepizza blanca e integral con costos distintos ($4.500 y $5.000) pero se venden al mismo precio. Falta cargar los costos en el panel de Tiendanube (Claude no tiene acceso al panel; quedó anotado en pendientes con el paso a paso).

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
