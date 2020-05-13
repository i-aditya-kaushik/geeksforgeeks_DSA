#include <iostream>
#include<unordered_map>
using namespace std;

int func(long long int a[], long long int b[],int n);

int func(long long int a[],long long int b[],int n){
    unordered_map <long long int,long long int> s,s2;
    for(int x=0;x<n;x++){
        s[a[x]]+=1;
    }
    for(int x=0;x<n;x++){
        s2[b[x]]+=1;
    }
    if(s==s2){
        return(1);
    }
    return(0);
}

int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
	    int size;
	    cin>>size;
	    long long int a[size],b[size];
	    for(int j=0;j<size;j++){
	        cin>>a[j];
	    }
	    for(int j=0;j<size;j++){
	        cin>>b[j];
	    }
	    cout<<func(a,b,size)<<endl;
	}
	return 0;
}