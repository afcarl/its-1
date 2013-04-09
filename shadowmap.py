import sys
import csv

reader = csv.reader (sys.stdin)
writer = csv.writer (sys.stdout)
newrow = []
for row in reader:
    for d in row:
        d = float (d)
        nd = int (d > 20)
        newrow.append (nd)
    writer.writerow (newrow)
    del newrow[:]

