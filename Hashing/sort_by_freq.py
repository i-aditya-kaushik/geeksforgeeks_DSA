def sortByFreq(a,n):
    a.sort()
    a = sorted(a,key = lambda x:a.count(x),reverse=True)
    for x in a:
        print(x,end=" ")
    print()