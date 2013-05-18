import glob
import numpy as np
import sys
grid = np.zeros ((512, 512),  dtype = np.int32)
for f in glob.glob ('F:/gridcdata/*'):
    grid += np.genfromtxt (f, dtype = np.int32)
np.savetxt (sys.stdout, grid, fmt = '%d')


