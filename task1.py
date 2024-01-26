a=int(input())
out=''
for i in range(a):
    for j in range(a):
        if i==a//2 or j==a//2:
            print(' ',end=' ')
        else:
            print(' *',end=' ')
    print()