import csv
import sys
from direction import direction, center

def judge (path, TRANS):
    prob = 1.0
    for i in range (len(path) - 1):
        d = direction (center[path[i]], center[path[-1]])
        prob = prob * TRANS[d, path[i], path[i+1]]
    return [prob] + path

def test ():
    tranfile = open (sys.argv[1])
    reader = csv.reader (tranfile)
    TRANS = dict ()  
    for row in reader:
        TRANS[int(row[0]), int(row[1]), int(row[2])] = float (row[3])

    writer = csv.writer (sys.stdout)
    tfile = open (sys.argv[2])
    reader = csv.reader(tfile)
    i = 1
    for row in reader:
        print >> sys.stderr, i
        i += 1
        path = [int (p) for p in row[5:]]
        writer.writerow (judge (path, TRANS))

if __name__ == '__main__':
    test ()

