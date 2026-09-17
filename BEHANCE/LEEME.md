# Case study para Behance — Renueva Smart

8 paneles a 2880px de ancho, listos para subir a un proyecto de Behance en este
orden (el nombre ya lo indica).

| Archivo | Qué muestra |
|---|---|
| `01-cover.jpg` | Portada del proyecto |
| `02-el-proyecto.jpg` | El brief, en números |
| `03-sistema-visual.jpg` | Tipografía, color y criterio de foto |
| `04-fijados.jpg` | Los 3 carruseles fijados, como serie |
| `05-el-feed.jpg` | La grilla de 19 posteos y la regla de reparto |
| `06-destacados.jpg` | Los 7 destacados y tres historias de detalle |
| `07-caso-real.jpg` | Antes/después real de Escribanía Acosta Pastore |
| `08-cierre.jpg` | Cierre y créditos |

## Antes de subir — dos cosas para personalizar

1. **Poné tu nombre.** Aparece como `TU NOMBRE` en `01-cover.jpg` (pie de página)
   y en `08-cierre.jpg`. Se edita en `_fuente/behance/p01-cover.html` y
   `p08-cierre.html`, buscando "Tu Nombre" / "TU NOMBRE".
2. **Revisá los tags de portada** ("Branding · Social media · Dirección de
   arte" en `01-cover.jpg`) — dejalos como están o ajustalos a como categorizás
   vos el proyecto en tu perfil.

## Cómo se regenera

Todo sale de HTML — si cambia una pieza del sistema (un fijado, el feed, un
destacado), los paneles se rehacen solos, no hay que reexportar a mano:

```bash
cd _fuente/behance
python render_behance.py              # los 8 paneles
python render_behance.py p05-feed.html   # uno solo
```

Después de editar el nombre en `p01-cover.html` / `p08-cierre.html`, hay que
volver a correr el render para que el cambio llegue al JPG.

## Por qué este recorte y no otro

El proyecto real tiene ~120 piezas (3 fijados, 19 posteos, 7 destacados con 43
historias). Un case study de Behance no es una galería de todo lo que existe —
es la historia de las decisiones. Por eso cada panel muestra una decisión con
su motivo (la paleta separada del cliente ficticio, el reparto sin diagonales
en la grilla, el caso real en vez de un mock) en lugar de listar piezas.
