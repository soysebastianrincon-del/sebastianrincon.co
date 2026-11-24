import sys
sys.path.insert(0, '/home/user/sebastianrincon.co/herramientas')
import generar as g

D = 1
U = '/paginas-web-y-tiendas-shopify/'
T = 'Páginas web y tiendas Shopify en Colombia | Sebastián Rincón'
DESC = 'Diseño de páginas web, landing pages y tiendas Shopify listas para vender y para recibir pauta en Google y Meta. Precios desde y cotización por WhatsApp.'
A = g.ARROW
CHECK = '<svg class="ck" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
WA = g.WA

PAQUETES = [
    ('Landing page', 'PRECIO_LANDING', 'Una sola página enfocada en una oferta, hecha para recibir tráfico de Google Ads o Meta Ads y convertirlo en contactos.',
     ['Diseño a la medida de tu marca', 'Pensada primero para celular', 'Botón y formulario que llevan a tu WhatsApp', 'Google Tag Manager, Analytics y píxel de Meta', 'Textos orientados a vender', 'SEO básico']),
    ('Página web', 'PRECIO_WEB', 'La web de tu empresa con varias páginas: inicio, servicios, nosotros y contacto, para que te encuentren y te escriban.',
     ['Todo lo de la landing page', 'Varias páginas internas', 'Estructura pensada para posicionar en Google', 'Velocidad y versión móvil cuidadas', 'Capacitación para editarla']),
    ('Tienda Shopify', 'PRECIO_SHOPIFY', 'Tu ecommerce en Shopify listo para vender: catálogo, pagos, envíos y medición desde el primer día.',
     ['Tema configurado con tu identidad', 'Catálogo, variantes y colecciones', 'Pasarelas de pago y envíos en Colombia', 'Píxel de Meta, Google y analítica', 'Catálogo conectado a Meta y Google Shopping', 'Capacitación para administrarla']),
]

FAQ = [
    ('¿Qué incluye el precio "desde"?', 'Es el valor base de cada paquete. El precio final depende de cuántas páginas o productos necesites, de las integraciones y de si ya tienes textos y fotos. Te doy un valor cerrado antes de empezar.'),
    ('¿Puedo administrar la página o la tienda yo mismo?', 'Sí. Al entregarla te enseño a cambiar textos, subir productos, gestionar pedidos y crear promociones, según el paquete.'),
    ('¿El plan de Shopify está incluido?', 'No. El plan mensual de Shopify se paga directamente a Shopify desde tu cuenta, así la tienda queda a tu nombre. Te ayudo a elegir el plan que necesitas.'),
    ('¿También me hacen la pauta en Google o Meta?', 'Sí, es mi especialidad. Puedo encargarme de la página y de las campañas en Google Ads y Meta Ads que le llevan clientes, con la medición conectada desde el primer día.'),
    ('¿Trabajan con empresas fuera de Colombia?', 'Sí. Trabajo con empresas en Colombia, Estados Unidos, México, Ecuador, Perú, Curazao y otros países.'),
]

graph = [g.PERSON, g.WEBSITE,
         {"@type": "Service", "@id": f"{g.DOM}{U}#servicio", "name": "Páginas web y tiendas Shopify",
          "serviceType": "Diseño de páginas web, landing pages y tiendas Shopify", "description": DESC, "url": f"{g.DOM}{U}",
          "provider": {"@id": f"{g.DOM}/#sebastian"},
          "areaServed": ["Colombia", "Estados Unidos", "México", "Ecuador", "Perú", "Curazao"]},
         {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]

head = g.head(D, T, DESC, U, graph).replace(
    'content="index, follow, max-image-preview:large, max-snippet:-1"', 'content="noindex, follow"')
r = lambda u: g.r(u, D)

paq = ''
for nombre, precio, desc, items in PAQUETES:
    lis = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in items)
    paq += (f'<li class="pkg"><h3>{nombre}</h3><p class="pkg-price"><span>Desde</span> <b>{precio}</b></p>'
            f'<p class="pkg-desc">{desc}</p><ul>{lis}</ul>'
            f'<a href="{WA}" target="_blank" rel="noopener" class="btn btn-line">Cotizar {nombre[0].lower() + nombre[1:]} {A}</a></li>')

faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)

body = f'''
<header class="nav lp-top">
  <div class="wrap nav-in">
    <a href="{r('/')}" class="logo"><img class="logo-mark" src="{r('/assets/img/marca/sr-mark.png')}" alt="" width="38" height="33"><span>Sebastián Rincón<small>Páginas web · Tiendas Shopify</small></span></a>
    <a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold lp-top-cta">WhatsApp</a>
  </div>
</header>

<main id="main">
<header class="svc-hero lp-hero">
  <div class="wrap">
    <div class="svc-grid">
      <div class="svc-copy">
        <p class="hx-tag">Páginas web · Landing pages · Tiendas Shopify</p>
        <h1>Páginas web y tiendas Shopify hechas para vender</h1>
        <p class="lead">Diseño tu página o tu tienda con mirada de trafficker: rápida, clara y lista para recibir pauta en Google y Meta y convertir visitas en mensajes y ventas.</p>
        <div class="ctas"><a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold">Cotizar por WhatsApp {A}</a><a href="#paquetes" class="btn btn-line">Ver paquetes y precios</a></div>
      </div>
      <aside class="fit"><h2>Es para ti si</h2><ul><li>{CHECK}<span>Tu negocio no tiene página web o la que tienes no te trae clientes</span></li><li>{CHECK}<span>Vendes por redes o WhatsApp y quieres tu tienda en línea</span></li><li>{CHECK}<span>Vas a hacer pauta y necesitas una página que convierta</span></li><li>{CHECK}<span>Quieres a alguien que entienda de ventas, no solo de diseño</span></li></ul></aside>
    </div>
  </div>
  <div class="proof"><div class="wrap proof-in"><p><b>8</b><span>años haciendo pauta en Meta Ads y Google Ads</span></p><p><b>+100</b><span>empresas acompañadas desde Since</span></p><p><b>13</b><span>personas en el equipo, con desarrollo web y diseño</span></p></div></div>
</header>

<section class="svc-intro">
  <div class="wrap intro-grid">
    <figure class="intro-photo rv"><div class="intro-frame"><picture><source srcset="{r('/assets/img/sebastian-rincon-trabajo.webp')}" type="image/webp"><img src="{r('/assets/img/sebastian-rincon-trabajo.jpg')}" alt="Sebastián Rincón Peña revisando una página web en su escritorio" width="720" height="840" loading="lazy"></picture></div><figcaption><b>Sebastián Rincón Peña</b><span>Trafficker · Fundador de Since</span></figcaption></figure>
    <div class="intro-text"><h2 class="rv">Una web bonita no es suficiente</h2><div class="prose rv">
<p>La mayoría de páginas se ven bien pero no venden: cargan lento en el celular, no dicen claro qué ofreces, esconden el WhatsApp y no miden nada. Cuando les llega tráfico pagado, la plata se va sin dejar clientes.</p>
<p>Llevo <strong>8 años haciendo pauta</strong> y sé lo que pasa cuando una persona llega desde un anuncio. Por eso diseño cada página para que <strong>cargue rápido, genere confianza y lleve al contacto</strong>, con la medición de Google y Meta conectada desde el primer día.</p>
<p>Detrás está el equipo de <strong>Since Agencia Marketing Digital</strong>: desarrollo web, diseño y pauta trabajando sobre el mismo objetivo, que tu página traiga clientes.</p>
</div></div>
  </div>
</section>

<section class="paper lp-pkgs" id="paquetes">
  <div class="wrap">
    <div class="split-head rv"><h2>Paquetes y precios</h2><p>Precios de referencia. El valor final depende de lo que necesites y te lo confirmo antes de empezar.</p></div>
    <ol class="pkgs rv">{paq}</ol>
  </div>
</section>

<!-- PORTAFOLIO: se agrega cuando haya webs de clientes autorizadas -->

<section class="svc-process">
  <div class="wrap"><div class="split-head rv"><h2>Cómo trabajamos</h2></div><ol class="process timeline rv">
  <li><span class="n">01</span><h3>Diagnóstico</h3><p>Me cuentas qué vendes, a quién y qué quieres lograr con la página.</p></li>
  <li><span class="n">02</span><h3>Propuesta</h3><p>Estructura, paquete y precio cerrado por escrito antes de empezar.</p></li>
  <li><span class="n">03</span><h3>Diseño y montaje</h3><p>Construimos la página o la tienda y la revisas antes de publicar.</p></li>
  <li><span class="n">04</span><h3>Entrega</h3><p>Publicamos, conectamos la medición y te enseño a administrarla.</p></li>
</ol></div>
</section>

<section class="lp-form-sec" id="cotizar">
  <div class="wrap lp-form-grid">
    <div class="rv"><h2>Cotiza en 1 minuto</h2><p class="muted">Responde estas preguntas y se abre WhatsApp con tu mensaje listo. Te respondo con el paquete y el precio que te sirve.</p></div>
    <form id="leadForm" class="lp-form rv">
      <div><label for="f-nombre">Tu nombre</label><input id="f-nombre" name="nombre" required autocomplete="name"></div>
      <div><label for="f-empresa">Empresa o marca</label><input id="f-empresa" name="empresa" autocomplete="organization"></div>
      <div class="full"><label for="f-servicio">¿Qué necesitas?</label><select id="f-servicio" name="servicio" required><option value="">Elige una opción</option><option>Landing page</option><option>Página web</option><option>Tienda Shopify</option><option>Página o tienda + pauta en Google/Meta</option><option>No estoy seguro</option></select></div>
      <div class="full"><label for="f-mensaje">¿Qué vendes?</label><textarea id="f-mensaje" name="mensaje" rows="3" placeholder="Ej.: tratamientos de estética en Bogotá"></textarea></div>
      <button type="submit" class="btn btn-gold full">Enviar por WhatsApp {A}</button>
    </form>
  </div>
</section>

<section class="svc-faq">
  <div class="wrap faq-grid">
    <div class="faq-head rv"><h2>Preguntas frecuentes</h2><p>¿Tienes otra pregunta? Escríbeme y te respondo yo.</p><a class="more" href="{WA}" target="_blank" rel="noopener">Preguntar por WhatsApp {A}</a></div>
    <div class="faq rv">{faq}</div>
  </div>
</section>

{g.closing('¿Hacemos tu página?')}

</main>

<footer class="lp-foot">
  <div class="wrap"><span>© <span data-year></span> Sebastián Rincón Peña · Colombia</span><a href="{r('/')}">sebastianrincon.co</a></div>
</footer>
'''
html = head + '\n' + body + '\n' + g.tail(D)
import os
os.makedirs('/home/user/sebastianrincon.co/sitio' + U, exist_ok=True)
open('/home/user/sebastianrincon.co/sitio' + U + 'index.html', 'w').write(html)
print('ok')
