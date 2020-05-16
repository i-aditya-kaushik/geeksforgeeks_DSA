#include<algorithm>
#include<string>
string caseSort(string str, int n){
    
    vector<int> lc,uc;
    string ans="";
    for(int i=0;i<str.length();i++){
        if(str[i]>='a' && str[i]<='z'){
            lc.push_back(str[i]);
        }
        else{
            uc.push_back(str[i]);
        }
    }
    sort(lc.begin(),lc.end());
    sort(uc.begin(),uc.end());
    for(int i=0;i<str.length();i++){
        if(str[i]>='a' && str[i]<='z'){
            char c = lc[0];
            ans+= c;
            lc.erase(lc.begin());
        }
        else{
            char c = uc.front();
            ans+= c;
            uc.erase(uc.begin());
        }
    }
    return(ans);
}