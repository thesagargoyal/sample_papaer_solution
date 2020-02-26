list=list(map(int,input().split()))
c=list[0]
list2=[]
for j in list:
    if c==j:
        pass
    if c!=j:
        list2.append(c)
    c=c+1
print(list2)
        
