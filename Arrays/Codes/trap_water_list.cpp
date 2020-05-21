#include <iostream>
#include<list>
#include <bits/stdc++.h> 

using namespace std;

long int func(int a[],int n){
    list<int> lmax,rmax;
    int max1 = INT_MIN;
    int max2 = INT_MIN;
    for(int i=0;i<n;i++){
        max1 = max(a[i],max1);
        lmax.push_back(max1);
    }
    for(int i=n-1;i>=0;i--){
        max2 = max(a[i],max2);
        rmax.push_front(max2);
    }
    long int res=0,i=0;
    auto it = lmax.begin();
    auto it2 = rmax.begin();
    while(it!=lmax.end()){
        res+= min(*it,*it2) - a[i];
        i+=1;
        it++;
        it2++;
    }
    return(res);
}

int main() {
	int n;
	cin>>n;
	for(int i = 0;i<n;i++){
	    int size;
	    cin>>size;
	    int a[size];
	    for(int j=0;j<size;j++){
	        cin>>a[j];
	    }
	    cout<<func(a,size)<<endl;
	}
	return 0;
}