def getId(m,n):
    l=[]
    for x in range(len(m)):
        if 1 in m[x]:
            continue
        l.append(x)
    # print(l)
    if(len(l)==n):
        return(-1)
    for x in l:
        for y in range(len(m)):
            if(y==x):
                continue
            if(m[y][x]!=1):
                break
            continue
        return(x)
    return(-1)