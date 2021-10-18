import csv
import pandas as pd

with open('score.csv', 'r') as csvfile:
    scorereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in scorereader:
        print(', '.join(row))




df=pd.read_csv('score.csv')
print(df)