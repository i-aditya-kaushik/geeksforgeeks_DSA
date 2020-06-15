bool check(int index,vector<int> adj[],int vis[]){ 
    vis[index] = 1;
    for(auto i = adj[index].begin(); i != adj[index].end(); i++){
        if(vis[*i] == 0){
            if(check(*i,adj,vis))
                return true;
        }
        else if(vis[*i] == 1)
            return true;
    }
    vis[index] = 2;
    return false;
}



bool isCyclic(int V, vector<int> adj[])
{
    int vis[V];
    fill(vis,vis+V,0);
    for(int i=0;i<V;i++){
        if(vis[i] == 0){
            if(check(i,adj,vis))
                return true;
        }
    }
    return false;
}