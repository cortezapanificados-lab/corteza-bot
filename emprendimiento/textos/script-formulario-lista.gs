/**
 * Corteza — crea el formulario de lista de espera y su planilla.
 *
 * Cómo usarlo:
 *  1. Entrá a script.google.com con tu cuenta (corteza.panificados@gmail.com)
 *  2. "Nuevo proyecto"
 *  3. Borrá todo lo que aparece y pegá este archivo entero
 *  4. Botón "Ejecutar"
 *  5. Autorizá (ver las notas de abajo)
 *  6. Los links te quedan abajo, en el "Registro de ejecución"
 */

function crearFormularioCorteza() {

  // ---------- EDITÁ ESTAS DOS LÍNEAS ANTES DE EJECUTAR ----------
  var TELEFONO_LINDO = '11 5415-3989';      // como querés que se lea
  var TELEFONO_WA    = '5491154153989';     // 54 + 9 + número sin el 15 ni espacios
  var LINK_TIENDA    = 'https://www.cortezapan.com.ar';
  // --------------------------------------------------------------

  var form = FormApp.create('Corteza — Lista de espera CABA');

  form.setDescription(
    'En septiembre empezamos a repartir en CABA y alrededores.\n' +
    'Dejanos tus datos y te avisamos primero, antes de que abramos al público.\n\n' +
    'Son 3 datos, 15 segundos. Te escribimos una sola vez, cuando abramos.'
  );

  // 1 — Nombre
  form.addTextItem()
    .setTitle('¿Cómo te llamás?')
    .setRequired(true);

  // 2 — Contacto (acepta WhatsApp o mail)
  var contacto = form.addTextItem()
    .setTitle('WhatsApp o mail')
    .setHelpText('Como prefieras que te avisemos. Si es WhatsApp, con característica y sin el 15 (ej: 11 5555 4444).')
    .setRequired(true);

  contacto.setValidation(
    FormApp.createTextValidation()
      .requireTextLengthGreaterThanOrEqualTo(7)
      .setHelpText('Escribí un WhatsApp completo o un mail.')
      .build()
  );

  // 3 — Zona
  form.addListItem()
    .setTitle('¿De dónde sos?')
    .setChoiceValues(['CABA', 'Zona Norte', 'Zona Oeste', 'Zona Sur'])
    .setRequired(true);

  // Pantalla de confirmación — es la que hace que después les llegue la difusión
  form.setConfirmationMessage(
    '¡Listo, ya estás en la lista! 🌾\n\n' +
    'Si nos dejaste tu WhatsApp, un último paso para que el aviso te llegue:\n\n' +
    '1. Guardá nuestro número: ' + TELEFONO_LINDO + '\n' +
    '   (WhatsApp solo entrega los avisos a quien nos tenga agendados)\n' +
    '2. Mandanos un "hola": https://wa.me/' + TELEFONO_WA + '\n\n' +
    'Te avisamos el día que abrimos en tu zona.\n\n' +
    'Mientras tanto, mirá qué vas a poder pedir: ' + LINK_TIENDA
  );

  form.setCollectEmail(false);        // que no pida iniciar sesión
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setAcceptingResponses(true);

  // Planilla de respuestas
  var planilla = SpreadsheetApp.create('Corteza — Anotados lista de espera');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, planilla.getId());

  // Links
  var publico = form.getPublishedUrl();
  var corto;
  try {
    corto = form.shortenFormUrl(publico);
  } catch (e) {
    corto = '(no se pudo acortar, usá el largo)';
  }

  Logger.log('===========================================');
  Logger.log('LINK PARA COMPARTIR (el que va en todos lados):');
  Logger.log(corto);
  Logger.log('');
  Logger.log('Link largo: ' + publico);
  Logger.log('Editar el formulario: ' + form.getEditUrl());
  Logger.log('Planilla de anotados: ' + planilla.getUrl());
  Logger.log('===========================================');
}
