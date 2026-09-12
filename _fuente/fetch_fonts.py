import re, base64, pathlib, urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# exactamente lo que carga renuevasmart.com
CSS_URL = ("https://fonts.googleapis.com/css2?"
           "family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500;1,600"
           "&family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,500;1,9..144,700"
           "&display=swap")

HERE = pathlib.Path(__file__).parent


def get(url):
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40).read()


css = get(CSS_URL).decode("utf-8")

# Google parte cada familia en subsets; nos quedamos solo con latin y latin-ext
bloques = re.findall(r"(/\*\s*([\w-]+)\s*\*/\s*)?(@font-face\s*\{.*?\})", css, re.S)
salida, total = [], 0
for _, subset, blk in bloques:
    if subset not in ("latin", "latin-ext"):
        continue
    m = re.search(r"url\((https://[^)]+\.woff2)\)", blk)
    if not m:
        continue
    datos = get(m.group(1))
    total += len(datos)
    uri = "data:font/woff2;base64," + base64.b64encode(datos).decode()
    salida.append(blk.replace(m.group(1), uri))
    fam = re.search(r"font-family:\s*'([^']+)'", blk).group(1)
    peso = re.search(r"font-weight:\s*([^;]+)", blk).group(1).strip()
    est = re.search(r"font-style:\s*([^;]+)", blk).group(1).strip()
    print("%-20s %-10s %-8s %-10s %5d KB" % (fam, peso, est, subset, len(datos) // 1024))

(HERE / "renueva-fonts.css").write_text("\n".join(salida), encoding="utf-8")
print("\n%d caras · %d KB en total" % (len(salida), total // 1024))
