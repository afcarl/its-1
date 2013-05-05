#! /usr/bin/python

import numpy as np
import sys

BLANK = 0
IGNORE = 1
TURN = 2
"""
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
"""
def neighbormap (grids):
    width, height = grids.shape
    nei = np.zeros (grids.shape, dtype = np.int32)
    for x in range (1, width - 1):
        for y in range (1, height - 1):
            nei[x, y] = grids[x-1:x+2, y-1:y+2].sum() - grids[x,y]
    return nei

def passway (grids, neighbor, point):
    stack = []
    stack.append (point)
    way = []
    cur = 0
    while cur < len (stack):
        x, y = stack[cur]
        if grids[x, y]==1:
            way.append ((x, y))
            if neighbor [x, y] == 1 or neighbor[x,y] == 2:
                for i in range (x - 1, x + 2):
                    for j in range (y - 1, y + 2):
                        if (i, j) not in stack:
                            stack.append ((i, j))
        cur += 1
    return way


def markroad (grids):
    roadmap = np.zeros (grids.shape, dtype = np.int32)
    neighbor = neighbormap(grids)
    width, height = grids.shape
    roadid = 10
    for x in range (0, width):
        for y in range (0, height):
            if roadmap [x, y] > 0:
                continue
            if grids[x, y] == 0:
                roadmap[x, y] == BLANK
                continue
            if neighbor [x, y] == 0:
                roadmap[x, y] = IGNORE
            elif neighbor [x, y] == 2 or neighbor [x, y] == 1:
                way = passway (grids, neighbor,(x, y))
                if len (way) < 3:
                    m = IGNORE
                else :
                    m = roadid
                    roadid += 1
                for g in way:
                    roadmap [g] = m
            else:
                roadmap [x, y] = TURN

    return roadmap

if __name__ == '__main__':
    grids = np.genfromtxt (sys.stdin, dtype = np.int32)
    roadmap = markroad (grids)
    np.savetxt (sys.stdout, roadmap, fmt = '%d')

