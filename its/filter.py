#! /usr/bin/python


import numpy as np

def nnei (grid, point):
    cx, cy = point
    width, height = grid.shape
    b = 0
    for x in range (cx -1, cx + 2):
        for y in range (cy - 1, cy + 2):
            if 0 <= x < width and 0 <= y < height:
                b += (grid[x, y] > 0)
    return b - (grid[cx, cy] > 0)

def two_means (data):
    from scipy.cluster.vq import vq, kmeans, whiten
    mean = data.mean ()
    data[data > mean] = mean
    feature = data.reshape (data.size, 1)
    whitened = whiten (feature)
    book, distortion = kmeans (whitened, 2)
    book = book.reshape (1, book.size)
    book.sort ()
    book = book.reshape (book.size, 1)
    label, distort = vq (whitened, book)
    label = label.reshape (data.shape)
    data[:, :] = label

def two_means_filter (data):
    data = data
    size = 512
    width, height = data.shape
    for x in range (0, width, size):
        for y in range (0, height, size):
            if data.std () == 0:
                data[:,:] = 0
            two_means (data[x:x + size, y:y + size])
    return data

def logfilter (data):
    sep = np.log (data.mean () + 1)
    data = np.log (data + 1)
    data [data < sep] = 0
    return data

def areafilter (data):
    width, height = data.shape
    size = 64
    for x in range (0, width, size):
        for y in range (0, height, size):
            area = data[x:x + size, y:y + size]
            mean = area.mean ()
            area[area < mean] = 0
    return data

def gradient_filter (data):
    width, height = data.shape
    grad = np.zeros (data.shape, dtype = np.float)
    for x in range (1, width - 1):
        for y in range (1, height - 1):
            if data[x, y] == 0:
                continue
            area = data[x - 1: x + 2, y - 1:y + 2]
            m = area.max ()
            grad [x, y] = (m - data[x, y]) / data[x, y]
    data [grad > 2] = 0
    return data

def coverfilter (data):
    sep = 0.3
    width, height = data.shape
    delete = np.zeros (data.shape, dtype = np.bool)
    for x in range (1, width - 1):
        for y in range (1, height - 1):
            if data[x, y] == 0:
                continue
            for i in range (x - 1, x + 2):
                for j in range (y - 1, y + 2):
                    if data[i, j] < data[x, y] * sep :
                        delete[i, j] = True
                        """
    for x in range (1, width - 1):
        for y in range (1, height - 1):
            cover = False
            equal = False
            if delete [i, j] == False:
                continue
            for nx in range (x - 1, x + 2):
                for ny in range (y - 1, y + 2):
                    if nx == x and ny == y:
                        continue
                    if delete[nx, ny] == False and\
                        data[nx, ny] * sep > data[x, y]:
                        cover = True
                    elif delete[nx, ny] == False and\
                        abs (data[nx, ny] - data[x, y]) < 0.2 * data[x,y]:
                        equal = True
            if cover and equal:
                delete [x, y] = False
            """

    data[delete] = 0
    return data

if __name__ == '__main__':
    import sys
    data = np.genfromtxt (sys.stdin)
    data = two_means_filter (data)
    np.savetxt (sys.stdout, data, fmt = '%d')

