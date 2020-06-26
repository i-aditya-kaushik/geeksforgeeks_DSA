int spanningTree(int V, int E, vector<vector<int>> &graph) {
    priority_queue <pair<int,int> ,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    vector <bool> vis(V,false);
    vis[0]=true;
    int count=1;
    for(int i=1;i<V;i++)
    {
        if(graph[0][i]!=INT_MAX) pq.push({graph[0][i],i});

    }
    int w,i,j;
    int res=0;
    while(pq.size() && count<V)
    {
        w=pq.top().first;
        
        j=pq.top().second;
        pq.pop();
        
        if(vis[j]==true) continue;
        count++;
        res+=w;
        vis[j]=true;
         
        for(int k=0;k<V;k++)
        {
            if(!vis[k] && graph[j][k]!=INT_MAX) pq.push({graph[j][k],k});
        }
    }
    
    return res;
}