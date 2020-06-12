void dfs(vector<int>g[],int s,bool visited[],vector<int>&v){
    visited[s]=1;
    v.push_back(s);
    for(int x:g[s]){
        if(visited[x]==0)
            dfs(g,x,visited,v);
    }
}
vector <int> dfs(vector<int> g[], int N)
{
    bool visited[N]={0};
    vector<int>v;
    dfs(g,0,visited,v);
    return v;
}