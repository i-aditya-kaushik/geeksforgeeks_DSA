#include <iostream>
#include <vector>
using namespace std;

void dfs(vector<char> adj[],int p,int q,int i,int j){
    if(i<0 || j<0 || i>=p || j>=q || adj[i][j]=='Y' || adj[i][j]=='O'){
        return;
    }
    if(adj[i][j]=='X') adj[i][j]='Y';
    // for(int k=0;k<p;k++){
    //     for(int l=0;l<q;l++){
    //         cout<<adj[k][l]<<" ";
    //     }
    //     cout<<endl;
    // }
    // cout<<endl;
    dfs(adj,p,q,i+1,j);
    dfs(adj,p,q,i,j+1);
    dfs(adj,p,q,i-1,j);
    dfs(adj,p,q,i,j-1);
}

void func(vector<char> adj[],int p,int q,int& res){
    for(int i=0;i<p;i++){
        for(int j=0;j<q;j++){
            if(adj[i][j]=='X'){
                res+=1;
                // cout<<res<<endl;
                dfs(adj,p,q,i,j);
            }
        }
    }
}

int main() {
	int n;
	cin>>n;
	int res = 0;
	for(int i=0;i<n;i++){
	    int p,q;
	    char ch;
	    cin>>p>>q;
	    vector<char> adj[p];
	    for(int j=0;j<p;j++){
	        for(int k=0;k<q;k++){
	            cin>>ch;
	            adj[j].push_back(ch);
	        }
	    }
	    func(adj,p,q,res);
	    cout<<res<<endl;
	    res=0;
	}
	return 0;
}