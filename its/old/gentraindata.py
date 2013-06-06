import csv
import sys

def gentraindata (fin, fout, fdic):
    index = {'4':'1'}
    nextindex = 3
    reader = csv.reader (fin)
    for row in reader:
        fout.write ('2 ')
        for p in row[5:]:
            if p in index:
                fout.write (index[p] + ' ')
            else:
                idx = str (nextindex)
                index[p] = idx
                fout.write (idx + ' ')
                nextindex += 1
        fout.write ('2 ')
    for k, v in index.items ():
        fdic.write (k + ':' +  v + '\n')

if __name__ == '__main__':
    dicfile = open (sys.argv[1], 'w')
    gentraindata (sys.stdin, sys.stdout, dicfile)


