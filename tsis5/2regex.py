import re
def match(txt):
    pattern='^a{2}(b{3})$'
    if re.search(pattern,txt):
        return "Match"
    else:
            return "Not matched"

txt=input()
print(match(txt))