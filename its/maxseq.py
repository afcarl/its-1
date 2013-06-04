import csv
import sys
from direction import direction, center
prob = [0] * 8000
prev = [0] * 8000
TRANS = dict ()
def gen_path (start, end):
    prob[start] = 1.0
    prev[start] = 0
    change = True
    while change:
        change = False
        for tran, p in TRANS.items ():
            a, d, b = tran
            if direction (center[a], center[end]) != d:
                #print direction (center[a], center[end]), d
                continue
            if prob[b] < prob[a] * p:
                prob[b] = prob[a] * p
                prev[b] = a
                change = True
    pr = prev[end]
    path = [end]

    while pr != start and pr != 0:
        path.append (pr)
        pr = prev[pr]
    path.append (start)
    return path

def run ():
    start = int (sys.argv[1])
    end = int (sys.argv[2])
    reader = csv.reader (sys.stdin)
    writer = csv.writer (sys.stdout)
    for row in reader:
        TRANS[int(row[0]), int(row[1]), int(row[2])] = float (row[3])
    writer.writerow (gen_path (start, end))

def test ():
    tranfile = open (sys.argv[1])
    reader = csv.reader (tranfile)
    for row in reader:
        TRANS[int(row[0]), int(row[1]), int(row[2])] = float (row[3])

    writer = csv.writer (sys.stdout)
    tfile = open (sys.argv[2])
    reader = csv.reader(tfile)
    for row in reader:
        writer.writerow (gen_path (int (row[0]), int (row[-1])))

if __name__ == '__main__':
    test ()

