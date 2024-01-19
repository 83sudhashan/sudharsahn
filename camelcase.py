a='Hello_my_name_is_raju'
i=0
out=' '
temp=True
while i<len(a):
    if a[i]==' ':
        temp=True
    elif temp and 'a'<=a[i]<='z':
        out=''
        out+=chr(ord(a[i])-32)
    else:
        out+=a[i]
        temp=False
    i+=1
print(out)