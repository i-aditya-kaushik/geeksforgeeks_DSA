void DFS(int v, vector<bool> &vis, vector<int> g[]) {
    vis[v] = true;
    for(auto i = g[v].begin(); i != g[v].end(); i++) {
        if(!vis[*i]) {
            DFS(*i, vis, g);
        }
    }
    
}

int findMother(int V, vector<int> g[]) 
{ 
    vector<bool> vis(V, false);
    int v = 0;
    for(int i = 0; i < V; i++) {
        if(vis[i] == false) {
            DFS(i, vis, g);
            v = i;
        }
    }
    fill(vis.begin(), vis.end(), false);
    DFS(v, vis, g);
    for(int i = 0; i < V; i++) {
        if(vis[i] == false)
            return -1;
    }
    return v;
} 