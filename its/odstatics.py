import csv
import numpy as np
import sys
ofile = sys.argv[1]
dfile = sys.argv[2]
reader = csv.reader (sys.stdin)
omatrix = np.zeros ((512, 512))
dmatrix = np.zeros ((512, 512))
for row in reader:
    if len (row) < 6:
        continue
    o = int (row[2][0:3]), int (row[2][3:])
    d = int (row[4][0:3]), int (row[4][3:])
    omatrix[o] += 1
    dmatrix[d] += 1
np.savetxt (ofile, omatrix, fmt='%d')
np.savetxt (dfile, dmatrix, fmt='%d')

