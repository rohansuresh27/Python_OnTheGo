import csv

with open('HDFCBANK.csv') as f:
   reader = csv.reader(f, delimiter=',')
   for row in reader:
      print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
      #print(colmn[1])

