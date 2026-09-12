import re, pathlib, base64
from PIL import Image

HERE = pathlib.Path(__file__).parent

# ---------- 1. logo version tinta (el original es blanco + naranja) ----------
im = Image.open(HERE / "assets/logo.png").convert("RGBA")
px = im.load()
INK = (11, 12, 14)
for y in range(im.height):
    for x in range(im.width):
        r, g, b, a = px[x, y]
        if a == 0:
            continue
        # naranja: r alto, g medio/bajo, b bajo  -> se mantiene
        if r > 150 and b < 120 and (r - b) > 70:
            continue
        px[x, y] = (INK[0], INK[1], INK[2], a)
im.save(HERE / "assets/logo-dark.png")
print("logo-dark.png", im.size)

# ---------- 2. subset de fuentes ----------
WANT = {
    ("Archivo", "700", "normal"), ("Archivo", "800", "normal"),
    ("Inter", "400", "normal"), ("Inter", "500", "normal"),
    ("Inter", "600", "normal"), ("Inter", "700", "normal"),
    ("JetBrains Mono", "500", "normal"), ("JetBrains Mono", "600", "normal"),
}
seen, out = set(), []
for f in ["fonts-a.css"]:
    s = (HERE / f).read_text(encoding="utf-8")
    for m in re.finditer(r"@font-face\s*\{.*?\}", s, re.S):
        blk = m.group(0)
        fam = re.search(r"font-family:\s*'([^']+)'", blk)
        w = re.search(r"font-weight:\s*([^;]+)", blk)
        st = re.search(r"font-style:\s*([^;]+)", blk)
        key = (fam.group(1) if fam else "?",
               (w.group(1).strip() if w else "400"),
               (st.group(1).strip() if st else "normal"))
        if key in WANT and key not in seen:
            seen.add(key)
            out.append(blk)
(HERE / "renueva-fonts.css").write_text("\n".join(out), encoding="utf-8")
print("fuentes:", sorted(seen))
print("css KB:", (HERE / "renueva-fonts.css").stat().st_size // 1024)

# ---------- 3. imagenes a base64 ----------
imgs = {}
for name in ["logo-dark.png", "logo.png", "resena-antes-poster.jpg", "resena-despues-poster.jpg"]:
    p = HERE / "assets" / name
    mime = "image/png" if name.endswith(".png") else "image/jpeg"
    imgs[name] = "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())
import json
(HERE / "img.json").write_text(json.dumps(imgs), encoding="utf-8")
print("img.json listo")
