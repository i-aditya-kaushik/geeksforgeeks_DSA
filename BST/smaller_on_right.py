import bisect

def func(arr,n):
    s=[]
    res=-1
    count=0
    for x in arr[::-1]:
        if x not in s:
            bisect.insort(s,x)
        count = s.index(x)
        res = max(count,res)
    print(res)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    func(arr,n)