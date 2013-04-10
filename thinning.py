""" thinning the map to get the skeleton"""
import sys
import numpy as np

def A (grid, point):
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

def B (grid, point):
    cx, cy = point
    b = 0
    for x in range (cx -1, cx + 2):
        for y in range (cy - 1, cy + 2):
            b += grid[x, y]
    return b - grid[cx, cy]


def thinning (grid):
    width, height = grid.shape
    while True:
# add for filter single point
        for x in range (1, width - 1):
            for y in range (1, height - 1):
                if B (grid, (x, y)) < 1:
                    grid[x, y] = 0
        c = 0
        for x in range (1, width - 1):
            for y in range (1, height - 1):
                if 2 <= B (grid, (x, y)) <= 6 and A (grid, (x, y)) == 1 and \
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
                if 2 <= B (grid,(x, y)) <= 6 and A (grid, (x, y)) == 1 and \
                        grid[x-1, y] * grid[x, y+1] * grid[x, y-1] == 0 and \
                        grid[x-1, y] * grid[x+1, y] * grid[x, y-1] == 0 :
                    if grid[x, y] == 1:
                        grid[x, y] = 0
                        c += 1
        if c == 0:
            return grid

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
    np.savetxt (sys.stdout, grid, fmt = '%d')

