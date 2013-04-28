#! /usr/bin/python

import numpy as np
import sys

def markentity (entity, roadmap):
    entitymap = np.array (roadmap)
    width, height = entity.shape
    change = 1
    while change > 0:
        change = 0
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                if entity[x, y] == 0 or entitymap[x,y] != 0:
                    continue
                maxnei = 0
                for i in range (x - 1, x + 2):
                    for j in range (y - 1, y + 2):
                        if entitymap [i, j] > 0 and entity[i, j] > maxnei:
                            maxnei = entitymap[i, j]
                            change += 1
                entitymap[x, y] = maxnei
    return entitymap

if __name__ == '__main__':
    entity = np.genfromtxt (sys.argv[1])
    roadmap = np.genfromtxt (sys.argv[2])
    entitymap = markentity (entity, roadmap)
    np.savetxt (sys.stdout, entitymap, fmt = '%d')


