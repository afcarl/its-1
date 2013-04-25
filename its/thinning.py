#! /usr/bin/python

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
    link = np.zeros (8, dtype = np.bool)    
    neighbor = np.zeros (8, dtype = np.bool)
    x, y = point
    width, height = grid.shape
    if not ( 0 < x < width - 1 and 0 < y < height - 1):
        return False
    if grid[x - 1, y - 1] > 0:
        neighbor[0] = True
        link[1] = True
        link[7] = True
    if grid[x - 1, y] > 0:
        neighbor[1] = True
        link[0] = True
        link[2] = True
        link[7] = True
        link[3] = True
    if grid[x - 1, y + 1] > 0:
        neighbor[2] = True
        link[1] = True
        link[3] = True
    if grid[x, y + 1] > 0:
        neighbor [3] = True
        link[2] = True
        link[4] = True
        link[1] = True
        link[5] = True
    if grid[x + 1, y + 1] > 0:
        neighbor [4] = True
        link[3] = True
        link[5] = True
    if grid[x + 1, y] > 0:
        neighbor [5] = True
        link[3] = True
        link[4] = True
        link[6] = True
        link[7] = True
    if grid[x + 1, y - 1] > 0:
        neighbor [6] = True
        link[5] = True
        link[7] = True
    if grid[x, y - 1] > 0:
        neighbor [7] = True
        link[5] = True
        link[6] = True
        link[0] = True
        link[1] = True
    for i in range (8):
        if neighbor[i] and not link[i]:
            return True
    return False

def findneighbor (grid, point, line):
    sx, sy = point
    for x in range (sx - 1, sx + 2):
        for y in range (sy - 1, sy + 2):
            if grid[x, y] > 0 and (x, y) not in line:
                return (x, y)

def eatline (grid, point):
    sx, sy = point
    line = [(sx, sy)]
    p = findneighbor (grid, point, line)
    while nnei (grid , p) == 2:
        line.append (p)
        if len (line) > 10:
            return
        p = findneighbor (grid, p, line)
    for p in line:
        grid[p] = 0
    """
    else:
        for d in line:
            grid[d] = 0
        grid[p] = 0
        for x in range (p[0] - 1, p[0] + 2):
            for y in range (p[1] - 1, p[1] + 2):
                if islink (grid, (x, y)):
                    grid[x,y] = 1
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
    for cx in range (1, width - 1):
        for cy in range (1, height - 1):
            if grid[cx, cy] == 0:
                continue
            n = nnei (grid, (cx, cy))
            if n == 0:
                grid[cx, cy] = 0
                count += 1
            elif n == 1:
                eatline (grid, (cx, cy))
            else: 
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

