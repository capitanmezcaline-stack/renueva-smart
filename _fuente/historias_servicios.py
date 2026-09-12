"""Destacado 'Servicios' — qué hacemos y para quién. Historias de 1080x1920."""
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
.h .sector{display:flex;align-items:baseline;gap:26px;padding:24px 0;
           border-top:1px solid rgba(255,255,255,.24)}
.h .sector .p{width:12px;height:12px;background:var(--ink);flex:0 0 12px;
              transform:rotate(45deg)}
.h .sector span{font-family:var(--f-display);font-weight:600;font-size:50px;
                line-height:1.14;letter-spacing:-.018em}
"""

H = []

# Todo el texto sale de renuevasmart.com (secciones "Qué hacemos" y "Sectores"),
# pasado a tuteo neutro y con "celular" -> "teléfono".

# 01 — el gancho: es el titular de la seccion Servicios del sitio
H.append("""
<div class="h tinta" id="s1">
  <img class="bg" src="fotos_hi/px-9331582.jpg"
       style="object-position:50% 54%;filter:grayscale(1) brightness(.58) contrast(1.12)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Qué hacemos</div>
  <div class="cuerpo" style="bottom:470px">
    <h2 style="color:#fff;font-size:84px">Que tu profesionalismo<br>también se vea en el<br><span class="it" style="color:var(--orange)">ámbito digital.</span></h2>
  </div>
</div>""")

# 02 — Diseño
H.append("""
<div class="h papel" id="s2">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">01 — Diseño</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-50%)">
    <div class="eyebrow">01</div>
    <h2 style="margin-top:26px;font-size:112px">Diseño.</h2>
    <div class="txt" style="margin-top:42px">
      Identidad visual, estructura y contenido ordenados para que el visitante
      entienda en segundos qué ofreces y por qué elegirte.
    </div>
  </div>
</div>""")

# 03 — Rendimiento
H.append("""
<div class="h tinta" id="s3">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">02 — Rendimiento</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-50%)">
    <div class="eyebrow">02</div>
    <h2 style="margin-top:26px;color:#fff;font-size:112px">Rendimiento.</h2>
    <div class="txt" style="margin-top:42px">
      Sitios rápidos, adaptados al teléfono, hechos para tus clientes.
    </div>
  </div>
</div>""")

# 04 — Soporte
H.append("""
<div class="h papel" id="s4">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">03 — Soporte</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-50%)">
    <div class="eyebrow">03</div>
    <h2 style="margin-top:26px;font-size:112px">Soporte.</h2>
    <div class="txt" style="margin-top:42px">
      Después de publicado el diseño, seguimos disponibles para asesorarte
      en lo que necesites.
    </div>
  </div>
</div>""")

# 05 — Sectores, tal como los lista el sitio
H.append("""
<div class="h naranja" id="s5">
  <div class="marca"><img src="assets/logo-white.png" alt=""></div>
  <div class="rot">Sectores</div>
  <div class="cuerpo" style="top:490px">
    <h2 style="font-size:86px">Servicios<br>profesionales que<br>venden confianza.</h2>
  </div>
  <div style="position:absolute;left:96px;right:96px;top:900px;z-index:6">
    <div class="sector"><span class="p"></span><span>Abogados y estudios jurídicos</span></div>
    <div class="sector"><span class="p"></span><span>Notarías y escribanías</span></div>
    <div class="sector"><span class="p"></span><span>Gestorías y asesorías</span></div>
    <div class="sector"><span class="p"></span><span>Inmobiliarias</span></div>
    <div class="sector"><span class="p"></span><span>Clínicas dentales</span></div>
    <div class="sector" style="border-bottom:1px solid rgba(255,255,255,.24)">
      <span class="p"></span><span>Clínicas de estética</span></div>
  </div>
</div>""")

# 06 — el llamado, tal como lo dice el sitio
H.append("""
<div class="h tinta" id="s6">
  <img class="bg" src="fotos_hi/px-2290554.jpg"
       style="object-position:50% 46%;filter:grayscale(1) brightness(.56) contrast(1.14)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Empieza aquí</div>
  <div class="cuerpo" style="bottom:460px">
    <h2 style="color:#fff;font-size:92px">Envíanos el link<br>de tu web actual.</h2>
    <div class="txt" style="margin-top:42px">
      Armamos tu antes/después, sin costo ni compromiso.
    </div>
    <div class="it" style="margin-top:54px;font-family:var(--f-display);font-size:56px;
         letter-spacing:-.02em;color:var(--orange);display:inline-block;
         border-bottom:3px solid var(--orange);padding-bottom:14px">
      Escríbenos por DM →
    </div>
  </div>
</div>""")

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="renueva-fonts.css"><style>' + base + CSS + EXTRA +
       '</style></head><body>' + "".join(H) + '</body></html>')
HERE.joinpath("historias-servicios.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS" / "servicios"
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000})
    pg.goto(HERE.joinpath("historias-servicios.html").resolve().as_uri())
    pg.wait_for_timeout(2400)
    fuera = pg.evaluate("""() => { const o=[];
      document.querySelectorAll('.h').forEach(h=>{ const hb=h.getBoundingClientRect();
        h.querySelectorAll('h2,.txt,.eyebrow,.marca,.rot,.it,.sector').forEach(el=>{
          const b=el.getBoundingClientRect(), t=b.top-hb.top, bo=b.bottom-hb.top;
          if(t<260||bo>1660) o.push(h.id+' '+(el.className||el.tagName)+' '+Math.round(t)+'-'+Math.round(bo)); }); });
      return o; }""")
    print("fuera de zona segura:", fuera if fuera else "nada")
    for i in range(1, 7):
        guardar(pg.query_selector("#s%d" % i), OUT / ("servicios-%02d.png" % i))
    b.close()
print("6 historias en DESTACADOS/servicios/")
