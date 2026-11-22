---
titulo: Cómo medir conversiones en Google Ads (GA4, llamadas y WhatsApp)
seo_titulo: Cómo medir conversiones en Google Ads en 2026
descripcion: Cómo configurar conversiones en Google Ads: etiqueta de Google, GA4, conversiones mejoradas, llamadas, WhatsApp y ventas offline. Qué medir y qué evitar.
palabra_clave: conversiones en Google Ads
categoria: google-ads
fecha: 2026-11-22
resumen: Para medir conversiones en Google Ads instala la etiqueta de Google, define como conversión principal solo lo que se parece a una venta (compra, formulario, llamada calificada), activa las conversiones mejoradas y, si vendes por fuera de la web, importa qué contactos se volvieron clientes.
---

Medir bien las **conversiones en Google Ads** es lo primero que reviso en cualquier cuenta. Antes de las palabras clave, antes de los anuncios, antes del presupuesto. Porque Google optimiza hacia lo que tú le dices que es una conversión. Si le dices que una conversión es "visitó la página de contacto", te va a traer gente que visita la página de contacto. No clientes.

La respuesta corta: instala la etiqueta de Google en tu sitio, define como conversión principal solo las acciones que se parecen a una venta (una compra, un formulario enviado, una llamada que duró lo suficiente, un WhatsApp iniciado), activa las conversiones mejoradas y, si cierras la venta por fuera de la web, devuélvele a Google la información de qué contactos se volvieron clientes. Con eso, la plataforma aprende a buscar compradores.

## Qué es una conversión en Google Ads

Una conversión es una acción valiosa que alguien hace después de interactuar con tu anuncio. Puede ser:

- Una compra en tu tienda online.
- Un formulario de contacto o de cotización enviado.
- Una llamada desde el anuncio o desde tu web.
- Un clic en el botón de WhatsApp o una conversación iniciada.
- Una cita agendada.
- Una venta que se cerró después, por teléfono o en persona.

Cada una se configura como una **acción de conversión**. Y aquí viene lo importante: cada acción puede ser **[principal o secundaria](https://support.google.com/google-ads/answer/11461796?hl=es)**.

- **Principal:** cuenta en la columna de conversiones y se usa para optimizar las pujas.
- **Secundaria:** se registra para que la puedas ver, pero no se usa para optimizar.

Uno de los errores más comunes que encuentro es tener todo como principal: visitas a páginas, clics en el correo, scroll. La campaña termina optimizando hacia lo más fácil de conseguir, que casi nunca es lo que te paga.

## Paso 1: instalar la etiqueta de Google

La etiqueta de Google (Google tag) es el código que conecta tu sitio con Google Ads y Google Analytics. Puedes instalarla:

- **Directo en el código** del sitio.
- **Con Google Tag Manager**, que es lo que yo prefiero porque permite agregar y cambiar eventos sin tocar el código cada vez.
- **Con la integración de tu plataforma.** Shopify, por ejemplo, tiene la aplicación de Google & YouTube, que conecta la tienda con Google Ads y Merchant Center.

Después creas las acciones de conversión y defines qué evento las dispara: la página de gracias, el formulario, un botón.

## Paso 2: GA4 o etiqueta de Google Ads, ¿cuál usar?

Tienes dos caminos para que Google Ads reciba conversiones:

1. **Conversiones de la etiqueta de Google Ads**, configuradas directamente en Google Ads.
2. **Eventos clave importados de GA4.** En Google Analytics 4 marcas un evento como evento clave y luego lo importas a Google Ads como conversión.

| Opción | Ventaja | Cuidado |
|---|---|---|
| Etiqueta de Google Ads | Medición directa, pensada para optimizar pujas | Solo ve el tráfico de Google Ads |
| Importar desde GA4 | Una sola configuración para analítica y pauta | Modelos de atribución y tiempos pueden diferir |

Lo que hago normalmente: uso la etiqueta de Google Ads para la conversión principal que optimiza las pujas, y vinculo GA4 con Google Ads para analizar el comportamiento en el sitio. Lo que no hago es tener la misma conversión como principal por los dos caminos, porque se duplica.

## Paso 3: activar las conversiones mejoradas

Las conversiones mejoradas toman datos que el usuario ya te dio (correo o teléfono, por ejemplo, en un formulario o en una compra), los cifran y se los envían a Google para emparejar mejor la conversión con el clic. Esto ayuda a recuperar conversiones que se pierden por bloqueos de cookies, cambios de dispositivo y restricciones de los navegadores.

Hay dos usos:

- **Para la web:** mejora la medición de compras y formularios en tu sitio.
- **Para clientes potenciales:** captura el correo o teléfono del formulario para que después puedas decirle a Google qué contactos se convirtieron en clientes.

[Según Google](https://support.google.com/google-ads/answer/16884284?hl=es), desde junio de 2026 las conversiones mejoradas para la web y para clientes potenciales se unificaron en un solo ajuste que se activa o desactiva, y las cuentas existentes se migraron de forma automática. Revisa en la configuración de conversiones de tu cuenta que esté activo.

Ojo con los datos personales: en Colombia rige la Ley 1581 de 2012 de protección de datos. Tu política de privacidad y tus formularios deben informar cómo usas la información.

## Paso 4: medir las llamadas

En servicios, muchas ventas empiezan con una llamada. Hay tres formas de medirlas:

1. **Llamadas desde el anuncio.** Con los recursos de llamada y el informe de llamadas activado, Google usa un número de desvío y registra la llamada y su duración. Colombia está entre los países donde están disponibles estos números.
2. **Llamadas desde la web.** Google puede mostrar un número de desvío en tu sitio a quienes llegaron desde un anuncio.
3. **Clics en el número** desde el celular, medidos como evento.

En todos los casos, define una duración mínima para contar la llamada como conversión. Una llamada de 10 segundos no es un cliente potencial.

## Paso 5: medir WhatsApp

En Colombia, WhatsApp es el canal de venta por excelencia. Hay dos situaciones:

### Botón de WhatsApp en tu página

Mides el clic en el botón como evento con Google Tag Manager. Es una conversión útil, pero ojo: un clic no es una conversación. Mucha gente abre WhatsApp y no escribe. Por eso, si es posible, la dejo como secundaria y uso como principal algo más cercano a la venta.

### Recursos de mensajes desde el anuncio

Google tiene recursos de mensajes que abren una conversación de WhatsApp directo desde el anuncio en campañas de búsqueda y Performance Max. Google agregó una acción de conversión de "conversación iniciada" para estos casos. La disponibilidad puede variar según la cuenta, así que revisa si te aparece.

Si también pautas en Meta, la lógica es parecida a la del píxel y la API de conversiones, que te explico en [píxel de Meta y API de conversiones](/blog/pixel-de-meta-y-api-de-conversiones/).

## Paso 6: importar las ventas que cierras por fuera

Este es el paso que separa una cuenta normal de una cuenta que de verdad optimiza hacia ventas. En servicios de alto valor, la venta no pasa en la web: pasa en una llamada, una valoración o una reunión días después.

Si no le cuentas a Google cuáles contactos compraron, Google trata igual a un curioso que a un cliente que pagó $10.000.000.

La forma recomendada hoy es usar las conversiones mejoradas para clientes potenciales: el formulario captura el correo o teléfono, tu CRM registra cuáles se volvieron clientes y esa información se sube a Google Ads, ya sea manualmente, con el administrador de datos de Google Ads o con una integración del CRM. Google considera la importación clásica de conversiones offline por GCLID como una función heredada. Y si lo haces por API, Google indicó que desde el 15 de junio de 2026 estas cargas pasan a su Data Manager API, así que confirma que tu integración esté actualizada.

## Paso 7: asignar valor a las conversiones

No todas las conversiones valen lo mismo. Si vendes productos, el valor de la compra se envía automáticamente. Si vendes servicios, asigna un valor estimado.

### Un ejemplo con números

Supongamos que, de cada 10 formularios, cierras 2 clientes y cada cliente te deja $3.000.000 de margen. Cada formulario vale en promedio $600.000. Si una llamada calificada cierra el doble que un formulario, podría valer $1.200.000. Con esos valores, Google puede priorizar lo que más te deja. Son números ilustrativos; usa los de tu negocio.

Con valores bien puestos, puedes usar estrategias como ROAS objetivo, que son las que más se benefician de buenos datos, sobre todo en [Performance Max](/blog/performance-max/).

## Cómo saber si tu medición está bien

Revisa esta lista:

- Las conversiones principales son pocas y se parecen a una venta.
- No hay conversiones duplicadas (la misma acción por GA4 y por etiqueta como principal).
- El estado de las acciones dice que están registrando conversiones.
- Las conversiones mejoradas están activas.
- Las llamadas tienen una duración mínima.
- Los números de Google Ads se parecen, más o menos, a los formularios, llamadas y ventas reales del negocio.
- Si vendes offline, estás importando qué contactos se volvieron clientes.

Si quieres revisar toda la cuenta, no solo la medición, te sirve el checklist de [cómo auditar tu cuenta de Meta Ads o Google Ads](/blog/auditoria-de-cuenta-publicitaria/).

## Errores comunes al medir conversiones

1. Contar visitas a páginas como conversión principal.
2. Duplicar conversiones por tener GA4 y la etiqueta como principales.
3. Contar cada recarga de la página de gracias como una conversión nueva en formularios (en clientes potenciales, normalmente se cuenta "una" por clic).
4. No medir llamadas ni WhatsApp en negocios que venden por ahí.
5. No importar ventas offline en servicios de alto valor.
6. Poner el mismo valor a todo.

Mi principio es que los números se explican. Si un reporte dice 80 conversiones y tu equipo comercial solo recibió 20 contactos, algo está mal medido, y eso hay que resolverlo antes de invertir un peso más. Si quieres que alguien revise y lleve tu cuenta con este cuidado, puedes ver mi servicio como [especialista en Google Ads](/servicios/pauta-google-ads/).

¿No estás seguro de qué está contando Google como conversión en tu cuenta? Escríbeme por WhatsApp y lo revisamos juntos.

## Preguntas frecuentes

### ¿Qué es una conversión en Google Ads?

Es una acción valiosa que alguien hace después de ver o hacer clic en tu anuncio, como una compra, un formulario enviado, una llamada o una conversación de WhatsApp. Google Ads usa las conversiones principales para optimizar las pujas. Por eso es clave que representen ventas o contactos reales.

### ¿Es mejor medir conversiones con GA4 o con la etiqueta de Google Ads?

Las dos opciones funcionan. Yo suelo usar la etiqueta de Google Ads para la conversión principal que optimiza las pujas y vincular GA4 para analizar el comportamiento en el sitio. Lo importante es no tener la misma acción como principal por los dos caminos, porque se duplica.

### ¿Qué son las conversiones mejoradas?

Son una función que envía a Google, de forma cifrada, datos que el usuario ya te dio, como el correo o el teléfono. Así Google empareja mejor la conversión con el clic y recupera conversiones que se perderían por bloqueos de cookies o cambios de dispositivo. También permiten importar qué contactos se convirtieron en clientes.

### ¿Cómo mido las conversiones de WhatsApp en Google Ads?

Puedes medir el clic en el botón de WhatsApp de tu página con Google Tag Manager, o usar los recursos de mensajes de Google, que tienen una acción de conversación iniciada. Un clic en WhatsApp no siempre es una conversación real, así que conviene tratarlo con cuidado como conversión principal.

### ¿Cómo le digo a Google Ads qué contactos se volvieron clientes?

Con las conversiones mejoradas para clientes potenciales: capturas el correo o teléfono en el formulario, registras en tu CRM quién compró y subes esa información a Google Ads. Se puede hacer manualmente, con el administrador de datos de Google Ads o con una integración de tu CRM.
