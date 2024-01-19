a=input('enter student name')
b=int(input('enter marks'))
if b>90 and b<=100:
    print('A+ grade')
elif b>80 and b<90:
    print('A grade')
elif b>70 and b<80:
    print('B+ grade')
elif b>60 and b<70:
    print('B grade')
elif b>50 and b<60:
    print('C grade')
elif b>=35 and b<50:
    print('pass')
elif b>35 and b<=0:
    print('fail')
else:
    print('invalid')