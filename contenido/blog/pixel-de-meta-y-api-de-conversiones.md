---
titulo: Píxel de Meta y API de conversiones: qué son y cómo configurarlos
seo_titulo: Píxel de Meta y API de conversiones explicados
descripcion: Qué es el píxel de Meta, qué es la API de conversiones, por qué conviene usar los dos, cómo deduplicar eventos y cómo revisar la calidad de tus datos.
palabra_clave: píxel de Meta y API de conversiones
categoria: meta-ads
fecha: 2026-11-22
resumen: El píxel de Meta mide desde el navegador lo que hace la gente en tu web; la API de conversiones envía esos mismos eventos desde tu servidor. Usar los dos, bien deduplicados, le da a Meta datos más completos para optimizar.
---

El píxel de Meta y la API de conversiones son las dos formas de contarle a Meta qué pasa después de que alguien ve tu anuncio: si visitó tu página, si agregó al carrito, si compró o si dejó sus datos. El píxel lo hace desde el navegador de la persona. La API de conversiones lo hace desde tu servidor o tu plataforma. Lo recomendable hoy es usar los dos al tiempo y configurarlos para que Meta no cuente dos veces el mismo evento.

¿Por qué importa tanto? Porque Meta optimiza con los datos que le das. Si el píxel pierde compras por bloqueadores, por navegadores que limitan cookies o por una mala instalación, el algoritmo aprende de información incompleta. Y tú tomas decisiones con un reporte que no cuadra con tus ventas reales.

Te explico cómo funcionan, cómo saber si están bien y los errores que más veo.

## ¿Qué es el píxel de Meta?

El píxel es un fragmento de código que se instala en tu página web. Cuando alguien entra, el código se ejecuta en su navegador y le envía a Meta eventos como:

- **PageView:** vio una página.
- **ViewContent:** vio un producto o servicio.
- **AddToCart:** agregó al carrito.
- **InitiateCheckout:** empezó el proceso de pago.
- **Purchase:** compró, con el valor y la moneda.
- **Lead:** dejó sus datos en un formulario.

Con esos eventos Meta puede optimizar tus campañas para que busquen personas con más probabilidad de hacer esa acción, crear públicos de remarketing y reportarte resultados.

### La limitación del píxel

El píxel depende del navegador. Si la persona usa un bloqueador de anuncios, si el navegador restringe el rastreo, si la página se cierra antes de que cargue el código o si alguien edita el sitio y borra el script, el evento se pierde. Por eso, con solo el píxel, es común que Meta reporte menos conversiones de las que de verdad ocurrieron.

## ¿Qué es la API de conversiones?

La API de conversiones (Conversions API o CAPI) envía los eventos desde tu servidor directamente a Meta, sin depender del navegador. Cuando alguien compra en tu tienda, tu plataforma le avisa a Meta: "esta persona compró por este valor".

Ventajas principales:

- **Menos pérdida de datos**, porque no depende de bloqueadores ni cookies del navegador.
- **Más información de coincidencia**, como el correo o el teléfono del cliente (enviados de forma cifrada), que ayuda a Meta a relacionar la compra con la persona que vio el anuncio.
- **Eventos que no pasan por la web**, como una venta cerrada por teléfono, en tienda física o en un CRM.

## ¿Por qué usar el píxel y la API de conversiones juntos?

Porque se complementan. El píxel captura bien el comportamiento en el navegador y la API de conversiones cubre lo que el píxel no alcanza. La [recomendación de Meta](https://www.facebook.com/business/help/308855623839366) es implementarlos en conjunto, lo que llama una configuración redundante.

| Aspecto | Píxel de Meta | API de conversiones |
|---|---|---|
| Desde dónde envía | Navegador de la persona | Tu servidor o plataforma |
| Afectado por bloqueadores | Sí | No |
| Instalación | Más sencilla | Requiere integración o configuración |
| Eventos fuera de la web | No | Sí |
| Datos de coincidencia | Limitados | Puede enviar más |

## La deduplicación: el paso que casi todos olvidan

Si envías la misma compra por el píxel y por la API, Meta la puede contar dos veces. Eso infla tu ROAS y le enseña al algoritmo datos falsos.

Para evitarlo existe la [deduplicación](https://developers.facebook.com/documentation/ads-commerce/conversions-api/deduplicate-pixel-and-server-events). Meta identifica que dos eventos son el mismo cuando tienen:

1. **El mismo nombre de evento**, por ejemplo Purchase en los dos lados.
2. **El mismo identificador de evento** (event_id en el servidor y eventID en el píxel).

Si los dos coinciden, Meta se queda con uno solo. Si el identificador falta o no coincide, puede contar el evento doble.

> Una cuenta con compras duplicadas puede mostrar un ROAS espectacular que no existe. Antes de celebrar, compara las compras de Meta con las de tu tienda.

## Calidad de coincidencia de eventos: qué es y cómo mejorarla

En el administrador de eventos, Meta muestra una calificación llamada **calidad de coincidencia de eventos** (Event Match Quality), en una escala de 1 a 10. Indica qué tan bien Meta logra relacionar tus eventos con personas reales en sus plataformas. A noviembre de 2026, Meta recomienda apuntar a una calificación de 6 o más cuando sea posible, y esta métrica está disponible para eventos web, según su [documentación para desarrolladores](https://developers.facebook.com/documentation/ads-commerce/conversions-api/dataset-quality-api).

Para mejorarla:

- Envía por la API de conversiones datos del cliente como correo, teléfono, nombre y ciudad. Meta los procesa cifrados.
- Envía un identificador externo de cliente (external_id) de forma constante.
- Incluye el event_id en todos los eventos.
- Revisa que el teléfono vaya con el indicativo del país (57 para Colombia) y en el formato que pide Meta.

## Cómo configurarlos según tu plataforma

### Si tienes tienda en Shopify

Shopify tiene una integración oficial con Meta que instala el píxel y activa la API de conversiones desde el panel, sin código. Lo importante es elegir el nivel máximo de intercambio de datos que te ofrezca la integración y verificar después en el administrador de eventos que las compras lleguen con valor y moneda. Si además vas a usar catálogo, revisa [cómo conectar Shopify con el catálogo de Meta](/blog/catalogo-de-shopify-para-anuncios/).

### Si tienes WordPress u otra plataforma

Muchas plataformas tienen complementos o integraciones de socios que configuran píxel y API de conversiones. También existe la opción de una configuración por servidor propio o una herramienta intermedia. En cualquier caso, la prueba final es la misma: que los eventos lleguen, sin duplicarse y con buenos datos de coincidencia.

### Si vendes por WhatsApp o por asesoría

Aquí la venta no ocurre en la web. Puedes enviar eventos desde tu CRM, como "cliente potencial calificado" o "venta cerrada", usando la API de conversiones. Así Meta aprende a buscar clientes de verdad y no solo personas que llenan formularios. Es la misma lógica que en Google Ads con las conversiones importadas, que explico en [cómo medir conversiones en Google Ads](/blog/conversiones-en-google-ads/).

## Cómo revisar que todo funcione

Hazlo cada vez que cambies algo en tu web y, como mínimo, una vez al mes:

1. Entra al **administrador de eventos** de Meta y abre tu conjunto de datos.
2. Usa la herramienta de **probar eventos** y haz una compra o un registro de prueba.
3. Confirma que el evento llega por el navegador y por el servidor, y que aparece como deduplicado.
4. Revisa que Purchase traiga **valor y moneda** (COP si vendes en pesos).
5. Mira la **calidad de coincidencia** de tus eventos principales.
6. Compara las compras de los últimos 7 días en Meta con las de tu plataforma. No van a coincidir al 100 %, porque Meta usa su propia ventana de atribución, pero no deberían estar muy lejos.

## Errores comunes con el píxel y la API de conversiones

- **Tener dos píxeles instalados** en la misma web, uno viejo y uno nuevo.
- **Enviar Purchase sin valor** o con el valor en otra moneda.
- **Disparar Purchase en la página de carrito** y no en la de confirmación.
- **No deduplicar** y celebrar un ROAS que no existe.
- **Optimizar para compras sin volumen**: si casi no hay compras, conviene optimizar para un evento anterior mientras se junta información.
- **Instalar y olvidarse**: un cambio de plantilla o de tema puede borrar el código sin que nadie lo note.

Cuando una campaña no vende, la medición es una de las primeras cosas que reviso. Lo explico dentro del diagnóstico completo en [por qué tus anuncios no venden](/blog/por-que-mis-anuncios-no-venden/).

En mi servicio de [trafficker de Meta Ads](/servicios/pauta-meta-ads/), la medición se revisa antes de invertir el primer peso, porque sin datos confiables cualquier optimización es adivinar.

Si no estás seguro de que tu píxel y tu API de conversiones estén midiendo bien, escríbeme por WhatsApp y revisamos tu configuración.

## Preguntas frecuentes

### ¿Necesito la API de conversiones si ya tengo el píxel?

Es muy recomendable. El píxel por sí solo pierde eventos por bloqueadores, restricciones del navegador o fallas de carga. La API de conversiones ayuda a recuperar parte de esa información y le da a Meta más datos para optimizar.

### ¿La API de conversiones es difícil de instalar?

Depende de tu plataforma. En Shopify y otras plataformas grandes se activa desde una integración, sin código. En sitios hechos a la medida o para eventos de un CRM puede requerir apoyo técnico o una herramienta intermedia.

### ¿Por qué Meta y mi tienda muestran números de ventas distintos?

Es normal que no coincidan exactamente. Meta atribuye ventas según su ventana de atribución y puede incluir ventas de personas que vieron el anuncio sin hacer clic. Pero si la diferencia es muy grande, revisa la instalación y la deduplicación.

### ¿Qué es un conjunto de datos en Meta?

Es el lugar en el administrador de eventos donde Meta agrupa los eventos de tu negocio, tanto los del píxel como los de la API de conversiones y otras fuentes. Ahí revisas qué eventos llegan, su calidad y si hay errores.

### ¿El píxel sirve si vendo por WhatsApp?

Sirve para medir lo que pasa en tu web, pero la venta por WhatsApp no la ve. Para eso necesitas registrar las ventas en un CRM o en tu proveedor de WhatsApp Business y enviarlas a Meta como eventos. Así cierras el ciclo entre el anuncio y la venta real.
