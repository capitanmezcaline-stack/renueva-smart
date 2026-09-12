import sys, pathlib
from PIL import Image, ImageDraw

src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
cols = sys.argv[3].split(";")          # "a1,a2;b1,b2;c1,c2"
labels = sys.argv[4].split(";") if len(sys.argv) > 4 else []
W = 430
GAP, PAD, HEAD = 22, 26, 46

grids = [c.split(",") for c in cols]
rows = max(len(g) for g in grids)
ims = [[Image.open(src / (n + ".png")) for n in g] for g in grids]
h = int(ims[0][0].height * (W / ims[0][0].width))

canvas = Image.new("RGB", (PAD*2 + len(grids)*W + (len(grids)-1)*GAP,
                           PAD*2 + HEAD + rows*h + (rows-1)*GAP), "#232326")
d = ImageDraw.Draw(canvas)
for ci, col in enumerate(ims):
    x = PAD + ci*(W+GAP)
    if ci < len(labels):
        d.text((x+4, PAD+10), labels[ci], fill="#FFFFFF")
    for ri, im in enumerate(col):
        canvas.paste(im.convert("RGB").resize((W, h), Image.LANCZOS),
                     (x, PAD+HEAD+ri*(h+GAP)))
canvas.save(out, quality=92)
print(out, canvas.size)
