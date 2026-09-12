# Plan de contenido — @renuevasmart

3 fijados + 19 posteos en cuatro semanas. Las portadas están renderizadas en
`portadas/post-NN.png` y la simulación del feed en `FEED.jpg`.

## Cómo se decidió el material de cada portada

Cuatro materiales: **negro, naranja, blanco y foto**.

El primer intento fue un ciclo regular de 4. Evita vecinos iguales —4 y 3 no comparten
divisores— pero justamente por eso dibuja **diagonales perfectas** y el feed se lee
mecánico, como un tablero de ajedrez.

El reparto actual salió de una búsqueda aleatoria con restricciones sobre 500.000
combinaciones:

- **Prohibido** repetir material a la izquierda y arriba.
- **Penalizado**: coincidencias en diagonal, filas idénticas, filas en espejo (mismo
  material en la primera y la tercera columna) y que una columna quede dominada por un
  material.
- Reparto parejo: quedó 5 naranja / 4 blanco / 5 negro / 5 foto.

Resultado: ningún vecino repetido, ninguna fila igual a otra, y sólo dos coincidencias
en diagonal en toda la grilla. Se ve repartido sin verse ordenado.

La única repetición deliberada es la **primera fila**: los tres fijados van los tres con
foto en blanco y negro, porque son una serie y conviene que se lean como un bloque.

**Ojo con el orden.** El material está asignado por *posición en la grilla*, no por fecha.
Instagram muestra lo más nuevo primero, así que el último posteo de la semana 4 queda
arriba, justo debajo de los fijados. Si cambiás el orden de publicación, hay que
recalcular: se corre `_fuente/grilla_feed.py`.

## Los 19 posteos, en orden de publicación

| # | Sem | Posteo | Portada |
|---|---|---|---|
| 01 | 1 | 3 señales de una web vieja | blanco |
| 02 | 1 | Web Roast #1 | negro |
| 03 | 1 | 5 errores de diseño | naranja |
| 04 | 1 | ¿Tu web parece de 2015? | foto |
| 05 | 1 | Presentación de Renueva Smart | foto |
| 06 | 2 | Antes/después restaurante | blanco |
| 07 | 2 | Antes/después inmobiliaria | negro |
| 08 | 2 | Antes/después dentista | naranja |
| 09 | 2 | Cómo mejorar una home | negro |
| 10 | 2 | Rediseño en 30 segundos | foto |
| 11 | 3 | Qué debe tener una web moderna | foto |
| 12 | 3 | Errores en mobile | blanco |
| 13 | 3 | CTA que debería tener tu web | naranja |
| 14 | 3 | Web Roast #2 | naranja |
| 15 | 3 | No necesitas rehacer todo tu negocio | foto |
| 16 | 4 | Caso de transformación | negro |
| 17 | 4 | Cuánto cuesta renovar una web | negro |
| 18 | 4 | Qué incluye Renueva Smart | blanco |
| 19 | 4 | Web Roast #3 | naranja |

**Producidos hasta ahora:** 01, 02 y 03, en `POSTS/`. Cada uno tiene sus PNG a 2160×2700,
el HTML autónomo y el CAPTION. Las portadas de `portadas/` son el punto de partida: la
portada real del carrusel tiene que coincidir con la de la grilla, o el feed simulado
deja de decir la verdad.

## Dos cosas a resolver antes de producir

**Los antes/después de la semana 2** (restaurante, inmobiliaria, dentista) necesitan
material. Hoy el único caso real es Acosta Pastore, que ya se usa en el Fijado 3. Hay dos
caminos: conseguir tres casos reales más, o producirlos como **rediseños conceptuales** y
decirlo en la pieza. Lo que no corresponde es mostrarlos como trabajos hechos si no lo son.

**Los Web Roast** analizan webs ajenas en público. Conviene definir la política: pedir
permiso, difuminar la marca, o usar sitios propios. Señalar por nombre la web de un
negocio real que no es cliente puede traer más problema que alcance.

## Qué es cada archivo

- `FEED.jpg` — la grilla simulada, con el recorte 1:1 real de Instagram.
- `portadas/post-NN.png` — las 19 portadas a 1080×1350, listas para usar como punto de
  partida de cada carrusel.
- `_fuente/grilla_feed.py` — el generador: se edita la tabla `PLAN`, se corre, y salen de
  nuevo el HTML, las 19 portadas y `FEED.jpg`. Antes sólo escribía el HTML y las portadas
  había que rehacerlas a mano, así que un cambio en `PLAN` dejaba el feed simulado
  diciendo algo que ya no era cierto.
