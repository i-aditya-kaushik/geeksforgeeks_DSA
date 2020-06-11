long long minCost(long long arr[], long long n) {
    long long ans = 0;
    long long temp = 0;
    priority_queue<long long,vector<long long>,greater<long long>> s;
    for(long long i=0;i<n;i++){
        s.push(arr[i]);
    }
    while(s.size()!=0){
        temp+= s.top();
        s.pop();
        if(s.size()==0){
            break;
        }
        temp+=s.top();
        s.pop();
        s.push(temp);
        ans+=temp;
        temp = 0;
    }
    return(ans);
}
