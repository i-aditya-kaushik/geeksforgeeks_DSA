
def func(l,l2):
    l.sort()
    l2.sort()
    if(l==l2):
        return(1)
    return(0)
    
 
for x in range(int(input())):
    n= int(input())
    l = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    print(func(l,l2))