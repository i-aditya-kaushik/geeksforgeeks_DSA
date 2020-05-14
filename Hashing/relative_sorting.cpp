#include <iostream>
#include<unordered_map>
#include<vector>
#include<algorithm>
using namespace std

void func(int arr1[],int n,int arr2[],int n2);

void func(int a[],int n,int b[],int m){
    unordered_map<int,int> s;
    vector<int> c;
    for(int i=0;i<m;i++){
        s[b[i]]=0;
    }
    for(int i=n-1;i>=0;i--){
        if(s.find(a[i])!=s.end())
            s[a[i]]+=1;
        else{
            c.push_back(a[i])
        }
    }
    for(auto it= s.begin();it!= s.end() ; it++){
        for(int i=0;i< (it->second);i++){
            cout<< (it->first) <<" ";
        }
    }
    sort(c.begin(), c.end()); 
    for(int x:c){
        cout<<x<<" ";
    }
    cout<<endl;
}

int main() {
	int n,n2,m;
	cin>>m;
	for(int j=0;j<m;j++){
	    cin>>n;
    	cin>>n2;
    	int arr[n],arr2[n2];
    	for(int i=0;i<n;i++){
    	    cin>>arr[i];
    	}
    	for(int i=0;i<n2;i++){
    	    cin>>arr2[i];
    	}
    	func(arr,n,arr2,n2);
	}
	return 0;
}