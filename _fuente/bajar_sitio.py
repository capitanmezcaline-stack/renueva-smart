"""Baja renuevasmart.com y deja el texto plano en _sitio.txt.

El copy de las piezas sale de ahí. Las preguntas frecuentes están plegadas en la
página, pero sí vienen en el HTML, así que este volcado las incluye.
"""
import html
import pathlib
import re
import urllib.request

HERE = pathlib.Path(__file__).parent
URL = "https://renuevasmart.com/"

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
doc = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "ignore")
HERE.joinpath("_sitio.html").write_text(doc, encoding="utf-8")

txt = re.sub(r"<script.*?</script>|<style.*?</style>", " ", doc, flags=re.S)
txt = html.unescape(re.sub(r"<[^>]+>", "\n", txt))
lineas = [l.strip() for l in txt.split("\n") if l.strip()]
HERE.joinpath("_sitio.txt").write_text("\n".join(lineas), encoding="utf-8")

print("_sitio.txt  ·  %d líneas de texto" % len(lineas))
print("\nSecciones para ubicarte:")
for i, l in enumerate(lineas):
    if l in ("Sin letra chica", "Preguntas", "Precios", "Sectores",
             "Cómo trabajamos", "Reseñas", "Qué hacemos"):
        print("  línea %-4d %s" % (i + 1, l))
