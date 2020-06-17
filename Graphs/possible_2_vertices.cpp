void dfs(int x,list<int> g[], int V, int s, int d,int &res){
    if(x==d){
        res+=1;
    }
    for(int y: g[x]){
        dfs(y,g,V,s,d,res);
    }
}

int countPaths(list<int> g[], int V, int s, int d) {
    int res=0;
    if(s==d){
        return(1);
    }
    for(int x: g[s]){
        dfs(x,g,V,s,d,res);
    }
    return(res);
}