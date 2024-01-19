a='good morning'
out=[]
for k in range(len(a)):
    if a[k] in 'aeiouAEIOU':
        out+=[k]
print(out)
