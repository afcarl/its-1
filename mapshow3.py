import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
"""
def readdata ():
    rdata = []
    reader = csv.reader (sys.stdin)
    nr = 0
    for row in reader:
        nr += 1
        for d in row:
            rdata.append (float (d))
    nc = len (rdata) / nr
    data = np.array (rdata)
    data = data.reshape (nr, nc)
    sep = np.log (data.mean() + 1)
    data = np.log (data + 1)
    data[data < sep] = np.nan
    return data
"""
def showimg ():
    data = np.genfromtxt ('gridcdata.txt')
    sep = np.log (data.mean() + 1)
    data = np.log (data + 1)
    data[data < sep] = np.nan
    plt.figure ()
    plt.grid (color='w')
    plt.imshow (data.T[::-1, :], extent=[0,1,0,1], cmap=plt.cm.coolwarm,
        interpolation='gaussian')
    ax = plt.gca ()
    ax.set_axis_bgcolor ('k')
    ax.set_xticks (np.linspace (0,1,11))
    ax.set_yticks (np.linspace (0, 1, 11))
    ax.set_xticklabels ([])
    ax.set_yticklabels ([])
    plt.colorbar ()
    fig = plt.gcf ()
    plt.savefig ('cw.png', bbox_inches='tight')
    plt.show ()

showimg ()

