def histogram(list):
        for x in range(0,len(list)):
                print('*' * list[x])
        return
li=[int(x) for x in input().split()]
histogram(li)