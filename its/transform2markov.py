import sys
import csv
reader = csv.reader (sys.stdin)
writer = csv.writer (sys.stdout)
last = 0
output = []
s = 0
for row in reader:
    a = int (row[0])
    if a == last or last == 0:
        s += int(row[2])
        output.append (row)
    else:
        for row in output:
            row [2] = float (row[2]) / s
            writer.writerow (row)
        s = 0
        output = []
    last = a

