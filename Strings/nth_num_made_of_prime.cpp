#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

void func(int num);

void func(int num){
    vector<int> v = {2,3,5,7};
    vector<int> ans;
    while(num>=4){
        if(num%4-1>=0){
            ans.push_back(v[num%4-1]);
        }
        else{
            ans.push_back(v[3]);
            num-=1;
        }
        num/=4;
    }
    if(num-1>=0)
        ans.push_back(v[num-1]);
    reverse(ans.begin(),ans.end());
    for(int x:ans){
        cout<<x;
    }
    cout<<endl;
}

int main() {
	int n;
	cin>>n;
	int num;
	for(int i=0;i<n;i++){
	    cin>>num;
	    func(num);
	}
	return 0;
}