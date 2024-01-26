import csv
with open('sample.csv','a',newline='') as file:
    record=csv.writer(file)
    record.writerow([4,'hsihu'])