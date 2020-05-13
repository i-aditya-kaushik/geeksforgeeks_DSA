#code
def func(l,n):
    s={1,2,3}
    ans=[]
    for x in l:
        flag=1
        for num in str(x):
            if(int(num) in s):
                continue
            flag=0
            break
        if(flag):
            ans.append(x)
    if(len(ans)==0):
        print(-1)
        return
    for x in ans:
        print(x,end=" ")
    print()

for x in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    func(l,n)