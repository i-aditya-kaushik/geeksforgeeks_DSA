def func(l1,m):
    for x in l1:
        if l1.count(x)>1:
            return(l1.index(x)+1)
    return(-1)

n = int(input())
for x in range(n):
    m = int(input())
    l1 = list(map(int,input().split()))
    print(func(l1,m))