import csv
import sys
from collections import Counter
from direction import direction, center

def static_markov ():
    reader = csv.reader (sys.stdin)
    markov = {}
    for row in reader:
        end = (int (row[4][:3]), int (row[4][3:]))
        row = [int (p) for p in row]
        for i in range (5, len (row) - 1):
            d = direction (center[row[i]], end)
            if not (row[i],d) in markov:
                markov[row[i], d] = Counter ()
            markov[row[i], d][row[i + 1]] += 1
    return markov

if __name__ == '__main__':
    markov = static_markov ()
    writer = csv.writer (sys.stdout)
    for key, cnt in markov.items():
        s = sum (cnt.values ())
        for p, c in cnt.items():
            writer.writerow ([key[0], key[1], p, float (c) / s, c])

