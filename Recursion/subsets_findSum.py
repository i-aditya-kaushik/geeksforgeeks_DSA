q=[0]

def func(ch,st,n,c):
    if(n == len(st)):
        if(ch==c):
            q.append(1)
            return
        return
    
    func(ch+int(st[n]),st,n+1,c)
    func(ch,st,n+1,c)

st = list(map(int,input().split()))
check = int(input())
(func(0,st,0,check))
print((max(q)))
#Time COmplexity: Theta(n^2)