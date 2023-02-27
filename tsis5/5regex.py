import re
def match(txt):
    pattern='^a\w*b$'
    if re.search(pattern,txt):
        return "Match"
    else:
            return "Not matched"

txt=input()
print(match(txt))