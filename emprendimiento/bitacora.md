# Bitácora

Registro con fecha de decisiones, avances y charlas importantes. Las entradas más nuevas van arriba.

## 10/08/2026 — Corrección clave: el AMBA está frenado por la mudanza, no por capacidad

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
