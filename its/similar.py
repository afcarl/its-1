import csv
import sys
from collections import Counter

tfile = open (sys.argv[1])
pfile = open (sys.argv[2])
tcnt = Counter ()
pcnt = Counter ()
treader = csv.reader (tfile)
preader = csv.reader (pfile)
for row in treader:
    for p in row:
        tcnt[int(p)] += 1
for row in preader:
    for p in row:
        pcnt[int(p)] += 1

print 'len_t:', len (tcnt)
print 'len_p:', len (pcnt)

ratek = 0.1
while ratek <= 1.0:
    k = int(ratek * len (pcnt))
    set_t = set ([p[0] for p in tcnt.most_common (k)])
    set_p = set ([p[0] for p in pcnt.most_common (k)])
    s = 1.0 * len (set_t & set_p) / len (set_t | set_p)
    print
    print 'ratek:', ratek
    print 'k:    ', k
    print 's:    ', s
    ratek += 0.1

