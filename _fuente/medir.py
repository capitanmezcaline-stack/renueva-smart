"""Busca el cuerpo maximo que entra en el ancho util para cada linea de titular."""
import pathlib, json
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
ANCHO = 1080 - 112 * 2          # margen seguro a ambos lados

# (etiqueta, texto, peso, estilo, familia)
LINEAS = [
    ("s01 portada L1", "Tu web dice", 700, "normal", "display"),
    ("s01 portada L2", "otra cosa.", 700, "italic", "display"),
    ("s02 L2", "primera impresión.", 700, "normal", "display"),
    ("s03 una linea", "Se ve desactualizada.", 700, "normal", "display"),
    ("s03 dos lineas", "desactualizada.", 700, "normal", "display"),
    ("s04 L1", "En el celular", 700, "normal", "display"),
    ("s05 L1", "No queda claro", 700, "normal", "display"),
    ("s06 L2", "el nivel de tu negocio.", 700, "normal", "display"),
    ("s07 L1", "¿Y si tu web estuviera", 700, "normal", "display"),
    ("s07 alt L1", "¿Y si tu web", 700, "normal", "display"),
    ("s07 alt L2", "estuviera a la altura", 700, "italic", "display"),
    ("s09 L2", "para que tu negocio", 700, "normal", "display"),
    ("s10 L1", "¿Tu web necesita", 700, "normal", "display"),
    ("pregunta larga", "¿Por qué debería elegirte?", 600, "normal", "display"),
    ("item largo", "Experiencia móvil", 700, "normal", "display"),
    ("cuerpo s03", "Si parece de hace diez años, tu cliente asume", 400, "normal", "body"),
]

HTML = """<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="renueva-fonts.css">
<style>
body{margin:0}
#m{position:absolute;white-space:nowrap;visibility:hidden;
   font-optical-sizing:auto;letter-spacing:-.018em}
.display{font-family:'Fraunces',serif}
.body{font-family:'Plus Jakarta Sans',sans-serif;letter-spacing:-.008em}
</style><span id="m"></span>"""

(HERE / "_medir.html").write_text(HTML, encoding="utf-8")

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto((HERE / "_medir.html").as_uri())
    pg.wait_for_timeout(1500)

    print("ancho util: %d px\n" % ANCHO)
    print("%-18s %-46s %s" % ("linea", "texto", "cuerpo maximo"))
    print("-" * 82)
    for etiqueta, texto, peso, estilo, fam in LINEAS:
        bajo, alto = 20, 320
        while alto - bajo > 1:
            medio = (bajo + alto) // 2
            ancho = pg.evaluate(
                """([t,w,s,f,size]) => {
                    const m = document.getElementById('m');
                    m.className = f; m.textContent = t;
                    m.style.fontWeight = w; m.style.fontStyle = s;
                    m.style.fontSize = size + 'px';
                    return m.getBoundingClientRect().width;
                }""", [texto, peso, estilo, fam, medio])
            if ancho <= ANCHO:
                bajo = medio
            else:
                alto = medio
        print("%-18s %-46s %d px" % (etiqueta, texto[:44], bajo))
    b.close()
