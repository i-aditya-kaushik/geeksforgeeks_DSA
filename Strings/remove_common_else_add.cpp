string concatenatedString(string s1, string s2) 
{ 
    vector<int> v1(256,0);
    vector<int> v2(256,0);
    string ans;
    for(int i=0;i<s1.length();i++){
        v1[s1[i]]=1;
    }
    for(int i=0;i<s2.length();i++){
        v2[s2[i]]=-1;
    }
    for(int i=0;i<s1.length();i++){
        if(v2[s1[i]]==-1){
            continue;
        }
        ans+=s1[i];
    }
    
    for(int i=0;i<s2.length();i++){
        if(v1[s2[i]]==1){
            continue;
        }
        ans+=s2[i];
    }
    return(ans);
    
}
