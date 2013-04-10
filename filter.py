import numpy as np
data = np.genfromtxt ('gridcdata.txt')
width, height = data.shape

for x in range (0, width, 8):
    for y in range (0, height, 8):
        area = data[x:x + 8, y:y + 8]
        mean = area.mean ()
        area[area < mean] = 0

np.savetxt ('filtered.txt', data)

