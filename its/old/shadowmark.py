import numpy as np
import sys
import mark

def shadowmark (entity):
    shadow = np.array (entity)
    width, height = entity.shape
    for x in range (1, width):
        for y in range (1, height):
            if entity[x, y] == 0:
                continue
            for i in range (x - 1, x + 2):
                for j in range (y - 1, y + 2):
                    if entity[i, j] == mark.TURN:
                        for k in range (i - 1, i+2):
                            for m in range (j - 1, j + 2):
                                shadow[k, m] = mark.TURN
                    elif shadow[i,j] == 0:
                        shadow[i,j] = entity[x,y]
                    elif entity[i,j] == 0 and shadow[i,j] != entity[x,y]:
                        shadow[i,j] = mark.IGNORE

    return shadow

if __name__ == '__main__':
    entity = np.genfromtxt (sys.stdin, dtype = np.int32)
    shadow = shadowmark (entity)
    np.savetxt (sys.stdout, shadow, fmt='%d')

