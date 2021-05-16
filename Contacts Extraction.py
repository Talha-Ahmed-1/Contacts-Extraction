import re
import os
try:
    os.system("ren contacts.vcf contacts.txt")
except:
    os.popen("ren contacts.vcf contacts.txt")
a=open("contacts.txt","r")
b=a.read()
e=re.sub("[a-z]+","",b)
ee=re.sub("[A-Z]+","",e)
eee=re.sub(";","",ee)
eeee=re.sub(":","",eee)
eeeee=re.sub("\.","",eeee)
eeeeee=re.sub("-","",eeeee)
#print(eeeeee)
a.close()
ab=re.findall("[0-9].........[0-9]",eeeeee)
#print(ab)
open1=open("contactsExtracted.txt","w+")
for i in ab:
    b=open1.write(i+"\n")
open1.close()