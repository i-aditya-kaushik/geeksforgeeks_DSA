bool comp(pair<int,int> &a, pair<int,int> &b){
    return(a.second>b.second);
}

int print_N_mostFrequentNumber(int arr[],int n, int k) 
{ 
    map<int,int> s;
    for(int i=0;i<n;i++){
        s[arr[i]]++;
    }
    vector<pair<int,int>> q(s.begin(),s.end());
    sort(q.begin(),q.end(),comp);
    auto it = q.begin();
    int ans = 0;
    while(k--){
        ans+= it->second;
        it++;
    }
    return(ans);
} 