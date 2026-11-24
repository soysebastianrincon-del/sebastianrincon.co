# Guía de redacción del blog de sebastianrincon.co

Esta guía es para quien escriba artículos del blog (personas o agentes). El generador
`herramientas/generar.py` convierte cada archivo de `contenido/blog/*.md` en una página.

## Quién habla

Escribe en primera persona como **Sebastián Rincón Peña**, trafficker colombiano. Tutea al lector.
Usa español de Colombia ("pauta", "clientes potenciales", "peso", "WhatsApp"). El tono es directo
y cercano, sin humo: "si tu agencia no te explica los números, yo sí". Las frases son cortas.
Nada de relleno ni de frases como "en el mundo digital de hoy". Ve a lo práctico.

### Datos reales que puedes usar (no inventes otros)

- 8 años haciendo pauta en Meta Ads y Google Ads, y creando tiendas en Shopify.
- Fundador de **Since Agencia Marketing Digital** (agenciasincemarketing.com): más de 100 empresas
  acompañadas, con clientes en Colombia, Estados Unidos, México, Ecuador, Perú, Curazao y otros
  países. Tiene un equipo de 13 personas, y cada cliente tiene un trafficker asignado.
- Cofundador de **Medipro** (medipro.com.co), creada con su socia. Es un asistente con IA que responde,
  agenda y hace seguimiento 24/7 por WhatsApp, Instagram y Facebook, y además entrena a los equipos
  de recepción. Trabaja para médicos, clínicas y centros de estética.
- CMO de **MR Soluciones Integrales**, que implementa el SG-SST en PyMEs.
- **Cumbre Café Gourmet** es su marca familiar de café de especialidad, de Salamina, Caldas. Vende en
  Shopify con envíos a toda Colombia.
- Especialidad: empresas de servicios de alto valor (high ticket), ventas por WhatsApp y ecommerce.
- Resultados publicados por Since. Atribúyelos siempre al equipo y no a Sebastián solo:
  - Dr. Eduardo T.: ROAS 30x en Meta Ads (septiembre 2026).
  - Camargo: ROAS 17x.
  - Smartshop.bga: ROAS 15x.
  - Amada Holistic: ROAS 12x.
  - Haskell (Venezuela): ROAS 5x, más de 20 leads diarios.
  - Holographic (Ecuador): más de 15 leads diarios.
  - Una cuenta con más de 25.000 mensajes a WhatsApp y 924 clientes potenciales calificados.
  - ROAS reportado por clientes entre 4x y 30x.
- Principios: los números se explican; las ventas van antes que el alcance; primero lo prueba en sus
  propios proyectos.
- Contacto: WhatsApp +57 301 329 1994. Instagram @soysebastianrincon.

**Está prohibido inventar** clientes, casos, testimonios, cifras de resultados, precios de los
servicios de Sebastián o estadísticas de mercado. Si das un dato de mercado (por ejemplo, precios de
Shopify o costos promedio), verifícalo con WebSearch. Escríbelo con cautela ("a noviembre de 2026",
"aproximadamente", "varía según…") y no pongas URL de fuente en el texto. Si no lo puedes verificar,
no des la cifra y explica los factores que la determinan. Los ejemplos numéricos ilustrativos están
permitidos siempre que se presenten como ejemplo ("supongamos que tu ticket es de $2.000.000…").

**Precios de Sebastián o de Since: nunca.** Ni cifras, ni porcentajes de fee, ni ejemplos
ilustrativos de lo que cobran (por ejemplo, "15 % sobre la inversión"). Todo se trabaja bajo
**cotización sin compromiso**: cuando el tema sea precio, dilo así e invita a escribir por WhatsApp.

## Qué hace que un artículo posicione

- Responde la pregunta en los primeros 2 o 3 párrafos, porque eso es lo que citan Google y las IA.
  Después profundiza.
- Debe tener entre 1.300 y 2.000 palabras útiles: pasos, criterios, errores comunes, ejemplos con
  números y una tabla si aporta.
- Usa la palabra clave principal en el título, en el primer párrafo, en al menos un H2 y de forma
  natural en el resto. Incluye variantes y sinónimos.
- Usa encabezados `##` (H2) y `###` (H3) descriptivos, que suelen ser preguntas que la gente busca.
- **Enlaces internos** (obligatorios, con rutas absolutas desde la raíz):
  - 1 o 2 enlaces a la página de servicio relacionada, con texto ancla descriptivo.
  - 2 o 3 enlaces a otros artículos del blog de la lista de abajo. Usa solo slugs de esa lista.
  - Opcional: `/sobre-mi/` o `/resultados/`.
- Cierra con una sección `## Preguntas frecuentes` que tenga 4 o 5 preguntas en `###`, cada una
  con una respuesta de 2 a 4 frases. Con ella se genera el schema FAQPage.
- Antes de las preguntas frecuentes, pon un párrafo corto que invite a escribir por WhatsApp para
  revisar la cuenta o el proyecto. No pongas el enlace de WhatsApp porque la plantilla lo agrega.

## Formato del archivo

Guarda el archivo en `contenido/blog/<slug>.md`, exactamente así:

```
---
titulo: Cuánto invertir en Meta Ads en Colombia (guía 2026)
seo_titulo: Cuánto invertir en Meta Ads en Colombia en 2026
descripcion: Cómo calcular tu presupuesto de Meta Ads según tu meta de ventas, ticket y margen. Fórmula, ejemplos en pesos y errores que hacen perder plata.
palabra_clave: cuánto invertir en Meta Ads
categoria: meta-ads
fecha: 2026-11-22
resumen: Respuesta directa en 1 o 2 frases (máximo 300 caracteres). Aparece en un recuadro "En corto" arriba del artículo.
---

Primer párrafo...

## Primer H2

Texto con **negritas**, *cursivas* y [enlaces](/servicios/pauta-meta-ads/).

- viñeta
- viñeta

1. paso
2. paso

| Columna | Columna |
|---|---|
| dato | dato |

> Cita o idea clave destacada.

## Preguntas frecuentes

### ¿Pregunta?

Respuesta.
```

Reglas del formato:

- `seo_titulo` tiene máximo 55 caracteres, porque la plantilla le agrega " | Sebastián Rincón".
- `descripcion` tiene entre 140 y 158 caracteres.
- `categoria` es una de estas: `meta-ads`, `google-ads`, `shopify`, `empresas-de-servicios`,
  `estrategia`.
- No uses `#` (H1) en el cuerpo, porque la plantilla pone el título. No uses HTML ni imágenes.
- Las tablas deben ser simples, con una sola línea por fila.

## Páginas de servicio (destinos de los enlaces)

- `/servicios/pauta-meta-ads/`: Trafficker de Meta Ads
- `/servicios/pauta-google-ads/`: Especialista en Google Ads
- `/servicios/tiendas-shopify/`: Creación de tiendas Shopify
- `/servicios/pauta-empresas-de-servicios/`: Pauta para empresas de servicios high ticket
- `/servicios/publicidad-para-medicos-y-clinicas/`: Publicidad para médicos y clínicas
- `/servicios/`: todos los servicios

## Lista completa de artículos (slug: tema)

**meta-ads**
- `cuanto-invertir-en-meta-ads`: cuánto invertir en Meta Ads en Colombia (cálculo de presupuesto)
- `campanas-de-whatsapp-meta-ads`: campañas de mensajes a WhatsApp con Meta Ads
- `por-que-mis-anuncios-no-venden`: por qué tus anuncios de Facebook e Instagram no venden (diagnóstico)
- `pixel-de-meta-y-api-de-conversiones`: píxel de Meta y API de conversiones explicados
- `metricas-de-meta-ads`: cómo leer un reporte de Meta Ads (CPM, CTR, CPC, CPA, ROAS, frecuencia)
- `estructura-de-campanas-meta-ads`: cómo estructurar campañas en Meta Ads en 2026 (Advantage+, públicos, creativos)

**google-ads**
- `google-ads-vs-meta-ads`: Google Ads o Meta Ads, cuál conviene a tu negocio
- `cuanto-cuesta-google-ads-en-colombia`: cuánto cuesta Google Ads en Colombia
- `performance-max`: Performance Max, qué es y cuándo usarla
- `google-ads-para-empresas-de-servicios`: campañas de búsqueda para empresas de servicios (palabras clave, negativas, llamadas)
- `conversiones-en-google-ads`: cómo medir conversiones en Google Ads (GA4, conversiones mejoradas, llamadas, WhatsApp)

**shopify**
- `cuanto-cuesta-una-tienda-shopify-en-colombia`: cuánto cuesta crear una tienda Shopify en Colombia
- `shopify-en-colombia-pagos-y-envios`: vender con Shopify en Colombia (pasarelas de pago, pesos, envíos, facturación)
- `shopify-vs-otras-plataformas`: Shopify vs WooCommerce, Tiendanube y otras opciones
- `tienda-shopify-que-convierta`: checklist para que tu tienda Shopify convierta el tráfico de pauta
- `catalogo-de-shopify-para-anuncios`: conectar Shopify con el catálogo de Meta y Google Shopping

**empresas-de-servicios**
- `embudo-de-venta-para-servicios-high-ticket`: embudo de venta para servicios de alto valor
- `politicas-de-publicidad-en-salud`: publicidad para médicos y clínicas en Meta y Google (políticas y qué sí funciona)
- `leads-que-no-se-convierten`: por qué tus clientes potenciales no se convierten en clientes
- `costo-por-cliente-potencial`: costo por lead vs costo por cliente, cómo calcular cuánto puedes pagar
- `seguimiento-comercial-con-ia`: seguimiento comercial y automatización con IA por WhatsApp

**estrategia**
- `que-es-un-trafficker`: qué es un trafficker y qué hace
- `cuanto-cobra-un-trafficker`: cuánto cobra un trafficker en Colombia (modelos de cobro y qué incluye, sin inventar precios de Sebastián)
- `agencia-o-trafficker-freelance`: agencia de marketing o trafficker freelance, cómo elegir
- `que-es-el-roas`: qué es el ROAS, cómo se calcula y cuál es un buen ROAS
- `auditoria-de-cuenta-publicitaria`: cómo auditar tu cuenta de Meta Ads o Google Ads (checklist)
