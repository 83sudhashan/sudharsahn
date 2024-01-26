import re 
file=open('samp.txt','r')
data=file.read()
print(re.findall('[AEIOUaeiou]',data))