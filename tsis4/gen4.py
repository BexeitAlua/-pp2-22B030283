import math
def squares(a, b):
    for i in range(a,b + 1):
        x=math.sqrt(i)
        if x % 1 == 0:
            yield i
a,b=map(int,input().split())
print(*squares(a, b))