#include <iostream>
#include<unordered_set>
using namespace std;

int func(int arr1[],int n1,int arr2[],int n2);

int func(int arr1[],int n1,int arr2[],int n2){
    unordered_set<int> s1,s2,ans;
    for(int i=0;i<n1;i++){
        s1.insert(arr1[i]);
    }
    for(int i=0;i<n2;i++){
        s2.insert(arr2[i]);
    }
    if(s1.size()>s2.size()){
        for(auto x:s1){
            if(s2.find(x)!=s2.end()){
                ans.insert(x);
            }
        }
    }
    else{
        for(auto x:s2){
            if(s1.find(x)!=s1.end()){
                ans.insert(x);
            }
        }
    }
    return(ans.size());
}

int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
	    int n1,n2;
	    cin>>n1>>n2;
	    int a[n1],b[n2];
	    for(int i=0;i<n1;i++){
	        cin>>a[i];
	    }
	    for(int i=0;i<n2;i++){
	        cin>>b[i];
	    }
	    cout<<func(a,n1,b,n2)<<endl;
	}
	return 0;
}