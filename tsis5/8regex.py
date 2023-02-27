import re
txt=input()
pattern='[A-Z][^A-Z]*'
x=re.findall(pattern,txt)
print(x)