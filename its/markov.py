import csv
import sys
from collections import Counter

def static_markov ():
    reader = csv.reader (sys.stdin)
    markov = {}
    for row in reader:
        for i in range (8, len (row) - 1, 2):
            if not row[i] in markov:
                markov[row[i]] = Counter ()
            markov[row[i]][row[i + 2]] += 1
    return markov

if __name__ == '__main__':
    markov = static_markov ()
    writer = csv.writer (sys.stdout)
    for passway, cnt in markov.items():
        data = [passway]
        for p, c in cnt.items():
            data.append (p)
            data.append (c)
        writer.writerow (data)

