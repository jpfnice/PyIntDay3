with open("gapMinder.csv") as fic:
    rowNumber=0
    total=0
    fic.readline()
    for line in fic:
        columns=line.split(",")
        rowNumber+=1
        total = total + float(columns[4])
        
print("The mean of column 4 is:", total/rowNumber)

