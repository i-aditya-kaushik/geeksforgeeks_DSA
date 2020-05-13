def printNonRepeated(arr,n):
    s = []
    for x in set(arr):
        s.append([x,arr.count(x)])
    s = sorted(s,key = lambda x:arr.index(x[0]))
    for x in s:
        if(x[1]==1):
            print(x[0],end=" ")