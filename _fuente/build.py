"""Deja un HTML autocontenido: fuentes e imágenes embebidas en base64.

    python build.py posts/p01.src.html ../POSTS/01/post.html

Las rutas de dentro del HTML se resuelven **respecto del archivo fuente**, no de
este script, para que funcione igual con las piezas de _fuente/ y con los posteos
que viven en posts/ y referencian con "../".
"""
import base64
import mimetypes
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
src = pathlib.Path(sys.argv[1]).resolve()
dst = pathlib.Path(sys.argv[2])

html = src.read_text(encoding="utf-8")
fuentes = (HERE / "renueva-fonts.css").read_text(encoding="utf-8")

# el <link> puede apuntar con o sin "../" segun donde viva el fuente
html = re.sub(r'<link rel="stylesheet" href="[^"]*renueva-fonts\.css">',
              '<style id="embedded-fonts">\n' + fuentes + '\n</style>', html)

faltan = []
for rel in sorted(set(re.findall(r'src="((?:\.\./)*(?:assets|fotos_hi)/[^"]+)"', html))):
    archivo = (src.parent / rel).resolve()
    if not archivo.exists():
        faltan.append(rel)
        continue
    mime = mimetypes.guess_type(archivo.name)[0] or "application/octet-stream"
    uri = "data:%s;base64,%s" % (mime, base64.b64encode(archivo.read_bytes()).decode())
    html = html.replace('src="%s"' % rel, 'src="%s"' % uri)

dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_text(html, encoding="utf-8")

peso = dst.stat().st_size / 1024 / 1024
print("%s  %.2f MB" % (dst, peso))
if faltan:
    print("  OJO, no se encontraron:", ", ".join(faltan))
if peso < 1:
    print("  OJO: pesa menos de 1 MB, probablemente no se embebio nada")
