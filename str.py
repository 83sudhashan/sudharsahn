st=input('enter a string:- ')
out=[]
i=0
start=0
while i<len(st):
    if st[i]=='':
        out==[st[start:i]]
        start=i+1
    i+=1
if start<len(st):
    out+=[st[start:]]
print(out)