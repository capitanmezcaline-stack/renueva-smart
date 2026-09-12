"""Destacado 'Proceso' — los 5 pasos de "Cómo trabajamos". Historias de 1080x1920.

Todo el texto sale de renuevasmart.com, sección "Cómo trabajamos",
pasado a tuteo neutro ("ajustamos con vos" -> "ajustamos contigo").
"""
import pathlib
from playwright.sync_api import sync_playwright

def guardar(el, destino, intentos=6):
    """OneDrive bloquea el archivo de a ratos: se reintenta antes de fallar."""
    import time
    datos = el.screenshot()
    for _ in range(intentos):
        try:
            pathlib.Path(destino).write_bytes(datos)
            return
        except OSError:
            time.sleep(0.7)
    raise OSError("no se pudo escribir %s" % destino)


HERE = pathlib.Path(__file__).parent
base = HERE.joinpath("post-1.src.html").read_text(encoding="utf-8").split("<style>")[1].split("</style>")[0]
CSS = HERE.joinpath("_historias.css").read_text(encoding="utf-8")

EXTRA = """
.h .num{font-family:var(--f-body);font-weight:700;font-size:22px;letter-spacing:.2em;
        color:var(--orange)}
.h.naranja .num{color:var(--ink)}
.h .regla{height:1px;background:var(--line);margin:36px 0}
.h.tinta .regla{background:#22262B}
.h.naranja .regla{background:rgba(255,255,255,.34)}
"""

def paso(idf, fondo, logo, n, titulo, texto, extra=""):
    return """
<div class="h %s" id="%s">
  <div class="marca"><img src="assets/%s" alt=""></div>
  <div class="rot">Paso %s</div>
  <div class="cuerpo" style="top:50%%;transform:translateY(-50%%)">
    <div class="num">Paso %s</div>
    <div class="regla"></div>
    <h2 style="font-size:96px">%s</h2>
    <div class="txt" style="margin-top:40px">%s</div>
  </div>
  %s
</div>""" % (fondo, idf, logo, n, n, titulo, texto, extra)

H = []

# 01 — el gancho: titular y bajada de la seccion del sitio
H.append("""
<div class="h tinta" id="p1">
  <img class="bg" src="fotos_hi/px-11565004.jpg"
       style="object-position:50% 50%;filter:grayscale(1) brightness(.56) contrast(1.14)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Cómo trabajamos</div>
  <div class="cuerpo" style="bottom:470px">
    <h2 style="color:#fff;font-size:88px">El proceso completo,<br><span class="it" style="color:var(--orange)">sin que arriesgues nada.</span></h2>
    <div class="txt" style="margin-top:42px">
      Antes de pedirte nada, te mostramos el resultado.
    </div>
  </div>
</div>""")

H.append(paso("p2", "papel", "logo-dark.png", "01",
              "Analizamos<br>tu web actual.",
              "Vemos qué está funcionando y qué no, antes de tocar nada."))

H.append(paso("p3", "naranja", "logo-white.png", "02",
              "Diseñamos,<br>sin costo.",
              "Hacemos una versión nueva completa, con tu contenido real, "
              "sin que te tengas que preocupar por nada."))

# el paso 03 es el momento de la revelacion: se muestra con la captura real
H.append(paso("p4", "tinta", "logo.png", "03",
              "Te mostramos<br>el cambio.",
              "Un enlace privado con tu web ya rediseñada y navegable. "
              "Ese es tu antes/después.",
              """
  <div class="frame lift" style="left:96px;right:96px;bottom:300px;height:320px">
    <div class="bar"><i></i><i></i><i></i><span>enlace privado</span></div>
    <img src="assets/caso-despues-desktop.jpg" style="width:100%;display:block">
  </div>"""))

H.append(paso("p5", "papel", "logo-dark.png", "04",
              "Ajustamos<br>contigo.",
              "Si te gusta pero quieres cambios, los hacemos antes de publicar nada."))

H.append(paso("p6", "tinta", "logo.png", "05",
              "Publicamos y<br>acompañamos.",
              "Ponemos la web en línea y seguimos disponibles para ajustes y soporte."))

# 07 — el llamado
H.append("""
<div class="h naranja" id="p7">
  <div class="marca"><img src="assets/logo-white.png" alt=""></div>
  <div class="rot">Empieza aquí</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-52%)">
    <h2 style="font-size:94px">El primer paso<br>no te cuesta nada.</h2>
    <div class="txt" style="margin-top:42px">
      Envíanos el link de tu web actual y armamos tu antes/después.
    </div>
    <div class="it" style="margin-top:56px;font-family:var(--f-display);font-size:56px;
         letter-spacing:-.02em;color:var(--ink);display:inline-block;
         border-bottom:3px solid var(--ink);padding-bottom:14px">
      Escríbenos por DM →
    </div>
  </div>
</div>""")

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="renueva-fonts.css"><style>' + base + CSS + EXTRA +
       '</style></head><body>' + "".join(H) + '</body></html>')
HERE.joinpath("historias-proceso.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS" / "proceso"
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000})
    pg.goto(HERE.joinpath("historias-proceso.html").resolve().as_uri())
    pg.wait_for_timeout(2600)
    fuera = pg.evaluate("""() => { const o=[];
      document.querySelectorAll('.h').forEach(h=>{ const hb=h.getBoundingClientRect();
        h.querySelectorAll('h2,.txt,.num,.marca,.rot,.it,.frame').forEach(el=>{
          const b=el.getBoundingClientRect(), t=b.top-hb.top, bo=b.bottom-hb.top;
          if(t<260||bo>1660) o.push(h.id+' '+(el.className||el.tagName)+' '+Math.round(t)+'-'+Math.round(bo)); }); });
      return o; }""")
    print("fuera de zona segura:", fuera if fuera else "nada")
    for i in range(1, 8):
        guardar(pg.query_selector("#p%d" % i), OUT / ("proceso-%02d.png" % i))
    b.close()
print("7 historias en DESTACADOS/proceso/")
