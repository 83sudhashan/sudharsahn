import re
file=open(r"C:\Users\administrator.MCA\Desktop\text1.txt",'r')
data=file.read()
out=re.sub(' ','_',data)
print(out)
file=open(r"C:\Users\administrator.MCA\Desktop\text1.txt",'w')
file.write(out)
file.close()
