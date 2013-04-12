import sys
import csv
def gensequence ():
    reader = csv.reader (sys.stdin)
    for row in reader:
        seq = row[5:]
        if seq != []:
            print (','.join (seq))

gensequence ()
