"""
some config about grid
"""
# dj * 100 / dx = 0.0011718
# dw * 100 / dy = 0.0008984

# min latitude and gratitue
# data beyond this range will be ignored
MINX = 116.23
MINY = 39.78
# number of grid x and y
NX = 512
NY = 512
# delta latitue and gratitude 
DELTAX = 0.0005859#0.0011#0.00055
DELTAY = 0.0004992#0.0009#0.00045
MAXX = MINX + NX * DELTAX
MAXY = MINY + NY * DELTAY
rate = 1.0 / 1024 / 3600
BLANK = 0
IGNORE = 1
TURN = 2
OTHER = 4

MAXINTER = 300

def gridid (x, y):
    x = x * rate
    y = y * rate
    if not (MINX <= x < MAXX) or not (MINY <= y < MAXY):
        return (0, 0)
    ix = int ((x - MINX) / DELTAX)
    iy = int ((y - MINY) / DELTAY)
    return (ix, iy)
