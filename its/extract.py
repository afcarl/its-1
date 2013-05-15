import direction
import csv
import sys
reader = csv.reader (sys.stdin)
writer = [None] * 8
for i  in range (1, 9):
    f = open ('path'+str(i)+'.dat', 'w')
    writer[i - 1] = csv.writer (f)

for row in reader:
    if len (row) < 10:
        continue
    start = (int (row[2][:3]), int (row[2][3:]))
    end = (int (row[4][:3]), int (row[4][3:]))
    d = direction.direction (start, end)
    writer[d-1].writerow (row)

