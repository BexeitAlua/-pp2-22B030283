def unique(l1):
    unique_list = []
    for x in l1:
        if x not in unique_list:
            unique_list.append(x)
  
    for x in unique_list:
        print (x)
 
 

l1 = list(map(int,input().split()))
unique(l1)
 
 
