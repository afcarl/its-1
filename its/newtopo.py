
import csv
import sys
import numpy as np
import config

def topo (entity):
    writer = csv.writer(sys.stdout)
    width, height = entity.shape
    topo = set ()
    for i in range (width):
        for j in range (height):
            if entity[i, j] == 0 or entity[i, j] > 10000:
                continue
            for k in range (i - 1, i + 2):
                for m in range (j - 1, j + 2):
                    if k < 0 or k >= config.NX:
                        continue
                    if m < 0 or m >= config.NY:
                        continue
                    if entity[k, m] == 0:
                        continue
                    if entity[k, m] > entity[i, j]:
                        topo.add ((entity[i, j], entity[k, m]))
                    elif entity[k, m] < entity[i, j]:
                        topo.add ((entity[k, m], entity[i, j]))
    for a, b in topo:
        print a, b

if __name__ == '__main__':
    entity = np.genfromtxt (sys.stdin, dtype = np.int32)
    topo (entity)


