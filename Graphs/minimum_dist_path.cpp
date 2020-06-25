#include<bits/stdc++.h>
using namespace std;
int main()
 {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int a[n][n];
	    int w[n][n];
	    for(int i=0;i<n;i++)
	    for(int j=0;j<n;j++)
	    {
	        cin>>a[i][j];
	        w[i][j]=INT_MAX;
	    }
	    w[0][0]=a[0][0];
	    queue<pair<int,int>> q;
	    q.push({0,0});
	    vector<vector<bool>> vis(n,vector<bool>(n,false));
	    vis[0][0]=true;
	    int i,j,x;
	    while(q.size()>0)
	    {
	        i=q.front().first;
	        j=q.front().second;
	        q.pop();
	        vis[i][j]=false;
	        if(i>0)
	        {
	            x=w[i-1][j];
	            w[i-1][j]=min(w[i-1][j],a[i-1][j]+w[i][j]);
	            if (x!=w[i-1][j] && !vis[i-1][j]) { q.push({i-1,j}); vis[i-1][j]=true;}
	        }
	        if(j>0)
	        {
	            x=w[i][j-1];
	            w[i][j-1]=min(w[i][j-1],a[i][j-1]+w[i][j]);
	            if (x!=w[i][j-1] && !vis[i][j-1]) { q.push({i,j-1}); vis[i][j-1]=true;}
	        }
	        if(i<n-1)
	        {
	            x=w[i+1][j];
	            w[i+1][j]=min(w[i+1][j],a[i+1][j]+w[i][j]);
	            if (x!=w[i+1][j] && !vis[i+1][j]) { q.push({i+1,j}); vis[i+1][j]=true;}
	        }
	        if(j<n-1)
	        {
	            x=w[i][j+1];
	            w[i][j+1]=min(w[i][j+1],a[i][j+1]+w[i][j]);
	            if (x!=w[i][j+1] && !vis[i][j+1]) { q.push({i,j+1}); vis[i][j+1]=true;}
	        }
	        
	    }
	    cout<<w[n-1][n-1]<<endl;
	}
	return 0;
}