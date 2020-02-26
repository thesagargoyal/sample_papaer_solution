import math
a=list(map(int,input().split()))
for i in a:
    b=math.factorial(i)
    print(b,end=',')
