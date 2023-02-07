def filter_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def only_prime(s):
    return [x for x in s if filter_prime(x)]



s = list(map(int,input().split()))

print(only_prime(s)) 

