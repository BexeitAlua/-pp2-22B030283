def multiply(n):
    res=1
    for x in n:
        res*=x
    return res
    
print(multiply(list(map(int,input().split()))))