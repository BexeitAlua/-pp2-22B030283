def a(n):
    for i in range(n,-1,-1):
        yield i

print(*a(int(input())))