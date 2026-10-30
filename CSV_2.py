import csv

with open("gapMinder.csv") as fic:
    rowNumber=0
    total=0
    fic.readline()
    reader=csv.reader(fic)
    for line in reader:
        rowNumber+=1
        total = total + float(line[4])
        
print("The mean of column 4 is:", total/rowNumber)

