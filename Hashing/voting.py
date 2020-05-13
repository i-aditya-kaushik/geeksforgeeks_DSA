import math
#Complete this function
def winner(arr,n):
    s={}
    ans=[]
    max = -math.inf
    for x in arr:
        try:
            s[x]+=1
        except:
            s[x]=1
        if(s[x]>max):
            max = s[x]
    # s= sorted(key= lambda x:x[0])
    for x in s:
        if(s[x]==max):
            ans.append(x)
    ans.sort()
    print(str(ans[0])+" "+str(s[ans[0]]),end=" ")