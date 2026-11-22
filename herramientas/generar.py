#!/usr/bin/env python3
"""Generador del blog y de los archivos SEO de sebastianrincon.co.

Uso:  python3 herramientas/generar.py

Qué hace (se puede correr las veces que quieras, el resultado es el mismo):
  1. Convierte cada contenido/blog/*.md en sitio/blog/<slug>/index.html
  2. Crea el índice del blog y una página por tema (sitio/blog/tema/<tema>/)
  3. Unifica menú y pie de página en TODAS las páginas del sitio
  4. Actualiza los datos estructurados de la persona (schema Person) en todas las páginas
  5. Inserta "Guías relacionadas" en las páginas de servicio y "Del blog" en la portada
  6. Regenera sitemap.xml y llms.txt

Sin dependencias externas: solo Python 3.
"""
import datetime
import glob
import html
import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = os.path.join(BASE, 'sitio')
CONTENIDO = os.path.join(BASE, 'contenido', 'blog')
DOM = 'https://sebastianrincon.co'
HOY = datetime.date.today().isoformat()
CSS_V = '202611220900'

WA_TXT = 'Hola%20Sebasti%C3%A1n%2C%20vi%20tu%20web%20y%20quiero%20informaci%C3%B3n%20sobre%20pauta%20para%20mi%20empresa%2E'
WA = f'https://wa.me/573013291994?text={WA_TXT}'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'
GO = '<svg class="go" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'

TEMAS = {
    'meta-ads': ('Meta Ads', 'Guías de pauta en Facebook e Instagram: presupuesto, campañas de WhatsApp, píxel, métricas y estructura de campañas.', '/servicios/pauta-meta-ads/', 'Pauta en Meta Ads'),
    'google-ads': ('Google Ads', 'Guías de Google Ads: costos en Colombia, búsqueda para servicios, Performance Max y medición de conversiones.', '/servicios/pauta-google-ads/', 'Pauta en Google Ads'),
    'shopify': ('Shopify', 'Guías para crear y vender con una tienda Shopify en Colombia: costos, pagos, envíos, conversión y catálogos para anuncios.', '/servicios/tiendas-shopify/', 'Tiendas en Shopify'),
    'empresas-de-servicios': ('Empresas de servicios', 'Pauta y embudos para servicios de alto valor: clientes potenciales, seguimiento comercial, salud y costo por cliente.', '/servicios/pauta-empresas-de-servicios/', 'Pauta para empresas de servicios'),
    'estrategia': ('Estrategia', 'Qué es un trafficker, cuánto cobra, cómo elegir agencia, ROAS y cómo auditar tu cuenta publicitaria.', '/servicios/', 'Pauta digital y tiendas Shopify'),
}

SERVICIOS = [
    ('/servicios/pauta-meta-ads/', 'Pauta en Meta Ads'),
    ('/servicios/pauta-google-ads/', 'Pauta en Google Ads'),
    ('/servicios/tiendas-shopify/', 'Tiendas en Shopify'),
    ('/servicios/pauta-empresas-de-servicios/', 'Pauta para empresas de servicios'),
    ('/servicios/publicidad-para-medicos-y-clinicas/', 'Publicidad para médicos y clínicas'),
]

# Qué artículos se muestran en cada página de servicio (categorías o slugs concretos)
RELACIONADOS = {
    'servicios/pauta-meta-ads/index.html': ['meta-ads'],
    'servicios/pauta-google-ads/index.html': ['google-ads'],
    'servicios/tiendas-shopify/index.html': ['shopify'],
    'servicios/pauta-empresas-de-servicios/index.html': ['empresas-de-servicios'],
    'servicios/publicidad-para-medicos-y-clinicas/index.html': ['politicas-de-publicidad-en-salud', 'seguimiento-comercial-con-ia', 'leads-que-no-se-convierten', 'campanas-de-whatsapp-meta-ads', 'embudo-de-venta-para-servicios-high-ticket', 'costo-por-cliente-potencial'],
    'servicios/index.html': ['estrategia'],
    'sobre-mi/index.html': ['que-es-un-trafficker', 'agencia-o-trafficker-freelance', 'cuanto-cobra-un-trafficker', 'auditoria-de-cuenta-publicitaria'],
    'resultados/index.html': ['que-es-el-roas', 'metricas-de-meta-ads', 'costo-por-cliente-potencial', 'auditoria-de-cuenta-publicitaria'],
    'contacto/index.html': ['auditoria-de-cuenta-publicitaria', 'cuanto-cobra-un-trafficker', 'agencia-o-trafficker-freelance'],
}

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

PERSON = {
    "@type": "Person",
    "@id": f"{DOM}/#sebastian",
    "name": "Sebastián Rincón Peña",
    "alternateName": ["Sebastián Rincón", "Sebastian Rincon", "Sebastian Rincon Peña", "Sebastián Rincón trafficker"],
    "givenName": "Sebastián",
    "familyName": "Rincón Peña",
    "url": f"{DOM}/",
    "mainEntityOfPage": f"{DOM}/sobre-mi/",
    "image": {"@type": "ImageObject", "url": f"{DOM}/assets/img/sebastian-rincon.jpg", "width": 720, "height": 840},
    "jobTitle": "Trafficker digital y fundador de Since Agencia Marketing Digital",
    "description": "Sebastián Rincón Peña es un trafficker colombiano con 8 años de experiencia en Meta Ads y Google Ads, especialista en pauta para empresas de servicios de alto valor y creador de tiendas Shopify. Es fundador de Since Agencia Marketing Digital, cofundador de Medipro y CMO de MR Soluciones Integrales.",
    "nationality": {"@type": "Country", "name": "Colombia"},
    "address": {"@type": "PostalAddress", "addressCountry": "CO"},
    "telephone": "+57 301 329 1994",
    "worksFor": [
        {"@id": f"{DOM}/#since"},
        {"@type": "Organization", "name": "MR Soluciones Integrales", "url": "https://mrsolucionesintegrales.co"},
        {"@type": "Organization", "name": "Medipro", "url": "https://medipro.com.co"},
    ],
    "knowsAbout": ["Meta Ads", "Facebook Ads", "Instagram Ads", "Google Ads", "Performance Max", "Shopify", "Ecommerce",
                   "Marketing digital", "Trafficker digital", "Pauta digital", "Pauta para empresas de servicios",
                   "Ventas high ticket", "Embudos de venta", "Campañas de WhatsApp", "Publicidad para médicos y clínicas"],
    "knowsLanguage": "es",
    "sameAs": ["https://www.instagram.com/soysebastianrincon/", "https://www.threads.net/@soysebastianrincon"],
}
SINCE = {
    "@type": "Organization",
    "@id": f"{DOM}/#since",
    "name": "Since Agencia Marketing Digital",
    "url": "https://agenciasincemarketing.com",
    "founder": {"@id": f"{DOM}/#sebastian"},
}
WEBSITE = {
    "@type": "WebSite",
    "@id": f"{DOM}/#web",
    "name": "Sebastián Rincón Peña",
    "alternateName": "Sebastián Rincón",
    "url": f"{DOM}/",
    "inLanguage": "es-CO",
    "publisher": {"@id": f"{DOM}/#sebastian"},
}


# ---------------------------------------------------------------- utilidades
def pref(depth):
    return '../' * depth if depth else './'


def r(url, depth):
    """Convierte una ruta absoluta del sitio (/servicios/...) en relativa a la profundidad dada."""
    if not url.startswith('/') or url.startswith('//'):
        return url
    p = pref(depth)
    u = url.lstrip('/')
    if not u:
        return p
    return (p if depth else '') + u


def fecha_larga(iso):
    d = datetime.date.fromisoformat(iso)
    return f'{d.day} de {MESES[d.month - 1]} de {d.year}'


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- plantillas
def nav(depth, actual):
    def a(url, txt, extra=''):
        cur = ' aria-current="page"' if actual == url or (url != '/' and url == '/blog/' and actual.startswith('/blog/')) else ''
        return f'<a href="{r(url, depth)}"{cur}{extra}>{txt}</a>'
    sub = ''.join(f'<li>{a(u, t)}</li>' for u, t in SERVICIOS)
    serv_cur = ' aria-current="page"' if actual.startswith('/servicios/') else ''
    return f'''<nav class="nav" aria-label="Principal">
  <div class="wrap nav-in">
    <a href="{pref(depth)}" class="logo"><img class="logo-mark" src="{r('/assets/img/marca/sr-mark.png', depth)}" alt="" width="38" height="33"><span>Sebastián Rincón<small>Pauta digital · Embudos de venta</small></span></a>
    <ul class="menu"><li>{a('/sobre-mi/', 'Sobre mí')}</li><li class="has-sub"><a href="{r('/servicios/', depth)}"{serv_cur}>Servicios</a><ul class="sub">{sub}</ul></li><li>{a('/resultados/', 'Resultados')}</li><li>{a('/blog/', 'Blog')}</li><li>{a('/emprendimientos/', 'Emprendimientos')}</li><li class="m-only">{a('/contacto/', 'Contacto')}</li></ul>
    <a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold nav-cta">WhatsApp</a>
    <button class="burger" aria-label="Abrir menú" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 8h18M3 16h18"/></svg></button>
  </div>
</nav>'''


GUIAS_PIE = [
    ('/blog/que-es-un-trafficker/', 'Qué es un trafficker'),
    ('/blog/cuanto-invertir-en-meta-ads/', 'Cuánto invertir en Meta Ads'),
    ('/blog/cuanto-cuesta-google-ads-en-colombia/', 'Cuánto cuesta Google Ads'),
    ('/blog/cuanto-cuesta-una-tienda-shopify-en-colombia/', 'Cuánto cuesta una tienda Shopify'),
    ('/blog/que-es-el-roas/', 'Qué es el ROAS'),
    ('/blog/', 'Todas las guías'),
]


def footer(depth, slugs_existentes):
    serv = ''.join(f'<li><a href="{r(u, depth)}">{t}</a></li>' for u, t in SERVICIOS)
    guias = ''.join(f'<li><a href="{r(u, depth)}">{t}</a></li>' for u, t in GUIAS_PIE
                    if u == '/blog/' or u.strip('/').split('/')[-1] in slugs_existentes)
    return f'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a href="{pref(depth)}" class="logo"><img class="logo-mark" src="{r('/assets/img/marca/sr-mark.png', depth)}" alt="" width="38" height="33"><span>Sebastián Rincón<small>Pauta digital · Embudos de venta</small></span></a>
        <p style="max-width:340px">Sebastián Rincón Peña, trafficker con 8 años invirtiendo en Meta Ads y Google Ads. Fundador de Since Agencia Marketing Digital. Colombia.</p>
      </div>
      <div><h4>Servicios</h4><ul>{serv}</ul></div>
      <div><h4>Guías</h4><ul>{guias}</ul></div>
      <div><h4>Empresas</h4><ul><li><a href="https://agenciasincemarketing.com" target="_blank" rel="noopener">Since Agencia Marketing Digital</a></li><li><a href="https://medipro.com.co" target="_blank" rel="noopener">Medipro</a></li><li><a href="https://cumbrecafegourmet.com" target="_blank" rel="noopener">Cumbre Café Gourmet</a></li><li><a href="https://mrsolucionesintegrales.co" target="_blank" rel="noopener">MR Soluciones Integrales</a></li></ul></div>
      <div><h4>Contacto</h4><ul>
        <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="https://www.instagram.com/soysebastianrincon/" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="https://www.threads.net/@soysebastianrincon" target="_blank" rel="noopener">Threads</a></li>
        <li><a href="{r('/contacto/', depth)}">Contacto</a></li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>© <span data-year></span> Sebastián Rincón Peña</span>
      <span>Colombia · Clientes en Colombia, Estados Unidos, México, Ecuador, Perú, Curazao y más</span>
    </div>
  </div>
</footer>'''


WA_FLOAT = f'<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg></a>'


def closing(titulo='¿Revisamos tu cuenta?'):
    return f'''<section class="closing">
  <div class="wrap closing-grid">
    <div class="rv">
      <span class="kicker">Contacto</span>
      <h2>{titulo}</h2>
      <a class="wa ulink" href="{WA}" target="_blank" rel="noopener">+57 301 329 1994</a>
      <div class="ctas"><a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold">Escríbeme por WhatsApp {ARROW}</a><a href="https://www.instagram.com/soysebastianrincon/" target="_blank" rel="noopener" class="btn btn-line">Instagram</a></div>
    </div>
    <p class="muted rv">Escríbeme con lo que vendes y lo que estás invirtiendo hoy. Te respondo yo, no un asistente.</p>
  </div>
</section>'''


def head(depth, titulo, desc, url, graph, og_type='website', extra=''):
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    return f'''<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="Sebastián Rincón Peña">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{DOM}{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Sebastián Rincón Peña">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{DOM}{url}">
<meta property="og:locale" content="es_CO">
<meta property="og:image" content="{DOM}/assets/img/og-sebastian-rincon.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sebastián Rincón Peña, trafficker en Meta Ads y Google Ads">
{extra}<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B0B0B">
<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-55NCQQNH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
</script>
<link rel="icon" type="image/png" href="{r('/assets/img/marca/favicon.png', depth)}">
<link rel="apple-touch-icon" href="{r('/assets/img/marca/apple-touch-icon.png', depth)}">
<link rel="alternate" type="application/rss+xml" title="Blog de Sebastián Rincón" href="{DOM}/blog/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Roboto:wdth,wght@75..100,400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r('/assets/css/styles.css', depth)}?v={CSS_V}">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>'''


def tail(depth):
    return f'''{WA_FLOAT}
<script src="{r('/assets/js/main.js', depth)}?v={CSS_V}" defer></script>
</body>
</html>
'''


def breadcrumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{DOM}{u}"} for i, (n, u) in enumerate(items)]}


def crumbs_html(items, depth):
    out = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            out.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            out.append(f'<li><a href="{r(u, depth)}">{esc(n)}</a></li>')
    return '<ol class="crumbs">' + ''.join(out) + '</ol>'


# ---------------------------------------------------------------- markdown
def slugify(t):
    t = t.lower()
    for a, b in zip('áéíóúüñ', 'aeiouun'):
        t = t.replace(a, b)
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    return t[:60].strip('-')


def inline(t, depth):
    t = esc(t).replace('&#x27;', "'")
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    def link(m):
        txt, url = m.group(1), html.unescape(m.group(2))
        if url.startswith('/'):
            return f'<a href="{esc(r(url, depth))}">{txt}</a>'
        return f'<a href="{esc(url)}" target="_blank" rel="noopener">{txt}</a>'
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


def md_to_html(md, depth):
    """Devuelve (html_cuerpo, toc, faqs). Las preguntas frecuentes se separan del cuerpo."""
    lines = md.strip('\n').split('\n')
    out, toc, faqs = [], [], []
    i, in_faq = 0, False
    para = []

    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para), depth) + '</p>')
            para.clear()

    while i < len(lines):
        ln = lines[i].rstrip()
        s = ln.strip()
        if not s:
            flush(); i += 1; continue
        if s.startswith('## '):
            flush()
            t = s[3:].strip()
            if re.match(r'preguntas frecuentes', t, re.I):
                in_faq = True; i += 1; continue
            in_faq = False
            hid = slugify(t)
            toc.append((hid, t))
            out.append(f'<h2 id="{hid}">{inline(t, depth)}</h2>')
            i += 1; continue
        if in_faq:
            if s.startswith('### '):
                q = s[4:].strip(); ans = []; i += 1
                while i < len(lines) and not lines[i].strip().startswith('#'):
                    ans.append(lines[i].strip()); i += 1
                blocks = [b for b in re.split(r'\n\s*\n', '\n'.join(ans)) if b.strip()]
                faqs.append((q, [' '.join(b.split('\n')) for b in blocks]))
                continue
            i += 1; continue
        if s.startswith('### '):
            flush(); out.append(f'<h3>{inline(s[4:].strip(), depth)}</h3>'); i += 1; continue
        if re.match(r'^[-*] ', s):
            flush(); items = []
            while i < len(lines) and re.match(r'^\s*[-*] ', lines[i]):
                items.append(re.sub(r'^\s*[-*] ', '', lines[i]).strip()); i += 1
                while i < len(lines) and lines[i].startswith('  ') and lines[i].strip() and not re.match(r'^\s*([-*]|\d+\.) ', lines[i]):
                    items[-1] += ' ' + lines[i].strip(); i += 1
            out.append('<ul>' + ''.join(f'<li>{inline(x, depth)}</li>' for x in items) + '</ul>'); continue
        if re.match(r'^\d+[.)] ', s):
            flush(); items = []
            while i < len(lines) and re.match(r'^\s*\d+[.)] ', lines[i]):
                items.append(re.sub(r'^\s*\d+[.)] ', '', lines[i]).strip()); i += 1
                while i < len(lines) and lines[i].startswith('  ') and lines[i].strip() and not re.match(r'^\s*([-*]|\d+\.) ', lines[i]):
                    items[-1] += ' ' + lines[i].strip(); i += 1
            out.append('<ol>' + ''.join(f'<li>{inline(x, depth)}</li>' for x in items) + '</ol>'); continue
        if s.startswith('|'):
            flush(); rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            hdr = rows[0]; body = [x for x in rows[1:] if not all(re.match(r'^:?-{2,}:?$', c) for c in x)]
            t = '<div class="tbl"><table><thead><tr>' + ''.join(f'<th>{inline(c, depth)}</th>' for c in hdr) + '</tr></thead><tbody>'
            t += ''.join('<tr>' + ''.join(f'<td>{inline(c, depth)}</td>' for c in rw) + '</tr>' for rw in body)
            out.append(t + '</tbody></table></div>'); continue
        if s.startswith('>'):
            flush(); q = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                q.append(lines[i].strip()[1:].strip()); i += 1
            out.append('<blockquote><p>' + inline(' '.join(q), depth) + '</p></blockquote>'); continue
        para.append(s); i += 1
    flush()
    return '\n'.join(out), toc, faqs


def leer_md(path):
    txt = open(path, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', txt, re.S)
    if not m:
        raise ValueError(f'{path}: falta el encabezado ---')
    meta = {}
    for ln in m.group(1).split('\n'):
        if ':' in ln:
            k, v = ln.split(':', 1)
            meta[k.strip()] = v.strip().strip('"')
    meta['slug'] = os.path.splitext(os.path.basename(path))[0]
    meta['cuerpo'] = m.group(2)
    palabras = len(re.findall(r'\w+', m.group(2)))
    meta['palabras'] = palabras
    meta['minutos'] = max(3, round(palabras / 220))
    meta.setdefault('fecha', HOY)
    meta.setdefault('actualizado', meta['fecha'])
    meta.setdefault('categoria', 'estrategia')
    if meta['categoria'] not in TEMAS:
        raise ValueError(f"{path}: categoría desconocida {meta['categoria']}")
    return meta


# ---------------------------------------------------------------- piezas comunes
def fila_articulo(a, depth, n):
    return (f'<a class="row" href="{r("/blog/" + a["slug"] + "/", depth)}"><span class="n">{n:02d}</span><div>'
            f'<h3>{esc(a["titulo"])}</h3><p>{esc(a["descripcion"])}</p></div>{GO}</a>')


def seccion_guias(arts, depth, kicker='Guías', titulo='Guías relacionadas', texto='Lo que le explico a mis clientes antes de invertir, por escrito.'):
    if not arts:
        return ''
    filas = ''.join(fila_articulo(a, depth, i + 1) for i, a in enumerate(arts))
    return f'''<!-- blog:relacionados -->
<section class="">
  <div class="wrap sec">
    <div class="sec-head rv"><span class="kicker">{kicker}</span><h2>{titulo}</h2><p>{texto}</p></div>
    <div><div class="rows rv">{filas}</div><p style="margin-top:30px"><a class="more" href="{r('/blog/', depth)}">Ver todas las guías {ARROW}</a></p></div>
  </div>
</section>
<!-- /blog:relacionados -->'''


# ---------------------------------------------------------------- páginas del blog
def pagina_articulo(a, todos, slugs):
    depth = 2
    url = f'/blog/{a["slug"]}/'
    tema, _, serv_url, serv_nombre = TEMAS[a['categoria']]
    cuerpo, toc, faqs = md_to_html(a['cuerpo'], depth)
    items = [('Inicio', '/'), ('Blog', '/blog/'), (tema, f'/blog/tema/{a["categoria"]}/'), (a['titulo'], url)]
    graph = [
        {"@type": "BlogPosting", "@id": f"{DOM}{url}#articulo", "headline": a['titulo'][:110], "description": a['descripcion'],
         "url": f"{DOM}{url}", "mainEntityOfPage": f"{DOM}{url}", "datePublished": a['fecha'], "dateModified": a['actualizado'],
         "inLanguage": "es-CO", "articleSection": tema, "keywords": a.get('palabra_clave', ''), "wordCount": a['palabras'],
         "image": f"{DOM}/assets/img/og-sebastian-rincon.jpg", "author": {"@id": f"{DOM}/#sebastian"},
         "publisher": {"@id": f"{DOM}/#sebastian"}, "isPartOf": {"@id": f"{DOM}/#web"},
         "about": [{"@type": "Thing", "name": a.get('palabra_clave', tema)}]},
        breadcrumbs(items), PERSON, WEBSITE,
    ]
    if faqs:
        graph.append({"@type": "FAQPage", "@id": f"{DOM}{url}#faq", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ' '.join(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', p).replace('**', '') for p in ps)}}
            for q, ps in faqs]})
    seo = a.get('seo_titulo') or a['titulo']
    titulo_tag = f"{seo} | Sebastián Rincón"
    extra = (f'<meta property="article:published_time" content="{a["fecha"]}">\n'
             f'<meta property="article:modified_time" content="{a["actualizado"]}">\n'
             f'<meta property="article:author" content="Sebastián Rincón Peña">\n'
             f'<meta property="article:section" content="{esc(tema)}">\n')
    toc_html = ''.join(f'<li><a href="#{h}">{esc(t)}</a></li>' for h, t in toc)
    if faqs:
        toc_html += '<li><a href="#preguntas-frecuentes">Preguntas frecuentes</a></li>'
    faq_html = ''
    if faqs:
        faq_html = '<h2 id="preguntas-frecuentes">Preguntas frecuentes</h2><div class="faq">' + ''.join(
            f'<details><summary>{inline(q, depth)}</summary>' + ''.join(f'<p>{inline(p, depth)}</p>' for p in ps) + '</details>'
            for q, ps in faqs) + '</div>'
    rel = [x for x in todos if x['categoria'] == a['categoria'] and x['slug'] != a['slug']][:3]
    if len(rel) < 3:
        rel += [x for x in todos if x['slug'] != a['slug'] and x not in rel][:3 - len(rel)]
    pic = r('/assets/img/sebastian-rincon-retrato', depth)
    out = head(depth, titulo_tag, a['descripcion'], url, graph, og_type='article', extra=extra)
    out += '\n' + nav(depth, url) + f'''

<main>
<header class="page-hero art-hero">
  <div class="wrap">
    {crumbs_html(items, depth)}
    <div class="rv">
      <span class="kicker"><b>{esc(tema)}</b> · {a['minutos']} min de lectura</span>
      <h1>{esc(a['titulo'])}</h1>
      <p class="lead">{esc(a['descripcion'])}</p>
      <div class="byline"><picture><source srcset="{pic}.webp" type="image/webp"><img src="{pic}.jpg" alt="Sebastián Rincón Peña" width="44" height="51"></picture><div><a href="{r('/sobre-mi/', depth)}" rel="author">Sebastián Rincón Peña</a><span>Trafficker · Actualizado el <time datetime="{a['actualizado']}">{fecha_larga(a['actualizado'])}</time></span></div></div>
    </div>
  </div>
</header>

<section class="art-sec">
  <div class="wrap art-grid">
    <aside class="art-side">
      <nav class="toc" aria-label="Contenido del artículo"><h2>Contenido</h2><ol>{toc_html}</ol></nav>
      <div class="side-cta"><span class="kicker">Servicio</span><p><strong>{esc(serv_nombre)}</strong><br>¿Prefieres que lo haga por ti? Revisemos tu caso.</p><a class="more" href="{r(serv_url, depth)}">Ver servicio {ARROW}</a></div>
    </aside>
    <article class="article">
      <div class="tldr"><b>En corto</b><p>{inline(a.get('resumen', a['descripcion']), depth)}</p></div>
{cuerpo}
      <div class="art-cta"><p><strong>¿Quieres que revise tu caso?</strong> Escríbeme por WhatsApp con lo que vendes y cuánto inviertes hoy, y te digo por dónde empezaría.</p><a href="{WA}" target="_blank" rel="noopener" class="btn btn-gold">Escríbeme por WhatsApp {ARROW}</a></div>
      {faq_html}
      <div class="author-box"><picture><source srcset="{pic}.webp" type="image/webp"><img src="{pic}.jpg" alt="Sebastián Rincón Peña" width="96" height="112" loading="lazy"></picture><div><span class="kicker">Sobre el autor</span><p><strong>Sebastián Rincón Peña</strong> es trafficker con 8 años haciendo pauta en Meta Ads y Google Ads y creando tiendas en Shopify. Fundó <a href="https://agenciasincemarketing.com" target="_blank" rel="noopener">Since Agencia Marketing Digital</a>, que ha acompañado a más de 100 empresas en Colombia y el exterior, y es cofundador de Medipro.</p><a class="more" href="{r('/sobre-mi/', depth)}">Conoce a Sebastián {ARROW}</a></div></div>
    </article>
  </div>
</section>

{seccion_guias(rel, depth, kicker='Sigue leyendo', titulo='Más guías', texto='Otras guías que te pueden servir.')}

{closing()}

</main>

{footer(depth, slugs)}

{tail(depth)}'''
    return out


def pagina_lista(depth, url, titulo_tag, desc, h1, lead, items_crumbs, grupos, kicker, graph_extra, slugs, chips_actual=None):
    graph = [{"@type": "CollectionPage", "@id": f"{DOM}{url}#pagina", "name": h1, "description": desc, "url": f"{DOM}{url}",
              "inLanguage": "es-CO", "isPartOf": {"@id": f"{DOM}/#web"}, "author": {"@id": f"{DOM}/#sebastian"}},
             breadcrumbs(items_crumbs), PERSON, WEBSITE] + graph_extra
    chips = '<ul class="chips">' + f'<li><a href="{r("/blog/", depth)}"{" aria-current=\"page\"" if chips_actual is None else ""}>Todas</a></li>' + ''.join(
        f'<li><a href="{r(f"/blog/tema/{k}/", depth)}"{" aria-current=\"page\"" if chips_actual == k else ""}>{v[0]}</a></li>' for k, v in TEMAS.items()) + '</ul>'
    secs = ''
    for i, (k, t, p, arts, link) in enumerate(grupos):
        filas = ''.join(fila_articulo(a, depth, j + 1) for j, a in enumerate(arts))
        more = f'<p style="margin-top:30px"><a class="more" href="{r(link[0], depth)}">{link[1]} {ARROW}</a></p>' if link else ''
        secs += f'''
<section class="{'paper' if i % 2 else ''}">
  <div class="wrap sec">
    <div class="sec-head rv"><span class="kicker">{k}</span><h2>{t}</h2><p>{p}</p></div>
    <div><div class="rows rv">{filas}</div>{more}</div>
  </div>
</section>
'''
    out = head(depth, titulo_tag, desc, url, graph) + '\n' + nav(depth, url) + f'''

<main>
<header class="page-hero">
  <div class="wrap">
    {crumbs_html(items_crumbs, depth)}
    <div class="ph-grid">
      <div class="rv">
        <span class="kicker">{kicker}</span>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        {chips}
      </div>
      <div class="aside-box rv"><h2>Escrito por</h2><ul><li>Sebastián Rincón Peña</li><li>8 años en Meta Ads y Google Ads</li><li>Fundador de Since Agencia Marketing Digital</li><li>Más de 100 empresas acompañadas</li></ul></div>
    </div>
  </div>
</header>
{secs}
{closing()}

</main>

{footer(depth, slugs)}

{tail(depth)}'''
    return out


# ---------------------------------------------------------------- páginas existentes
def depth_de(rel_path):
    return rel_path.count('/')


def url_de(rel_path):
    u = '/' + rel_path[:-len('index.html')] if rel_path.endswith('index.html') else '/' + rel_path
    return u


def actualizar_jsonld(s, rel_path):
    m = re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', s, re.S)
    if not m:
        return s
    data = json.loads(m.group(1))
    graph = data.get('@graph', [data])
    nuevo, tiene_web, tiene_since = [], False, False
    for n in graph:
        t = n.get('@type')
        if t == 'Person' and n.get('@id', '').endswith('#sebastian'):
            nuevo.append(PERSON); continue
        if t == 'WebSite':
            nuevo.append(WEBSITE); tiene_web = True; continue
        if n.get('@id') == f'{DOM}/#since':
            nuevo.append(SINCE); tiene_since = True; continue
        nuevo.append(n)
    if not any(n.get('@type') == 'Person' for n in nuevo):
        nuevo.insert(0, PERSON)
    if not tiene_web:
        nuevo.append(WEBSITE)
    if not tiene_since:
        nuevo.append(SINCE)
    url = url_de(rel_path)
    if rel_path == 'sobre-mi/index.html' and not any(n.get('@type') == 'ProfilePage' for n in nuevo):
        nuevo.append({"@type": "ProfilePage", "@id": f"{DOM}/sobre-mi/#pagina", "url": f"{DOM}/sobre-mi/",
                      "name": "Sobre Sebastián Rincón Peña", "mainEntity": {"@id": f"{DOM}/#sebastian"},
                      "isPartOf": {"@id": f"{DOM}/#web"}, "inLanguage": "es-CO", "dateModified": HOY})
    ld = json.dumps({"@context": "https://schema.org", "@graph": nuevo}, ensure_ascii=False, indent=2)
    return s[:m.start(1)] + ld + s[m.end(1):]


def actualizar_existente(rel_path, arts, slugs):
    path = os.path.join(SITIO, rel_path)
    s = open(path, encoding='utf-8').read()
    depth = depth_de(rel_path)
    url = url_de(rel_path)
    s = re.sub(r'<nav class="nav".*?</nav>', lambda m: nav(depth, url), s, count=1, flags=re.S)
    s = re.sub(r'<footer>.*?</footer>', lambda m: footer(depth, slugs), s, count=1, flags=re.S)
    s = re.sub(r'styles\.css\?v=\d+', f'styles.css?v={CSS_V}', s)
    s = re.sub(r'main\.js\?v=\d+', f'main.js?v={CSS_V}', s)
    if 'og:image:width' not in s:
        s = s.replace('<meta name="twitter:card"', '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n<meta property="og:image:alt" content="Sebastián Rincón Peña, trafficker en Meta Ads y Google Ads">\n<meta name="twitter:card"', 1)
    if 'application/rss+xml' not in s and '<link rel="preconnect"' in s:
        s = s.replace('<link rel="preconnect"', f'<link rel="alternate" type="application/rss+xml" title="Blog de Sebastián Rincón" href="{DOM}/blog/feed.xml">\n<link rel="preconnect"', 1)
    s = s.replace('content="index, follow, max-image-preview:large"', 'content="index, follow, max-image-preview:large, max-snippet:-1"')
    s = actualizar_jsonld(s, rel_path)
    # bloque de guías relacionadas
    s = re.sub(r'\n?<!-- blog:relacionados -->.*?<!-- /blog:relacionados -->\n?', '\n', s, flags=re.S)
    claves = RELACIONADOS.get(rel_path)
    bloque = ''
    if rel_path == 'index.html':
        orden = ['que-es-un-trafficker', 'cuanto-invertir-en-meta-ads', 'embudo-de-venta-para-servicios-high-ticket',
                 'google-ads-vs-meta-ads', 'cuanto-cuesta-una-tienda-shopify-en-colombia', 'que-es-el-roas']
        sel = [a for k in orden for a in arts if a['slug'] == k]
        bloque = seccion_guias(sel, depth, kicker='Blog', titulo='Guías para invertir mejor', texto='Lo que le explico a mis clientes antes de invertir un peso, escrito para que lo apliques en tu negocio.')
    elif claves:
        sel = [a for a in arts if a['categoria'] in claves] + [a for k in claves for a in arts if a['slug'] == k]
        bloque = seccion_guias(sel[:6], depth)
    if bloque:
        # antes de "Otros servicios" si existe; si no, antes del cierre
        idx = s.find('<span class="kicker">Otros servicios</span>')
        if idx > -1:
            idx = s.rfind('<section', 0, idx)
        else:
            idx = s.find('<section class="closing">')
        if idx == -1:
            idx = s.find('</main>')
        s = s[:idx] + bloque + '\n\n' + s[idx:]
    open(path, 'w', encoding='utf-8').write(s)


# ---------------------------------------------------------------- sitemap, llms, feed
def sitemap(arts):
    fechas = {f'/blog/{a["slug"]}/': a['actualizado'] for a in arts}
    urls = []
    for f in sorted(glob.glob(os.path.join(SITIO, '**', 'index.html'), recursive=True)):
        rel = os.path.relpath(f, SITIO).replace(os.sep, '/')
        u = url_de(rel)
        txt = open(f, encoding='utf-8').read()
        if 'noindex' in txt[:3000]:
            continue
        if u == '/':
            pr = '1.0'
        elif u.startswith('/servicios/') or u in ('/sobre-mi/',):
            pr = '0.9'
        elif u.startswith('/blog/') and u.count('/') == 3 and not u.startswith('/blog/tema/'):
            pr = '0.7'
        else:
            pr = '0.6'
        urls.append(f'  <url><loc>{DOM}{u}</loc><lastmod>{fechas.get(u, HOY)}</lastmod><priority>{pr}</priority></url>')
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(urls) + '\n</urlset>\n'
    open(os.path.join(SITIO, 'sitemap.xml'), 'w', encoding='utf-8').write(x)
    return len(urls)


def feed(arts):
    items = ''
    for a in sorted(arts, key=lambda x: x['fecha'], reverse=True):
        d = datetime.date.fromisoformat(a['fecha'])
        pub = d.strftime('%a, %d %b %Y 09:00:00 -0500')
        items += (f'<item><title>{esc(a["titulo"])}</title><link>{DOM}/blog/{a["slug"]}/</link>'
                  f'<guid>{DOM}/blog/{a["slug"]}/</guid><pubDate>{pub}</pubDate>'
                  f'<description>{esc(a["descripcion"])}</description></item>\n')
    x = (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Blog de Sebastián Rincón Peña</title>'
         f'<link>{DOM}/blog/</link><description>Guías de pauta en Meta Ads, Google Ads, Shopify y embudos de venta.</description>'
         f'<language>es-co</language>\n{items}</channel></rss>\n')
    open(os.path.join(SITIO, 'blog', 'feed.xml'), 'w', encoding='utf-8').write(x)


def llms(arts):
    L = ['# Sebastián Rincón Peña', '',
         '> Sebastián Rincón Peña (también escrito Sebastian Rincon) es un trafficker colombiano con 8 años de experiencia en pauta en Meta Ads (Facebook e Instagram) y Google Ads, especialista en empresas de servicios de alto valor (high ticket), ventas por WhatsApp y creación de tiendas Shopify. Es fundador de Since Agencia Marketing Digital, cofundador de Medipro y CMO de MR Soluciones Integrales.',
         '',
         '- Sitio oficial: https://sebastianrincon.co/',
         '- Contacto: WhatsApp +57 301 329 1994 · Instagram @soysebastianrincon',
         '- Ubicación: Colombia. Atiende empresas en Colombia, Estados Unidos, México, Ecuador, Perú, Curazao y otros países.',
         '- Agencia: Since Agencia Marketing Digital (https://agenciasincemarketing.com), más de 100 empresas acompañadas, equipo de 13 personas.',
         '- Resultados publicados por Since: ROAS reportado por clientes entre 4x y 30x en Meta Ads.',
         '', '## Páginas principales', '',
         f'- [Sobre Sebastián Rincón Peña]({DOM}/sobre-mi/): historia, principios y empresas que lidera.',
         f'- [Servicios]({DOM}/servicios/): pauta digital, embudos de venta y tiendas Shopify.',
         f'- [Resultados]({DOM}/resultados/): casos de éxito en Meta Ads y Google Ads.',
         f'- [Emprendimientos]({DOM}/emprendimientos/): Since, Medipro, Cumbre Café Gourmet y MR Soluciones Integrales.',
         f'- [Contacto]({DOM}/contacto/): WhatsApp e Instagram.',
         '', '## Servicios', '',
         f'- [Trafficker de Meta Ads]({DOM}/servicios/pauta-meta-ads/): campañas de ventas, mensajes a WhatsApp y clientes potenciales en Facebook e Instagram.',
         f'- [Especialista en Google Ads]({DOM}/servicios/pauta-google-ads/): búsqueda, Shopping, Performance Max y YouTube.',
         f'- [Creación de tiendas Shopify]({DOM}/servicios/tiendas-shopify/): ecommerce listo para vender y para recibir tráfico de pauta.',
         f'- [Pauta para empresas de servicios]({DOM}/servicios/pauta-empresas-de-servicios/): servicios high ticket con embudo de venta hasta el cierre.',
         f'- [Publicidad para médicos y clínicas]({DOM}/servicios/publicidad-para-medicos-y-clinicas/): pacientes desde Meta Ads y Google Ads cumpliendo las políticas de salud.',
         '', '## Guías del blog', '']
    for k, v in TEMAS.items():
        sel = [a for a in arts if a['categoria'] == k]
        if not sel:
            continue
        L.append(f'### {v[0]}')
        L.append('')
        for a in sel:
            L.append(f'- [{a["titulo"]}]({DOM}/blog/{a["slug"]}/): {a.get("resumen", a["descripcion"])}')
        L.append('')
    open(os.path.join(SITIO, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(L).rstrip() + '\n')


# ---------------------------------------------------------------- principal
def main():
    arts = [leer_md(p) for p in sorted(glob.glob(os.path.join(CONTENIDO, '*.md')))]
    orden_tema = list(TEMAS)
    arts.sort(key=lambda a: (orden_tema.index(a['categoria']), a.get('orden', '50'), a['slug']))
    slugs = {a['slug'] for a in arts}
    errores = []
    for a in arts:
        for campo in ('titulo', 'descripcion'):
            if not a.get(campo):
                errores.append(f'{a["slug"]}: falta {campo}')
        for u in re.findall(r'\]\((/[^)\s]*)\)', a['cuerpo']):
            p = u.split('#')[0]
            if p.startswith('/blog/') and p.strip('/').split('/')[-1] not in slugs and p != '/blog/':
                errores.append(f'{a["slug"]}: enlace a artículo inexistente {u}')
            elif not p.startswith('/blog/') and not os.path.exists(os.path.join(SITIO, p.lstrip('/'), 'index.html')) and not os.path.exists(os.path.join(SITIO, p.lstrip('/'))):
                errores.append(f'{a["slug"]}: enlace roto {u}')
    # artículos
    for a in arts:
        d = os.path.join(SITIO, 'blog', a['slug'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(pagina_articulo(a, arts, slugs))
    # índice del blog
    grupos = []
    for k, v in TEMAS.items():
        sel = [a for a in arts if a['categoria'] == k]
        if sel:
            grupos.append(('Tema', v[0], v[1], sel, (v[2], f'Servicio: {v[3]}')))
    lista_items = [{"@type": "ListItem", "position": i + 1, "url": f"{DOM}/blog/{a['slug']}/", "name": a['titulo']} for i, a in enumerate(arts)]
    os.makedirs(os.path.join(SITIO, 'blog'), exist_ok=True)
    open(os.path.join(SITIO, 'blog', 'index.html'), 'w', encoding='utf-8').write(pagina_lista(
        1, '/blog/', 'Blog de Meta Ads, Google Ads y Shopify | Sebastián Rincón',
        'Guías prácticas de Sebastián Rincón sobre Meta Ads, Google Ads, Shopify y embudos de venta para empresas de servicios en Colombia y el exterior.',
        'Blog de pauta digital', 'Guías sobre Meta Ads, Google Ads, Shopify y embudos de venta, con los números sobre la mesa. Lo que aprendí en 8 años invirtiendo en pauta, explicado sin humo.',
        [('Inicio', '/'), ('Blog', '/blog/')], grupos, '<b>Blog</b> · Guías de Sebastián Rincón',
        [{"@type": "ItemList", "itemListElement": lista_items}], slugs))
    # páginas por tema
    for k, v in TEMAS.items():
        sel = [a for a in arts if a['categoria'] == k]
        if not sel:
            continue
        u = f'/blog/tema/{k}/'
        d = os.path.join(SITIO, 'blog', 'tema', k)
        os.makedirs(d, exist_ok=True)
        li = [{"@type": "ListItem", "position": i + 1, "url": f"{DOM}/blog/{a['slug']}/", "name": a['titulo']} for i, a in enumerate(sel)]
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(pagina_lista(
            3, u, f'Guías de {v[0]} | Blog de Sebastián Rincón', v[1][:158], f'Guías de {v[0]}', v[1],
            [('Inicio', '/'), ('Blog', '/blog/'), (v[0], u)],
            [('Guías', v[0], f'{len(sel)} guías escritas por Sebastián Rincón Peña.', sel, (v[2], f'Servicio: {v[3]}'))],
            f'<b>Blog</b> · {v[0]}', [{"@type": "ItemList", "itemListElement": li}], slugs, chips_actual=k))
    # páginas existentes
    generadas = {'blog/index.html'} | {f'blog/{a["slug"]}/index.html' for a in arts} | {f'blog/tema/{k}/index.html' for k in TEMAS}
    for f in sorted(glob.glob(os.path.join(SITIO, '**', 'index.html'), recursive=True)):
        rel = os.path.relpath(f, SITIO).replace(os.sep, '/')
        if rel in generadas:
            continue
        actualizar_existente(rel, arts, slugs)
    n = sitemap(arts)
    feed(arts)
    llms(arts)
    print(f'{len(arts)} artículos, {n} URLs en el sitemap')
    for e in errores:
        print('AVISO:', e)


if __name__ == '__main__':
    main()
