l=list(map(int,input().split(',')))
def spy_game(nums):
    flag = False
    flag_a = False
    for n in nums:
        if (n==0):
            flag = True
            continue
        if (n==0 and flag is True):
            flag_a = True
            continue
        if (n==7 and flag_a is True):
            return True
        else:
            return False

print(spy_game(l))
