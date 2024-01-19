a=input('enter a string   ')
out=''
for k in a:
    if k not in out:
        out=out+k
print(out)
