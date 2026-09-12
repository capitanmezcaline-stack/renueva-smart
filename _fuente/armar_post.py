"""Ensambla un posteo del plan de contenido.

    python armar_post.py p01

Toma el CSS base del Fijado 1 —para que los posteos no se desincronicen del
sistema— le suma el CSS propio del posteo si existe, y le pega el cuerpo.
Deja posts/<nombre>.src.html listo para render.py y build.py.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
POSTS = HERE / "posts"

if len(sys.argv) < 2:
    disponibles = sorted(p.stem.replace("-cuerpo", "") for p in POSTS.glob("*-cuerpo.html"))
    sys.exit("Falta el nombre del posteo. Disponibles: " + ", ".join(disponibles))

nombre = sys.argv[1]
cuerpo_f = POSTS / (nombre + "-cuerpo.html")
if not cuerpo_f.exists():
    sys.exit("No existe %s" % cuerpo_f)

base = HERE.joinpath("post-1.src.html").read_text(encoding="utf-8").split("<style>")[1].split("</style>")[0]
extra_f = POSTS / (nombre + "-extra.css")
extra = extra_f.read_text(encoding="utf-8") if extra_f.exists() else ""
cuerpo = cuerpo_f.read_text(encoding="utf-8")

FLECHA = ('<svg viewBox="0 0 62 14" fill="none"><path d="M0 7h56M49 1.5l7 5.5-7 5.5" '
          'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
          'stroke-linejoin="round"/></svg>')
cuerpo = cuerpo.replace("FLECHA", FLECHA)

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">\n'
       '<title>Renueva Smart — %s</title>\n'
       '<link rel="stylesheet" href="../renueva-fonts.css">\n'
       '<style>%s%s</style></head><body>\n\n%s\n</body></html>\n' % (nombre, base, extra, cuerpo))

destino = POSTS / (nombre + ".src.html")
destino.write_text(doc, encoding="utf-8")
print("%s  ·  %d KB  ·  %d slides" % (destino.name, len(doc) // 1024, doc.count('class="slide')))
