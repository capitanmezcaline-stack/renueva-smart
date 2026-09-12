import pathlib, urllib.request, sys

IDS = """5673490 7781900 36207471 7876197 30375847 35058546 34410146 36356065 7654131
17976144 39224683 8386437 17729218 3892808 6903157 6077665 9367109 8112115
7800666 35188667 6129152 9545914 30948318 8460095 31071253 6201497 8260620 6446313
8092431 6502305 4300078
10225663 5648383 13929418 4910129 1552636 4047875 30747682 29249664 11594551
38341926 32330792
5371683 946310 29012619 18285958 28102352""".split()

W = int(sys.argv[1]) if len(sys.argv) > 1 else 1400
OUT = pathlib.Path(__file__).parent / ("fotos" if W <= 1500 else "fotos_hi")
OUT.mkdir(exist_ok=True)

for i in IDS:
    dst = OUT / ("px-%s.jpg" % i)
    if dst.exists():
        continue
    url = "https://images.pexels.com/photos/%s/pexels-photo-%s.jpeg?auto=compress&cs=tinysrgb&w=%d" % (i, i, W)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        dst.write_bytes(urllib.request.urlopen(req, timeout=30).read())
        print("ok", i)
    except Exception as e:
        print("ERR", i, e)
