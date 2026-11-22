---
titulo: Shopify en Colombia: pagos, pesos, envíos y facturación
seo_titulo: Shopify en Colombia: pagos, envíos y facturación
descripcion: Cómo vender con Shopify en Colombia: pasarelas que integran (Wompi, Mercado Pago, PayU), precios en pesos, envíos, contraentrega y factura electrónica DIAN.
palabra_clave: Shopify en Colombia
categoria: shopify
fecha: 2026-11-22
resumen: Shopify funciona en Colombia, pero sin Shopify Payments. Cobras con una pasarela local (Wompi, Mercado Pago, PayU, ePayco u otra), vendes en pesos, despachas con una app de transportadoras y emites la factura electrónica con una integración a tu software contable.
---

¿Se puede vender con Shopify en Colombia? Sí, y funciona muy bien. Pero hay una diferencia importante frente a Estados Unidos o España: a noviembre de 2026, **Shopify Payments no está disponible en Colombia**. Eso significa que cobras con una pasarela de pago local, y que Shopify cobra una comisión adicional por usarla.

Para que una tienda Shopify en Colombia opere bien necesitas resolver cuatro cosas: con qué pasarela cobras (tarjeta, PSE, Nequi), cómo muestras los precios en pesos, cómo despachas (incluida la contraentrega) y cómo emites la factura electrónica ante la DIAN. Si una de las cuatro falla, pierdes ventas o te metes en un problema contable.

Te lo cuento desde la práctica. Además de montar tiendas para clientes de Since, tengo la mía: Cumbre Café Gourmet, el café de especialidad de mi familia en Salamina, Caldas, vende en Shopify con envíos a toda Colombia. Lo que sigue es lo que hay que configurar y en qué orden.

## Pagos en Shopify Colombia: cómo funcionan sin Shopify Payments

En los países donde existe, Shopify Payments es la pasarela propia de Shopify: el cliente paga dentro del checkout y Shopify no cobra comisión extra. En Colombia no está, así que tienes que conectar un proveedor externo.

Las consecuencias prácticas son estas:

- **Pagas dos comisiones por venta**: la de la pasarela y la de Shopify por usar una pasarela externa. La de Shopify depende del plan (aproximadamente 2 % en Basic, 1 % en Grow y menos en Advanced, a noviembre de 2026). Confírmala en Configuración > Pagos de tu administrador.
- **La experiencia de pago cambia según la pasarela**. Algunas abren una ventana o redirigen al cliente a otra página para pagar. Otras permiten pagar con tarjeta sin salir del checkout. Cada salto extra es una oportunidad de que el cliente abandone.
- **Los métodos locales dependen de la pasarela**. PSE, Nequi, Daviplata, Bancolombia o pago en efectivo en puntos físicos no los da Shopify: los da el proveedor que conectes.

### Qué pasarelas de pago integran con Shopify en Colombia

Las opciones cambian, así que la fuente de verdad es tu propio administrador: en Configuración > Pagos aparecen los proveedores disponibles para una tienda registrada en Colombia. A noviembre de 2026, las que más se usan son:

| Pasarela | Cómo se integra | Qué revisar |
|---|---|---|
| Wompi | App en la tienda de apps de Shopify | Si el pago con tarjeta queda dentro del checkout y qué métodos locales habilita |
| Mercado Pago | Proveedor de pagos en el administrador | Si el cliente es redirigido y si le pide crear cuenta |
| PayU | Proveedor de pagos en el administrador | Métodos disponibles y tiempos de desembolso |
| ePayco | Proveedor o app, según disponibilidad | Comisiones vigentes y experiencia de pago |
| PayPal | Proveedor en el administrador | Útil si vendes al exterior |

No te doy las comisiones de cada una porque cambian y dependen del volumen y del método de pago. Pídelas por escrito a cada proveedor y compáralas con tu ticket promedio: un valor fijo por transacción pesa mucho más en una venta de $40.000 que en una de $400.000.

### Cómo elegir la pasarela

Mi criterio, en este orden:

1. **Que el cliente pague con lo que ya usa.** En Colombia eso es tarjeta, PSE y Nequi como mínimo. Si tu público es joven, Nequi y Daviplata pesan mucho.
2. **Que la experiencia tenga los menos pasos posibles.** Prueba tú mismo una compra desde el celular. Si te pide crear una cuenta o te saca a otra página con otro diseño, tu cliente siente lo mismo.
3. **Que le pase el evento de compra correcto a Shopify.** Si la pasarela no devuelve al cliente a la página de confirmación del pedido, la compra puede no registrarse bien en el píxel de Meta y en Google. Esto es crítico si vas a pautar.
4. **Comisión y tiempos de desembolso.** Importan, pero después de lo anterior. Una pasarela un punto más barata que te hace perder ventas en el checkout sale cara.

### Pagos manuales: contraentrega y transferencia

Shopify permite crear métodos de pago manuales, como "Pago contraentrega" o "Transferencia bancaria". El pedido queda pendiente de pago y tú lo marcas como pagado cuando recibes la plata.

La contraentrega sube la conversión en categorías donde el cliente desconfía de pagar por adelantado, pero trae devoluciones y pedidos que nadie recibe. Si la ofreces, confirma cada pedido por WhatsApp antes de despacharlo y evalúa limitarla por zona o por valor del pedido.

## Precios en pesos colombianos

Configura la **moneda de la tienda en pesos colombianos (COP)** desde el inicio. Cambiarla después de tener pedidos es más complicado y puede afectar reportes.

Algunas recomendaciones:

- Revisa el formato del precio para que se vea como lo lee un colombiano: $89.900 y no $89,900.00.
- Decide si tus precios incluyen IVA y configúralo en impuestos. Si tus productos están gravados, lo normal en Colombia es mostrar el precio final con IVA incluido.
- Si vendes al exterior, Shopify permite mercados con otras monedas. Pero si vas a vender solo en Colombia, mantén una sola moneda y una sola configuración. Menos variables, menos errores.

Recuerda que **Shopify te cobra el plan en dólares** aunque tu tienda venda en pesos. En [cuánto cuesta una tienda Shopify en Colombia](/blog/cuanto-cuesta-una-tienda-shopify-en-colombia/) te explico cómo presupuestarlo.

## Envíos: cómo despachar a toda Colombia desde Shopify

Shopify no tiene transportadoras propias en Colombia. Tienes tres caminos:

### 1. Tarifas fijas configuradas a mano

Creas zonas (por ejemplo, tu ciudad, ciudades principales y resto del país) y le pones una tarifa a cada una. Luego generas las guías por fuera, en la página de la transportadora.

Sirve para arrancar con pocos pedidos. El problema es que con volumen se vuelve lento y es fácil equivocarse copiando direcciones.

### 2. Apps de logística que conectan varias transportadoras

Hay apps que conectan tu tienda con varias transportadoras nacionales (Servientrega, Coordinadora, Envía, TCC, Deprisa, Interrapidísimo, según la app). Te permiten generar la guía desde el pedido, comparar tarifas y, en algunos casos, manejar contraentrega y recaudo.

Ejemplos que encontrarás en la tienda de apps de Shopify son Mipaquete y Envia.com, entre otras. Antes de instalar una, lee las reseñas recientes, revisa en qué moneda cobra y prueba con unos cuantos pedidos reales. La calidad del soporte varía mucho entre apps.

### 3. Operador logístico o fulfillment

Si ya tienes volumen, un operador puede almacenar tu inventario, empacar y despachar. Lo normal es que se conecte a Shopify por app o integración y lea los pedidos automáticamente.

### Qué configurar en envíos sí o sí

- **Tiempos de entrega claros** en la página de producto y en el checkout: ciudades principales y municipios no son lo mismo.
- **Umbral de envío gratis** solo si tu margen lo soporta. Calcúlalo así: supongamos que el envío promedio te cuesta $15.000 y tu ticket promedio es $90.000. Si pones envío gratis desde $120.000, empujas al cliente a agregar algo más y el envío se paga con ese margen extra.
- **Peso de cada producto** bien cargado, si usas tarifas calculadas.
- **Notificaciones de seguimiento**: por correo o WhatsApp. Un cliente que sabe dónde está su pedido no te escribe diez veces.

En Cumbre Café, por ejemplo, despachar café a toda Colombia obliga a pensar en empaque y tiempos de entrega, porque el producto llega a ciudades grandes y a municipios pequeños. Ese tipo de decisión no te la resuelve ninguna app: la defines tú según tu producto.

## Facturación electrónica DIAN desde Shopify

Si estás obligado a facturar electrónicamente, Shopify por sí solo **no emite la factura electrónica ante la DIAN**. La forma habitual de resolverlo es una app que conecte Shopify con tu software de facturación.

A noviembre de 2026, en la tienda de apps de Shopify hay integraciones con **Siigo** y **Alegra**, y otros proveedores colombianos que convierten los pedidos en facturas electrónicas y, en algunos casos, generan notas crédito cuando hay reembolsos. Los planes van desde opciones gratuitas hasta unos pocos dólares al mes, según el volumen de documentos.

Antes de elegir:

1. Pregúntale a tu contador qué software usa o recomienda. La integración tiene que llegar a donde él trabaja.
2. Revisa si la app factura automáticamente al pagarse el pedido o si tienes que darle un botón.
3. Confirma cómo maneja devoluciones, descuentos y pedidos contraentrega.
4. Pide al cliente los datos de facturación en el checkout (tipo y número de documento) si los necesitas. Algunas apps agregan esos campos.

Esta parte no la improvises. Un error de configuración aquí se nota meses después, cuando el contador cruza las ventas.

## Orden recomendado para dejar todo listo

1. Moneda en COP e impuestos configurados.
2. Pasarela de pago principal conectada y probada con una compra real.
3. Métodos manuales (transferencia o contraentrega) si los vas a ofrecer.
4. Zonas y tarifas de envío, o app de logística conectada.
5. App de facturación electrónica conectada al software de tu contador.
6. Políticas de envío, cambios y devoluciones publicadas.
7. Píxel de Meta y Google conectados, y verificación de que la compra se registra después de pagar con tu pasarela.

Este último punto es el que más veo fallar. Si vas a pautar, lee [cómo funcionan el píxel de Meta y la API de conversiones](/blog/pixel-de-meta-y-api-de-conversiones/) antes de gastar el primer peso. Y si prefieres que te entreguen la tienda con todo esto resuelto, en [creación de tiendas Shopify](/servicios/tiendas-shopify/) te cuento cómo trabajo.

Si ya tienes la tienda y algo de esto no te cuadra (pagos que no registran, envíos que te comen el margen, facturas que no salen), escríbeme por WhatsApp y revisamos tu configuración.

## Preguntas frecuentes

### ¿Shopify Payments funciona en Colombia?

No. A noviembre de 2026, Shopify Payments no está disponible para tiendas registradas en Colombia. Debes usar una pasarela externa como Wompi, Mercado Pago o PayU, y Shopify cobra una comisión adicional según tu plan.

### ¿Puedo recibir pagos por PSE y Nequi en Shopify?

Sí, a través de la pasarela que conectes. Shopify no ofrece esos métodos directamente; los habilita el proveedor de pagos. Antes de elegir pasarela, verifica cuáles métodos locales incluye y cómo se ve el pago desde el celular.

### ¿Shopify permite contraentrega en Colombia?

Sí, como método de pago manual, y algunas apps de logística manejan el recaudo con la transportadora. Conviene confirmar cada pedido antes de despacharlo para reducir pedidos que no se reciben.

### ¿Shopify genera factura electrónica para la DIAN?

No de forma nativa. Necesitas una app que conecte Shopify con tu software de facturación, como Siigo o Alegra, u otro proveedor autorizado. Coordina con tu contador antes de elegirla.

### ¿Puedo vender en pesos aunque Shopify me cobre en dólares?

Sí. La moneda de tu tienda puede ser pesos colombianos y tus clientes pagan en pesos. Lo que se cobra en dólares es el plan de Shopify y la mayoría de apps.
