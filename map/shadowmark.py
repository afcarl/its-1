import numpy as np
import sys

def markshadow (shadow, roadmap):
    shadowmap = np.array (roadmap)
    width, height = shadow.shape
    change = 1
    while change > 0:
        change = 0
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                if shadow[x, y] == 0 or shadowmap[x,y] != 0:
                    continue
                maxnei = 0
                for i in range (x - 1, x + 2):
                    for j in range (y - 1, y + 2):
                        if shadowmap [i, j] > 0 and shadow[i, j] > maxnei:
                            maxnei = shadow[i, j]
                            change += 1
                shadowmap[x, y] = maxnei
    return shadowmap

if __name__ == '__main__':
    shadow = np.genfromtxt (sys.argv[1])
    roadmap = np.genfromtxt (sys.argv[2])
    shadowmap = markshadow (shadow, roadmap)
    np.savetxt (sys.stdout, shadowmap, fmt = '%d')


