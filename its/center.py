import numpy as np
import sys
import csv
"""compute every passway's center grid"""
center = {}
entity = np.genfromtxt ('data/entitymap.datx', dtype=np.int32)
width, height = entity.shape
for i in range (width):
    for j in range (height):
        e = entity[i, j]
        if e >= 10000 or e == 0:
            continue
        if e not in center:
            center[e] = [0, 0, 0]
        center[e][0] += 1 # count
        center[e][1] += i # sum x
        center[e][2] += j # sum y

writer = csv.writer (sys.stdout)
for c, v in center.items ():
    writer.writerow ([c, v[1] / v[0], v[2]/v[0]])
    
