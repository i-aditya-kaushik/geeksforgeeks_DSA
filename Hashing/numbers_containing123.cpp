#include <iostream>
#include<map>
#include<unordered_set>
using namespace std;

int func(int a[],int n);

int func(int a[],int n){
    unordered_set<int> s;
    s.insert(1);
    s.insert(2);
    s.insert(3);
    map<int,int> s2;
    for(int i=0;i<n;i++){
        int flag=0;
        int temp = a[i];
        while(temp!=0){
            if(s.find(temp%10)==s.end()){
                flag=0;
                temp=temp/10;
                break;
            }
            temp=temp/10;
            flag = 1;
        }
        if(flag==1){
            s2[a[i]]+=1;
        }
    }
    if(s2.size()==0){
        cout<<-1<<endl;
        return 0;
    }
    for(auto it=s2.begin();it!=s2.end();it++){
        for(int i=0;i<it->second;i++)
            cout<<it->first<<" ";
    }
    cout<<endl;
    return 0;
}

int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
	    int size;
	    cin>>size;
	    int a[size];
	    for(int j=0;j<size;j++){
	        cin>>a[j];
	    }
	    func(a,size);
	}
	return 0;
}