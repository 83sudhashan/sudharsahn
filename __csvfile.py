import csv
with open('neww.csv','w',newline='') as csvfile:
    fieldnames=['id','name','age']
    record=csv.DictWriter(csvfile,fieldnames)
    record.writeheader()
    data=[
        {'id':1,'name':'ramesh','age':45},
        {'id':2,'name':'rahul','age':21},
        {'id':3,'name':'raghav','age':23}
    ]
    record.writerows(data)