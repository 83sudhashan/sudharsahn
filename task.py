import re 
file=open('samp.txt','r')
data=file.read()
a=re.findall('[AEIOUaeiou]',data)
print(len(a))