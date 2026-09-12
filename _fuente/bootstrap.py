"""Deja el proyecto listo para renderizar, desde un clon limpio.

El repo no versiona las fotos (58 MB) ni las capturas del caso a tamaño original,
porque se pueden volver a bajar. Esto las trae.

    python bootstrap.py

Es idempotente: lo que ya existe no se vuelve a bajar.
"""
import pathlib
import re
import subprocess
import sys
import urllib.request

HERE = pathlib.Path(__file__).parent
FOTOS = HERE / "fotos_hi"
UA = {"User-Agent": "Mozilla/5.0"}


def fuentes():
    css = HERE / "renueva-fonts.css"
    if css.exists() and css.stat().st_size > 100_000:
        print("  fuentes: ya están (%d KB)" % (css.stat().st_size // 1024))
        return
    print("  fuentes: bajando de Google...")
    subprocess.run([sys.executable, str(HERE / "fetch_fonts.py")], check=True)


def fotos_usadas():
    """Las fotos que realmente referencian las piezas, no una lista fija."""
    ids = set()
    for f in list(HERE.glob("*.py")) + list(HERE.glob("*.html")):
        if f.name.startswith(("_", "bootstrap")):
            continue
        ids |= set(re.findall(r"px-(\d+)\.jpg", f.read_text(encoding="utf-8", errors="ignore")))
    return sorted(ids)


def fotos():
    FOTOS.mkdir(exist_ok=True)
    ids = fotos_usadas()
    faltan = [i for i in ids if not (FOTOS / ("px-%s.jpg" % i)).exists()]
    print("  fotos: %d referenciadas, %d por bajar" % (len(ids), len(faltan)))
    for i in faltan:
        url = ("https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg"
               "?auto=compress&cs=tinysrgb&w=2400" % (i, i))
        try:
            datos = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
            (FOTOS / ("px-%s.jpg" % i)).write_bytes(datos)
            print("    ok px-%s" % i)
        except Exception as e:
            print("    ERROR px-%s  %s" % (i, e))


def caso():
    """Capturas propias de los dos sitios reales del caso Acosta Pastore."""
    necesarias = ["caso-antes-desktop.jpg", "caso-despues-desktop.jpg",
                  "caso-antes-movil.jpg", "caso-despues-movil.jpg"]
    assets = HERE / "assets"
    if all((assets / n).exists() for n in necesarias):
        print("  caso: las capturas ya están")
        return
    print("  caso: capturando los dos sitios en vivo...")
    subprocess.run([sys.executable, str(HERE / "capturar_caso.py")], check=True)

    from PIL import Image
    for nombre, ancho in [("caso-antes-desktop", 1720), ("caso-despues-desktop", 1720),
                          ("caso-antes-movil", 620), ("caso-despues-movil", 620)]:
        src = assets / (nombre + ".png")
        if not src.exists():
            continue
        im = Image.open(src).convert("RGB")
        im = im.resize((ancho, int(im.height * ancho / im.width)), Image.LANCZOS)
        im.save(assets / (nombre + ".jpg"), quality=88, optimize=True)
    print("  caso: capturas optimizadas a .jpg")


print("Preparando el proyecto...\n")
fuentes()
fotos()
caso()
print("\nListo. Probá con:")
print("  python render.py post-1.src.html ../FIJADO-1/_render s01 1.0")
