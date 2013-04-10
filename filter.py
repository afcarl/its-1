import numpy as np

def logfilter (data):
    sep = np.log (data.mean () + 1)
    data = np.log (data + 1)
    data [data < sep] = 0
    return data

def areafilter (data):
    width, height = data.shape

    for x in range (0, width, 8):
        for y in range (0, height, 8):
            area = data[x:x + 8, y:y + 8]
            mean = area.mean ()
            area[area < mean] = 0
    return data

if __name__ == '__main__':
    import sys
    data = np.genfromtxt (sys.stdin)
    data = logfilter (data)
    np.savetxt (sys.stdout, data, fmt = '%d')

