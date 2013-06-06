import csv
import sys
from direction import direction, center

def gen_path (start, end, TRANS):
    prob = [0] * 8000
    prev = [0] * 8000
    markov = {}
    prob[start] = 1.0
    prev[start] = 0
    change = True
    for tran, p in TRANS.items ():
        d, a, b = tran
        if direction (center[a], center[end]) == d:
            markov[a, b] = p
    while change:
        change = False
        for tran, p in markov.items ():
            a, b = tran
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
    path.append (prob[end])
    path.reverse ()
    return path

def run ():
    start = int (sys.argv[1])
    end = int (sys.argv[2])
    reader = csv.reader (sys.stdin)
    writer = csv.writer (sys.stdout)
    TRANS = dict ()  
    for row in reader:
        TRANS[int(row[0]), int(row[1]), int(row[2])] = float (row[3])
    writer.writerow (gen_path (start, end, TRANS))

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
        writer.writerow (gen_path (int (row[5]), int (row[-1]), TRANS))

if __name__ == '__main__':
    test ()

