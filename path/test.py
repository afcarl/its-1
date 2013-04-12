import csv
with open ("Topo.csv", newline = '') as f:
    reader = csv.reader (f)
    count = 0 
    for row in reader:
        count += 1
        print (row)
        if (count > 10):
            break

