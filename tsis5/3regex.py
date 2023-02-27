import re
def match(txt):
    pattern='\w*[a-z]{1}_[a-z]{1}\w*'
    if re.search(pattern,txt):
        return "Match"
    else:
            return "Not matched"

txt=input()
print(match(txt))