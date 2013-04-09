import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
def readdata ():
    rdata = []
    reader = csv.reader (sys.stdin)
    nr = 0
    for row in reader:
        nr += 1
        for d in row:
            rdata.append (int (float (d) < 100))
    nc = len (rdata) / nr
    data = np.array (rdata)
    data = data.reshape (nr, nc)
    tdata = np.zeros (data.shape, dtype = 'int32')
    for r in range (nr):
        for c in range (nc):
            tdata[nr - r - 1][c] = data[r][c]
    return tdata

def showimg (data):
    plt.gray ()
    plt.imshow (data)
    plt.show ()

showimg (readdata ())

