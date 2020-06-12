vector <int> bfs(vector<int> g[], int N) {
    int i=0;
    vector<bool> check(N,false);
    vector<int> res;
    queue<int> s;
    s.push(0);
    check[0] = true;
    Label:
    while(s.size()!=0){
        for(int x:g[s.front()]){
            if(!check[x]){
                s.push(x);
                check[x] = true;
            }
        }
        res.push_back(s.front());
        s.pop();
    }
    // i=0;
    // for(bool x:check){
    //     // cout<<x<<" ";
    //     if(!x){
    //         s.push(i);
    //         check[i]=true;
    //         goto Label;
    //     }
    //     // cout<<i<<endl;
    //     i++;
    // }
    return(res);
}