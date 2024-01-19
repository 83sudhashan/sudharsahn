import random
n=random.randint(100,1000)
while True:
    a=int(input('enter a number'))
    if a==n:
        print('done')
    elif a<n:
        print('enter a greater number')
    else:
        print('enter smaller number')
