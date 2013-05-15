import csv
import sys
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
    return path

if __name__ == '__main__':
    start = int (sys.argv[1])
    end = int (sys.argv[2])
    reader = csv.reader (sys.stdin)
    writer = csv.writer (sys.stdout)
    for row in reader:
        TRANS[int(row[0]), int(row[1])] = float (row[2])
    writer.writerow (gen_path (start, end))
