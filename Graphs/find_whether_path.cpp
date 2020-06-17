#include <iostream>
#include<vector>
using namespace std;

void dfs(vector<int> adj[], int n, int i, int j,int& flag){
    if(i<0 || j<0 || i>=n || j>=n || adj[i][j]==0){
        return;
    }
    if(adj[i][j]==2){
        flag = 1;
        return;
    }
    
    if(adj[i][j]==3){
        adj[i][j]=-1;
        dfs(adj,n,i+1,j,flag);
        dfs(adj,n,i,j+1,flag);
        dfs(adj,n,i-1,j,flag);
        dfs(adj,n,i,j-1,flag);
    }
}

bool func(vector<int> adj[],int n){
    int flag=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(adj[i][j]==1){
                dfs(adj,n,i+1,j,flag);
                dfs(adj,n,i,j+1,flag);
                dfs(adj,n,i-1,j,flag);
                dfs(adj,n,i,j-1,flag);
            }
        }
    }
    return(flag==1);
}

int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
	    int size;
	    cin>>size;
	    vector<int> adj[size];
	    for(int j=0;j<size;j++){
	       for(int k=0;k<size;k++){
	           int ele;
	           cin>>ele;
	           adj[j].push_back(ele);
	       }
	    }
	    cout<<func(adj,size)<<endl;
	}
	return 0;
}