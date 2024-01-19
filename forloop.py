a="user@123#admin"
out=' '
for k in a:
    if not'0'<=k<='9':
        out+=k
print(out,end='\n')