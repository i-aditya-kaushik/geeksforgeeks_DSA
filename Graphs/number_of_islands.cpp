void dfs(vector<int>a[],int n,int m,int i,int j)
{
    if(i<0||j<0||i>=n||j>=m||a[i][j]==0||a[i][j]==-1)
        return;
    a[i][j]=-1;
    dfs(a,n,m,i+1,j);
    dfs(a,n,m,i-1,j);
    dfs(a,n,m,i,j+1);
    dfs(a,n,m,i,j-1);
    dfs(a,n,m,i-1,j-1);
    dfs(a,n,m,i-1,j+1);
    dfs(a,n,m,i+1,j-1);
    dfs(a,n,m,i+1,j+1);
}
int findIslands(vector<int> a[], int n, int m) 
{
  int i,j,ans=0;
  for(i=0;i<n;i++){
      for(j=0;j<m;j++)
      {
          if(a[i][j]==1)
          {
              ans++;
              dfs(a,n,m,i,j);
          }
      }
  }
 return ans;
}