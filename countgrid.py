import csv
import sys
reader = csv.reader (sys.stdin)
total = 0
check = 0
for row in reader:
    for d in row:
        d = float (d)
        total += 1
        if d > 100.0:
            check += 1
    
print (total, check, check / total)
