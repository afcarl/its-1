import sys
import csv
from grid import gridid
import mark

class Path:
    def __init__(self, car, stime, sgrid):
        self.car = car
        self.stime = stime
        self.etime = ''
        self.sgrid = sgrid
        self.egrid = None
        self.passways = [] 
    def tolist (self):
        return [self.car, self.stime, self.sgrid, self.etime, self.egrid] \
            + [str (it) for it in self.passways]

def genpath (gmap):
    paths = {}
    # read cdata
    reader = csv.reader (sys.stdin)
    writer = csv.writer (sys.stdout)
    for row in reader:
        if len (row) != 13:
            continue
        car = row[2]
        grid = gridid (float(row[6]), float(row[7]))
        passway = gmap [grid]
        time = row[3][8:12]
        # car is serving
        if row[10] == '1':
            if car in paths:
                if passway < 10:
                    continue
                pw = paths[car].passways
                if len(pw) == 0 or pw[len(pw)-1] != passway:
                    pw.append (passway)
            else:
                start = str (grid[0]).zfill (3) + str(grid[1]).zfill(3)
                paths[car] = Path (car, time, start)
                paths[car].passways.append (passway)
        else:
            if car in paths:
                paths[car].etime = time
                end = str (grid[0]).zfill (3) + str(grid[1]).zfill(3)
                paths[car].egrid = end
                writer.writerow (paths[car].tolist ())
                del paths[car]

if __name__ == '__main__':
    import numpy as np
    gmap = np.genfromtxt (sys.argv[1], dtype = np.int32)
    genpath (gmap)

