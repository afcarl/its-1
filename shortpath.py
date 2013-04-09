""" comput the shortest path between 2 points"""

import numpy as np
# TODO: fix this method
def shortpath (grid, origin, dest):
    pathmap = np.zerors (grid.shape ())
    queue = []
    queue.append (dest)

