import sys
import numpy as np
import csv
import config
class Path:
    def __init__(self, car, stime, sgrid):
        self.car = car
        self.stime = stime
        self.etime = ''
        self.lasttime = stime
        self.lastgrid = sgrid
        self.sgrid = sgrid
        self.egrid = sgrid
        self.passways = [] 
    def tolist (self):
        return [self.car, self.stime, str_grid(self.sgrid), self.etime, \
                str_grid(self.egrid)] + [str (it) for it in self.passways]

def delta_time (a, b):
    ta = int (a[0:2]) * 60 + int(a[2:4])
    tb = int (a[0:2]) * 60 + int(a[2:4])
    if ta < tb:
        ta += 24 * 60 * 60
    return ta - tb

def str_grid (grid):
    return str(grid[0]).zfill(3) + str(grid[1]).zfill(3)

def genpath (gmap):
    paths = {}
    # read cdata
    reader = csv.reader (sys.stdin)
    writer = csv.writer (sys.stdout)
    for row in reader:
        if len (row) != 13:
            continue
        car = row[2]
        grid = config.gridid (float(row[6]), float(row[7]))
        if grid == (0, 0):
            continue
        passway = gmap [grid]
        time = row[3][8:12]
        # car is serving
        if row[10] == '1':
            if car not in paths:
                paths[car] = Path (car, time, grid)
            elif delta_time (time, paths[car].lasttime) > config.MAXINTER:
                paths[car].etime = paths[car].lasttime
                paths[car].egrid = paths[car].lastgrid
                writer.writerow (paths[car].tolist ())
                paths[car] = Path (car, time, grid)
            if passway < 10:
                ps = paths[car].passways
                if passway == config.TURN and len(ps) > 0:
                    passway = ps[-1]
                else:
                    passway = config.OTHER
            paths[car].passways.append (passway)
        elif car in paths:
            if delta_time (time, paths[car].lasttime) > config.MAXINTER:
                paths[car].etime = paths[car].lasttime
                paths[car].egrid = paths[car].lastgrid
            else:
                paths[car].etime = time
                paths[car].egrid = grid
            writer.writerow (paths[car].tolist ())
            del paths[car]

if __name__ == '__main__':
    gmap = np.genfromtxt (sys.argv[1], dtype = np.int32)
    genpath (gmap)

