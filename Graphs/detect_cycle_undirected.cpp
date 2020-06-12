void DFS(int index,vector<int> adj[],int vis[],int V,int p,bool &val){//p -> parent of the index
  vis[index] = true;
  for(auto i=adj[index].begin();i!=adj[index].end();i++){
    if(vis[*i] == 0){
      DFS(*i,adj,vis,V,index,val);

      if(val)
        return;
    }
    else if(vis[*i] == 1 && p != *i){// if(u,v) -> both are visited && v is not the parent of u(index)
      val = true;
      return;
    }
  }
  return;
}


int isCyclic(vector<int> adj[],int V){
  int vis[V];
  fill(vis,vis+V,0);
  bool val = false;
  for(int i=0;i<V;i++)
    if(vis[i] == 0)
      DFS(i,adj,vis,V,-1,val);
  return (val)? 1 : 0;
}
