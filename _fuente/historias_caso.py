"""Destacado 'El caso' — Escribanía Acosta Pastore. Historias de 1080x1920.

Texto tomado de renuevasmart.com (sección Reseñas) y capturas propias de los dos
sitios reales, bajadas con capturar_caso.py.
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
.h .cita{font-family:var(--f-display);font-weight:700;font-style:italic;font-size:64px;
         line-height:1.22;letter-spacing:-.02em}
.h .firma{font-family:var(--f-body);font-weight:700;font-size:22px;letter-spacing:.18em;
          text-transform:uppercase;margin-top:44px;display:block}
.h .pie{font-family:var(--f-body);font-weight:700;font-size:20px;letter-spacing:.2em;
        text-transform:uppercase;color:var(--grey)}
.h.tinta .pie{color:#767C83}
"""

H = []

# 01 — el gancho
H.append("""
<div class="h tinta" id="c1">
  <img class="bg" src="fotos_hi/px-22037275.jpg"
       style="object-position:50% 46%;filter:grayscale(1) brightness(.54) contrast(1.14)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Caso real</div>
  <div class="cuerpo" style="bottom:470px">
    <h2 style="color:#fff;font-size:100px">Un caso<br><span class="it" style="color:var(--orange)">real.</span></h2>
    <div class="txt" style="margin-top:42px">
      Escribanía Acosta Pastore, en Carrasco, Montevideo.
    </div>
  </div>
</div>""")

# 02 — el antes
H.append("""
<div class="h tinta" id="c2">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Antes</div>
  <div class="cuerpo" style="top:520px">
    <div class="eyebrow">Antes</div>
    <h2 style="margin-top:26px;color:#fff;font-size:96px">Toda su presencia,<br>en un blog.</h2>
  </div>
  <div class="frame lift" style="left:96px;right:96px;top:900px;height:500px">
    <div class="bar"><i></i><i></i><i></i><span>escribaniacostapastore.com</span></div>
    <img src="assets/caso-antes-desktop.jpg" style="width:100%;display:block">
  </div>
  <div class="pie" style="position:absolute;left:96px;bottom:300px;z-index:9">Plantilla genérica</div>
</div>""")

# 03 — el despues
H.append("""
<div class="h papel" id="c3">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">Después</div>
  <div class="cuerpo" style="top:520px">
    <div class="eyebrow">Después</div>
    <h2 style="margin-top:26px;font-size:96px">Un sitio propio,<br>con criterio.</h2>
  </div>
  <div class="frame lift-soft" style="left:96px;right:96px;top:900px;height:500px">
    <div class="bar"><i></i><i></i><i></i><span>acostapastore.com</span></div>
    <img src="assets/caso-despues-desktop.jpg" style="width:100%;display:block">
  </div>
  <div class="pie" style="position:absolute;left:96px;bottom:300px;z-index:9;color:var(--orange)">Rediseño completo</div>
</div>""")

# 04 — el movil, lado a lado
H.append("""
<div class="h tinta" id="c4">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">En el teléfono</div>
  <div class="cuerpo" style="top:490px">
    <h2 style="color:#fff;font-size:92px">Y en el teléfono,<br>que es donde miran.</h2>
  </div>
  <div style="position:absolute;left:96px;top:840px;width:380px;z-index:6">
    <span class="pie" style="display:block;margin-bottom:18px">Antes</span>
    <div style="border-radius:26px;overflow:hidden;border:8px solid #22262B;height:470px;opacity:.62">
      <img src="assets/caso-antes-movil.jpg" style="width:100%;display:block;filter:grayscale(1)">
    </div>
  </div>
  <div style="position:absolute;right:96px;top:840px;width:380px;z-index:6">
    <span class="pie" style="display:block;margin-bottom:18px;color:var(--orange)">Después</span>
    <div class="lift" style="border-radius:26px;overflow:hidden;border:8px solid #16181B;height:470px">
      <img src="assets/caso-despues-movil.jpg" style="width:100%;display:block">
    </div>
  </div>
</div>""")

# 05 — la reseña, textual del sitio
H.append("""
<div class="h naranja" id="c5">
  <div class="marca"><img src="assets/logo-white.png" alt=""></div>
  <div class="rot">Lo que dicen</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-50%)">
    <div class="cita">"Me encontré admirado por lo que Renueva Smart hizo con total liberalidad.
      Su diseño es superior a lo que yo tenía publicado."</div>
    <span class="firma">Bruno Acosta Pastore · Escribano</span>
  </div>
</div>""")

# 06 — el llamado
H.append("""
<div class="h papel" id="c6">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">Empieza aquí</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-52%)">
    <h2 style="font-size:96px">¿Hacemos lo mismo<br>con la tuya?</h2>
    <div class="txt" style="margin-top:42px">
      Envíanos el link de tu web actual y armamos tu antes/después,
      sin costo ni compromiso.
    </div>
    <div class="it" style="margin-top:56px;font-family:var(--f-display);font-size:56px;
         letter-spacing:-.02em;color:var(--orange);display:inline-block;
         border-bottom:3px solid var(--orange);padding-bottom:14px">
      Escríbenos por DM →
    </div>
  </div>
</div>""")

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="renueva-fonts.css"><style>' + base + CSS + EXTRA +
       '</style></head><body>' + "".join(H) + '</body></html>')
HERE.joinpath("historias-caso.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS" / "el-caso"
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000})
    pg.goto(HERE.joinpath("historias-caso.html").resolve().as_uri())
    pg.wait_for_timeout(2600)
    fuera = pg.evaluate("""() => { const o=[];
      document.querySelectorAll('.h').forEach(h=>{ const hb=h.getBoundingClientRect();
        h.querySelectorAll('h2,.txt,.eyebrow,.marca,.rot,.it,.frame,.cita,.firma,.pie').forEach(el=>{
          const b=el.getBoundingClientRect(), t=b.top-hb.top, bo=b.bottom-hb.top;
          if(t<260||bo>1660) o.push(h.id+' '+(el.className||el.tagName)+' '+Math.round(t)+'-'+Math.round(bo)); }); });
      return o; }""")
    print("fuera de zona segura:", fuera if fuera else "nada")
    for i in range(1, 7):
        guardar(pg.query_selector("#c%d" % i), OUT / ("el-caso-%02d.png" % i))
    b.close()
print("6 historias en DESTACADOS/el-caso/")
