import sys, re, json, pathlib, base64

HERE = pathlib.Path(__file__).parent
src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])

html = src.read_text(encoding="utf-8")
fonts = (HERE / "renueva-fonts.css").read_text(encoding="utf-8")

html = html.replace(
    '<link rel="stylesheet" href="renueva-fonts.css">',
    '<style id="embedded-fonts">\n' + fonts + '\n</style>')

for rel in set(re.findall(r'src="((?:assets|fotos_hi)/[^"]+)"', html)):
    p = HERE / rel
    mime = "image/png" if rel.endswith(".png") else "image/jpeg"
    uri = "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())
    html = html.replace('src="%s"' % rel, 'src="%s"' % uri)

dst.write_text(html, encoding="utf-8")
print(dst, round(dst.stat().st_size / 1024 / 1024, 2), "MB")
