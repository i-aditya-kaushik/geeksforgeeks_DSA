#include<bits/stdc++.h>

using namespace std;

bool search(string, string, int);
bool search(string pat, string txt, int q) 
{ 
    if(pat.length()>txt.length())
        return(0);
    int m=0;
    string check = txt.substr(m,pat.length());
    cout<<check<<endl;
    if(check==pat){
        return(1);
    }
    for(int i=pat.length();i<txt.length();i++){
        m++;
        check = txt.substr(m,pat.length());
        cout<<check<<endl;
        if(check==pat){
            return(1);
        }
    }
    return(0);
} 
int main() 
{ 
    int t;
    cin >> t;
    
    while(t--){
	    string s, p;
	    cin >> s >> p;
	    int q = 101; // A prime number 
	    if(search(p, s, q)) cout << "Yes" << endl;
	    else cout << "No" << endl;
    }
	return 0; 
} 