#include <bits/stdc++.h>
using namespace std;


int a[1000000];

void sortByFreq(int arr[],int n);

int main() {
	
	
	int t;
	cin >> t;
	
	
	while(t--){
	    
	    
	    int n;
	    cin >> n;
	    
	    for(int i = 0;i<n;i++){
	        cin >> a[i];
	    }
	    
	    sortByFreq(a,n);
	    cout << endl;
	}
	
	return 0;
}

void sortByFreq(int arr[],int n)
{
    multimap<int,int> ans;
    map <int,int> s;
    for(int i=0;i<n;i++){
        s[arr[i]]+=1;
    }
    for (auto it=s.begin(); it!=s.end(); it++) 
	{
		ans.insert(make_pair(it->second, it->first));
	}
	for (auto it = ans.rbegin(); it != ans.rend(); it++)
      for(int i=0;i<it->first;i++){
          cout<<it->second<<" ";
      }
}