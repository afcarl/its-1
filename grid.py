import sys
import csv
import numpy
from config import *

def gridid (x, y):
    if not (MINX <= x < MAXX) or not (MINY <= y < MAXY):
        return None
    ix = int ((x - MINX) // DELTAX)
    iy = int ((y - MINY) // DELTAY)
    return (ix, iy)

def test ():
    print (gridid (116.30, 39.99))
    print (gridid (0, 0))

def gridcdata ():
    grids = numpy.zeros ((NX, NY))
    reader = csv.reader (sys.stdin)
    total = 0
    check = 0
    for row in reader:
        if len (row) < 9:
            continue
        v = int (row[8])
        if v == 0:
            continue
        total += 1
        gid = gridid (float (row[4]), float (row[5]))
        if gid:
            check += 1
            x, y = gid
            grids[x][y] += 1
    print (check, total, check / total)
    numpy.savetxt ('gridcdata.txt', grids)
    """
    writer = csv.writer (sys.stdout)
    for row in grids:
        writer.writerow (row)
    """

gridcdata ()
