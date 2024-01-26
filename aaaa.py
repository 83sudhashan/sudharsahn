a=int(input())
out=''
for i in range(a):
    for j in range(a):
        if i==j or i==a-j-1:
            out+=' '
        else:
            out+='* '
    out+='\n'
name=input('enter a number:-  ')
with open(f'{name}.txt','w') as file:
    file.write(out)


