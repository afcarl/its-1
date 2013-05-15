import math

def direction (origin, dest):
    dx = float(dest[0] - origin[0])
    dy = float(dest[1] - origin[1])
    if dx == 0 and dy >= 0:
        return 1
    if dx == 0 and dy < 0:
        return 5
    rate = dy / dx
    if rate > math.tan (math.pi * 3 / 8):
        if dx > 0:
            return 1
        return 5
    elif rate > math.tan (math.pi / 8):
        if dx > 0:
            return 2
        return 6
    elif rate > - math.tan (math.pi / 8):
        if dx > 0:
            return 3
        return 7
    elif rate > - math.tan (math.pi * 3 / 8):
        if dx > 0:
            return 4
        return 8
    else:
        if dx > 0:
            return 5
        return 1
def oddirection (start, end, entity):
    width, height = entity.shape
    for x in range (width):
        for y in range (height):
            if entity[x, y] == start:
                s = (x, y)
            if entity[x, y] == end:
                e = (x, y)
    return direction (s, e)
if __name__ == '__main__':
    import numpy as np
    import sys
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    entity = np.genfromtxt ('data/entitymap.datx', dtype = np.int32)
    print (oddirection (start, end, entity))

