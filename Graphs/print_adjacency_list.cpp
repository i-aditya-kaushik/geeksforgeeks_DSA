void printGraph(vector<int> adj[], int V)
{
    for(int i=0;i<V;i++){
        cout<<i;
        for(int x:adj[i]){
            cout<<"-> "<<x;
        }
        cout<<endl;
    }
}