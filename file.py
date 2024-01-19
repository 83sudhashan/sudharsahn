a=input()
i=0
b=a[-1:-len(a):-1]
while i<len(a):
    if b[i] not in b[i+1:]:
        print(b[i])
        break
    i+=1
