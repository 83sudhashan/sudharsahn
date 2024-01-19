print('WELCOME TO MyBus')
print('enter \n 1--->Chennai \n 2--->Delhi \n3--->Mumbai\n 4--->Hyderabad')
print('enter ac\n nonac')
#a=input('enter persons name from banglore  ')
b=input('ENTER A OPTION (1,2,3,4) from there    ')
n=int(input('number of adult persons:- '))
m=int(input('enter of child persons :-  '))
if b=='1':
    if b=='ac':
        acd=n*350*10
        acc=m*350*5
        print('price for adult:-',acd)
        print('price for child:-',acc)
        print('total:-',acd+acc)
    else:
        nacd=n*350*5
        nacc=m*359*3
        print('price for adult:-',nacd)
        print('price for child:-',nacc)
        print('total:-',nacd+nacc)

elif b=='2':
    if b=='a/c':
        acd=2000*10*n
        print('price for adult:-',acd)
        acc=2000*5*m
        print('price for child:-',acc)
        print('total:-',acd+acc)
    else:
        nacd=n*2000*5
        nacc=m*200083
        print('price for adult:-',nacd)
        print('price for child:-',nacc)
        print('total:-',nacd+nacc)
elif b=='3':
    if b=='3':
        acd=n*800*10
        acc=m*800*5
        print('price for adult:-',acd)
        print('price for child:-',acc)
        print('total:-',acd+acc)
    else:
        nacd=n*800*5
        nacc=m*800*3
        print('price for adult:-',nacd)
        print('price for child :-',nacc)
        print('total:-',nacd+nacc)
elif b=='4':
    if b=='a/c':
        acd=n*500*10
        acc=m*50085
        print('price for adult:-',acd)
        print('price for child:-',acc)
        print('total:-',acd+acc)
    else:
        nacd=n*500*5 
        nacc=m*500*5
        print('price for adult:-',nacd)
        print('price for child :-',nacc)
        print('total:-',nacd+nacc)
else:
    print('enter a currect option')   

