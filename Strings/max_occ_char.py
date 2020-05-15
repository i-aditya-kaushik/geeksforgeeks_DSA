def getMaxOccurringChar(str):
    s= {}
    max=0 
    c=[]
    for x in range(len(str)):
        try:
            s[str[x]]+=1
        except:
            s[str[x]]=1
        if(s[str[x]]==max):
            c.append(str[x])
        if(s[str[x]]>max):
            c=[]
            max = s[str[x]]
            c.append(str[x])
    c.sort()
    return(c[0])