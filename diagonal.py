a=int(input())
for i in range(a):
    for j in range(a):
        if i==j or i==a-j-1:
            print(' ',end='')
        else:
            print('* ',end='')
    print()