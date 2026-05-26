const express = require('express');
const app = express();
app.use(express.json());

const VERIFY_TOKEN = 'corteza2024';

const SYSTEM_PROMPT = `Sos el asistente virtual de Corteza, una panadería artesanal ubicada en Pilar, Argentina. Tu tono es amigable, cálido y cercano. Respondés en español rioplatense (usás "vos", "te", "podés", etc). Sos conciso pero simpático. Nunca uses markdown como asteriscos o guiones, respondé en texto plano.

CATÁLOGO Y PRECIOS:
- Pan de molde blanco: $10.000 (masa madre, harina agroecológica)
- Pan de molde integral: $10.000 (masa madre, harina agroecológica)
- Pan de molde de centeno: $10.000 (masa madre, harina agroecológica)
- Pan de campo blanco: $8.500 (masa madre, harina agroecológica)
- Pan de campo integral: $8.500 (masa madre, harina agroecológica)
- Pan de campo de centeno: $8.500 (masa madre, harina agroecológica)
- Pan árabe integral x5: $8.500 (masa madre, harina agroecológica)
- Prepizzas x2: $8.500 (masa madre, harina agroecológica)
- Grisines integrales: $5.000 (harina agroecológica)
- Budín integral: $9.000 (harina agroecológica)
- Budín blanco: $9.000 (harina agroecológica)
- Pepas integrales: $7.000 (harina agroecológica)
- Cookies integrales con chips de chocolate y nuez: $7.000 (harina agroecológica)

INGREDIENTES: Todos los productos usan harinas 100% agroecológicas. Los panes (molde, campo, árabe, prepizzas) son de masa madre. Los grisines, budines, pepas y cookies NO son de masa madre pero sí son 100% agroecológicos.

LOGÍSTICA:
- Zona de entrega: únicamente Pilar
- Días de entrega: martes y viernes
- Horario: de 9hs a 17hs aprox
- No hay pedido mínimo
- Envío gratis en pedidos de $25.000 o más
- Pedidos menores a $25.000 tienen costo de envío de $5.000

MEDIOS DE PAGO: transferencia bancaria, efectivo, tarjeta de crédito y débito.

PEDIDOS: Para hacer un pedido, dirigí al cliente a la tienda online o decile que puede escribirnos por acá.

Si te preguntan algo que no sabés, decí amablemente que lo consultás con el equipo.`;

const conversaciones = {};

app.get('/webhook', (req, res) => {
  const mode = req.query['hub.mode'];
  const token = req.query['hub.verify_token'];
  const challenge = req.query['hub.challenge'];
  if (mode === 'subscribe' && token === VERIFY_TOKEN) {
    console.log('Webhook verificado!');
    res.status(200).send(challenge);
  } else {
    res.sendStatus(403);
  }
});

app.post('/webhook', async (req, res) => {
  res.sendStatus(200);

  try {
    const body = req.body;
    if (body.object !== 'whatsapp_business_account') return;

    const entry = body.entry?.[0];
    const change = entry?.changes?.[0];
    const message = change?.value?.messages?.[0];
    if (!message || message.type !== 'text') return;

    const from = message.from;
    const text = message.text.body;
    const phoneNumberId = change.value.metadata.phone_number_id;

    console.log(`Mensaje de ${from}: ${text}`);

    if (!conversaciones[from]) conversaciones[from] = [];
    conversaciones[from].push({ role: 'user', parts: [{ text }] });

    if (conversaciones[from].length > 10) {
      conversaciones[from] = conversaciones[from].slice(-10);
    }

    // Llamar a Gemini
    const geminiRes = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${process.env.GEMINI_API_KEY}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          system_instruction: { parts: [{ text: SYSTEM_PROMPT }] },
          contents: conversaciones[from]
        })
      }
    );

    const geminiData = await geminiRes.json();
    const reply = geminiData.candidates?.[0]?.content?.parts?.[0]?.text;
    if (!reply) return;

    conversaciones[from].push({ role: 'model', parts: [{ text: reply }] });

    // Enviar respuesta por WhatsApp
    await fetch(`https://graph.facebook.com/v18.0/${phoneNumberId}/messages`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.WHATSAPP_TOKEN}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        messaging_product: 'whatsapp',
        to: from,
        text: { body: reply }
      })
    });

    console.log(`Respuesta enviada a ${from}`);
  } catch (err) {
    console.error('Error:', err);
  }
});

app.get('/', (req, res) => res.send('Bot de Corteza funcionando 🌾'));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor corriendo en puerto ${PORT}`));
