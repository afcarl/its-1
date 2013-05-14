#! /usr/bin/python

import numpy as np
import sys

def markentity (entity, roadmap):
    entitymap = np.array (roadmap)
    width, height = entity.shape
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if entity[x, y] == 0 or entitymap[x,y] != 0:
                continue
            m = 2000000
            for i in range (x - 1, x + 2):
                for j in range (y - 1, y + 2):
                    if m > roadmap [i, j] > 0:
                        m = roadmap [i, j]
                    
            if m > 0:
                entitymap [x, y] = m
    return entitymap

if __name__ == '__main__':
    entity = np.genfromtxt (sys.argv[1])
    roadmap = np.genfromtxt (sys.argv[2])
    entitymap = markentity (entity, roadmap)
    np.savetxt (sys.stdout, entitymap, fmt = '%d')


