#! /usr/bin/python

import numpy as np
import sys

cross = 0 

def neighbor (grid, cx, cy):
    n = 0
    width, height = grid.shape
    if grid[cx, cy] > 0:
        n -= 1
    for x in range (cx - 1, cx + 2):
        for y in range (cy - 1, cy + 2):
            if 0 <= x < width and 0 <= y < height and grid[x, y] > 0:
                n += 1
    return n

def mark (grid, roadmap, x, y, roadid):
    width, height = grid.shape
    if not (0 <= x < width and 0 <= y < height) \
        or grid [x, y] == 0 or roadmap[x, y] != 0:
        return
    n = neighbor (grid, x, y)
    if n == 0:
        return
    if n == 1:
        roadmap[x, y] = roadid
        return
    if n >= 3:
        roadmap[x, y] = roadid
        return
    roadmap[x, y] = roadid

    mark (grid, roadmap, x - 1, y - 1, roadid)
    mark (grid, roadmap, x - 1, y, roadid)
    mark (grid, roadmap, x - 1, y + 1, roadid)
    mark (grid, roadmap, x, y - 1, roadid)
    mark (grid, roadmap, x, y + 1, roadid)
    mark (grid, roadmap, x + 1, y - 1, roadid)
    mark (grid, roadmap, x + 1, y, roadid)
    mark (grid, roadmap, x + 1, y + 1, roadid)
    
def markroad (grid):
    roadmap = np.zeros (grid.shape, dtype = np.int32)
    it = np.nditer (grid, flags = ['multi_index'])
    roadid = 1
    while not it.finished:
        x, y = it.multi_index
        if it[0] != 0 and roadmap[x, y] == 0:
            mark (grid, roadmap, x, y, roadid)
            roadid += 1
        it.iternext ()
    return roadmap

if __name__ == '__main__':
    grid = np.genfromtxt (sys.stdin, dtype = np.int32)
    roadmap = markroad (grid)
    np.savetxt (sys.stdout, roadmap, fmt = '%d')

