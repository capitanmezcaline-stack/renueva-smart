"""Genera las portadas del plan de contenido y arma la grilla del feed."""
import pathlib, subprocess, re

HERE = pathlib.Path(__file__).parent

# --- los 19 posteos en ORDEN DE PUBLICACION ---
# (semana, titulo del plan, linea 1, linea 2, bajada, etiqueta)
PLAN = [
 (1,"3 señales de una web vieja","Tres señales","de una web vieja.","Las que aparecen una y otra vez.","Diagnóstico"),
 (1,"Web Roast #1","Web roast","#01","Analizamos una web real, sin filtro.","Web roast"),
 (1,"5 errores de diseño","Cinco errores","de diseño web.","Los que hacen que una web parezca poco profesional.","Diseño"),
 (1,"¿Tu web parece de 2015?","¿Tu web parece","de 2015?","Seis detalles que la delatan.","Diagnóstico"),
 (1,"Presentación de Renueva Smart","Renovamos webs","que quedaron atrás.","Quiénes somos y cómo trabajamos.","Quiénes somos"),

 (2,"Antes/después restaurante","Antes y después:","un restaurante.","Mismo local, otra primera impresión.","Caso"),
 (2,"Antes/después inmobiliaria","Antes y después:","una inmobiliaria.","Ordenar para que encuentren.","Caso"),
 (2,"Antes/después dentista","Antes y después:","una clínica dental.","Pedir cita en un toque.","Caso"),
 (2,"Cómo mejorar una home","Cómo mejorar","tu página de inicio.","Lo primero que ve todo el mundo.","Estructura"),
 (2,"Rediseño en 30 segundos","Un rediseño","en 30 segundos.","El antes y el después, rápido.","Antes y después"),

 (3,"Qué debe tener una web moderna","Qué tiene hoy","una web moderna.","Seis cosas que ya no son opcionales.","Autoridad"),
 (3,"Errores en mobile","Los errores","que se ven en el teléfono.","Donde te mira casi todo el mundo.","Móvil"),
 (3,"CTA que debería tener tu web","El botón que","tu web no tiene.","Y por eso nadie te escribe.","Conversión"),
 (3,"Web Roast #2","Web roast","#02","Analizamos una web real, sin filtro.","Web roast"),
 (3,"No necesitas rehacer todo tu negocio","No necesitas rehacer","todo tu negocio.","Sólo que tu web lo cuente mejor.","Autoridad"),

 (4,"Caso de transformación","Un caso de","transformación.","De un blog genérico a una web propia.","Caso real"),
 (4,"Cuánto cuesta renovar una web","¿Cuánto cuesta","renovar una web?","Lo decimos de frente.","Precios"),
 (4,"Qué incluye Renueva Smart","Qué incluye","una renovación.","Sin letra chica.","Servicio"),
 (4,"Web Roast #3","Web roast","#03","Analizamos una web real, sin filtro.","Web roast"),
]

# --- reparto de materiales por POSICION EN LA GRILLA ---
# Un ciclo regular de 4 evita vecinos iguales pero dibuja diagonales y se lee mecanico.
# Esto salio de una busqueda aleatoria con restricciones (ver REPARTO.md):
# prohibido repetir a la izquierda y arriba; penalizadas las diagonales, las filas
# identicas y las filas en espejo; reparto parejo entre los cuatro materiales.
POR_POSICION = ["naranja","blanco","negro", "negro","foto","naranja",
                "naranja","blanco","foto",  "foto","negro","naranja",
                "negro","blanco","foto",    "foto","naranja","negro",
                "blanco"]
# criterio: oficina profesional en uso, obra y ciudad. Nada de bodegones ni texturas.
FOTOS = ["px-25461690.jpg", "px-12314551.jpg", "px-946310.jpg",
         "px-3818947.jpg", "px-15275312.jpg"]

# el feed muestra lo mas nuevo primero: la posicion 4 de la grilla es el ultimo posteo
N = len(PLAN)
material = {}
for pos in range(N):                              # pos 0 => posicion 4 de la grilla
    material[N - 1 - pos] = POR_POSICION[pos]

base = HERE.joinpath("post-1.src.html").read_text(encoding="utf-8").split("<style>")[1].split("</style>")[0]

EXTRA = """
.slide{width:1080px;height:1350px}
.tile-foto .bg{filter:grayscale(1) brightness(.82) contrast(1.12)}
.l1,.l2{display:table;white-space:nowrap}
.bloque.abajo{bottom:300px}
.bloque.centrado{top:50%;transform:translateY(-46%)}
"""

def tile(i, d, mat):
    sem, plan, l1, l2, baja, etiqueta = d
    idf = "t%02d" % i
    if mat == "foto":
        n_foto = sorted(k for k, v in material.items() if v == "foto").index(i)
        foto = FOTOS[n_foto % len(FOTOS)]
        clases, logo = "slide dark on-dark tile-foto", "assets/logo.png"
        fondo = ('<img class="bg" src="fotos_hi/%s" style="object-position:50%% 52%%">'
                 '<div class="veil-cover"></div>' % foto)
        col1, col2, colb = "#fff", "var(--orange)", "#A7ACB2"
    elif mat == "negro":
        clases, logo, fondo = "slide dark on-dark", "assets/logo.png", ""
        col1, col2, colb = "#fff", "var(--orange)", "#A7ACB2"
    elif mat == "naranja":
        clases, logo, fondo = "slide orange", "assets/logo-white.png", ""
        # tinta en la primera linea y blanco en la italica: sobre naranja el
        # negro da el peso y la italica blanca salta. Al reves la italica se hunde.
        col1, col2, colb = "var(--ink)", "#fff", "rgba(255,255,255,.94)"
    else:
        clases, logo, fondo = "slide white", "assets/logo-dark.png", ""
        col1, col2, colb = "var(--ink)", "var(--orange)", "var(--body)"

    ancla = "centrado" if mat in ("negro","naranja","blanco") else "abajo"
    return """
<div class="%s" id="%s">
  %s
  <div class="top"><img src="%s" alt=""><span class="lbl">%s</span></div>
  <div class="bloque %s" style="position:absolute;left:var(--safe);right:var(--safe);z-index:6">
    <h1 class="tit" style="font-size:120px;color:%s">
      <span class="l1">%s</span><span class="l2 it" style="color:%s">%s</span>
    </h1>
    <div class="line" style="margin-top:38px;color:%s">%s</div>
  </div>
</div>
""" % (clases, idf, fondo, logo, etiqueta, ancla, col1, l1, col2, l2, colb, baja)

tiles = "".join(tile(i, d, material[i]) for i, d in enumerate(PLAN))

AJUSTE = """
<script>
document.fonts.ready.then(() => {
  const util = 1080 - 112*2;
  document.querySelectorAll('.tit').forEach(h => {
    let px = 132;
    h.style.fontSize = px + 'px';
    const lineas = [...h.querySelectorAll('.l1,.l2')];
    while (px > 40 && lineas.some(l => l.getBoundingClientRect().width > util)) {
      px -= 2; h.style.fontSize = px + 'px';
    }
  });
  document.documentElement.setAttribute('data-listo','1');
});
</script>
"""

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="renueva-fonts.css">'
       '<style>' + base + EXTRA + '</style></head><body>' + tiles + AJUSTE + '</body></html>')
HERE.joinpath("grilla-feed.html").write_text(doc, encoding="utf-8")
print("grilla-feed.html con", N, "portadas")

for i, d in enumerate(PLAN):
    print("  %02d  S%d  %-38s %s" % (i + 1, d[0], d[1][:38], material[i]))

# ------------------------------------------------------------------
# Render de las 19 portadas y armado de FEED.jpg.
# Antes esto se hacia a mano y el docstring mentia: al cambiar la tabla
# PLAN se regeneraba el HTML pero FEED.jpg y portadas/ quedaban viejas.
# ------------------------------------------------------------------
import shutil, sys, time
from PIL import Image, ImageDraw

TILE, GAP, HEAD = 302, 3, 56
RAIZ = HERE.parent
DEST = RAIZ / "PLAN-CONTENIDO" / "portadas"
DEST.mkdir(parents=True, exist_ok=True)
TMP = HERE / "_tiles"

subprocess.run([sys.executable, "render.py", "grilla-feed.html", "_tiles",
                ",".join("t%02d" % i for i in range(N)), "1.0"],
               cwd=HERE, check=True, stdout=subprocess.DEVNULL)

def guardar(origen, destino):
    """OneDrive a veces tiene el archivo tomado; reintentar."""
    for _ in range(12):
        try:
            shutil.copy(origen, destino); return
        except OSError:
            time.sleep(1.5)
    raise SystemExit("no se pudo escribir " + str(destino))

for i in range(N):
    guardar(TMP / ("t%02d.png" % i), DEST / ("post-%02d.png" % (i + 1)))

# Instagram muestra lo mas nuevo primero: los 3 fijados y despues los
# posteos en orden inverso al de publicacion.
caras = [RAIZ / ("FIJADO-%d/RS-F%d-01.png" % (k, k)) for k in (1, 2, 3)]
caras += [DEST / ("post-%02d.png" % n) for n in range(N, 0, -1)]

filas = (len(caras) + 2) // 3
feed = Image.new("RGB", (3 * TILE + 2 * GAP, HEAD + filas * TILE + (filas - 1) * GAP),
                 "#FFFFFF")
d = ImageDraw.Draw(feed)
d.rectangle([0, 0, feed.width, HEAD], fill="#14171A")
d.text((14, 14), "FEED @renuevasmart · 3 fijados + %d posteos" % N, fill="#FFFFFF")
d.text((14, 32), "fotos: oficina profesional, obra y ciudad · ninguna se repite",
       fill="#9AA0A6")
for i, p in enumerate(caras):
    im = Image.open(p).convert("RGB")
    lado = im.width                      # recorte 1:1 real de la grilla de IG
    arriba = (im.height - lado) // 2
    im = im.crop((0, arriba, lado, arriba + lado)).resize((TILE, TILE), Image.LANCZOS)
    feed.paste(im, ((i % 3) * (TILE + GAP), HEAD + (i // 3) * (TILE + GAP)))

guardar_feed = RAIZ / "PLAN-CONTENIDO" / "FEED.jpg"
feed.save(guardar_feed, quality=92)
shutil.rmtree(TMP, ignore_errors=True)
print("portadas/post-01..%02d.png  ·  FEED.jpg %dx%d" % (N, feed.width, feed.height))
