"""Destacado '¿Tu web?' — las 4 señales, en historias de 1080x1920."""
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

OLD = """
      <div class="old" style="transform:scale(.888)">
        <div class="oh"><span class="olog">ESTUDIO GONZÁLEZ &amp; ASOC.</span>
          <span class="onav">Inicio | Quiénes somos | Servicios | Contacto</span></div>
        <div class="oban">BIENVENIDOS A NUESTRO SITIO WEB</div>
        <div class="obody">
          <div class="ocol"><div class="ottl">Quiénes somos</div>
            <p>Somos una empresa dedicada a brindar el mejor servicio a nuestros clientes, con una amplia trayectoria en el mercado y un equipo de profesionales altamente capacitados.</p></div>
          <div class="oimg">imagen.jpg</div>
        </div>
      </div>"""

OLD_MOVIL = """
      <div class="old" style="transform:scale(.46)">
        <div class="oh"><span class="olog">ESTUDIO GONZÁLEZ &amp; ASOC.</span>
          <span class="onav">Inicio | Quiénes somos | Servicios | Contacto</span></div>
        <div class="oban">BIENVENIDOS A NUESTRO SITIO WEB</div>
        <div class="obody">
          <div class="ocol"><div class="ottl">Quiénes somos</div>
            <p>Somos una empresa dedicada a brindar el mejor servicio a nuestros clientes, con una amplia trayectoria en el mercado y un equipo de profesionales altamente capacitados que trabaja día a día para superar sus expectativas.</p>
            <p>No dude en contactarnos para solicitar más información sobre nuestros servicios.</p></div>
          <div class="oimg">imagen.jpg</div>
        </div>
        <div class="obody"><div class="ocol"><div class="ottl">Nuestros servicios</div>
          <p>Contamos con una amplia gama de servicios pensados para cubrir todas las necesidades de nuestros clientes, tanto particulares como empresas.</p>
          <p>Consúltenos sin compromiso y le responderemos a la brevedad.</p></div></div>
        <div class="obody"><div class="ocol"><div class="ottl">Novedades</div>
          <p>Manténgase informado sobre las últimas novedades del sector a través de nuestra sección de noticias, actualizada periódicamente por nuestro equipo de profesionales.</p>
          <p>Suscríbase a nuestro boletín para recibir información en su correo.</p></div></div>
        <div class="ofoot"><span>© 2014 Estudio González &amp; Asoc.</span>
          <span class="ocount">Visitas: 004821</span></div>
      </div>"""

H = []

# 01 — el gancho
H.append("""
<div class="h tinta" id="w1">
  <img class="bg" src="fotos_hi/px-22711217.jpg"
       style="object-position:50% 50%;filter:grayscale(1) brightness(.6) contrast(1.14)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Diagnóstico</div>
  <div class="cuerpo" style="bottom:520px">
    <h2 style="color:#fff">¿Esto<br><span class="it" style="color:var(--orange)">te suena?</span></h2>
    <div class="txt" style="margin-top:44px">Cuatro señales de que tu web quedó atrás.</div>
  </div>
</div>""")

# 02 — señal 01
H.append("""
<div class="h papel" id="w2">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">Señal 01</div>
  <div class="cuerpo" style="top:560px">
    <div class="eyebrow">Señal 01</div>
    <h2 style="margin-top:26px;font-size:96px">Se ve<br>desactualizada.</h2>
    <div class="txt" style="margin-top:38px">
      Si parece de hace diez años, tu cliente asume que tu negocio también.
    </div>
  </div>
  <div class="frame lift-soft" style="left:96px;right:96px;bottom:330px;height:400px">
    <div class="bar"><i></i><i></i><i></i><span>tuestudio.com</span></div>
    <div style="overflow:hidden;height:100%">@MOCK@</div>
  </div>
</div>""".replace("@MOCK@", OLD))

# 03 — señal 02
H.append("""
<div class="h tinta" id="w3">
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Señal 02</div>
  <div class="cuerpo" style="top:560px">
    <div class="eyebrow">Señal 02</div>
    <h2 style="margin-top:26px;color:#fff;font-size:96px">En el teléfono<br>se ve mal.</h2>
    <div class="txt" style="margin-top:38px;max-width:520px">
      Si tienen que hacer zoom para leerte, ya se fueron.
    </div>
  </div>
  <div class="phone lift-soft" style="right:120px;bottom:300px;width:330px;height:620px">
    <div class="notch"></div>
    <div style="overflow:hidden;height:100%">@MOCK@</div>
  </div>
  <div class="tag" style="left:466px;bottom:392px">Se sale de la pantalla</div>
</div>""".replace("@MOCK@", OLD_MOVIL))

# 04 — señal 03
H.append("""
<div class="h papel" id="w4">
  <div class="marca"><img src="assets/logo-dark.png" alt=""></div>
  <div class="rot">Señal 03</div>
  <div class="cuerpo" style="top:560px">
    <div class="eyebrow">Señal 03</div>
    <h2 style="margin-top:26px;font-size:96px">No queda claro<br>qué haces.</h2>
  </div>
  <div style="position:absolute;left:96px;right:96px;top:940px;z-index:6">
    <div class="preg">¿Qué haces?</div>
    <div class="preg">¿Para quién?</div>
    <div class="preg">¿Por qué debería elegirte?</div>
    <div class="preg">¿Cómo te contacto?</div>
  </div>
  <div class="txt" style="position:absolute;left:96px;right:96px;bottom:330px;z-index:6">
    Nadie se queda a averiguarlo.
  </div>
</div>""")

# 05 — señal 04
H.append("""
<div class="h tinta" id="w5">
  <img class="bg" src="fotos_hi/px-14721776.jpg"
       style="object-position:50% 42%;filter:grayscale(1) brightness(.58) contrast(1.14)">
  <div class="velo"></div>
  <div class="marca"><img src="assets/logo.png" alt=""></div>
  <div class="rot">Señal 04</div>
  <div class="cuerpo" style="bottom:480px">
    <div class="eyebrow">Señal 04</div>
    <h2 style="margin-top:26px;color:#fff;font-size:92px">No representa<br>el nivel de tu<br>negocio.</h2>
    <div class="txt" style="margin-top:40px">
      Tu negocio creció.<br>
      <span class="it" style="font-family:var(--f-display);font-size:54px;color:var(--orange)">Tu web quedó atrás.</span>
    </div>
  </div>
</div>""")

# 06 — el remate y el llamado
H.append("""
<div class="h naranja" id="w6">
  <div class="marca"><img src="assets/logo-white.png" alt=""></div>
  <div class="rot">El remate</div>
  <div class="cuerpo" style="top:50%;transform:translateY(-52%)">
    <h2 style="font-size:96px">No necesitas<br>más marketing.</h2>
    <div class="txt" style="margin-top:44px">
      Necesitas que tu web trabaje para tu negocio.
    </div>
    <div class="it" style="margin-top:64px;font-family:var(--f-display);font-size:56px;
         letter-spacing:-.02em;color:var(--ink);display:inline-block;
         border-bottom:3px solid var(--ink);padding-bottom:14px">
      Escríbenos por DM →
    </div>
  </div>
</div>""")

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="renueva-fonts.css"><style>' + base + CSS +
       '</style></head><body>' + "".join(H) + '</body></html>')
HERE.joinpath("historias-tuweb.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS" / "tu-web"
OUT.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000})
    pg.goto(HERE.joinpath("historias-tuweb.html").resolve().as_uri())
    pg.wait_for_timeout(2400)
    fuera = pg.evaluate("""() => { const o=[];
      document.querySelectorAll('.h').forEach(h=>{ const hb=h.getBoundingClientRect();
        h.querySelectorAll('h2,.txt,.eyebrow,.marca,.rot,.it,.preg,.frame,.phone,.tag').forEach(el=>{
          const b=el.getBoundingClientRect(), t=b.top-hb.top, bo=b.bottom-hb.top;
          if(t<260||bo>1660) o.push(h.id+' '+(el.className||el.tagName)+' '+Math.round(t)+'-'+Math.round(bo)); }); });
      return o; }""")
    print("fuera de zona segura:", fuera if fuera else "nada")
    for i in range(1, 7):
        guardar(pg.query_selector("#w%d" % i), OUT / ("tu-web-%02d.png" % i))
    b.close()
print("6 historias en DESTACADOS/tu-web/")
