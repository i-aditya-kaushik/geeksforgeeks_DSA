#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    long long int n,ele;
    cin>>n;
    vector<long long int> q;
    for(int i=0;i<n;i++){
        cin>>ele;
        q.push_back(ele);
    }
    sort(q.begin(),q.end());
    cout<<endl<<endl<<endl<<"--------------------------------------------------------------ANSWER------------------------------------"<<endl;
    for(auto it= q.begin();it!=q.end();it++){
        cout<<*it<<" ";
    }
    return 0;
}