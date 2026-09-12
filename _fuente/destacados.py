"""Tapas de destacados de Instagram, en dos estilos, y simulacion del perfil."""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent

# (palabra en la tapa, nombre debajo del circulo)
DEST = [
    ("¿Tu web?",  "¿Tu web?"),
    ("Servicios", "Servicios"),
    ("Proceso",   "Proceso"),
    ("El caso",   "El caso"),
    ("Precios",   "Precios"),
    ("Preguntas", "Preguntas"),
    ("Gratis",    "Gratis"),
]

base = HERE.joinpath("post-1.src.html").read_text(encoding="utf-8").split("<style>")[1].split("</style>")[0]

CSS = """
.hist{width:1080px;height:1920px;position:relative;overflow:hidden;
      display:flex;align-items:center;justify-content:center}
.hist.tinta{background:var(--ink)}
.hist.naranja{background:var(--orange)}
.hist.papel{background:var(--paper)}
/* el perfil recorta la tapa a un circulo centrado: todo vive acá adentro */
.circulo{width:700px;height:700px;border-radius:50%;display:flex;flex-direction:column;
         align-items:center;justify-content:center;text-align:center;padding:0 40px}
.palabra{font-family:var(--f-display);font-weight:700;font-size:96px;line-height:1.04;
         letter-spacing:-.02em;font-optical-sizing:auto;white-space:nowrap}
.marca{width:92px;height:4px;margin-bottom:38px}
.guia{position:absolute;width:700px;height:700px;border-radius:50%;
      border:2px dashed rgba(255,0,90,.0)}
"""

def tapa(i, palabra, estilo):
    if estilo == "A":                       # todas en tinta, la ultima en naranja
        if i == len(DEST) - 1:
            fondo, color, raya = "naranja", "#fff", "var(--ink)"
        else:
            fondo, color, raya = "tinta", "var(--paper)", "var(--orange)"
    elif estilo == "C":                     # todas en papel, la ultima en naranja
        if i == len(DEST) - 1:
            fondo, color, raya = "naranja", "#fff", "var(--ink)"
        else:
            fondo, color, raya = "papel", "var(--ink)", "var(--orange)"
    else:                                   # alternadas
        # "Gratis" es la oferta: va en naranja aunque le toque otro color
        ciclo = ["tinta", "naranja", "papel"]
        fondo = "naranja" if i == len(DEST) - 1 else ciclo[i % 3]
        color = {"tinta": "var(--paper)", "naranja": "#fff", "papel": "var(--ink)"}[fondo]
        raya = {"tinta": "var(--orange)", "naranja": "var(--ink)", "papel": "var(--orange)"}[fondo]
    return ('<div class="hist %s" id="%s%d"><div class="circulo">'
            '<span class="marca" style="background:%s"></span>'
            '<span class="palabra" style="color:%s">%s</span>'
            '</div><div class="guia"></div></div>') % (fondo, estilo, i, raya, color, palabra)

AJUSTE = """
<script>
document.fonts.ready.then(() => {
  document.querySelectorAll('.palabra').forEach(p => {
    let px = 132; p.style.fontSize = px + 'px';
    while (px > 30 && p.getBoundingClientRect().width > 606) { px -= 2; p.style.fontSize = px + 'px'; }
  });
  document.documentElement.setAttribute('data-listo','1');
});
</script>
"""

cuerpo = "".join(tapa(i, d[0], e) for e in ("B",) for i, d in enumerate(DEST))
doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">'
       '<link rel="stylesheet" href="renueva-fonts.css"><style>' + base + CSS +
       '</style></head><body>' + cuerpo + AJUSTE + '</body></html>')
HERE.joinpath("destacados.html").write_text(doc, encoding="utf-8")

OUT = HERE.parent / "DESTACADOS"
(OUT / "tapas").mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 2000})
    pg.goto(HERE.joinpath("destacados.html").resolve().as_uri())
    pg.wait_for_selector('html[data-listo="1"]', timeout=30000)
    pg.wait_for_timeout(800)
    for e in ("B",):
        for i, d in enumerate(DEST):
            nombre = d[1].replace("¿","").replace("?","").strip().lower().replace(" ","-")
            pg.query_selector("#%s%d" % (e, i)).screenshot(
                path=str(OUT / "tapas" / ("tapa-%d-%s.png" % (i + 1, nombre))))
    b.close()
print("tapas generadas en DESTACADOS/tapas/")
