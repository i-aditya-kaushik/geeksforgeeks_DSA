#include <bits/stdc++.h>
using namespace std;

int findLongestConseqSubseq(int arr[], int n);
 
// Driver program
int main()
{
 int  t,n,i,a[100001];
 cin>>t;
 while(t--)
 {
  cin>>n;
  for(i=0;i<n;i++)
  cin>>a[i];
  cout<<findLongestConseqSubseq(a, n)<<endl;
 }
      
    return 0;
}

int findLongestConseqSubseq(int arr[], int n)
{
  map<int,int> s;
  int answer=0;
  for(int i=0;i<n;i++){
      s[arr[i]]+=1;
  }
  int res =0;
  for(auto it=s.begin();it!=s.end();it++){
      if(s.find(it->first+1)!=s.end()){
          res+=1;
      }
      else{
          answer= max(res,answer);
          res=0;
      }
  }
  return(answer+1);
}