import re
txt=input()
pattern='(\w)([A-Z])'
x=re.sub(pattern, r'\1 \2',txt)
print(x)