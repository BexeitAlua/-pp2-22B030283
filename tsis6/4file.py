import os
def numberoflines(file):
    with open(file) as f:
        for i ,l in enumerate(f):
            pass
    return i+1
print(numberoflines("input.txt"))