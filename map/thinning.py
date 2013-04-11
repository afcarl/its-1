""" thinning the map to get the skeleton"""
import sys
import numpy as np

def nseq (grid, point):
    a = 0
    x, y = point
    if grid[x - 1, y] == 0 and grid[x - 1, y + 1] == 1:
        a += 1
    if grid[x - 1, y + 1] == 0 and grid[x, y + 1] == 1:
        a += 1
    if grid[x, y + 1] == 0 and grid[x + 1, y + 1] == 1:
        a += 1
    if grid[x + 1, y + 1] == 0 and grid[x + 1, y] == 1:
        a += 1
    if grid[x + 1, y] == 0 and grid[x + 1, y - 1] == 1:
        a += 1
    if grid[x + 1, y - 1] == 0 and grid[x, y - 1] == 1:
        a += 1
    if grid[x, y - 1] == 0 and grid[x - 1, y - 1] == 1:
        a += 1
    if grid[x - 1, y - 1] == 0 and grid[x - 1, y] == 1:
        a += 1
    return a

def nnei (grid, point):
    cx, cy = point
    width, height = grid.shape
    b = 0
    for x in range (cx -1, cx + 2):
        for y in range (cy - 1, cy + 2):
            if 0 <= x < width and 0 <= y < height:
                b += grid[x, y]
    return b - grid[cx, cy]

def postnei (grid, point):
    cx, cy = point
    width, height = grid.shape
    nei = set ()
    for x in range (cx - 1, cx + 2):
        for y in range (cy - 1, cy + 2):
            if (x, y) == (cx, cy) or not (0 <= x < width) \
                or not (0 <= y < height):
                continue
            nei.add ((x, y))
    return nei


def islink (grid, point):
    nb = postnei (grid, point)
    linknb = set ()
    for n in nb:
        linknb |= postnei (grid, n)
    return nb <= linknb
"""
    if len (nb) == 0:
        return False
    linknb = []
    n = nb[0]
    linknb.append (n)
    for n in nb:
        for ln in linknb:
            if n in postnei (nb):
                linknb.append (n)
    if len (linknb) == len (nb):
        return True
    return False
"""
    
def thinning (grid):
    width, height = grid.shape
    while True:
        c = 0
        for x in range (1, width - 1):
            for y in range (1, height - 1):
                if 2 <= nnei (grid, (x, y)) <= 6 and \
                        nseq (grid, (x, y)) == 1 and \
                        grid[x-1, y] * grid[x, y+1] * grid[x+1, y] == 0 and \
                        grid[x, y+1] * grid[x+1, y] * grid[x, y-1] == 0 :
                    if grid[x, y] == 1:
                        grid[x, y] = 0
                        c += 1
        if c == 0:
            return grid
        c = 0
        for x in range (1, width - 1):
            for y in range (1, height - 1):
                if 2 <= nnei (grid,(x, y)) <= 6 and \
                    nseq (grid, (x, y)) == 1 and \
                        grid[x-1, y] * grid[x, y+1] * grid[x, y-1] == 0 and \
                        grid[x-1, y] * grid[x+1, y] * grid[x, y-1] == 0 :
                    if grid[x, y] == 1:
                        grid[x, y] = 0
                        c += 1
        if c == 0:
            return grid

def clean (grid):
    count = 0
    width, height = grid.shape
    for cx in range (1, width):
        for cy in range (1, height):
            if grid[cx, cy] == 0:
                continue
            n = nnei (grid, (cx, cy))
            if n == 0:
                grid[cx, cy] = 0
                count += 1
            elif 3 >= n > 1: 
                if not islink (grid, (cx, cy)):
                    grid[cx, cy] = 0
                    count += 1
    return count

if __name__ == "__main__":
    grid = np.genfromtxt (sys.stdin)
    w, h = grid.shape
    #sep = 100
    #grid[grid < sep] = 0
    #grid[grid >= sep] = 1
    grid[grid > 0] = 1
    grid[0,:] = 0
    grid[w - 1, :] = 0
    grid[:, 0] = 0
    grid[:, h - 1] = 0

    thinning (grid)
    n = clean (grid)
    while n > 0:
        n = clean (grid)
    np.savetxt (sys.stdout, grid, fmt = '%d')

