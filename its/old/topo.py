import csv
import sys
import numpy as np
import config

def topo (entity):
    writer = csv.writer(sys.stdout)
    width, height = entity.shape
    visited = np.zeros (entity.shape, dtype = np.bool)
    for i in range (width):
        for j in range (height):
            if entity[i, j] == 0 or entity[i,j] > 8:
                continue
            linkset = set ()
            edgeset = set ()
            linkset.add ((i, j))
            while len (linkset) > 0:
                p = linkset.pop ()
                visited[p] = True
                for k in range (i - 1, i + 2):
                    for m in range (j - 1, j + 2):
                        if k < 0 or k >= config.NX:
                            continue
                        if m < 0 or m >= config.NY:
                            continue

                        if visited[k,m]:
                            continue
                        if entity[k,m] > 8:
                            edgeset.add (entity[k,m])
                        else:
                            linkset.add ((k,m))
            if len (edgeset) > 1:
                writer.writerow (list(edgeset))

if __name__ == '__main__':
    entity = np.genfromtxt (sys.stdin, dtype = np.int32)
    topo (entity)


