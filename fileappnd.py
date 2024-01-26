file=open('samp.txt','a')
data='\nwijfihiohisj'
file.write(data)
file.close()

file=open('samp.txt','r')
data=file.read()
print(data)
file.close()