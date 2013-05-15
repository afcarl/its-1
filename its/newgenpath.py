
import sys
import numpy as np
import csv
import config
from completepath import complete_path
class Path:
    def __init__(self, car, stime, sgrid):
        self.car = car
        self.stime = stime
        self.etime = stime
        self.sgrid = sgrid
        self.egrid = sgrid
        self.passways = [] 

    def tolist (self):
        inters = []
        for p in self.passways:
            if p > 10000:
                continue
            if len(inters) == 0:
                inters.append (p)
            elif inters[-1] == p:
                continue
            else:
                inters.append (p)

        return [self.car, self.stime, str_grid(self.sgrid), self.etime, \
                str_grid(self.egrid)] + [str (p) for p in inters]



def delta_time (a, b):
    ta = int (a[0:2]) * 60 + int(a[2:4])
    tb = int (a[0:2]) * 60 + int(a[2:4])
    if ta < tb:
        ta += 24 * 60 * 60
    return ta - tb


def str_grid (grid):
    return str(grid[0]).zfill(3) + str(grid[1]).zfill(3)


def genpath (gmap, topo):
    paths = {}
    # read cdata
    reader = csv.reader (sys.stdin)
    writer = csv.writer (sys.stdout)
    for row in reader:
        if len (row) != 13:
            continue
        grid = config.gridid (int(row[6]), int(row[7]))
        # beyond research area
        if grid == (0, 0):
            continue

        car = row[2]
        passway = gmap [grid]
        time = row[3][8:12]

        # car is serving
        if row[10] == '1':
            if car not in paths:
                paths[car] = Path (car, time, grid)
            elif delta_time (time, paths[car].etime) > config.MAXINTER:
                writer.writerow (paths[car].tolist ())
                paths[car] = Path (car, time, grid)
            if passway == 0:
                continue
            pws = paths[car].passways
            if len (pws) == 0:
                pws.append (passway)
            elif passway == pws[-1]:
                continue
            elif pws[-1] in topo and passway in topo[pws[-1]]:
                pws.append (passway)
            else:
                inter = complete_path (pws[-1], passway, topo)
                if inter == []:
                    writer.writerow (paths[car].tolist())
                    paths[car] = Path (car, time, grid)
                else:
                    pws.extend (inter)
                    pws.append (passway)

        elif car in paths:
            if delta_time (time, paths[car].etime) <= config.MAXINTER:
                paths[car].etime = time
                paths[car].egrid = grid
            writer.writerow (paths[car].tolist ())
            del paths[car]

if __name__ == '__main__':
    gmap = np.genfromtxt (sys.argv[1], dtype = np.int32)
    topo = {}
    topofile = open (sys.argv[2])
    reader = csv.reader (topofile)
    for row in reader:
        row = [int(p) for p in row]
        for p in row:
            s = set (row)
            if p not in topo:
                topo[p] = set()
            topo[p] |= s
    genpath (gmap, topo)

