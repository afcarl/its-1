"""
some config about grid
"""
# min latitude and gratitue
# data beyond this range will be ignored
MINX = 116.22
MINY = 39.80
MAXX = 116.54
MAXY = 40.00

# delta latitue and gratitude 
DELTAX = 0.0011#0.00055
DELTAY = 0.0009#0.00045

# number of grid x and y
NX = int ((MAXX - MINX) / DELTAX + 1)
NY = int ((MAXY - MINY) / DELTAY + 1)
