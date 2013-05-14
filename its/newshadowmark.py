#! /usr/bin/python

import numpy as np
import sys
WAIT = 0
def markshadow (entity):
    shadow = np.array (entity)
    width, height = entity.shape
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if entity[x, y] == 0:
                continue
            for i in range (x - 1, x + 2):
                for j in range (y - 1, y + 2):
                    if entity [i,j] > 0:
                        continue
                    if shadow [i,j] == 0:
                        shadow[i, j] = entity[x,y]
                    elif shadow[i,j] == entity[x,y]:
                        continue
                    elif shadow[i,j] < 10000:
                        continue
                    elif entity[i, j] < 10000:
                        shadow[i, j] = entity[i,j]
                    else:
                        shadow[i, j] = WAIT
    return shadow

if __name__ == '__main__':
    entity = np.genfromtxt (sys.argv[1])
    entitymap = markshadow (entity)
    np.savetxt (sys.stdout, entitymap, fmt = '%d')


