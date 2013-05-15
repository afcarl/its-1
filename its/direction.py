import math
import csv
center = {}
centerfile = open ('data/center.datx')
reader = csv.reader (centerfile)
for row in reader:
    center[int (row[0])] = (int (row[1]), int (row[2]))

def direction (origin, dest):
    dx = float(dest[0] - origin[0])
    dy = float(dest[1] - origin[1])
    if dx == 0 and dy >= 0:
        return 0
    if dx == 0 and dy < 0:
        return 4
    rate = dy / dx
    if rate > math.tan (math.pi * 3 / 8):
        if dx > 0:
            return 0
        return 4
    elif rate > math.tan (math.pi / 8):
        if dx > 0:
            return 1
        return 5
    elif rate > - math.tan (math.pi / 8):
        if dx > 0:
            return 2
        return 6
    elif rate > - math.tan (math.pi * 3 / 8):
        if dx > 0:
            return 3
        return 7
    else:
        if dx > 0:
            return 4
        return 0
def oddirection (start, end):
    return direction (center[start], center[end])
if __name__ == '__main__':
    import sys
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    print (oddirection (start, end))

