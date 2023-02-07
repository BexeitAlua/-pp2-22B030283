l=list(map(int,input().split(',')))
def has_33(nums):
    for i, x in enumerate(nums):
        if x == 3:     
            if i == len(nums) - 1: return False
            elif nums[i + 1] == 3: return True

print(has_33(l))