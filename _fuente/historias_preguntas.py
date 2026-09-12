"""Destacado 'Preguntas' — las FAQ del sitio. Historias de 1080x1920.

Preguntas y respuestas textuales de renuevasmart.com, seccion "Preguntas".
De las siete del sitio se eligen las cinco que resuelven objeciones;
la del precio vive en el destacado "Precios".
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
.h .textopreg{font-family:var(--f-display);font-weight:700;font-size:82px;line-height:1.1;
             letter-spacing:-.02em}
.h .regla{height:1px;background:var(--line);margin:40px 0}
.h.tinta .regla{background:#22262B}
.h.naranja .regla{background:rgba(255,255,255,.34)}
"""

# (id, fondo, logo, pregunta con <br>, respuesta)
FAQ = [
    ("q2", "papel", "logo-dark.png",
     "¿Cómo hacen el<br>antes/después<br>sin que se lo pida?",
     "Elegimos negocios cuya web creemos que podemos mejorar mucho, y armamos "
     "la propuesta nosotros, sin compromiso de tu parte. Tú solo ves el resultado y decides."),
    ("q3", "tinta", "logo.png",
     "¿Tiene costo ver<br>mi antes/después?",
     "No. Diseñamos y te damos la muestra sin costo ni compromiso de compra por tu parte."),
    ("q4", "papel", "logo-dark.png",
     "¿Y si no me gusta<br>el resultado?",
     "No pasa nada. Ves la propuesta, y si no te convence, no seguimos. No hay letra chica."),
    ("q5", "tinta", "logo.png",
     "¿Cuánto tarda<br>el rediseño<br>completo?",
     "Depende del tamaño de la web, pero la mayoría de los sitios quedan listos para "
     "publicar en pocas semanas desde que confirmas que seguimos."),
    ("q6", "papel", "logo-dark.png",
     "¿Qué pasa con el<br>contenido de mi<br>web actual?",
     "Reutilizamos tus textos, fotos y datos reales. No inventamos información sobre "
     "tu negocio: solo la presentamos mejor."),
]

H = []

# 01 — el gancho: titular de la seccion en el sitio
H.append("""
<div class="h tinta" id="q1">
  <img class="bg" src="fotos_hi/px-26984758.jpg"
       style="object-position:50% 48%;filter:grayscale(1) brightness(.54) contrast(1.14)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Preguntas</div>
  <div class="cuerpo" style="bottom:470px">
    <h2 style="color:#fff;font-size:90px">Todo lo que necesitas<br>saber<span class="it" style="color:var(--orange)"> antes de empezar.</span></h2>
  </div>
</div>""")

for idf, fondo, logo, preg, resp in FAQ:
    color = "#fff" if fondo == "tinta" else "var(--ink)"
    H.append("""
<div class="h %s" id="%s">
  <div class="marca"><img src="assets/%s" alt=""></div>
  <div class="rot">Preguntas</div>
  <div class="cuerpo" style="top:50%%;transform:translateY(-50%%)">
    <div class="textopreg" style="color:%s">%s</div>
    <div class="regla"></div>
    <div class="txt">%s</div>
  </div>
</div>""" % (fondo, idf, logo, color, preg, resp))

# 07 — el llamado
H.append("""
<div class="h naranja" id="q7">
  <div class="marca"><img src="assets/logo-white.png" alt=""></div>
  <div class="rot">Empieza aquí</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-52%)">
    <h2 style="font-size:94px">¿Te quedó<br>alguna duda?</h2>
    <div class="txt" style="margin-top:44px">
      Escríbenos y te la respondemos. Y si quieres, envíanos el link de tu web
      y armamos tu antes/después.
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
HERE.joinpath("historias-preguntas.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS" / "preguntas"
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000})
    pg.goto(HERE.joinpath("historias-preguntas.html").resolve().as_uri())
    pg.wait_for_timeout(2600)
    fuera = pg.evaluate("""() => { const o=[];
      document.querySelectorAll('.h').forEach(h=>{ const hb=h.getBoundingClientRect();
        h.querySelectorAll('h2,.txt,.marca,.rot,.it').forEach(el=>{
          const b=el.getBoundingClientRect(), t=b.top-hb.top, bo=b.bottom-hb.top;
          if(t<260||bo>1660) o.push(h.id+' '+(el.className||el.tagName)+' '+Math.round(t)+'-'+Math.round(bo)); }); });
      return o; }""")
    print("fuera de zona segura:", fuera if fuera else "nada")
    ids = ["q1"] + [f[0] for f in FAQ] + ["q7"]
    for i, idf in enumerate(ids, 1):
        guardar(pg.query_selector("#" + idf), OUT / ("preguntas-%02d.png" % i))
    b.close()
print("7 historias en DESTACADOS/preguntas/")
