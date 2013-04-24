import sys
import csv
from its.gridmap.grid import gridid

class Path:
    def __init__(self, car, stime, sgrid):
        self.car = car
        self.stime = stime
        self.etime = ''
        self.sgrid = sgrid
        self.egrid = None
        self.passways = [] 
    def tolist ():
        return [self.car, str(self.sgrid[0]), str(self.sgrid[1]), self.stime, \
            str(self.egrid[0]), str(self.egrid[1]), self.etime,] \
            + [str (it) for it in self.passways]

    def __str__ (self):
        sp = ','.join ([self.car, self.stime, self.etime, 
            str(len (self.passways))] + self.passways)
        return sp

def genpath (gmap):
    paths = {}
    # read cdata
    reader = csv.reader (sys.stdin)
    writer = csv.writer (sys.stdout)
    for row in reader:
        car = row[1]
        grid = gridid (int(row[4]), int(row[5]))
        # TODO implete the gridmap()
        passway = gmap (grid)
        # not in the grid map, ignore
        if passway == 0:
            continue
        time = row[3]
        # car is serving
        if row[10] == '1':
            if car in paths:
                p = paths[car]
                if p.passways[len (p.passways) - 1] == passway:
                    continue
                else:
                    p.passways.append (time, passway)
            else:
                paths[car] = Path (car, time, grid)
                paths[car].append (passway)
        else:
            if car in paths:
                paths[car].etime = time
                paths[car].dgrid = grid
                writer.writerow (paths[car].tolist ())
                del paths[car]

if __name__ == '__main__':
    import numpy as np
    gmap = np.genfromtxt (sys.argv[1])
    genpath (gmap)

