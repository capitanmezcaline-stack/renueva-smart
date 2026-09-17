"""Renderiza los paneles del case study de Behance.

    python render_behance.py p01-cover.html
    python render_behance.py            # todos los que haya en la carpeta

A diferencia de render.py (carruseles, 1080x1350 fijo), acá cada panel mide
1920 de ancho y la altura que necesite — la mide en el DOM antes de capturar.
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent.parent / "BEHANCE"
OUT.mkdir(parents=True, exist_ok=True)

# el panel 05 usa la grilla del feed sin la franja de titulo que trae FEED.jpg
feed = HERE.parent.parent / "PLAN-CONTENIDO" / "FEED.jpg"
if feed.exists():
    from PIL import Image
    im = Image.open(feed)
    im.crop((0, 56, im.width, im.height)).save(HERE / "_feed-crop.jpg", quality=93)

archivos = (
    [HERE / sys.argv[1]] if len(sys.argv) > 1
    else sorted(HERE.glob("p[0-9][0-9]-*.html"))
)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1.5)
    for f in archivos:
        pg.goto(f.resolve().as_uri())
        pg.wait_for_timeout(600)
        alto = pg.eval_on_selector(".panel", "el => el.offsetHeight")
        pg.set_viewport_size({"width": 1920, "height": alto})
        pg.wait_for_timeout(200)
        destino = OUT / (f.stem[1:] + ".jpg")   # "p01-cover" -> "01-cover.jpg"
        pg.locator(".panel").screenshot(path=str(destino), type="jpeg", quality=92)
        print("ok", destino.name, "· %dpx alto" % alto)
    b.close()
