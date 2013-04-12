import sys
import csv

odfile = 'filteredod.csv'
Paths = {}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Path:
    def __init__(self, car, stime, etime, spoint, epoint):
        self.car = car
        self.stime = stime
        self.etime = etime
        self.spoint = spoint
        self.epoint = epoint
        self.links = [] 
    def __str__ (self):
        sp = ','.join ([self.car, self.stime, self.etime, 
            str(len (self.links))] + self.links)
        return sp


def initOD ():
    with open (odfile, newline = '') as odf:
        reader = csv.reader (odf)
        for row in reader:
            car = row[2]
            sp = Point (row[4], row[5])
            ep = Point (row[7], row[8])
            path = Path (car, row[3].zfill(4), row[6].zfill(4), sp, ep)
            if car in Paths:
                Paths[car].append (path)
            else:
                Paths[car] = [path]

def genpath ():
    reader = csv.reader (sys.stdin)
    for row in reader:
        car = row[1]
        time = ''.join ([row[9], row[10]])
        if car in Paths:
            for path in Paths[car]:
                if path.stime <= time < path.etime:
                    links = path.links
                    l = len (links)
                    if l == 0 or row[2] != links[l - 1]:
                        links.append (row[2])
def test ():
    for car, paths in Paths.items():
        for p in paths:
            print (p)

initOD ()
genpath ()
test ()

