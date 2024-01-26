import re
#print(re.findall('[0-9]','abcdef212gh45'))#0-9 only
#print(re.findall('[^0-9]','abcdef2123425#$%^gh45'))# non digit character
#print(re.findall('.','eduioggy&^78978'))# every character in string
#print(re.findall('[0-9]+','s5444fuf44g4hw5q44#44$'))
#print(re.findall('[0-9]*','s54fuf44g4hw5q67@44#44$'))
#print(re.findall('[0-9]?','s544uf44g4hw5q57@44#44$'))
#print(re.findall('[0-9]{2}','s544uf44g4hw5q57@44#44$'))
#print(re.findall('[0-9]{2}','s544uf44g4hw5q57@44#44$'))
#print(re.findall('\d{2}','s544uf44g4hw5q57@44#44$'))
#print(re.findall('[0-9]{1,3}','s544uf44g4hw5q57@44#44$'))
#print(re.findall('[6-9][0-9]{9}','9877546255624dghshg65673676767dhghjfg2435666'))
#print(re.findall('[A-Z]{5}[0-9]{4}[A-Z]','ASADFGD87556378NBFU9876878'))
print(re.findall('AP[ ]?[0-3][1-9][ ]?[a-zA-Z][ ]?[0-9]{4}','AP01A8765PA 09 H 9876'))
print(re.findall('\+91\-[6-9][0-9]{9}','+91-9877546255624dghshg65673676767dhghjfg2435666'))

