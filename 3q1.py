l=int(input())
list=[]
for i in range(l):
    a=int(input())
    list.append(i)
list2=[]
for i in list:
    if i==0:
        list2.append(i)
        list1.remove(i)
list3=list1 + list2
