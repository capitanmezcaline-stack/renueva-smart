# Renueva Smart — sistema de contenido para Instagram

Piezas de @renuevasmart generadas desde HTML y renderizadas con Playwright: carruseles de
1080×1350 e historias de 1080×1920, con las fuentes de la marca embebidas.

**Si vas a trabajar acá, leé primero [`CLAUDE.md`](CLAUDE.md).** Son las reglas del
sistema, y Claude Code las toma solo al abrir la carpeta.

## Puesta en marcha

Un solo comando, con Python ya instalado:

```bash
cd _fuente && python bootstrap.py
```

Instala las librerías (`playwright`, `pillow`), baja el navegador que usa Playwright para
renderizar, y trae lo que el repo no versiona: las fuentes en base64, las 24 fotos que
usan las piezas y las capturas del caso real. Es idempotente: lo que ya está no se
vuelve a bajar.

## Generar las piezas

```bash
cd _fuente

# Fijado 1 — se edita a mano en post-1.src.html
python render.py post-1.src.html ../FIJADO-1 s01,s02,s03,s04,s05,s06,s07,s08,s09,s10 2.0
python build.py  post-1.src.html ../FIJADO-1/renueva-fijado-1.html

# Fijados 2 y 3 — se editan en post-N-cuerpo.html y se ensamblan
python armar_post2.py && python render.py post-2.src.html ../FIJADO-2 s01,...,s11 2.0
python armar_post3.py && python render.py post-3.src.html ../FIJADO-3 s01,...,s08 2.0

# Destacados — uno por script, cada uno verifica la zona segura solo
python historias_tuweb.py
python historias_servicios.py
python historias_proceso.py
python historias_caso.py
python historias_precios.py
python historias_preguntas.py
python historias_gratis.py
python destacados.py            # las 7 tapas

# Plan de contenido — 19 portadas + la simulación del feed
python grilla_feed.py
```

`render.py` toma escala: `1.0` para revisar rápido, `2.0` para el PNG retina que se
publica. `build.py` deja un HTML autocontenido con fuentes e imágenes en base64, que se
abre en cualquier navegador sin dependencias.

## Qué hay

```
FIJADO-1/      10 slides · "¿Tu web necesita una renovación?"  → captar
FIJADO-2/      11 slides · "Qué hacemos"                        → explicar
FIJADO-3/       8 slides · "Así transformamos una web"          → demostrar
DESTACADOS/     7 destacados, 43 historias                      → ver LEEME.md
PLAN-CONTENIDO/ 19 portadas y 4 semanas de plan                 → ver PLAN.md
SISTEMA-VISUAL.md  paleta, tipografía, fotografía y composición
_fuente/        generadores, HTML fuente y utilidades
```

## Utilidades

| Script | Para qué |
|---|---|
| `bajar_sitio.py` | Vuelca el texto de renuevasmart.com, de donde sale todo el copy |
| `medir.py` | Cuerpo tipográfico máximo que entra en el ancho útil |
| `fetch_fonts.py` | Rearma `renueva-fonts.css` desde Google Fonts |
| `fetch_pexels.py` | Baja fotos nuevas de Pexels |
| `capturar_caso.py` | Recaptura los dos sitios del caso Acosta Pastore |
| `montage.py` | Grilla de revisión de un carrusel |

## Notas

Las fotos son de **Pexels** (licencia gratuita, sin atribución obligatoria). No se
versionan: `bootstrap.py` las vuelve a bajar.

Las tipografías son **Fraunces** y **Plus Jakarta Sans**, ambas con licencia SIL Open
Font, las mismas que carga el sitio.

Las capturas del caso son de webs públicas de un cliente real de Renueva Smart.
