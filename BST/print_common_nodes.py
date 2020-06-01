def printCommon(root1, root2):
    l = []
    lr = []
    rr = []
    r = []
    l.append(root1)
    r.append(root2)
    while(len(l)!=0):
        lr.append(l[0].data)
        if l[0].left:
            l.append(l[0].left)
        if l[0].right:
            l.append(l[0].right)
        l=l[1:]
    while(len(r)!=0):
        rr.append(r[0].data)
        if r[0].left:
            r.append(r[0].left)
        if r[0].right:
            r.append(r[0].right)
        r=r[1:]
    return(sorted(list(set(lr).intersection(rr))))