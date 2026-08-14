# Captura de lista de espera — CABA

*Armado el 13/08/2026. Todo lo que hay acá es para copiar y pegar.*

**Objetivo: 150 anotados al 14/9.** Quedan 4 semanas y media → **33 por semana.**

---

## Cómo se resuelve el campo "zona"

El newsletter nativo de Tiendanube solo guarda el mail. Y el mail solo no te sirve: el 17/9 vas a necesitar saber **quién es de CABA** (envío $3.919, podés regalarlo) y **quién es de zona norte** (envío $8.800, no lo podés regalar). Son dos mensajes distintos.

**La solución: barra de anuncio en Tiendanube que linkea a un Google Form.**

- Gratis, sin apps, sin tocar código
- Lo armás en 15 minutos
- Los datos caen solos en una planilla ordenada
- Podés filtrar por zona y mandar mensajes distintos

La contra: un clic de más. Se pierde algo de gente. Pero un anotado sin zona no te sirve para nada, así que es un clic bien gastado.

### Tres campos: nombre, contacto y zona

El formulario pide **nombre, WhatsApp o mail (el que prefieran) y zona. Nada más.** Tres campos, quince segundos.

**Se deja elegir el canal a propósito.** Hay gente que no le da el teléfono a una marca que no conoce, y esa gente sí deja el mail. Obligar a poner el número te haría perder anotados justo en CABA, que es donde nadie te conoce todavía.

La contra es de trabajo, no de plata: te van a quedar los dos tipos de contacto mezclados en una misma columna y hay que separarlos para mandar. Se resuelve con una fórmula (está más abajo, en "Cómo medir").

**Y hay una trampa de WhatsApp que hay que tapar sí o sí:** las listas de difusión **solo le llegan a quien tenga tu número agendado**. Si alguien se anota y no te guarda, el mensaje del 9 de septiembre no le llega nunca y vos no te enterás.

Por eso la pantalla de confirmación pide dos cosas: **que guarden el número** y **que te manden un mensaje** con un botón. Con eso el contacto queda abierto y la difusión llega.

---

## PASO 1 — El Google Form

### El atajo: armarlo con un script (10 segundos)

En `script-formulario-lista.gs` está el formulario entero escrito como programa. Hace todo solo: las 3 preguntas, la validación, el mensaje de confirmación y la planilla ya conectada.

1. Entrá a **script.google.com** con tu cuenta → **Nuevo proyecto**
2. Borrá todo lo que aparece y pegá el archivo entero
3. Cambiá las tres líneas de arriba (teléfono y link de la tienda)
4. **Ejecutar**
5. Los links te aparecen abajo, en el "Registro de ejecución"

⚠️ **La primera vez te va a pedir permiso y la pantalla asusta.** Va a decir *"Google no verificó esta aplicación"*. Es normal: la aplicación sos vos, es un script tuyo en tu propia cuenta. Apretá **Configuración avanzada** → **Ir a (no seguro)** → **Permitir**.

### O a mano, si preferís

Andá a **forms.google.com** → formulario en blanco. Cargá esto:

### Título del formulario
> **Activá tu recordatorio**

### Descripción
> En septiembre abrimos en todo el AMBA.
> Dejanos por dónde avisarte y te escribimos apenas abramos en tu zona.
>
> Son 3 datos, 15 segundos. Te escribimos una sola vez, cuando abramos.

### Las preguntas (3 — no agregues ni una más)

**1. ¿Cómo te llamás?** · Respuesta corta · Obligatoria

**2. WhatsApp o mail** · Respuesta corta · Obligatoria
> Como prefieras que te avisemos. Si es WhatsApp, con característica y sin el 15 (ej: 11 5555 4444).

*(Validación: Respuesta corta → ⋮ → Validación de respuestas → **Longitud** → Cantidad mínima de caracteres → **7**. Frena las respuestas escritas a medias y no traba ni a un número con espacios ni a un mail corto.)*

**3. ¿De dónde sos?** · Desplegable · Obligatoria

Opciones (en este orden):
```
CABA
Zona Norte
Zona Oeste
Zona Sur
```

### Mensaje de confirmación
*(Configuración → Presentación → Mensaje de confirmación)*

**Este texto es tan importante como el formulario.** Es lo que hace que el aviso del 9 de septiembre efectivamente llegue.

> **Listo, tu recordatorio está activado 🌾**
>
> **Si nos dejaste tu WhatsApp**, un último paso para que el aviso te llegue:
>
> **1. Guardá nuestro número: 11 5415-3989** (WhatsApp solo entrega los avisos a quien nos tenga agendados).
> **2. Mandanos un "hola" 👉 [link de wa.me]**
>
> Te avisamos el día que abrimos en tu zona.
>
> Mientras tanto, mirá qué vas a poder pedir: **[link a la tienda]**

**Cómo armar el link de wa.me:** es `https://wa.me/5491154153989` (54 + 9 + tu número sin el 15 y sin espacios). Si querés que el mensaje ya venga escrito, le agregás `?text=Hola!%20Me%20anoté%20en%20la%20lista`. Probalo desde tu celular antes de publicarlo.

### Al terminar
Apretá **Enviar** → pestaña del eslabón 🔗 → **Acortar URL** → copiá ese link. Ese es el link que va en todos lados.

### Un link distinto por anuncio (para los anuncios por zona)

Si vas a hacer un anuncio por zona (ver `zonas-amba-ranking.md`), Google Forms te deja armar **links con la zona ya elegida**: el que viene del anuncio de Nordelta abre el formulario con "Zona Norte" puesto y solo completa dos campos.

Cómo: ⋮ (arriba a la derecha) → **Obtener vínculo prellenado** → elegís la zona → **Obtener vínculo** → copiás. Uno por zona.

Sirve para dos cosas: **baja la fricción** y **te dice de qué anuncio vino cada anotado** sin tener que agregar ninguna pregunta.

Y en la pestaña **Respuestas** → ícono verde de Sheets → se te crea la planilla sola. Ahí vas a ver crecer los anotados.

---

## PASO 2 — La barra en Tiendanube

**Dónde:** Panel → Diseño de tu tienda → Personalizar → **Barra de anuncios** (o "Barra de novedades", según el tema).

Poné el texto y en el link pegás la URL del formulario.

✅ **Publicada el 14/08:** `ESTAMOS POR ABRIR EN TODO AMBA — ANOTATE`

Si en algún momento la querés alinear con el resto:
> Abrimos en todo AMBA el 17 de septiembre · Activá tu recordatorio →

Si el tema te deja elegir color, poné el fondo en un tono cálido (el verde o el ocre de la marca) y el texto en blanco. Que se vea, pero que no tape el logo.

---

## PASO 3 — Instagram

### Posteo fijo

**Imagen:** la hogaza **cortada al medio**, con la miga a la vista, recortada a 4:5. Es la única toma que muestra el adentro, y la miga abierta es la prueba de la fermentación larga. **Sin texto encima**: en el feed la foto limpia rinde más y el texto va en el epígrafe.

Mejor todavía, como carrusel: (1) cortada, (2) integral con semillas, (3) molde blanco. Instagram vuelve a mostrar los carruseles a quien no los abrió.

**Copy:**

> **Llegamos a CABA. 🌾**
>
> Después de dos años seleccionando panaderos y productores del conurbano, en septiembre empezamos a repartir en Capital.
>
> Corteza no hornea: **elegimos**. Buscamos a los que trabajan de verdad con **harinas 100% agroecológicas** —sin agroquímicos, de molinos que sabemos cómo trabajan— y masa madre de fermentación larga. Y te lo llevamos a tu casa.
>
> Pan de campo, pan de molde rebanado, prepizzas, grisines. Y una despensa chica y elegida: aceite de oliva, mermeladas sin azúcar agregada, pastas.
>
> **Arrancamos el jueves 17 de septiembre.** Los de la lista se enteran primero y entran antes.
>
> 📲 **Activá tu recordatorio en el link de la bio.** Son tres datos, 15 segundos.
>
> #harinasagroecologicas #masamadre #agroecologia #comidareal #caba #palermo #villacrespo #colegiales #belgrano #panartesanal #sinagrotoxicos #alimentacionconsciente

**Después de publicarlo:** ⋮ → **Fijar en el perfil**.

### Bio

**Nombre** (el campo de arriba, que no es la bio): `Corteza · Panificados`

**Bio** — versión final, decidida el 14/08:

> 100% agroecológico
> Envíos a todo AMBA desde el 17 de septiembre
> 👇 Activá tu recordatorio

**Por qué "activá tu recordatorio" y no "anotate":** invierte quién le hace el favor a quién. No le pedís los datos, le das un servicio. Es la misma acción y convierte más. **La condición es que el formulario diga lo mismo** —título, descripción y confirmación—, así la promesa es coherente de punta a punta.

Y en el link de la bio: el Google Form. **Mientras dure la captura, el link de la bio es el formulario, no la tienda.** Si querés los dos, usá un Linktree con el formulario arriba de todo.

### Historia (subila 2 veces por semana)

Las placas están hechas, en 1080×1920: **`story-caba.png`** (la de la encuesta, con el espacio de abajo libre para el sticker) y **`story-amba.png`** (la informativa, para alternar).

Encima de la primera, el sticker de encuesta:

> **¿Sos de CABA?**
> · Sí, quiero 🙋
> · No, soy de zona norte

A los que votan "Sí" les respondés por privado con el link. Es la forma más barata de sumar anotados: la historia se la muestra Instagram a tus seguidores actuales sin que pagues nada.

---

## PASO 4 — Respuestas rápidas de WhatsApp

**El mensaje de ausencia automático quedó descartado:** las consultas las contesta ella. Lo que sí van son las **respuestas rápidas**, que no son automáticas: son atajos para no reescribir lo mismo treinta veces.

**Dónde:** WhatsApp Business → Herramientas para la empresa → **Respuestas rápidas** → **+**. En "Atajo" va la palabra, en "Mensaje" el texto. **Pegá los links ya escritos adentro del texto**, la gracia es que sea un solo movimiento.

### `/caba` — cuando preguntan si llegás a su zona

> ¡Hola! Todavía no llegamos a tu zona, pero falta poco: **arrancamos en CABA y todo el AMBA el jueves 17 de septiembre** 🌾
>
> Activá tu recordatorio acá y sos de los primeros en enterarte, además comprás antes que el resto: [link del formulario]
>
> Repartimos una vez por semana, los jueves, con envío a domicilio.

### `/cierre` — cuando preguntan cuándo llega el pedido

> Los pedidos cierran los **lunes a las 14:00** y entregamos los **jueves** 🌾
> Lo que pidas después del lunes a las 14 ya va para la semana siguiente.
> 👉 [link a la tienda]

### `/envio` — la que más te van a preguntar a partir del 17

> El envío depende de la zona:
> · CABA — $4.200
> · Vicente López, San Isidro, Martínez, San Fernando — $6.700
> · Resto del AMBA — $8.800
>
> **En CABA el envío es sin cargo a partir de $25.000.**

---

## PASO 5 — Qué hacés con la lista después

Guardá estos dos mensajes, son los que convierten la lista en pedidos. Los mandás **solo a los que pusieron CABA**: por difusión de WhatsApp a unos, por mail con CCO a los otros. El texto es el mismo para los dos.

**Antes de mandar el primero, hacé esta prueba:** mandá un mensaje cualquiera a la difusión una semana antes y fijate a cuántos les figura entregado. A los que no, es porque no te agendaron — a esos escribiles uno por uno. Con 150 anotados no son tantos, y es la diferencia entre que el lanzamiento salga o no.

### Miércoles 9 de septiembre — el aviso

*(A los que pusieron CABA)*

> **Abrimos en tu zona el jueves 17. 🌾**
>
> Hola [nombre], te escribimos porque te anotaste en la lista de espera de Corteza.
>
> Ya está: **el jueves 17 de septiembre hacemos el primer reparto en CABA.**
>
> Cómo funciona:
> · Pedís hasta el **lunes 14 a las 14:00**
> · Te llega el **jueves 17**
> · **Envío sin cargo** en CABA a partir de $25.000
>
> Como sos de la lista, te dejamos entrar antes que al resto: **la tienda abre para ustedes desde hoy.**
>
> 👉 [link a la tienda]

*(Si va por mail, el asunto: **"Abrimos en CABA el jueves 17 🌾"**)*

### Lunes 14 a la mañana — el cierre

> [nombre], **hoy a las 14:00 cerramos los pedidos** del primer reparto en CABA 🌾
>
> Lo que pidas antes de esa hora te llega el jueves. Después de las 14 ya va para la semana siguiente.
>
> 👉 [link a la tienda]

**El segundo mensaje es el que más vende.** La gente se anota con ganas y después se olvida: el recordatorio del lunes recupera la mitad.

---

## Cómo medir si vas bien

Mirá la planilla de Google **todos los domingos** y anotá el número.

| Domingo | Anotados acumulados que deberías tener |
|---|---:|
| 17/8 | 33 |
| 24/8 | 66 |
| 31/8 | 100 |
| 7/9 | 133 |
| **14/9** | **150** ✅ |

Si el 31/8 no llegaste a 100, ahí es donde entra la plata de Meta a acelerar (semana 3 y 4 del plan). Si el 7/9 vas muy abajo de 133, **corré el lanzamiento al 24/9** — está en la regla que no se negocia del `plan-lanzamiento.md`.

Y mirá también **el mix por zona**. Si te da que más de la mitad no son de CABA, el mensaje está apuntando mal y hay que corregirlo antes de poner plata en publicidad.

### Separar los WhatsApp de los mails

Como el campo de contacto acepta las dos cosas, en la planilla te van a quedar mezclados. Se separan solos con una fórmula.

En la primera celda vacía a la derecha (suponiendo que el contacto está en la **columna C**), pegá:

```
=SI(ESNUMERO(HALLAR("@";C2));"Mail";"WhatsApp")
```

Arrastrala para abajo y listo: te queda una columna que dice "Mail" o "WhatsApp" en cada fila. Después usás **Datos → Crear un filtro** y armás las dos listas por separado.

**Para los que dejaron mail:** no hace falta ninguna herramienta. Copiás las direcciones, las pegás en el campo **CCO** de un mail común de Gmail y mandás uno solo. Gmail te deja hasta 500 por día, así que con 150 anotados vas sobrado. **Usá CCO siempre**, para que nadie vea la dirección de los demás.

**Los que no son de CABA no se descartan, pero se les habla distinto:** a ellos el envío les sale entre $6.265 y $8.196 y no se los podés regalar. Van en otra difusión, con el precio del envío dicho de frente. La localidad exacta la vas a tener igual cuando compren, en los datos del checkout.
