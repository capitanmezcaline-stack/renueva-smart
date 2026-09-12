"""Genera las portadas del plan de contenido y arma la grilla del feed."""
import pathlib, subprocess, re

HERE = pathlib.Path(__file__).parent

# --- los 19 posteos en ORDEN DE PUBLICACION ---
# (semana, titulo del plan, linea 1, linea 2, bajada, etiqueta)
PLAN = [
 (1,"3 señales de una web vieja","Tres señales","de una web vieja.","Las que aparecen una y otra vez.","Diagnóstico"),
 (1,"Web Roast #1","Web roast","#01","Analizamos una web real, sin filtro.","Web roast"),
 (1,"5 errores de diseño","Cinco errores","de diseño web.","Y cómo se ven desde afuera.","Diseño"),
 (1,"¿Tu web parece de 2015?","¿Tu web parece","de 2015?","Cuatro detalles que la delatan.","Diagnóstico"),
 (1,"Presentación de Renueva Smart","Renovamos webs","que quedaron atrás.","Quiénes somos y cómo trabajamos.","Quiénes somos"),

 (2,"Antes/después restaurante","Antes y después:","un restaurante.","Mismo local, otra primera impresión.","Caso"),
 (2,"Antes/después inmobiliaria","Antes y después:","una inmobiliaria.","Ordenar para que encuentren.","Caso"),
 (2,"Antes/después dentista","Antes y después:","una clínica dental.","Pedir cita en un toque.","Caso"),
 (2,"Cómo mejorar una home","Cómo mejorar","tu página de inicio.","Lo primero que ve todo el mundo.","Estructura"),
 (2,"Rediseño en 30 segundos","Un rediseño","en 30 segundos.","El antes y el después, rápido.","Antes y después"),

 (3,"Qué debe tener una web moderna","Qué tiene hoy","una web moderna.","Seis cosas que ya no son opcionales.","Autoridad"),
 (3,"Errores en mobile","Los errores","que se ven en el celular.","Donde te mira casi todo el mundo.","Móvil"),
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
        col1, col2, colb = "#fff", "var(--ink)", "rgba(255,255,255,.94)"
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
