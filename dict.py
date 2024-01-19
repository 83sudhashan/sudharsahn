user=input('enter user name')
password=int(input('enter password'))
db={'username':'password'}
if user==db['user'] and password==db['password']:
    print('matching')
else:
    print('not matching') 