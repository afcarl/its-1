#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def showcwmap (data):
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
    #plt.savefig ('cw.png', bbox_inches='tight')
    plt.show ()

if __name__ == '__main__':
    import sys
    data = np.genfromtxt (sys.stdin)
    showcwmap (data)

