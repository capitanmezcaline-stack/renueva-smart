import sys, pathlib
from playwright.sync_api import sync_playwright

SRC = pathlib.Path(sys.argv[1]).resolve()
OUT = pathlib.Path(sys.argv[2]).resolve()
IDS = sys.argv[3].split(",")
SCALE = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
OUT.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 1400}, device_scale_factor=SCALE)
    pg.goto(SRC.as_uri())
    pg.wait_for_timeout(1800)
    for i in IDS:
        el = pg.query_selector("#" + i)
        el.screenshot(path=str(OUT / (i + ".png")))
        print("ok", i)
    b.close()
