"""Destacado 'Gratis' — las historias de adentro. Formato 1080x1920."""
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

H = []

# 01 — la oferta
H.append("""
<div class="h tinta" id="g1">
  <img class="bg" src="fotos_hi/px-8369211.jpg"
       style="object-position:50% 52%;filter:grayscale(1) brightness(.62) contrast(1.12)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Muestra gratis</div>
  <div class="cuerpo" style="bottom:520px">
    <h2 style="color:#fff">La muestra<br><span class="it" style="color:var(--orange)">es gratis.</span></h2>
    <div class="txt" style="margin-top:44px">Ves tu web rediseñada antes de decidir nada.</div>
  </div>
</div>""")

# 02 — que es exactamente
H.append("""
<div class="h papel" id="g2">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">Qué hacemos</div>
  <div class="cuerpo" style="top:620px">
    <div class="eyebrow">Sin costo</div>
    <h2 style="margin-top:28px">Rediseñamos<br>tu web entera.</h2>
    <div class="txt" style="margin-top:44px">
      Con tu contenido real: tus textos, tus fotos, tus datos.
      No es una plantilla ni un boceto.
    </div>
  </div>
</div>""")

# 03 — como funciona
H.append("""
<div class="h tinta" id="g3">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Cómo funciona</div>
  <div class="cuerpo" style="top:560px">
    <h2 style="color:#fff;font-size:92px">Cómo funciona.</h2>
    <div style="margin-top:56px">
      <div class="paso"><span class="n">01</span><p>Nos envías el link de tu web.</p></div>
      <div class="paso"><span class="n">02</span><p>La rediseñamos entera.</p></div>
      <div class="paso"><span class="n">03</span><p>Te pasamos un enlace privado, navegable.</p></div>
      <div class="paso" style="border-bottom:1px solid rgba(255,255,255,.18)">
        <span class="n">04</span><p>Decides sobre algo real.</p></div>
    </div>
  </div>
</div>""")

# 04 — la condicion
H.append("""
<div class="h naranja" id="g4">
  <div class="marca"><img src="assets/logo-white.png" alt=""></div>
  <div class="rot">Sin letra chica</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-50%)">
    <h2>Sin costo.<br><span class="it">Sin compromiso.</span></h2>
    <div class="txt" style="margin-top:48px">
      Si te convence, la publicamos. Si no, no pasa nada y te quedas con la idea.
    </div>
  </div>
</div>""")

# 05 — el llamado
H.append("""
<div class="h tinta" id="g5">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Empieza aquí</div>
  <div class="cuerpo" style="top:620px">
    <h2 style="color:#fff">Envíanos el link<br>de tu web.</h2>
    <div class="txt" style="margin-top:44px">Te la devolvemos rediseñada, navegable y sin cargo.</div>
    <div class="it" style="margin-top:64px;font-family:var(--f-display);font-size:58px;
         letter-spacing:-.02em;color:var(--orange);display:inline-block;
         border-bottom:3px solid var(--orange);padding-bottom:14px">
      Escríbenos por DM →
    </div>
  </div>
</div>""")

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="renueva-fonts.css"><style>' + base + CSS +
       '</style></head><body>' + "".join(H) + '</body></html>')
HERE.joinpath("historias-gratis.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS" / "gratis"
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000}, device_scale_factor=1)
    pg.goto(HERE.joinpath("historias-gratis.html").resolve().as_uri())
    pg.wait_for_timeout(2200)
    # control: nada fuera de la zona segura de historia (260 a 1660)
    fuera = pg.evaluate("""() => { const o=[];
      document.querySelectorAll('.h').forEach(h=>{ const hb=h.getBoundingClientRect();
        h.querySelectorAll('h2,.txt,.paso,.eyebrow,.marca,.rot,.it').forEach(el=>{
          const b=el.getBoundingClientRect();
          const t=b.top-hb.top, bo=b.bottom-hb.top;
          if(t<260||bo>1660) o.push(h.id+' '+(el.className||el.tagName)+' '+Math.round(t)+'-'+Math.round(bo)); }); });
      return o; }""")
    print("fuera de zona segura:", fuera if fuera else "nada")
    for i in range(1, 6):
        guardar(pg.query_selector("#g%d" % i), OUT / ("gratis-%02d.png" % i))
    b.close()
print("5 historias en DESTACADOS/gratis/")
