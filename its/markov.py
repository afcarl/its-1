import csv
import sys
from collections import Counter
from direction import direction, center

def static_markov ():
    reader = csv.reader (sys.stdin)
    markov = [{}] * 8
    for row in reader:
        end = (int (row[4][:3]), int (row[4][3:]))
        row = [int (p) for p in row]
        for i in range (5, len (row) - 1):
            d = direction (center[row[i]], end)
            if row[i] not in markov[d]:
                markov[d][row[i]] = Counter ()
            markov[d][row[i]][row[i+1]] += 1
    return markov

if __name__ == '__main__':
    markov = static_markov ()
    writer = csv.writer (sys.stdout)
    for d in range (8):
        for r, cnt in markov[d].items ():
            s = sum (cnt.values ())
            for p, c in cnt.items():
                writer.writerow ([d, r, p, float (c) / s, c])

