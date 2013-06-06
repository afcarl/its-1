import csv
import sys
from direction import direction, center

def gen_path (start, end, TRANS):
    N = 5000
    prob = [0] * N
    prev = [0] * N
    Q = set ()
    adj = [[]] * N
    prob[start] = 1.0
    prev[start] = 0
    for tran, p in TRANS.items ():
        d, a, b = tran
        if direction (center[a], center[end]) == d:
            Q.add (a)
            Q.add (b)
            adj[a].append ((b, p))
    #change = True

    while len(Q) > 0:
        #change = False
        maxv = 0
        maxp = 0
        for v in Q:
            if prob[v] >= maxp:
                maxv = v
                maxp = p
        Q.remove (maxv)
        for n, p in adj[maxv]:
            if prob[maxv] * p >= prob[n]:
                prob[n] = prob[maxv] * p
                prev[n] = maxv
                #change = True

    path = [end]
    pr = prev[end]
    print pr
    while pr != start:
        print pr
        if pr == 0:
            print >> sys.stderr, 'zero'
            break
        path.append (pr)
        pr = prev[n]
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
    test()
