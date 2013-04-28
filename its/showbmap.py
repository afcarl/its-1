#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def showbmap (data):
    data = data.T[::-1, :]
    plt.gray ()
    plt.imshow (data)
    plt.show ()


if __name__ == '__main__':
    import sys
    data = np.genfromtxt (sys.stdin)
    data[data > 0] = 1
    showbmap (data)
