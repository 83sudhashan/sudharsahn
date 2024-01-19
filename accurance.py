s=input('enter a string')
out={} 
for ch in s:
    if not(ch in out):
        out[ch]=1
    else:
        out[ch]+=1
print(out)