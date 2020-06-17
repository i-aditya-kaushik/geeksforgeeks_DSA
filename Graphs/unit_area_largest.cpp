void dfs(int a[SIZE][SIZE],int N, int M,int i,int j, int& count){
    if(i<0 || j<0 || i>=N || j>=M || a[i][j]==-1 || a[i][j]==0){
        return;
    }
    if(a[i][j]==1){
        count+=1;
        a[i][j]=-1;
        dfs(a,N,M,i,j+1,count);
        dfs(a,N,M,i,j-1,count);
        dfs(a,N,M,i+1,j,count);
        dfs(a,N,M,i-1,j,count);
        dfs(a,N,M,i+1,j+1,count);
        dfs(a,N,M,i-1,j-1,count);
        dfs(a,N,M,i+1,j-1,count);
        dfs(a,N,M,i-1,j+1,count);
    }
}

int findMaxArea(int N, int M, int a[SIZE][SIZE] )
{
    int res=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(a[i][j]==1){
                int count = 0;
                dfs(a,N,M,i,j,count);
                if(count>res) res=count;
            }
        }
    }
    return res;
}