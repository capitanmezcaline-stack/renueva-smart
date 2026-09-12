"""Arma "PARA SUBIR/" y el ZIP de entrega a partir de las piezas ya exportadas.

    python empaquetar.py

Renombra todo a nombres que se entiendan sin conocer el sistema —slide-01,
historia-03, "TEXTO DEL POST.txt"— porque la carpeta la abre alguien que va a
subir a Instagram desde el telefono, no a leer el repo.

Esto se hacia a mano y quedaba viejo al dia siguiente de tocar una pieza.
"""
import pathlib
import shutil
import time
import zipfile

HERE = pathlib.Path(__file__).parent
RAIZ = HERE.parent
DEST = RAIZ / "PARA SUBIR"
ZIP = RAIZ / "RENUEVA SMART - piezas para publicar.zip"

FIJADOS = [
    (1, "FIJADO 1 - Tu web necesita una renovacion"),
    (2, "FIJADO 2 - Que hacemos"),
    (3, "FIJADO 3 - Asi transformamos una web"),
]

# carpeta del repo -> nombre que ve quien publica
POSTEOS = [
    ("01-tres-senales",   "01 - Tres senales de una web vieja"),
    ("02-web-roast-01",   "02 - Web Roast 01"),
    ("03-cinco-errores",  "03 - Cinco errores de diseno web"),
    ("04-parece-de-2015", "04 - Tu web parece de 2015"),
    ("05-presentacion",   "05 - Presentacion de Renueva Smart"),
]

# el orden es el del embudo, no alfabetico: ver DESTACADOS/LEEME.md
DESTACADOS = [
    ("tu-web",    "1 - Tu web"),
    ("servicios", "2 - Servicios"),
    ("proceso",   "3 - Proceso"),
    ("el-caso",   "4 - El caso"),
    ("precios",   "5 - Precios"),
    ("preguntas", "6 - Preguntas"),
    ("gratis",    "7 - Gratis"),
]


def copiar(origen, destino):
    """OneDrive a veces tiene el archivo tomado; reintentar."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    for _ in range(12):
        try:
            shutil.copy(origen, destino)
            return
        except OSError:
            time.sleep(1.5)
    raise SystemExit("no se pudo escribir " + str(destino))


def vaciar(carpeta):
    for _ in range(12):
        try:
            shutil.rmtree(carpeta, ignore_errors=False)
            return
        except FileNotFoundError:
            return
        except OSError:
            time.sleep(1.5)
    raise SystemExit("no se pudo vaciar " + str(carpeta))


vaciar(DEST)
n = 0

for k, nombre in FIJADOS:
    src = RAIZ / ("FIJADO-%d" % k)
    caras = sorted(src.glob("RS-F%d-*.png" % k))
    if not caras:
        raise SystemExit("faltan las piezas del Fijado %d: corre render.py" % k)
    for i, p in enumerate(caras, 1):
        copiar(p, DEST / "CARRUSELES FIJADOS" / nombre / ("slide-%02d.png" % i))
        n += 1
    copiar(src / "CAPTION.txt",
           DEST / "CARRUSELES FIJADOS" / nombre / "TEXTO DEL POST.txt")

producidos = set()
for carpeta, nombre in POSTEOS:
    src = RAIZ / "POSTS" / carpeta
    caras = sorted(src.glob("slide-*.png"))
    if not caras:
        raise SystemExit("faltan las piezas de %s: corre render.py" % carpeta)
    for p in caras:
        copiar(p, DEST / "POSTEOS DEL PLAN" / nombre / p.name)
        n += 1
    copiar(src / "CAPTION.txt",
           DEST / "POSTEOS DEL PLAN" / nombre / "TEXTO DEL POST.txt")
    producidos.add(int(carpeta[:2]))

for slug, nombre in DESTACADOS:
    caras = sorted((RAIZ / "DESTACADOS" / slug).glob("%s-*.png" % slug))
    if not caras:
        raise SystemExit("faltan las historias de %s" % slug)
    for i, p in enumerate(caras, 1):
        copiar(p, DEST / "DESTACADOS" / nombre / ("historia-%02d.png" % i))
        n += 1
    tapa = RAIZ / "DESTACADOS" / "tapas" / ("tapa-%s-%s.png" % (nombre[0], slug))
    copiar(tapa, DEST / "DESTACADOS" / nombre / "TAPA (la foto del circulo).png")
    n += 1

# Solo las portadas de lo que TODAVIA no esta producido. Dejar tambien las de
# los posteos ya armados invita a subir la portada sola en vez del carrusel.
pendientes = 0
for p in sorted((RAIZ / "PLAN-CONTENIDO" / "portadas").glob("post-*.png")):
    if int(p.stem[-2:]) in producidos:
        continue
    copiar(p, DEST / "PORTADAS DE LO QUE FALTA" / p.name)
    pendientes += 1
    n += 1

copiar(HERE / "leeme-para-subir.txt", DEST / "LEEME PRIMERO.txt")
copiar(RAIZ / "PLAN-CONTENIDO" / "FEED.jpg", DEST / "COMO VA A QUEDAR EL FEED.jpg")
n += 2

for _ in range(12):
    try:
        if ZIP.exists():
            ZIP.unlink()
        break
    except OSError:
        time.sleep(1.5)

with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in sorted(DEST.rglob("*")):
        if p.is_file():
            z.write(p, p.relative_to(DEST.parent))

print("PARA SUBIR/  ·  %d archivos  ·  %d portadas pendientes (posteos %s)"
      % (n, pendientes, "06-19"))
print("%s  ·  %.1f MB" % (ZIP.name, ZIP.stat().st_size / 1e6))
