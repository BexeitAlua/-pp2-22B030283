import re
def match(txt):
    pattern='^[A-Z]{1}+[a-z]'
    if re.search(pattern,txt):
        return "Match"
    else:
            return "Not matched"

txt=input()
print(match(txt))