"""Ensambla post-2.src.html a partir del CSS base del Fijado 1 + extras + cuerpo."""
import pathlib

HERE = pathlib.Path(__file__).parent

# el CSS base se toma del Fijado 1 para que los dos fijados no se desincronicen
base = HERE.joinpath("post-1.src.html").read_text(encoding="utf-8").split("<style>")[1].split("</style>")[0]
extra = HERE.joinpath("post-2-extra.css").read_text(encoding="utf-8")
cuerpo = HERE.joinpath("post-2-cuerpo.html").read_text(encoding="utf-8")

FLECHA = ('<svg viewBox="0 0 62 14" fill="none"><path d="M0 7h56M49 1.5l7 5.5-7 5.5" '
          'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
          'stroke-linejoin="round"/></svg>')
cuerpo = cuerpo.replace("FLECHA", FLECHA)

doc = ('<!doctype html><html lang="es"><head><meta charset="utf-8">\n'
       '<title>Renueva Smart — Fijado 2</title>\n'
       '<link rel="stylesheet" href="renueva-fonts.css">\n'
       '<style>' + base + extra + '</style></head><body>\n\n' + cuerpo + '\n</body></html>\n')

HERE.joinpath("post-2.src.html").write_text(doc, encoding="utf-8")
print("post-2.src.html", len(doc) // 1024, "KB")
