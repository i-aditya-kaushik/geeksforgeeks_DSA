def func(n,a,b,c):
    if(n==0):
        return 0
    if(n<0):
        return -1
    res = max((func(n-a,a,b,c)),(func(n-b,a,b,c)),(func(n-c,a,b,c)))
    if(res==-1):
        return -1
    return(res+1)

print(func(5,2,1,5))