#include <iostream>
#include<stdio.h>
#include <unordered_map>
using namespace std;

int fun(int arr[],int size);

int fun(int a[],int n){
    int sum=0,count=0;
    unordered_map<int,int>s;
    s[0]++;
    for(int i=0;i<n;i++){
        sum+=a[i];
        if(s.find(sum)!=s.end()){
                count+=s[sum];
            }
        s[sum]++;
    }
    return count;
}


int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
	    int size;
	    cin>>size;
	    int arr[size];
	    for(int j = 0; j<size;j++){
	        cin>>arr[j];
	    }
	    cout<<fun(arr,size);
	    cout<<endl;
	}
	return 0;
}