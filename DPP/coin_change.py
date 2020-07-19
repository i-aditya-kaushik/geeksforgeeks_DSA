def minimumNumberOfCoins(ar,n,m):
    dp=[1000001]*(m+1)
    dp[0]=0
    for i in range(1,m+1):
        for j in range(n):
            if(ar[j]<=i):
                dp[i]=min(dp[i],dp[i-ar[j]]+1)
    if dp[m]==1000001:
        return -1
    return dp[m]