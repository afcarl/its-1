import csv
import sys
States = {}

class transnode:
    def __init__(self, lid):
        self.lid = lid
        self.count = 1

class state:
    def __init__(self):
        self.count = 1
        self.transnodes = []

def genstate ():
    f = open ('Topo.csv', newline = '')
    reader = csv.reader (f)
    for row in reader:
        lid = row[1] + row[2].zfill(5)
        s = state ()
        nin = int (row[6])
        start = 9 + nin * 5
        for i in range (start, len(row) - 1, 5):
            tn = transnode (row[i] + row[i + 1].zfill(5))
            s.transnodes.append (tn)

        States[lid] = s
    f.close ()

def static ():
    reader = csv.reader (sys.stdin)
    for row in reader:
        for i in range (len (row) - 1):
            States[row[i]].count += 1
            trs = row[i + 1]
            for tn in States[row[i]].transnodes:
                if tn.lid == trs:
                    tn.count += 1
        States[row[len(row) - 1]].count += 1

def test ():
    writer = csv.writer (sys.stdout)
    for lid, state in States.items():
        #writer.writerow ([lid, state.count] + zip (
        print (lid, state.count, 
            ','.join ([n.lid +',' +  str(n.count) for n in state.transnodes]))

genstate ()
static ()
test ()
