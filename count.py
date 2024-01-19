a=input()
i=0
count=0
while i<=len(a):
    if a[i] in 'AEIOUaeiou':
        count+=1
    i+=1
print(count)