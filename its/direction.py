import math

def direction (origin, dest):
    dx = float(dest[0] - origin[0])
    dy = float(dest[1] - origin[1])
    if dx == 0 and y > 0:
        return 1
    if dx == 0 and y < 0:
        return 5
    rate = dy / dx

    if rate > math.tan (math.pi * 3 / 8):
        if dx > 0:
            return 1
        return 5
    elif rate > 1:
        if dx > 0:
            return 2
        return 6
    elif rate > math.tan (math.pi / 8):
        if dx > 0:
            return 2
        return 6
    elif rate > 0:
        if dx > 0:
            return 3
        return 7
    elif rate > - math.tan (math.pi / 8):
        if dx > 0:
            return 3
        return 7
    elif rate > - 1:
        if dx > 0:
            return 4
        return 8
    elif rate > - math.tan (math.pi * 3 / 8):
        if dx > 0:
            return 4
        return 8
    else:
        if dx > 0:
            return 5
        return 1

