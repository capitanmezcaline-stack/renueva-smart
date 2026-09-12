# Sistema visual — Renueva Smart (Instagram)

Dirección: **DIAGNÓSTICO LIMPIO**. Papel limpio y moderno (la pieza demuestra el producto
que se vende) + un mecanismo de anotación naranja encima (la pieza demuestra el servicio:
detectar qué está mal en una web).

## Paleta

| Token | Hex | Uso |
|---|---|---|
| `--orange` | `#FF6A00` | acento único, anotaciones, palabra clave del titular |
| `--ink` | `#0B0C0E` | texto principal, fondos oscuros, marcos de dispositivo |
| `--paper` | `#F5F3EE` | fondo base |
| `--white` | `#FFFFFF` | fondo alterno |
| `--grey` | `#92979D` | labels mono |
| `--body` | `#5A6068` | texto de cuerpo |
| `--line` | `#DFE0DC` | filetes y bordes suaves |

Los tres primeros salen de la web real (`renuevasmart.com`). El naranja es el único
puente con el sitio: todo lo demás es propio de redes.

## Tipografía

Las **mismas dos familias que carga renuevasmart.com**, sin inventar nada nuevo para redes:

- **Display:** **Fraunces** 700 — el serif del hero del sitio. `line-height: 1.1`,
  `letter-spacing: -.018em`, `font-optical-sizing: auto`. **Portada 182px; titulares
  interiores de 86 a 108px.** Fraunces lee ópticamente más chica que un grotesk al mismo
  cuerpo: al migrar desde Archivo hubo que subir ~20% sólo para mantener la presencia.
  Ojo: Fraunces pide **mucho menos tracking negativo que un grotesk**. Los -.03em que
  funcionaban con Archivo le cierran los remates y la ensucian.
- **Cursiva:** **Fraunces 700 italic**, el gesto de énfasis del sitio (en el hero,
  *"sin comprometerte"*). Se usa en **una sola palabra o frase corta por pieza**, casi
  siempre en naranja: es el reemplazo natural de la elipse dibujada sobre foto.
- **Cuerpo:** **Plus Jakarta Sans** 400 — 46px, `line-height: 1.4`.
- **Labels:** Plus Jakarta Sans **700 en versalitas** — 20px, `letter-spacing: .2em`.
  El sistema usaba una monoespaciada, pero el sitio no carga ninguna: se reemplazó por
  Jakarta en mayúsculas tracked. La monoespaciada quedó sólo dentro de los mockups (la
  barra de URL), donde es un elemento de interfaz, no tipografía de marca.

**Pocas palabras, pero grandes.** Menos texto no significa texto chico: una vez recortado
el copy, lo que queda tiene que crecer para ocupar el espacio que dejó. El aire va
alrededor del bloque, no dentro de él. Esta escala se subió dos veces y las dos quedó
corta — ante la duda, más grande.

**Medir, no estimar.** `_fuente/medir.py` hace una búsqueda binaria con la fuente real en
Chromium y devuelve el cuerpo máximo que entra en el ancho útil (856px) para cada línea de
titular. Es la forma de subir la escala hasta el límite sin descubrir a mano que un
titular se parte feo. Los máximos medidos de este fijado: portada 185px, "Se ve
desactualizada." en una línea 103px, "el nivel de tu negocio." 103px.

A veces el límite no es el cuerpo sino **dónde se corta la línea**: en el slide del giro,
pasar de `¿Y si tu web estuviera / a la altura` a `¿Y si tu web / estuviera a la altura`
permitió subir de 96 a 104px sin tocar nada más.

**Efecto secundario a vigilar:** cada vez que sube la escala, las etiquetas naranjas
crecen con ella y empiezan a tapar lo que señalaban. Después de cualquier cambio de
tamaño hay que revisar los `.tag` sobre los mockups, uno por uno, y correr la verificación
de desbordes y de zona segura de grilla.

Todo va embebido en base64 (`renueva-fonts.css`, 22 caras, ~890 KB). Nunca Google Fonts
por CDN. Para regenerarlo: `python _fuente/fetch_fonts.py` — pide a Google la misma URL
de `css2` que usa el sitio, se queda con los subsets `latin` y `latin-ext` y los inyecta
en base64.

## Reglas de composición

- Lienzo 1080×1350, exportado a 2160×2700 (retina 2x).
- Margen seguro **112px** en los cuatro lados.
- **Todo alineado a la izquierda.** Nada centrado.
- Chrome fijo: label arriba izquierda + tema del slide arriba derecha; logo abajo
  izquierda; **indicador de deslizar abajo derecha**.
- **Sin paginación.** El contador `NN / NN` se eliminó: no aporta nada al lector y mete
  números en una pieza que ya usa números como contenido (las señales). En su lugar va una
  flecha SVG de 62px trazada a 2px — en la portada acompañada de la palabra `DESLIZA`, en
  los slides intermedios sola, y **en el último slide no va**: ahí el recorrido termina y
  lo único que debe pedir la pieza es escribir por DM.
- Un número por slide como máximo. El número de señal vive sobre el titular (`SEÑAL 01`,
  en naranja) y el chrome superior derecho nombra el tema sin repetirlo —
  `DISEÑO`, `MÓVIL`, `CONTENIDO`, `PERCEPCIÓN`.
- **Zona segura de grilla:** Instagram recorta la portada a 1:1 en la grilla del perfil,
  o sea que se come los primeros y últimos 135px. Por eso la fila de chrome arranca en
  **y=152** y no en el margen de 112: a 112 la línea de corte pasaba por la mitad del logo
  y lo partía en todas las miniaturas del feed. La tinta del logo queda en 152–208, con
  aire suficiente. El titular tampoco puede caer en esas bandas.
- **Cuatro materiales de fondo, alternados:** negro, naranja, blanco/papel y foto. El
  carrusel se lee mejor cuando ninguno se repite dos veces seguidas — la dinámica sale del
  contraste entre uno y el siguiente, no de la pieza aislada. En el Fijado 1:
  foto B/N → negro → papel → **naranja** → papel → foto oscura → foto clara → negro →
  blanco → **naranja**.
- El **naranja pleno** funciona cuando lo ocupa un objeto claro que le haga contraste (el
  teléfono del slide 04) o cuando es el cierre. Sobre naranja se invierte todo: los labels
  de sección van en blanco, el número de señal y las etiquetas van en **tinta**, y el logo
  en su versión blanca.

## Registro: premium minimal

La regla que ordena todo lo demás: **una idea por slide, y nada más**. Titular corto más
una línea de apoyo; si hace falta un segundo párrafo, es que sobra. Las listas van sin
descripciones — un índice numerado con filetes finos dice más que cuatro bullets
explicados.

El aire no es espacio sobrante, es el material. Tipografía más chica y más espacio
alrededor se lee más caro que tipografía grande apretada.

## El mecanismo de anotación

Es lo que diferencia a esta marca de cualquier carrusel limpio, pero en este registro va
**racionado: una sola marca naranja por pieza, y no en todas las piezas**. Cuando el
naranja aparece en cada slide deja de señalar y pasa a ser decoración.

- `.mark` — elipse SVG naranja alrededor de una palabra o frase corta del titular.
  Rotada ~1.5° para que no se lea como una forma de software.
- `.tag` — chip naranja con texto mono en mayúsculas, apoyado sobre el borde de un
  dispositivo. Nombra el problema, no lo describe: "TEXTO CORTADO", "DISEÑO DE 2014".
- `.ring` — óvalo naranja que rodea un detalle dentro de una captura.

Regla: las anotaciones señalan problemas ajenos (webs "tipo", genéricas), nunca
el trabajo de un cliente real.

## Fotografía

Librería propia en `_fuente/fotos_hi/` (Pexels, descargadas con `fetch_pexels.py`).
**La librería de fotos de PUSH no se usa en esta marca** — es de otra marca y otro registro.

**Tres temas, y nada más:**

1. **Oficina profesional en uso** — escritorios con trabajo encima, estudios, salas,
   recepciones. Que se vea gente trabajando o el rastro de que alguien trabaja ahí.
2. **Obra y estructura** — construcción, andamios, hormigón, vigas. Es la metáfora
   literal del negocio: algo que se levanta y se renueva.
3. **Ciudad y arquitectura** — avenidas, torres, fachadas. Da escala y "nivel".

**Lo que no va:** bodegones (libros, relojes, plantas sueltas), texturas abstractas
(mármol, papel, degradados), hostelería y espacios de ocio, y el stock de "equipo feliz
chocando los cinco" o gente genérica con laptop.

Un bodegón se ve bonito suelto y no dice nada del negocio; una textura llena el cuadro
pero no aporta significado. Si la foto no se puede explicar como *oficina, obra o ciudad*,
no entra.

Dos formatos, nunca otro:

- **A sangre completa** (portada y slides de statement): foto al 100% del cuadro con
  `.veil` encima — un degradado a tinta que abre oscuro arriba, aclara en el tercio
  superior y cierra opaco abajo. El titular vive en la zona opaca de abajo.
- **A media altura** (slides de señal): la foto sangra desde el borde superior hasta los
  628px, con corte duro, y el texto va debajo sobre papel. Sin velo — el borde duro
  alcanza.

### El logo

Archivo maestro: `_fuente/assets/logo.png`, 1774×887 con transparencia real. Las otras dos
versiones se derivan de él por script, no se rehacen a mano:

- `logo-dark.png` — para fondo claro: el naranja se conserva y el blanco pasa a tinta.
- `logo-white.png` — todo blanco, **sólo para fondo naranja**, donde el naranja de "Smart"
  se perdería contra el fondo.

### Alineación del logo

El PNG trae **148px de margen transparente arriba y abajo** (simétrico) y **23px a la
izquierda** sobre un lienzo de 1774×887. Eso importa: alinear por la caja del `<img>` deja
el logo 2px corrido respecto de los textos. Se compensa con `margin-left:-2px`.

Las bandas fijas del sistema, iguales en los diez slides:

- Fila superior: `.top` con `height:56px`. En la portada el logo desborda esa caja, pero su
  **tinta** cae exactamente dentro de la banda (y 112 a 168), así que los labels de todos
  los slides quedan centrados en y=140.
- Pie: logo a `bottom:56px` con 168px de ancho → su tinta ocupa la banda y 1226 a 1282.
- La flecha de deslizar usa `height:56px` y `bottom:68px` para ocupar **esa misma banda**,
  y así queda ópticamente alineada con el logo del lado opuesto.

Sobre foto va el **logo original** (Renueva blanco + Smart naranja), no la versión blanca:
con el archivo en alta y el velo de portada, el naranja se sostiene y es lo que identifica
a la marca. La versión blanca se reserva para cuando el naranja no tiene dónde apoyarse.

### La portada

Foto a sangre **en blanco y negro** (`grayscale(1) brightness(.56) contrast(1.16)`) con el
velo de portada encima, y el titular enorme —124px— anclado abajo con una palabra en
naranja plano.

Tres cosas que se probaron y no funcionaron: el desenfoque fuerte hace que el titular
domine pero convierte la foto en una mancha sin significado; la foto a color compite con
el naranja del titular; y la elipse dibujada se pierde sobre una foto cargada — sobre foto
va la palabra en naranja plano, la elipse se reserva para los fondos lisos.

La foto en blanco y negro cumple dos funciones a la vez: deja el naranja como único color
de la pieza, y permite que la escena se lea (un interior distinguido = "tu negocio puede
ser excelente") sin robarle jerarquía al título.

En portada el logo va en su **versión original**, con el naranja de "Smart" intacto.

### El ritmo del feed

Cuatro materiales de portada —negro, naranja, blanco y foto— rotando en un **ciclo de 4**.
La grilla tiene 3 columnas y 4 no es múltiplo de 3, así que el ciclo nunca deja dos
portadas iguales pegadas, ni horizontal ni verticalmente. No hay que acomodar nada a mano.

El material se asigna por **posición en la grilla**, no por fecha: Instagram muestra lo más
nuevo primero, así que el último posteo publicado es el que queda arriba. El generador
está en `_fuente/grilla_feed.py` y la simulación del feed en `PLAN-CONTENIDO/FEED.jpg`.

En portadas de fondo pleno (negro, naranja, blanco) el bloque de texto va **centrado**, no
anclado abajo: sin foto que llene la parte superior, el anclaje inferior deja un hueco que
se lee como error.

### Las portadas son una serie

Los fijados se ven uno al lado del otro en la grilla del perfil, así que la portada no se
juzga sola: se juzga en el par. La receta es fija para los tres:

1. Foto de interior profesional, **siempre en blanco y negro**, oscurecida con el velo de
   portada.
2. Titular de dos líneas: la primera en redonda blanca, **la segunda en cursiva naranja**.
3. Logo arriba a la izquierda, tema del fijado arriba a la derecha.
4. Bajada en gris debajo del titular.

Lo que cambia entre fijados es la foto y el titular; nada más. Fijado 1 usa una escalera
clásica, Fijado 2 una oficina moderna — mismo registro, escenas distintas.

**Nada blanco y grande en la portada.** El primer intento del Fijado 2 tenía el mockup de
navegador flotando sobre la foto: recortado a 1:1 en la grilla, ese rectángulo blanco es lo
más brillante del cuadro, se come el titular y rompe la dupla con el Fijado 1. El mockup se
mudó adentro del carrusel. Para decidir esto sirve simular el recorte de la grilla
(`crop(0, 135, 1080, 1215)`) y poner las dos portadas lado a lado, no mirarlas sueltas.

Reglas: el sujeto nunca va centrado, va corrido hacia el lado opuesto al texto. Nada de
franjas finas: la foto ocupa la mitad del cuadro o todo. Las fotos no llevan duotono —
eso es del sistema de PUSH, acá van en color.

## Dispositivos

- `.frame` — ventana de navegador: sin borde, radio 6px, barra clara de 46px con tres
  puntos grises y la URL en mono. La barra oscura pesaba de más.
- `.phone` — teléfono: borde `#16181B` de 10px, radio 44px, notch de 124px.
- `.lift` / `.lift-soft` — la sombra larga y difusa es lo que separa un mockup premium de
  una captura pegada. Sobre fondo oscuro va fuerte; sobre papel, casi imperceptible.

### La web vieja (`.old`)

El activo más reutilizable del sistema: una web anticuada **inventada** —"Estudio González
& Asoc."— maquetada en HTML, no una captura. Georgia, header con doble filete, nav de
links azules separados por pipes, banner en degradé azul, texto justificado, un
`imagen.jpg` gris que no cargó y un contador de visitas.

Vive a 1000px de ancho con `transform-origin: top left`, así que la misma pieza sirve
escalada para todo: llena la portada, entra diminuta en un teléfono (`scale(.33)` — que es
justo el punto de "en el celular se ve mal", porque se sale de la pantalla de verdad), o
se recorta de arriba para un detalle.

Regla de escala: para que no corte palabras, el `scale` tiene que dar el ancho exacto del
marco (ancho interior ÷ 1000). A ancho completo con margen de 112px eso es `scale(.856)`.
Un zoom mayor que eso corta texto por el costado y se lee como un render roto, no como una
decisión.

Nunca se muestra la web real de un negocio identificable para ilustrar un problema.

### La web moderna (`.new`) — la contracara

Agregada en el Fijado 2. Mismo principio que `.old` pero al revés: una web **bien hecha**,
también inventada, para poder mostrar el "después" sin depender del material del caso real
(que está limitado a 700px). Definida una sola vez en **`_fuente/_web-nueva.css`**, que
`armar_post2.py`, `armar_post3.py` y `armar_post.py` anteponen al CSS base. Tiene variante
`.movil` de 390px para meterla dentro del teléfono.

**El hero va con foto a sangre**, al ras de los cuatro bordes, y la tipografía encima:
`.nhero` en `position:relative` con la `<img>` en `object-fit:cover`, un velo en degradé
diagonal (`.nvelo`, opaco a la izquierda y casi limpio a la derecha) y el bloque de texto
anclado abajo a la izquierda —eyebrow naranja, titular Fraunces blanco, botón naranja—.
Es el mismo esquema que usa renuevasmart.com, y por eso funciona: el "después" tiene que
verse premium de un vistazo, no describirse como premium.

La primera versión partía el hero en dos columnas con una foto chica al costado. Eso *es*
el patrón que el carrusel está criticando dos slides antes; el antes/después se anulaba.

La foto del hero se elige con el mismo criterio que el resto (oficina, obra o ciudad) y
lleva `filter:brightness(1.22)` porque el velo encima se la come. Cuidado con las fotos
que datan la pieza: la primera candidata tenía gente con barbijo, y la segunda resultó ser
un baño de spa —a tamaño de miniatura pasaba por mármol—. Siempre mirar el hero al 100%
antes de aprobarlo.

Tener las dos —`.old` y `.new`— permite armar un antes/después genérico en cualquier
slide, sin gastar el caso de Acosta Pastore, que se reserva para el cierre.

### Trampa de los mockups dentro de flex

Los mocks miden 1000px de ancho y se achican con `transform: scale()`. Como `transform` no
afecta al layout, **un contenedor flex no encoge el ítem por debajo de esos 1000px** salvo
que lleve `min-width:0`. Sin eso, el segundo panel de un antes/después se empuja fuera del
cuadro y el slide se renderiza con una sola columna. Pasó en el Fijado 2 y costó verlo
porque no da error: simplemente falta media pieza.

## Voz

Tuteo neutro (`tú`, `tienes`, `envíanos`). Directo, sin humo, sin promesas de resultados
inventados. Frases cortas. El remate de cada bloque es la frase corta, no la larga.

Prohibido: inventar métricas, testimonios o casos. El único testimonio publicable hoy es
el de Bruno Acosta Pastore, que ya está en la web.

## Archivos

- `_fuente/prep.py` — recolorea el logo para fondo claro y arma el subset de fuentes.
- `_fuente/render.py` — renderiza slides a PNG con Playwright (`1.0` para revisar, `2.0` para publicar).
- `_fuente/montage.py` — arma la grilla de revisión.
- `_fuente/build.py` — inyecta fuentes e imágenes en base64 y deja el HTML standalone.
