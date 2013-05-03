
#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def showbmap (gmap, paths):
    gmap = gmap.T[::-1, :]
    pic = np.zeros (gmap.shape)
    for p in paths:
        pic += (gmap == p)
    
    plt.gray ()
    plt.imshow (pic)
    plt.show ()


if __name__ == '__main__':
    import sys
    fgmap = sys.argv[1]
    fpaths = sys.argv[2]
    gmap = np.genfromtxt (fgmap)
    paths = []
    for row in open (fpaths):
        paths.extend ([int(p) for p in row.split(',')])
    showbmap (gmap, paths)
