#! /usr/bin/python

import sys
import csv
import numpy as np

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

def gridid (x, y):
    if not (MINX <= x < MAXX) or not (MINY <= y < MAXY):
        return None
    ix = int ((x - MINX) // DELTAX)
    iy = int ((y - MINY) // DELTAY)
    return (ix, iy)

def gridcdata ():
    grids = np.zeros ((NX, NY), dtype = np.int32)
    reader = csv.reader (sys.stdin)
    for row in reader:
        if len (row) < 9:
            continue
        v = int (row[8])
        if v == 0:
            continue
        gid = gridid (float (row[4]), float (row[5]))
        if gid:
            grids[gid] += 1
    np.savetxt (sys.stdout, grids, fmt = '%d')

if __name__ == '__main__':
    gridcdata ()
