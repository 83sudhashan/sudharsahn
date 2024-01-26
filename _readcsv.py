import csv
with open('samplee.csv','r',newline='') as file:
    record=csv.DictReader(file)
    for i in record:
        print(i)