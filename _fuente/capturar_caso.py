"""Capturas propias del caso Acosta Pastore, en alta, antes y despues."""
import pathlib
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

SITIOS = {
    "antes":   "https://www.escribaniacostapastore.com/",
    "despues": "https://avvedit-creator.github.io/nuevaescribaniacostapastore/",
}

with sync_playwright() as p:
    nav = p.chromium.launch()

    for nombre, url in SITIOS.items():
        # --- escritorio ---
        pg = nav.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        pg.goto(url, wait_until="networkidle", timeout=60000)
        pg.wait_for_timeout(2500)
        pg.screenshot(path=str(OUT / ("caso-%s-desktop.png" % nombre)))
        # tramo largo, para recortes verticales
        pg.set_viewport_size({"width": 1440, "height": 1800})
        pg.wait_for_timeout(1200)
        pg.screenshot(path=str(OUT / ("caso-%s-desktop-largo.png" % nombre)))
        pg.close()

        # --- movil ---
        pg = nav.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=3,
                          is_mobile=True, has_touch=True,
                          user_agent=("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                                      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 "
                                      "Mobile/15E148 Safari/604.1"))
        pg.goto(url, wait_until="networkidle", timeout=60000)
        pg.wait_for_timeout(2500)
        pg.screenshot(path=str(OUT / ("caso-%s-movil.png" % nombre)))
        pg.close()
        print("ok", nombre)

    nav.close()

from PIL import Image
for f in sorted(OUT.glob("caso-*.png")):
    print("%-34s %s" % (f.name, Image.open(f).size))
