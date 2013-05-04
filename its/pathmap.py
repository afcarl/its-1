import sys
import csv
import numpy as np
reader = csv.reader (sys.stdin)
writer = csv.writer (sys.stdout)
paths = set ()
for row in reader:
    for p in row[5:]:
        paths.add (int(p))

entity = np.genfromtxt (sys.argv[1], dtype = np.int32)
width, height = entity.shape
for x in range (width):
    for y in range (height):
        if entity[x, y] in paths:
            entity[x, y] = 1
        else:
            entity[x, y] = 0
np.savetxt (sys.stdout, entity, fmt='%d')
