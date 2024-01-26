import csv
#file=open('sample.csv','w')
with open('sample.csv','w') as file:
    data=[
        [1,'raju',45],
        [2,'rani',40],
        [3,'manthri',50],
        [4,'police',36],
        [5,'donga',40],
        ]
    record=csv.writer(file)
    record.writerow(['id','name','age'])
    record.writerows(data)