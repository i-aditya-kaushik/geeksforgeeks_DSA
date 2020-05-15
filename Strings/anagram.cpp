bool isAnagram(string c, string d){
    
    unordered_map <int,int> s;
    for(int i=0;i<c.length();i++){
        s[c[i]]++;
    }
    for(int j=0;j<d.length();j++){
        s[d[j]]--;
        if(s[d[j]]==0){
            s.erase(d[j]);
        }
    }
    // for(auto it=s.begin();it!=s.end();it++){
    //     cout<<it->first<<" "<<it->second;
    //     cout<<endl;
    // }
    if(s.size()==0){
        return(1);
    }
    return(0);
}