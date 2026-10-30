import pandas

df=pandas.read_csv("gapMinder.csv")
       
print("The mean of column 4 is:", df["lifeExp"].mean())

