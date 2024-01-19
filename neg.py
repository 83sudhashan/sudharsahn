a=input('enter a string')
i=-1
count=0
v='AEIOUaeiou'
while i<len(a):
    if a[-i] in v:
        count+=1
    i+=1
print(count)