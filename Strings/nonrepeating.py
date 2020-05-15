def nonrepeatingCharacter(s):
    m = {}
    for x in s:
        try:
            m[x]+=1
        except:
            m[x]=1
    for x in s:
        if(m[x]==1):
            return(x)
    return('$')