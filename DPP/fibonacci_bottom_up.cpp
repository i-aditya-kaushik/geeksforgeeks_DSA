long long findNthFibonacci(int number)
{
    vector<long long> dp(number,-1);
    if(number==1){
        return 1;
    }
    dp[0]=0;
    dp[1]=1;
    int i=2;
    //cout<<0<<" "<<1<<" ";
    while(i!=number){
        dp[i] = dp[i-1]+dp[i-2];
        //cout<<dp[i]<<" ";
        i+=1;
    }
    //cout<<endl;
    return dp[number-1]+dp[number-2];
}