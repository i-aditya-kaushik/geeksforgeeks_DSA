#include <iostream>
#include<map>
#include<unordered_set>
using namespace std;

int func(int a[],int n);

int func(int a[],int n){
    map <int,int> s;
    unordered_set<int> s1;
    for(int x=0;x<n;x++){
        s[a[x]]+=1;
    }
    for(auto it=s.begin();it!=s.end();it++){
        if(s.find(-1*(it->first))!=s.end() && it->first!=0){
            s1.insert(abs(it->first));
        }
    }
    for(int x:s1){
    cout<< abs(x)<<" "<<-1*abs(x)<<" ";}
    if(s1.size()==0){
        cout<<0;
    }
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
	    cout<<endl;
	}
	return 0;
}