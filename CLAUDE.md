# CLAUDE.md — Renueva Smart

Sistema de contenido de Instagram para **@renuevasmart**: rediseño web para negocios de
servicios profesionales (notarías, abogados, gestorías, inmobiliarias, clínicas).

Este archivo son las reglas del sistema. Leelo antes de tocar cualquier pieza.
La definición visual completa está en `SISTEMA-VISUAL.md`.

---

## Las cinco reglas que no se negocian

### 1. El copy sale de la web, no se inventa

El texto de cada pieza se toma de **renuevasmart.com**. La web ya tiene la voz resuelta;
reescribirla mete variaciones que nadie pidió y que contradicen lo que el prospecto lee
después. Sólo dos adaptaciones permitidas:

- **Voseo → tuteo neutro.** La web mezcla; en redes se unificó en tuteo.
- **"celular" → "teléfono".**

Para bajar el sitio y leerlo: `python _fuente/bajar_sitio.py` deja el texto plano en
`_fuente/_sitio.txt`. Las FAQ están plegadas en la página pero sí vienen en el HTML.

### 2. Las fotos son oficina, obra o ciudad

Una foto entra sólo si se puede explicar como **oficina profesional en uso**, **obra y
estructura** o **ciudad y arquitectura**. Quedan fuera bodegones (libros, relojes,
plantas), texturas abstractas (mármol, papel), hostelería y el stock de "equipo feliz
chocando los cinco".

Un bodegón se ve bonito suelto y no dice nada del negocio. Obra y ciudad, en cambio, son
la metáfora literal de lo que vende la marca.

**Previsualizá las candidatas ya en blanco y negro y oscurecidas**, que es como van a
existir. Una foto puede funcionar a color y desarmarse con el tratamiento.

Ninguna foto se repite entre piezas. Bajar más con `_fuente/fetch_pexels.py`.

### 3. Pocas palabras, pero grandes

Menos texto no significa texto chico. Al recortar copy, lo que queda tiene que **crecer**
para ocupar el espacio que dejó. El aire va alrededor del bloque, no adentro.

Antes de fijar un cuerpo, medí: `python _fuente/medir.py` hace búsqueda binaria con la
fuente real y devuelve el máximo que entra en el ancho útil (856px). A veces el límite no
es el cuerpo sino **dónde se corta la línea**: cambiar el `<br>` puede dar 10px más.

### 4. La grilla de Instagram recorta 135px arriba y abajo

En piezas de 1080×1350 el perfil recorta a 1:1. Por eso la fila de chrome arranca en
**y=152**, no en el margen de 112: a 112 la línea de corte partía el logo al medio en
todas las miniaturas.

Antes de dar por buena una portada, **simulá el recorte** (`crop(0,135,1080,1215)`) y
mirala al lado de las vecinas, no sola. Una portada puede verse perfecta suelta y romper
la grilla.

En historias (1080×1920) la zona segura es **y=260 a y=1660**: Instagram tapa ~230px
arriba y ~250px abajo.

### 5. Mostrar, no describir

Ante cualquier decisión visual, renderizá las opciones y mostralas. No las expliques.
Vale para portadas, fotos, tratamientos y tipografía.

---

## Cómo está armado

### Tipografía

Las **mismas dos familias que carga el sitio**: **Fraunces** (serif, titulares y las
cursivas de énfasis) y **Plus Jakarta Sans** (cuerpo y labels en versalitas). Embebidas en
base64 en `_fuente/renueva-fonts.css`. Nunca Google Fonts por CDN.

Regenerar: `python _fuente/fetch_fonts.py` — pide a Google la misma URL de `css2` que usa
el sitio y las inyecta en base64.

La **cursiva naranja de Fraunces** es el gesto de énfasis de la marca, copiado del hero
del sitio. Va en una sola palabra o frase corta por pieza.

### Los cuatro materiales de fondo

Negro, naranja, blanco/papel y foto. Nunca se repite el mismo dos veces seguidas, ni en
el carrusel ni en la grilla del perfil.

En fondos plenos el bloque de texto va **centrado**; en fondos con foto va **anclado
abajo**. Sin foto que llene la parte superior, el anclaje inferior deja un hueco que se
lee como error.

### Componentes reutilizables

- **`.old`** — una web anticuada *inventada* ("Estudio González & Asoc."), maquetada en
  HTML, no una captura. Mide 1000px con `transform-origin: top left`, así que la misma
  pieza sirve escalada para todo. Nunca se muestra la web real de un negocio
  identificable para ilustrar un problema.
- **`.new`** — su contracara: una web bien hecha, también inventada, para mostrar el
  "después" sin gastar el caso real. Vive en **`_fuente/_web-nueva.css`**, un solo archivo
  que los tres ensambladores anteponen al CSS base; no se copia en los `-extra.css`.
  El hero va con **foto a sangre y tipografía encima**, como renuevasmart.com. Un hero
  partido en dos columnas con una foto chica al costado es un patrón viejo y arruina el
  "después": el slide tiene que dar envidia, no explicar que da envidia.
- **`.frame` / `.phone`** — navegador y teléfono, con sombra larga (`.lift`). Esa sombra
  es la diferencia entre un mockup premium y una captura pegada.

**Trampa conocida:** los mocks miden 1000px y se achican con `transform`, que no afecta al
layout. Un contenedor flex no los encoge salvo que lleve `min-width:0`. Sin eso, el
segundo panel de un antes/después se va fuera del cuadro y falta media pieza, sin error.

### El caso real

Los dos sitios de Escribanía Acosta Pastore siguen en línea y se capturan en alta:
`python _fuente/capturar_caso.py` baja escritorio y móvil a 2x del blog viejo
(`escribaniacostapastore.com`) y del rediseño
(`avvedit-creator.github.io/nuevaescribaniacostapastore`).

Es un trabajo real, así que **no lleva leyenda de "rediseño conceptual"**. El crédito es un
activo: "Escribanía Acosta Pastore · Montevideo".

---

## Qué hay producido

| | |
|---|---|
| **3 fijados** | `FIJADO-1/2/3` — funcionan como mini landing del perfil. Se diseñan como serie: las tres portadas comparten receta (foto de interior en B/N, titular de dos líneas con la segunda en cursiva naranja). |
| **7 destacados** | `DESTACADOS/` — 43 historias. Es un embudo, no un escaparate: el más a la izquierda es el más tocado y ahí va el problema, nunca la presentación de la empresa. Ver `DESTACADOS/LEEME.md`. |
| **19 portadas** | `PLAN-CONTENIDO/` — cuatro semanas de plan, con el reparto de materiales resuelto para que la grilla no dibuje patrones. Ver `PLAN-CONTENIDO/PLAN.md`. |

**Prohibido:** inventar casos, testimonios o métricas. El único testimonio publicable es
el de Bruno Acosta Pastore, que ya está en la web. Y nada de nombres genéricos de
destacado tipo "Nosotros", "Branding" o "Inspiración".

---

## Flujo de trabajo

```bash
cd _fuente
python bootstrap.py          # primera vez: librerias, fuentes, fotos y capturas

# carruseles
python render.py post-1.src.html ../FIJADO-1 s01,s02,... 2.0   # PNGs retina
python build.py  post-1.src.html ../FIJADO-1/renueva-fijado-1.html
python armar_post2.py        # el Fijado 2 y 3 se ensamblan desde -cuerpo.html

# destacados
python historias_gratis.py   # uno por destacado; cada uno verifica la zona segura

# plan de contenido
python grilla_feed.py        # genera las 19 portadas y el reparto de materiales
```

`post-1.src.html` se edita a mano. Los Fijados 2 y 3 se editan en su `-cuerpo.html` y se
ensamblan con `armar_post2.py` / `armar_post3.py`, que toman el CSS base del Fijado 1 para
que los tres no se desincronicen.

**OneDrive bloquea archivos de a ratos** al escribir capturas. Los generadores llevan una
función `guardar()` con reintentos; sin eso fallan de forma intermitente.

---

## Verificaciones antes de dar algo por terminado

1. **Desbordes** — que ningún elemento se salga del lienzo.
2. **Zona segura** — grilla (135/1215) en carruseles, historia (260/1660) en destacados.
3. **Etiquetas naranjas** — cada vez que sube la escala tipográfica, los `.tag` crecen con
   ella y empiezan a tapar lo que señalaban. Revisarlos uno por uno.
4. **Balance de `<div>`** — un cierre faltante no da error: simplemente se traga las
   piezas siguientes.
5. **Fotos repetidas** — `grep -o 'px-[0-9]*\.jpg' | sort | uniq -c`.
