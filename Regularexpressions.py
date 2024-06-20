'''import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\d")#select digit
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\D")#select except digit
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="hello world"
pattern=re.compile(r"\w")#select word character not space,space is not word character
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 03/06/12"
pattern=re.compile(r"\w+")#select only word
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\W")#select except word charcter,select only space
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\s")#select only spaces
res=re.finditer(pattern,data)
for row in res:
    print(row)'
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\S")#select except spaces
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="ef"
pattern=re.compile(r"sample\b")#check boundary
res=re.finditer(pattern,data)
for row in res:
    print(row)
    import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\B")#select text
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="ab cd ef gh"
pattern=re.compile(r"[a-b]")#select only lower case alphabets,A-Z=upper alphabets,0-9=numbers
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample"
pattern=re.compile(r"[^A-Z]")#select except what we give(2365){}=for length
res=re.finditer(pattern,data)
for row in res:
    print(row)
#url validation
import re
file=open("example.txt","r")
data=file.read()
pattern=re.compile(r"(http|https)://[a-z]")
res=re.finditer(pattern,data)
for row  in res:
    print(row)'''
#email id
'''import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\d")#select digit
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\D")#select except digit
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="hello world"
pattern=re.compile(r"\w")#select word character not space,space is not word character
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 03/06/12"
pattern=re.compile(r"\w+")#select only word
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\W")#select except word charcter,select only space
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\s")#select only spaces
res=re.finditer(pattern,data)
for row in res:
    print(row)'
import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\S")#select except spaces
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="ef"
pattern=re.compile(r"sample\b")#check boundary
res=re.finditer(pattern,data)
for row in res:
    print(row)
    import re
data="sample data 2365 20/03/12"
pattern=re.compile(r"\B")#select text
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="ab cd ef gh"
pattern=re.compile(r"[a-b]")#select only lower case alphabets,A-Z=upper alphabets,0-9=numbers
res=re.finditer(pattern,data)
for row in res:
    print(row)
import re
data="sample"
pattern=re.compile(r"[^A-Z]")#select except what we give(2365){}=for length
res=re.finditer(pattern,data)
for row in res:
    print(row)
#email validation
import re
file=open("example.txt","r")
data=file.read()
pattern=re.compile(r"[0-9]{2}[0-9]{2}[0-9]{1}[a-zA-Z]{1}[0-9]{2}[0-9A-Za-z]{2}")
res=re.finditer(pattern,data)
for row  in res:
    print(row)
import re
file=open("example.txt","r")
data=file.read()
pattern=re.compile(r"[6-9]{1}[0-9]{4}[0-9]{5}")
res=re.finditer(pattern,data)
for row  in res:
    print(row)'''
import re
file=open("example.txt","r")
data=file.read()
pattern=re.compile(r"(?=[A-Z]+(?=[a-z]+)(?=[0-9]+)(@#$%^(*)")
res=re.finditer(pattern,data)
for row  in res:
    print(row)

