# SEO: qué se hizo y qué te toca a ti

## Lo que ya quedó hecho (rama `claude/seo-z4nmrv`)

**Contenido**
- Blog nuevo en `/blog/` con **26 guías** de 1.400 a 1.900 palabras cada una, unas 42.000 palabras en total. Están en 5 temas: Meta Ads, Google Ads, Shopify, empresas de servicios y estrategia.
- Hay una página por tema (`/blog/tema/meta-ads/`, etc.) y un feed RSS (`/blog/feed.xml`).
- Página de servicio nueva: **Publicidad para médicos y clínicas** (`/servicios/publicidad-para-medicos-y-clinicas/`).
- Las 4 páginas de servicio tienen una sección nueva con más texto y 4 preguntas frecuentes más cada una.
- "Sobre mí" tiene la sección nueva **"¿Quién es Sebastián Rincón?"** y preguntas frecuentes sobre ti, pensadas para las búsquedas de tu nombre.
- Cada servicio, la portada, "Sobre mí", "Resultados" y "Contacto" enlazan a las guías relacionadas. Así se refuerza el enlazado interno.

**Búsquedas de tu nombre (marca personal)**
- El schema `Person` está en todas las páginas con las variantes "Sebastián Rincón", "Sebastian Rincon" y "Sebastian Rincon Peña". También indica tu cargo, tus temas, tus empresas y tus redes.
- "Sobre mí" está marcada como `ProfilePage`. Since aparece como organización fundada por ti.
- Cada artículo lleva tu firma, una caja de autor y un enlace a "Sobre mí", que son señales de autoría para Google.

**Técnico**
- El video de la portada pasó de 6,2 MB a 1,3 MB, con la misma resolución.
- Tus fotos ahora tienen una versión WebP: la principal pasó de 179 KB a 57 KB. La imagen para redes pasó de 193 KB a 97 KB.
- `sitemap.xml` tiene 43 URLs y fechas actualizadas.
- `llms.txt` sirve para que ChatGPT, Perplexity y otras IA entiendan quién eres y qué haces.
- Hay datos estructurados en todo el sitio: BlogPosting, FAQPage, BreadcrumbList, Service, CollectionPage y ProfilePage.
- Todas las páginas tienen el mismo menú (que ahora incluye Blog) y el mismo pie de página (que ahora incluye Guías).
- La web ya no depende del .zip: vive en `sitio/`.

## Lo que te toca a ti (en orden de impacto)

1. **Revisar y aprobar**: lee algunas guías y, si te gustan, fusiona la rama en `main` para publicar.
2. **Google Search Console** (search.google.com/search-console): agrega `sebastianrincon.co` como propiedad de dominio y envía `https://sebastianrincon.co/sitemap.xml`. Después pide la indexación de la portada, "Sobre mí" y los servicios.
3. **Enlaces desde tus otras webs**: es lo que más ayuda a que Google te asocie con tu nombre. Pide un enlace a `sebastianrincon.co` con el texto "Sebastián Rincón" desde:
   - agenciasincemarketing.com (página "Nosotros": "Fundada por Sebastián Rincón Peña")
   - medipro.com.co, mrsolucionesintegrales.co y cumbrecafegourmet.com (en el pie de página o en "Nosotros")
4. **Redes**: pon `sebastianrincon.co` en la bio de Instagram y Threads. Si tienes LinkedIn, Facebook, YouTube o TikTok, pásame los enlaces y los agrego al schema (`sameAs`). Esto ayuda a que Google arme tu panel de conocimiento.
5. **Perfil de LinkedIn**: si no lo tienes, créalo como "Sebastián Rincón Peña · Trafficker · Fundador de Since" con enlace a la web. Suele salir de segundo en las búsquedas de nombre.
6. **Publicar seguido**: un artículo nuevo cada 1 o 2 semanas mantiene el sitio vivo. Sigue `contenido/GUIA-REDACCION.md`.
7. **Comparte cada guía** en Instagram y Threads con el enlace. Las visitas de marca también cuentan.

## Datos que conviene confirmar

- Los artículos usan solo datos reales tuyos y de Since. Los precios de Shopify, las políticas de Meta y Google y otros datos de las plataformas se verificaron en noviembre de 2026 y están escritos con cautela. Cuando las plataformas cambien, revisa en especial:
  - `cuanto-cuesta-una-tienda-shopify-en-colombia`
  - `shopify-en-colombia-pagos-y-envios`
  - `politicas-de-publicidad-en-salud`
- `cuanto-cobra-un-trafficker` no da tus precios. Tiene un solo ejemplo ilustrativo (15 % sobre $6.000.000). Si no quieres esa cifra, la quitamos.
