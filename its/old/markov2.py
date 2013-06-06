import csv
import sys
from collections import Counter
reader = csv.reader (sys.stdin)
writer = csv.writer (sys.stdout)
counter = Counter ()
for row in reader:
    if len (row) <= 6:
        continue
    seq = []
    for p in row[6:]:
        p = int (p)
        if p != 4 and (len(seq) == 0 or p != seq[-1]):
            seq.append (int (p))
    for i in range (0, len (seq) - 1):
        counter[(seq[i], seq[i+1])] += 1
for a, b in counter.items ():
    writer.writerow ([a[0], a[1], b])

