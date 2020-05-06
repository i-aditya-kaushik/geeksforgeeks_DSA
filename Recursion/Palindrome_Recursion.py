def func(s,m,n):
    if(m==len(s)//2-1 and n==len(s)//2+1 and s[m]==s[n]):
        return(1)
    if(s[m]!=s[n]):
        return 0
    func(s,m+1,n-1)

s = input()
print(func(s,0,len(s)-1))