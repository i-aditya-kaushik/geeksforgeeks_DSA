def isAnagram(a,b):
    dict = {}
    for x in a:
        try:
            dict[x]+=1
        except:
            dict[x]=1
    for x in set(b):
        try:
            dict[x]-=b.count(x)
            if(dict[x]==0):
                del dict[x]
        except:
            return(0)
    if(len(dict)==0):
        return(1)
