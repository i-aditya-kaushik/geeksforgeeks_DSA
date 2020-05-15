#include<bits/stdc++.h>
using namespace std;

bool isIsogram(string s);

int main()
 {
    int t;
    cin>>t;
    while(t--)
    {
        
        string s;
        cin>>s;
        
        cout<<isIsogram(s)<<endl;
        
    }
	return 0;
}
bool isIsogram(string s)
{
    vector<int> vec(256,0);
    for(int i=0;i<s.length();i++){
        vec[s[i]]+=1;
        if(vec[s[i]]>=2){
            return(0);
        }
    }
    return(1);
}