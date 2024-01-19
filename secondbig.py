a=int(input('a   '))
b=int(input('b   '))
c=int(input('c    '))
if a>b and a>c:
    if b>c:
        print(b,'is gretest number')
    else:
        print(c,'is gerter')
elif b>c:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if a>b:
        print(a)
    else:
        print(b)
        