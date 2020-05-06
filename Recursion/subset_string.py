def func(ch,st,n):
    if(n == len(st)):
        print(ch)
        return
    
    func(ch+st[n],st,n+1)
    func(ch,st,n+1)


st = input()

print(func("",st,0))
