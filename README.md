# sebastianrincon.co
Web de marca personal de Sebastián Rincón Peña

## Estructura

- `sitio/`: la web tal cual se publica. GitHub Pages la sube automáticamente cada vez que hay cambios en `main`.
- `contenido/blog/`: los artículos del blog en Markdown. Hay uno por archivo.
- `contenido/GUIA-REDACCION.md`: reglas para escribir artículos nuevos (tono, formato y datos permitidos).
- `herramientas/generar.py`: arma el blog, el menú, el pie de página, el schema, el `sitemap.xml`, el `llms.txt` y el feed RSS.

## Publicar un artículo nuevo

1. Crea `contenido/blog/<slug>.md` siguiendo `contenido/GUIA-REDACCION.md`.
2. Corre `python3 herramientas/generar.py`. Si hay enlaces rotos, el script te los avisa.
3. Haz commit y push a `main`.

> Ya no hace falta subir `sitio-deploy.zip`. Si subes un .zip nuevo, la carpeta `sitio/` tiene prioridad y el .zip se ignora.

Las tareas de SEO que debes hacer por fuera del código están en `SEO-PENDIENTES.md`.
