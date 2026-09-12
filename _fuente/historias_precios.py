"""Destacado 'Precios' — Sin letra chica + los rangos. Historias de 1080x1920.

Texto tomado de renuevasmart.com: seccion "Sin letra chica" y la respuesta
a "cuanto cuesta el rediseno" de las preguntas frecuentes.
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
.h .tarifa{display:flex;justify-content:space-between;align-items:baseline;gap:24px;
           padding:32px 0;border-top:1px solid var(--line)}
.h.tinta .tarifa{border-top-color:#22262B}
.h .tarifa .q{font-family:var(--f-body);font-weight:400;font-size:36px;color:var(--body)}
.h.tinta .tarifa .q{color:#A7ACB2}
.h .tarifa .v{font-family:var(--f-display);font-weight:700;font-size:52px;
              letter-spacing:-.02em;white-space:nowrap}
.h .tarifa .v b{color:var(--orange);font-weight:700}
.h .inc{display:flex;gap:26px;padding:28px 0;border-top:1px solid var(--line)}
.h.tinta .inc{border-top-color:#22262B}
.h .inc .d{width:13px;height:13px;background:var(--orange);flex:0 0 13px;
           transform:rotate(45deg);margin-top:18px}
.h .inc b{font-family:var(--f-display);font-weight:700;font-size:46px;letter-spacing:-.02em;
          display:block;margin-bottom:8px}
.h .inc span{font-family:var(--f-body);font-size:31px;line-height:1.4;color:var(--body)}
.h.tinta .inc span{color:#A7ACB2}
"""

H = []

# 01 — el gancho
H.append("""
<div class="h tinta" id="r1">
  <img class="bg" src="fotos_hi/px-12446411.jpg"
       style="object-position:50% 44%;filter:grayscale(1) brightness(.54) contrast(1.14)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Precios</div>
  <div class="cuerpo" style="bottom:470px">
    <h2 style="color:#fff;font-size:92px">Lo que incluye,<br><span class="it" style="color:var(--orange)">dicho de frente.</span></h2>
    <div class="txt" style="margin-top:42px">
      Las condiciones, claras desde el principio. Sin sorpresas al final.
    </div>
  </div>
</div>""")

# 02 — los rangos
H.append("""
<div class="h papel" id="r2">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">Referencia</div>
  <div class="cuerpo" style="top:490px">
    <h2 style="font-size:92px">Cuánto cuesta<br>un rediseño.</h2>
  </div>
  <div style="position:absolute;left:96px;right:96px;top:820px;z-index:6">
    <div class="tarifa"><span class="q">Una página</span><span class="v">400 – 650 <b>€</b></span></div>
    <div class="tarifa"><span class="q">De 2 a 5 páginas</span><span class="v">700 – 1.200 <b>€</b></span></div>
    <div class="tarifa" style="border-bottom:1px solid var(--line)">
      <span class="q">De 6 a 10 páginas</span><span class="v">1.200 – 2.200 <b>€</b></span></div>
  </div>
  <div class="txt" style="position:absolute;left:96px;right:96px;bottom:300px;z-index:6;font-size:34px">
    Como referencia orientativa. El precio depende sobre todo del tamaño.
  </div>
</div>""")

# 03 — la salvedad
H.append("""
<div class="h tinta" id="r3">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">El número cerrado</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-50%)">
    <h2 style="color:#fff;font-size:92px">El número cerrado<br>te lo damos<br><span class="it" style="color:var(--orange)">tras ver tu web.</span></h2>
    <div class="txt" style="margin-top:44px">
      Depende del tamaño, de si partimos de cero y de quién la publica.
    </div>
  </div>
</div>""")

# 04 — que incluye
H.append("""
<div class="h papel" id="r4">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">Incluido</div>
  <div class="cuerpo" style="top:470px">
    <h2 style="font-size:96px">Qué incluye.</h2>
  </div>
  <div style="position:absolute;left:96px;right:96px;top:720px;z-index:6">
    <div class="inc"><span class="d"></span><div>
      <b>Pago único</b><span>Un solo pago cuando publicamos. Sin cuotas mensuales ni permanencia.</span></div></div>
    <div class="inc"><span class="d"></span><div>
      <b>Alojamiento incluido</b><span>Dejamos el sitio publicado y funcionando, con el alojamiento cubierto.</span></div></div>
    <div class="inc" style="border-bottom:1px solid var(--line)"><span class="d"></span><div>
      <b>Dos rondas de ajustes</b><span>Incluidas en el precio, antes de publicar nada.</span></div></div>
  </div>
</div>""")

# 05 — plazos
H.append("""
<div class="h tinta" id="r5">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Plazos</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-50%)">
    <h2 style="color:#fff;font-size:96px">Plazos<br>que cumplimos.</h2>
    <div style="margin-top:52px">
      <div class="tarifa">
        <span class="q">Una web pequeña</span><span class="v" style="color:#fff">2 a 3 <b>semanas</b></span></div>
      <div class="tarifa" style="border-bottom:1px solid #22262B">
        <span class="q">Una mediana</span><span class="v" style="color:#fff">3 a 5 <b>semanas</b></span></div>
    </div>
    <div class="txt" style="margin-top:42px">Lo acordamos antes de empezar.</div>
  </div>
</div>""")

# 06 — el recordatorio y el llamado
H.append("""
<div class="h naranja" id="r6">
  <div class="marca"><img src="assets/logo-white.png" alt=""></div>
  <div class="rot">Muestra gratis</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-52%)">
    <h2 style="font-size:96px">Y el antes/después<br><span class="it">es gratis.</span></h2>
    <div class="txt" style="margin-top:44px">
      Ves tu web rediseñada con tu contenido real antes de decidir.
      Sin compromiso de compra.
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
HERE.joinpath("historias-precios.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS" / "precios"
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000})
    pg.goto(HERE.joinpath("historias-precios.html").resolve().as_uri())
    pg.wait_for_timeout(2600)
    fuera = pg.evaluate("""() => { const o=[];
      document.querySelectorAll('.h').forEach(h=>{ const hb=h.getBoundingClientRect();
        h.querySelectorAll('h2,.txt,.eyebrow,.marca,.rot,.it,.tarifa,.inc').forEach(el=>{
          const b=el.getBoundingClientRect(), t=b.top-hb.top, bo=b.bottom-hb.top;
          if(t<260||bo>1660) o.push(h.id+' '+(el.className||el.tagName)+' '+Math.round(t)+'-'+Math.round(bo)); }); });
      return o; }""")
    print("fuera de zona segura:", fuera if fuera else "nada")
    for i in range(1, 7):
        guardar(pg.query_selector("#r%d" % i), OUT / ("precios-%02d.png" % i))
    b.close()
print("6 historias en DESTACADOS/precios/")
