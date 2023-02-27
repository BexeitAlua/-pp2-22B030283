word = input()
word = ''.join(word.title() for word in word.split('_'))
print(word) 