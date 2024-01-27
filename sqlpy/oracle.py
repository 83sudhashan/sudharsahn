import csv
import cx_Oracle
res=cx_Oracle.Connection('system/manager@mother')
cur=res.cursor()

def  createtable():
    query='''create table sudharshan45mca(
    id number(2) primary key,
    name varchar(40)
    )
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    #query="insert into sudharshan45mca(id,name) value())",record
    #query='''insert into sudharshan45mca(id,name) values(1,'neeraj kumar')'''
    #query='''insert into sudharshan45mca(id,name) values(2,'ummaleti')'''
    cur.execute("insert into sudharshan45mca(id,name) values(:id,:name)",record)
    res.commit()
# insertrecord(0,'raghu')
def read_records():
    query='select * from sudharshan45mca'
    cur.execute(query)
    records=cur.fetchall()
    with open('sqll.csv','w',newline='') as csvfile: 
        data=csv.writer(csvfile)
        data.writerow(['id','name']) 
        for row in records:
            data.writerow(row)
#read_records() 
def insertdata():
    with open('record.csv','r',newline='') as file:
        record=csv.DictReader(file)
        for i in  record:
            cur.execute("insert into sudharshan45mca(id,name) values(:id,:name)",i)
            res.commit()
insertdata() 
  
def update_record(sid,name):
    record={'id':str(sid),'name':name}
    # "update sudharshan45mca set name='scientist' where id=1",record
    cur.execute("update sudharshan45mca set name=(:name) where id=(:id)",record)
    res.commit()
# update_record(1,'edhar')   
def delete_record(sid):
    record={'id':str(sid)}
     #"update sudharshan45mca set name='scientist' where id=1",record
    cur.execute("delete from sudharshan45mca where id=(:id)",record)
    res.commit()
# delete_record(1,'suredhar')   
def fetch_record(sid):
    record={'id':str(sid)}
    cur.execute("select * from sudharshan45mca where id=(:id)",record)
    record=cur.fetchall()
    for i in record:
         print(i)
# fetch_record(3)   
def truncate():
    query='truncate table sudharshan45mca'
    cur.execute(query)


  


