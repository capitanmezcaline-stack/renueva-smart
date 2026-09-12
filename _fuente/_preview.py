"""Arma la tira de revision de un destacado, con las bandas que tapa Instagram."""
import sys, glob, pathlib
from PIL import Image, ImageDraw

carpeta, titulo = sys.argv[1], sys.argv[2]
fs = sorted(glob.glob("../DESTACADOS/%s/*.png" % carpeta))
W = 222; H = int(W * 1920 / 1080); GAP = 12; HEAD = 26
cv = Image.new("RGB", (len(fs) * (W + GAP) + 20, H + HEAD + 16), "#232326")
d = ImageDraw.Draw(cv)
d.text((10, 7), titulo, fill="#cfcfd4")
for i, f in enumerate(fs):
    im = Image.open(f).convert("RGB").resize((W, H), Image.LANCZOS)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    od.rectangle([0, 0, W, int(260 * H / 1920)], fill=(255, 40, 80, 55))
    od.rectangle([0, int(1660 * H / 1920), W, H], fill=(255, 40, 80, 55))
    cv.paste(Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB"), (10 + i * (W + GAP), HEAD))
dst = "../_direcciones/HIST-%s.jpg" % carpeta.upper()
cv.save(dst, quality=93)
print(dst, cv.size)
