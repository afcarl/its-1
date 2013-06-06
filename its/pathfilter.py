import csv
import sys
"""
minox = 252
minoy = 342
maxox = 319
maxoy = 387
mindx = 165
mindy = 148
maxdx = 217
maxdy = 197
"""

reader = csv.reader (sys.stdin)
writer = csv.writer (sys.stdout)
for row in reader:
    """
    ox = int (row[2][:3])
    oy = int (row[2][3:])
    dx = int (row[4][:3])
    dy = int (row[4][3:])
    if not minox < ox < maxox or not minoy < oy < maxoy \
            or not mindx < dx <maxdx or not mindy < dy < maxdy:
        continue
    """
    if row[1][:2] != '05' or len(row) < 10:
        continue
    writer.writerow (row)

