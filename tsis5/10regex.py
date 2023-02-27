import re

word = input()
word = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
print(word) 