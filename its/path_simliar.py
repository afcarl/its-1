import sys
import csv
tfile = open (sys.argv[1])
pfile = open (sys.argv[2])
treader = csv.reader (tfile)
preader = csv.reader (pfile)
writer = csv.writer (sys.stdout)

while True:
    try:
        trow = next (treader)
        prow = next (preader)
    except:
        break

    tset = set (trow[1:])
    pset = set (prow[1:])
    s = len (tset & pset) * 1.0 / len (tset | pset)
    writer.writerow ([len (tset), len (pset), s])


