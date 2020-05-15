def reverseWords(s):
    ans=""
    l=[]
    for x in s:
        ans+=x
        if(x=='.'):
            l.append(ans)
            ans=""
            continue
    l.append(ans)
    answer=""
    for x in range(len(l)-1,-1,-1):
        answer+=l[x]
        if(x==len(l)-1):
            answer+='.'
    print(answer[0:-1],end="")