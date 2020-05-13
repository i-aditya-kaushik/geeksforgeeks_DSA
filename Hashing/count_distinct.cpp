#include <bits/stdc++.h>
using namespace std;

int countNonRepeated(int arr[], int n);

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n];
	    
	    for(int i=0;i<n;i++)
	    cin>>arr[i];
	    
	    cout<<countNonRepeated(arr,n)<<endl;
	    
	}
	return 0;
}

int countNonRepeated(int arr[], int n)
{
    unordered_map<int,int> s;
    int res = 0;
    for(int i=0;i<n;i++){
        s[arr[i]]+=1;
    }
    for(auto x:s){
        if(x.second==1){
            res+=1;
        }
    }
    return(res);
}